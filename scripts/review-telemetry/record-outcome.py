#!/usr/bin/env python3
"""Record what happened to a closed PR's review findings.

scrape-review-outcomes.py already derives each finding's terminal outcome
(fixed / conceded / ignored / unconfirmed-at-merge / abandoned, plus the
disputed flag) from the frozen pinned comments, but only the weekly digest
calls it, and only as an aggregate. This script runs it for one PR when that
PR closes and lands the record in the content-review ledger bucket, beside the
review's evidence objects, so the warehouse can join outcomes to verdicts and
cost on (pr, head_sha).

    record-outcome.py --pr N [--repo owner/repo]

Writes `.pr-review-outcomes/<pr>.json` always, and uploads it to
`$PR_REVIEW_OUTCOMES_URI/<pr>.json` (e.g. `s3://<ledger>/pr-review/outcomes`)
when that is set, via `aws s3 cp -` like record-evidence.py. A PR the pipeline
never reviewed (`no_review_data`, `pr_unavailable`) writes nothing: there is
no outcome to record. A reopened-and-closed PR overwrites its record; bucket
versioning keeps the earlier one.

Same degradation contract as the other record steps: URI unset ⇒ local file
plus `::warning::`; any failure ⇒ `::warning::` and exit 0. Telemetry never
fails the close.

Self-contained smoke checks: `record-outcome.py --self-test`.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
import traceback
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[1]
SCRAPER = REPO_ROOT / ".claude" / "commands" / "docs-review" / "scripts" / "scrape-review-outcomes.py"
SCHEMA_VERSION = 1
DEFAULT_OUT_DIR = ".pr-review-outcomes"
SKIP_STATUSES = ("no_review_data", "pr_unavailable")


def log(msg: str) -> None:
    print(f"record-outcome: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"::warning::record-outcome: {msg}")


def scrape(repo: str, pr: int) -> dict | None:
    """Run the scraper in its single-PR mode. It exits 1 on a decode failure
    but still prints the record, which is worth keeping: the status says the
    comment format moved."""
    proc = subprocess.run(
        [sys.executable, str(SCRAPER), "--pr", str(pr), "--repo", repo],
        capture_output=True, text=True,
    )
    if proc.stderr:
        sys.stderr.write(proc.stderr)
    try:
        record = json.loads(proc.stdout)
    except json.JSONDecodeError:
        warn(f"scraper printed no record for #{pr} (exit {proc.returncode})")
        return None
    return record if isinstance(record, dict) else None


def envelope(record: dict, repo: str, now: str | None = None) -> dict:
    return {
        "schema_version": SCHEMA_VERSION,
        "repo": repo,
        "recorded_at": now or datetime.now(timezone.utc).isoformat(timespec="seconds"),
        **record,
    }


def upload(record: dict, key: str) -> bool:
    try:
        subprocess.run(["aws", "s3", "cp", "-", key, "--content-type", "application/json"],
                       input=json.dumps(record, indent=2, ensure_ascii=False),
                       text=True, check=True, capture_output=True)
        return True
    except FileNotFoundError:
        warn("aws CLI not available; record not uploaded")
    except subprocess.CalledProcessError as e:
        warn(f"upload to {key} failed: {(e.stderr or '').strip()[:500]}")
    return False


def run(args, scrape_fn=scrape, upload_fn=upload) -> int:
    record = scrape_fn(args.repo, args.pr)
    if record is None:
        return 0
    status = record.get("status")
    if status in SKIP_STATUSES:
        log(f"#{args.pr}: {status}; nothing to record")
        return 0
    rec = envelope(record, args.repo)
    out = Path(args.out_dir) / f"{args.pr}.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    log(f"#{args.pr}: {status} → {out}")
    uri = (os.environ.get("PR_REVIEW_OUTCOMES_URI") or "").rstrip("/")
    if not uri:
        warn("PR_REVIEW_OUTCOMES_URI unset; outcome recorded locally only")
        return 0
    key = f"{uri}/{args.pr}.json"
    if upload_fn(rec, key):
        log(f"uploaded {key}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--pr", type=int)
    p.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY") or "pulumi/docs")
    p.add_argument("--out-dir", default=DEFAULT_OUT_DIR)
    p.add_argument("--self-test", action="store_true")
    return p


def main() -> int:
    p = build_parser()
    args = p.parse_args()
    if args.self_test:
        return self_test()
    if not args.pr:
        p.error("--pr is required")
    try:
        return run(args)
    except Exception:  # noqa: BLE001 — telemetry must never fail the close
        warn("unexpected error; outcome not recorded\n" + traceback.format_exc())
        return 0


def self_test() -> int:
    failures = 0

    def check(name: str, cond: bool) -> None:
        nonlocal failures
        print(f"  {'PASS' if cond else 'FAIL'}  {name}")
        if not cond:
            failures += 1

    check("scraper path resolves", SCRAPER.is_file())

    scraped = {"pr": 9, "status": "scraped", "merged": True, "surface": "v3",
               "outcomes": {"fixed": 2, "ignored_outstanding": 1}}
    uploads: list[tuple[dict, str]] = []

    def fake_upload(rec, key):
        uploads.append((rec, key))
        return True

    with tempfile.TemporaryDirectory() as td:
        args = build_parser().parse_args(["--pr", "9", "--repo", "pulumi/docs", "--out-dir", td])
        old = os.environ.pop("PR_REVIEW_OUTCOMES_URI", None)
        try:
            os.environ["PR_REVIEW_OUTCOMES_URI"] = "s3://ledger/pr-review/outcomes/"
            rc = run(args, scrape_fn=lambda r, n: dict(scraped), upload_fn=fake_upload)
            written = json.loads((Path(td) / "9.json").read_text())
            check("scraped: exit 0", rc == 0)
            check("scraped: envelope + record", written["schema_version"] == 1 and written["repo"] == "pulumi/docs"
                  and written["outcomes"]["fixed"] == 2 and "recorded_at" in written)
            check("scraped: uploaded to <uri>/<pr>.json", uploads and uploads[0][1] == "s3://ledger/pr-review/outcomes/9.json")

            uploads.clear()
            (Path(td) / "9.json").unlink()
            run(args, scrape_fn=lambda r, n: {"pr": 9, "status": "no_review_data"}, upload_fn=fake_upload)
            check("unreviewed PR: nothing written or uploaded", not uploads and not (Path(td) / "9.json").exists())

            run(args, scrape_fn=lambda r, n: None, upload_fn=fake_upload)
            check("scraper gave nothing: no upload", not uploads)

            run(args, scrape_fn=lambda r, n: {"pr": 9, "status": "decode_failed", "detail": "x"}, upload_fn=fake_upload)
            check("decode_failed is still recorded", len(uploads) == 1 and uploads[0][0]["status"] == "decode_failed")

            uploads.clear()
            del os.environ["PR_REVIEW_OUTCOMES_URI"]
            rc = run(args, scrape_fn=lambda r, n: dict(scraped), upload_fn=fake_upload)
            check("URI unset: local only, exit 0", rc == 0 and not uploads and (Path(td) / "9.json").exists())
        finally:
            os.environ.pop("PR_REVIEW_OUTCOMES_URI", None)
            if old is not None:
                os.environ["PR_REVIEW_OUTCOMES_URI"] = old

    print(f"record-outcome self-test: {'FAILED' if failures else 'passed'} ({failures} failure(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
