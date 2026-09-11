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
| G4 infra-evidence | commit status `staging/pulumi-test-io` green at the current head | "a tools-team member comments `/deploy-staging`" — **not waivable** |
| G5 oversized-ack | `review:oversized` PRs: approval body contains `sentinel:oversized-ack` | explains the ack |

Conclusions are explicit about the fails-open trap: any gate ERROR (corrupt
REVIEW_STATE, a team-membership lookup failure) concludes `action_required`
— never `neutral`/`skipped`, which GitHub counts as passing for required
checks. `review:waived` ⇒ success with a banner naming the actor, except a
red G4, which stands. External contributors (no push permission) skip G1/G2
per config — the approving reviewer's review is the review. Rollout switch:
repo variable `REVIEW_V3_SENTINEL` is tri-state — unset = dark (no job, no
check-run, the review lanes skip their pokes; the state the file merges in),
`'report'` = report-only (conclusions `neutral` with "would be: …" in the
summary), `'1'` = enforcing. `/deploy-staging` follows the same switch. The
surface itself is `REVIEW_V3_COMMENTS` (repo default) or the `surface:v3`
label (one PR in or out, regardless of the variable). `REVIEW_V3_BOT_PRS`
= `'1'` makes the content-review and glow-up lanes open their bot PRs
already wearing the label — free v3 test traffic that no human author
sees, once the lane rewiring has merged (before that the label only reaches
the `/resolve` listener). Order of operations: run the `gh label create`
line for `surface:v3` first, then flip the variable — otherwise every bot
PR takes the unlabeled fallback with a `::warning::`. The
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

Subjects (closed set, all seven required in the matrix): `docs`, `blog`,
`website`, `programs` (docs-guild or marketing per the matrix), `infra` —
exactly the build and deploy pipeline (`infrastructure/`, `.github/workflows/`,
`scripts/`, Makefile, bundler config): tools approves and a staging run is
required — `frontend` — the rendering layer (`layouts/`, `theme/`, `assets/`,
`static/`): reviewed under the infra criteria, approved by marketing, never a
staging run — and `other`, the classifier's fallback (repo plumbing such as
`.claude/`, `styles/`, generated `data/` files): tools approves, so an infra PR
that also touches plumbing dedupes to one team. Content-serving `data/` files
(docs nav, blog taxonomies, author bios, the pricing matrix) classify with the
content they serve; the map is `CONTENT_DATA_EXACT` in `triage-classify.py`.

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
