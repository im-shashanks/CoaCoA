# Task: shard_doc

1. Read PRD and Architecture docs.
2. Generate epics & stories with IDs using `file_prefixes.story` and `file_prefixes.epic`.
3. For *each story*:
   - Embed only micro-context snippets (≤ `limits.max_snippet_loc` LOC).
   - Link to exact file paths & function names.
4. Apply anti-hallucination checklist.
