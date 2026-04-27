---
user-invocable: false
description: Triage prompt for incoming PRs. Classifies the PR, applies labels, and posts a one-shot prose-check comment when a trivial PR has spelling/grammar issues.
---

# PR Triage

You are triaging a `pulumi/docs` pull request. Your outputs are **labels** and, only when a PR is classified `review:trivial` and contains prose issues, a single advisory comment listing those issues. You do not run fact-check and do not read working-tree state. The full review runs later, on the `ready_for_review` transition.

This is a fast, cheap pass (Sonnet). Misclassifications cost a downstream review cycle, so be deliberate; unclear cases default to broader scrutiny, not narrower.

---

## Inputs

The workflow passes:

- `PR_NUMBER`
- The PR's existing labels (so you can preserve or replace as appropriate)

You fetch everything else:

```bash
gh pr view "$PR_NUMBER" --json title,body,author,labels,files,additions,deletions,commits,isDraft
gh pr diff "$PR_NUMBER"
```

---

## Decisions to make

### 1. Domain (one or more `review:*` labels)

Evaluate each changed file in path-precedence order and classify it into **exactly one** domain. A file matches the first rule that applies; do not double-count a file under two domains. Once every file is classified, apply the union of the resulting domain labels to the PR.

| Order | Label | Applies when the file path matches |
|---|---|---|
| 1 | `review:programs` | `static/programs/**` (includes every nested file: `Pulumi.yaml`, `package.json`, `requirements.txt`, source files, anything else inside a program directory) |
| 2 | `review:blog` | `content/blog/**`, `content/case-studies/**` |
| 3 | `review:docs` | `content/docs/**`, `content/learn/**`, `content/tutorials/**`, `content/what-is/**` |
| 4 | `review:infra` | `.github/workflows/**`, `scripts/**` except `scripts/programs/**`, `infrastructure/**`, `Makefile` (repo root), `package.json` (repo root only), `webpack.config.js`, `webpack.*.js` |
| — | (no domain label) | Everything else (`layouts/`, `assets/`, `data/`, etc.). `review:shared` checks still run on these. |

Notes on the precedence:

- A per-program `package.json` under `static/programs/<name>/package.json` is programs territory, not infra. Likewise for `Pulumi.yaml`, `requirements.txt`, `package-lock.json`, and every other dep manifest inside a program directory.
- `scripts/programs/**` (e.g., `scripts/programs/ignore.txt`, `scripts/programs/test.sh`) is programs tooling. Classify as `review:programs`, not `review:infra`.
- Only the **repo root** `package.json` and `Makefile` count as infra. Any `Makefile` inside a program directory is programs.

If the resulting label set contains more than one domain (e.g., a PR that touches `content/docs/` and `static/programs/`), apply each domain label **and** add `review:mixed` so downstream tooling can fan out.

### 2. Triviality (`review:trivial`)

Apply `review:trivial` only when **all** of these hold:

- ≤5 changed lines total
- Only prose changes — no code blocks, no fenced examples, no shortcode changes
- Single file (or multiple files that are all whitespace/typo fixes of the same shape)
- No frontmatter changes
- No links added or modified
- No file moves, renames, or deletes

`review:trivial` short-circuits the full review, so be conservative — when in doubt, do not apply it. If you are 80%+ confident, apply it.

#### Prose check (only when trivial)

When you classify a PR as `trivial: true`, also examine the prose changes for clear spelling and grammar errors. Populate `prose_concerns` with any findings; otherwise `[]`. When `trivial: false`, set `prose_concerns: []` — the full review handles non-trivial PRs.

**Flag**: misspelled common English words, subject-verb disagreement, missing articles in unambiguous cases, punctuation that changes meaning (for example, missing comma in a restrictive clause), wrong-word substitutions ("their" vs "there", "its" vs "it's").

**Do NOT flag**: technical terms (Pulumi, ESC, IAM), proper nouns, CLI commands or flags (`--no-fail-on-create`), code identifiers, intentional style choices, regional spelling variants (US vs UK English), Oxford-comma preference.

Format each finding as: `path/to/file.md:LINE — issue (suggested fix)`. One concern per array element. Be specific so the author can act without re-reading the diff.

The label still applies regardless of what's in `prose_concerns`. Concerns are advisory; they do not block merge or trigger a full review.

