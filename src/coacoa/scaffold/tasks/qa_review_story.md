# Task · qa_review_story
_Assigned to: QA agent_

## Inputs
* Story file (post-Dev)
* Changed code diff (git show)
* Coverage report
* Lint & build logs

## Steps
1. **Re-run build & tests** using `build_info.json`; store fresh coverage %.
2. **Run quality checklists**
   * QA.md sections 1–7
   * Build-Integrity B-1…B-4
   * Anti-Hallucination H-1…H-12
   * Link-Integrity L-1…L-11
3. **Complexity guard** – if any new function `cyclomatic > 20`, reject.
4. **Write QA report** appended to story file:
    ```QA Report

    Verdict: PASS
    Reviewer: 
    Date: YYYY-MM-DD
    Notes: …
    ```
5. If FAIL, set Verdict: FAIL and list blocking items.

Return `COMPLETED qa_review_story` or failure string.