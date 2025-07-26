# Changelog

## [0.1.0-beta] – 2025-07-30
### Added
- First public beta of **CoaCoA**: scaffold CLI, 12 agents, quality gates, dependency-aware orchestrator.
- Supports Claude-Code and Cline.

### Fixed
- CLI now succeeds outside git repos.
- Path handling moves all artefacts into `.coacoa/`.

### Internal
- 92 % test coverage, PyYAML & Typer dependencies frozen.