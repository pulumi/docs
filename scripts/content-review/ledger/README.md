# Content-review ledger

One JSON file per reviewed page, written by the automated existing-content
review (`.github/workflows/review-existing-content.yml` via the
`review-existing-content` skill). The filename is the page's slug
(`content/docs/iac/concepts/stacks/_index.md` → `docs-iac-concepts-stacks.json`).

```json
{
  "path": "content/docs/iac/concepts/stacks/_index.md",
  "reviewed_at": "2026-06-12",
  "pr": "https://github.com/pulumi/docs/pull/19999",
  "lane": "priority",
  "clean": false,
  "fixes": 4,
  "skipped_findings": 2
}
```

`scripts/content-review/select-articles.py` reads this directory for review
cooldowns and stale-lane ordering; PR outcomes (merged/closed) are derived
live from GitHub, not stored here. Useful commands:

- `select-articles.py --stats` — merged/closed/open outcomes across entries.
- `select-articles.py --prune` — GC entries whose pages no longer exist.

Per-page files are deliberate: same-day PRs each touch a distinct file, so
ledger merge conflicts can't happen. Don't consolidate this into one file.
