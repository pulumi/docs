# PR Review Pipeline Labels

This document lists the labels that the PR review pipeline (`claude-triage.yml`, `claude-code-review.yml`, `claude.yml`) reads or writes. Cam runs the create commands manually the first time after merge.

> Use `gh label create` for the initial setup. Already-present labels can be updated with `gh label edit`. The `--force` flag on `gh label create` will create-or-update in one shot if you don't care about preserving manual color/description edits.

## Domain labels (set by triage)

Informational signal labels — surfaced for human filterability. Routing in CI is path-based (`docs-review:references:domain-routing`); these labels do not gate workflow logic.

Every triaged PR carries exactly one of these, `domain:other` included, so **the absence of a `domain:` label means triage never ran** — the PR was opened as a draft and hasn't been marked ready, the author lacks write access, or the classifier errored. It never means "triage ran and had nothing to say."

| Label | Color | Description |
|---|---|---|
| `domain:docs` | `0e8a16` | PR touches technical docs (`content/docs/`, `content/tutorials/`, `content/what-is/`). |
| `domain:blog` | `a2eeef` | PR touches blog posts or customer stories (`content/blog/`, `content/case-studies/`). |
| `domain:infra` | `d4c5f9` | PR touches workflows, scripts, infrastructure code, Makefile, build/bundling config, or the site build pipeline (`layouts/`, `assets/`, `theme/`, `static/`). |
| `domain:programs` | `fbca04` | PR touches example programs under `static/programs/`. |
| `domain:website` | `c5def5` | PR touches marketing, pricing, legal, or competitive landing pages (any other `content/**.md`). |
| `domain:mixed` | `bfd4f2` | PR touches more than one domain. Each file is reviewed under its domain. |
| `domain:other` | `ededed` | PR touches no domain-specific path (`data/`, `styles/`, `archetypes/`, `.claude/`, non-workflow `.github/` files, repo-root dotfiles). Reviewed under shared criteria only. Applied only when nothing else matched, so it never appears beside another `domain:` label. |

## Workflow-state labels

Load-bearing — these gate workflow execution.

| Label | Color | Description |
|---|---|---|
| `review:trivial` | `c2e0c6` | Tiny prose-only change. Skips Claude review entirely; lint still runs. Set by triage. |
| `review:frontmatter-only` | `e0f5d8` | Hugo content `.md` files where every change is inside the frontmatter block. Skips Claude review; lint still runs. Set by triage. |
| `review:oversized` | `f9d0c4` | Diff exceeds the automated review budget (>15K changed lines or >150 files — in practice generated corpora). Skips Claude review; triage posts a `<!-- TRIAGE_OVERSIZED -->` advisory comment. Set by triage. |
| `review:prose-flagged` | `fef2c0` | Trivial or frontmatter-only PR where triage's prose-check pass found possible spelling/grammar issues. See the `<!-- TRIAGE_PROSE -->` comment. Set by triage. |
| `review:triaging` | `e8db95` | Claude Triage is currently classifying the PR (domain routing, trivial/frontmatter-only short-circuit). Visible from PR-open until triage finishes (~10-60s). |
| `review:in-progress` | `fbca04` | Claude review is currently running for this PR's current state. |
| `review:outstanding-issues` | `b60205` | Claude review completed and 🚨 Outstanding contains at least one author-actionable finding. |
| `review:no-blockers` | `0e8a16` | Claude review completed cleanly — 🚨 Outstanding is empty. |
| `review:stale` | `ededed` | New commits landed since the last Claude review; refresh on next ready-transition or `@claude` mention. |
| `review:error` | `e11d21` | Workflow failed before publishing a review. See the Actions logs. |
| `needs-author-response` | `f7c6c7` | Review surfaced unverifiable claims; author needs to provide sources or fix. Applied by `pr-review`. |

The six `review:*` state labels are **mutually exclusive**. Setting one removes the others. `set-review-label.sh` (under `.claude/commands/docs-review/scripts/`) enforces this atomically and supports a `--clear` mode that strips any state label without adding a new one (used by claude-triage.yml's `if: always()` cleanup).

> **Before merging a change that introduces a new label:** create it first. Triage applies its whole ADD set in a single `gh pr edit --add-label a,b,c` call, and `gh` rejects the entire call if any one name doesn't exist in the repo — the workflow's `|| true` then swallows it, so the other labels in that batch go missing too, silently.

## Create them all (`gh` one-liner)

Run from a clone of `pulumi/docs` with `gh` authenticated as a user with write access:

```bash
gh label create "domain:docs"            --color 0e8a16 --description "PR touches technical docs"
gh label create "domain:blog"            --color a2eeef --description "PR touches blog posts or customer stories"
gh label create "domain:infra"           --color d4c5f9 --description "PR touches workflows, scripts, infra, Makefile, build config, or the site build pipeline"
gh label create "domain:programs"        --color fbca04 --description "PR touches static/programs/"
gh label create "domain:website"         --color c5def5 --description "PR touches marketing, pricing, legal, or competitive landing pages"
gh label create "domain:mixed"           --color bfd4f2 --description "PR touches more than one domain"
gh label create "domain:other"           --color ededed --description "PR touches no domain-specific path; reviewed under shared criteria only"
gh label create "review:trivial"         --color c2e0c6 --description "Tiny prose-only change; skips Claude review"
gh label create "review:frontmatter-only" --color e0f5d8 --description "Frontmatter-only Hugo content edit; skips Claude review"
gh label create "review:oversized"       --color f9d0c4 --description "Diff too large for automated review (generated corpora); skips Claude review"
gh label create "review:prose-flagged"   --color fef2c0 --description "Triage's prose-check found possible spelling/grammar issues on a short-circuited PR"
gh label create "review:triaging"        --color e8db95 --description "Claude Triage is currently classifying the PR"
gh label create "review:in-progress"     --color fbca04 --description "Claude review is currently running"
gh label create "review:outstanding-issues" --color b60205 --description "Claude review completed; 🚨 Outstanding has author-actionable findings"
gh label create "review:no-blockers"     --color 0e8a16 --description "Claude review completed cleanly; 🚨 Outstanding is empty"
gh label create "review:stale"           --color ededed --description "New commits since last Claude review; refresh on next ready-transition or @claude mention"
gh label create "review:error"           --color e11d21 --description "Workflow failed before publishing a review; see Actions logs"
gh label create "needs-author-response"  --color f7c6c7 --description "Review surfaced unverifiable claims; author owes a response"
```

## Migrate from the old two-label scheme

If a repo still carries the legacy `review:claude-ran` / `review:claude-stale` labels, run once:

```bash
gh label edit "review:claude-stale" --name "review:stale"  # preserve any PRs already marked
gh label delete "review:claude-ran" --yes
```

Then create the new labels above. `set-review-label.sh` will atomically move PRs from any state to the correct new state on their next workflow run.

Add `--force` to any of the above to update an existing label in place. To remove a stale label later: `gh label delete "<name>" --yes`.
