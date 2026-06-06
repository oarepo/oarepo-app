#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-app (see https://github.com/oarepo/oarepo-app).
#
# oarepo-app is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
from __future__ import annotations

import copy

import pytest
from invenio_accounts.models import User
from invenio_records_resources.services.errors import PermissionDeniedError
from invenio_requests.proxies import current_requests_service
from oarepo_runtime.typing import record_from_result
from oarepo_workflows.proxies import current_oarepo_workflows
from pytest_invenio.user import UserFixtureBase

from tests.model import datasets_model
from tests.utils import restrict_workflows


def _create_non_member_user(app, db, email="non_member@community_test.example.com") -> UserFixtureBase:
    """Create an ad-hoc authenticated user who is not a member of any community."""
    existing = db.session.query(User).filter_by(email=email).first()
    if existing:
        db.session.delete(existing)
        db.session.commit()
    u = UserFixtureBase(email=email)
    u.create(app, db)
    return u


def test_submit_record_default_workflow(app, communities, users, location, vocabularies, simple_record):
    with restrict_workflows("default-community", individual="noone"):
        _owner, curator, submitter, member = users[:4]
        community = communities["default-community"]

        with pytest.raises(PermissionDeniedError):
            datasets_model.proxies.current_service.create(member.identity, data=simple_record)

        record = datasets_model.proxies.current_service.create(submitter.identity, data=simple_record)

        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        with pytest.raises(PermissionDeniedError):
            datasets_model.proxies.current_service.review.create(
                member.identity,
                data=copy.deepcopy(submission_request_data),
                record=record_from_result(record),
            )
        review_request = datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record_from_result(record),
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


# --- Group A: Draft creation ---


def test_member_cannot_create_by_default(app, communities, users, location, vocabularies, simple_record):
    """Assert that a community member without submitter role cannot create a draft in the default workflow."""
    with restrict_workflows("default-community", individual="noone"):
        _, _, _, member = users[:4]

        with pytest.raises(PermissionDeniedError):
            datasets_model.proxies.current_service.create(member.identity, data=copy.deepcopy(simple_record))


def test_member_can_create_when_community_role_allows(
    app, db, communities, users, location, vocabularies, simple_record
):
    """Assert that a member CAN create a draft when 'member' is listed in draft_creation_community_roles."""
    with restrict_workflows("community-member-creates", individual="noone"):
        _, _, _, member = users[:4]

        record = datasets_model.proxies.current_service.create(member.identity, data=copy.deepcopy(simple_record))
        assert record is not None

        non_member = _create_non_member_user(app, db)
        with pytest.raises(PermissionDeniedError):
            datasets_model.proxies.current_service.create(non_member.identity, data=copy.deepcopy(simple_record))


def test_any_authenticated_user_can_create_in_open_community(
    app, db, communities, users, location, vocabularies, simple_record
):
    """Assert that any authenticated user (even a non-community-member) can create a draft.

    Tests the case when authenticated_draft_creation=True.
    """
    with restrict_workflows("community-open", individual="noone"):
        non_member = _create_non_member_user(app, db)

        record = datasets_model.proxies.current_service.create(non_member.identity, data=copy.deepcopy(simple_record))
        assert record is not None


# --- Group B: Review request initiation (community_curator_roles) ---


def test_only_record_owner_can_request_review_by_default(
    app, communities, users, location, vocabularies, simple_record
):
    """Assert that only the record owner may initiate a community-submission request.

    Tests the default workflow where community_curator_roles is empty.
    """
    with restrict_workflows("default-community", individual="noone"):
        _, curator, submitter, _ = users[:4]
        community = communities["default-community"]

        record = datasets_model.proxies.current_service.create(submitter.identity, data=copy.deepcopy(simple_record))

        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        # Curator is not the record owner and community_curator_roles is empty by default.
        with pytest.raises(PermissionDeniedError):
            datasets_model.proxies.current_service.review.create(
                curator.identity,
                data=copy.deepcopy(submission_request_data),
                record=record_from_result(record),
            )
        review_request = datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record_from_result(record),
        )
        assert review_request is not None


