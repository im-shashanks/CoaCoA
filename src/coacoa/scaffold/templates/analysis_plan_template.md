# Enterprise Codebase Analysis Plan

**Repository**: {{repo_name}}  
**Analysis Scope**: Enterprise Full-Stack Analysis  
**Execution Mode**: {{execution_mode}}  
**Created**: {{timestamp}}  
**Estimated Duration**: {{duration_estimate}}

### Schema Validation Requirements
**CRITICAL**: All JSON artifacts must validate against `coacoa/schemas/artifact_schemas.json`

**Required Artifact-Schema Mappings**:
- `repo-intelligence.json` → `repository_intelligence_schema`
- `build-info.json` → `build_analysis_schema`
- `architecture.json` → `architecture_analysis_schema`
- `complexity.json` → `complexity_analysis_schema`
- `security-analysis.json` → `security_analysis_schema`
- `git-analysis.json` → `git_analysis_schema`
- `performance-analysis.json` → `performance_analysis_schema`

---

## Executive Summary
**Status**: ⏳ Pending Final Consolidation

- **Repository Health Score**: TBD/100
- **Critical Issues Found**: TBD
- **Security Vulnerabilities**: TBD
- **Technical Debt Hours**: TBD
- **Recommended Priority Actions**: TBD

---

## Analysis Progress Overview

| Phase | Status | Artifact | Report | Completion |
|-------|--------|----------|---------|------------|
| 1. Repository Intelligence | ⏳ Pending | `artifacts/repo-intelligence.json` | `reports/task-001-analysis.md` | - |
| 2. Build System Analysis | ⏳ Pending | `artifacts/build-info.json` | `reports/task-002-analysis.md` | - |
| 3. Architecture Analysis | ⏳ Pending | `artifacts/architecture.json` | `reports/task-003-analysis.md` | - |
| 4. Quality Assessment | ⏳ Pending | `artifacts/complexity.json` | `reports/task-004-analysis.md` | - |
| 5. Security Analysis | ⏳ Pending | `artifacts/security-analysis.json` | `reports/task-005-analysis.md` | - |
| 6. Git History Analysis | ⏳ Pending | `artifacts/git-analysis.json` | `reports/task-006-analysis.md` | - |
| 7. Performance Analysis | ⏳ Pending | `artifacts/performance-analysis.json` | `reports/task-007-analysis.md` | - |
| 8. Final Consolidation | ⏳ Pending | `consolidated/executive-summary.md` | `consolidated/recommendations.md` | - |

**Overall Progress**: 0/8 phases complete

---

## Phase 1: Repository Intelligence & Discovery
**Status**: ⏳ Pending  
**Assigned Task**: `task-001-repo-intelligence`  
**Priority**: Critical - Foundation for all subsequent analysis

### Complete Task Instructions:
You are executing **Repository Intelligence & Discovery** analysis. This is the foundation phase that informs all subsequent analysis.

#### Your Specific Objectives:
1. **File System Analysis**: Comprehensive repository structure mapping
2. **Technology Stack Detection**: Primary languages, frameworks, architecture patterns  
3. **Repository Structure Assessment**: Organization patterns and conventions

#### Detailed Methodology:

**Step 1: File Discovery & Classification**
- Scan from repository root (containing `coacoa/` folder)
- Apply enterprise exclusion patterns:
  ```
  Base: .git/, coacoa/, .DS_Store, Thumbs.db, *.tmp
  Standard: **/dist, **/node_modules, **/target, **/build, **/.venv, **/.env*
  Enterprise: **/vendor, **/.terraform, **/coverage, **/reports, **/*.egg-info
  Build Artifacts: **/bazel-*, **/.nx, **/rush-*, **/.rush, **/__pycache__
  Binaries: **/*.jar, **/*.war, **/*.so, **/*.dll, **/*.exe, **/*.zip
  ```

**Step 2: Language & Framework Detection**
- Classify files by language using extensions and content analysis
- Identify framework indicators:
  - Python: Django (settings.py), Flask (app.py), FastAPI (main.py)
  - Node.js: Express, React (package.json), Next.js (next.config.js)
  - Java: Spring (application.properties), Maven/Gradle structure
  - .NET: *.csproj, Program.cs, Startup.cs

**Step 3: Architecture Pattern Recognition**
- **Monolith**: Single deployment unit, shared database
- **Microservices**: Multiple services, API boundaries, separate databases
- **Layered**: Clear separation (presentation, business, data layers)
- **Clean Architecture**: Dependency inversion, domain-centric structure

