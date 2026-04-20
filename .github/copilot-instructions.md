# Copilot Instructions — Chromaspace (Core + Chromacore Registry)

## Purpose
Chromaspace is the kernel of the colour‑geometry platform. It provides:
- Geometric primitives
- Colour‑space adapters
- System‑level interfaces
- The Chromacore Registry (core registry)
- Integration with tUilKit config + logging

All extensions (Chromaschemes, Chromagrams, renderers, exporters) depend on Chromaspace.

Copilot must ensure:
- The Chromacore Registry is implemented as a first‑class subsystem
- All modules register through the registry
- All config loading uses tUilKit’s deterministic config framework
- All logging uses tUilKit structured logging
- All interfaces are explicit, typed, and stable
- All modules remain modular, override‑friendly, and auditable

---

## Project Structure
  - Chromaspace/ 
    - src/chromaspace/
      - core/
      - registry/
      - colour_spaces/
      - geometry/
      - interfaces/
    - config/
      - CHROMASPACE_SPEC/
        - COLOUR_SYSTEM_CONFIG.json
      - CHROMASPACE.d/
      - CHROMASPACE_CONFIG.json
    - docs/      
    - tests/


---

## Chromacore Registry Requirements

### Responsibilities
Copilot must implement the registry as a subsystem that:
- Maintains typed module tables
- Validates module metadata
- Enforces deterministic ordering
- Integrates with tUilKit config
- Logs registration events
- Provides lookup APIs for:
  - Scheme generators
  - Animation sequences
  - Renderers
  - Colour‑space adapters
  - Future module types

### Registry API
Copilot must implement:
- `register(module_type, name, version, factory, capabilities, config_schema)`
- `get(module_type, name)`
- `get_all(module_type)`
- `find(module_type, capability)`
- `disable(module_type, name)`
- `metadata(module_type, name)`
- `freeze()`

### Decorators
Copilot must provide:
- `@register_scheme`
- `@register_animation`
- `@register_renderer`
- `@register_colour_space`

Decorators must:
- Validate metadata
- Register the module
- Attach metadata to the class

### Module Types
Defined in `module_types.py`:
- `scheme_generator`
- `animation_sequence`
- `renderer`
- `colour_space`
- `utility` (future)

### Metadata Schema
Copilot must enforce:
- `name`
- `version`
- `capabilities`
- `config_schema`
- `priority` (optional)

---

## Interfaces
Copilot must maintain stable interfaces:
- `SchemeInterface`
- `AnimationInterface`
- `RendererInterface`
- `ColourSpaceInterface`

All modules must implement these interfaces.

---

## Geometry + Colour Spaces
Copilot must ensure:
- All geometry primitives are modular
- All colour‑space adapters register themselves
- All math is deterministic and auditable

---

## tUilKit Integration
Copilot must:
- Load config via tUilKit
- Support `.d` override directories
- Log registry events
- Provide audit‑friendly metadata

---

## Testing Requirements
Copilot must scaffold:
- Registry tests
- Geometry tests
- Colour‑space tests
- Interface compliance tests