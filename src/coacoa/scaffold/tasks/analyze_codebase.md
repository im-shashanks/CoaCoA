# Task · analyze_codebase (Unified Workflow)

## Assigned to: code-explorer agent

> **Objective**  
> Execute comprehensive enterprise codebase analysis using unified methodology. Generate master plan, execute analysis phases, and produce consolidated intelligence artifacts.

---

## 0 · Configuration

Load `coacoa/coacoa.yaml` for analysis settings:

| Config key                    | Usage                                  |
|-------------------------------|----------------------------------------|
| `coa.paths.analysis_dir`      | Main analysis output directory         |
| `coa.paths.analysis_plan`     | Master plan location                   |
| `coa.paths.analysis_artifacts`| JSON intelligence files directory     |
| `coa.analysis.enterprise_mode`| Enable enterprise-specific features   |
| `coa.analysis.max_file_tokens`| Single file token limit               |

---

## 1 · Generate Master Plan

1. **Create analysis directories:**
   - `coacoa/context/analysis/artifacts/`
   - `coacoa/context/analysis/reports/` 
   - `coacoa/context/analysis/consolidated/`

2. **Use template to generate plan:**
   - Read `templates/codebase_analysis_master.md`
   - Create comprehensive plan at `coacoa/context/analysis/plan.md`
   - Plan contains 7 analysis phases with detailed instructions
   - Each phase specifies required outputs and completion criteria

3. **Repository assessment:**
   - Scan repository structure and estimate scope
   - Detect primary languages, build systems, frameworks
   - Customize plan based on repository characteristics

---

## 2 · Execute Analysis Phases

**For Cline (Sequential Mode):**
Execute phases one at a time based on plan.md:

1. **Find next pending phase** in plan.md (status: "⏳ Pending")
2. **Execute current phase** using instructions from plan.md section
3. **Create required outputs:**
   - Artifact file in `artifacts/` directory
   - Report file in `reports/` directory
4. **Update plan.md** to mark phase as "✅ Complete"
5. **Continue to next phase** or consolidation if all phases complete

**For Claude Code (Sequential Parallel Mode):**

**MANDATORY: Validate Framework Files First**
Before proceeding, confirm these files exist and are readable:
- [ ] `coacoa/coacoa.yaml` (configuration) 
- [ ] `tasks/analyze_codebase.md` (this task file)
- [ ] `templates/codebase_analysis_master.md` (master template)

If any file missing: **STOP** and report "Framework not properly installed"

After generating plan.md, execute phases **one at a time using parallel Task tools**:

1. **Read plan.md** to get detailed phase instructions
2. **Execute phases sequentially with Task tool:**
   - **Phase 1**: Launch Task → Wait for completion → Process results
   - **Phase 2**: Launch Task → Wait for completion → Process results
   - **Phase 3**: Continue this pattern through all 7 phases
3. **Each Task uses general-purpose agent** with specific phase methodology from plan.md
4. **Only 1 Task runs at a time** - wait for completion before next phase

**Phase Execution Protocol (Claude Code):**
For each phase, launch Task with specific instructions:
```
Execute Phase {N}: {phase_name}

Instructions: Follow methodology in plan.md section "{phase_section}"
Outputs: Create {artifact_path} and {report_path}
Wait for completion before proceeding to next phase.
```

**Phase Completion Protocol (Cline only):**
When completing a phase in sequential mode, create next task:
```
Phase {N} complete. 

Execute Phase {N+1}: {next_phase_name}

Instructions: Follow methodology in plan.md section "{next_phase_section}"
Outputs: Create {artifact_path} and {report_path}
```

---

## 3 · Analysis Phases (from plan.md)

1. **Repository Intelligence** → `artifacts/repo-intelligence.json`
2. **Architecture Analysis** → `artifacts/architecture.json`
3. **Dependency Analysis** → `artifacts/dependencies.json`
4. **Complexity Analysis** → `artifacts/complexity.json`
5. **Security Analysis** → `artifacts/security-analysis.json`
6. **Git Analysis** → `artifacts/git-analysis.json`
7. **Performance Analysis** → `artifacts/performance-analysis.json`

Each phase creates both JSON artifact and markdown report.

---

## 4 · Consolidation

When all 7 phases complete:

1. **Validate artifacts:**
   - Check all JSON files parse correctly
   - Verify required fields populated
   - Cross-reference data consistency

2. **Generate executive summary:**
   - Calculate repository health score (0-100)
   - Identify critical issues and priorities
   - Create actionable recommendations

3. **Create consolidated outputs:**
   - `consolidated/executive-summary.md`
   - `consolidated/recommendations.md`
   - `consolidated/analysis-metadata.json`

---

## 5 · Success Criteria

- [ ] All 7 analysis phases completed
- [ ] Required artifacts and reports created
- [ ] Executive summary generated
- [ ] Repository health score calculated
- [ ] No hallucinated information (evidence-based findings only)

**Success message:**
```
COMPLETED analyze_codebase

✅ Analysis complete - 7/7 phases
📊 Repository health: {score}/100
🔍 {critical_count} critical issues found
📁 Results: coacoa/context/analysis/consolidated/
```

---

## Error Handling

- If artifact creation fails → retry once, then log error
- If phase times out → mark as failed in plan.md, continue to next
- If consolidation fails → provide partial results with error details
- Missing dependencies → `/orchestrator fix <artifact>`