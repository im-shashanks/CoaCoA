# Task · refine_epics
_Assigned to: PO agent_

> **Goal**  
> Transform PM-generated Epics (`e_*.md`) into a backlog-ready state:
> • add INVEST acceptance criteria  
> • rank by business value vs effort  
> • link dependencies & risks

---

## 0 · Inputs

| File | Source |
|------|--------|
| `{{cfg.prd.main}}` | From PM |
| `{{cfg.prd.shard_dir}}/{{cfg.file_prefixes.epic}}*.md` | Epic files |
| `{{cfg.paths.hotspots}}` (brownfield) | for tech-debt weight |
| `{{cfg.paths.dependencies}}` | licence / vendor risk |

---

## 1 · Acceptance-criteria upgrade

For each epic file:

1. Replace plain bullets with **INVEST format**  
   * *Independent, Negotiable, Valuable, Estimable, Small, Testable*  
2. Append “Definition of Done” bullets (security, docs, QA).

---

## 2 · Effort & value scoring

*Value* = User impact (1–5) × Market reach (1–5) – Licence risk (0–3)  
*Effort* = Story points **OR** T-shirt size (S/M/L/XL) if points unknown.  
Output a table in **`backlog.md`**:

| Epic | Value | Effort | Risk | Rank |
|------|-------|--------|------|------|

Sort descending by Value/Effort ratio.

---

## 3 · Dependency & risk links

* If epic touches a hotspot file ⇒ add 🔥 tag, raise risk score by 1.  
* If epic introduces new OSS package ⇒ note licence column.

---

## 4 · Validation

* **Anti-Hallucination** H-1…H-12  
* **Link-Integrity** L-1, L-2, L-8  
* All epics now contain an **`acceptance_criteria:`** front-matter key.

Return: COMPLETED refine_epics or `FAILED refine_epics – <reason>`.