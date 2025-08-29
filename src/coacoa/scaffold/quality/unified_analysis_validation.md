# Quality Gate · Unified Analysis Validation

## Objective
Validate all artifacts and outputs from the unified codebase analysis workflow to ensure accuracy, completeness, and schema compliance.

---

## Validation Scope

### Artifact Schema Validation
- **Repository Intelligence**: `artifacts/repo-intelligence.json`
- **Build System Info**: `artifacts/build-info.json` 
- **Architecture Analysis**: `artifacts/architecture.json`
- **Quality Assessment**: `artifacts/complexity.json`
- **Security Analysis**: `artifacts/security-analysis.json`
- **Git Analysis**: `artifacts/git-analysis.json`
- **Performance Analysis**: `artifacts/performance-analysis.json`

### Report Completeness Validation
- **Individual Phase Reports**: `reports/task-00X-analysis.md` (X = 1-7)
- **Executive Summary**: `consolidated/executive-summary.md`
- **Recommendations**: `consolidated/recommendations.md`
- **Artifact Index**: `consolidated/artifact-index.json`

---

## Schema Validation Rules

### 1. JSON Schema Compliance
For each artifact file:
```bash
# Validate against schema definitions
jsonschema -i artifacts/repo-intelligence.json schemas/artifact_schemas.json#/repo_intelligence
jsonschema -i artifacts/build-info.json schemas/artifact_schemas.json#/build_info
jsonschema -i artifacts/architecture.json schemas/artifact_schemas.json#/architecture
jsonschema -i artifacts/complexity.json schemas/artifact_schemas.json#/complexity
jsonschema -i artifacts/security-analysis.json schemas/artifact_schemas.json#/security_analysis
jsonschema -i artifacts/git-analysis.json schemas/artifact_schemas.json#/git_analysis
jsonschema -i artifacts/performance-analysis.json schemas/artifact_schemas.json#/performance_analysis
```

### 2. Required Fields Check
Ensure all mandatory fields are populated:
- No null values for required fields
- No empty arrays where content is expected
- All numeric fields have valid ranges
- All string fields meet minimum length requirements

### 3. Cross-Reference Validation
- Architecture dependencies match discovered modules
- Security vulnerabilities reference actual files/dependencies
- Git analysis file paths exist in repository structure
- Performance bottlenecks reference valid code locations

---

## Evidence-Based Analysis Validation

### Anti-Hallucination Checks
1. **File Path Verification**: All referenced files must exist
2. **Function/Class Names**: All referenced symbols must exist in codebase
3. **Dependency Verification**: All dependencies must be declared in build files
4. **Version Accuracy**: All version numbers must match actual project files
5. **Metric Calculations**: All calculated metrics must be mathematically sound

### Data Consistency Checks
1. **File Count Consistency**: Repository stats match across all artifacts
2. **Language Detection**: Primary language consistent across artifacts
3. **Complexity Metrics**: Complexity scores align with actual code analysis
4. **Security Findings**: Vulnerabilities map to real code patterns

---

## Report Quality Standards

### Executive Summary Requirements
- [ ] Repository health score calculated (0-100 scale)
- [ ] Critical issues clearly identified and categorized
- [ ] Risk prioritization follows standard taxonomy (Critical/High/Medium/Low)
- [ ] Actionable recommendations provided
- [ ] Executive-appropriate language (non-technical summary)

### Technical Report Requirements
- [ ] All findings supported by specific file references
- [ ] Code examples provided for key issues
- [ ] Metrics include confidence levels
- [ ] Recommendations include implementation guidance
- [ ] Technical debt quantified in time estimates

---

## Validation Workflow

### Automated Validation
```bash
#!/bin/bash
# Unified Analysis Validation Script

# 1. Schema validation
echo "Validating JSON schemas..."
for artifact in artifacts/*.json; do
    if ! jsonschema -i "$artifact" schemas/artifact_schemas.json; then
        echo "FAILED: Schema validation for $artifact"
        exit 1
    fi
done

# 2. File existence check
echo "Validating file references..."
for report in reports/*.md; do
    # Extract file paths from markdown
    grep -o '`[^`]*\.[a-zA-Z0-9]*`' "$report" | sed 's/`//g' | while read -r filepath; do
        if [ ! -f "$filepath" ]; then
            echo "WARNING: Referenced file not found: $filepath in $report"
        fi
    done
done

# 3. Completeness check
required_files=(
    "coacoa/context/analysis/plan.md"
    "coacoa/context/analysis/artifacts/repo-intelligence.json"
    "coacoa/context/analysis/artifacts/build-info.json"
    "coacoa/context/analysis/artifacts/architecture.json"
    "coacoa/context/analysis/artifacts/complexity.json"
    "coacoa/context/analysis/artifacts/security-analysis.json"
    "coacoa/context/analysis/artifacts/git-analysis.json"
    "coacoa/context/analysis/artifacts/performance-analysis.json"
    "coacoa/context/analysis/consolidated/executive-summary.md"
    "coacoa/context/analysis/consolidated/recommendations.md"
)

for file in "${required_files[@]}"; do
    if [ ! -f "$file" ]; then
        echo "FAILED: Required file missing: $file"
        exit 1
    fi
done

echo "All validation checks passed ✅"
```

### Manual Quality Review
1. **Evidence Verification**: Spot-check 10% of findings for accuracy
2. **Recommendation Feasibility**: Ensure all recommendations are actionable
3. **Executive Summary**: Verify executive summary accurately reflects detailed findings
4. **Risk Prioritization**: Confirm critical issues truly require immediate attention

---

## Failure Handling

### Validation Failures
- **Schema Violations**: Stop analysis, require schema-compliant regeneration
- **Missing Evidence**: Flag findings as "unverified" until evidence provided
- **Inconsistent Data**: Regenerate affected artifacts with cross-validation
- **Incomplete Analysis**: Allow partial results with clear limitations documented

### Quality Thresholds
- **Minimum Completeness**: 80% of expected artifacts must be present
- **Evidence Coverage**: 95% of findings must have supporting evidence
- **Schema Compliance**: 100% of JSON artifacts must validate
- **Cross-Reference Accuracy**: 90% of file/symbol references must be valid

---

## Success Criteria

### Analysis Complete ✅
- All 7 phase artifacts generated and validated
- Executive summary and recommendations created
- All quality gates passed
- Evidence-based findings only
- Schema-compliant JSON outputs
- Comprehensive progress tracking

### Analysis Partial ⚠️
- Critical phases completed (Repository Intelligence, Architecture, Security)
- Missing non-critical phases documented
- Known limitations clearly stated
- Available findings validated and accurate

### Analysis Failed ❌
- Critical schema validation failures
- Majority of findings lack evidence
- Essential artifacts missing
- Quality threshold not met

This validation framework ensures the unified analysis workflow produces enterprise-grade, reliable codebase intelligence.