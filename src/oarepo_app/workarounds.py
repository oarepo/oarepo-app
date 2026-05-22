"""Workarounds for invenio/oarepo issues.

These should be removed once the issues are fixed. This file is called as a part of
config loading, so reasonably early in the process.
"""

# workaround: loading vocabularies
from invenio_rdm_records.fixtures.vocabularies import PrioritizedVocabulariesFixtures

current_vocabulary_fixtures_init = PrioritizedVocabulariesFixtures.__init__


def new_vocabulary_fixtures_init(self, *args, **kwargs):
    """Workaround: loading vocabularies.

    Normally vocabularies are loaded in a background task in parallel in many threads,
    but this causes issues with the hierarchical vocabularies. It might happen that a
    parent vocabulary item is not finalized when children items are created and this
    causes the child item not to be created.

    As a workaround before we find a way of how to do it safely, we serialize the request
    by indexing in process, not in a background task.
    """
    current_vocabulary_fixtures_init(self, *args, **kwargs)
    # import vocabularies immedially, not in a background task
    self._delay = False


PrioritizedVocabulariesFixtures.__init__ = new_vocabulary_fixtures_init
