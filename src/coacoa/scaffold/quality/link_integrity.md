# Link-Integrity Checklist

## Applies to: PM · PO · Architect · Scrum-Master · QA · Orchestrator

> **Purpose** — Ensure every reference between documents, epics, stories, code files, and diagrams is resolvable.

| # | Asset type | Integrity rules |
|---|------------|-----------------|
| **L-1** | **PRD ↔ Architecture** | Every requirement in `prd.*` maps to at least one section or diagram in `arch.*`. |
| **L-2** | **Epic ↔ Story** | Story front-matter `epic_id` matches an existing `e_*.md`. |
| **L-3** | **Story ↔ Code** | All `micro_context.file` paths exist; line ranges fall inside file length. |
| **L-4** | **Cross-shard links** | `[[link]]`/`[text](rel/path)` between shards are valid (no 404 in Markdown preview). |
| **L-4a** | New intelligence artefacts | (`dependencies.json`, `cycles.json`) exist and parse. |
| **L-5** | **Diagram sources** | Mermaid or SVG diagrams declaring a file/module reference point to real files. |
| **L-6** | **External URLs** | HTTP/HTTPS links return 200-level status (skip for intranet). |
| **L-7** | **Workflow YAML** | Stages in `workflows/*.yml` correspond to actual agent IDs. |
| **L-8** | **Config keys** | Every `{{cfg.…}}` token used in any template resolves in `coacoa.yaml`. |
| **L-9** | **Removed artefacts** | Deleted files are not referenced anywhere in current docs/stories after merge. |
| **L-10**| **SemVer tags** | Version strings in README / setup / docs stay in sync (e.g. `__version__`, `pyproject.toml`). |
| **L-11**| **Open-Source licences** | Any third-party library noted in docs/arch links to an OSS licence file present in repo. |