def test_curator_roles_are_included_as_requesters_when_configured(app):
    """Assert that community_curator_roles are wired into the community-submission requesters.

    This is a unit test that inspects the built workflow's request policy directly.
    It verifies the *configuration* without going through the full InvenioRDM review
    service (which requires the record to already have a community association).
    """
    from invenio_rdm_records.requests.community_submission import CommunitySubmission
    from oarepo_communities.services.permissions.generators import PrimaryCommunityRole
    from oarepo_workflows.services.permissions import IfInState

    from oarepo_app.config.workflows.community import CommunityWorkflow

    # Build a workflow with two curator roles and inspect the requesters.
    workflow = CommunityWorkflow(
        code="test",
        community_curator_roles=["curator", "manager"],
    ).build_workflow()

    policy = workflow.request_policy_cls(workflow)
    submission = policy.requests_by_id[CommunitySubmission.type_id]

    # Flatten: IfInState wraps the actual generators; unwrap one level.
    flat_generators = [
        gen
        for requester in submission.requesters
        for gen in (requester.then_ if isinstance(requester, IfInState) else [requester])
    ]
    primary_roles = [g for g in flat_generators if isinstance(g, PrimaryCommunityRole)]
    present_roles = {g._role for g in primary_roles}  # noqa: SLF001
    assert "curator" in present_roles, "'curator' should appear in requesters"
    assert "manager" in present_roles, "'manager' should appear in requesters"


def test_no_community_roles_in_requesters_by_default(app):
    """Assert that no PrimaryCommunityRole appears in requesters when community_curator_roles is empty (default)."""
    from invenio_rdm_records.requests.community_submission import CommunitySubmission
    from oarepo_communities.services.permissions.generators import PrimaryCommunityRole
    from oarepo_workflows.services.permissions import IfInState

    from oarepo_app.config.workflows.community import CommunityWorkflow

    workflow = CommunityWorkflow(code="test").build_workflow()
    policy = workflow.request_policy_cls(workflow)
    submission = policy.requests_by_id[CommunitySubmission.type_id]

    flat_generators = [
        gen
        for requester in submission.requesters
        for gen in (requester.then_ if isinstance(requester, IfInState) else [requester])
    ]
    assert not any(isinstance(g, PrimaryCommunityRole) for g in flat_generators), (
        "No PrimaryCommunityRole should appear in requesters with empty community_curator_roles"
    )


# --- Group C: Decline & resubmit flow ---


def test_curator_can_decline_community_submission(app, communities, users, location, vocabularies, simple_record):
    """Assert that a curator can decline a community submission and a plain member cannot."""
    with restrict_workflows("default-community", individual="noone"):
        _, curator, submitter, member = users[:4]
        community = communities["default-community"]

        record = datasets_model.proxies.current_service.create(submitter.identity, data=copy.deepcopy(simple_record))

        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        review_request = datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record_from_result(record),
        )

        current_requests_service.execute_action(
            submitter.identity,
            review_request.id,
            "submit",
        )

        # A plain member must not be able to decline.
        with pytest.raises(PermissionDeniedError):
            current_requests_service.execute_action(
                member.identity,
                review_request.id,
                "decline",
            )

        # Curator (community can_manage role) can decline without error.
        current_requests_service.execute_action(
            curator.identity,
            review_request.id,
            "decline",
        )


# --- Group D: Draft / submitted record read permissions ---


def test_member_cannot_read_submitted_record_by_default(app, communities, users, location, vocabularies, simple_record):
    """Assert that a community member cannot preview a submitted draft.

    Tests the case when read_draft_community_roles is empty (default).
    """
    with restrict_workflows("default-community", individual="noone"):
        _, _, submitter, member = users[:4]
        community = communities["default-community"]

        record = datasets_model.proxies.current_service.create(submitter.identity, data=copy.deepcopy(simple_record))

        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        review_request = datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record_from_result(record),
        )
        current_requests_service.execute_action(
            submitter.identity,
            review_request.id,
            "submit",
        )

        submitted_draft = datasets_model.proxies.current_service.read_draft(submitter.identity, record.id)

        workflow = current_oarepo_workflows.workflow_by_code["default-community"]
        assert not workflow.permissions("preview", record=record_from_result(submitted_draft)).allows(member.identity)


def test_member_can_read_submitted_record_with_draft_read_permission(
    app, communities, users, location, vocabularies, simple_record
):
    """Assert that a community member CAN preview a submitted draft when read_draft_community_roles=['member']."""
    with restrict_workflows("community-member-reads", individual="noone"):
        _, _, submitter, member = users[:4]
        community = communities["community-member-reads"]

        record = datasets_model.proxies.current_service.create(submitter.identity, data=copy.deepcopy(simple_record))

        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        review_request = datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record_from_result(record),
        )
        current_requests_service.execute_action(
            submitter.identity,
            review_request.id,
            "submit",
        )

        submitted_draft = datasets_model.proxies.current_service.read_draft(submitter.identity, record.id)

        workflow = current_oarepo_workflows.workflow_by_code["community-member-reads"]
        assert workflow.permissions("preview", record=record_from_result(submitted_draft)).allows(member.identity)


