
"""CLI script to generate the full colour_system.json."""
from pathlib import Path
import sys

# Allow running this script directly from the scripts folder by exposing
# the workspace root (the folder that contains `Dev`).
WORKSPACE_ROOT = Path(__file__).resolve().parents[3]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from Dev.Chromaspace.src.Chromaspace.generator import generate_colour_entries
from Dev.Chromaspace.src.Chromaspace.export import export_to_json
from Dev.Chromaspace.src.Chromaspace.cli_utils import save_json
from Dev.Chromaspace.src.Chromaspace.cli_utils import (
    ensure_output_dir,
    get_output_file,
)

if __name__ == "__main__":
    colours = generate_colour_entries()
    out_path = get_output_file(
        "COLOUR_SYSTEM_JSON",
        "../output/colour_system.json",
        with_system_suffix=True,
    )
    ensure_output_dir(out_path)
    # Optionally use save_json if not using export_to_json
    # save_json(colours, out_path)
    export_to_json(colours, out_path)
    print(f"Generated {len(colours)} colours to {out_path}")
