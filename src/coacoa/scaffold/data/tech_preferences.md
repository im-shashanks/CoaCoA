# CoaCoA Technology Preferences

## Purpose
This document provides opinionated technology choices for AI coding assistants to ensure consistent technology selection and prevent decision paralysis during code generation.

---

## Backend Frameworks

### Python
- **Web Framework**: FastAPI (preferred) > Flask > Django
  - FastAPI: For APIs, async support, automatic docs
  - Flask: For simple web apps, microservices
  - Django: For content-heavy applications with admin needs

- **HTTP Client**: httpx > requests
  - httpx: Modern, async support, HTTP/2
  - requests: Only for simple synchronous cases

- **Database ORM**: SQLAlchemy 2.0 > Tortoise ORM > Django ORM
  - SQLAlchemy: Full-featured, battle-tested
  - Tortoise: For async-first applications

### TypeScript/Node.js
- **Web Framework**: Express.js > Fastify > NestJS
  - Express: Simple, lightweight, great ecosystem
  - Fastify: Performance-critical applications
  - NestJS: Large enterprise applications requiring structure

- **HTTP Client**: axios > fetch > node-fetch
  - axios: Rich feature set, interceptors, timeout handling
  - fetch: Native web standard, simple use cases

- **Database ORM**: Prisma > TypeORM > Sequelize
  - Prisma: Type-safe, great DX, migrations
  - TypeORM: Decorator-based, familiar to Java developers

### Java
- **Web Framework**: Spring Boot > Micronaut > Quarkus
  - Spring Boot: Mature ecosystem, extensive documentation
  - Micronaut: Cloud-native, fast startup
  - Quarkus: Native compilation, Kubernetes-optimized

- **HTTP Client**: OkHttp > Apache HttpClient
  - OkHttp: Modern, efficient, great for mobile

- **Database**: JPA/Hibernate > MyBatis > JDBC Template
  - Hibernate: Standard, feature-rich ORM
  - MyBatis: SQL-first approach, performance control

### Go
- **Web Framework**: Gin > Echo > Chi > Standard library
  - Gin: Fast, simple, good middleware ecosystem
  - Echo: Similar to Gin, good documentation
  - Standard library: Simple applications, learning

- **HTTP Client**: Standard library `net/http` > Resty
  - Standard library: Sufficient for most use cases
  - Resty: REST-focused, chainable API

- **Database**: GORM > sqlx > database/sql
  - GORM: Full-featured ORM, migrations
  - sqlx: SQL-first with struct scanning

---

## Frontend Technologies

### React Ecosystem
- **Framework**: Next.js > Create React App > Vite
  - Next.js: SSR, file-based routing, full-stack features
  - Vite: Fast development, simple SPAs

- **State Management**: Zustand > Redux Toolkit > React Context
  - Zustand: Simple, minimal boilerplate
  - Redux Toolkit: Complex state, time-travel debugging
  - Context: Component-level state only

- **Styling**: Tailwind CSS > styled-components > CSS Modules
  - Tailwind: Utility-first, consistent design system
  - styled-components: Component-scoped styles, dynamic styling

- **Form Handling**: React Hook Form > Formik
  - React Hook Form: Performance, minimal re-renders
  - Formik: Complex validation requirements

### Vue.js Ecosystem
- **Framework**: Nuxt.js > Vue CLI > Vite
- **State Management**: Pinia > Vuex
- **Styling**: Tailwind CSS > Vue styled-components

---

## Database Technologies

### Primary Database
- **Relational**: PostgreSQL > MySQL > SQLite
  - PostgreSQL: Feature-rich, JSON support, reliability
  - MySQL: High performance, widespread adoption
  - SQLite: Local development, small applications

- **Document**: MongoDB > CouchDB
  - MongoDB: Rich query language, aggregation pipeline
  - CouchDB: Offline-first applications

### Caching
- **In-Memory**: Redis > Memcached
  - Redis: Data structures, persistence, pub/sub
  - Memcached: Simple key-value caching

### Search
- **Full-Text Search**: Elasticsearch > PostgreSQL FTS > SQLite FTS
  - Elasticsearch: Complex search requirements, analytics
  - PostgreSQL FTS: Simple search in existing PostgreSQL setup

---

## Testing Frameworks

### Python
- **Unit Testing**: pytest > unittest
- **HTTP Testing**: httpx.AsyncClient > requests-mock
- **Mocking**: pytest-mock > unittest.mock

### TypeScript/JavaScript
- **Unit Testing**: Jest > Vitest > Mocha
- **Integration**: Supertest > Testing Library
- **E2E Testing**: Playwright > Cypress

### Java
- **Unit Testing**: JUnit 5 > TestNG
- **Mocking**: Mockito > EasyMock
- **Integration**: Spring Boot Test > Testcontainers

### Go
- **Unit Testing**: Standard library `testing` + testify
- **HTTP Testing**: httptest package
- **Mocking**: testify/mock > GoMock

---

## Development Tools