# --- Group E: Restricted published record read permissions ---


def test_member_cannot_read_restricted_published_record_by_default(
    app, communities, users, location, vocabularies, restricted_record
):
    """Assert that a community member cannot read a restricted published record.

    Tests the case when read_restricted_community_roles is empty (default).
    """
    with restrict_workflows("default-community", individual="noone"):
        _, curator, submitter, member = users[:4]
        community = communities["default-community"]

        record = datasets_model.proxies.current_service.create(
            submitter.identity, data=copy.deepcopy(restricted_record)
        )

        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        review_request = datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record_from_result(record),
        )
        current_requests_service.execute_action(
            submitter.identity,
            review_request.id,
            "submit",
        )
        current_requests_service.execute_action(
            curator.identity,
            review_request.id,
            "accept",
        )

        # The record is published and restricted; read the published version as submitter
        # to get the correct record object for the permission check.
        published = datasets_model.proxies.current_service.read(submitter.identity, record.id)
        workflow = current_oarepo_workflows.workflow_by_code["default-community"]
        assert not workflow.permissions("view", record=record_from_result(published)).allows(member.identity)


def test_member_can_read_restricted_published_record_with_permission(
    app, communities, users, location, vocabularies, restricted_record
):
    """Assert that a community member CAN read a restricted published record.

    Tests the case when read_restricted_community_roles=['member'].
    """
    with restrict_workflows("community-member-reads", individual="noone"):
        _, curator, submitter, member = users[:4]
        community = communities["community-member-reads"]

        record = datasets_model.proxies.current_service.create(
            submitter.identity, data=copy.deepcopy(restricted_record)
        )

        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        review_request = datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record_from_result(record),
        )
        current_requests_service.execute_action(
            submitter.identity,
            review_request.id,
            "submit",
        )
        current_requests_service.execute_action(
            curator.identity,
            review_request.id,
            "accept",
        )

        # The record is published and the member role grants restricted read access.
        published = datasets_model.proxies.current_service.read(submitter.identity, record.id)
        workflow = current_oarepo_workflows.workflow_by_code["community-member-reads"]
        assert workflow.permissions("view", record=record_from_result(published)).allows(member.identity)


# --- Group F: Record management permissions ---


def test_member_cannot_manage_record_by_default(app, communities, users, location, vocabularies, simple_record):
    """Assert that a community member cannot manage a draft record.

    Tests the case when record_manage_community_roles is empty (default).
    """
    with restrict_workflows("default-community", individual="noone"):
        _, _, submitter, member = users[:4]
        community = communities["default-community"]

        record = datasets_model.proxies.current_service.create(submitter.identity, data=copy.deepcopy(simple_record))

        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        # Create the review request so the community is associated via the review receiver,
        # allowing CommunityRole to resolve it during the permission check.
        datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record_from_result(record),
        )

        submitted_draft = datasets_model.proxies.current_service.read_draft(submitter.identity, record.id)

        workflow = current_oarepo_workflows.workflow_by_code["default-community"]
        assert not workflow.permissions("manage", record=record_from_result(submitted_draft)).allows(member.identity)


def test_member_can_manage_record_with_permission(app, communities, users, location, vocabularies, simple_record):
    """Assert that a community member CAN manage a draft record when record_manage_community_roles=['member']."""
    with restrict_workflows("community-member-manages", individual="noone"):
        _, _, submitter, member = users[:4]
        community = communities["community-member-manages"]

        record = datasets_model.proxies.current_service.create(submitter.identity, data=copy.deepcopy(simple_record))

        submission_request_data = {
            "receiver": {"community": community.id},
            "type": "community-submission",
        }

        # Create the review request so the community is associated via the review receiver,
        # allowing CommunityRole to resolve it during the permission check.
        datasets_model.proxies.current_service.review.create(
            submitter.identity,
            data=copy.deepcopy(submission_request_data),
            record=record_from_result(record),
        )

        submitted_draft = datasets_model.proxies.current_service.read_draft(submitter.identity, record.id)

        workflow = current_oarepo_workflows.workflow_by_code["community-member-manages"]
        assert workflow.permissions("manage", record=record_from_result(submitted_draft)).allows(member.identity)
