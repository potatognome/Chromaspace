## [0.3.0] - 2026-04-19
- Workspace migration to Core/SuiteTools/Applications layout.
- Path normalization for portable multi-device use (no machine-specific absolute roots).
- Consolidated Copilot instructions at project scope.

## [0.2.0] - 2026-04-19
- Workspace migration to Core/SuiteTools/Applications layout.
- Path normalization for portable multi-device use (no machine-specific absolute roots).
- Consolidated Copilot instructions at project scope.

# Chromaspace — Changelog

All notable changes to this project will be documented here.
Format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## [0.1.0] — 2026-04-05

### Added
- Renamed project from `colour_system` to **Chromaspace**
- tUilKit factory imports wired into `config.py`, `generator.py`, `export.py`
- `CHROMASPACE_CONFIG.json` — app-level config with ROOT_MODES, PATHS, LOG_FILES, SHARED_CONFIG
- `main.py` — menu-driven CLI entry point via `chromaspace` console script
- `logFiles/` folder for session and master logs
- `docs/` folder with README, CHANGELOG, ROADMAP
- Multi-space colour engine: HSV, OKLCh (Ottosson), CIE Lab
- `colour_engine.py` dispatch router for swappable colour-space backends
- `colour_spaces/` subpackage: `hsv.py`, `oklch.py`, `lab.py`
- Uniform hue variant spacing derived from anchor step
- Sorted hue angle output order in generator and visualization
- Strengthened test suite: spacing uniformity and sorted-order assertions

### Fixed
- Variant offset calculation now uses `gap = anchor_step / variant_count` (was hardcoded ±5°)
- HTML table XKCD display now shows `"name (d.d)"` format
- Hue squares renderer: variants side-by-side per anchor row (mega-grid layout)

---