### Code Quality
- **Python**: Black (formatter) + isort (imports) + flake8 (linting) + mypy (types)
- **TypeScript**: Prettier (formatter) + ESLint (linting) + TypeScript compiler
- **Java**: Google Java Format + Checkstyle + SpotBugs + PMD
- **Go**: gofmt + golangci-lint + govulncheck

### Package Management
- **Python**: Poetry > pip-tools > pipenv
- **TypeScript**: pnpm > yarn > npm
- **Java**: Maven > Gradle
- **Go**: Go modules (built-in)

### Documentation
- **API Documentation**: 
  - OpenAPI/Swagger for REST APIs
  - GraphQL schema for GraphQL APIs
  - AsyncAPI for event-driven APIs

- **Code Documentation**:
  - Python: Sphinx + Napoleon
  - TypeScript: TypeDoc
  - Java: Javadoc
  - Go: pkg.go.dev (built-in)

---

## Authentication & Authorization

### Authentication
- **Standards**: OAuth 2.0 + OpenID Connect > SAML 2.0
- **JWT Libraries**:
  - Python: PyJWT > python-jose
  - TypeScript: jsonwebtoken > jose
  - Java: java-jwt > jjwt
  - Go: golang-jwt/jwt

### Authorization
- **Pattern**: RBAC (Role-Based Access Control) > ABAC (Attribute-Based)
- **Implementation**: 
  - Policy engines: Open Policy Agent (OPA)
  - Simple cases: Custom middleware/decorators

---

## Logging & Monitoring

### Logging
- **Structured Logging**: JSON format preferred
- **Libraries**:
  - Python: structlog > loguru > standard logging
  - TypeScript: winston > pino
  - Java: SLF4J + Logback > Log4j2
  - Go: slog (Go 1.21+) > logrus > zap

### Monitoring
- **Metrics**: Prometheus + Grafana
- **Tracing**: OpenTelemetry > Jaeger
- **Error Tracking**: Sentry > Rollbar

---

## Security

### Input Validation
- **Python**: Pydantic > marshmallow > cerberus
- **TypeScript**: Zod > Yup > Joi
- **Java**: Bean Validation (JSR 303) > Hibernate Validator
- **Go**: go-playground/validator > Custom validation

### Encryption
- **Hashing**: bcrypt > scrypt > Argon2
- **Symmetric**: AES-256-GCM
- **Asymmetric**: RSA-2048 (minimum) or ECDSA P-256

---

## Configuration Management

### Environment Configuration
- **Format**: Environment variables + .env files > YAML > JSON
- **Libraries**:
  - Python: pydantic-settings > python-decouple
  - TypeScript: dotenv + joi validation
  - Java: Spring Boot Configuration > MicroProfile Config
  - Go: viper > godotenv

### Secrets Management
- **Development**: .env files (gitignored)
- **Production**: Cloud provider secrets (AWS Secrets Manager, Azure Key Vault, GCP Secret Manager)
- **Self-hosted**: HashiCorp Vault > Docker Secrets

---

## Deployment & Infrastructure

### Containerization
- **Runtime**: Docker > Podman
- **Orchestration**: Kubernetes > Docker Compose

### Cloud Providers
- **Preference Order**: AWS > Google Cloud > Azure
- **Services**:
  - Compute: Kubernetes > Serverless (Lambda/Cloud Functions) > VMs
  - Storage: Object Storage (S3) + Block Storage
  - Database: Managed services preferred (RDS, Cloud SQL)

### CI/CD
- **Platforms**: GitHub Actions > GitLab CI > Jenkins
- **Deployment**: Blue-green > Rolling > Canary

---

## Performance Guidelines

### Caching Strategy
1. **Browser Cache**: Static assets (images, CSS, JS)
2. **CDN**: Geographic distribution of static content
3. **Application Cache**: Redis for session data, computed results
4. **Database Cache**: Query result caching, connection pooling

### Database Optimization
- **Indexing**: Index foreign keys, search columns, sort columns
- **Query Optimization**: Use EXPLAIN to analyze query plans
- **Connection Management**: Connection pooling, prepared statements

---

## Decision Rationale

### Why These Choices?
1. **Maturity**: Prefer battle-tested technologies with strong communities
2. **Developer Experience**: Tools that improve productivity and reduce errors
3. **Performance**: Reasonable performance without over-optimization
4. **Maintainability**: Code that's easy to understand and modify
5. **Security**: Security by default, well-audited libraries

### When to Deviate
- **Existing Codebase**: Match existing technology stack first
- **Team Expertise**: Prefer technologies the team already knows
- **Specific Requirements**: Performance, security, or compliance needs may override defaults
- **Ecosystem Constraints**: Platform or deployment environment limitations

### Upgrading Guidelines
- **Major Versions**: Plan migrations, test thoroughly
- **Security Updates**: Apply promptly
- **Feature Updates**: Evaluate based on value vs. risk
- **EOL Software**: Create migration plan before end-of-life