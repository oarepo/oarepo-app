#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-app (see https://github.com/oarepo/oarepo-app).
#
# oarepo-app is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
from __future__ import annotations

import contextlib

from flask import current_app
from oarepo_workflows.proxies import current_oarepo_workflows


@contextlib.contextmanager
def restrict_workflows(*workflow_codes: str, individual=None):
    def clear_cache() -> None:
        with contextlib.suppress(AttributeError):
            del current_oarepo_workflows.workflow_by_code
        with contextlib.suppress(AttributeError):
            del current_oarepo_workflows.state_changed_notifiers

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
