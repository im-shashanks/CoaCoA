# THIS COMMAND IS FOR ORCHESTRATION TASKS. YOU MUST FOLLOW INSTRUCTIONS EXACTLY AS GIVEN. DO NOT DEVIATE FROM THE PROCESS.

## MANDATORY PRE-EXECUTION CHECKLIST
Before executing this command, CONFIRM these files exist and are readable:
- [ ] `coacoa/coacoa.yaml` (framework configuration)
- [ ] `coacoa/agents/orchestrator.md` (agent instructions)
- [ ] `coacoa/workflows/*.yml` (workflow definitions)
- [ ] `coacoa/tasks/` (task methodology directory)
- [ ] `coacoa/quality/anti_hallucination.md` (validation checklist)
- [ ] `coacoa/quality/link_integrity.md` (reference validation)

**IF ANY FILE IS MISSING:** Stop and report "❌ VALIDATION FAILED: Framework not properly installed - run 'coacoa init' first"
**ONLY PROCEED** if all framework files confirmed present.

## INSTRUCTION
As an orchestrator agent you **MUST** follow the instructions **EXACTLY** as in **Path:** `coacoa/agents/orchestrator.md`