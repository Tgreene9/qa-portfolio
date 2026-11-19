# Git cheat sheet – my branch → PR → merge loop

> Open in VS Code with **Ctrl+Shift+V** for a formatted preview.

## Where am I?

| Question | Command / place |
| --- | --- |
| Which branch am I on? | Bottom-left of the VS Code status bar, or `git branch` (`*` = current) |
| What changed? | `git status` |
| What did I change in a file? | `git diff` (or click the file in Source Control) |
| History as a graph | `git log --oneline --graph --all` (or **Git Graph** button in Source Control) |

## The loop (one per chunk of chapters)

### 1. Start from an up-to-date main

```bash
git switch main
git pull
git switch -c <branch-name>      # e.g. pytest-basics
```

### 2. Work and commit (after each chapter)

```bash
pytest                           # run tests first
git add .
git commit -m "Ch 1: first test case"
```

### 3. Push and open a PR

```bash
git push -u origin <branch-name>
```

On GitHub: **Compare & pull request** → title + short description (what changed, how it was tested) → **Create pull request** → wait for checks → **Merge** → **Delete branch**.

### 4. Clean up locally (VS Code does NOT do this for you)

```bash
git switch main                  # you can't delete the branch you're on
git pull                         # get the merged work
git branch -d <branch-name>      # delete the local branch
git fetch --prune                # forget branches deleted on GitHub
```

## Branch plan – TAU Introduction to pytest

| Chapters | Branch |
| --- | --- |
| 1–4 | `pytest-basics` |
| 5–6 | `pytest-classes-fixtures` |
| 7–9 | `pytest-config-filtering-plugins` |
| 10–11 | `pytest-api-ui` |

## Common errors

| Error | Meaning | Fix |
| --- | --- | --- |
| `branch 'x' not found` | That branch doesn't exist locally | `git branch` to see real names |
| `cannot delete branch 'x' used by worktree` | You're currently on `x` | `git switch main`, then delete |
| `branch 'x' is not fully merged` | `-d` safety check: work not merged into main | Merge the PR first (or `git pull` on main) |
| `Your branch is behind 'origin/main'` | GitHub has newer commits | `git pull` |
| `git` not recognized | Terminal opened before Git was installed | Restart VS Code |
| Push rejected (non-fast-forward) | Remote has commits you don't | `git pull`, then push again |

## Undo (safe ones)

| I want to… | Command |
| --- | --- |
| Discard changes to a file (not committed) | `git restore <file>` |
| Unstage a file | `git restore --staged <file>` |
| Fix the last commit message (not pushed yet) | `git commit --amend -m "new message"` |
| Undo a merged PR | **Revert** button on the PR in GitHub |

## One-time settings

```bash
git config --global fetch.prune true      # auto-prune on fetch/pull
git config --global init.defaultBranch main
```
