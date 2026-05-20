from __future__ import annotations

import dataclasses

from invenio_i18n import lazy_gettext as _
from invenio_rdm_records.requests.community_submission import CommunitySubmission
from invenio_rdm_records.services.generators import (
    RecordCommunitiesAction,
    RecordOwners,
)
from invenio_records_permissions.generators import AuthenticatedUser, Generator
from invenio_records_permissions.policies.base import BasePermissionPolicy
from oarepo_communities.services.permissions.generators import (
    CommunityRole,
    InAnyCommunity,
    PrimaryCommunityRole,
)
from oarepo_requests.services.permissions.generators import RequestActive
from oarepo_requests.types import PublishDraftRequestType
from oarepo_workflows import IfInState
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
class CommunityWorkflow(BaseWorkflowSettings):
    """Workflow configuration for deposits inside communities."""

    authenticated_draft_creation: bool = False
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

    draft_creation_community_roles: list[str] = dataclasses.field(
        default_factory=lambda: ["submitter"]
    )
    """
        Restrict draft creation to authenticated users with at least
        one of these community roles. If not specified, any member of a community
        can create a draft.
    """

    read_restricted_community_roles: list[str] = dataclasses.field(
        default_factory=lambda: []
    )
    """
    List of community roles that are able to read the content of restricted
    records without having to ask for the access. If empty, only the record
    owner can read the content after publishing.

    Note: we are using community roles instead of RecordCommunitiesAction
    so that each workflow can have different read/draft/manage permissions.
    """

    read_draft_community_roles: list[str] = dataclasses.field(
        default_factory=lambda: []
    )
    """
    List of community roles that are able to read the content of draft
    records without having to ask for the access. If empty, only the record
    owner can read the content of the draft.

    Note that curators can always read the content of draft records when
    the record is submitted for review.

    Note: we are using community roles instead of RecordCommunitiesAction
    so that each workflow can have different read/draft/manage permissions.
    """

    record_manage_community_roles: list[str] = dataclasses.field(
        default_factory=lambda: []
    )
    """
    List of community roles that are able to manage the record (e.g. edit,
    delete, publish). If empty, only the record owner can manage the record.

    Note: we are using community roles instead of RecordCommunitiesAction
    so that each workflow can have different read/draft/manage permissions.
    """

    community_curator_roles: list[str] = dataclasses.field(default_factory=list)
    """Community roles that allow users to review and curate records."""

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
            can_read = (
                self.base_permission_policy.can_read
                + self._build_record_view_permissions()
            )
            can_rdm_manage = self._build_record_rdm_manage_generators(
                self.base_permission_policy.can_rdm_manage
            )
            can_rdm_view = self._build_record_rdm_view_permissions(
                self.base_permission_policy.can_rdm_view
            )
            can_rdm_preview = self._build_record_rdm_preview_generators(
                self.base_permission_policy.can_rdm_preview
            )
            can_publish = [*self.base_permission_policy.can_publish, RequestActive()]

        return PermissionPolicy

    def _build_record_rdm_view_permissions(
        self, original_rdm_permissions
    ) -> list[Generator]:
        # remove the RecordCommunitiesAction from the can_rdm_view permissions
        ret = [
            gen
            for gen in original_rdm_permissions
            if not isinstance(gen, RecordCommunitiesAction)
        ]
        for role in self.read_restricted_community_roles:
            ret.append(CommunityRole(role))
        return ret

    def _build_record_rdm_preview_generators(
        self, original_rdm_permissions
    ) -> list[Generator]:
        ret = [
            gen
            for gen in original_rdm_permissions
            if not isinstance(gen, RecordCommunitiesAction)
        ]
        for role in self.read_draft_community_roles:
            ret.append(CommunityRole(role))
        return ret

    def _build_record_rdm_manage_generators(
        self, original_rdm_permissions
    ) -> list[Generator]:
        ret = [
            gen
            for gen in original_rdm_permissions
            if not isinstance(gen, RecordCommunitiesAction)
        ]
        for role in self.record_manage_community_roles:
            ret.append(CommunityRole(role))
        return ret

    def _build_record_create_generators(self) -> tuple[Generator, ...]:
        """Build and return the generators for record creation."""
        create_generators = []
        if self.draft_creation_roles:
            # if draft_creation_roles are set, use them to define the generators
            create_generators += [
                UserWithRole(role_name) for role_name in self.draft_creation_roles
            ]
        if self.draft_creation_needs:
            # if draft_creation_needs are set, use them to define the generators
            create_generators += [
                HasActionNeed(action) for action in self.draft_creation_needs
            ]
        if not create_generators and self.authenticated_draft_creation:
            # if no generators are set and authenticated_draft_creation is enabled,
            # use AuthenticatedUser as a fallback
            create_generators = [AuthenticatedUser()]

        # add PrimaryCommunityRole generator if roles are set
        for role in self.draft_creation_community_roles:
            # TODO: this need optimization, raises with the number of communities !!!
            create_generators += [InAnyCommunity(PrimaryCommunityRole(role))]

        return tuple(create_generators)

    def _build_record_view_permissions(self) -> tuple[Generator, ...]:
        if not self.record_view_permissions:
            return ()
        return tuple(
            IfInState(state, then_=generators)
            for state, generators in self.record_view_permissions.items()
        )

    def _build_request_policy(self) -> type[WorkflowRequestPolicy]:

        curator_need_generators: list[PrimaryCommunityRole] = []
        if self.community_curator_roles:
            curator_need_generators = [
                PrimaryCommunityRole(role) for role in self.community_curator_roles
            ]

        requests = {
            CommunitySubmission.type_id: WorkflowRequest(
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

        CommunityReviewRequestPolicy = type(
            "CommunityReviewRequestPolicy", (self.base_request_policy,), requests
        )

        return CommunityReviewRequestPolicy
