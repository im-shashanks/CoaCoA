# THIS COMMAND IS FOR QUALITY ASSURANCE REVIEW. YOU MUST FOLLOW INSTRUCTIONS EXACTLY AS GIVEN. DO NOT DEVIATE FROM THE PROCESS.

## MANDATORY PRE-EXECUTION CHECKLIST
Before executing this command, CONFIRM these files exist and are readable:
- [ ] `coacoa/coacoa.yaml` (framework configuration)
- [ ] `coacoa/agents/qa.md` (agent instructions)
- [ ] `coacoa/tasks/qa_review_story.md` (QA review methodology)
- [ ] `coacoa/quality/test_coverage.md` (testing standards)
- [ ] `coacoa/quality/anti_hallucination.md` (validation checklist)
- [ ] `coacoa/quality/link_integrity.md` (code reference validation)

**IF ANY FILE IS MISSING:** Stop and report "❌ VALIDATION FAILED: Framework not properly installed - run 'coacoa init' first"
**ONLY PROCEED** if all framework files confirmed present.

## INSTRUCTION
As a qa agent you **MUST** follow the instructions **EXACTLY** as in **Path:** `coacoa/agents/qa.md`