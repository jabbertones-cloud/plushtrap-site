# GITHUB ACCOUNTS + STAY LOCAL — READ THIS FIRST, EVERY SESSION

**STOP.** Before any `git commit`, `git push`, `vercel deploy`, or any deploy command: verify the GitHub account. Using the wrong one wastes tokens and breaks builds. Scott has called this out repeatedly. This block is the source of truth and lives at the TOP of CLAUDE.md in every repo.

## Canonical account per repo

| Repo | `git config user.email` | GitHub account |
|---|---|---|
| exotic-soda | scott@openclaw.ai | openclaw (scott) |
| plushtrap | scott@openclaw.ai | openclaw (scott) |
| plushtrap-site | scott@openclaw.ai | openclaw (scott) |
| v0-skyn-patch | v0skynpatch | v0skynpatch |
| jabbertones-cloud | [RECORD FIRST TIME — DO NOT GUESS] | [RECORD FIRST TIME — DO NOT GUESS] |
| any repo not in this table | STOP and ask Scott | STOP and ask Scott |

## Hard rules (do not negotiate)

1. **Never guess.** Repo not in table = STOP and ask. Do not try one to see what happens.
2. **Verify before commit.** `cd <repo> && git config user.email` must match the table. Set per-repo with `git config user.email <value>`. Never rely on global config.
3. **One failed push = STOP.** Never rotate accounts to retry. Rotating is the token-burn loop Scott has called out explicitly.
4. **First time in a new repo: add it to this table BEFORE committing.** Writing it down later = writing it down never. Do not stash it in some obscure `.gitignored` file you'll never find again.
5. **STAY LOCAL is the default.** No `vercel deploy`, no `git push`, no `wrangler deploy`, no `npm run deploy` unless Scott explicitly asks in the current message. "Finish the task" = local edits + local typecheck, nothing else.
6. **Do not hide this block.** It lives at the TOP of `CLAUDE.md` in every repo, tracked in git, NOT in a dotfile, NOT in `.claude/`, NOT gitignored. If you can't find the account mapping from memory, the first thing to do is open `CLAUDE.md` in the repo root.

## Incident history

- exotic-soda task #7: committer email corrupted to `2/dev/null`, blocked Vercel. Fix: reset to `scott@openclaw.ai`.
- exotic-soda task #20: Vercel author authorization failed. Fix: commit with `scott@openclaw.ai`.
- Multiple sessions have rediscovered the jabbertones-cloud account because nobody wrote it down. **Write it down the first time it's used.**

---
