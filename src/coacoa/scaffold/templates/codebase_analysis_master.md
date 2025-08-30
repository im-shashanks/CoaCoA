# Master Enterprise Codebase Analysis Template

## Assigned to: code-explorer agent

> **Objective**  
> Create a comprehensive, self-contained analysis plan following enterprise-grade methodology. This plan will serve as the single source of truth for systematic codebase analysis, with each phase containing complete instructions for independent execution.

### Schema Validation Requirements
**CRITICAL**: All artifacts generated during analysis MUST validate against schemas defined in:
- `coacoa/schemas/artifact_schemas.json`

**Artifact-Schema Mappings**:
- `architecture.json` → `architecture_analysis_schema`
- `dependencies.json` → `dependency_analysis_schema`  
- `complexity.json` → `complexity_analysis_schema`
- `git-analysis.json` → `git_analysis_schema`
- `build-info.json` → `build_analysis_schema`
- `team-knowledge.json` → `team_knowledge_schema`

**Validation Protocol**: Before finalizing any artifact, verify it matches the required schema structure. If validation fails, revise the artifact to comply with schema requirements.

---

## Planning Phase: Generate Detailed Analysis Plan

### Plan Structure Template

```markdown
# Enterprise Codebase Analysis Plan

**Repository**: {{repo_name}}  
**Analysis Scope**: Enterprise Full-Stack Analysis  
**Execution Mode**: {{execution_mode}} (Parallel/Sequential)  
**Created**: {{timestamp}}  
**Estimated Duration**: {{duration_estimate}}

---

## Executive Summary
[To be completed after analysis]
- **Repository Health Score**: TBD/100
- **Critical Issues Found**: TBD
- **Recommended Priority Actions**: TBD

---

## Phase 1: Repository Intelligence & Discovery
**Status**: ⏳ Pending  
**Assigned Task**: `task-001-repo-intelligence`  
**Output Files**: `artifacts/repo-intelligence.json`, `reports/task-001-analysis.md`

### Detailed Methodology:
#### 1.1 File System Analysis
**Scan Strategy**:
- Start from repository root (containing `coacoa/` folder)
- Apply enterprise exclusion patterns in this priority order:
  ```
  Base: .git/, coacoa/, .DS_Store, Thumbs.db, *.tmp
  Standard: **/dist, **/node_modules, **/target, **/build, **/.venv, **/.env*
  Enterprise: **/vendor, **/.terraform, **/coverage, **/reports, **/*.egg-info
  Build Artifacts: **/bazel-*, **/.nx, **/rush-*, **/.rush, **/__pycache__
  Binaries: **/*.jar, **/*.war, **/*.so, **/*.dll, **/*.exe, **/*.zip
  ```

**File Classification Protocol**:
- **Language Detection**: Use file extensions with fallback to content analysis
- **Purpose Classification**:
  - `source`: Main application code (src/, lib/, app/)
  - `test`: Test files (*test*, *spec*, test/, tests/, __tests__)
  - `config`: Configuration (*.json, *.yaml, *.toml, *.env, config/)
  - `doc`: Documentation (*.md, docs/, README*, LICENSE*)
  - `build`: Build scripts and configs (Makefile, build.*, *.gradle)

**Metrics Collection**:
```json
{
  "file_path": "src/services/payment.py",
  "language": "python",
  "purpose": "source", 
  "loc": 245,
  "tokens_estimated": 1030,
  "complexity_hint": "medium",
  "is_entry_point": false,
  "framework_indicators": ["fastapi", "sqlalchemy"]
}
```

#### 1.2 Technology Stack Detection
**Primary Detection Targets**:
- **Entry Points**: main.py, index.js, Application.java, main.go, lib.rs
- **Framework Indicators**: 
  - Python: Django (settings.py), Flask (app.py), FastAPI (main.py)
  - Node.js: Express, React (package.json scripts), Next.js (next.config.js)
  - Java: Spring (application.properties), Maven/Gradle structure
  - .NET: *.csproj, Program.cs, Startup.cs

**Architecture Pattern Recognition**:
- **Monolith**: Single deployment unit, shared database
- **Microservices**: Multiple services, API boundaries
- **Layered**: Clear separation (presentation, business, data)
- **Clean Architecture**: Dependency inversion patterns

#### 1.3 Repository Structure Analysis
**Look for Standard Patterns**:
- **Source Organization**: src/, lib/, pkg/, internal/
- **Test Organization**: tests/, test/, __tests__, *_test.go
- **Configuration**: config/, conf/, settings/
- **Documentation**: docs/, documentation/, README*
- **Scripts**: scripts/, bin/, tools/

**Output Schema**:
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
    "monorepo": false
  }
}
```

