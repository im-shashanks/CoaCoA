# CoaCoA rules for Cline

- Always read `.coacoa/coacoa.yaml` for configuration values before acting.
- Commands map 1:1 with agents. Example:
  - `/analyze-codebase` → use `.coacoa/agents/code_explorer.md`.
  - `/pm new-prd` → use `.coacoa/agents/pm.md` with `.coacoa/templates/prd.md`.
  - When a required artefact path in `coacoa.yaml` does not exist, call `/orchestrator fix <artefact>`.

- AGENT SELECTION HINTS

  - If `.coacoa/context/analysis.md` is **absent**, default to greenfield flows (analyst → pm → architect).
  - If present, default to brownfield flows (code-explorer → pm → architect / sm).

# CoaCoA command palette for Cline

commands:
  - trigger: /analyze-codebase
    description: Initialise Code-Intelligence snapshot (code-explorer)
    agent: code-explorer
    file: .coacoa/agents/code_explorer.md

  - trigger: /analyst init
    description: Begin Domain Analysis with optional quoted idea
    agent: analyst
    file: .coacoa/agents/analyst.md

  - trigger: /analyst
    description: Continue answering Analyst questions
    agent: analyst
    file: .coacoa/agents/analyst.md

  - trigger: /pm new-prd
    description: Create / refresh PRD
    agent: pm
    file: .coacoa/agents/pm.md

  - trigger: /ux-designer make-ui
    description: Generate UI/UX specification
    agent: ux-designer
    file: .coacoa/agents/ux_designer.md

  - trigger: /po refine-epics
    description: Refine epics and backlog
    agent: po
    file: .coacoa/agents/po.md

  - trigger: /architect finalize-arch
    description: Generate architecture docs + ADRs
    agent: architect
    file: .coacoa/agents/architect.md

  - trigger: /scrum-master create
    description: Split epics into stories
    agent: scrum-master
    file: .coacoa/agents/scrum_master.md

  - trigger: /dev implement
    placeholder: "<story_id>"
    description: Implement a story
    agent: dev
    file: .coacoa/agents/dev.md

  - trigger: /qa review
    description: Run QA gate on story
    agent: qa
    file: .coacoa/agents/qa.md

  - trigger: /orchestrator
    placeholder: '"<instruction>"'
    description: natural-language orchestration (see README)
    agent: orchestrator
    file: .coacoa/agents/orchestrator.md

  - trigger: /orchestrator run
    description: Drive Dev→QA loop for next backlog story
    agent: orchestrator
    file: .coacoa/agents/orchestrator.md

  - trigger: /orchestrator log
    description: Show orchestrator log
    agent: orchestrator
    file: .coacoa/agents/orchestrator.md

  - trigger: /orchestrator fix
    placeholder: "<artefact>"
    description: Regenerate missing artefact (internal)
    agent: orchestrator
    file: .coacoa/agents/orchestrator.md