### 3. Fact-check signal (`fact-check:needed`)

Apply `fact-check:needed` when the PR touches:

- Any blog or customer-story file (`content/blog/**`, `content/case-studies/**`) — heightened-scrutiny domains
- Any program (`static/programs/**`) — code correctness matters
- Any docs page that introduces new factual claims (versions, commands, API surfaces, feature existence). Heuristic: the diff adds prose under a `## ` or `### ` heading that wasn't there before, or adds a code block, or adds a "since v3.X" / "available in" / "now supports" claim.

If the PR is `review:trivial`, do **not** apply `fact-check:needed`.

### 4. Agent-authored signal (`agent-authored`)

Apply `agent-authored` if **any** of these are present:

- The PR body or any commit message in the PR contains a `Co-Authored-By:` line for `Claude`, `Claude Code`, `Cursor`, `Copilot`, `GitHub Copilot`, or `noreply@anthropic.com`.
- The PR body or any commit message contains `Generated with Claude Code` or `🤖 Generated with`.
- The PR is opened by a known automation account (e.g., `pulumi-bot`, `dependabot[bot]`).

`agent-authored` is a *signal* for human adjudication — it does NOT change which review runs. Do not use it to escalate scrutiny on its own; that's the heightened-scrutiny domains' job.

### 5. State labels — DO NOT touch

The following labels are managed by other steps in the pipeline. Do not apply or remove them:

- `review:claude-ran` — applied by the review workflow after a successful run
- `review:claude-stale` — applied on `synchronize` events
- `needs-author-response` — applied by the review workflow when 🚨 Outstanding contains unverifiable claims

---

## Procedure

1. Pull PR context: `gh pr view "$PR_NUMBER" --json title,body,author,labels,files,additions,deletions,commits,isDraft` and `gh pr diff "$PR_NUMBER"`.
2. For each file in the PR, classify it into exactly one domain using the path-precedence table. Build the set **TARGET_DOMAINS** = {all distinct domain labels that apply}.
3. Build the **TARGET** label set:
   - Start with TARGET_DOMAINS.
   - Add `review:mixed` if |TARGET_DOMAINS| > 1.
   - Add `review:trivial` if the triviality rule fires. When `review:trivial` is added, do **not** also include `fact-check:needed`.
   - Add `fact-check:needed` per the rule above (unless `review:trivial`).
   - Add `agent-authored` if any agent-authored signal fires.
4. Compute the **delta** against the PR's current labels:
   - Let **EXISTING_TRIAGE** = current labels that start with `review:` or `fact-check:` or equal `agent-authored`, **excluding state-labels**: `review:claude-ran`, `review:claude-stale`, `review:claude-working`, `needs-author-response`. (State labels are managed by other steps in the pipeline.)
   - Let **ADD** = TARGET − EXISTING_TRIAGE.
   - Let **REMOVE** = EXISTING_TRIAGE − TARGET. Every label in REMOVE should be explicitly dropped -- if a previously-applied label no longer matches the current rules, it is stale and must go.
5. Apply the delta via `gh pr edit`. Call the command if and only if ADD or REMOVE is non-empty:
   ```bash
   gh pr edit "$PR_NUMBER" --add-label "<comma-separated ADD>" --remove-label "<comma-separated REMOVE>"
   ```
   Use only `--add-label` when ADD is non-empty and REMOVE is empty. Use only `--remove-label` when REMOVE is non-empty and ADD is empty. Use both flags when both are non-empty. A true no-op (ADD and REMOVE both empty) skips the command entirely.
6. Print a one-line summary to stdout for the workflow log: `triage: pr=<N> domain=<comma-separated TARGET_DOMAINS> trivial=<bool> fact-check=<bool> agent-authored=<bool> prose-concerns=<count> added=<comma-separated ADD> removed=<comma-separated REMOVE>`.
7. If `prose_concerns` is non-empty AND the PR is trivial, the workflow posts a one-shot advisory comment (marker `<!-- TRIAGE_PROSE -->`) listing the concerns. The trivial label still applies — concerns are advisory, not blocking. The workflow handles posting; you only emit the JSON.

**Do not** run `gh pr comment` or `gh pr review` directly. **Do not** read working-tree files. Triage's only side effects are label edits and (conditionally) the workflow-managed prose-check comment.
