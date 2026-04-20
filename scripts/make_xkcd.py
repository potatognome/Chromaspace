


import json
import os
from pathlib import Path
import sys

import requests

WORKSPACE_ROOT = Path(__file__).resolve().parents[3]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from Dev.Chromaspace.src.Chromaspace.config import _config
from Dev.Chromaspace.src.Chromaspace.cli_utils import ensure_output_dir, save_json

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return [int(hex_str[i:i+2], 16) for i in (0, 2, 4)]

# Download from official source
url = "https://xkcd.com/color/rgb.txt"
response = requests.get(url)
lines = response.text.split('\n')

colors = {}
for idx, line in enumerate(lines):
    # Skip header (first line) and comments
    if idx == 0 or not line or line.startswith('#'):
        continue
    try:
        if '\t' not in line:
            continue
        name, hex_val = line.split('\t', 1)
        name = name.strip()
        hex_val = hex_val.strip()
        colors[name] = {"rgb": hex_to_rgb(hex_val)}
    except Exception as e:
        # Optionally log or print the error, but continue
        continue

# Save to JSON using config path
xkcd_path = _config["PATHS"]["FILES"]["XKCD_JSON"]
ensure_output_dir(xkcd_path)
save_json(colors, xkcd_path)
