from __future__ import annotations

import dataclasses

from invenio_i18n import lazy_gettext as _
from invenio_rdm_records.services.generators import RecordOwners
from invenio_records_permissions.generators import AuthenticatedUser, Generator
from invenio_records_permissions.policies.base import BasePermissionPolicy
from oarepo_requests.services.permissions.generators import RequestActive
from oarepo_requests.types import PublishDraftRequestType
from oarepo_workflows.requests import WorkflowRequest, WorkflowTransitions
from oarepo_workflows.requests.policy import WorkflowRequestPolicy
from oarepo_workflows.services.permissions import IfInState
from oarepo_workflows.services.permissions.composite import (
    CompositeAndGenerator,
    CompositePermissionPolicyMixin,
)
from oarepo_workflows.services.permissions.generators import HasActionNeed, UserWithRole

from .base import BaseWorkflowSettings


@dataclasses.dataclass
class IndividualWorkflow(BaseWorkflowSettings):
    """Workflow configuration for deposits outside of communities."""

    code = "individual"
    """Unique code identifier for this workflow."""

    label = _("Individual Submission Workflow")
    """Human-readable label for this workflow."""

    authenticated_draft_creation: bool = True
    """Allow authenticated users to create drafts in this workflow.

    When enabled, any authenticated user can create a draft record.
    """

    draft_creation_roles: list[str] = dataclasses.field(default_factory=list)
    """Restrict draft creation to authenticated users with at least one of these roles.

    If this list is non-empty, `authenticated_draft_creation` is ignored.
    """

    draft_creation_needs: list[str] = dataclasses.field(default_factory=list)
    """Restrict draft creation to authenticated users with at least one of these permission needs.

    If this list is non-empty, `authenticated_draft_creation` is ignored.
    """

    publish_without_review: bool = False
    """Allow draft owners to publish without submitting a review request.

    When enabled, draft owners can publish directly, subject to
    `publish_without_review_states`.
    """

    publish_without_review_roles: list[str] = dataclasses.field(default_factory=list)
    """Roles that allow a draft owner to publish without a review request.

    Users must still be owners of the draft record. If the list is non-empty,
    `publish_without_review` is ignored.
    """

    publish_without_review_needs: list[str] = dataclasses.field(default_factory=list)
    """Permission needs that allow a draft owner to publish without a review request.

    Users must still be owners of the draft record. If the list is non-empty,
    `publish_without_review` is ignored.
    """

    publish_without_review_states: list[str] = dataclasses.field(
        default_factory=lambda: ["draft"]
    )
    """Record workflow states in which publication without review is allowed."""

    review_required: bool = False
    """Require a review request before publication.

    If `publish_without_review` is False and `review_required` is False,
    records can only be published through a community workflow.
    """

    reviewer_roles: list[str] = dataclasses.field(default_factory=list)
    """Roles that allow users to review and curate records.

    Users with these roles are also granted read access to draft records.
    """

    reviewer_needs: list[str] = dataclasses.field(default_factory=list)
    """Permission needs that allow users to review and curate records.

    Users with these needs are also granted read access to draft records.
    """

    def _build_permission_policy(self) -> type[BasePermissionPolicy]:

        def add_if_in_state(
            states: list[str],
            generators: tuple[Generator, ...],
        ) -> list[Generator]:
            if not states:
                return list(generators)
            return [IfInState(states, then_=generators)]

        class PermissionPolicy(
            CompositePermissionPolicyMixin, self.base_permission_policy
        ):
            """A permission policy for the workflow."""

            can_create = self._build_record_create_generators()
            can_publish = add_if_in_state(
                self.publish_without_review_states,
                self._build_record_publish_generators(),
            ) + [IfInState("submitted", then_=[RequestActive()])]
            can_read = (
                self.base_permission_policy.can_read
                + self._build_record_view_permissions()
            )

        return PermissionPolicy

    def _build_record_create_generators(self) -> tuple[Generator, ...]:
        """Build and return the generators for record creation."""
        create_generators = []
        if self.draft_creation_roles:
            # if draft_creation_roles are set, use them to define the generators
            create_generators += [
                UserWithRole(role_name) for role_name in self.draft_creation_roles
            ]
            pass
        if self.draft_creation_needs:
            # if draft_creation_needs are set, use them to define the generators
            create_generators += [
                HasActionNeed(action) for action in self.draft_creation_needs
            ]
        if not create_generators and self.authenticated_draft_creation:
            # if no generators are set and authenticated_draft_creation is enabled,
            # use AuthenticatedUser as a fallback
            create_generators = [AuthenticatedUser()]

        return tuple(create_generators)

    def _build_record_publish_generators(self) -> tuple[Generator, ...]:
        """Build and return the generators for record publishing."""
        # note: SystemProcess added automatically
        publish_generators = []
        if self.publish_without_review_roles:
            # if publish_without_review_roles are set, use them to define the generators
            publish_generators += [
                CompositeAndGenerator(RecordOwners(), UserWithRole(role_name))
                for role_name in self.publish_without_review_roles
            ]
        if self.publish_without_review_needs:
            # if publish_without_review_needs are set, use them to define the generators
            publish_generators += [
                CompositeAndGenerator(RecordOwners(), HasActionNeed(action))
                for action in self.publish_without_review_needs
            ]
        if not publish_generators and self.publish_without_review:
            # if no generators are set and publish_without_review is enabled,
            # use RecordOwners as a fallback
            publish_generators = [RecordOwners()]

        return tuple(publish_generators)

    def _build_record_view_permissions(self) -> tuple[Generator, ...]:
        if not self.record_view_permissions:
            return ()
        return tuple(
            IfInState(state, then_=generators)
            for state, generators in self.record_view_permissions.items()
        )

    def _build_request_policy(self) -> type[WorkflowRequestPolicy]:
        if not self.review_required:
            return self.base_request_policy

        curator_need_generators: list[UserWithRole | HasActionNeed] = []
        if self.reviewer_roles:
            curator_need_generators = [
                UserWithRole(role) for role in self.reviewer_roles
            ]
        if self.reviewer_needs:
            curator_need_generators.extend(
                [HasActionNeed(need) for need in self.reviewer_needs]
            )
        if not self.publish_after_review:
            raise NotImplementedError(
                "Disabling publish_after_review is not supported in this version, please ask the maintainers to enable it"
            )

        requests = {
            PublishDraftRequestType.type_id: WorkflowRequest(
                requesters=[
                    # Record owners and curators can request review
                    IfInState(
                        ["draft", "review_requested"],
                        [RecordOwners(), *curator_need_generators],
                    )
                ],
                recipients=curator_need_generators,
                transitions=WorkflowTransitions(
                    submitted="submitted",
                    accepted="published",
                    declined="review_requested",
                ),
            )
        }

        GlobalReviewRequestPolicy = type(
            "GlobalReviewRequestPolicy", (self.base_request_policy,), requests
        )

        return GlobalReviewRequestPolicy
