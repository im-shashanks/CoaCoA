# Security Quality Gate Checklist

## Applies to: Dev · QA · Security Review · Orchestrator

> **Purpose**  
> This checklist ensures code meets enterprise security standards before production deployment.  
> All items must pass for security-sensitive changes.

---

## Input Validation & Sanitization

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **IV-1** | **Parameter validation** — All API parameters are validated for type, length, and format. | Joi, Pydantic, Bean Validation | |
| **IV-2** | **SQL injection prevention** — All database queries use parameterized statements or ORM methods. | PreparedStatement, SQLAlchemy | |
| **IV-3** | **XSS prevention** — User input is escaped/sanitized before rendering in HTML. | DOMPurify, bleach, html/template | |
| **IV-4** | **Path traversal protection** — File paths are validated and normalized. | Path validation libraries | |
| **IV-5** | **Command injection prevention** — No user input passed directly to system commands. | Input validation, whitelisting | |
| **IV-6** | **JSON/XML parsing** — External data parsing has size limits and schema validation. | JSON Schema, XML validation | |

---

## Authentication & Authorization

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **AA-1** | **Authentication required** — Protected endpoints verify user authentication. | JWT, session middleware | |
| **AA-2** | **Authorization checks** — Users can only access resources they own or have permission for. | RBAC, ACL implementation | |
| **AA-3** | **Token validation** — JWT tokens are properly validated (signature, expiry, audience). | JWT libraries | |
| **AA-4** | **Session management** — Sessions have appropriate timeouts and are securely stored. | Secure session storage | |
| **AA-5** | **Password policies** — Passwords meet complexity requirements and are properly hashed. | bcrypt, Argon2 | |
| **AA-6** | **Multi-factor authentication** — Sensitive operations support/require MFA. | TOTP, SMS, email verification | |

---

## Data Protection

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **DP-1** | **Encryption in transit** — All sensitive data transmitted over HTTPS/TLS. | TLS 1.2+, HSTS headers | |
| **DP-2** | **Encryption at rest** — Sensitive data encrypted in database/storage. | Database encryption, field encryption | |
| **DP-3** | **PII handling** — Personal data follows privacy regulations (GDPR, CCPA). | Data classification, consent | |
| **DP-4** | **Secret management** — API keys, passwords stored in secure secret managers. | HashiCorp Vault, cloud secret managers | |
| **DP-5** | **Data masking** — Sensitive data masked in logs and non-production environments. | Logging frameworks, data masking | |
| **DP-6** | **Backup security** — Database backups are encrypted and access-controlled. | Encrypted backups, secure storage | |

---

## Communication Security

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **CS-1** | **HTTPS enforcement** — All HTTP traffic redirected to HTTPS. | Web server configuration | |
| **CS-2** | **Security headers** — Appropriate security headers set (CSP, HSTS, X-Frame-Options). | Helmet.js, security middleware | |
| **CS-3** | **CORS policy** — Cross-origin requests restricted to trusted domains. | CORS middleware configuration | |
| **CS-4** | **API rate limiting** — Public APIs have rate limiting to prevent abuse. | Rate limiting middleware | |
| **CS-5** | **Certificate validation** — External HTTPS connections validate certificates. | Certificate pinning, validation | |
| **CS-6** | **Webhook security** — Incoming webhooks are verified and authenticated. | HMAC verification, IP whitelisting | |

---

## Error Handling & Logging

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **EL-1** | **Information disclosure** — Error messages don't leak sensitive system information. | Custom error pages, message filtering | |
| **EL-2** | **Logging security** — Logs don't contain passwords, tokens, or PII. | Log filtering, structured logging | |
| **EL-3** | **Audit trail** — Security events are logged (authentication, authorization failures). | Audit logging framework | |
| **EL-4** | **Log integrity** — Logs are tamper-evident and stored securely. | Log signing, centralized logging | |
| **EL-5** | **Error consistency** — Authentication/authorization failures return consistent responses. | Standardized error responses | |

---

## Dependency Security

| # | Rule | Tools | Pass/Fail |
|---|------|-------|-----------|
| **DS-1** | **Vulnerability scanning** — No known high/critical vulnerabilities in dependencies. | npm audit, Snyk, OWASP Dependency Check | |
| **DS-2** | **Supply chain security** — Dependencies are from trusted sources with valid signatures. | Package verification, lock files | |
| **DS-3** | **Minimal dependencies** — Only necessary dependencies included; unused ones removed. | Dependency analysis tools | |
| **DS-4** | **Update policy** — Security patches applied within defined timeframes. | Automated security updates | |
| **DS-5** | **License compliance** — All dependencies have compatible licenses. | License scanning tools | |

---

## Code Security

