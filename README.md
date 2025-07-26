# CoaCoA v0.1 — Context-Optimised Agentic Coding Assistant  
*“Drop it in, branch out, ship confidently.”*

---

## 📌 TL;DR  

1. `pip install coacoa`                *(once v0.1 hits PyPI — for now, copy the `coacoa/` folder)*  
2. `coacoa init`                       *(or manual copy) — scaffolds `coacoa/`, `CLAUDE.md`, `.clinerules`*  
3. `git add . && git commit -m "init coa"`  
4. In your IDE (Claude Code / Cline):  

   ```text
   /analyze-codebase        # brown-field   │  or  │  /analyst init      # green-field
   /pm new-prd
   /ux-designer make-ui
   /po refine-epics
   /architect finalize-arch
   /scrum-master create
   /orchestrator run        # Dev → QA loop
   ```
5. Review staged branch feature/s_001_01, commit & push.
6. Rinse, repeat → production-ready PRs with ≥ 90 % test coverage and zero broken builds.

## ✨ Why CoaCoA?
| Area | CoaCoA v0.1 |  
| - | - |  
| Config schema | 28-key namespaced YAML |  
| Code-intel | map + deps + complexity + hotspots + coverage + cycles + build_info |  
| Quality gates | 🎯 5 checklists (Anti-Hallucination, Link, QA, Arch, Build) |  
| Workflow | 12 agents (UX, PO, Architect, Code-Explorer, Orchestrator) |  
| Branching | auto feature/<story> branch (staged, not committed) |  
| SOLID policy | Pragmatic SRP/OCP mandatory, rest advisory via ADR |  

## 🗂 Folder & file map
coacoa/  
├─ coacoa.yaml               ← config (paths, limits, workflows…)  
├─ agents/                   ← markdown specs (analyst, pm, … orchestrator)  
├─ tasks/                    ← step-by-step recipes (analyze_codebase.md …)  
├─ templates/                ← PRD, UI/UX, architecture, story, ADR…  
├─ quality/                  ← checklists (anti_hallucination, build_integrity…)  
├─ data/                     ← tech_preferences.md, solid_policy.md, style_guides/  
├─ workflows/                ← default_greenfield.yml, default_brownfield.yml  
└─ context/                  ← generated intelligence artefacts  

**Git**
Add coacoa/* to .gitignore.  
Orchestrator stages changes; you commit/push.  

### ⚙ coacoa.yaml — key highlights
```yaml
paths:                             # where artefacts live
    analysis: context/analysis.md
    module_map: context/intelligence/module_map.json
    build_info: context/intelligence/build_info.json
limits:                            # token / LOC budgets
    max_snippet_loc: 120
    max_tokens_context: 12000
workflows:
    greenfield: workflows/default_greenfield.yml
    brownfield: workflows/default_brownfield.yml
quality:
    anti_hallucination: quality/anti_hallucination.md
docs:
    adr_dir: docs/adr/              # Architecture Decision Records
    file_prefixes:
story: "s_"                     # s_001_01.md
epic:  "e_"                     # e_001.md
```

(Full schema lives in the file itself.)

## 💬 Command palette (Claude Code / Cline)

| Slash command | Agent invoked | When you use it |  
| - | - | - |  
| /analyze-codebase | Code-Explorer | First step in brown-field repo |  
| /analyst init | Analyst | First step in green-field idea |  
| /pm new-prd | PM | Generate / refresh PRD |  
| /ux-designer make-ui | UX-Designer | Add UI flows & a11y notes |  
| /po refine-epics | Product Owner | Rank epics, create backlog |  
| /architect finalize-arch | Architect | Produce architecture doc & ADRs |  
| /scrum-master create | Scrum-Master | Split epics into stories |  
| /dev implement <story> | Developer | Work a single story |  
| /qa review | QA | Validate Dev’s story |  
| /orchestrator run | Orchestrator | Drive Dev → QA for next story |  

*(Run /orchestrator log anytime to see pipeline status.)*  

## 🚀 Green-field walk-through (idea → app)

```text
/analyst init    "Real-time expense tracker for remote teams"
/analyst         # responds with clarifying questions
→  You answer those questions until ✔ Open-Questions list is empty

/pm new-prd
    ↳ prd.md + initial epics e_001.md … e_n.md
/ux-designer make-ui
    ↳ ui_ux.md with wireframes + a11y notes
/po refine-epics
    ↳ backlog.md (ranked)
/architect finalize-arch
    ↳ architecture.md + docs/adr/2025-07-26-db-choice.md
/scrum-master create
    ↳ stories/s_001_01.md …
/orchestrator run
    ⇒ feature/s_001_01 branch staged
    ⇒ Dev builds, tests (≥ 90 % coverage), updates story footer
    ⇒ QA validates, appends report
Human: git commit -m "story s_001_01 – user onboarding" && git push
```  

#### Notes
•	"/analyst init `"<one-sentence product idea>"`  *– You can supply a single-line vision statement inline, or just run /analyst init and paste whatever raw notes you have.*  
•	The Analyst will always ask follow-up questions until its Open-Questions list is empty; that guarantees the PM starts with a complete domain doc.  
•	Everything after the Analyst step remains identical to the original workflow.  

## 🔧 Brown-field quick-start

```bash
git clone <legacy-repo>
cp -r coacoa/ CLAUDE.md .clinerules .
echo "coacoa/" >> .gitignore
/analyze-codebase         # CIS artefacts + build_info.json
/pm new-prd               # aligns PRD with real modules
/po refine-epics
/architect finalize-arch  # breaks cycles, writes ADR
/scrum-master create
/orchestrator run
```

*Branch rule  
Each story = its own branch feature/s_<id> staged only.  Humans merge to  
trunk after review → zero surprise refactors.*  

### ✅ Quality gates snapshot
•	Build-Integrity – build, test, lint run before QA (B-1…B-5).  
•	Coverage – ≥ 90 % lines for touched files; delta tracked in story footer.  
•	Anti-Hallucination – 12-point symbol & path sanity.  
•	Arch-Integrity – no dependency cycles, ADRs linked.  
•	SOLID (pragmatic) – SRP & OCP hard-enforced; others advisory via ADR.  

### 🧑‍🎓 Extending CoaCoA
•	Add a new agent: drop agents/<name>.md, reference it in a workflow YAML.  
•	Add a new quality gate: create checklist in quality/, list it under agent’s checks:.  
•	Swap LLM: change llm.default in coacoa.yaml.  

### 🤔 FAQ

Q: Why no auto-commit?  
A: Corporate compliance often requires human sign-off; CoaCoA stages but never commits.  

Q: Will stories bloat token context over time?  
A: Micro-context is capped to max_snippet_loc (120 LOC); old modules are referenced by path, not pasted.  

Q: Can I lower coverage?  
A: Yes—set quality.target_coverage in a future release, but 90 % is the sane default for v0.1.  

⸻

### ✍ Contributing
1.	Fork, branch fix/<topic>.  
2.	Run /orchestrator run on sample examples/petclinic_py.  
3.	Ensure all checklists pass.  
4.	PR with linking ADR if changing architecture.  

⸻

**© Licence**

*Apache-2.0 (see LICENSE).*

*Happy shipping! :-)*
>>>>>>> 38d1138 (INITIAL COMMIT: SHASHANK)
