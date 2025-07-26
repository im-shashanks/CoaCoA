# Task · generate_prd

Assigned to: PM agent

> **Objective**  
> Produce or refresh the Product Requirements Document (PRD) so that it is:
> • consistent with either Code-Intelligence (brownfield) or Domain Analysis (greenfield)  
> • fully shardable, traceable, and free of hallucinations

---

## 0 · Inputs (resolved via `coacoa.yaml`)

| Mode | Required artefacts |
|------|-------------------|
| Greenfield | `{{cfg.file_prefixes.domain_doc}}*.md` |
| Brownfield | `{{cfg.paths.analysis}}`, `{{cfg.paths.hotspots}}`, `{{cfg.paths.dependencies}}` |

---

## 1 · Pre-flight checks

* Verify **Anti-Hallucination** items H-1…H-12.  
* Verify **Link-Integrity** items L-4a (intelligence artefacts parse).  
* Load `tech_preferences.md` for naming rules.

If any pre-flight fails → `/orchestrator fix <issue>` and stop.

---

## 2 · Section-by-section instructions

1. **Summary**  
   * ≤ 150 words.  Include repo name and mode (Greenfield | Brownfield).  
2. **Goals & Non-goals**  
   * Pull user-facing goals from Domain Analysis (green) or high-churn hotspots (brown).  
3. **Personas**  
   * List each persona, role, primary pain-point.  (Greenfield → from domain doc; Brownfield → infer from existing CLI/API usage in `analysis.md`.)  
4. **Functional Requirements**  
   * Numbered FR-1, FR-2, …  Each <= 1 sentence.  
5. **Non-functional Requirements**  
   * Table: Performance, Availability, Security, Accessibility, Scalability, Observability.  Fill with explicit, measurable targets.  
6. **UI/UX Overview**  
   * Embed reference to `ui_ux.md` plus one sentence per major screen / flow.  
7. **API / Data Contracts**  
   * If Brownfield: list current public modules (from `module_map.json`) + proposed additions.  
8. **Dependencies / Constraints**  
   * Auto-insert top-level packages from `dependencies.json` that are **not** stdlib; note licence placeholders.  
9. **Acceptance Criteria – Epic level**  
   * For each planned epic (see §3 below) include a bullet list of Done criteria.  
10. **Glossary**  
    * Table term → definition; merge existing glossary if file exists.

---

## 3 · Epic enumeration

Produce an **Epics table** (ID → Title → Source).  
Rules:

* Use prefix `{{cfg.file_prefixes.epic}}` (e.g. `e_001` …).  
* Derive IDs as:  
  * Greenfield → one epic per MVP feature or UI flow.  
  * Brownfield → one epic per hotspot cluster or architectural layer.  
* Each epic has ≤ 7 acceptance-criteria bullets.  
* Store each epic in its own Markdown file using **`templates/epic.md`** (see below) inside `{{cfg.prd.shard_dir}}/`.

---

## 4 · Sharding logic

If `prd.sharded == true`:

1. Split PRD main into max 3 000-token shards (`prd_part_1.md`, etc.).  
2. Maintain front-matter in each shard:  

   ```yaml
   prd_version: 0.1.0
   shard: 1/3
   parent: ../prd.md
   sha: <latest_git_sha>

## 5 · Validation

* Run Anti-Hallucination H-1–H-12 again on all shards & epics.
* Run Link-Integrity L-1, L-2, L-8 (config keys) on PRD+epic files.

If any fail → write FAILED generate_prd – `<reason>`; else: COMPLETED generate_prd

## 6. UI / UX Overview

Place the placeholder:  
> “(UI/UX flows will be added by UX-Designer in `ui_ux.md`).”
