# Template · Error Handling for Unified Analysis Workflow

## Objective
Standardized error handling patterns and recovery procedures for the unified codebase analysis workflow, ensuring graceful degradation and clear user guidance.

---

## Error Categories

### 1. Pre-Analysis Errors
**Context**: Issues during planning and setup phase

#### Tool Detection Failures
```markdown
**Error**: Unable to detect execution mode (Task tool availability unclear)
**Recovery**: 
- Default to sequential (Cline) mode
- Notify user of mode selection: "Defaulting to sequential mode. Use Claude Code for parallel execution."
- Proceed with sequential workflow
```

#### Repository Structure Issues  
```markdown
**Error**: Repository root not found or coacoa/ directory missing
**Recovery**:
- Return: "FAILED analyze_codebase: Repository not initialized. Run 'coacoa init' first."
- Provide setup guidance
- Exit workflow
```

#### Configuration Errors
```markdown
**Error**: coacoa.yaml malformed or missing required settings
**Recovery**:
- Use framework defaults from scaffold/coacoa.yaml  
- Log warning: "Using default configuration due to: {specific_error}"
- Continue with defaults
```

### 2. Planning Phase Errors

#### Template Access Issues
```markdown
**Error**: Cannot read codebase_analysis_master.md or analysis_plan_template.md
**Recovery**:
- Return: "FAILED analyze_codebase: Analysis templates corrupted. Reinstall framework."
- Provide reinstall guidance: "Run 'pip install --force-reinstall git+https://github.com/im-shashanks/CoaCoA.git'"
- Exit workflow
```

#### Directory Creation Failures
```markdown
**Error**: Cannot create coacoa/context/analysis/ directory structure
**Recovery**:
- Check permissions and disk space
- Return: "FAILED analyze_codebase: Cannot create analysis directories. Check permissions."
- Suggest: "Ensure write access to project directory"
- Exit workflow
```

### 3. Execution Phase Errors

#### Claude Code Parallel Mode Errors
```markdown
**Error**: Task tool failure or agent non-response
**Recovery Pattern**:
1. Wait for timeout (default 10 minutes per task)
2. Check task status in plan.md
3. For failed tasks: 
   - Mark as "❌ Failed: {reason}" in plan.md
   - Log failure details
   - Continue with remaining tasks
4. For non-critical failures (Performance, Git Analysis):
   - Mark as "⚠️ Partial: {reason}" 
   - Generate partial results
   - Continue workflow
5. For critical failures (Repository Intelligence, Security):
   - Return: "FAILED analyze_codebase: Critical analysis failed - {specific_task}"
   - Provide partial results if available
   - Exit workflow
```

#### Cline Sequential Mode Errors
```markdown
**Error**: Task execution failure mid-workflow  
**Recovery Pattern**:
1. Update plan.md status: "❌ Failed at Phase {N}: {error_reason}"
2. Create recovery task: "Please retry Phase {N} or continue with Phase {N+1}"
3. For critical phase failures:
   - Offer manual retry: "Phase {N} failed. Retry? (y/n/skip)"
   - If skip: Mark as partial and continue
   - If retry: Regenerate task with error context
4. For non-critical failures:
   - Auto-continue to next phase
   - Mark as "⚠️ Skipped due to: {reason}"
```

### 4. Analysis Execution Errors

#### File Access Errors
```markdown
**Error**: Cannot read source files during analysis
**Recovery**:
- Skip inaccessible files
- Log in artifacts: "excluded_files": [{"path": "...", "reason": "permission_denied"}]
- Continue analysis with available files  
- Note in report: "Analysis based on {accessible_count}/{total_count} files"
```

#### Token Limit Exceeded
```markdown
**Error**: Analysis scope exceeds context limits
**Recovery**:
1. **Auto-reduction**: Prioritize critical files (config, main modules, tests)
2. **Progressive analysis**: Analyze in order of importance
3. **Summary mode**: Generate high-level insights only
4. Log in artifacts: "analysis_scope": "limited", "reason": "token_constraints"
5. Note in executive summary: "Analysis limited to critical components due to scope"
```

