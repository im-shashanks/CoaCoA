# Task Progression Example

This example shows exactly how tasks flow in both Claude Code and Cline modes.

## Claude Code (Parallel Mode) - All Tasks Launched at Once

**Initial Command**: `/analyze-codebase`

**Main Orchestrator Task**:
```
1. Generate comprehensive plan → plan.md
2. Launch ALL 8 tasks simultaneously:
   - Task A: "Execute Phase 1: Repository Intelligence"
   - Task B: "Execute Phase 2: Build System Analysis" 
   - Task C: "Execute Phase 3: Architecture Analysis"
   - Task D: "Execute Phase 4: Quality Assessment"
   - Task E: "Execute Phase 5: Security Analysis"
   - Task F: "Execute Phase 6: Git Analysis"
   - Task G: "Execute Phase 7: Performance Analysis"
   - Task H: "Execute Phase 8: Final Consolidation"
3. Monitor all tasks for completion
4. Return final results when all complete
```

**Key Point**: Main task handles all orchestration, no subtask needs to create other subtasks.

---

## Cline (Sequential Mode) - Chain of Task Creation

**Initial Command**: `/analyze-codebase`

### **Task 1: Main Planning Task**
**What it does**:
- Generate comprehensive plan → plan.md
- Execute Phase 1: Repository Intelligence
- Create next task

**Task 1 Completion Message**:
```
✅ Repository Intelligence analysis complete.

📊 Results:
- Repository has 1,247 Python/TypeScript files
- FastAPI + React architecture detected
- 68% test coverage estimated

📁 Outputs created:
- artifacts/repo-intelligence.json
- reports/task-001-analysis.md

➡️ Next phase: Build System Analysis

**Creating next task**: Please execute Phase 2: Build System Analysis using the detailed instructions in plan.md section "Phase 2: Build System & Environment Analysis".

**Context**: All instructions are self-contained in the plan. No additional context needed.
```

### **Task 2: Build System Analysis**
**What it does**:
- Execute Phase 2: Build System Analysis (using plan.md instructions)
- Create next task

**Task 2 Completion Message**:
```
✅ Build System Analysis complete.

📊 Results:
- Poetry + Docker build system detected
- GitHub Actions CI/CD configured
- 3 deployment environments found

📁 Outputs created:
- artifacts/build-info.json
- reports/task-002-analysis.md

➡️ Next phase: Architecture Analysis

**Creating next task**: Please execute Phase 3: Architecture & Dependency Analysis using the detailed instructions in plan.md section "Phase 3: Architecture & Dependency Analysis".
```

### **Task 3-7: Continue Chain**
Each task follows the same pattern:
1. Execute its phase using plan.md instructions
2. Create outputs
3. Update progress in plan.md
4. Create next task with reference to plan section

### **Task 8: Final Consolidation**
**Task 8 Completion Message**:
```
✅ Final Consolidation complete - Analysis workflow finished.

📊 Executive Summary:
- Repository Health Score: 73/100
- 3 Critical issues found (security vulnerabilities)
- 42.5 hours technical debt estimated
- 15 prioritized recommendations generated

📁 Final Outputs:
- consolidated/executive-summary.md
- consolidated/recommendations.md
- consolidated/artifact-index.json

🎉 **Task chain complete** - No further tasks needed.

All analysis phases finished successfully. Results available in coacoa/context/analysis/consolidated/
```

---

## Key Differences Summary

| Aspect | Claude Code (Parallel) | Cline (Sequential) |
|--------|------------------------|-------------------|
| **Task Creation** | Main orchestrator launches all tasks at once | Each task creates the next task in chain |
| **Context Transfer** | All tasks get complete context from plan | Minimal context - just plan section reference |
| **User Interaction** | Fully automated | User approves each task transition |
| **Failure Handling** | Orchestrator retries failed tasks | Each task handles own failures |
| **Progress Visibility** | All tasks visible immediately | One task at a time, sequential visibility |

## Critical Implementation Detail

**For Cline**: The completion protocol MUST include explicit next task creation:

```markdown
**Upon Completion Instructions (Built into every plan phase):**
1. Update status to "✅ [Phase Name] Complete"
2. **For Cline users**: Create next task with exact message:
   "[Phase] complete. Please execute Phase [N+1]: [Next Phase Name] using plan.md section '[Next Phase Section]'."
```

This ensures the task chain continues automatically until all phases are complete, with user approval at each step.

Without this explicit instruction, the Cline workflow would stop after each task, requiring manual intervention to continue the analysis.