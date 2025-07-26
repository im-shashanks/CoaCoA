# Architecture-Integrity Checklist

## Applies to: Architect · Orchestrator · QA

| # | Rule |
|---|------|
| A-1 | New components follow layering constraints in `arch.*` (e.g. no UI → DB direct calls). |
| A-2 | Public interfaces are versioned; breaking changes bump SemVer **major** in docs. |
| A-3 | Deployment topology diagrams include latency & throughput annotations for each link. |
| A-4 | ADR present & linked for every new architectural pattern (e.g. CQRS, event sourcing). |
| A-5 | Infrastructure concerns (observability, feature flags, config) referenced, even if DevOps is out-of-scope. |
| A-6 | Internationalisation & accessibility considerations noted for UI components. |
| A-7 | Licensing of incorporated OSS components reviewed (compatible with project licence). |