---

## Phase 2: Build System & Environment Analysis
**Status**: ⏳ Pending  
**Assigned Task**: `task-002-build-analysis`  
**Output Files**: `artifacts/build-info.json`, `reports/task-002-analysis.md`

### Detailed Methodology:
#### 2.1 Build System Detection Priority Order
**Enterprise Build Systems** (Check First):
1. **Bazel**: Look for `WORKSPACE`, `MODULE.bazel`, `BUILD` files
   - Extract: targets, dependencies, workspace structure
   - Commands: `bazel build //...`, `bazel test //...`
2. **Buck/Buck2**: Look for `.buckconfig`, `BUCK` files
   - Extract: build rules, target dependencies
3. **Rush (Microsoft)**: Look for `rush.json`, `common/config/rush/`
   - Extract: package management, build orchestration
4. **Nx (Nrwl)**: Look for `nx.json`, `workspace.json`
   - Extract: project graph, task dependencies

**Standard Build Systems**:
1. **Node.js Ecosystem**:
   - `package.json`: Extract scripts, dependencies, workspaces
   - `yarn.lock`/`package-lock.json`: Lock file analysis
   - `lerna.json`: Monorepo configuration
2. **Python Ecosystem**:
   - `pyproject.toml` > `setup.py` > `requirements.txt`
   - `poetry.lock`: Dependency locking
   - `Pipfile`: Pipenv configuration
3. **Java Ecosystem**:
   - `pom.xml`: Maven projects, modules, dependencies
   - `build.gradle`: Gradle projects, multi-module setup
4. **Go Ecosystem**:
   - `go.mod`: Module definition and dependencies
   - `go.work`: Workspace configuration

#### 2.2 CI/CD Integration Detection
**Look for CI/CD Configuration**:
- **GitHub Actions**: `.github/workflows/*.yml`
- **GitLab CI**: `.gitlab-ci.yml`
- **Jenkins**: `Jenkinsfile`
- **Azure Pipelines**: `azure-pipelines.yml`
- **CircleCI**: `.circleci/config.yml`

**Extract Information**:
- Build stages and dependencies
- Test execution strategy
- Deployment targets
- Environment configurations

#### 2.3 Containerization & Deployment
**Docker Analysis**:
- `Dockerfile`: Multi-stage builds, base images, security practices
- `docker-compose.yml`: Service orchestration, dependencies
- `.dockerignore`: Build optimization patterns

**Kubernetes Analysis**:
- `k8s/`, `kubernetes/`: Manifest files
- `Chart.yaml`: Helm charts
- Service mesh configurations (Istio, Linkerd)

**Output Schema**:
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

---

## Phase 3: Architecture & Dependency Analysis  
**Status**: ⏳ Pending  
**Assigned Task**: `task-003-architecture-analysis`  
**Output Files**: `artifacts/architecture.json`, `artifacts/dependencies.json`, `reports/task-003-analysis.md`

### Detailed Methodology:
#### 3.1 Module & Component Mapping
**AST Analysis Strategy**:
- **Python**: Use `ast` module to extract classes, functions, imports
- **JavaScript/TypeScript**: Parse with AST tools for exports, imports
- **Java**: Analyze package structure, class definitions, annotations
- **Go**: Parse package declarations, struct definitions, interfaces

**Component Identification**:
```json
{
  "module_name": "src.services.payment",
  "file_path": "src/services/payment.py", 
  "components": [
    {
      "type": "class",
      "name": "PaymentService",
      "line_range": [15, 89],
      "public_methods": ["process_payment", "refund_payment"],
      "dependencies": ["src.models.payment", "external.stripe"]
    }
  ],
  "exports": ["PaymentService", "PaymentError"],
  "imports": [
    {"module": "src.models.payment", "symbols": ["Payment"]},
    {"module": "stripe", "symbols": ["*"], "external": true}
  ]
}
```

#### 3.2 Dependency Graph Analysis
**Multi-Layer Dependency Mapping**:

