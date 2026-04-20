"""CLI tool to classify a given RGB/HSV into the system."""
from pathlib import Path
import sys

WORKSPACE_ROOT = Path(__file__).resolve().parents[3]
if str(WORKSPACE_ROOT) not in sys.path:
    sys.path.insert(0, str(WORKSPACE_ROOT))

from Dev.Chromaspace.src.Chromaspace.hsv import hsv_to_rgb
from Dev.Chromaspace.src.Chromaspace.xkcd import nearest_xkcd_colour

if __name__ == "__main__":
    if len(sys.argv) == 4:
        h, s, v = map(float, sys.argv[1:4])
        rgb = hsv_to_rgb(h, s, v)
        print(f"RGB: {rgb}")
        print(f"Nearest XKCD: {nearest_xkcd_colour(rgb)}")
    elif len(sys.argv) == 4:
        r, g, b = map(int, sys.argv[1:4])
        print(f"Nearest XKCD: {nearest_xkcd_colour([r, g, b])}")
    else:
        print("Usage: inspect_colour.py H S V | R G B")
