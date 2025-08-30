# Progress Tracking Template

### Schema Validation Protocol
**Before marking any task complete**: Validate all generated JSON artifacts against `coacoa/schemas/artifact_schemas.json`

## Status Update Instructions

This template provides standardized status update patterns for maintaining consistency across both Claude Code and Cline workflows.

### Status Icons and Meanings

| Icon | Status | Meaning |
|------|--------|---------|
| ⏳ | Pending | Task not yet started, waiting for execution |
| 🔄 | In Progress | Task currently being executed |
| ✅ | Complete | Task successfully completed with all outputs generated |
| ❌ | Failed | Task failed, requires attention or retry |
| ⚠️ | Blocked | Task blocked by external dependency or issue |
| 🔄 | Retry | Task being retried after initial failure |

### Standard Status Update Format

**For Task Completion:**
```markdown
| Phase | Status | Artifact | Report | Completion |
|-------|--------|----------|---------|------------|
| 1. Repository Intelligence | ✅ Complete | `artifacts/repo-intelligence.json` | `reports/task-001-analysis.md` | 2025-08-29 14:30 |
```

**For Task Progress:**
```markdown
| Phase | Status | Artifact | Report | Completion |
|-------|--------|----------|---------|------------|
| 2. Build System Analysis | 🔄 In Progress | `artifacts/build-info.json` | `reports/task-002-analysis.md` | - |
```

**For Task Failure:**
```markdown
| Phase | Status | Artifact | Report | Completion |
|-------|--------|----------|---------|------------|
| 3. Architecture Analysis | ❌ Failed | `artifacts/architecture.json` | `reports/task-003-analysis.md` | Error: Missing AST parser |
```

### Progress Percentage Calculation

```
Overall Progress = (Completed Phases / Total Phases) × 100
```

Standard phases count: 8 (including consolidation)

### Executive Summary Updates

**During Analysis:**
```markdown
## Executive Summary
**Status**: 🔄 Analysis in Progress (Phase X of 8)

- **Repository Health Score**: In Progress...
- **Critical Issues Found**: TBD
- **Security Vulnerabilities**: Scanning...
- **Technical Debt Hours**: Calculating...
- **Recommended Priority Actions**: Pending analysis completion
```

**Upon Completion:**
```markdown
## Executive Summary
**Status**: ✅ Analysis Complete

- **Repository Health Score**: 73/100
- **Critical Issues Found**: 3
- **Security Vulnerabilities**: 2 High, 5 Medium
- **Technical Debt Hours**: 42.5
- **Recommended Priority Actions**: Security fixes, refactor payment service
```

### Failure Handling Templates

**For Recoverable Failures:**
```markdown
## Phase X: [Phase Name]
**Status**: 🔄 Retry (Attempt 2/3)
**Issue**: [Brief description of the issue]
**Action**: [What is being done to resolve it]
```

**For Blocking Issues:**
```markdown
## Phase X: [Phase Name]  
**Status**: ⚠️ Blocked
**Blocker**: [Description of blocking issue]
**Required Action**: [What needs to be done to unblock]
**Impact**: [How this affects subsequent phases]
```

### Artifact Validation Checklist

Before marking a phase as complete, verify:

- [ ] Required JSON artifact exists and is valid
- [ ] Analysis report exists and contains specific findings
- [ ] Artifact follows the defined schema
- [ ] No placeholder or "TBD" values in critical fields
- [ ] Status updated in plan.md with timestamp

### Context Handoff Template (For Cline Sequential Mode)

**Context Package for Next Task:**
```markdown
### Context for Next Task: [Task Name]

**Current Status**: Phase X complete, proceeding to Phase Y
**Key Findings from Previous Phase**: 
- [Specific finding 1]
- [Specific finding 2]
- [Specific finding 3]

**Artifacts Available**:
- [List of generated artifacts with brief description]

**Plan Section to Execute**: 
- Reference to specific section in plan.md
- All instructions self-contained in plan

**Expected Outputs**:
- Artifact: [specific file path]
- Report: [specific file path]
```

### Quality Gate Validation

**Before Phase Completion:**
1. **Artifact Quality**: JSON validates against schema
2. **Report Quality**: Contains specific, actionable findings
3. **Evidence-Based**: All claims supported by code analysis
4. **No Hallucination**: No invented or assumed information
5. **Completeness**: All required schema fields populated

### Final Consolidation Triggers

**Claude Code (Parallel Mode):**
- All phase statuses show "✅ Complete" 
- All required artifacts exist and validate
- Progress tracker shows 100% completion

**Cline (Sequential Mode):**
- Current phase is "8. Final Consolidation"
- All previous phases marked complete
- Sequential execution reached end of task list

### Emergency Procedures

**For Critical Failures:**
1. Mark phase as "❌ Failed" with specific error
2. Document failure reason and attempted solutions
3. Assess impact on subsequent phases
4. Determine if analysis can continue with partial results

**For Partial Analysis:**
If analysis cannot complete fully, provide partial results with:
- Clear documentation of what was completed
- Identification of missing components
- Risk assessment of incomplete analysis
- Recommendations for completing analysis later

This progress tracking system ensures consistency, visibility, and reliability across both Claude Code and Cline execution modes.