| # | Rule | Tools | Pass/Fail |
|---|------|-------|-----------|
| **CSec-1** | **Static security analysis** — Code passes security-focused static analysis. | SonarQube, CodeQL, Bandit | |
| **CSec-2** | **Secret detection** — No hardcoded secrets, API keys, or passwords. | git-secrets, TruffleHog | |
| **CSec-3** | **Cryptographic practices** — Strong cryptographic algorithms and proper key management. | Crypto libraries, key rotation | |
| **CSec-4** | **Race condition prevention** — Concurrent code properly synchronized. | Thread safety analysis | |
| **CSec-5** | **Buffer overflow protection** — Memory-safe practices (primarily C/C++). | AddressSanitizer, static analysis | |

---

## Infrastructure Security

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **IS-1** | **Environment isolation** — Production environment isolated from development/test. | Network segmentation, access controls | |
| **IS-2** | **Principle of least privilege** — Services run with minimal required permissions. | Service accounts, IAM roles | |
| **IS-3** | **Network security** — Firewalls and network controls properly configured. | Security groups, network ACLs | |
| **IS-4** | **Container security** — Container images scanned for vulnerabilities. | Image scanning tools | |
| **IS-5** | **Secrets in deployment** — No secrets in container images or deployment configs. | Secret injection, ConfigMaps | |

---

## Data Flow Security

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **DFS-1** | **Data classification** — Sensitive data identified and labeled appropriately. | Data classification framework | |
| **DFS-2** | **Access logging** — Data access is logged and monitored. | Database audit logs | |
| **DFS-3** | **Data retention** — Old/unnecessary data is purged according to policy. | Automated data lifecycle | |
| **DFS-4** | **Cross-border transfers** — International data transfers comply with regulations. | Legal compliance review | |
| **DFS-5** | **Data anonymization** — Personal data anonymized for analytics/testing. | Anonymization tools | |

---

## Security Testing

| # | Rule | Tools | Pass/Fail |
|---|------|-------|-----------|
| **ST-1** | **Penetration testing** — Regular penetration tests of critical systems. | Professional pen testing | |
| **ST-2** | **DAST scanning** — Dynamic application security testing of running application. | OWASP ZAP, Burp Suite | |
| **ST-3** | **Security unit tests** — Security-focused unit tests for authentication/authorization. | Security test frameworks | |
| **ST-4** | **Fuzzing** — Input fuzzing for API endpoints and parsers. | AFL, libFuzzer | |
| **ST-5** | **Load testing** — Security under load conditions (DDoS resistance). | Load testing tools | |

---

## Compliance & Governance

| # | Rule | Framework | Pass/Fail |
|---|------|-----------|-----------|
| **CG-1** | **Privacy compliance** — GDPR, CCPA, or other applicable privacy laws. | Privacy impact assessment | |
| **CG-2** | **Industry standards** — SOX, PCI-DSS, HIPAA compliance where applicable. | Compliance frameworks | |
| **CG-3** | **Security documentation** — Security architecture and threat models documented. | Threat modeling, security docs | |
| **CG-4** | **Incident response** — Security incident response procedures defined. | Incident response plan | |
| **CG-5** | **Security training** — Developers trained on secure coding practices. | Training records | |

---

## Security Gate Enforcement

### Critical Security Issues (Automatic Block)
- High/Critical vulnerabilities in dependencies (DS-1)
- Hardcoded secrets detected (CSec-2)
- SQL injection vulnerabilities (IV-2)
- Missing authentication on protected endpoints (AA-1)
- Sensitive data in logs (EL-2)

### High Priority Issues (Manual Review Required)
- Medium-severity vulnerabilities (DS-1)
- Missing input validation (IV-1)
- Insufficient authorization checks (AA-2)
- Missing security headers (CS-2)
- Inadequate error handling (EL-1)

### Medium Priority Issues (Document and Track)
- Minor security improvements
- Security documentation gaps
- Non-critical compliance issues

---

## Security Tools Configuration

### Python Security Stack
```bash
# Security scanning
bandit -r src/
safety check
pip-audit
semgrep --config=auto src/

# Dependency scanning
pip-audit --format=json
```

### Node.js Security Stack
```bash
# Security scanning
npm audit --audit-level=high
npx audit-ci --high
eslint-plugin-security
semgrep --config=auto src/

# Runtime security
helmet.js middleware
express-rate-limit
```

### Go Security Stack
```bash
# Security scanning
gosec ./...
nancy sleuth
govulncheck ./...

# Static analysis with security focus
staticcheck ./...
```

### Infrastructure as Code Security
```bash
# Terraform security
tfsec .
checkov -d .

# Kubernetes security
kube-score score manifest.yaml
polaris validate --audit-path=.
```

---

## Security Incident Response

### Security Issue Classification
- **Critical**: Active exploit, data breach, system compromise
- **High**: Potential data exposure, authentication bypass
- **Medium**: Information disclosure, DoS vulnerabilities
- **Low**: Security improvements, hardening opportunities

### Response Timeline
- **Critical**: Immediate response (< 1 hour)
- **High**: Within 4 hours
- **Medium**: Within 24 hours  
- **Low**: Next sprint planning

### Communication Plan
1. Security team notification
2. Engineering management escalation
3. Legal/compliance team (for data-related issues)
4. Customer communication (if required)
5. Post-incident review and documentation