# review-v3 — deterministic machinery for the v3 PR review workflow

Scripts here implement the v3 review surface: S3-resident evidence, the two
pinned comments (author card + reviewer brief), the Sentinel merge gate, lane
routing, and the SLA sweep. Everything in this directory is deterministic —
no model calls. Model output enters only as validated artifacts.

Covered by `make test-review-pipeline` (pytest + standalone `test_*.py`
harnesses + `--self-test` flags), same contract as `scripts/content-review/`
and `scripts/blog-review/`.

## The evidence object (system of record)

One JSON object per (PR, head SHA), written by the credentialed record job in
`claude-code-review.yml` — never by the model. Comments are renderings of it.

- Bucket: the content-review ledger bucket (versioned, private), resolved from
  the `contentReviewLedgerBucketName` stack output, passed as
  `PR_REVIEW_EVIDENCE_URI` (e.g. `s3://content-review-ledger-…/pr-review`).
- Keys: `pr-review/<pr>/<head_sha>.json` (immutable per SHA — bucket
  versioning is the history) and `pr-review/<pr>/latest.json` (pointer +
  current disposition state, mirrored one-way from the PR's REVIEW_STATE
  block; the PR is the disposition source of truth, S3 is the telemetry/audit
  mirror).
- Other prefixes: `pr-review/waives/` (waive log), `pr-review/state/<pr>.json`
  (SLA-sweep actions), `pr-review/runs/<date>/` (immutable run records).
- Degradation contract (same as `scripts/content-review/record-review.py`):
  `PR_REVIEW_EVIDENCE_URI` unset ⇒ write local files + `::warning::`, never
  fail. The record job uploads the local copies as a workflow artifact either
  way (`if-no-files-found: error`), which is what the fork battery verifies.

Schema: `evidence-schema.json` in this directory is the documented contract;
`validate-evidence.py` is the enforcement (closed sets, evidence-required,
counts consistency). Bump `schema_version` on any breaking change and teach
readers both shapes for one transition window.

Downstream readers of `latest.json` beyond this directory: the glow-up lane's
`scripts/content-review/build-glowup-backlog.py` banks a content-review PR's
still-open / accepted-as-is / held findings and every `preexisting` row as
page debt (records reach its unprivileged worker via `select-glowup.py
--pr-review-dir`, which stamps them on the queue article).

### Finding IDs

`F<n>`, assigned by the composer in first-appearance order, monotonically
increasing per PR, never reused (the counter's high-water mark travels in the
evidence object). The update lane preserves existing IDs; new findings take
the next index. IDs are the join key across the author comment's checklist,
REVIEW_STATE, the evidence object, `/resolve`, and the Sentinel's red
messages.

### Buckets

