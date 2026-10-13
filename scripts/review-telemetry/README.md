# Review telemetry

Durable cost and outcome records for the Claude review pipeline, so cost per
PR, per step and per claim (and what the findings were worth) can be read
from the warehouse instead of reconstructed from console CSVs and expiring
artifacts. Observation only: nothing here changes a model call, a prompt or a
review decision.

Both writers land in the content-review ledger bucket (the
`contentReviewLedgerBucketName` stack output), which the data team already
loads:

| Prefix | Writer | When | Shape |
|---|---|---|---|
| `usage/<YYYY-MM-DD>/<run_id>-<attempt>-<job>.ndjson` | `record-usage.py`, copied by `record-docs-agent-usage.yml` | end of every job that calls Claude, failed and cancelled runs included | NDJSON, one row per model call (`grain: step`) and per verified claim (`grain: claim`) |
| `pr-review/outcomes/<pr>.json` | `record-outcome.py`, from `pr-closed.yml` | a reviewed PR closes | one JSON record: `scrape-review-outcomes.py --pr` plus an envelope |

## Usage rows

`record-usage.py` reads what each step already writes (pre-step JSON `meta`
totals, `.verified-claims.json` `model_usage`, claude-code-action's execution
log) and never calls an API. Its docstring documents the sources; the row
fields are:

| Field | Grain | Notes |
|---|---|---|
| `schema_version` | both | `1` |
| `grain` | both | `step` or `claim` |
| `repo`, `workflow`, `job`, `step` | both | `step` is a slug: `extract-atomic`, `extract-holistic`, `readthrough`, `verify`, `compose`, `triage-prose`, `update-v2`, `update-v3` |
| `run_id`, `run_attempt` | both | join to the warehouse's workflow-run table |
| `pr`, `head_sha` | both | null when the job has no PR |
| `page_path` | both | content-review jobs; null on PR review |
| `model`, `effort` | both | `effort` as configured, null when unset |
| `input_tokens`, `output_tokens`, `cache_read_input_tokens`, `cache_creation_input_tokens` | both | raw counts |
| `turns` | both | where known |
| `reported_cost_usd` | step | claude-code-action's own `costUSD`, per model; null elsewhere |
| `started_at`, `duration_ms` | step | `started_at` falls back to the job start |
| `outcome` | step | `success`, `failed`, `timeout`, `cancelled`, `skipped`, `degraded` (ran, but the artifact recorded errors) |
| `claim_id`, `entity_key`, `claim_type`, `file`, `line_range`, `route`, `verdict`, `confidence`, `turn_cap_exhausted`, `source_discipline_gate` | claim | `claim_id` joins to the evidence `trail[]` for the same (`pr`, `head_sha`) |

Rules for consumers:

- **Spend is the sum of `step` rows.** `claim` rows split the `verify` step's
  tokens by claim, so adding both counts verify twice.
- **A claude-code-action step writes one row per model** in its `modelUsage`
  (the Opus step's subagents can run on another model), so a step can have
  several rows. `turns` and `duration_ms` sit on the configured model's row.
- **No prices are stored.** Price tokens at query time from an effective-dated
  price seed. `reported_cost_usd` is the action's own figure, useful as a
  cross-check.
- **Extraction cost is step-grain.** Allocating it across a file's claims is a
  dashboard calculation and should be labeled as allocated.
- A run killed before claude-code-action wrote its `result` event is summed
  from the streamed messages, which undercounts output tokens. Its `outcome`
  says so.

## How the pieces fit

1. Each Claude job checks out `scripts/review-telemetry/` from the default
   branch (never the PR head), runs `record-usage.py` with `if: always()`, and
   uploads `.docs-agent-usage/` as a `docs-agent-usage-<job>-attempt<n>`
   artifact.
2. A final `if: always()` job calls `record-docs-agent-usage.yml`, which
   collects those artifacts and copies them to `usage/` with the production
   role. The review's call also collects the triage run that triggered it, so
   the triage Haiku call needs no credentials of its own.
3. `pr-closed.yml`'s `record-review-outcome` job runs `record-outcome.py` when a
   same-repo PR closes.

Everything degrades the same way the evidence record does: no bucket ⇒ the
artifact is the record and a `::warning::` says so. Nothing here fails a run.

Instrumented today: `claude-code-review.yml`, `claude-update.yml` and
`claude-triage.yml`. Another workflow joins by adding the same three steps to
its Claude job and a `record-usage` job; `test_usage_wiring.py` pins the
contract for each instrumented workflow, so add the new one there too.

## Tests

`make test-review-pipeline` runs `record-usage.py --self-test`,
`record-outcome.py --self-test` and `test_usage_wiring.py`.
