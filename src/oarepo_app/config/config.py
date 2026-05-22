from __future__ import annotations

from .workflows.base import BaseWorkflowSettings
from .workflows.community import CommunityWorkflow
from .workflows.individual import IndividualWorkflow

__all__ = [
    "BaseWorkflowSettings",
    "IndividualWorkflow",
    "CommunityWorkflow",
    "configure_workflows",
]


def configure_workflows(
    individual: IndividualWorkflow | None = None,
    **other_workflows: IndividualWorkflow | CommunityWorkflow,
):
    """Configure named workflow policies for individual and community deposits."""
    pass
