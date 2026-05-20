import copy

import pytest
from invenio_records_resources.services.errors import PermissionDeniedError
from invenio_requests.proxies import current_requests_service

from tests.model import datasets_model
from tests.utils import restrict_workflows


def test_submit_record_default_workflow(
    app, communities, users, location, vocabularies, simple_record
):
    with restrict_workflows("default-community", individual="noone"):
        owner, curator, submitter, member = users[:4]
        community = communities["default-community"]

        with pytest.raises(PermissionDeniedError):
            datasets_model.proxies.current_service.create(
                member.identity, data=simple_record
            )

        record = datasets_model.proxies.current_service.create(
            submitter.identity, data=simple_record
        )

        print("Community ID:", community.id)
        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        with pytest.raises(PermissionDeniedError):
            datasets_model.proxies.current_service.review.create(
                member.identity,
                data=copy.deepcopy(submission_request_data),
                record=record._record,
            )

        review_request = datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record._record,
        )

        with pytest.raises(PermissionDeniedError):
            current_requests_service.execute_action(
                member.identity,
                review_request.id,
                "submit",
            )

        current_requests_service.execute_action(
            submitter.identity,
            review_request.id,
            "submit",
        )

        with pytest.raises(PermissionDeniedError):
            current_requests_service.execute_action(
                member.identity,
                review_request.id,
                "accept",
            )

        current_requests_service.execute_action(
            curator.identity,
            review_request.id,
            "accept",
        )
