# CoaCoA – Pragmatic SOLID Policy (v0.1)

1. **Single Responsibility (SRP)**  
   *Apply at module-or-class granularity, not per 10-line function.*  
   Classes > 400 LOC or with ≥ 3 “reasons to change” must be split.

2. **Open/Closed (OCP)**  
   Prefer extension via functions or small mix-in classes; **do not** create
   abstract base classes unless ≥ 2 concrete implementations exist.

3. **Liskov Substitution (LSP)**  
   Enforced implicitly by type hints + mypy strict mode.

4. **Interface Segregation (ISP)**  
   Avoid “god” interfaces; if interface > 7 methods, split.

5. **Dependency Inversion (DIP)**  
   Use constructor injection for external dependencies (db, api clients).
   For brown-field, match existing dependency pattern first.

## When to refactor for new extensions
* If a second implementation **appears later** (new story/epic),
  **Architect** must create an ADR proposing abstract base class or interface.
* **Dev** for the second implementation:
  1. Reads the ADR (status: *Proposed*).
  2. Refactors original code to extract interface **only if** ADR is *Accepted*.
  3. Keeps change set minimal—do not rename modules unless specified by ADR.
