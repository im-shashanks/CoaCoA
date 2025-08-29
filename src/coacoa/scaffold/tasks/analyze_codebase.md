# Task · analyze_codebase (Unified Workflow)

## Assigned to: code-explorer agent

> **Objective**  
> Execute comprehensive enterprise codebase analysis using unified methodology. Single entry point for both Claude Code (parallel) and Cline (sequential) workflows, with intelligent execution mode detection and comprehensive planning phase.

---

## 0 · Execution Mode Detection

**Automatic Mode Selection:**
- **Claude Code**: If Task tool available → Parallel execution mode
- **Cline**: If Task tool unavailable → Sequential execution mode

**Configuration Reading:**
- Load `{{cfg.analysis}}` settings from `coacoa.yaml`
- Apply enterprise mode settings if enabled
- Initialize central analysis directory structure

---

## 1 · Comprehensive Planning Phase

### 1.1 · Generate Master Analysis Plan

1. **Invoke Planning Template:**
   - Use `templates/codebase_analysis_master.md` to generate detailed plan
   - Plan contains complete methodology for each analysis phase
   - Each phase has self-contained instructions and output specifications

2. **Repository Assessment:**
   - Scan repository structure and estimate scope
   - Detect primary languages, build systems, and architecture patterns
   - Calculate estimated analysis duration and resource requirements

3. **Plan Customization:**
   - Adapt plan based on detected technologies and repository size
   - Add enterprise-specific phases if `coa.analysis.enterprise_mode` enabled
   - Set priority levels based on repository characteristics

4. **Create Central Plan:**
   - Write comprehensive plan to `coacoa/context/analysis/plan.md`
   - Include detailed task breakdown with complete instructions
   - Initialize progress tracking system

### 1.2 · Directory Structure Setup

```
coacoa/context/analysis/
├── plan.md                    # Master plan with progress tracking
├── artifacts/                 # JSON intelligence outputs
│   ├── repo-intelligence.json
│   ├── build-info.json
│   ├── architecture.json
│   ├── dependencies.json
│   ├── complexity.json
│   ├── security-analysis.json
│   ├── git-analysis.json
│   └── performance-analysis.json
├── reports/                   # Individual phase analysis reports
│   ├── task-001-analysis.md
│   ├── task-002-analysis.md
│   └── ...
└── consolidated/              # Final consolidated outputs
    ├── executive-summary.md
    └── recommendations.md
```

---

## 2 · Execution Mode Routing

### 2.1 · Claude Code: Parallel Execution Mode

**Prerequisites:**
- Verify Task tool availability
- Confirm plan.md exists with complete task breakdown
- Initialize progress monitoring system

**Parallel Task Orchestration:**
1. **Parse Analysis Plan:**
   - Extract individual tasks from `plan.md`
   - Identify dependencies and execution order
   - Prepare task-specific contexts from plan sections

2. **Launch Parallel Tasks:**
   ```
   For each task in analysis_plan.tasks:
     Use Task tool with:
     - description: "Execute {task.name}"
     - subagent_type: "general-purpose" 
     - prompt: """
       You are executing {task.name} from the comprehensive codebase analysis plan.
       
       Complete Instructions:
       {task.detailed_instructions_from_plan}
       
       Required Outputs:
       - Artifact: {task.output_artifact}
       - Report: {task.output_report}
       
       Upon completion:
       1. Create both required output files
       2. Update status in plan.md: "✅ {task.name} Complete"
       3. Return "COMPLETED {task.name}"
       """
   ```

3. **Progress Monitoring:**
   - Monitor plan.md for task completion status updates
   - Validate required outputs are created for each completed task
   - Handle task failures and retry logic

4. **Completion Detection:**
   - When all tasks show "✅ Complete" status in plan.md
   - Verify all artifacts and reports exist
   - Proceed to consolidation phase

### 2.2 · Cline: Sequential Execution Mode

**Prerequisites:**
- Confirm plan.md exists with complete task breakdown
- Initialize sequential task state tracking

**Sequential Task Execution:**
1. **Current Task Selection:**
   - Find first task in plan.md with "⏳ Pending" status
   - If no pending tasks exist, proceed to consolidation

2. **Task Context Preparation:**
   - Extract complete instructions from plan section
   - Prepare self-contained task context (no external dependencies)
   - Set current task status to "🔄 In Progress" in plan.md

3. **Task Execution:**
   - Execute current task using instructions from plan
   - Create required artifact and report files
   - Update task status to "✅ Complete" in plan.md

