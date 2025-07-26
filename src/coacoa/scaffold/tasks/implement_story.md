# Task · implement_story
_Assigned to: Dev agent_

## Inputs
* Story file (`s_*.md`)
* `module_map.json`, `build_info.json`
* Tech prefs, style guides

## Steps
1. **Load story front-matter** – snaffle component path & micro-context.
2. **Create / modify code** so acceptance criteria pass.
**2a. Scoped diff check**  
* Run `git diff --name-only` and ensure every path is within allowed list (micro_context files + new component dir).  
* If violation → abort with `FAILED implement_story – scope_violation`.
3. **Update test stub** in `tests/unit/test_<story_id>.py`; achieve ≥ 90 % coverage for touched files.
4. **Run build & test commands** from `build_info.commands.*`.
5. **Run linter / type checker** (`ruff`, `mypy --strict`).
6. Measure coverage % for touched files.  If < 90 % → add tests until ≥ 90 %.
7. Update story footer:
    Build-OK: true
    Tests-OK: true
    Coverage: 93 %
8. Commit diff ready; do **NOT** change unrelated files.

## Validation
* Anti-Hallucination H-1…H-12  
* Build-Integrity B-1…B-4  

Return `COMPLETED implement_story` or failure string.