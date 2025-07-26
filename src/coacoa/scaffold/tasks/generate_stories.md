# Task · generate_stories
_Assigned to: scrum-master agent_

> **Objective**  
> For each epic, create 1–n INVEST-compliant stories with
> embedded micro-context (≤ {{cfg.limits.max_snippet_loc}} LOC total)
> so Dev/QA agents have all they need without re-prompting.

---

## 0 · Inputs

| Artefact | Purpose |
|----------|---------|
| `{{cfg.docs.prd.shard_dir}}/{{cfg.file_prefixes.epic}}*.md` | Source epics |
| `{{cfg.arch.main}}` + shards | Component boundaries |
| `{{cfg.paths.module_map}}` | Symbol lookup |
| `{{cfg.paths.dep_graph}}` | For traceability links |
| `{{cfg.paths.build_info}}` | For build info |
| `backlog.md` | Epic ranking → story priority |

---

### Pre-Process Dependencies
1. Parse `backlog.md` under the `## Dependencies` header.  
   → Build a dict `epic_blockers = {"e_003": ["e_002"], "e_004":["e_002","e_003"], …}`

### Shard & Emit Stories
2. For each epic shard → create `s_*.md` and add YAML key  
   `depends_on: [ <story_ids of blocker epics> ]`  
   (use the **final story ID** of each blocker epic, e.g. `s_002_last`).

## 1 · Story ID & file naming

* Prefix `{{cfg.file_prefixes.story}}` (e.g. `s_001_01` = first story of epic `e_001`).
* Files live in `stories/` sub-dir inside epic shard location.

---

## 2 · Story structure (`templates/story.md`)

* Front-matter keys:
  * `story_id`
  * `epic_id`
  * `priority` (inherited from backlog rank)
  * `component` (service / module)
  * `micro_context` (list of file+line ranges)
  * `acceptance_criteria`
  * `definition_of_done` (checklist)

---

## 3 · Micro-context injection rules

1. For each acceptance criterion, locate **exact** function/class or API in `module_map.json`.
2. Extract start/end lines; ensure sum of ranges ≤ `{{cfg.limits.max_snippet_loc}}`.
3. Embed with fenced code block annotated by lang.
4. *Embed Dev-Setup using build_info.commands.* into story template.

---

## 4 · INVEST enforcement

* **Independent** – no cross-story blocking unless noted in `depends_on`.
* **Negotiable** – criteria bullets can be adjusted by Dev if unclear.
* **Valuable** – ties back to user persona.
* **Estimable** – ≤ 5 SP; if larger, split story.
* **Small** – target completion < 1 dev-day.
* **Testable** – criteria map to at least one unit/integration test.

---

## 5 · Validation

* **Anti-Hallucination** H-1…H-12  
* **Link-Integrity** L-2 (epic↔story), L-3, L-8  
* **Story micro-context paths exist and line ranges valid.**
* **Inject Dev-Setup & Test-Stub**
    •	Load {{cfg.paths.build_info}}.
    •	Replace placeholder {{build_info.commands.*}} in story template.

Return: `COMPLETED generate_stories` or failure string.