4. **Next Task Creation Protocol:**
   ```markdown
   Upon task completion, ALWAYS follow this protocol:
   
   a) **Check Plan Status:**
      - Scan plan.md for next task with "⏳ Pending" status
      - If found: Create next task
      - If none: Proceed to final consolidation
   
   b) **Create Next Task:**
      I have completed {current_phase_name}.
      
      Next phase: {next_phase_name}
      
      **New Task Creation:**
      Please execute Phase {N}: {next_phase_name}
      
      **Complete Instructions:**
      Follow detailed methodology in plan.md section "{next_phase_section}"
      
      **Required Outputs:**
      - Artifact: {artifact_path}
      - Report: {report_path}
      
      **Upon Completion:**
      1. Create both required output files
      2. Update plan.md: mark phase as "✅ Complete"
      3. Create next task following this same protocol
      4. If no more phases, proceed to consolidation
      
      **Context Reference:**
      - Master plan: coacoa/context/analysis/plan.md
      - Progress: Phase {N-1} complete → Phase {N} starting
      - All instructions self-contained in plan
   
   c) **Consolidation Trigger:**
      If all 7 analysis phases complete, create final consolidation task:
      
      "All analysis phases complete. Execute final consolidation phase using plan.md section 'Phase 8: Final Consolidation'."
   ```

5. **Error Handling:**
   - If task fails: Update plan.md with failure status and reason
   - Create retry task or escalate to user based on failure type
   - Maintain progress tracking through failures

---

## 3 · Consolidation Phase

### 3.1 · Artifact Validation
- **JSON Validation:** Ensure all artifact files parse correctly
- **Schema Compliance:** Validate against defined schemas in plan
- **Completeness Check:** Verify all required fields populated
- **Cross-Reference Validation:** Check consistency between artifacts

### 3.2 · Executive Summary Generation
1. **Risk Assessment Aggregation:**
   - Compile critical, high, medium, low priority findings
   - Calculate repository health score (0-100)
   - Identify immediate action items

2. **Executive Dashboard Creation:**
   - Repository statistics and technology summary
   - Architecture and dependency analysis highlights
   - Security and compliance status overview
   - Quality metrics and technical debt assessment

3. **Actionable Recommendations:**
   - Prioritized improvement roadmap
   - Resource requirements and time estimates  
   - Team assignment suggestions
   - Implementation sequence recommendations

### 3.3 · Final Output Assembly
- **Consolidated Executive Summary:** `consolidated/executive-summary.md`
- **Detailed Recommendations:** `consolidated/recommendations.md`
- **Artifact Index:** `consolidated/artifact-index.json`
- **Analysis Metadata:** `consolidated/analysis-metadata.json`

---

## 4 · Quality Gates & Validation

### 4.1 · Comprehensive Validation Checklist
- [ ] All planned tasks completed successfully
- [ ] Required artifacts present and valid
- [ ] Analysis reports comprehensive and specific
- [ ] Executive summary actionable and clear
- [ ] No hallucinated information (all findings evidence-based)
- [ ] Proper risk prioritization and categorization

### 4.2 · Success Criteria
- Repository health score calculated
- All critical issues identified and documented
- Actionable recommendations provided with priorities
- Executive summary suitable for technical leadership

---

## 5 · Completion Protocol

**Success Return Message:**
```
COMPLETED analyze_codebase

✅ Comprehensive analysis complete
📊 Repository health score: {score}/100  
🔍 {critical_count} critical issues found
📋 {total_recommendations} recommendations generated
📁 Results available in: coacoa/context/analysis/consolidated/
```

**Failure Return Message:**
```
FAILED analyze_codebase: {specific_reason}

❌ Analysis incomplete: {failure_details}
🔧 Required actions: {remediation_steps}
📁 Partial results available in: coacoa/context/analysis/
```

---

## 6 · Enterprise Integration Notes

**Large Repository Handling:**
- Automatic scope reduction for repositories > 100K files
- Progressive analysis with summary-first approach
- Resource-aware batch sizing based on available context

**Enterprise Security:**
- Credential scanning with enterprise patterns
- Compliance framework integration
- Internal package recognition and analysis

**Quality Assurance:**
- Anti-hallucination validation at each phase
- Evidence-based findings requirement
- Cross-validation between analysis phases

This unified workflow provides enterprise-grade codebase analysis through a single, consistent interface while optimizing execution for each tool's capabilities.