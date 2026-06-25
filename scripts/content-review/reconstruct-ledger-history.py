#!/usr/bin/env python3
"""Reconstruct the full history of content-review actions from the S3 ledger.

`record-review.py` writes one object per page slug and overwrites it each review,
but the ledger bucket has versioning enabled (infrastructure/index.ts), so every
overwrite is preserved as an immutable S3 object version. This walks those
versions and assembles a single chronological timeline of every review the
pipeline ever did — outcome AND selection signal (tier / score / monthly_visits)
— so metrics are reconstructable from day one without depending on the ~90-day
GitHub run logs.

Resolve the bucket from the stack output (never hardcode it):

    BUCKET=$(pulumi -C infrastructure stack output contentReviewLedgerBucketName --stack <stack>)
    reconstruct-ledger-history.py --bucket "$BUCKET" --format csv --out history.csv

Or point it at the same URI the workflow uses:

    reconstruct-ledger-history.py --uri "s3://$BUCKET/ledger/" --format jsonl

Needs the AWS CLI and read access to the bucket (the ContinuousDelivery role, or
your own creds). Run `--self-test` to exercise the timeline assembly offline.
"""

from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
import tempfile
from pathlib import Path

# Flat columns for --format csv (the high-signal subset; --format jsonl keeps
# every field plus the _version_* metadata).
CSV_COLUMNS = [
    "last_modified", "reviewed_at", "slug", "status", "tier", "score",
    "monthly_visits", "traffic_available", "fixes", "skipped_findings",
    "attempts", "clarity_flag", "retirement", "pr_number", "_version_id",
]


# ---- S3 access (thin wrappers; the testable core is build_timeline/emit) -----


def parse_uri(uri: str) -> tuple[str, str]:
    """s3://bucket/prefix/ -> (bucket, prefix)."""
    rest = uri[len("s3://"):] if uri.startswith("s3://") else uri
    bucket, _, prefix = rest.partition("/")
    return bucket, prefix


def list_versions(bucket: str, prefix: str) -> list[dict]:
    """Every object version under the prefix (the AWS CLI auto-paginates)."""
    out = subprocess.run(
        ["aws", "s3api", "list-object-versions",
         "--bucket", bucket, "--prefix", prefix, "--output", "json"],
        capture_output=True, text=True, check=True,
    )
    data = json.loads(out.stdout or "{}")
    return data.get("Versions", []) or []


def fetch_body(bucket: str, key: str, version_id: str) -> dict | None:
    """Fetch one object version's JSON body."""
    with tempfile.NamedTemporaryFile(suffix=".json") as tmp:
        r = subprocess.run(
            ["aws", "s3api", "get-object", "--bucket", bucket, "--key", key,
             "--version-id", version_id, tmp.name],
            capture_output=True, text=True, check=False,
        )
        if r.returncode != 0:
            print(f"reconstruct: get-object failed for {key}@{version_id}: {r.stderr.strip()}",
                  file=sys.stderr)
            return None
        try:
            return json.loads(Path(tmp.name).read_text())
        except (OSError, json.JSONDecodeError):
            return None


# ---- assembly (pure; unit-tested) -------------------------------------------


def build_timeline(versions: list[dict], bodies: dict[str, dict]) -> list[dict]:
    """Merge version metadata with each fetched record, sorted oldest-first.

    `versions` is the list-object-versions output (each: Key, VersionId,
    LastModified, IsLatest). `bodies` maps VersionId -> the parsed record JSON.
    Versions whose body is missing/unparseable are skipped. Ordering is by the
    S3 LastModified timestamp (precise even when several reviews share a
    reviewed_at date), with VersionId as a stable tiebreak.
    """
    rows: list[dict] = []
    for v in versions:
        body = bodies.get(v.get("VersionId"))
        if not isinstance(body, dict):
            continue
        rows.append({
            **body,
            "_version_id": v.get("VersionId"),
            "_last_modified": v.get("LastModified"),
            "_is_latest": bool(v.get("IsLatest")),
            "last_modified": v.get("LastModified"),
        })
    rows.sort(key=lambda r: (r.get("_last_modified") or "", r.get("_version_id") or ""))
    return rows


def to_jsonl(rows: list[dict]) -> str:
    return "".join(json.dumps(r, sort_keys=True) + "\n" for r in rows)


def to_csv(rows: list[dict]) -> str:
    import io
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=CSV_COLUMNS, extrasaction="ignore")
    w.writeheader()
    for r in rows:
        w.writerow({c: r.get(c) for c in CSV_COLUMNS})
    return buf.getvalue()


