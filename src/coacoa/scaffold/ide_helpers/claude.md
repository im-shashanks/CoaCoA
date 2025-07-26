# CoaCoA Command Palette for Claude Code

| Slash command | Purpose (⇢ agent) |
|---------------|------------------|
| `/analyze-codebase` | Initialise Code-Intelligence snapshot **(code-explorer)** |
| `/analyst init "<idea>"` | Start Domain Analysis Q&A loop **(analyst)** |
| `/analyst` | Continue answering Analyst follow-ups |
| `/pm new-prd` | Generate / refresh PRD **(pm)** |
| `/ux-designer make-ui` | Produce UI/UX spec **(ux-designer)** |
| `/po refine-epics` | Rank backlog & refine epics **(po)** |
| `/architect finalize-arch` | Produce architecture doc & ADRs **(architect)** |
| `/scrum-master create` | Split epics into stories **(scrum-master)** |
| `/dev implement <story_id>` | Implement single story **(dev)** |
| `/qa review` | Run QA gate on current story **(qa)** |
| `/orchestrator run` | Full workflow (default) |
| `/orchestrator "agents:dev,qa story=s_001_04"` | Run Dev & QA on one story |
| `/orchestrator fix <artefact>` | Regenerate a missing artefact (internal use) |

**Parameter notes**

* `<idea>` – one-line vision statement in quotes, e.g.  
  `/analyst init "Serverless photo-tagging SaaS"`
* `<story_id>` – file stem such as `s_001_01`.