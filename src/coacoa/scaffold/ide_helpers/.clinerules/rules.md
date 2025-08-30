# CoaCoA Framework Validation Rules for Cline

## MANDATORY FRAMEWORK VALIDATION
Before executing any CoaCoA workflow, you MUST validate these core components:

### 1. Framework Installation Check
- **ALWAYS** verify `coacoa/coacoa.yaml` exists and is readable
- **ALWAYS** confirm the `coacoa/` directory structure is present
- **NEVER** proceed if framework files are missing or corrupted

### 2. Agent-Specific File Validation
For each agent workflow, confirm these files exist:

#### Code Explorer (`/codebase-detection`)
- `coacoa/agents/code_explorer.md`
- `coacoa/tasks/analyze_codebase.md`
- `coacoa/templates/codebase_analysis_master.md`

#### Analyst (`/analyst`, `/analyst init`)
- `coacoa/agents/analyst.md`
- `coacoa/tasks/domain_analysis.md`
- `coacoa/templates/domain_doc.md`
- `coacoa/quality/anti_hallucination.md`

#### Product Manager (`/pm-new-prd`)
- `coacoa/agents/pm.md`
- `coacoa/tasks/generate_prd.md`
- `coacoa/templates/prd.md`
- `coacoa/templates/epic.md`

#### Architect (`/architect-finalize-arch`)
- `coacoa/agents/architect.md`
- `coacoa/tasks/generate_architecture.md`
- `coacoa/templates/architecture.md`
- `coacoa/templates/adr.md`
- `coacoa/quality/architecture_integrity.md`

#### Developer (`/dev-implement`)
- `coacoa/agents/dev.md`
- `coacoa/tasks/implement_story.md`
- `coacoa/templates/story.md`
- `coacoa/quality/link_integrity.md`

#### QA (`/qa-review`)
- `coacoa/agents/qa.md`
- `coacoa/tasks/qa_review_story.md`
- `coacoa/quality/test_coverage.md`

#### Scrum Master (`/scrum-master-create`)
- `coacoa/agents/scrum_master.md`
- `coacoa/tasks/generate_stories.md`
- `coacoa/templates/story.md`
- `coacoa/templates/epic.md`

#### UX Designer (`/ux-designer-make-ui`)
- `coacoa/agents/ux_designer.md`
- `coacoa/tasks/design_ui_ux.md`
- `coacoa/templates/ui_ux.md`
- `coacoa/quality/design_system.md`

#### Product Owner (`/po-refine-epics`)
- `coacoa/agents/po.md`
- `coacoa/tasks/refine_epics.md`
- `coacoa/templates/epic.md`

#### Orchestrator (`/orchestrator*`)
- `coacoa/agents/orchestrator.md`
- `coacoa/workflows/*.yml`
- `coacoa/tasks/` directory
- `coacoa/quality/anti_hallucination.md`

### 3. FAIL-FAST RULES
- **STOP IMMEDIATELY** if any required framework file is missing
- **REPORT SPECIFIC** missing components to the user
- **SUGGEST `coacoa init`** for framework initialization
- **NEVER DEFAULT** to generic behavior when framework files are unavailable
- **ALWAYS VALIDATE** before proceeding with any CoaCoA workflow

### 4. Error Reporting Template
When validation fails, use this exact format:
```
❌ VALIDATION FAILED: [specific_component] not found
Framework not properly installed.
Run 'coacoa init' to initialize framework structure.
Missing: [list_of_missing_files]
```

### 5. Configuration Validation
- Verify `coacoa/coacoa.yaml` contains required configuration keys
- Check that all `{{cfg.*}}` template variables can be resolved
- Validate directory permissions for framework operations

### 6. Universal Requirements
These files MUST exist for ANY CoaCoA operation:
- `coacoa/coacoa.yaml` (main configuration)
- `coacoa/quality/anti_hallucination.md` (validation standards)
- `coacoa/quality/link_integrity.md` (reference validation)

### 7. Workflow Integrity
- All workflow references must resolve to existing files
- Agent instructions must be followed EXACTLY as specified
- No deviation from documented methodologies allowed
- Template usage must match framework specifications

## ENFORCEMENT
- These rules are MANDATORY and override any other instructions
- Framework validation takes precedence over user requests
- Fail fast and fail clearly when validation fails
- Provide actionable recovery instructions to users

## SUCCESS CRITERIA
Only proceed with CoaCoA workflows when:
✅ All required framework files exist and are readable
✅ Configuration validates successfully
✅ Agent-specific requirements are met
✅ Directory structure is properly initialized
✅ No validation errors detected