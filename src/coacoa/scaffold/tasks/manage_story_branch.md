# Task · manage_story_branch
_Assigned to: Orchestrator_

Inputs: `story_id`

Steps
1. Derive branch name: `feature/{{story_id}}`.
2. Run:
   ```shell
   git switch -c feature/{{story_id}}
   ```
   If branch exists: git switch feature/{{story_id}}.
   if not cfg.branching.auto_create:
        log(\"➟ Skipping branch creation (auto_create=false)\")
        return
3. After Dev finishes and Build-OK: true is present, run:
    git add --all
    git status --short  # show to user
4.	Stop! Do **NOT** commit or push; human developer reviews & commits.

Return BRANCH_READY feature/{{story_id}}.