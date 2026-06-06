import contextlib

from flask import current_app
from oarepo_workflows.proxies import current_oarepo_workflows


@contextlib.contextmanager
def restrict_workflows(*workflow_codes, individual=None):
    def clear_cache():
        try:
            del current_oarepo_workflows.workflow_by_code
        except AttributeError:
            pass
        try:
            del current_oarepo_workflows.state_changed_notifiers
        except AttributeError:
            pass

    orig_workflows = current_app.config["WORKFLOWS"]
    orig_default_workflow = current_app.config["WORKFLOWS_DEFAULT_WORKFLOW"]
    current_app.config["WORKFLOWS"] = [
        wf for wf in orig_workflows if wf.code in workflow_codes or wf.code == individual
    ]
    current_app.config["WORKFLOWS_DEFAULT_WORKFLOW"] = individual
    try:
        clear_cache()
        yield
    finally:
        current_app.config["WORKFLOWS"] = orig_workflows
        current_app.config["WORKFLOWS_DEFAULT_WORKFLOW"] = orig_default_workflow
        clear_cache()
