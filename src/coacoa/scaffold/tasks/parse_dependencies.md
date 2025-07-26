---
id: parse_dependencies
role: "System Task – Dependency Parser"
purpose: >
  Build two in-memory maps for the Orchestrator:
  • epic_blockers → which epics depend on which other epics  
  • story_map     → every story’s status + depends_on list
inputs:
  - backlog.md
  - ".coacoa/docs/prd/e_*.md"
  - ".coacoa/docs/prd/stories/s_*.md"
outputs:
  - (returns python dicts to caller; writes nothing to disk)
---

## Steps

```python
import re, yaml, glob
from pathlib import Path

root = Path.cwd()

# ---------------- backlog.md → epic_blockers
dep_section = (root / "backlog.md").read_text(encoding="utf-8")
pattern = r"\*\*(e_\d+)\*\*.*?(?:requires|depends on).*?\*\*(e_\d+)\*\*"
epic_blockers = {}
for a, b in re.findall(pattern, dep_section, flags=re.I):
    epic_blockers.setdefault(a, []).append(b)

# ---------------- story files → story_map
story_map = {}
for p in glob.glob(".coacoa/docs/prd/stories/s_*.md"):
    front = Path(p).read_text().split("---", 2)[1]
    meta = yaml.safe_load(front)
    story_map[meta["story_id"]] = {
        "status": meta.get("status", "TODO"),
        "depends_on": meta.get("depends_on", []),
        "epic": meta["epic"],
    }

# ---------------- epic status
epic_status = {}
for p in glob.glob(".coacoa/docs/prd/e_*.md"):
    front = Path(p).read_text().split("---", 2)[1]
    meta = yaml.safe_load(front)
    epic_status[meta["epic_id"]] = meta.get("status", "TODO")

# ---------------- return to caller (Orchestrator)
return {"epic_blockers": epic_blockers,
        "story_map": story_map,
        "epic_status": epic_status}
        