1. **File-Level Dependencies**:
   ```json
   {
     "from": "src/services/payment.py",
     "to": "src/models/payment.py",
     "type": "import", 
     "symbols": ["Payment", "PaymentStatus"],
     "weight": 3
   }
   ```

2. **Module-Level Dependencies**:
   ```json
   {
     "from": "src.services",
     "to": "src.models", 
     "coupling_strength": 0.7,
     "shared_concepts": ["Payment", "User", "Order"]
   }
   ```

3. **External Dependencies**:
   ```json
   {
     "name": "stripe",
     "version": "5.4.0",
     "usage_locations": ["src/services/payment.py", "src/utils/billing.py"],
     "usage_intensity": "heavy",
     "security_scan": "clean",
     "license": "MIT"
   }
   ```

#### 3.3 Architectural Pattern Detection
**Layer Violation Detection**:
- Identify architectural layers (presentation, application, domain, infrastructure)
- Detect violations (e.g., presentation layer directly accessing database)
- Flag circular dependencies between modules

**Enterprise Pattern Recognition**:
- **Microservices**: Service boundaries, API contracts
- **Domain-Driven Design**: Bounded contexts, aggregates
- **CQRS/Event Sourcing**: Command/query separation
- **Hexagonal Architecture**: Port/adapter patterns

---

## Phase 4: Quality & Complexity Assessment
**Status**: ⏳ Pending  
**Assigned Task**: `task-004-quality-analysis`  
**Output Files**: `artifacts/complexity.json`, `artifacts/quality-metrics.json`, `reports/task-004-analysis.md`

### Detailed Methodology:
#### 4.1 Code Complexity Analysis
**Metrics Collection Strategy**:
- **Cyclomatic Complexity**: Decision points in control flow
- **Cognitive Complexity**: Mental effort required to understand code  
- **Maintainability Index**: Composite metric (0-100 scale)
- **Technical Debt Ratio**: Code issues vs clean code patterns

**Tools and Techniques**:
- Python: `radon cc` for cyclomatic complexity
- JavaScript: `eslint` complexity rules
- Java: `checkstyle` or `PMD` complexity metrics
- Generic: Count nesting levels, function length, parameter count

**Complexity Thresholds**:
```json
{
  "complexity_levels": {
    "low": {"cyclomatic": "< 10", "cognitive": "< 15"},
    "medium": {"cyclomatic": "10-20", "cognitive": "15-25"}, 
    "high": {"cyclomatic": "20-40", "cognitive": "25-50"},
    "very_high": {"cyclomatic": "> 40", "cognitive": "> 50"}
  }
}
```

#### 4.2 Test Coverage & Quality Gates
**Test Coverage Analysis**:
- **Unit Test Coverage**: Line, branch, function coverage
- **Integration Test Coverage**: API endpoints, database interactions
- **End-to-End Coverage**: User journey completeness

**Quality Gate Assessment**:
- **Build Success Rate**: Recent build history analysis
- **Test Stability**: Flaky test identification
- **Code Review Coverage**: Pull request analysis patterns

#### 4.3 Code Quality Patterns
**Anti-Pattern Detection**:
- **God Classes**: Classes with too many responsibilities
- **Long Methods**: Functions exceeding reasonable length
- **Dead Code**: Unreferenced code segments
- **Code Duplication**: Copy-paste patterns

**Best Practice Assessment**:
- **SOLID Principles**: Single responsibility, open/closed, etc.
- **Design Patterns**: Proper usage of common patterns
- **Error Handling**: Exception handling consistency
- **Documentation**: Code comments and API documentation

---

## Phase 5: Security & Compliance Analysis
**Status**: ⏳ Pending  
**Assigned Task**: `task-005-security-analysis`  
**Output Files**: `artifacts/security-analysis.json`, `artifacts/compliance-report.json`, `reports/task-005-analysis.md`

### Detailed Methodology:
#### 5.1 Dependency Security Analysis
**Vulnerability Scanning Strategy**:
- **Known CVE Detection**: Cross-reference with vulnerability databases
- **License Compliance**: GPL contamination, commercial license conflicts
- **Supply Chain Analysis**: Dependency confusion, typosquatting detection
- **Outdated Dependencies**: Version comparison with security releases

**Internal Package Analysis**:
- **Company Package Detection**: Internal registry patterns
- **Version Consistency**: Same internal packages at different versions
- **Security Policy Compliance**: Approved/forbidden package lists

