# QA checklist

- [ ] Test names clearly map to acceptance criteria.
- [ ] Refactors do not change public interfaces unless story said so.
- [ ] No story leaves TODOs unresolved without justification.
- [ ] Unit tests achieve ≥ 90 % line coverage for changed files.

## QA Checklist

### Applies to: QA agent (primary), Dev agent (pre-commit), Orchestrator (gatekeeper)

## 0. Preconditions

- [ ] Current branch merges cleanly with main.
- [ ] `{{cfg.paths.analysis}}` exists (brownfield) _or_ domain analysis doc exists (greenfield).

## 1. Automated tests

- [ ] New or changed code has **unit tests** with ≥ 90 % line coverage for touched files **or** matches project exemption list.
- [ ] All tests pass with `pytest -q`.
- [ ] Test names clearly map to story acceptance criteria (`test_<story_id>_*`).
- [ ] **Static typing** check (`mypy --strict`) passes for new/changed Python files.
- [ ] **Thread-safety / async-safety** unit tests exist for code using threading / `asyncio`.

## 2. Code quality

- [ ] `ruff` or `flake8` yields **0 errors** (config from `data/tech_preferences.md`).
- [ ] Cyclomatic complexity of new functions ≤ 15 **or** justified in story.
- [ ] Public APIs maintain backward compatibility unless story explicitly breaks them.
- [ ] Error handling follows project exception hierarchy; no naked `except:` blocks.
- [ ] Logging uses structured logger from `tech_preferences.md`; no `print()` left in production code.

## 3. Docs & comments

- [ ] Docstrings present for every public function/class.
- [ ] PRD section _“Implemented Changes”_ updated with story ID and brief summary.
- [ ] ADR (Architecture Decision Record) updated in `/docs/adr/` if design choices changed.

## 4. Security & secrets

- [ ] `detect-secrets scan` reports no findings.
- [ ] No plain-text credentials, keys, tokens, or personal data.
- [ ] `pip-audit` (or equivalent) shows **0 high/critical CVEs** on dependency tree.

## 5. Performance & scalability

- [ ] DB queries in new code are indexed or batched (if applicable).
- [ ] Logging is at appropriate level (INFO/ERROR) and uses structured logging library.
- [ ] Memory footprint measured for long-running tasks if story introduces new daemon/service.

## 6. Anti-hallucination & link integrity

- [ ] All **H-1…H-10** checks pass (import `anti_hallucination.md`).
- [ ] All **L-1…L-9** checks pass (import `link_integrity.md`).

## 7. Story closure

- [ ] Acceptance criteria in story are all **checked off**.
- [ ] Story file footer includes:  
- [ ] Roll-back steps documented if change is non-trivial (DB schema, API contract).

**QA-Approved-By:**
**Date:**