#### Required Output Schema:
**Artifact**: `artifacts/repo-intelligence.json`
```json
{
  "repository_stats": {
    "total_files": 1247,
    "languages": {"python": 45, "typescript": 32, "java": 15},
    "primary_language": "python",
    "loc_by_language": {"python": 15420, "typescript": 8930},
    "test_coverage_estimate": 0.68,
    "documentation_files": 23
  },
  "technology_stack": {
    "primary_frameworks": ["fastapi", "react", "postgresql"],
    "build_tools": ["poetry", "webpack", "docker"],
    "testing_frameworks": ["pytest", "jest"],
    "architecture_style": "microservices"
  },
  "structure_assessment": {
    "follows_conventions": true,
    "has_tests": true,
    "has_documentation": true,
    "monorepo": false,
    "entry_points": ["src/main.py", "web/index.js"]
  }
}
```

**Report**: `reports/task-001-analysis.md`
- Repository overview and technology summary
- Architecture assessment and recommendations
- File organization analysis
- Foundation recommendations for subsequent phases

#### Completion Checklist:
- [ ] JSON artifact created and validates against schema
- [ ] Analysis report completed with specific findings
- [ ] Technology stack accurately identified
- [ ] Architecture pattern determined
- [ ] Entry points and main components identified

**Upon Completion**: 
1. Update status to "✅ Repository Intelligence Complete"
2. **For Cline users**: Create next task with message: "Repository Intelligence complete. Please execute Phase 2: Build System Analysis using plan.md section 'Phase 2: Build System & Environment Analysis'."

---

## Phase 2: Build System & Environment Analysis
**Status**: ⏳ Pending  
**Assigned Task**: `task-002-build-analysis`  
**Priority**: High - Critical for understanding deployment and development workflow

### Complete Task Instructions:
You are executing **Build System & Environment Analysis**. Focus on understanding how the codebase is built, tested, and deployed.

#### Your Specific Objectives:
1. **Build System Detection**: Identify primary and secondary build systems
2. **CI/CD Analysis**: Understand automation and deployment pipelines
3. **Environment Configuration**: Development, staging, production setup
4. **Dependency Management**: Package managers and dependency resolution

#### Detailed Methodology:

**Step 1: Build System Detection (Priority Order)**
1. **Enterprise Build Systems** (check first):
   - Bazel: `WORKSPACE`, `MODULE.bazel`, `BUILD` files
   - Buck/Buck2: `.buckconfig`, `BUCK` files  
   - Rush: `rush.json`, `common/config/rush/`
   - Nx: `nx.json`, `workspace.json`

2. **Standard Build Systems**:
   - Node.js: `package.json`, `yarn.lock`, `package-lock.json`
   - Python: `pyproject.toml` > `setup.py` > `requirements.txt`
   - Java: `pom.xml` (Maven), `build.gradle` (Gradle)
   - Go: `go.mod`, `go.work`

**Step 2: CI/CD Integration Analysis**
- GitHub Actions: `.github/workflows/*.yml`
- GitLab CI: `.gitlab-ci.yml`  
- Jenkins: `Jenkinsfile`
- Azure Pipelines: `azure-pipelines.yml`
- CircleCI: `.circleci/config.yml`

**Step 3: Container & Deployment Analysis**
- Docker: `Dockerfile`, `docker-compose.yml`
- Kubernetes: `k8s/`, `*.yaml` manifests
- Helm: `Chart.yaml`, `values.yaml`
- Terraform: `*.tf` files

#### Required Output Schema:
**Artifact**: `artifacts/build-info.json`
```json
{
  "primary_build_system": {
    "type": "gradle",
    "version": "8.2",
    "detected_files": ["build.gradle.kts", "settings.gradle.kts"],
    "multi_module": true,
    "modules": [
      {"name": "api", "path": "modules/api", "type": "library"},
      {"name": "web", "path": "modules/web", "type": "application"}
    ],
    "commands": {
      "build": "./gradlew build",
      "test": "./gradlew test",
      "lint": "./gradlew checkstyleMain",
      "run": "./gradlew :web:bootRun"
    }
  },
  "ci_cd": {
    "platforms": ["github-actions", "docker"],
    "build_stages": ["compile", "test", "package", "deploy"],
    "deployment_targets": ["staging", "production"],
    "quality_gates": ["unit-tests", "integration-tests", "security-scan"]
  }
}
```

#### Completion Checklist:
- [ ] Primary build system identified and analyzed
- [ ] CI/CD pipeline configuration understood
- [ ] Container/deployment strategy documented
- [ ] Build commands and workflows validated

