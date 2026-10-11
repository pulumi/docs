# review-admin

Browse and export the review/state data our automated processes keep in S3:

| Data | S3 location | Producer |
|------|-------------|----------|
| Docs review ledger | `content-review-ledger-*/ledger/` | review-existing-content workflow |
| Fact-check claims | `content-review-ledger-*/claims/` | content-review claim pipeline |
| Blog known-issues index | `content-review-ledger-*/blog-review/` | blog-review-index workflow |
| Signal health | `content-review-ledger-*/health/state.json` | signal-health check |
| Social post state | `social-post-state-*/posted*.json` | schedule-social workflow |

None of this is human-browsable in the S3 console (one small JSON object at a
time). This tool syncs everything into a local cache and then works offline.
It is **read-only** — it never writes to S3.

This is the interim browse/export layer until the DWH ingestion in pulumi/data
lands; the exports are already in the flat shape ingestion wants (and DuckDB
reads them directly, e.g. `duckdb -c "select * from 'claims.jsonl'"`).

## Prerequisites

- The AWS CLI with read access to the buckets (set `AWS_PROFILE` to a profile
  in the Pulumi AWS account; refresh your SSO session if sync fails).
- Only `sync` touches AWS; every other subcommand reads the local cache at
  `.review-admin-cache/` (gitignored; override with `--cache-dir` or
  `$REVIEW_ADMIN_CACHE`).

Bucket names are Pulumi auto-named and discovered by name prefix; set
`CONTENT_REVIEW_LEDGER_BUCKET` / `SOCIAL_STATE_BUCKET` to pin them explicitly.

## Usage

```bash
# Pull both buckets into the local cache (or: make review-admin-sync)
scripts/review-admin/review-admin.py sync

# Console overview of everything captured
scripts/review-admin/review-admin.py summary

# Filterable listings per domain (docs | claims | blog | social)
scripts/review-admin/review-admin.py list claims --verdict contradicted
scripts/review-admin/review-admin.py list docs --status reviewed --since 2026-07-01

# Full paper trail for one article/post across all domains
scripts/review-admin/review-admin.py show docs-iac-get-started-aws-configure

# DWH/DuckDB-ready flat exports (CSV + JSONL) into <cache>/exports/
scripts/review-admin/review-admin.py export

# Self-contained HTML dashboard (or: make review-admin-dashboard)
scripts/review-admin/review-admin.py html --open
```

## Testing

```bash
scripts/review-admin/review-admin.py --self-test
python3 -m pytest scripts/review-admin/test_review_admin.py
```

## Version history

The ledger buckets are versioned, and this tool intentionally shows current
state only. To reconstruct how records changed over time, use
`scripts/content-review/reconstruct-ledger-history.py`.
