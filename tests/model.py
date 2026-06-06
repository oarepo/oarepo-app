#
# Copyright (c) 2026 CESNET z.s.p.o.
#
# This file is a part of oarepo-app (see https://github.com/oarepo/oarepo-app).
#
# oarepo-app is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.
#
from __future__ import annotations

from oarepo_communities.model.presets import communities_preset
from oarepo_model.api import model
from oarepo_rdm.model import rdm_complete_preset
from oarepo_requests.model.presets.requests import requests_preset
from oarepo_workflows.model.presets import workflows_preset

datasets_model = model(
    "datasets",
    version="1.1.0",
    presets=[
        rdm_complete_preset,
        workflows_preset,
        requests_preset,
        communities_preset,
    ],
    types=[{"Metadata": {}}],
    metadata_type="Metadata",
    customizations=[],
    configuration={"ui_blueprint_name": "datasets_ui"},
)