#### 5.2 Code Security Patterns
**Security Anti-Pattern Detection**:
- **Hardcoded Secrets**: API keys, passwords, tokens in source
- **SQL Injection Risks**: String concatenation in queries
- **XSS Vulnerabilities**: Unescaped user input in templates
- **Authentication Bypasses**: Missing auth checks on endpoints

**Security Best Practice Assessment**:
- **Input Validation**: User input sanitization patterns
- **Cryptography Usage**: Strong encryption, proper key management
- **Access Control**: Role-based access, principle of least privilege
- **Logging Security**: No sensitive data in logs

#### 5.3 Compliance Framework Assessment
**Enterprise Compliance Standards**:
- **SOX Compliance**: Financial data handling, audit trails
- **GDPR/Privacy**: Personal data processing, consent management
- **Industry Standards**: PCI-DSS for payments, HIPAA for healthcare
- **Internal Policies**: Company-specific security requirements

---

## Phase 6: Git History & Risk Analysis
**Status**: ⏳ Pending  
**Assigned Task**: `task-006-git-analysis`  
**Output Files**: `artifacts/git-analysis.json`, `artifacts/risk-assessment.json`, `reports/task-006-analysis.md`

### Detailed Methodology:
#### 6.1 Repository History Analysis
**Commit Pattern Analysis**:
- **Commit Frequency**: Changes per file over time
- **Author Patterns**: Contributor activity, knowledge distribution  
- **Commit Message Analysis**: Bug fixes vs features vs refactoring
- **Temporal Patterns**: Weekend commits, emergency fixes, release cycles

**Git Commands for Analysis**:
```bash
# Commit frequency per file
git log --follow --pretty=format: --name-only | sort | uniq -c

# Author contribution patterns  
git log --pretty=format:"%an %ad %s" --date=short --since="1 year ago"

# Bug fix pattern detection
git log --grep="fix\|bug\|patch" --pretty=format:"%h %ad %s" --date=short
```

#### 6.2 Team Knowledge Mapping (Enhanced)
**Code Ownership Analysis**:
```bash
# Generate ownership data
git log --pretty=format:"%an %ae" --since="1 year ago" | sort | uniq -c | sort -nr > /tmp/contributors

# File ownership mapping  
for file in $(find . -name "*.py" -o -name "*.js" -o -name "*.java" -o -name "*.go"); do
  PRIMARY_AUTHOR=$(git log --follow --pretty=format:"%an" "$file" | head -20 | sort | uniq -c | sort -nr | head -1 | awk '{print $2}')
  COMMIT_COUNT=$(git log --follow --oneline "$file" | wc -l)
  LAST_MODIFIED=$(git log -1 --pretty=format:"%ad" --date=short "$file")
  
  echo "$file,$PRIMARY_AUTHOR,$COMMIT_COUNT,$LAST_MODIFIED" >> /tmp/ownership_map
done
```

**Team Expertise Identification**:
- **Domain Experts**: Authors with >50% commits in specific directories
- **Cross-Team Contributors**: Authors working across multiple components  
- **Recent Contributors**: Active in last 90 days
- **Legacy Maintainers**: Long-term stewards of specific components

#### 6.3 Knowledge Risk Assessment (Enhanced)
**Bus Factor Analysis**:
- **Single Points of Failure**: Files with only one active contributor
- **Knowledge Distribution**: How many people understand each component
- **Expertise Concentration**: Critical files with limited ownership
- **Onboarding Risk**: New developer learning curve assessment

**Collaboration Pattern Analysis**:
- **Cross-Team Changes**: Files modified by multiple teams
- **Code Review Patterns**: Review engagement and quality
- **Mentorship Evidence**: Junior/senior developer collaboration

#### 6.4 Hotspot Identification
**Risk Scoring Algorithm**:
```
Hotspot Score = (Commit Frequency × Complexity × Business Criticality) / Knowledge Distribution

Where:
- Commit Frequency: Changes in last 12 months
- Complexity: Cyclomatic complexity or LOC
- Business Criticality: Payment, auth, core business logic = high
- Knowledge Distribution: Number of active contributors
```

**Critical File Identification**:
- **High-Churn, High-Complexity**: Files that change frequently and are complex
- **Business-Critical**: Payment processing, authentication, core algorithms
- **Dependency Hubs**: Files that many other files depend on
- **Legacy Components**: Old code with minimal recent maintenance

