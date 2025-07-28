# Changelog

## [0.1.0b2.post2] – 2025-07-31
### Fixed
- Packaged `.clinerules/**` folder so that `coacoa init --cline` works when
  the package is installed from PyPI.  
  (Hidden directories were previously excluded by setuptools.)

### Packaging
- Updated `pyproject.toml` `package-data` glob to include
  `ide_helpers/.clinerules/**`.

## [0.1.0b2] – 2025-07-31
### Fixed
- `coacoa init --cline` now copies only the `.clinerules/` helper directory into the project root and no longer duplicates `ide_helpers/` inside `.coacoa/`.

### Internal
- Added directory‑aware helper installation logic.
- Updated package‐data glob and CI tests (coverage unchanged at 92 %).

## [0.1.0b1] – 2025-07-30
### Added
- First public beta of **CoaCoA**: scaffold CLI, 12 agents, quality gates, dependency-aware orchestrator.
- Supports Claude-Code and Cline.

### Fixed
- CLI now succeeds outside git repos.
- Path handling moves all artefacts into `.coacoa/`.

### Internal
- 92 % test coverage, PyYAML & Typer dependencies frozen.