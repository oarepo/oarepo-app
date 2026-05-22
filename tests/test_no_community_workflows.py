import re

import pytest
from flask_principal import ActionNeed
from invenio_access.models import ActionUsers
from invenio_accounts.models import Role, User
from oarepo_requests.proxies import current_requests_service
from oarepo_workflows.proxies import current_oarepo_workflows
from pytest_invenio.user import UserFixtureBase

from tests.model import datasets_model

creation_access = ActionNeed("creation-access")
review_access = ActionNeed("review-access")


@pytest.mark.parametrize(
    "workflow_type,user_roles,user_needs,outcome",
    [
        ("individual", [], [], True),
        ("noone", [], [], False),
        ("individual_creator_role", [], [], False),
        ("individual_creator_role", ["creator-role"], [], True),
        ("individual_creator_need", [], [], False),
        ("individual_creator_need", [], [creation_access], True),
    ],
)
def test_create_record(app, db, roles, workflow_type, user_roles, user_needs, outcome):
    u = create_user(app, db, user_roles, user_needs)

    workflow = current_oarepo_workflows.workflow_by_code[workflow_type]
    permissions = workflow.permissions("create")
    assert permissions.allows(u.identity) == outcome


@pytest.mark.parametrize(
    "workflow_type,user_roles,user_needs,outcome",
    [
        ("individual", [], [], True),
        ("individual_creator_role", ["creator-role"], [], True),
        ("individual_creator_need", [], [creation_access], False),
        ("individual_creator_need", ["publisher-role"], [creation_access], True),
        ("curated", [], [], False),
        ("curated_with_access", [], [], False),
    ],
)
def test_publish_record(
    app, db, roles, location, workflow_type, user_roles, user_needs, outcome
):
    u = create_user(app, db, user_roles, user_needs)

    record_result = datasets_model.proxies.current_service.create(
        u.identity, data={"parent": {"workflow": workflow_type}}
    )

    workflow = current_oarepo_workflows.workflow_by_code[workflow_type]
    permissions = workflow.permissions("publish", record=record_result._record)
    assert permissions.allows(u.identity) == outcome


@pytest.mark.parametrize(
    "workflow_type,user_roles,user_needs,reviewer_role, reviewer_needs, outcome",
    [
        ("individual", [], [], [], [], False),
        ("individual_creator_role", ["creator-role"], [], [], [], False),
        ("individual_creator_need", [], [creation_access], [], [], False),
        (
            "individual_creator_need",
            ["publisher-role"],
            [creation_access],
            [],
            [],
            False,
        ),
        ("curated", [], [], ["reviewer-role"], [], True),
        ("curated_with_access", [], [], [], ["review-access"], True),
    ],
)
def test_publish_with_review(
    app,
    db,
    roles,
    location,
    vocabularies,
    simple_record,
    workflow_type,
    user_roles,
    user_needs,
    reviewer_role,
    reviewer_needs,
    outcome,
):
    u = create_user(app, db, user_roles, user_needs, email="submitter@test.com")

    reviewer = create_user(
        app, db, ["reviewer-role"], [review_access], email="reviewer@test.com"
    )

    record_result = datasets_model.proxies.current_service.create(
        u.identity,
        data={"parent": {"workflow": workflow_type}, **simple_record},
    )

    available_requests = {
        x["type_id"]: x
        for x in current_requests_service.applicable_request_types(
            u.identity, record_result._record
        )
    }
    assert ("publish_draft" in available_requests) == outcome

    if not outcome:
        return

    # create and submit publication request
    request = current_requests_service.create(
        u.identity,
        request_type="publish_draft",
        topic=record_result._record,
        data={"payload": {"version": "1.0"}},
    )
    if reviewer_role:
        assert request.data["receiver"] == {
            "group": db.session.query(Role).filter_by(name=reviewer_role[0]).first().id
        }
    elif reviewer_needs:
        assert request.data["receiver"] == {"action_need": reviewer_needs[0]}

    mail = app.extensions.get("mail")
    assert mail

    # when the request is submitted, a notification should be sent to the reviewer
    with mail.record_messages() as outbox:
        current_requests_service.execute_action(u.identity, request.id, action="submit")
        assert len(outbox) == 1
        sent_mail = outbox[0]
        assert "reviewer@test.com" in sent_mail.recipients
        assert "Request to publish record blah" in sent_mail.subject

    # when the request is accepted, a notification should be sent to the submitter
    with mail.record_messages() as outbox:
        current_requests_service.execute_action(
            reviewer.identity, request.id, action="accept"
        )
        assert len(outbox) == 1
        sent_mail = outbox[0]
        assert "submitter@test.com" in sent_mail.recipients
        assert "Record 'blah' has been published" in sent_mail.subject


def create_user(app, db, user_roles, user_needs, email="myuser@test.com"):
    # create the user
    # delete the user if exists
    u = db.session.query(User).filter_by(email=email).first()
    if u:
        db.session.delete(u)
        db.session.commit()

    u = UserFixtureBase(email=email)
    u.create(app, db)

    for role in user_roles:
        u.user.roles.append(db.session.query(Role).filter_by(name=role).first())
    db.session.add(u.user)
    db.session.commit()

    for un in user_needs:
        a = ActionUsers.allow(un, user_id=u.id)
        db.session.add(a)
    db.session.commit()
    return u
