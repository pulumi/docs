---
name: docs-review
description: Review docs and blog post quality before committing (style, accuracy, Pulumi best practices). Use when you've made content changes locally and want a quality pass on open files, the current branch, or a specific PR — outputs to the conversation, never posts to GitHub.
user-invocable: true
---

# Docs Review (interactive)

Output goes into the conversation. This skill never posts to GitHub.

## Usage

`/docs-review [PR_NUMBER]`

If `PR_NUMBER` is provided, review the PR via `gh pr view` / `gh pr diff`. If omitted, auto-detect scope from the current IDE/terminal context.

## Scope detection (when no PR number is provided)

Walk these steps in order; stop at the first that yields a scope.

1. **Open files in the IDE.** Check the conversation context for system reminders that list open files. If any are present, treat those files as the scope.
2. **Uncommitted changes.** Check the gitStatus block (or run `git status`) for modified (`M`) and untracked (`??`) files. Use `git diff` and read the affected files.
3. **Branch changes vs. master:**

    ```bash
    git diff $(git merge-base --fork-point master HEAD)...HEAD
    ```

    If `--fork-point` fails (no reflog), fall back to `git diff $(git merge-base master HEAD)...HEAD`. Review every changed file in the branch.

## Performing the review

Route each file to a domain via `docs-review:references:domain-routing`, then apply that domain's criteria plus `docs-review:references:shared-criteria`. Render the output per `docs-review:references:output-format`.

For files under `content/docs/` or `content/blog/`, also run Vale and surface its findings per the Style-findings render contract in `docs-review:references:output-format`: entries with `"blocker": true` (near-zero-false-positive correctness rules) go in 🚨 Outstanding as `[style-blocker]` bullets; everything else goes under ⚠️ Low-confidence (the `**line N:** [style] _category_ — <message>` bullet form, grouped under a `#### Style findings` H4, always collapsed, not counted). Pipe through the categorize filter so the JSON has a deterministic `category` field — never surface the raw rule name:

```bash
vale --no-exit --output=JSON <files> > /tmp/vale-raw.json
python3 .claude/commands/docs-review/scripts/vale-findings-filter.py \
    --in /tmp/vale-raw.json --out /tmp/vale-findings.json
# Render bullets from /tmp/vale-findings.json: use .category, not .rule.
```

Omit `--pr` in interactive mode (no diff to intersect; the filter accepts all findings, categorizes, caps). If `vale --version` fails or `vale` is not on PATH, skip the Vale step with a one-line note (e.g., "Skipping Vale: not installed. Install via `mise install` to enable style nits.") and continue the review without Vale findings — don't hard-fail.

For PR-number invocations:

```bash
gh pr view {{arg}} --json title,body,files,additions,deletions,labels
gh pr diff {{arg}}
```

Format for terminal display. Include the scope in the summary, and offer to broaden if useful.

## Outcome telemetry (quarterly review)

Every closed PR's pinned review encodes what happened to its findings (✅ Resolved = fixed, `concede:` = conceded, `🛡️ Disputed … model held` = disputed, still-🚨-at-merge = ignored). `scripts/scrape-review-outcomes.py` derives per-finding outcomes from that structure; the weekly digest (`scripts/weekly-digest/digest.py`) aggregates the trailing week automatically. Quarterly, run the long-window tuning report:

```bash
uv run .claude/commands/docs-review/scripts/scrape-review-outcomes.py \
    --closed-since <quarter-start> --stats
```

What to do with the numbers: verdict categories with high **concede** or **ignored-at-merge** rates are candidates for demoting from the always-🚨 carve-out list (or pruning entirely — edit `docs-review:references:output-format` §Bucket rules in a PR); recurring prose findings with high **fix** rates are candidates for promotion into Vale rules so they're caught pre-review. High `unconfirmed_at_merge` counts mean reviews are routinely stale at merge — evidence for auto-refreshing on trivial deltas. Telemetry informs the tuning; humans make the edits.
