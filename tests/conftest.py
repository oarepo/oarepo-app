import pytest
from flask import Blueprint
from invenio_access.models import Role
from invenio_i18n import lazy_gettext as _
from oarepo_communities.services.permissions.policy import CommunityPermissionPolicy
from oarepo_requests.utils import system_identity

from oarepo_app.config.config import IndividualWorkflow
from oarepo_app.config.workflows.community import CommunityWorkflow

pytest_plugins = [
    "pytest_oarepo.requests.fixtures",
    "pytest_oarepo.records",
    "pytest_oarepo.fixtures",
    "pytest_oarepo.users",
    "pytest_oarepo.files",
    "pytest_oarepo.roles",
    "pytest_oarepo.communities.fixtures",
]


@pytest.fixture(scope="module")
def app_config(app_config):
    from .model import datasets_model

    datasets_model.register()

    app_config["WORKFLOWS"] = [
        # the default workflow, authenticated draft creation enabled
        IndividualWorkflow(
            code="individual",
            publish_without_review=True,
        ).build_workflow(),
        # noone except of superuser can create drafts
        IndividualWorkflow(
            code="noone",
            authenticated_draft_creation=False,
        ).build_workflow(),
        # users with the creator_role can create drafts. They can publish them without review
        IndividualWorkflow(
            code="individual_creator_role",
            draft_creation_roles=["creator-role"],
            publish_without_review=True,
        ).build_workflow(),
        # users with the creation_access need can create drafts. They can publish them without review
        # only if they simultaneously have the publisher_role
        IndividualWorkflow(
            code="individual_creator_need",
            draft_creation_needs=["creation-access"],
            publish_without_review=True,
            publish_without_review_roles=["publisher-role"],
        ).build_workflow(),
        # An external-preapprove is a process where an external system preapproves a deposit
        # by changing its state to "preapproved"
        IndividualWorkflow(
            code="external-preapprove",
            publish_without_review=True,
            publish_without_review_states=["preapproved"],
        ).build_workflow(),
        # TODO: reviewing workflow
        IndividualWorkflow(
            code="curated",
            review_required=True,
            reviewer_roles=["reviewer-role"],
        ).build_workflow(),
        IndividualWorkflow(
            code="curated_with_access",
            review_required=True,
            reviewer_needs=["review-access"],
        ).build_workflow(),
        # community workflows. Note: using slugs because we name communities in tests in the same way as workflows they use
        CommunityWorkflow(code="default-community").build_workflow(),
        # members can also create drafts
        CommunityWorkflow(
            code="community-member-creates",
            draft_creation_community_roles=["member", "submitter"],
        ).build_workflow(),
        # any authenticated user can create (community-open)
        CommunityWorkflow(
            code="community-open", authenticated_draft_creation=True
        ).build_workflow(),
        # curators are added as review requesters
        CommunityWorkflow(
            code="community-curator-requests", community_curator_roles=["curator"]
        ).build_workflow(),
        # members can read drafts/submitted + restricted published records
        CommunityWorkflow(
            code="community-member-reads",
            read_draft_community_roles=["member"],
            read_restricted_community_roles=["member"],
        ).build_workflow(),
        # members can manage records
        CommunityWorkflow(
            code="community-member-manages", record_manage_community_roles=["member"]
        ).build_workflow(),
    ]

    app_config["COMMUNITIES_ROLES"] = [
        dict(
            name="owner",
            title=_("Community owner"),
            description=_("Can manage community."),
            is_owner=True,
            can_manage=True,
            can_manage_roles=["owner", "curator", "member"],
        ),
        dict(
            name="curator",
            title=_("Curator"),
            description=_("Can curate records."),
            can_manage=True,
            # NTK decision: curator should NOT be able to manage curators
            can_manage_roles=["member"],
        ),
        dict(
            name="submitter",
            title=_("Submitter"),
            description=_("Community submitter - can submit records to the community."),
        ),
        dict(
            name="member",
            title=_("Member"),
            description=_("Community member with read permissions."),
        ),
    ]
    app_config["COMMUNITIES_PERMISSION_POLICY"] = CommunityPermissionPolicy

    app_config["MAIL_DEFAULT_SENDER"] = "test@oarepo-app.org"

    return app_config


