---
story_id: "{{id}}"
epic_id: "{{epic_id}}"
priority: "{{priority}}"
component: "{{component}}"
depends_on: []
micro_context:
  - file: "{{path}}"
    start: {{line_start}}
    end: {{line_end}}
limits:
  max_snippet_loc: "{{cfg.limits.max_snippet_loc}}"
acceptance_criteria:
  - …
definition_of_done:
  - Unit tests cover new code ≥ 90 %
  - Lint & type check pass
  - Docs updated
---

branch: "feature/{{story_id}}"

# Story {{id}} — {{title}}

## Description
(1–2 sentences)

## Description
(1–2 sentences)

## 🛠 Dev Setup
git switch -c {{branch}} || git switch {{branch}}
Run locally:
  ```shell
  {{build_info.commands.build}}
  {{build_info.commands.test}}
  ```

## 🧪 Test Stub
Create/modify file `tests/unit/test_{{story_id}}.py`:
  ```python
  def test_should_{{slug}}():
      # replace with real assertions
      assert False, "implement me"
  ```

## Implementation Hints
(Reference micro-context; note new files)

## Test Plan
- [ ] …