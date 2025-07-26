# CoaCoA – Command Palette for Claude Code

| Slash command | Purpose (⇢ agent) | Agent file |
|--------------|-------------------|------------|
| `/analyze-codebase` | Initialise Code-Intelligence snapshot **(code-explorer)** | `.coacoa/agents/code_explorer.md` |
| `/analyst init "<idea>"` | Start Domain Analysis Q&A loop **(analyst)** | `.coacoa/agents/analyst.md` |
| `/analyst` | Continue answering Analyst follow-ups | `.coacoa/agents/analyst.md` |
| `/pm new-prd` | Generate / refresh PRD **(pm)** | `.coacoa/agents/pm.md` |
| `/ux-designer make-ui` | Produce UI/UX spec **(ux-designer)** | `.coacoa/agents/ux_designer.md` |
| `/po refine-epics` | Rank backlog & refine epics **(po)** | `.coacoa/agents/po.md` |
| `/architect finalize-arch` | Produce architecture doc & ADRs **(architect)** | `.coacoa/agents/architect.md` |
| `/scrum-master create` | Split epics into stories **(scrum-master)** | `.coacoa/agents/scrum_master.md` |
| `/dev implement <story_id>` | Implement single story **(dev)** | `.coacoa/agents/dev.md` |
| `/qa review` | Validate Dev’s story **(qa)** | `.coacoa/agents/qa.md` |
| `/orchestrator run` | Drive full Dev → QA flow on next backlog story **(orchestrator)** | `.coacoa/agents/orchestrator.md` |
| `/orchestrator log` | Show latest orchestrator log | `.coacoa/agents/orchestrator.md` |
| `/orchestrator fix <artefact>` | Regenerate a missing artefact | `.coacoa/agents/orchestrator.md` |

---

**How to use**

1. Note the purpose for each command for context
2. Follow the file path provided in the table above for each command.

**Parameter notes**

* `<idea>` – one-line vision statement in quotes, e.g.  
  `/analyst init "Serverless photo-tagging SaaS"`
* `<story_id>` – file stem such as `s_001_01`.