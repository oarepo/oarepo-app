#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-app (see https://github.com/oarepo/oarepo-app).
#
# oarepo-app is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
"""OARepo application top-level configuration helpers."""

from __future__ import annotations

from .workflows.base import BaseWorkflowSettings
from .workflows.community import CommunityWorkflow
from .workflows.individual import IndividualWorkflow

__all__ = [
    "BaseWorkflowSettings",
    "CommunityWorkflow",
    "IndividualWorkflow",
    "configure_workflows",
]


def configure_workflows(
    individual: IndividualWorkflow | None = None,
    **other_workflows: IndividualWorkflow | CommunityWorkflow,
) -> None:
    """Configure named workflow policies for individual and community deposits."""
