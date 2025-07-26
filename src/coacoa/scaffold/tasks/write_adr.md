# Task · write_adr
_Called by: Architect agent_

## ADR template reference
`templates/adr.md`

**When to create**  
– Any decision that is costly to reverse, visible to many devs, or influences future choices.

**Steps**

1. Fill ADR front-matter:
   * id → date + serial (e.g., 2025-07-26-001)
   * status → “Proposed” (auto)  
2. Fill sections: Context, Decision, Consequences, Alternatives.  
3. Save file to `{{cfg.docs.adr_dir}}` using slugified title.  
4. Return file name so Architect can reference it.