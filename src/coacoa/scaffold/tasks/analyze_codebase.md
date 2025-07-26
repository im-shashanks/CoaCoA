# Task · analyze_codebase

## Assigned to: code-explorer agent

> **Objective**  
> Produce a complete Code-Intelligence snapshot for the current repository, persisting artefacts
> to the paths defined in `coacoa.yaml -> coa.paths.*`.  
> These artefacts must be **idempotent** (re-running yields identical JSON when repo unchanged).

---

## 0 · Inputs

| Config key                                  | Expected value / example                    |
|---------------------------------------------|---------------------------------------------|
| `coa.paths.analysis`                        | `.coacoa/context/analysis.md`                       |
| `coa.paths.module_map`                      | `.coacoa/context/intelligence/module_map.json`      |
| `coa.paths.dep_graph`                       | `.coacoa/context/intelligence/dep_graph.json`       |
| `coa.paths.complexity`                      | `.coacoa/context/intelligence/complexity.json`      |
| `coa.paths.hotspots`                        | `.coacoa/context/intelligence/hotspots.json`        |
| `coa.paths.coverage`                        | `.coacoa/context/intelligence/coverage.json`        |
| `coa.limits.max_tokens_context`             | Prompt budget for any summarisation step    |
| Exclude globs                               | `.git/ , coacoa/ , **/dist , **/node_modules` (hard-coded) |

---

## 1 · Language & file discovery

1. Start at repo root (file that contains `coacoa/` folder).  
2. Walk filesystem; build table:

   ```json
   {
     "<relative_path>": {
       "lang": "python|typescript|java|go|rust|cpp|…",
       "loc": 123,
       "is_test": true|false
     },
     …
   }
3. Persist language histogram (languages:) & total LOC in step-2 output bundle.

## 2 · Module Map (module_map.json)

   ```jsonc
   {
      "moduleName": {
         "file": "src/foo/bar.py",
         "classes": [
            {"name": "UserService", "line_start": 10, "line_end": 120}
         ],
         "functions": [
            {"name": "load_users", "line_start": 124, "line_end": 199}
         ]
      },
      …
   }
   ```

**Implementation hints (Python-centric but extendable):**

- moduleName = dotted path (src.foo.bar).
- Use Python ast or tree-sitter bindings for other languages to enumerate top-level defs.
- Exclude private (_name) items unless referenced elsewhere.

## 3 · Dependency Graph (dep_graph.json)

   ```json
   [
      ["src/foo/bar.py", "src/db/client.py"],
      ["src/foo/bar.py", "libs/common/log.py"],
   …
   ]
   ```

*Edge includes only direct file-level imports / requires / #include.*
*Post-process to remove duplicates.*

## 3.2 · Build/Run system (`build_info.json`)

   > **Schema**

   ```json
      {
      "ecosystem": "brazil",           // mvn | gradle | npm | bazel | make | brazil | …
      "detected_files": [".brazil-project.json", "pom.xml"],
      "commands": {
         "build": "brazil-build build",
         "test":  "brazil-test unit",
         "lint":  "python -m ruff",
         "run":   "brazil-run LocalMain"
         }
      }
      {
      "ecosystem": "python",
      "detected_files": ["pyproject.toml", ".venv"],
      "commands": {
         "build": "${VENV}/bin/pip install -e .[dev]",
         "test":  "${VENV}/bin/pytest -q",
         "lint":  "${VENV}/bin/python -m ruff",
         "type":  "${VENV}/bin/mypy --strict src/",
         "run":   "${VENV}/bin/python -m src.coacoa.__main__ --help"
         }
      }
   ```

**Detection hints**
•	Brazil: .brazil-build/ folder or .brazil-project.json.
•	Maven: pom.xml.
•	Gradle: build.gradle or settings.gradle.
•	Node: package.json with scripts.
•	Bazel: BUILD files at repo root.
•	Make: Makefile with test: or build: targets.

_If multiple ecosystems, pick the one at repo root; list others under secondary:[]._

## 4 · Package dependencies (`dependencies.json`)

> **Schema**

   ```json
   {
      "ecosystem": "python",
      "source": "pyproject.toml",
      "dependencies": [
         {"name": "fastapi", "version": "0.110.0"},
         {"name": "sqlalchemy", "version": "2.0.25"}
      ]
   }
   ```
**Extraction hints:**
- Python: read pyproject.toml or requirements*.txt.
- Node: parse package.json.
- Go: go list -m -json all.
- Rust: cargo metadata --format-version 1.
- If multiple ecosystems, output an array of such objects.

## 5 · Circular-dependency report (`cycles.json`)

> **Schema**

   ```
      [
         ["src/db/client.py", "src/db/__init__.py", "src/db/client.py"],
         ["src/service/auth.py", "src/service/user.py", "src/service/auth.py"]
      ]
   ```

**Algorithm**
 1. Build adjacency list from dep_graph.json.
 2. Run Tarjan or Kosaraju SCC algorithm.
 3. Persist each cycle as an ordered list of file paths (first == last for clarity).
 4. Append a brief note to analysis.md § Complex Files if any cycles exist.

## 6 · Complexity metrics (complexity.json)

   ```json
   {
      "src/foo/bar.py": {
         "cyclomatic": 18,
         "maint_index": 54.2,
         "h_cognitive": 12        // optional: Halstead, cognitive
      },
      …
   }
   ```
**Guidelines**
 • Use radon (radon cc -j) for Python; fall back to average nesting depth for other langs.
 • Any file with cyclomatic >= 20 or maint_index <= 40 is flagged “complex” later.

## 7 · Git churn & hotspots (hotspots.json)

   ```json
   {
      "src/foo/bar.py": {
         "churn": 37,             // commits touching file
         "last_commit": "2025-07-18T14:25:01Z",
         "is_complex": true,
         "hotspot_score": 666     // churn × cyclomatic
      },
      …
   }
   ```
**Steps:**
 1. If .git/ present, run git log --follow --pretty=format: --name-only.
 2. Count touches per file (churn).
 3. Compute hotspot_score = churn * max(cyclomatic, 1).
 4. Mark top-10 % scores as hotspots.

## 8 · Test-coverage (coverage.json)

Only for languages with coverage tooling (Python -→ pytest --cov --cov-report=json).
Store simple float per file.

   ```json
   {"src/foo/bar.py": 0.62, …}
   ```

_If tooling absent, omit file → agent consumers treat as null._

## 9 · analysis.md executive summary

**Sections (Markdown):**
 1. Repo Stats – languages, total LOC, #tests.
 2. Complex Files – table top-15 by cyclomatic.
 3. Hotspots – table top-15 by hotspot_score.
 4. Coverage Gaps – files < 70 % coverage.
 5. Next-Step Suggestions – bullet list for PO / Architect (e.g., “Refactor src/foo/bar.py”).
Limit entire file to ≤ {{cfg.limits.max_tokens_context}} tokens.

## 10 · Validation

**Run Link-Integrity checklist items:**
 • All JSON paths exist & are parseable.
 • All file paths referenced exist on disk.
 • Required keys present.

_If any validation fails → emit /orchestrator fix analyze_codebase-validation._

## 11 · Outputs

Write artefacts to disks paths configured in § 0.
Return the string: `COMPLETED analyze_codebase` for orchestrator consumption.
