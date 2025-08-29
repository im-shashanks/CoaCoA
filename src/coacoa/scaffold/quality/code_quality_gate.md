# Code Quality Gate Checklist

## Applies to: Dev · QA · Orchestrator

> **Purpose**  
> This checklist ensures code meets enterprise quality standards before merging.  
> All items must pass for the code to proceed to the next stage.

---

## Static Code Analysis

| # | Rule | Tools | Pass/Fail |
|---|------|-------|-----------|
| **CQ-1** | **Linting compliance** — Code passes all configured linting rules without warnings. | ESLint, Pylint, golangci-lint | |
| **CQ-2** | **Format consistency** — Code follows formatting standards (Prettier, Black, gofmt). | Prettier, Black, gofmt | |
| **CQ-3** | **Type checking** — All type annotations are valid and code passes type checker. | TypeScript, mypy, go vet | |
| **CQ-4** | **Import organization** — Imports are properly organized and unused imports removed. | isort, organize-imports | |
| **CQ-5** | **Dead code removal** — No unused variables, functions, or imports remain. | Dead code detectors | |

---

## Code Metrics

| # | Rule | Thresholds | Pass/Fail |
|---|------|------------|-----------|
| **CM-1** | **Cyclomatic complexity** — Functions ≤10 complexity, classes ≤20 average complexity. | radon, complexity-report | |
| **CM-2** | **Function length** — Functions ≤50 lines, methods ≤40 lines (excluding comments). | Line counting tools | |
| **CM-3** | **File length** — Source files ≤500 lines (excluding generated code). | Line counting tools | |
| **CM-4** | **Parameter count** — Functions ≤5 parameters (use objects for more). | Static analysis | |
| **CM-5** | **Nesting depth** — Maximum nesting depth ≤4 levels. | Complexity analyzers | |
| **CM-6** | **Code duplication** — No duplicate code blocks >10 lines. | PMD, SonarQube | |

---

## Testing Requirements

| # | Rule | Coverage | Pass/Fail |
|---|------|----------|-----------|
| **T-1** | **Unit test coverage** — New code has ≥90% line coverage. | jest, pytest-cov, go test | |
| **T-2** | **Branch coverage** — New code has ≥85% branch coverage. | Coverage tools | |
| **T-3** | **Test quality** — Tests have meaningful assertions, not just existence checks. | Manual review | |
| **T-4** | **Edge case testing** — Error conditions and boundary cases are tested. | Manual review | |
| **T-5** | **Integration tests** — External dependencies are integration tested. | Test frameworks | |
| **T-6** | **Performance tests** — Critical paths have performance benchmarks. | Performance testing | |

---

## Documentation Standards

| # | Rule | Requirements | Pass/Fail |
|---|------|--------------|-----------|
| **D-1** | **API documentation** — Public functions/classes have complete documentation. | JSDoc, Sphinx, godoc | |
| **D-2** | **README updates** — Changes update relevant README/documentation files. | Manual review | |
| **D-3** | **Code comments** — Complex logic has explanatory comments (not obvious statements). | Manual review | |
| **D-4** | **Changelog entry** — User-facing changes have changelog entries. | Manual review | |
| **D-5** | **Architecture docs** — Significant architectural changes are documented. | ADR, architecture docs | |

---

## Security Review

| # | Rule | Tools | Pass/Fail |
|---|------|-------|-----------|
| **SR-1** | **Vulnerability scan** — No high/critical security vulnerabilities. | Snyk, npm audit, safety | |
| **SR-2** | **Dependency audit** — All dependencies are from trusted sources and up-to-date. | Dependency checkers | |
| **SR-3** | **Secret detection** — No hardcoded secrets, keys, or passwords. | git-secrets, detect-secrets | |
| **SR-4** | **Input validation** — All external inputs are validated and sanitized. | Manual review | |
| **SR-5** | **Permission checks** — Access controls are properly implemented. | Manual review | |

---

## Performance Review

