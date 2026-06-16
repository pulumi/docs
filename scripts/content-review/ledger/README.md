# Content-review ledger

One JSON object per reviewed page, recording when it was last reviewed, written
by the automated existing-content review (`.github/workflows/review-existing-content.yml`
and its per-article worker `content-review-article.yml`). The object key is the
page's slug (`content/docs/iac/concepts/stacks/_index.md` →
`docs-iac-concepts-stacks.json`).

```json
{
  "path": "content/docs/iac/concepts/stacks/_index.md",
  "slug": "docs-iac-concepts-stacks",
  "reviewed_at": "2026-06-12",
  "pr": "https://github.com/pulumi/docs/pull/19999",
  "lane": "priority",
  "clean": false,
  "fixes": 4,
  "skipped_findings": 2
}
```

## The ledger lives in S3, not in git

The ledger is **not committed to this repo** — it lives in a versioned, private
S3 bucket (`contentReviewLedgerBucketName`, defined in `infrastructure/index.ts`),
located by the `CONTENT_REVIEW_LEDGER_S3_URI` repo variable (e.g.
`s3://<bucket>/ledger/`). Keeping it out of git means the daily review never has
to open a metadata-only PR for anyone to approve: the dispatcher syncs the ledger
down before selecting, and each per-article worker writes its page's object back
up after reviewing (fix and clean articles alike). `reviewed_at` is stamped by
the workflow's ledger-write step, not the model.

This directory holds only this README. Workflows sync the S3 ledger into a local
cache (`.ledger-cache/`, git-ignored) and point the tooling below at it.

`scripts/content-review/select-articles.py` reads the ledger directory for review
cooldowns and stale-lane ordering; PR outcomes (merged/closed) are derived live
from GitHub, not stored here. Run the maintenance commands against the synced
cache:

- `aws s3 sync "$CONTENT_REVIEW_LEDGER_S3_URI" .ledger-cache/`
- `select-articles.py --ledger-dir .ledger-cache --stats` — merged/closed/open outcomes.
- `select-articles.py --ledger-dir .ledger-cache --prune` — list entries whose
  pages no longer exist (then delete those keys from S3).

Per-page objects are deliberate: same-day reviews each touch a distinct key, so
ledger writes can't collide. Don't consolidate this into one object.
