"""Workarounds for invenio/oarepo issues.

These should be removed once the issues are fixed. This file is called as a part of
config loading, so reasonably early in the process.
"""

# workaround: loading vocabularies
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, cast

import tqdm
from flask import current_app
from invenio_access.permissions import (
    system_identity,
)
from invenio_base.signals import app_loaded
from invenio_db import db
from invenio_db.uow import UnitOfWork
from invenio_pidstore.errors import PersistentIdentifierError
from invenio_rdm_records.fixtures.vocabularies import (
    VocabulariesFixture,
    VocabularyEntry,
)
from invenio_records_resources.proxies import current_service_registry
from invenio_records_resources.services.records import RecordService
from invenio_records_resources.services.uow import RecordCommitOp
from invenio_vocabularies.records.api import Vocabulary
from sqlalchemy.exc import NoResultFound


def create_vocabulary_record(service: RecordService, data: dict, uow: UnitOfWork):
    """Create a vocabulary record using the service. Unlike RDM, this call accepts a uow.

    We do not want to put this to our RDM patches because Invenio is planning a complete rewrite
    of the fixtures.
    """
    try:
        if "type" in data:
            # We only check non-datastream vocabularies for updates
            pid = (data["type"], data["id"])
            try:
                # If the entry hasn't been added, this will fail
                record = Vocabulary.pid.resolve(pid)
                record = service.update(system_identity, pid, data=data, uow=uow)
            except PersistentIdentifierError:
                record = service.create(system_identity, data, uow=uow)
            return record._record.id
        if "id" in data:
            id = data["id"]
            try:
                # If the entry hasn't been added, this will fail
                record = service.read(system_identity, id)
                record = service.update(system_identity, id, data=data, uow=uow)
            except PersistentIdentifierError, NoResultFound:
                record = service.create(system_identity, data, uow=uow)
        else:
            record = service.create(system_identity, data, uow=uow)
        return record._record.id
    except Exception as e:
        import traceback

        traceback.print_exc()
        current_app.logger.error(f"failed to load vocabulary entry: {type(e).__name__} {e}:\n{data}")


def remove_record_index_operation(uow: UnitOfWork):
    """Remove all RecordCommitOp operations from the unit of work as we will be calling bulk index on these."""
    uow._operations = [x for x in uow._operations if not isinstance(x, RecordCommitOp)]


def bulk_index_records(service: RecordService, record_ids: list[str]):
    """Bulk index the records."""
    service.indexer.bulk_index(record_ids)


BATCH_SIZE = 500


def load_vocabulary_entry(self, identity, ignore=None, delay=False):
    """Template method design pattern for loading entries."""
    ignore = ignore or set()
    self.pre_load(identity, ignore=ignore)
    service = cast("RecordService", current_service_registry.get(self.service_str))
    record_ids: list[str] = []
    with UnitOfWork() as uow:
        for idx, data in enumerate(self.iterate(ignore=ignore), start=1):
            record_uuid = create_vocabulary_record(service, data, uow)
            if record_uuid is not None:
                record_ids.append(record_uuid)

            if idx % BATCH_SIZE == 0:
                # flush to the dabase and evict all ORM objects from the session to prevent the identity
                # map from accumulating references across the entire run.
                db.session.flush()
                db.session.expunge_all()

        # Remove the per-record index operation from the UoW to avoid indexing each record individually.
        remove_record_index_operation(uow)

        # And bulk index the records.
        bulk_index_records(service, record_ids)

        # commit the UoW to persist the changes to the database. This works because
        # this step does not depend on RecordCommitOp to be present in the uow -
        # the db.session.add(...) has already been called when the RecordCommitOp
        # was registered with the uow.
        uow.commit()
    return self.loaded()


VocabularyEntry.load = load_vocabulary_entry


# I/O-bound threads (DB writes) benefit from more parallelism than CPU count alone;
# use 2× logical CPUs, with a floor of 2 and a ceiling of 32.
MAX_VOCABULARIES_PARALLEL_WORKERS = max(2, min(32, (os.cpu_count() or 1) * 2))


def parallel_load_vocabulary_entries(self, ignore=None):
    """Load the whole fixture.

    ignore: iterable of ids to ignore

    For subjects (or any vocabulary with a dict of data-file), the id
    that counts is ``<vocabulary id>.<dict key>``.

    Returns all vocabulary ids loaded so far.
    """
    ids = set(ignore) if ignore else set()

    # Capture the app reference in the main thread; each worker must push its
    # own application context because Flask contexts are thread-local.
    app = current_app._get_current_object()

    def _load_in_ctx(entry):
        with app.app_context():
            return entry.load(self._identity, ignore=ids, delay=False)

    loaded_data = list(self.read())
    thread_count = min(len(loaded_data), MAX_VOCABULARIES_PARALLEL_WORKERS)
    current_app.logger.info(f"Using {thread_count} workers to load vocabularies")
    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        tasks = [executor.submit(_load_in_ctx, entry) for id_, entry in loaded_data]
        with tqdm.tqdm(total=len(tasks), desc="Loading vocabularies") as progress:
            for task in as_completed(tasks):
                task_ids = task.result()
                ids.update(task_ids)
                progress.update(1)

    return ids


VocabulariesFixture.load = parallel_load_vocabulary_entries


@app_loaded.connect
def application_loaded(*_args: Any, **_kwargs: Any) -> None:
    """Improve gc performance.

    This tweak is taken from:
    https://mkennedy.codes/posts/python-gc-settings-change-this-and-make-your-app-go-20pc-faster/
    """
    import gc

    # freeze the actual objects to prevent GC to collect them,
    # speeding up the garbage collection process
    gc.collect()
    gc.freeze()

    # do not call gc so often
    _, gen1, gen2 = gc.get_threshold()
    gc.set_threshold(50_000, 2 * gen1, 2 * gen2)
