# Build-Integrity Checklist
_Applies to: Dev · QA · Orchestrator_

| B-1 | `build_info.json` exists and parses. |
| B-2 | All commands in `build_info.commands.*` execute with exit-code 0. |
| B-3 | Lint command prints **0 errors**. |
| B-4 | Test command produces coverage report consumed by QA checklist. |
| B-5 | Story branch exists and is **ahead 1+ staged file(s)** but has 0 commits. |
| B-6 | All build commands executed inside the project's `.venv/` interpreter. |