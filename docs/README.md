# Chromaspace — User Guide

## Overview

Chromaspace is a perceptually-structured colour taxonomy generator. It produces semantically-named colour sets across configurable hue, saturation, and luminance bands, supporting multiple colour spaces (HSV, OKLCh, CIE Lab).

## Quick Start

### Install

```powershell
cd .
.\venv\base\Scripts\Activate
pip install -e .\Core\Chromaspace
```

### Run the CLI

```powershell
chromaspace
# or
python -m Chromaspace.main
```

### Generate a Colour JSON directly

```powershell
cd Core/Chromaspace/scripts
python generate_json.py
```

## Configuration

The active colour system is controlled by `config/_COLOUR_SYSTEM_POINTER.json`:

```json
{
    "COLOUR_SYSTEM_NAME": "3x20x4x4",
    "CONFIG_PATH": "COLOUR_SYSTEM_CONFIG_3x20x4x4.json"
}
```

Switch to a different config by editing this pointer. Available configs are in `config/COLOUR_SYSTEM_CONFIG_*.json`.

## Colour System Config Keys

| Key | Description |
|-----|-------------|
| `HUE_ANCHORS` | Named hue anchor points |
| `HUE_VARIANTS` | Variant offsets (e.g. cool/medium/warm) |
| `SAT_BANDS` | Saturation bands `[name, value]` |
| `LUM_BANDS` | Luminance bands `[name, value]` |
| `COLOUR_METHOD` | Engine: `"hsv"`, `"oklch"`, or `"lab"` (optional, default `"hsv"`) |

## Scripts

| Script | Purpose |
|--------|---------|
| `generate_json.py` | Generate full colour JSON |
| `render_hue_squares.py` | HTML tone grids per hue |
| `render_wheels.py` | HTML saturation/luminance wheels |
| `render_tone_grid.py` | HTML tone grid per hue variant |
| `preview_colours.py` | Full HTML colour table preview |
| `filter_colours.py` | Filter colour JSON by band |
| `inspect_colour.py` | Classify an RGB/HSV colour |
| `make_xkcd.py` | Rebuild the XKCD colour reference |

## Output

Generated files are placed in `output/` by default. HTML rendering outputs go to `output/HTML/`.

## Colour Spaces

Chromaspace supports three generation engines, selectable via `COLOUR_METHOD` in the colour config:

- **`hsv`** (default) — standard HSV → RGB
- **`oklch`** — OKLCh perceptual space (Björn Ottosson)
- **`lab`** — CIE L\*a\*b\* with D65 white reference
