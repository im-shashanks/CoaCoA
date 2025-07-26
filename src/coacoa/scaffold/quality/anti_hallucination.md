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