**Upon Completion**: 
1. Update status to "✅ Build System Analysis Complete"
2. **For Cline users**: Create next task: "Build System Analysis complete. Please execute Phase 3: Architecture & Dependency Analysis using plan.md section 'Phase 3: Architecture & Dependency Analysis'."

---

## Phase 3: Architecture & Dependency Analysis  
**Status**: ⏳ Pending  
**Assigned Task**: `task-003-architecture-analysis`  
**Priority**: Critical - Core structural understanding

### Complete Task Instructions:
You are executing **Architecture & Dependency Analysis**. This phase maps the internal structure and dependencies of the codebase.

#### Your Specific Objectives:
1. **Module Mapping**: Identify all components, classes, and functions
2. **Dependency Analysis**: Internal and external dependencies
3. **Architecture Assessment**: Layer violations, circular dependencies
4. **Design Pattern Recognition**: Enterprise patterns and anti-patterns

#### Required Output Schema:
**Artifact**: `artifacts/architecture.json`
```json
{
  "modules": {
    "src.services.payment": {
      "file_path": "src/services/payment.py",
      "components": [
        {
          "type": "class",
          "name": "PaymentService", 
          "line_range": [15, 89],
          "public_methods": ["process_payment", "refund_payment"]
        }
      ],
      "dependencies": ["src.models.payment", "external.stripe"]
    }
  },
  "dependency_graph": {
    "internal_dependencies": [
      {
        "from": "src.services.payment",
        "to": "src.models.payment",
        "type": "import",
        "coupling_strength": 0.7
      }
    ],
    "external_dependencies": [
      {
        "name": "stripe",
        "version": "5.4.0",
        "usage_locations": ["src/services/payment.py"]
      }
    ]
  }
}
```

#### Completion Checklist:
- [ ] Module map created with all major components
- [ ] Dependency graph generated (internal and external)
- [ ] Circular dependencies identified
- [ ] Architecture patterns documented

**Upon Completion**: 
1. Update status to "✅ Architecture Analysis Complete"
2. **For Cline users**: Create next task: "Architecture Analysis complete. Please execute Phase 4: Quality & Complexity Assessment using plan.md section 'Phase 4: Quality & Complexity Assessment'."

---

## Phase 4: Quality & Complexity Assessment
**Status**: ⏳ Pending  
**Assigned Task**: `task-004-quality-analysis`  
**Priority**: High - Technical debt and maintainability assessment

### Complete Task Instructions:
You are executing **Quality & Complexity Assessment**. Focus on code quality metrics and technical debt identification.

#### Required Output Schema:
**Artifact**: `artifacts/complexity.json`
```json
{
  "file_metrics": {
    "src/services/payment.py": {
      "cyclomatic_complexity": 18,
      "maintainability_index": 54.2,
      "lines_of_code": 245,
      "complexity_level": "high",
      "technical_debt_minutes": 45
    }
  },
  "quality_summary": {
    "high_complexity_files": 12,
    "technical_debt_hours": 23.5,
    "maintainability_score": 6.2
  }
}
```

#### Completion Checklist:
- [ ] Complexity metrics calculated for all major files
- [ ] Technical debt assessment completed
- [ ] Quality gates evaluated
- [ ] Refactoring priorities identified

**Upon Completion**: 
1. Update status to "✅ Quality Assessment Complete"
2. **For Cline users**: Create next task: "Quality Assessment complete. Please execute Phase 5: Security & Compliance Analysis using plan.md section 'Phase 5: Security & Compliance Analysis'."

---

## Phase 5: Security & Compliance Analysis
**Status**: ⏳ Pending  
**Assigned Task**: `task-005-security-analysis`  
**Priority**: Critical - Security vulnerabilities and compliance gaps

### Complete Task Instructions:
You are executing **Security & Compliance Analysis**. Focus on security vulnerabilities, compliance issues, and enterprise security patterns.

#### Required Output Schema:
**Artifact**: `artifacts/security-analysis.json`
```json
{
  "vulnerability_scan": {
    "critical_vulnerabilities": 0,
    "high_vulnerabilities": 2,
    "medium_vulnerabilities": 8,
    "vulnerable_dependencies": [
      {
        "name": "old-package",
        "version": "1.2.0",
        "vulnerability": "CVE-2023-12345",
        "severity": "high"
      }
    ]
  },
  "compliance_assessment": {
    "license_compliance": "compliant",
    "security_policies": "partial",
    "data_handling": "compliant"
  }
}
```

