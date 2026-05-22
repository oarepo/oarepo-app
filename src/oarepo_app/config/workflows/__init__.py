from oarepo.config.base import set_constants_in_caller
from oarepo_workflows import Workflow

from .base import BaseWorkflowSettings, add_if_in_state
from .community import CommunityWorkflow
from .individual import IndividualWorkflow


def configure_workflows(
    *workflow_definitions: BaseWorkflowSettings,
    default_individual_workflow: str = "individual",
    context=None,
) -> list[Workflow]:
    """
    This function sets up workflows based on the provided workflow definitions.
    It is intended to be called from within invenio.cfg and will create a "WORKFLOWS"
    entry in the invenio.cfg context (in the caller's globals).

    Example:

        .. code-block:: python

            # invenio.cfg
            from oarepo_app.config import configure_workflows, IndividualWorkflow, CommunityWorkflow

            configure_workflows(
                IndividualWorkflow(
                    authenticated_draft_creation=False,
                    review_required=True,
                    publish_without_review=False,
                ),
                CommunityWorkflow(),
            )
            # no need to assign the result to WORKFLOWS, that is done automatically


    If the workflow definitions are empty, a permissive IndividualWorkflow will be created
    (authenticated draft creation, publish without review allowed).

    If there is no IndividualWorkflow definition in the workflow definitions (but there are other workflow types), a
    restricted IndividualWorkflow (no deposition allowed) will be created with default settings.

    The default_individual_workflow parameter should be the code of the workflow to use
    as the default one for individual deposits, where no community is involved and the
    workflow code is not provided by the caller.

    If the context is provided, the "WORKFLOWS" entry will be added to it instead of
    the caller's globals.
    """
    if not workflow_definitions:
        workflow_definitions = (
            IndividualWorkflow(
                code=default_individual_workflow,
                authenticated_draft_creation=True,
                review_required=False,
                publish_without_review=True,
            ),
        )
    elif not any(
        isinstance(workflow, IndividualWorkflow) for workflow in workflow_definitions
    ):
        workflow_definitions = (
            *workflow_definitions,
            IndividualWorkflow(
                code=default_individual_workflow,
                authenticated_draft_creation=False,
                review_required=False,
                publish_without_review=False,
            ),
        )
    built_workflows = [workflow.build_workflow() for workflow in workflow_definitions]
    if not any(
        workflow.code == default_individual_workflow
        for workflow in workflow_definitions
    ):
        raise ValueError(
            f"No workflow with code '{default_individual_workflow}' found in workflow definitions"
        )
    # check for duplicated codes
    if len(workflow_definitions) != len(
        set(workflow.code for workflow in workflow_definitions)
    ):
        raise ValueError("Duplicate workflow codes found in workflow definitions")

    if context:
        context["WORKFLOWS"] = built_workflows
        context["WORKFLOWS_DEFAULT_WORKFLOW"] = default_individual_workflow
    else:
        set_constants_in_caller(
            {
                "WORKFLOWS": built_workflows,
                "WORKFLOWS_DEFAULT_WORKFLOW": default_individual_workflow,
            }
        )
    return built_workflows


__all__ = [
    "add_if_in_state",
    "BaseWorkflowSettings",
    "CommunityWorkflow",
    "IndividualWorkflow",
    "configure_workflows",
]
