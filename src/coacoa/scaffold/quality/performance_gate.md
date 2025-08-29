# Performance Quality Gate Checklist

## Applies to: Dev · QA · Performance Review · Orchestrator

> **Purpose**  
> This checklist ensures code meets enterprise performance standards before production deployment.  
> Critical for user-facing features and high-throughput systems.

---

## Database Performance

| # | Rule | Metrics | Pass/Fail |
|---|------|---------|-----------|
| **DB-1** | **Query optimization** — No N+1 queries; use eager loading, batching, or caching. | Query count per request | |
| **DB-2** | **Index usage** — Database queries use appropriate indexes; no full table scans on large tables. | EXPLAIN query plans | |
| **DB-3** | **Connection pooling** — Database connections are pooled and reused efficiently. | Connection pool metrics | |
| **DB-4** | **Transaction scope** — Database transactions are kept as short as possible. | Transaction duration | |
| **DB-5** | **Bulk operations** — Large data operations use batch processing instead of individual operations. | Batch size, processing time | |
| **DB-6** | **Query timeout** — All database queries have appropriate timeouts configured. | Timeout configuration | |

---

## Memory Management

| # | Rule | Thresholds | Pass/Fail |
|---|------|------------|-----------|
| **MM-1** | **Memory leaks** — No obvious memory leaks; memory usage stabilizes over time. | Memory growth over time | |
| **MM-2** | **Large collections** — Collections >10k items are processed in batches or streams. | Collection size monitoring | |
| **MM-3** | **Object lifecycle** — Expensive objects are properly disposed/closed. | Resource cleanup | |
| **MM-4** | **Caching strategy** — Memory usage for caches is bounded with appropriate eviction. | Cache size limits | |
| **MM-5** | **Buffer management** — I/O operations use appropriately sized buffers. | Buffer size optimization | |

---

## API Performance

| # | Rule | Targets | Pass/Fail |
|---|------|---------|-----------|
| **API-1** | **Response time** — 95th percentile response time <500ms for user-facing APIs. | Response time percentiles | |
| **API-2** | **Throughput** — APIs handle expected load with <2% error rate. | Requests per second, error rate | |
| **API-3** | **Pagination** — Large result sets use pagination with reasonable page sizes. | Page size limits | |
| **API-4** | **Caching headers** — Cacheable responses include appropriate cache headers. | Cache-Control, ETag headers | |
| **API-5** | **Compression** — Large responses use compression (gzip, brotli). | Response compression | |
| **API-6** | **Rate limiting** — APIs implement appropriate rate limiting to prevent abuse. | Rate limit configuration | |

---

## Algorithm & Computation

| # | Rule | Complexity | Pass/Fail |
|---|------|------------|-----------|
| **AC-1** | **Time complexity** — Algorithms are O(n log n) or better for expected data sizes. | Big O analysis | |
| **AC-2** | **Space complexity** — Memory usage grows linearly or better with input size. | Space complexity analysis | |
| **AC-3** | **Expensive operations** — CPU-intensive operations are cached or asynchronous. | CPU usage monitoring | |
| **AC-4** | **Loop optimization** — Nested loops minimized; expensive operations moved outside loops. | Code review | |
| **AC-5** | **Recursive algorithms** — Recursion depth bounded to prevent stack overflow. | Recursion depth limits | |

---

## I/O Performance

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **IO-1** | **Async patterns** — I/O operations use non-blocking async patterns where available. | async/await usage | |
| **IO-2** | **Concurrent requests** — External API calls are made concurrently when possible. | Concurrent request patterns | |
| **IO-3** | **File operations** — File I/O uses streaming for large files instead of loading entirely in memory. | Streaming implementation | |
| **IO-4** | **Network timeouts** — All network calls have appropriate timeouts and retries. | Timeout configuration | |
| **IO-5** | **Connection reuse** — HTTP clients reuse connections (keep-alive). | Connection pooling | |

---

## Frontend Performance

| # | Rule | Metrics | Pass/Fail |
|---|------|---------|-----------|
| **FE-1** | **Bundle size** — JavaScript bundles <250KB gzipped for main bundle. | Bundle analyzer | |
| **FE-2** | **Loading performance** — First Contentful Paint <1.5s, Largest Contentful Paint <2.5s. | Core Web Vitals | |
| **FE-3** | **Image optimization** — Images are optimized, properly sized, and use modern formats. | Image metrics | |
| **FE-4** | **Code splitting** — Large applications use code splitting and lazy loading. | Webpack bundle analysis | |
| **FE-5** | **Caching strategy** — Static assets have long-term caching with cache busting. | Cache headers | |
| **FE-6** | **DOM manipulation** — Minimal DOM queries; batch DOM updates. | Performance profiling | |

---

## Caching Strategy

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **CS-1** | **Cache hit ratio** — Application caches achieve >80% hit ratio for cached operations. | Cache metrics | |
| **CS-2** | **Cache invalidation** — Cache invalidation strategy prevents stale data issues. | Cache invalidation logic | |
| **CS-3** | **Multi-level caching** — Multiple cache layers (browser, CDN, application, database). | Caching architecture | |
| **CS-4** | **Cache sizing** — Cache memory usage is bounded and monitored. | Cache size monitoring | |
| **CS-5** | **TTL strategy** — Cache TTL values are appropriate for data volatility. | TTL configuration | |

---

## Resource Utilization