- `outstanding` (🚨 must fix or refute — blocks)
- `author-answer` (❓ only the author can answer — blocks)
- `reviewer-check` (⚠️ reviewer should look before approving — advisory)
- `preexisting` (💡 not this PR's fault — optional)

The ⚠️→❓/⚠️ split is verdict-driven in the composer: `unverifiable` →
`author-answer`; `framing-drift`, low-confidence hunches, soft cross-sibling
mismatches → `reviewer-check`. The model may promote
(reviewer-check → author-answer → outstanding) with a stated reason, never
demote.

## The REVIEW_STATE block (disposition source of truth)

Lives as an HTML comment in the bot-owned author comment:

```
<!-- REVIEW_STATE {"schema":1,"high_water":7,"findings":{"F3":{"disposition":"refuted","note":"flag exists in 3.261","actor":"cnunciato","sha":"abc123","bulk":false,"updated_at":"2026-08-31T17:00:00Z"}}} -->
```

- Dispositions: `fixed | refuted | deferred | accepted | not-applicable`
  (note required for `deferred`/`accepted`/`not-applicable` — same closed set
  as `review-worklist.py`).
- Writers: the update lane (`apply-update.py`) and the `/resolve` workflow —
  both merge per finding-id, latest `updated_at` wins, never whole-block
  overwrite. `bulk: true` marks `/resolve all …` answers (telemetry).
- Readers: Sentinel gate 2 (uncredentialed, fork-safe), `review-worklist.py`
  (`--body-file` / `--brief-file`), the record job's mirror into `latest.json`.
- Sentinel accepts the block only from the bot-authored comment.

## The Sentinel

`sentinel.py` + `.github/workflows/review-sentinel.yml` publish the one
blocking check-run ("Sentinel"). Deterministic, no model, no AWS, and —
because the workflow runs on `pull_request_target` — **never checks out or
executes PR code** (test-enforced). Gates, each red message naming its fix:

| Gate | Green when | Red says |
|---|---|---|
| G1 review-ran | author card's `CLAUDE_REVIEW_HEAD` == head SHA; or mechanical (no *model* review required — the lane team still approves at G3); or a legacy v2 review current at head (grandfather note) | push / `@claude #update-review` / `#new-review` |
| G2 findings-answered | every 🚨/❓ row carrying a REVIEW_STATE disposition | the undecided ids + the `@claude … #update-review` phrasing (the `/resolve` lane stays as agent-facing plumbing, never user-facing copy) |
| G3 right-approver | an APPROVED latest review from a human, non-denylisted, active member of every matrix-required team | the team slug(s) needed |
| G4 infra-evidence | the PR changes no path on `staging_evidence.paths` (skip); or this exact head deployed to staging successfully at least once — either the `staging/pulumi-test-io` commit status is green, or a completed run of `testing-build-and-deploy.yml` at this head SHA succeeded | the deploy is dispatched automatically (`staging-deploy-auto.yml`); `/deploy-staging` retries — **not waivable** |
| G5 oversized-ack | `review:oversized` PRs: approval body contains `sentinel:oversized-ack` | explains the ack |

**G4's two witnesses.** The commit status is a *report* of the deploy, not
the deploy: it is a separate API call after `gh run watch` returns, so a
cancelled runner, a lost token, or a hand-run deploy that never went through
`/deploy-staging` all leave a green deploy with no status. `_staging_evidence`
therefore accepts either the status or a successful
`testing-build-and-deploy.yml` run at the same head SHA — the run record *is*
the deploy. The status is still written, because it is what shows in the
merge box with a link. A failed run-history read degrades to "no evidence"
(red), not `action_required`: red is already the conservative answer, and
escalating would misreport an API hiccup as a corrupt PR.

**What G4 applies to.** `staging_evidence.paths` in
`.github/review-routing.yml` — a path list, NOT a subject. It used to be a
`staging_evidence: required` cell on the matrix's `infra` row, which made the
approver and the blast radius the same question and left "bend the path's
domain" as the only way to narrow the gate. The list is the Pulumi program,
the build entry points, the scripts `make ci_push` actually runs, and the two
workflows that run it. A `domain:infra` path that the deploy merely *reads*
(`scripts/redirects/*.txt`) or never touches (an unrelated workflow, the lint
and link-check scripts) is still tools' to approve and no longer asks for a
~9-minute deploy of the shared stack. `routing.requires_staging_evidence()`
answers it per path; the matcher is segment-aware (`*` never crosses `/`)
because `fnmatch` would have made `scripts/*` match `scripts/redirects/`.

Evidence supply is `staging-deploy-auto.yml`: every same-repo, non-draft PR
that `route-pr.py` says needs staging evidence gets a deploy dispatched on
open / push, skipping when the head already has one. It shares the
`staging-stack` concurrency group with the comment lane and calls the same
`staging-deploy.sh`, so the two lanes cannot drift on what they produce.

Conclusions are explicit about the fails-open trap: any gate ERROR (corrupt
REVIEW_STATE, a team-membership lookup failure) concludes `action_required`
— never `neutral`/`skipped`, which GitHub counts as passing for required
checks.

**`review:waived` is authorized, not just labelled.** A waive skips every
gate but G4, so applying one has to be at least as privileged as approving
something: `_waive_state` reads the actor off the label event and honors the
waive only when they are an **active member of any team in `teams:`** — any
of them, not just the one the PR routes to. Scoping it to the required team
would make a waive exactly as hard to get as the approval it bypasses, which
kills the case it most needs to cover (the required approver is the author).
It fails closed at every step — unreadable actor, failed membership lookup,
actor on no routing team — and an unauthorized waive is *refused out loud*
in the summary rather than silently ignored, so the same person doesn't try
it twice. A red G4 still stands under an authorized waive.

**The pinned status comment.** `render_status_comment` / `update_status_comment`
upsert one `<!-- SENTINEL_STATUS -->` comment per PR: a row per gate with its
state and, for a red one, the gate's own remediation text. The body is a pure
function of the verdict — no timestamps, no run ids — so a re-evaluation that
changes nothing produces a byte-identical body and the PATCH is skipped. The
workflow passes `--status-comment` unconditionally and the evaluator decides:
enforcing mode always maintains it; report-only mode does so only for a PR
labelled `sentinel:preview`, so the dry run stays invisible to anyone who
didn't opt in. `content-review-article.yml` applies that label to every
content-review and glow-up PR, making those lanes the canary cohort — the
same pattern the v3 review comments used before they went repo-wide. A few
real PRs a day exercise the surface, on the lane whose author is a workflow
and whose reader is already reading the output. External contributors (fork head repo — never the
author's permission level, which is `none` for GitHub Apps like workprentice)
skip G1/G2 per config — the approving reviewer's review is the review. A
`review:trivial` PR that isn't mechanical (prose-flagged) passes G1/G2 on
triage's `<!-- TRIAGE_PROSE -->` comment instead of a review; G3 still needs
the human approver the demotion asked for. Rollout switch:
repo variable `REVIEW_V3_SENTINEL` is tri-state — unset = dark (no job, no
check-run, the review lanes skip their pokes; the state the file merges in),
`'report'` = report-only (conclusions `neutral` with "would be: …" in the
summary), `'1'` = enforcing. `/deploy-staging` follows the same switch. The
surface itself is `REVIEW_V3_COMMENTS` (repo-wide; the per-PR `surface:v3`
opt-in label and `REVIEW_V3_BOT_PRS` were retired 2026-09-14 once the
variable had soaked). The
check summary embeds the reviewer brief (merge-box delivery), and on red the
sentinel PATCHes a ⛔ strip into the author card naming the exact commands.

**SLA sweep** (`sla-sweep.py`, `review-sla-sweep.yml`, cron every 2 h): its own
switch is `REVIEW_V3_SLA` — the job runs only while it is `'1'` (a manual
dispatch defaults to `dry_run`). Clocks are derived fresh from the GitHub
timeline each sweep; only the actions taken are recorded, under
`pr-review/state/<pr>.json` (per-PR idempotency: warns, closes, escalations
keyed by clock epoch) and `pr-review/runs/<date>/<ts>.json` (immutable run
records the weekly digest reduces). **Before flipping the switch, create the
`review:author-stalled` label** (`.github/labels-pr-review.md` has the
`gh label create` line) — the sweep applies it on the first author warn.

Two lanes make G4's evidence, and a third records it.
`staging-deploy-auto.yml` dispatches a deploy for every infra PR on
open/push; `/deploy-staging` (`staging-deploy-pr.yml`, tools-team members
only, same-repo branches only) is the retry. Both dispatch the existing
testing deploy at the PR head branch and write the *pending*
`staging/pulumi-test-io` status at the deployed SHA. Deploys queue on the
shared staging stack in the comment lane; a superseded request gets a
comment saying to re-run.

`staging-status.yml` writes the *terminal* status — one writer, a
`workflow_run` listener on "Build and deploy testing" — and then pokes the
Sentinel so G4 is re-scored against the finished deploy. It lives outside
the dispatched run on purpose: a `workflow_dispatch` executes the workflow
file from the ref it is dispatched at, so the in-run job this replaces
silently did not exist for a PR branch cut before it merged (#21676). **The
rule: anything that must work for a PR branch of any age belongs in a
default-branch-triggered workflow** — `workflow_run`, `schedule`,
`pull_request_target`, or a dispatch pinned to the default ref. Its
`workflow_dispatch` entry (`run_id`, optional `pr_number`) backfills a
status for a deploy that already finished.

## Superseded handoffs

The model job hands its validated review to the credentialed publish job as
an artifact stamped with the SHA it checked out. `handoff_guard.py` compares
that SHA with the live PR head at publish time and returns one of three
actions; the workflow owns the side effects of each. `publish` is the normal
path. `redispatch` (head moved) rests the label at `review:stale`, cleans up
the spinner, check-run and any `#new-review` confirmation, and hands off to
the `redispatch` job, which waits for the head to be quiet for `SETTLE_S`
and dispatches a fresh review at it with `supersede_depth` incremented.
`rest` (head moved AND this run is already `MAX_DEPTH` re-dispatches deep)
stops there and rewrites the spinner to say how to refresh by hand. One full
review per supersession, never per push: re-triggering on `synchronize` and
letting `cancel-in-progress` sort it out would burn a partial model run for
every push in a train. Before this guard learned to reset the label (#21642)
a superseded publish exited 0 with `review:in-progress` still on the PR and
nothing scheduled to replace it; `review-label-reconcile.yml` now also sweeps
that orphan (in-progress for 30+ minutes with no live spinner comment).

## Lane routing

`.github/review-routing.yml` (repo root config, schema-versioned) maps
subject × change type → required approver team. Subjects come from
`classify_path()` (shared with triage) applied to **live file lists**, never
labels. `routing.py` fails closed on any config it cannot validate.

The same resolution has two consumers. The Sentinel resolves it itself from
live API state to decide what G3 requires. Triage resolves it through
`route-pr.py` and *requests* those teams as PR reviewers — each team once
per PR, on open / ready **or on the push that first makes it required**.

The rule is "ask a team that has never been asked on this PR", and the
distinction from "not currently requested" is load-bearing. Assignments stay
sticky: a team that reviewed (GitHub drops it from `requested_teams` when it
does) or that a human un-requested is never re-pinged, because a re-request
on every push is the notification noise v3 exists to remove. The test is
therefore the timeline's `review_requested` events, not the PR's current
`requested_teams`.

What that buys is the case the open/ready-only version missed. The Sentinel
resolves from live paths on every evaluation, synchronize included, so a
push that WIDENS the path set — a docs PR that grows a `layouts/` file —
introduced a required approver nobody had been told about. Under enforcement
that is an author blocked by a team that was never pinged, with nothing on
the PR saying so. A first request for a newly-required team is not a
re-request; it is the notification that was missing.
Rollout switch: repo variable `REVIEW_V3_ROUTING` — `'1'` turns on both the
reviewer request and triage's synchronize label-delta pass; unset (how it
ships) means a push runs no triage pass and no team is ever requested, so
the matrix is enforced at the merge box without anyone having been told.
The request needs the **org-scoped** `PULUMI_BOT_TOKEN` (minted from ESC in
`claude-triage.yml`): the `requested_reviewers` endpoint resolves `org/slug`
against the org, which the repo-scoped `GITHUB_TOKEN` cannot do. Without it
the step logs the teams it would have requested and routes nobody — it is an
assist, never a gate.

Subjects (closed set, all seven required in the matrix): `docs`, `blog`,
`website`, `programs` (docs-guild, the blog team, or marketing per the
matrix), `infra` — exactly the build and deploy pipeline (`infrastructure/`,
`.github/workflows/`, `scripts/`, Makefile, bundler config): tools approves
(a staging run is a separate, path-keyed question — see G4 above) —
`frontend` — the rendering layer (`layouts/`, `theme/`, `assets/`,
`static/`): reviewed under the infra criteria, approved
by marketing, never a staging run — and `other`, the classifier's fallback
(repo plumbing such as `.claude/`, `styles/`, generated `data/` files): tools
approves, so an infra PR that also touches plumbing dedupes to one team.
Content-serving `data/` files (docs nav, blog taxonomies, author bios, the
pricing matrix) classify with the content they serve; the map is
`CONTENT_DATA_EXACT` in `triage-classify.py`.

**Every governed PR is routed and needs a human approval.** `none` matrix
cells are a config error, so `resolve_lanes` always returns at least one
required role, triage always has a team to request, and G3 always has an
approver to wait for. `mechanical` skips the *model* review at G1 and
nothing else.

That is a reversal, and the reason is worth keeping: the Sentinel is not the
gate that decides mergeability. GitHub's required-review rule is, and it
does not read `review-routing.yml`. So the two shortcuts that used to mean
"no human" — a `none` cell and the `auto_approve` clean-brief rule — never
removed the human. They removed the *reviewer request*, told the author
nobody was needed, and left a PR that read green and could not merge until
somebody stamped it by hand. Both are deleted; `auto_approve` is a hard
config error now, and nothing ever consumed the `auto_approved` verdict
field it set.

One optional config block still shapes what the Sentinel governs:

- `not_governed:` — the automated processes the Sentinel does not gate at
  all (`authors:` matches the PR author alone, e.g. Dependabot;
  `author_label_pairs:` needs both, e.g. pulumi-bot + `automation/merge` for
  the generated-docs regens). The check concludes `success` titled "Not
  governed" with no gates evaluated and `governed: false` in the verdict
  JSON. What makes these safe is not that they are bots: it is that
  `auto-approve-for-auto-merge.yml` posts a real approval for that exact
  author+label pair and the generating workflow arms `gh pr merge --auto`,
  so they satisfy the repo's required-review rule for real. pulumi-bot's
  content-review, glow-up, and broken-link PRs carry no such label and are
  governed, routed, and need a human — as are `workprentice[bot]`'s,
  `github-copilot[bot]`'s, and `eon-pulumi-agent[bot]`'s.

`review:prose-flagged` (triage's Haiku + Vale pass on a short-circuited PR)
demotes a mechanical PR to substantive inside the Sentinel — the bar is pure
diff shape and cannot see labels.
The bar itself also refuses edition-feature rewrites Layer A cannot see:
any change under `content/docs/support/faq/` or `content/what-is/`, and any
added line naming an edition ("the Enterprise edition") or pairing
"edition(s)" with a feature verb. Those reasons demote only; the marketing
claims overlay still keys on the `pricing-sensitive` paths alone.

## The /pr-review queue

The maintainer skill `/pr-review` (`.claude/commands/pr-review/SKILL.md`) is
a batch adjudication surface over every open PR. Its deterministic half lives
here so it is covered by `make test-review-pipeline`; the model writes only
the per-row judgment calls, as a JSON file the analyzer merges.

| Script | Role |
|---|---|
| `gh_client.py` | GitHub adapter: `gh` subprocess, REST with `GITHUB_TOKEN`/`GH_TOKEN`, or a snapshot directory (`<dir>/GET/<endpoint>.json`; writes go to `writes.jsonl`). `search_author_q()` owns the `author:app/<slug>` rewrite for GitHub App authors. `record_dir=` mirrors live reads into the snapshot layout. |
| `pr_review_config.py` | `~/.pr-review.yml` (`me:` lanes, `stamp_max_lines`, `stale_date_days`, `link_fixes`); routing itself stays in `.github/review-routing.yml`. |
| `collect.py` | Facts → `.pr-review-queue.json`: PR metadata, files + patches, `mergeable_state` (re-asked while `unknown`), check rollup, reviews, the parsed pinned review (`review-worklist.py`, both surfaces), `REVIEW_STATE`, triage prose, reviewed-head SHA, preview URL + per-page links, trust axes / risk tier / AI-suspect (ported from the retired pr-review shell scripts). A legacy (v2) review too long for one comment is split across several, each stamped `<!-- CLAUDE_REVIEW k/N -->`; `sentinel.legacy_pages` collects every page and `_find_legacy_comment` returns them joined in page order (via `review-worklist.join_pages`), so `review.pages` / `review.pages_missing` say how many there were and which GitHub did not return. Reading page 1 alone hid every finding on a split review, because the findings sections are the tail of the document. Cache under `/.pr-review-cache/<pr>/` per (head SHA, updated_at). |
| `analyze.py` | One verdict per PR (`stamp` / `judge` / `route` / `blocked`), reason codes (`REASON_CODES`), row actions — every verdict carries one; cross-PR collision clusters (overlap vs same-file), directional link conflicts against the Hugo `aliases:` map (`frontmatter-validate.build_global_maps`), duplicates, stale blog dates, self-accepted findings, stale brief summaries. A PR whose requested reviewers are humans other than the approver (`GET /user`, or `--approver`) is `handed_off`: it keeps its verdict but the renderer folds it into a "Waiting on others" list, and collisions against it are advisory (`:theirs`). A PR the approver already sent back with nothing pushed since is `waiting_on_author` (`sent-back:<date>`) and folds into "Waiting on the author"; the approver's own PR is `author:self` (route only). `--judgments FILE` merges the model's judge output without lowering a verdict, except that judging every open 🚨 with a resolvable disposition and a note lifts a `blocked` row. A review that did not arrive whole — a missing page, or a card whose tally declares more findings than its sections parsed into (`counts_shortfall`) — is `blocked` with `review:unreadable:<why>` and a `--rerun` unblock, never `judge`, where `--force` would merge over findings nobody saw; a review that merely parsed into nothing with nothing to corroborate it gets the weaker `review:parse-confidence:low` stamp gate. Each cluster carries a recommendation (consolidate / chain / ignore / theirs) and `do_next` lists the board's opening moves, including a batch card per mechanical unblock (`unblock` / `refresh` / `rerun` / `rerun-checks`). Two invariants hold over `do_next`: no card names a row the board does not render (cards are built from the same set `render_board` groups, so a card's row button always exists to be pressed), and no card offers an approval that needed a judgment call — `gate_fails` records every stamp gate a row missed, and the chain card offers `--chain` only where `only_collisions_hold()` (nothing but the cross-PR gates). A row a workflow opened (`author:generated`) that still carries open findings and whose branch `act.push_allowed` permits also gets a `handoffs` entry: `/address-review N`, an interactive run rather than an `act.py` fragment. |
| `render.py` | Board HTML (published as an Artifact), one PR's detail page, or `--terminal`. Server-side rendered, one `esc()`, queue inlined as JSON, no network. Rows are grouped owner → domain and ordered by PR number inside a group. The board's buttons compose one `--act` command (approve buttons fold into a single `--stamp` list, reasons are scoped as `--reason "N=…"`, no fragment repeats); a `handoffs` button composes on a second line of its own (`/address-review N`) and never joins `--act`. A Do-next card carries a live `on/total` tally of the rows still holding its decision and paints a third, partial state between lit and out. A blocked row with no unblock says "no action available" and is tallied. `--terminal` carries the same facts — wrapped reasons, blockers, open findings, judgments, every action's fragment, the Do-next commands, cluster members, both waiting lists. Fenced code blocks in a finding render as `<pre>`. |
| `act.py` | Plan → preview → execute (plan schema 2: every comment, review body, `/resolve` line and suggestion is rendered into the step at plan time, and execute sends exactly that; identical fragments dedupe, two decisions on one PR are refused). Every write is preceded by a preflight that re-reads the PR (open, head unchanged); a failed one skips that step and the batch continues; `--dry-run` runs the preflights and lists the writes, sending none and never running git. `--stamp` (repeatable, `N:merge` / `N:no-merge` per PR; per-PR preflight immediately before each squash-merge — mergeable, checks green with the Sentinel polled separately after the approval, no changes-requested by anyone else, no unanswered 🚨 on a live re-read of the cards; humans approve-only without `--merge-humans`; `--approve-note` appends a sentence), `--request-changes` (a changes-requested review from the row's judgments), `--chain C1` (the first link through `--stamp`'s own path, the next link's unblock `requires` that merge), `--route`, `--unblock` and `--fix` (a temporary detached worktree, `push HEAD:<branch>`, merge commits only, never the person's checkout; `--fix` re-reads the raw review comments, skips outdated suggestions, applies bottom-up), `--close` (repeatable; `--superseded-by M` or `N:M`), `--reason "N=text"`, `--refresh`, `--rerun`, `--rerun-checks`, `--render` (`screenshot.mjs`), `--deploy`. Attribution footer on every posted comment except the approval body. |
| `screenshot.mjs` | Playwright screenshot helper (`NODE_PATH=/opt/node22/lib/node_modules` on a web session). |

Tests: `test_gh_client.py`, `test_collect.py`, `test_analyze.py`,
`test_render.py`, `test_act.py` — pytest, and each script's `--self-test`
runs the matching file's `run_standalone()`. Fixtures come from
`.claude/commands/docs-review/scripts/testdata/` (the v3 author/brief pair,
the legacy monolith, the normalize-pr* triples) plus in-module PR specs
expanded into a snapshot directory by `test_collect.make_snapshot()`, so
every suite sees exactly the record `collect.py` writes.

The queue never runs a local review refresh: a stale v3 review is a blocked
row with a `--refresh` action (`@claude … #update-review`), and `pinned-
comment.sh upsert` is never called on a v3 PR.