#### Schema Validation Failures
```markdown
**Error**: Generated artifacts don't match expected schemas
**Recovery**:
1. **Auto-correction**: Attempt to fix common schema issues (missing fields, type mismatches)
2. **Partial artifacts**: Generate valid subset of expected schema
3. **Fallback format**: Use simplified schema if complex validation fails
4. Mark artifacts: "schema_compliance": "partial", "validation_errors": [...]
5. Continue workflow with validated portions
```

### 5. Consolidation Errors

#### Missing Artifacts
```markdown
**Error**: Required artifacts missing during consolidation  
**Recovery**:
1. **Graceful degradation**: Generate executive summary with available data
2. **Clear limitations**: Document what analysis could not be completed
3. **Partial scoring**: Calculate repository health score from available metrics
4. **Recommendation focus**: Prioritize recommendations based on successful analysis phases
5. Return: "COMPLETED analyze_codebase (partial): {successful_phases}/{total_phases} phases"
```

#### Report Generation Failures
```markdown
**Error**: Cannot generate executive summary or recommendations
**Recovery**:
1. **Raw data export**: Provide access to individual artifacts
2. **Manual template**: Offer template for manual summary generation  
3. **Status report**: Generate simple status report listing completed analyses
4. Return: "COMPLETED analyze_codebase: Raw analysis data available in artifacts/"
```

---

## Error Response Templates

### User-Facing Error Messages

#### Critical Errors (Workflow Cannot Continue)
```markdown
❌ **Analysis Failed**: {specific_reason}

**What happened**: {technical_explanation}

**Next steps**:
1. {specific_action_1}  
2. {specific_action_2}
3. If issue persists: {contact_info}

**Partial results**: {available_outputs_location}
```

#### Recoverable Errors (Workflow Continues with Limitations)
```markdown
⚠️ **Analysis Partial**: {issue_description}

**Impact**: {what_is_missing}

**Continuing with**: {what_will_proceed}

**To get complete analysis**: {recovery_suggestions}
```

#### Success with Warnings
```markdown
✅ **Analysis Complete** (with limitations)

**Results**: {main_achievements}

**Limitations**: {what_was_skipped_and_why}

**Recommendations**: {how_to_improve_next_time}
```

### Developer-Facing Error Messages

#### Debug Information Structure
```json
{
  "error_id": "unified_analysis_error_001",
  "timestamp": "2025-08-29T10:30:00Z",
  "phase": "execution",
  "task": "Phase 3: Architecture Analysis", 
  "error_type": "file_access_denied",
  "message": "Cannot read source files in src/protected/",
  "context": {
    "execution_mode": "parallel",
    "files_attempted": 127,
    "files_successful": 89,
    "files_failed": 38
  },
  "recovery_action": "continued_with_accessible_files",
  "impact": "architecture_analysis_partial"
}
```

---

## Error Prevention

### Pre-Flight Checks
```bash
# Unified Analysis Pre-Flight Validation
check_repository_structure() {
    [ -d "coacoa/" ] || return 1
    [ -f "coacoa/coacoa.yaml" ] || return 1  
    [ -d "coacoa/tasks/" ] || return 1
    return 0
}

check_permissions() {
    [ -w "." ] || return 1
    [ -w "coacoa/" ] || return 1
    return 0
}

check_disk_space() {
    available=$(df . | awk 'NR==2 {print $4}')
    required=100000  # 100MB in KB
    [ "$available" -gt "$required" ] || return 1
    return 0
}
```

### Graceful Degradation Strategy
1. **Essential vs Optional**: Identify must-have vs nice-to-have analysis components
2. **Progressive Failure**: Continue workflow even if non-critical components fail
3. **Clear Communication**: Always explain what succeeded, what failed, and why
4. **Recovery Guidance**: Provide specific steps to resolve issues or get complete analysis

---

## Monitoring and Logging

### Error Tracking
- Log all errors to `coacoa/context/analysis/error.log`
- Include error context, recovery actions, and impact assessment
- Track error patterns for framework improvement

### Success Metrics
- Analysis completion rate by phase
- Error recovery success rate  
- User satisfaction with error guidance
- Time-to-resolution for common issues

This error handling framework ensures the unified analysis workflow provides reliable, professional results even when facing unexpected issues.