| # | Rule | Limits | Pass/Fail |
|---|------|--------|-----------|
| **RU-1** | **CPU usage** — Normal operations use <70% CPU; peak usage <90%. | CPU monitoring | |
| **RU-2** | **Memory usage** — Application memory usage is predictable and bounded. | Memory monitoring | |
| **RU-3** | **Disk I/O** — Disk operations don't saturate I/O capacity. | Disk I/O monitoring | |
| **RU-4** | **Network bandwidth** — Network usage is optimized for available bandwidth. | Network monitoring | |
| **RU-5** | **Thread pool usage** — Thread pools are appropriately sized and monitored. | Thread pool metrics | |

---

## Scalability

| # | Rule | Architecture | Pass/Fail |
|---|------|-------------|-----------|
| **SC-1** | **Horizontal scaling** — Application can scale horizontally without shared state issues. | Stateless design | |
| **SC-2** | **Database scaling** — Database queries perform well as data volume grows. | Query performance testing | |
| **SC-3** | **Load distribution** — Load is evenly distributed across instances. | Load balancing metrics | |
| **SC-4** | **Graceful degradation** — System degrades gracefully under high load. | Circuit breakers, timeouts | |
| **SC-5** | **Auto-scaling** — Infrastructure can automatically scale based on demand. | Auto-scaling configuration | |

---

## Performance Testing

| # | Rule | Testing | Pass/Fail |
|---|------|---------|-----------|
| **PT-1** | **Load testing** — System tested under expected peak load. | Load test results | |
| **PT-2** | **Stress testing** — System behavior under extreme load is acceptable. | Stress test results | |
| **PT-3** | **Endurance testing** — System performance stable over extended periods. | Long-running tests | |
| **PT-4** | **Baseline performance** — Performance metrics compared against previous versions. | Performance regression tests | |
| **PT-5** | **Real user monitoring** — Production performance monitored with real user data. | RUM tools | |

---

## Monitoring & Observability

| # | Rule | Implementation | Pass/Fail |
|---|------|----------------|-----------|
| **MO-1** | **Performance metrics** — Key performance indicators are tracked and alerted. | APM tools | |
| **MO-2** | **Distributed tracing** — Request flows are traceable across services. | Tracing implementation | |
| **MO-3** | **Error rate monitoring** — Error rates and types are monitored and alerted. | Error tracking | |
| **MO-4** | **Performance profiling** — Regular performance profiling identifies bottlenecks. | Profiling tools | |
| **MO-5** | **SLA monitoring** — Service Level Agreements are monitored and reported. | SLA dashboards | |

---

## Performance Benchmarks

### API Response Time Targets
```
User-facing endpoints:
- 50th percentile: <200ms
- 95th percentile: <500ms  
- 99th percentile: <1000ms

Internal APIs:
- 50th percentile: <100ms
- 95th percentile: <300ms
- 99th percentile: <500ms

Background processes:
- No strict latency requirements
- Should not impact user-facing performance
```

### Database Performance Targets
```
Query Response Times:
- Simple queries: <10ms
- Complex queries: <100ms
- Reporting queries: <5s

Connection Pool:
- Pool utilization: <80%
- Connection wait time: <10ms
- Connection leak detection: enabled
```

### Memory Usage Guidelines
```
Application Memory:
- Startup memory: <500MB
- Normal operations: <2GB
- Memory growth: <10% per hour
- GC pressure: <5% of CPU time

Cache Memory:
- L1 cache: <100MB
- L2 cache: <500MB  
- Cache eviction: LRU or LFU
- Hit ratio: >80%
```

---

## Performance Tools Configuration

### Application Performance Monitoring
```yaml
# APM Configuration Example
apm:
  service_name: "user-service"
  sample_rate: 0.1
  capture_body: "errors"
  metrics:
    - response_time
    - throughput
    - error_rate
    - memory_usage
    - cpu_usage
```

### Database Performance Monitoring
```sql
-- PostgreSQL performance queries
SELECT query, calls, total_time, mean_time 
FROM pg_stat_statements 
ORDER BY total_time DESC 
LIMIT 10;

-- Index usage analysis  
SELECT schemaname, tablename, attname, n_distinct, correlation
FROM pg_stats
WHERE n_distinct < 100;
```

### Load Testing Configuration
```yaml
# Artillery.js load test example
config:
  target: 'https://api.example.com'
  phases:
    - duration: 60
      arrivalRate: 10
    - duration: 120  
      arrivalRate: 50
    - duration: 60
      arrivalRate: 100

scenarios:
  - name: "User registration flow"
    weight: 70
    flow:
      - post:
          url: "/api/users"
          json:
            email: "test@example.com"
            password: "password123"
```

### Profiling Setup
```bash
# Python profiling
python -m cProfile -o profile.stats main.py
py-spy top --pid 1234

# Node.js profiling
node --inspect app.js
clinic doctor -- node app.js

# Go profiling
go tool pprof http://localhost:6060/debug/pprof/profile
go test -bench=. -cpuprofile=cpu.prof
```

---

## Performance Gate Enforcement

### Critical Performance Issues (Automatic Block)
- Response times >2x baseline (API-1)
- Memory leaks detected (MM-1)
- Database N+1 queries (DB-1)
- Load test failures (PT-1)
- Critical resource exhaustion (RU-1, RU-2)

### High Priority Issues (Manual Review)
- Performance regression >50% (PT-4)
- Cache hit ratio <50% (CS-1)
- Missing performance monitoring (MO-1)
- Inefficient algorithms (AC-1)

### Performance Improvement Opportunities
- Optimization suggestions from profiling
- Caching opportunities
- Database query optimizations
- Code refactoring for performance

### Performance Review Process
1. **Automated Testing**: Load tests run in CI/CD
2. **Metrics Review**: Performance metrics compared to baseline
3. **Manual Review**: Complex performance changes reviewed by senior developers
4. **Production Monitoring**: Performance monitored post-deployment with rollback triggers