# Anti-Hallucination Checklist

## Applies to: Analyst · PM · PO · Architect · Scrum-Master · Dev · QA · Orchestrator

> **Usage**  
> • Each agent **must** insert this checklist into its reasoning loop and tick every box before producing final output.  
> • If any item fails, the agent should either:  
>
> 1. Ask the user / upstream agent a clarifying question, **or**  
> 2. Emit `/orchestrator fix …` with the missing artefact name.  

| # | Checkpoint | Pass/Fail |
|---|------------|-----------|
| **H-1** | **File & path validity** — Every referenced path exists _inside the repo root_. | |
| **H-2** | **Symbol validity** — For brownfield, every function / class / method exists in `{{cfg.paths.module_map}}`. | |
| **H-3** | **Identifier uniqueness** — Ambiguous symbols (same name in ≥2 modules) are qualified with full path. | |
| **H-4** | **Snippet budget** — Raw code injected into a doc/story ≤ `{{cfg.limits.max_snippet_loc}}` LOC total. | |
| **H-5** | **Config fidelity** — All hard-coded numbers / paths are pulled from `coacoa.yaml`, not guessed. | |
| **H-6** | **Prompt self-containment** — Output includes all context needed; no hidden dependencies on external chat state. | |
| **H-7** | **Clarify before coding** — If uncertainty ≥ 1 “unknown/???”, the agent pauses and requests detail. | |
| **H-8** | **No TODO placeholders** — “TODO”, “FIXME”, or “TBD” strings are absent from final code/docs. | |
| **H-9** | **Deterministic names** — Newly created files/functions follow naming rules in `{{cfg.data.tech_prefs}}`. | |
| **H-10** | **No secret leakage** — Output does not print keys, tokens, or passwords. | |
| **H-11** | **Coding-style compliance** — New code conforms to language style prefs in `{{cfg.data.tech_prefs}}` (indent, naming). | |
| **H-12** | **Comment accuracy** — Inline comments/docstrings do **not** contradict code behaviour. | |

## Performance Quality Gates

| # | Checkpoint | Pass/Fail |
|---|------------|-----------|
| **P-1** | **Database queries** — No N+1 query patterns; use eager loading or batching for related data. | |
| **P-2** | **Caching strategy** — Expensive computations or external API calls are cached appropriately. | |
| **P-3** | **Memory usage** — No obvious memory leaks; large collections are processed in batches. | |
| **P-4** | **Algorithm complexity** — Time complexity is reasonable for expected data sizes (O(n²) flagged for >1000 items). | |
| **P-5** | **Resource cleanup** — File handles, connections, and other resources are properly closed/disposed. | |
| **P-6** | **Async patterns** — I/O operations use async/await patterns where available; no blocking calls in async contexts. | |

## Security Quality Gates

| # | Checkpoint | Pass/Fail |
|---|------------|-----------|
| **S-1** | **Input validation** — All user inputs are validated and sanitized before processing. | |
| **S-2** | **SQL injection prevention** — Database queries use parameterized queries or ORM methods, never string concatenation. | |
| **S-3** | **Authentication checks** — Protected endpoints verify user authentication and authorization. | |
| **S-4** | **Sensitive data handling** — Passwords, tokens, and secrets are never logged or exposed in responses. | |
| **S-5** | **XSS prevention** — User-generated content is properly escaped/sanitized before rendering. | |
| **S-6** | **HTTPS enforcement** — Security-sensitive operations require encrypted connections. | |
| **S-7** | **Rate limiting** — Public APIs implement appropriate rate limiting to prevent abuse. | |
| **S-8** | **Error information** — Error messages don't leak sensitive system information to unauthorized users. | |

## Maintainability Quality Gates

| # | Checkpoint | Pass/Fail |
|---|------------|-----------|
| **M-1** | **Function complexity** — Functions have cyclomatic complexity ≤ 10; highly complex functions (>15) are refactored. | |
| **M-2** | **Function length** — Functions are ≤ 50 lines; longer functions are broken down or well-justified. | |
| **M-3** | **Class responsibility** — Classes follow Single Responsibility Principle; classes >500 LOC are reviewed. | |
| **M-4** | **Dependency management** — External dependencies are minimal and well-justified; no circular dependencies. | |
| **M-5** | **Code duplication** — No copy-pasted code blocks >5 lines; common functionality is extracted to shared functions. | |
| **M-6** | **Documentation coverage** — Public APIs have comprehensive documentation; complex business logic is explained. | |
| **M-7** | **Test coverage** — New functionality has ≥90% test coverage; edge cases and error conditions are tested. | |
| **M-8** | **Backwards compatibility** — API changes maintain backwards compatibility or follow proper deprecation process. | |

## Data Quality Gates

| # | Checkpoint | Pass/Fail |
|---|------------|-----------|
| **D-1** | **Data validation** — All data inputs have appropriate type and range validation. | |
| **D-2** | **Database constraints** — Database schema enforces data integrity with appropriate constraints. | |
| **D-3** | **Transaction boundaries** — Database operations use appropriate transaction boundaries; rollback on errors. | |
| **D-4** | **Data migration safety** — Database migrations are reversible and tested on production-like data. | |
| **D-5** | **PII handling** — Personally identifiable information follows data protection regulations (GDPR, CCPA). | |
| **D-6** | **Data retention** — Data retention policies are implemented; old data is archived or deleted appropriately. | |
