# PR Review Pipeline Labels

This document lists the labels that the PR review pipeline (`claude-triage.yml`, `claude-code-review.yml`, `claude.yml`) reads or writes. Cam runs the create commands manually the first time after merge.

> Use `gh label create` for the initial setup. Already-present labels can be updated with `gh label edit`. The `--force` flag on `gh label create` will create-or-update in one shot if you don't care about preserving manual color/description edits.

## Domain labels (set by triage)

| Label | Color | Description |
|---|---|---|
| `review:docs` | `0e8a16` | PR touches technical docs (`content/docs/`, `content/learn/`, `content/tutorials/`, `content/what-is/`). |
| `review:blog` | `a2eeef` | PR touches blog posts or customer stories (`content/blog/`, `content/customers/`). |
| `review:infra` | `d4c5f9` | PR touches workflows, scripts, infrastructure code, Makefile, or build/bundling config. |
| `review:programs` | `fbca04` | PR touches example programs under `static/programs/`. |
| `review:trivial` | `c2e0c6` | Tiny prose-only change. Skips Claude review entirely; lint still runs. |
| `review:mixed` | `bfd4f2` | PR touches more than one domain. Each file is reviewed under its domain. |

## Signal labels (set by triage)

| Label | Color | Description |
|---|---|---|
| `fact-check:needed` | `e99695` | PR introduces factual claims (versions, APIs, commands, features) — fact-check runs alongside review. |
| `agent-authored` | `5319e7` | PR is AI-authored or AI-assisted. Used as a signal during human adjudication; does not change which review runs. |
| `needs-author-response` | `f7c6c7` | Review surfaced unverifiable claims; author needs to provide sources or fix. |
| `review:prose-flagged` | `fef2c0` | Trivial PR where triage's prose-check pass found possible spelling/grammar issues. See the `<!-- TRIAGE_PROSE -->` comment. |

## State labels (set by review workflow)

| Label | Color | Description |
|---|---|---|
| `review:claude-working` | `c5def5` | Claude is running a review right now. Auto-removed when the run finishes. |
| `review:claude-ran` | `1d76db` | Claude review has completed for this PR's current state. |
| `review:claude-stale` | `ededed` | New commits landed since the last Claude review; refresh on next ready-transition or `@claude` mention. |

## Create them all (`gh` one-liner)

Run from a clone of `pulumi/docs` with `gh` authenticated as a user with write access:

```bash
gh label create "review:docs"            --color 0e8a16 --description "PR touches technical docs"
gh label create "review:blog"            --color a2eeef --description "PR touches blog posts or customer stories"
gh label create "review:infra"           --color d4c5f9 --description "PR touches workflows, scripts, infra, Makefile, or build config"
gh label create "review:programs"        --color fbca04 --description "PR touches static/programs/"
gh label create "review:trivial"         --color c2e0c6 --description "Tiny prose-only change; skips Claude review"
gh label create "review:mixed"           --color bfd4f2 --description "PR touches more than one domain"
gh label create "fact-check:needed"      --color e99695 --description "PR introduces factual claims; fact-check runs"
gh label create "agent-authored"         --color 5319e7 --description "AI-authored or AI-assisted; signal for human adjudication"
gh label create "needs-author-response"  --color f7c6c7 --description "Review surfaced unverifiable claims; author owes a response"
gh label create "review:prose-flagged"   --color fef2c0 --description "Trivial PR where triage's prose-check found possible spelling/grammar issues"
gh label create "review:claude-working"  --color c5def5 --description "Claude is running a review right now; auto-removed when the run finishes"
gh label create "review:claude-ran"      --color 1d76db --description "Claude review has completed for this PR's current state"
gh label create "review:claude-stale"    --color ededed --description "New commits since last Claude review; refresh on next ready-transition or @claude mention"
```

Add `--force` to any of the above to update an existing label in place. To remove a stale label later: `gh label delete "<name>" --yes`.
