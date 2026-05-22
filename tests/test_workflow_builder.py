"""Tests for workflow builder utilities.

Covers low-hanging-fruit gaps highlighted by the coverage report:

* add_if_in_state empty-states branch (base.py line 40)
* configure_workflows scenarios (config/workflows/__init__.py lines 50-93)
* extra_permissions / extra_requests as a class and as a callable
  (base.py lines 127-132, 134-139)
* record_view_permissions non-empty path (base.py line 160)
* publish_without_review_needs (individual.py line 132)
* publish_after_review=False raises NotImplementedError (individual.py line 152)
"""

import pytest
from invenio_records_permissions.generators import AnyUser, AuthenticatedUser
from invenio_records_permissions.policies.base import BasePermissionPolicy
from oarepo_workflows.requests.policy import WorkflowRequestPolicy
from oarepo_workflows.services.permissions import IfInState
from oarepo_workflows.services.permissions.composite import CompositeAndGenerator

from oarepo_app.config.workflows import configure_workflows
from oarepo_app.config.workflows.base import add_if_in_state
from oarepo_app.config.workflows.community import CommunityWorkflow
from oarepo_app.config.workflows.individual import IndividualWorkflow

# ---------------------------------------------------------------------------
# add_if_in_state
# ---------------------------------------------------------------------------


def test_add_if_in_state_empty_states_returns_plain_list(app, db):
    """When states is empty the generators are returned as-is, without IfInState."""
    gen = AuthenticatedUser()
    result = add_if_in_state([], [gen])
    assert result == [gen]


def test_add_if_in_state_with_states_wraps_in_if_in_state(app, db):
    """When states are provided a single IfInState generator is returned."""
    gen = AuthenticatedUser()
    result = add_if_in_state(["draft"], [gen])
    assert len(result) == 1
    assert isinstance(result[0], IfInState)


# ---------------------------------------------------------------------------
# configure_workflows
# ---------------------------------------------------------------------------


def test_configure_workflows_no_args_creates_permissive_individual(app, db):
    """With no arguments a single permissive IndividualWorkflow (code='individual') is built."""
    context = {"_": None}  # truthy so results land in context, not in caller globals
    workflows = configure_workflows(context=context)
    assert len(workflows) == 1
    assert workflows[0].code == "individual"
    assert context["WORKFLOWS"] is workflows
    assert context["WORKFLOWS_DEFAULT_WORKFLOW"] == "individual"


def test_configure_workflows_auto_adds_restricted_individual_when_missing(app, db):
    """If no IndividualWorkflow is given, a restricted one (code='individual') is appended."""
    context = {"_": None}
    configure_workflows(
        CommunityWorkflow(code="my-community"),
        context=context,
    )
    codes = {wf.code for wf in context["WORKFLOWS"]}
    assert "individual" in codes
    assert "my-community" in codes


def test_configure_workflows_raises_when_default_workflow_code_is_absent(app, db):
    """ValueError is raised when default_individual_workflow code is not in definitions."""
    with pytest.raises(ValueError, match="No workflow with code"):
        configure_workflows(
            IndividualWorkflow(code="custom"),
            default_individual_workflow="individual",  # "individual" not present
            context={},
        )


def test_configure_workflows_raises_on_duplicate_codes(app, db):
    """ValueError is raised when two workflow definitions share the same code."""
    with pytest.raises(ValueError, match="Duplicate workflow codes"):
        configure_workflows(
            IndividualWorkflow(code="individual"),
            CommunityWorkflow(code="individual"),  # same code as above
            context={},
        )


# ---------------------------------------------------------------------------
# extra_permissions
# ---------------------------------------------------------------------------


def test_extra_permissions_as_mixin_class(app, db):
    """extra_permissions given as a class is merged into the policy via type()."""

    class ExtraPerms(BasePermissionPolicy):
        can_extra = (AnyUser(),)

    workflow = IndividualWorkflow(
        code="extra-type",
        extra_permissions=ExtraPerms,
    ).build_workflow()

    assert issubclass(workflow.permission_policy_cls, ExtraPerms)
    assert hasattr(workflow.permission_policy_cls, "can_extra")


def test_extra_permissions_as_callable(app, db):
    """extra_permissions given as a callable is invoked with the generated policy class."""
    received = []

    def patch_perms(cls):
        received.append(cls)
        return cls

    IndividualWorkflow(
        code="extra-callable",
        extra_permissions=patch_perms,
    ).build_workflow()

    assert len(received) == 1


# ---------------------------------------------------------------------------
# extra_requests
# ---------------------------------------------------------------------------


def test_extra_requests_as_mixin_class(app, db):
    """extra_requests given as a class is merged into the request policy via type()."""

    class ExtraReqs(WorkflowRequestPolicy):
        pass

    workflow = IndividualWorkflow(
        code="extra-req-type",
        extra_requests=ExtraReqs,
    ).build_workflow()

    assert issubclass(workflow.request_policy_cls, ExtraReqs)


def test_extra_requests_as_callable(app, db):
    """extra_requests given as a callable is invoked with the generated request policy class."""
    received = []

    def patch_reqs(cls):
        received.append(cls)
        return cls

    IndividualWorkflow(
        code="extra-req-callable",
        extra_requests=patch_reqs,
    ).build_workflow()

    assert len(received) == 1


# ---------------------------------------------------------------------------
# record_view_permissions
# ---------------------------------------------------------------------------


def test_record_view_permissions_non_empty_builds_if_in_state(app, db):
    """A non-empty record_view_permissions dict produces IfInState generators."""
    gen = AuthenticatedUser()
    settings = IndividualWorkflow(
        code="view-perms",
        record_view_permissions={"submitted": [gen]},
    )
    result = settings._build_record_view_permissions()
    assert len(result) == 1
    assert isinstance(result[0], IfInState)


# ---------------------------------------------------------------------------
# IndividualWorkflow publish generators
# ---------------------------------------------------------------------------


def test_publish_without_review_needs_produces_composite_generators(app, db):
    """publish_without_review_needs creates CompositeAndGenerator entries."""
    settings = IndividualWorkflow(
        code="pub-needs",
        publish_without_review_needs=["publish-access"],
    )
    generators = settings._build_record_publish_generators()
    assert len(generators) == 1
    assert isinstance(generators[0], CompositeAndGenerator)


def test_publish_after_review_false_raises_not_implemented(app, db):
    """Setting publish_after_review=False together with review_required=True raises NotImplementedError."""
    with pytest.raises(NotImplementedError):
        IndividualWorkflow(
            code="no-after-review",
            review_required=True,
            publish_after_review=False,
        ).build_workflow()