# ---- main -------------------------------------------------------------------


def gather(bucket: str, prefix: str) -> list[dict]:
    versions = list_versions(bucket, prefix)
    bodies = {
        v["VersionId"]: fetch_body(bucket, v["Key"], v["VersionId"])
        for v in versions if v.get("VersionId") and v.get("Key")
    }
    return build_timeline(versions, bodies)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--uri", help="s3://bucket/prefix/ (e.g. the workflow's CONTENT_REVIEW_LEDGER_URI)")
    ap.add_argument("--bucket", help="bucket name (resolve from the stack output, don't hardcode)")
    ap.add_argument("--prefix", default="ledger/", help="key prefix (default: ledger/)")
    ap.add_argument("--format", choices=["jsonl", "csv"], default="jsonl")
    ap.add_argument("--out", help="output path (default: stdout)")
    ap.add_argument("--self-test", action="store_true", help="run the offline assembly checks")
    args = ap.parse_args()

    if args.self_test:
        return self_test()

    if args.uri:
        bucket, prefix = parse_uri(args.uri)
    elif args.bucket:
        bucket, prefix = args.bucket, args.prefix
    else:
        ap.error("one of --uri or --bucket is required")

    rows = gather(bucket, prefix)
    body = to_csv(rows) if args.format == "csv" else to_jsonl(rows)
    if args.out:
        Path(args.out).write_text(body)
        print(f"reconstruct: {len(rows)} event(s) → {args.out}", file=sys.stderr)
    else:
        sys.stdout.write(body)
    print(f"reconstruct: {len(rows)} ledger event(s) across {len({r['slug'] for r in rows if r.get('slug')})} page(s)",
          file=sys.stderr)
    return 0


def self_test() -> int:
    failures = []

    def check(name, cond):
        print(("ok: " if cond else "FAIL: ") + name, file=sys.stderr if not cond else sys.stdout)
        if not cond:
            failures.append(name)

    # Two pages, one reviewed twice — versions arrive unordered.
    versions = [
        {"Key": "ledger/a.json", "VersionId": "v2", "LastModified": "2026-06-20T10:00:00Z", "IsLatest": True},
        {"Key": "ledger/a.json", "VersionId": "v1", "LastModified": "2026-06-18T10:00:00Z", "IsLatest": False},
        {"Key": "ledger/b.json", "VersionId": "v3", "LastModified": "2026-06-19T10:00:00Z", "IsLatest": True},
        {"Key": "ledger/c.json", "VersionId": "vX", "LastModified": "2026-06-21T10:00:00Z", "IsLatest": True},
    ]
    bodies = {
        "v1": {"slug": "a", "status": "incomplete", "tier": 1, "score": 200.0, "monthly_visits": 50, "attempts": 1, "reviewed_at": "2026-06-18"},
        "v2": {"slug": "a", "status": "reviewed", "tier": 1, "score": 210.0, "monthly_visits": 55, "fixes": 1, "pr_number": 19999, "reviewed_at": "2026-06-20"},
        "v3": {"slug": "b", "status": "clean", "tier": 2, "score": 80.0, "monthly_visits": 12, "reviewed_at": "2026-06-19"},
        "vX": None,  # unparseable body -> skipped
    }
    rows = build_timeline(versions, bodies)

    check("drops versions with no body", len(rows) == 3)
    check("sorted oldest-first by LastModified",
          [r["_version_id"] for r in rows] == ["v1", "v3", "v2"])
    check("carries selection signal through", rows[2]["tier"] == 1 and rows[2]["score"] == 210.0)
    check("flags the current version", rows[2]["_is_latest"] is True and rows[0]["_is_latest"] is False)
    check("two pages' history reconstructed",
          {r["slug"] for r in rows} == {"a", "b"})
    check("page a shows the incomplete→reviewed progression",
          [r["status"] for r in rows if r["slug"] == "a"] == ["incomplete", "reviewed"])

    csv_out = to_csv(rows)
    check("csv has a header + one row per event", len(csv_out.strip().splitlines()) == 4)
    check("csv header is the flat column set", csv_out.splitlines()[0] == ",".join(CSV_COLUMNS))

    jsonl_out = to_jsonl(rows)
    check("jsonl has one line per event", len(jsonl_out.strip().splitlines()) == 3)
    check("uri parsing splits bucket/prefix", parse_uri("s3://my-bucket/ledger/") == ("my-bucket", "ledger/"))

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall reconstruct-ledger-history self-tests passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
