# PR Review Pipeline Labels

This document lists the labels that the PR review pipeline (`claude-triage.yml`, `claude-code-review.yml`, `claude.yml`) reads or writes. Cam runs the create commands manually the first time after merge.

> Use `gh label create` for the initial setup. Already-present labels can be updated with `gh label edit`. The `--force` flag on `gh label create` will create-or-update in one shot if you don't care about preserving manual color/description edits.

## Domain labels (set by triage)

Informational signal labels — surfaced for human filterability. Routing in CI is path-based (`docs-review:references:domain-routing`); these labels do not gate workflow logic.

Every triaged PR carries exactly one of these, `domain:other` included, so **the absence of a `domain:` label means triage never ran** — the PR was opened as a draft and hasn't been marked ready, the author lacks write access, or the classifier errored. It never means "triage ran and had nothing to say."

| Label | Color | Description |
|---|---|---|
| `domain:docs` | `0e8a16` | PR touches technical docs (`content/docs/`, `content/what-is/`). |
| `domain:blog` | `a2eeef` | PR touches blog posts or customer stories (`content/blog/`, `content/case-studies/`). |
| `domain:infra` | `d4c5f9` | PR touches the build and deploy pipeline: workflows, scripts, infrastructure code, Makefile, build/bundling config. The v3 matrix routes it to the tools team and requires a staging run. |
| `domain:frontend` | `7057ff` | PR touches the site's rendering layer: `layouts/`, `theme/`, `assets/`, `static/` (except programs), plus the hero-animation and color-token data files. Reviewed under the infra criteria (Hugo correctness, dark-mode pass) but the v3 matrix routes it to marketing, with no staging run. |
| `domain:programs` | `fbca04` | PR touches example programs under `static/programs/`. |
| `domain:website` | `c5def5` | PR touches marketing, pricing, legal, or competitive landing pages (any other `content/**.md`), or the site-chrome / pricing data files that render on them. |
| `domain:mixed` | `bfd4f2` | PR touches more than one domain. Each file is reviewed under its domain. |
| `domain:other` | `ededed` | PR touches no domain-specific path (generated `data/` files, `styles/`, `archetypes/`, `.claude/`, non-workflow `.github/` files, repo-root dotfiles). Reviewed under shared criteria only; the v3 matrix routes it to the tools team. Applied only when nothing else matched, so it never appears beside another `domain:` label. Content-serving `data/` files (docs nav, blog taxonomies, author bios, pricing matrix) classify with their content instead — see `docs-review:references:domain-routing`. |

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
| `review:waived` | `d93f0b` | **Break-glass.** A human deliberately waived the v3 merge gates (Sentinel concludes success, except infra staging evidence, which is never waivable). Actor and reason are logged to the waive ledger and the waive rate is tracked — apply it on purpose, in an incident, not to skip the answer loop. Applied by humans only; never by automation. |
| `review:author-stalled` | `fad8c7` | The PR has been waiting on its author (unanswered findings or a standing changes-requested review) for 14+ days. Applied and cleared by the SLA sweep; the PR closes at 21 days if nothing changes, with one-click reopen. |

The six `review:*` state labels are **mutually exclusive**. Setting one removes the others. `set-review-label.sh` (under `.claude/commands/docs-review/scripts/`) enforces this atomically and supports a `--clear` mode that strips any state label without adding a new one (used by claude-triage.yml's `if: always()` cleanup).

> **Before merging a change that introduces a new label:** create it first. Triage applies its whole ADD set in a single `gh pr edit --add-label a,b,c` call, and `gh` rejects the entire call if any one name doesn't exist in the repo — the workflow's `|| true` then swallows it, so the other labels in that batch go missing too, silently.

## Opt-in labels (set by humans)

| Label | Color | Description |
|---|---|---|
| `surface:v3` | `5319e7` | Opt this PR into the v3 review surface (author card + reviewer brief + evidence page) regardless of the `REVIEW_V3_COMMENTS` repo variable — the per-PR dark-launch and rollback lever. Add it to a draft and mark ready, or add it and comment `@claude #new-review`; remove it and `#new-review` again to return to the monolith. Read by the initial review lane and the `/resolve` listener; the update lane follows whichever cards are on the PR. Not a `review:*` state label — triage and the reconcile job never touch it. Redundant once `REVIEW_V3_COMMENTS` is `'1'`; retire it (and `REVIEW_V3_BOT_PRS`) after that flip has soaked. |

## Content-review class labels (set by the content-review workflow)

`content-review-article.yml` applies one of these to every bot content-review PR it opens, from `scripts/content-review/publish-gate.py`'s class verdict. Informational, and the record the v3 auto-merge job reads alongside the Sentinel verdict. The workflow's `gh pr edit --add-label` is fail-open, so the labels have to exist or the class is silently invisible (it was, until 2026-09-11).

| Label | Color | Description |
|---|---|---|
| `content-review/deterministic` | `c5def5` | Every applied fix is deterministic-class (link, Vale, frontmatter); the workflow arms GitHub auto-merge at publish. |
| `content-review/judgment` | `bfd4f2` | At least one judgment-class fix; opens un-armed and needs a human eye. |
| `content-review/glow-up` | `d4c5f9` | A whole-article glow-up from the glow-up lane. |

## Create them all (`gh` one-liner)

Run from a clone of `pulumi/docs` with `gh` authenticated as a user with write access:

```bash
gh label create "surface:v3"             --color 5319e7 --description "Opt this PR into the v3 review surface regardless of REVIEW_V3_COMMENTS"
gh label create "domain:docs"            --color 0e8a16 --description "PR touches technical docs"
gh label create "domain:blog"            --color a2eeef --description "PR touches blog posts or customer stories"
gh label create "domain:infra"           --color d4c5f9 --description "PR touches the build/deploy pipeline: workflows, scripts, infrastructure, Makefile, build config"
gh label create "domain:frontend"        --color 7057ff --description "PR touches Hugo templates, theme sources, or site assets (layouts/, theme/, assets/, static/)"
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
gh label create "review:waived"          --color d93f0b --description "Break-glass: a human waived the v3 merge gates; actor and reason are logged"
gh label create "review:author-stalled"  --color fad8c7 --description "Waiting on the author 14+ days; closes at 21 days, one-click reopen (SLA sweep)"
gh label create "content-review/deterministic" --color c5def5 --description "Content-review PR whose fixes are all deterministic-class (links, Vale, frontmatter)"
gh label create "content-review/judgment"      --color bfd4f2 --description "Content-review PR containing judgment-class fixes (needs a human eye)"
gh label create "content-review/glow-up"       --color d4c5f9 --description "Content glow-up PR (whole-article polish)"
```

## Migrate from the old two-label scheme

If a repo still carries the legacy `review:claude-ran` / `review:claude-stale` labels, run once:

```bash
gh label edit "review:claude-stale" --name "review:stale"  # preserve any PRs already marked
gh label delete "review:claude-ran" --yes
```

Then create the new labels above. `set-review-label.sh` will atomically move PRs from any state to the correct new state on their next workflow run.

Add `--force` to any of the above to update an existing label in place. To remove a stale label later: `gh label delete "<name>" --yes`.