@pytest.fixture(scope="module")
def app(app):
    bp = Blueprint("datasets_ui", __name__)

    @bp.route("/test-requests/preview/<pid_value>", methods=["GET"])
    def preview(pid_value: str) -> str:
        return "preview ok"

    @bp.route("/test-requests/", methods=["GET"])
    def search() -> str:
        return "search ok"

    @bp.route("/test-requests/uploads/<pid_value>", methods=["GET"])  # draft self_html
    def deposit_edit(pid_value: str) -> str:
        return "deposit edit ok"

    @bp.route("/test-requests/uploads/new", methods=["GET"])
    def deposit_create() -> str:
        return "deposit create ok"

    @bp.route("/test-requests/records/<pid_value>")
    def record_detail(pid_value) -> str:
        return "detail ok"

    @bp.route("/test-requests/records/<pid_value>/latest", methods=["GET"])
    def record_latest(pid_value: str) -> str:
        return "latest ok"

    @bp.route(
        "/test-requests/records/<pid_value>/export/<export_format>", methods=["GET"]
    )
    def export(pid_value, export_format: str) -> str:
        return "export ok"

    app.register_blueprint(bp)
    return app


@pytest.fixture
def roles(db):
    def _create(role_name):
        r = db.session.query(Role).filter_by(name=role_name).first()
        if not r:
            r = Role(name=role_name)
            db.session.add(r)
        return r

    _create("creator-role")
    _create("publisher-role")
    _create("reviewer-role")

    db.session.commit()


@pytest.fixture(scope="module")
def vocabularies(app, database):
    from invenio_vocabularies.proxies import current_service

    current_service.create_type(system_identity, "resourcetypes", "v_rstp")
    current_service.create(
        system_identity,
        {"type": "resourcetypes", "id": "dataset", "title": {"en": "Dataset"}},
    )
    current_service.indexer.refresh()


@pytest.fixture
def communities(
    app, db, community_get_or_create, users, location, init_communities_cf, invite
):

    def create_community(code):
        community = community_get_or_create(
            users[0], code, {}, workflow=code, allowed_workflows=[code]
        )
        invite(users[1], community.id, "curator")
        invite(users[2], community.id, "submitter")
        invite(users[3], community.id, "member")
        return community

    return {
        "default-community": create_community("default-community"),
        "community-member-creates": create_community("community-member-creates"),
        "community-open": create_community("community-open"),
        "community-curator-requests": create_community("community-curator-requests"),
        "community-member-reads": create_community("community-member-reads"),
        "community-member-manages": create_community("community-member-manages"),
    }


@pytest.fixture
def restricted_record():
    return {
        "metadata": {
            "title": "restricted blah",
            "resource_type": {"id": "dataset"},
            "publication_date": "2024-01-01",
            "creators": [
                {
                    "person_or_org": {
                        "type": "personal",
                        "name": "Jane Doe",
                        "first_name": "Jane",
                        "family_name": "Doe",
                    }
                }
            ],
        },
        "access": {
            "record": "restricted",
            "files": "restricted",
        },
        "files": {"enabled": False},
    }


@pytest.fixture
def simple_record():
    return {
        "metadata": {
            "title": "blah",
            "resource_type": {"id": "dataset"},
            "publication_date": "2024-01-01",
            "creators": [
                {
                    "person_or_org": {
                        "type": "personal",
                        "name": "John Doe",
                        "first_name": "John",
                        "family_name": "Doe",
                    }
                }
            ],
        },
        "files": {
            "enabled": False,
        },
    }