#### Enhanced Output Schema
```json
{
  "repository_activity": {
    "commit_frequency": 45.2,
    "active_contributors": 8,
    "bus_factor": 3.2,
    "knowledge_concentration": 0.67
  },
  "team_knowledge": {
    "code_ownership": [
      {
        "file_pattern": "src/payment/*",
        "primary_expert": "alice@company.com",
        "secondary_experts": ["bob@company.com"],
        "risk_level": "medium",
        "last_active": "2024-01-15"
      }
    ],
    "expertise_areas": [
      {
        "domain": "authentication", 
        "expert": "charlie@company.com",
        "file_count": 23,
        "confidence_score": 0.89
      }
    ],
    "knowledge_gaps": [
      {
        "component": "legacy/billing",
        "issue": "single_maintainer",
        "risk_mitigation": "documentation_needed"
      }
    ]
  },
  "hotspot_analysis": {
    "high_churn_files": [
      {
        "file": "src/services/payment.py",
        "churn_score": 87,
        "complexity": 22,
        "risk_level": "high",
        "unique_authors": 3,
        "last_modified": "2024-01-20T10:30:00Z"
      }
    ]
  }
}
```

---

## Phase 7: Performance & Scalability Assessment
**Status**: ⏳ Pending  
**Assigned Task**: `task-007-performance-analysis`  
**Output Files**: `artifacts/performance-analysis.json`, `reports/task-007-analysis.md`

### Detailed Methodology:
#### 7.1 Algorithmic Complexity Analysis
**Performance Pattern Detection**:
- **O(n²) Algorithms**: Nested loops over large datasets
- **Database N+1 Queries**: ORM patterns causing excessive queries
- **Memory Leaks**: Unclosed resources, growing collections
- **Synchronous Bottlenecks**: Blocking I/O in async contexts

**Scalability Assessment**:
- **Database Access Patterns**: Query complexity, indexing usage
- **Caching Strategy**: Cache hit ratios, cache invalidation patterns
- **Resource Management**: Connection pooling, memory usage patterns
- **Async/Parallel Patterns**: Concurrent processing utilization

#### 7.2 Infrastructure Readiness
**Cloud-Native Assessment**:
- **12-Factor App Compliance**: Configuration, dependencies, processes
- **Containerization Readiness**: Dockerfile optimization, image sizes
- **Horizontal Scaling**: Stateless design, load balancer compatibility
- **Monitoring/Observability**: Logging, metrics, distributed tracing

---

## Consolidation Phase: Executive Summary Generation
**Status**: ⏳ Pending  
**Assigned Task**: `task-008-consolidation`  
**Output Files**: `consolidated/executive-analysis.md`, `consolidated/recommendations.md`

### Summary Generation Strategy:
#### Risk-Prioritized Reporting
1. **Critical (P0)**: Security vulnerabilities, build failures, data loss risks
2. **High (P1)**: Architectural violations, knowledge concentration, compliance gaps  
3. **Medium (P2)**: Technical debt, performance bottlenecks, quality issues
4. **Low (P3)**: Code style, documentation gaps, minor improvements

#### Executive Dashboard Metrics
- **Repository Health Score**: Composite score (0-100)
- **Technical Debt Hours**: Estimated remediation effort
- **Security Risk Level**: Critical/High/Medium/Low
- **Team Velocity Impact**: Factors slowing development
- **Maintenance Burden**: Ongoing operational overhead

---

## Task Coordination Instructions

### For Parallel Execution (Claude Code):
- Each task runs independently using this plan as complete context
- Tasks update their status in this plan file upon completion
- Orchestrator monitors for all completions before final consolidation
- No inter-task communication required - plan contains all context

### For Sequential Execution (Cline):
- Each task follows their plan section completely
- Task creates next task with reference to specific plan section
- Progress updates maintain plan state continuity
- Context transfer minimal - plan is the primary context source

### Output Standards:
- All JSON artifacts must validate against provided schemas
- Analysis reports must include specific findings, not general statements
- Quality gates must pass before task completion
- Executive summary must be actionable for technical leadership
```

This plan serves as the complete blueprint for enterprise-grade codebase analysis. Each task contains sufficient detail for independent execution while maintaining consistency across the entire analysis workflow.