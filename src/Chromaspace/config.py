#!/usr/bin/env python3
"""
config.py
Loads Chromaspace app config via tUilKit (explicit path), then loads the
active colour-system JSON config via the pointer file.
"""
import json
import os


def _existing_path(candidates):
    for path in candidates:
        if path and os.path.exists(path):
            return path
    return None

# ---------------------------------------------------------------------------
# App-level config via tUilKit (CHROMASPACE_CONFIG.json)
# Using ConfigLoader with an explicit path so discovery works regardless of
# the working directory (tests run from workspace root, CLI from project dir).
# ---------------------------------------------------------------------------
_CHROMASPACE_CONFIG_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '../../config/CHROMASPACE_CONFIG.json')
)

_WORKSPACE_CHROMASPACE_CONFIG_PATH = os.path.normpath(
    os.path.join(
        os.path.dirname(__file__),
        '../../../../.projects_config/CHROMASPACE_CONFIG.json',
    )
)

try:
    from tUilKit.utils.config import ConfigLoader as _ConfigLoader
    _resolved_app_config_path = _existing_path(
        [_CHROMASPACE_CONFIG_PATH, _WORKSPACE_CHROMASPACE_CONFIG_PATH]
    )
    if _resolved_app_config_path is None:
        raise FileNotFoundError("No Chromaspace app config was found")

    _app_loader = _ConfigLoader(config_path=_resolved_app_config_path)
    app_config = _app_loader.global_config
except Exception:
    app_config = {}

LOG_FILES = app_config.get("LOG_FILES", {
    "SESSION": "logFiles/chromaspace_SESSION.log",
    "MASTER":  "logFiles/chromaspace_MASTER.log",
})

# ---------------------------------------------------------------------------
# Colour-system pointer → active colour config
# ---------------------------------------------------------------------------
_PROJECT_CONFIG_DIR = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '../../config')
)
_WORKSPACE_ROOT = app_config.get("ROOTS", {}).get(
    "WORKSPACE",
    os.path.normpath(os.path.join(os.path.dirname(__file__), '../../../../')),
)
_WORKSPACE_CONFIG_DIR = os.path.normpath(
    os.path.join(_WORKSPACE_ROOT, '.projects_config')
)

POINTER_PATH = _existing_path(
    [
        os.path.join(_PROJECT_CONFIG_DIR, 'CHROMASPACE.d', '_COLOUR_SYSTEM_POINTER.json'),
        os.path.join(_PROJECT_CONFIG_DIR, '_COLOUR_SYSTEM_POINTER.json'),
        os.path.join(_WORKSPACE_CONFIG_DIR, 'CHROMASPACE.d', '_COLOUR_SYSTEM_POINTER.json'),
        os.path.join(_WORKSPACE_CONFIG_DIR, '_COLOUR_SYSTEM_POINTER.json'),
    ]
)
if POINTER_PATH is None:
    raise FileNotFoundError("No Chromaspace colour-system pointer file was found")

with open(POINTER_PATH, 'r') as f:
    pointer = json.load(f)

COLOUR_SYSTEM_NAME = pointer.get("COLOUR_SYSTEM_NAME", "")
COLOUR_SYSTEM_SUFFIX = (
    f"_{COLOUR_SYSTEM_NAME}" if COLOUR_SYSTEM_NAME else ""
)

_spec_filename = pointer["CONFIG_PATH"]
CONFIG_PATH = _existing_path(
    [
        os.path.join(_PROJECT_CONFIG_DIR, 'CHROMASPACE_SPEC', _spec_filename),
        os.path.join(_PROJECT_CONFIG_DIR, _spec_filename),
        os.path.join(_WORKSPACE_CONFIG_DIR, 'CHROMASPACE_SPEC', _spec_filename),
        os.path.join(_WORKSPACE_CONFIG_DIR, _spec_filename),
    ]
)
if CONFIG_PATH is None:
    raise FileNotFoundError(
        f"No Chromaspace colour-system config file was found for {_spec_filename}"
    )

with open(CONFIG_PATH, 'r') as f:
    _config = json.load(f)

_bands = _config

HUE_ANCHORS = _bands["HUE_ANCHORS"]
HUE_VARIANTS = _bands["HUE_VARIANTS"]
SAT_BANDS = _bands["SAT_BANDS"]  # list of (name, value)
LUM_BANDS = _bands["LUM_BANDS"]  # list of (name, value)
SAT_BANDS_GREY = _bands["SAT_BANDS_GREY"]  # list of (name, value)
LUM_BANDS_GREY = _bands["LUM_BANDS_GREY"]  # list of (name, value)

# Global offsets for special tables
HUE_GLOBAL_OFFSET = _bands.get("HUE_GLOBAL_OFFSET", 0)
SAT_GLOBAL_OFFSET = _bands.get("SAT_GLOBAL_OFFSET", 0)
LUM_GLOBAL_OFFSET = _bands.get("LUM_GLOBAL_OFFSET", 0)

# Per-band offsets for special tables
HUE_OFFSETS = _bands.get("HUE_OFFSETS", [0]*len(HUE_ANCHORS))
SAT_OFFSETS = _bands.get("SAT_OFFSETS", [0]*len(SAT_BANDS))
LUM_OFFSETS = _bands.get("LUM_OFFSETS", [0]*len(LUM_BANDS))

from .hue import get_sorted_hues

# Combined tuples for easier table generation
HUE_TUPLES = get_sorted_hues()
SAT_TUPLES = [(i, name, value) for i, (name, value) in enumerate(SAT_BANDS)]
LUM_TUPLES = [(i, name, value) for i, (name, value) in enumerate(LUM_BANDS)]
GREY_TUPLES = [(i, name, value, LUM_BANDS_GREY[i][1])
               for i, (name, value) in enumerate(SAT_BANDS_GREY)]

__all__ = [
    "_config", "app_config", "LOG_FILES",
    "HUE_ANCHORS", "HUE_VARIANTS", "SAT_BANDS", "LUM_BANDS",
    "HUE_TUPLES", "SAT_TUPLES", "LUM_TUPLES", "GREY_TUPLES",
    "HUE_OFFSETS", "SAT_OFFSETS", "LUM_OFFSETS",
    "HUE_GLOBAL_OFFSET", "SAT_GLOBAL_OFFSET", "LUM_GLOBAL_OFFSET",
    "COLOUR_SYSTEM_NAME", "COLOUR_SYSTEM_SUFFIX"
]
