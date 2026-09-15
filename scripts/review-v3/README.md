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
| G1 review-ran | author card's `CLAUDE_REVIEW_HEAD` == head SHA; or mechanical (no review required); or a legacy v2 review current at head (grandfather note) | push / `@claude #update-review` / `#new-review` |
| G2 findings-answered | every 🚨/❓ row carrying a REVIEW_STATE disposition | the undecided ids + the `@claude … #update-review` phrasing (the `/resolve` lane stays as agent-facing plumbing, never user-facing copy) |
| G3 right-approver | an APPROVED latest review from a human, non-denylisted, active member of every matrix-required team | the team slug(s) needed |
| G4 infra-evidence | this exact head deployed to staging successfully at least once — either the `staging/pulumi-test-io` commit status is green, or a completed run of `testing-build-and-deploy.yml` at this head SHA succeeded | the deploy is dispatched automatically (`staging-deploy-auto.yml`); `/deploy-staging` retries — **not waivable** |
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
didn't opt in. External contributors (fork head repo — never the
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

`staging-deploy-pr.yml` makes G4's evidence: `/deploy-staging` (tools-team
members only, same-repo branches only) dispatches the existing testing
deploy at the PR head branch and records the outcome as the
`staging/pulumi-test-io` commit status at the deployed SHA. Deploys queue on
the shared staging stack; a superseded request gets a comment saying to
re-run.

## Lane routing

`.github/review-routing.yml` (repo root config, schema-versioned) maps
subject × change type → required approver team. Subjects come from
`classify_path()` (shared with triage) applied to **live file lists**, never
labels. `routing.py` fails closed on any config it cannot validate.

The same resolution has two consumers. The Sentinel resolves it itself from
live API state to decide what G3 requires. Triage resolves it through
`route-pr.py` and *requests* those teams as PR reviewers, once at open /
ready — never on synchronize, because assignments are sticky and a
re-request on every push is the notification noise v3 exists to remove.
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
and a staging run is required — `frontend` — the rendering layer (`layouts/`,
`theme/`, `assets/`, `static/`): reviewed under the infra criteria, approved
by marketing, never a staging run — and `other`, the classifier's fallback
(repo plumbing such as `.claude/`, `styles/`, generated `data/` files): tools
approves, so an infra PR that also touches plumbing dedupes to one team.
Content-serving `data/` files (docs nav, blog taxonomies, author bios, the
pricing matrix) classify with the content they serve; the map is
`CONTENT_DATA_EXACT` in `triage-classify.py`.

Two optional config blocks shape what the Sentinel governs:

- `not_governed:` — automation lanes the Sentinel does not gate (`authors:`
  matches the PR author alone, e.g. Dependabot; `author_label_pairs:` needs
  both, e.g. pulumi-bot + `automation/merge` for the generated-docs regens).
  The check concludes `success` titled "Not governed" with no gates evaluated
  and `governed: false` in the verdict JSON. pulumi-bot's content-review and
  glow-up PRs carry no such label and are governed like everyone else's.
- `auto_approve:` — the clean-brief rule. For a listed bot author, G3 is
  satisfied without a human when the author card's header says nothing
  blocks merge AND the brief's `### ⚠️ Check these before approving` table
  has no finding rows (either empty-table sentinel counts; the verdict-free
  editorial-stances H4 is outside the rule) AND the PR is not
  `review:prose-flagged`. Any ⚠️ row sends the PR to the matrix team. The
  verdict JSON carries `auto_approved: true` for the auto-merge job.

`review:prose-flagged` (triage's Haiku + Vale pass on a short-circuited PR)
demotes a mechanical PR to substantive inside the Sentinel — the bar is pure
diff shape and cannot see labels — and disqualifies the clean-brief rule.
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
| `pr_review_config.py` | `~/.pr-review.yml` (`me:` lanes, `stamp_max_lines`, `stale_date_days`); routing itself stays in `.github/review-routing.yml`. |
| `collect.py` | Facts → `.pr-review-queue.json`: PR metadata, files + patches, `mergeable_state` (re-asked while `unknown`), check rollup, reviews, the parsed pinned review (`review-worklist.py`, both surfaces), `REVIEW_STATE`, triage prose, reviewed-head SHA, preview URL + per-page links, trust axes / risk tier / AI-suspect (ported from the retired pr-review shell scripts). Cache under `/.pr-review-cache/<pr>/` per (head SHA, updated_at). |
| `analyze.py` | One verdict per PR (`stamp` / `judge` / `route` / `blocked`), reason codes (`REASON_CODES`), row actions; cross-PR collision clusters (overlap vs same-file), directional link conflicts against the Hugo `aliases:` map (`frontmatter-validate.build_global_maps`), duplicates, stale blog dates, self-accepted findings, stale brief summaries. A PR whose requested reviewers are humans other than the approver (`GET /user`, or `--approver`) is `handed_off`: it keeps its verdict but the renderer folds it into a "Waiting on others" list, and collisions against it are advisory (`:theirs`). `--judgments FILE` merges the model's judge output without lowering a verdict. |
| `render.py` | Board HTML (published as an Artifact), one PR's detail page, or `--terminal`. Server-side rendered, one `esc()`, queue inlined as JSON, no network. |
| `act.py` | Plan → preview → execute: `--stamp` (per-PR preflight immediately before each squash-merge; humans approve-only without `--merge-humans`), `--route`, `--unblock` (merge commit, never rebase), `--fix`, `--close --superseded-by`, `--refresh`, `--render` (`screenshot.mjs`), `--deploy`. Attribution footer on every posted comment except the approval body. |
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
