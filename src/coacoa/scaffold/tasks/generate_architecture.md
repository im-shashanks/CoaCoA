# Task · generate_architecture
_Assigned to: Architect agent_

> **Objective**  
> Produce (or refresh) the architecture document, its shards, Mermaid diagrams,
> and—when needed—one ADR per major decision.

---

## 0 · Inputs

| File / artefact | Purpose |
|-----------------|---------|
| `{{cfg.prd.main}}` & shards | Business + NFR source of truth |
| `ui_ux.md` (optional) | UI flows, component boundaries |
| `backlog.md` | Ranked epics, acceptance criteria |
| `{{cfg.paths.module_map}}` | Current modules/classes (brownfield) |
| `{{cfg.paths.cycles}}` | Cycles to break |
| `{{cfg.paths.dep_graph}}` | For diagram generation |

---

## 1 · High-level steps

1. **Context validation**  
   * Anti-Hallucination H-1…H-12  
   * Link-Integrity L-1, L-4, L-8, L-11  
   * Cycles: if any cycle involves new modules → abort & ask PM/PO.

2. **Logical view**  
   * Identify services/components; map to epics.  
   * Draw Mermaid C4: `context` and `container` diagrams.

3. **Module/component view**  
   * Brownfield → enumerate existing packages; mark those to refactor.  
   * Greenfield → propose module namespace & directory layout.  
   * Embed Mermaid dependency graph (uses `dep_graph.json`).

4. **Data/API view**  
   * For every public interface in backlog, define request/response JSON (or proto) shape.

5. **Non-functional alignment**  
   * Explicit tables: performance budgets, scalability targets, availability, observability, accessibility.

6. **Cross-cutting concerns**  
   * Security, logging, feature-flag, internationalisation sections.

7. **Sharding**  
   * If `arch.sharded == true` & doc > 3 000 tokens, split per logical view.

8. **ADR creation**  
   * For **each** major decision (database type, auth scheme, async vs sync, …):  
     * Run task `write_adr.md` to produce `docs/adr/YYYY-MM-DD-<slug>.md`.  
     * Link file name in Architecture doc front-matter under `adr:` list.

9. **Validation**  
   * Architecture-Integrity checklist A-1…A-7.  
   * Re-run Anti-Hallucination & Link-Integrity across shards + ADRs.

10. **Output**  
    * Write/overwrite `{{cfg.arch.main}}`, shards, ADRs.  
    * Return `COMPLETED generate_architecture` or failure string.

---