#### Completion Checklist:
- [ ] Dependency vulnerabilities scanned
- [ ] Code security patterns analyzed
- [ ] Compliance framework assessment
- [ ] Security recommendations generated

**Upon Completion**: 
1. Update status to "✅ Security Analysis Complete"
2. **For Cline users**: Create next task: "Security Analysis complete. Please execute Phase 6: Git History & Risk Analysis using plan.md section 'Phase 6: Git History & Risk Analysis'."

---

## Phase 6: Git History & Risk Analysis
**Status**: ⏳ Pending  
**Assigned Task**: `task-006-git-analysis`  
**Priority**: Medium - Team collaboration and knowledge risk assessment

### Complete Task Instructions:
You are executing **Git History & Risk Analysis**. Focus on understanding development patterns, team collaboration, and knowledge risks.

#### Required Output Schema:
**Artifact**: `artifacts/git-analysis.json`
```json
{
  "repository_activity": {
    "commit_frequency": 45.2,
    "active_contributors": 8,
    "bus_factor": 3.2,
    "knowledge_concentration": 0.67
  },
  "hotspot_analysis": {
    "high_churn_files": [
      {
        "file": "src/services/payment.py",
        "churn_score": 87,
        "complexity": 22,
        "risk_level": "high"
      }
    ]
  }
}
```

#### Completion Checklist:
- [ ] Commit patterns analyzed
- [ ] Knowledge risks identified
- [ ] Team collaboration patterns documented
- [ ] Code hotspots identified

**Upon Completion**: 
1. Update status to "✅ Git Analysis Complete"
2. **For Cline users**: Create next task: "Git Analysis complete. Please execute Phase 7: Performance & Scalability Assessment using plan.md section 'Phase 7: Performance & Scalability Assessment'."

---

## Phase 7: Performance & Scalability Assessment
**Status**: ⏳ Pending  
**Assigned Task**: `task-007-performance-analysis`  
**Priority**: Medium - Performance bottlenecks and scalability issues

### Complete Task Instructions:
You are executing **Performance & Scalability Assessment**. Focus on identifying performance bottlenecks and scalability concerns.

#### Required Output Schema:
**Artifact**: `artifacts/performance-analysis.json`
```json
{
  "performance_assessment": {
    "algorithmic_complexity_issues": 3,
    "database_query_concerns": 5,
    "memory_usage_patterns": "acceptable",
    "scalability_readiness": 7
  },
  "bottlenecks": [
    {
      "location": "src/services/data_processor.py:45",
      "issue": "O(n²) algorithm in large dataset processing",
      "impact": "high"
    }
  ]
}
```

#### Completion Checklist:
- [ ] Algorithmic complexity analyzed
- [ ] Database access patterns reviewed
- [ ] Scalability patterns assessed
- [ ] Performance recommendations generated

**Upon Completion**: 
1. Update status to "✅ Performance Analysis Complete"
2. **For Cline users**: Create final task: "Performance Analysis complete. All analysis phases finished. Please execute Phase 8: Final Consolidation using plan.md section 'Phase 8: Final Consolidation & Executive Summary'."

---

## Phase 8: Final Consolidation & Executive Summary
**Status**: ⏳ Pending  
**Assigned Task**: `task-008-consolidation`  
**Priority**: Critical - Executive summary and actionable recommendations

### Complete Task Instructions:
You are executing **Final Consolidation**. Create executive summary and actionable recommendations based on all previous analysis phases.

#### Required Outputs:
- **Executive Summary**: `consolidated/executive-summary.md`
- **Recommendations**: `consolidated/recommendations.md`
- **Artifact Index**: `consolidated/artifact-index.json`

#### Completion Checklist:
- [ ] All phase artifacts consolidated
- [ ] Repository health score calculated
- [ ] Executive summary created for leadership
- [ ] Prioritized recommendations generated
- [ ] Implementation roadmap provided

**Upon Completion**: 
1. Update status to "✅ Analysis Complete" - Full analysis finished.
2. **Task chain complete** - No further tasks needed. Analysis workflow finished.

---

## Notes & Context

**Repository Context**:
- Repository size: {{file_count}} files
- Primary languages: {{primary_languages}}
- Enterprise mode: {{enterprise_mode}}

**Quality Gates**:
- All findings must be evidence-based
- No hallucinated information allowed
- Cross-validation between phases required

**Progress Tracking**:
- Update status in this file after each phase completion
- Verify all required outputs before marking complete
- Report any blocking issues immediately