| # | Rule | Requirements | Pass/Fail |
|---|------|--------------|-----------|
| **PR-1** | **Database queries** — No N+1 queries; proper indexing considered. | Query analyzers | |
| **PR-2** | **Memory efficiency** — No obvious memory leaks or excessive allocations. | Profiling tools | |
| **PR-3** | **Algorithm efficiency** — Time complexity appropriate for expected data size. | Big O analysis | |
| **PR-4** | **Resource usage** — Proper cleanup of files, connections, and handles. | Manual review | |
| **PR-5** | **Caching strategy** — Expensive operations are cached where appropriate. | Manual review | |

---

## Build and Deploy

| # | Rule | Requirements | Pass/Fail |
|---|------|--------------|-----------|
| **BD-1** | **Build success** — Code builds successfully in clean environment. | CI/CD pipeline | |
| **BD-2** | **Test execution** — All tests pass in CI environment. | CI/CD pipeline | |
| **BD-3** | **Dependency resolution** — All dependencies resolve correctly. | Package managers | |
| **BD-4** | **Environment compatibility** — Code works in target environments. | Testing | |
| **BD-5** | **Deployment readiness** — Changes are ready for production deployment. | Manual review | |

---

## Code Review Checklist

| # | Rule | Focus | Pass/Fail |
|---|------|-------|-----------|
| **CR-1** | **Business logic accuracy** — Code correctly implements requirements. | Manual review | |
| **CR-2** | **Error handling** — Appropriate error handling and recovery mechanisms. | Manual review | |
| **CR-3** | **Code readability** — Code is self-documenting and easy to understand. | Manual review | |
| **CR-4** | **Best practices** — Code follows established patterns and conventions. | Manual review | |
| **CR-5** | **Backwards compatibility** — Changes don't break existing functionality. | Testing | |

---

## Quality Gate Enforcement

### Automated Checks
The following checks **MUST** be automated and block merge if they fail:
- CQ-1 through CQ-5 (Static Analysis)
- CM-1 through CM-6 (Code Metrics)  
- T-1 through T-2 (Test Coverage)
- SR-1 through SR-3 (Security Scanning)
- BD-1 through BD-4 (Build/Deploy)

### Manual Review Required
The following checks require human review and approval:
- T-3 through T-6 (Test Quality)
- D-1 through D-5 (Documentation)
- SR-4 through SR-5 (Security Review)
- PR-1 through PR-5 (Performance Review)
- CR-1 through CR-5 (Code Review)

### Override Process
Quality gate failures can only be overridden by:
1. **Senior Developer** approval for minor violations
2. **Tech Lead** approval for moderate violations  
3. **Engineering Manager** approval for major violations

All overrides must include:
- Detailed justification
- Risk assessment
- Remediation plan with timeline

---

## Tool Configuration Examples

### Python (pytest + mypy + black)
```bash
# Run quality checks
black --check .
isort --check-only .
mypy src/
pylint src/
pytest --cov=src --cov-report=html --cov-fail-under=90
```

### TypeScript (ESLint + Prettier + Jest)
```bash
# Run quality checks
npm run lint
npm run type-check
npm run format:check
npm run test:coverage
```

### Go (golangci-lint + go test)
```bash
# Run quality checks
go fmt ./...
go vet ./...
golangci-lint run
go test -race -coverprofile=coverage.out ./...
go tool cover -html=coverage.out
```

### Integration with CI/CD
```yaml
# GitHub Actions example
quality_gate:
  runs-on: ubuntu-latest
  steps:
    - name: Run static analysis
      run: |
        npm run lint
        npm run type-check
        
    - name: Run tests with coverage
      run: npm run test:coverage
      
    - name: Security scan
      uses: securecodewarrior/github-action-add-sarif@v1
      
    - name: Quality gate check
      run: |
        if [[ $(npm run test:coverage | grep "Coverage: " | cut -d' ' -f2 | cut -d'%' -f1) -lt 90 ]]; then
          echo "Coverage below threshold"
          exit 1
        fi
```