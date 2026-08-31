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
- `reviewer-check` (👀 reviewer should look before approving — advisory)
- `preexisting` (💡 not this PR's fault — optional)

The ⚠️→❓/👀 split is verdict-driven in the composer: `unverifiable` →
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
- Readers: Sentinel gate 2 (uncredentialed, fork-safe), `review-worklist.py
  --state-from-body`, the record job's mirror into `latest.json`.
- Sentinel accepts the block only from the bot-authored comment.

## The Sentinel

`sentinel.py` + `.github/workflows/review-sentinel.yml` publish the one
blocking check-run ("Sentinel"). Deterministic, no model, no AWS, and —
because the workflow runs on `pull_request_target` — **never checks out or
executes PR code** (test-enforced). Gates, each red message naming its fix:

| Gate | Green when | Red says |
|---|---|---|
| G1 review-ran | author card's `CLAUDE_REVIEW_HEAD` == head SHA; or mechanical (no review required); or a legacy v2 review current at head (grandfather note) | push / `@claude #update-review` / `#new-review` |
| G2 findings-answered | every 🚨/❓ row checked or carrying a REVIEW_STATE disposition | the undecided ids + the `/resolve` and `#update-review` commands |
| G3 right-approver | an APPROVED latest review from a human, non-denylisted, active member of every matrix-required team | the team slug(s) needed |
| G4 infra-evidence | commit status `staging/pulumi-test-io` green at the current head | "a tools-team member comments `/deploy-staging`" — **not waivable** |
| G5 oversized-ack | `review:oversized` PRs: approval body contains `sentinel:oversized-ack` | explains the ack |

Conclusions are explicit about the fails-open trap: any gate ERROR (corrupt
REVIEW_STATE, a team-membership lookup failure) concludes `action_required`
— never `neutral`/`skipped`, which GitHub counts as passing for required
checks. `review:waived` ⇒ success with a banner naming the actor, except a
red G4, which stands. External contributors (no push permission) skip G1/G2
per config — the approving reviewer's review is the review. Report-only
rollout: until repo variable `REVIEW_V3_SENTINEL` is `'1'`, conclusions are
`neutral` with "would be: …" in the summary. The check summary embeds the
reviewer brief (merge-box delivery), and on red the sentinel PATCHes a ⛔
strip into the author card naming the exact commands.

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
