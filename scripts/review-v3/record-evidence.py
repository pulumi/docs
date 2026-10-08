#!/usr/bin/env python3
"""Record one pr-review evidence object to the S3 evidence layer.

This is the credentialed record step: it runs in the deterministic job that
holds `PR_REVIEW_EVIDENCE_URI` (see README.md "The evidence object"), and it
is the only writer of the S3 objects the two pinned comments and the
rendered HTML page read back. The evidence object itself is composed
upstream (by the model, via the review pipeline) — this script never
invents content, only validates, merges, and ships it.

    record-evidence.py --evidence FILE --pr N --head-sha SHA

Steps, in order:

  1. Validate the evidence object with `validate_evidence` (imported from
     the sibling `validate-evidence.py` by file path, same technique
     `record-findings.py` uses for `validate-findings.py`). Invalid ⇒ print
     every problem and exit 1 — a bad object must never land anywhere,
     local or S3, so nothing is written on this path.
  2. Cross-check `--pr`/`--head-sha` against the object's own `pr`/
     `head_sha` fields — a record job invoked against the wrong evidence
     file is exactly the kind of silent mismatch this exists to catch, so
     it is folded into the same fatal path as an invalid object.
  3. Write two local files, ALWAYS, regardless of whether S3 is reachable:
     `.pr-review-evidence/<pr>-<sha>.json` (the immutable per-SHA record,
     written verbatim) and `.pr-review-evidence/<pr>-latest.json` (the
     current-disposition pointer — merged against the prior latest.json
     when one exists, see `merge_dispositions` below). These are the
     artifact the fork battery checks; the workflow uploads them as a
     workflow artifact regardless of the S3 outcome, so nothing here is
     allowed to skip writing them.
  4. When `PR_REVIEW_EVIDENCE_URI` is set, upload both files to
     `<uri>/<pr>/<sha>.json` and `<uri>/<pr>/latest.json` via `aws s3 cp -`
     from stdin, same technique as `record-findings.py`/`record-review.py`.
     Before overwriting `latest.json`, its current S3 content is read back
     (`load_prior`) and merged in: the PR's REVIEW_STATE block is the
     disposition source of truth, but a re-render composed from a stale
     REVIEW_STATE snapshot must never clobber a disposition mirrored by a
     later run. Upload failures are best-effort (warn, keep going) — the
     local copies double as the workflow artifact, so a lost S3 write is
     recoverable, unlike an invalid object landing.
  5. `PR_REVIEW_EVIDENCE_URI` unset ⇒ `::warning::` + local-only, exit 0.
     Same degradation contract, verbatim philosophy, as
     `scripts/content-review/record-review.py`.

Self-contained — run the smoke checks with `record-evidence.py --self-test`
(merge logic both directions, plus the degradation path, exercised with a
monkeypatched uploader — no real `aws` calls).
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent

# Reuse the validation gate from validate-evidence.py (single source of
# truth for the evidence contract). Hyphenated filename, so import by path;
# main() is guarded under __main__, so importing has no side effects.
_spec = importlib.util.spec_from_file_location(
    "validate_evidence_mod", HERE / "validate-evidence.py"
)
_validate = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_validate)
validate_evidence = _validate.validate_evidence

DEFAULT_OUT_DIR = ".pr-review-evidence"


def log(msg: str) -> None:
    print(f"record-evidence: {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    # `::warning::` surfaces in the GitHub Actions run summary.
    print(f"::warning::record-evidence: {msg}", file=sys.stderr)


# ---- merge -------------------------------------------------------------


def _parse_ts(ts: str | None):
    if not ts:
        return None
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00"))
    except ValueError:
        return None


def _newer(a: str | None, b: str | None) -> bool:
    """True if timestamp `a` is strictly newer than `b`.

    Parsed comparison when possible, falling back to string comparison for
    same-format ISO8601 timestamps that fail to parse for some reason —
    never crashes on a malformed value, since a bad timestamp must not
    block the merge it's trying to adjudicate.
    """
    pa, pb = _parse_ts(a), _parse_ts(b)
    if pa is not None and pb is not None:
        return pa > pb
    return (a or "") > (b or "")


def merge_dispositions(new_findings: list[dict], prior_findings: list[dict]) -> list[dict]:
    """Merge disposition state from `prior_findings` into `new_findings`, by id.

    `new_findings` is authoritative for everything else — id, bucket, file,
    text, status all come from this run's composed evidence. Only the
    per-finding `disposition` is contested: the PR's REVIEW_STATE block is
    the disposition source of truth, so ordinarily the new object's
    disposition (mirrored from the current REVIEW_STATE at compose time)
    wins. But a re-render can be composed from a REVIEW_STATE snapshot that
    predates a disposition another run already mirrored into latest.json —
    in that case the OLDER new-side disposition must not clobber the NEWER
    prior-side one. So: for each finding id, keep whichever disposition has
    the later `updated_at` (missing entirely counts as older than any
    timestamped one).

    A finding present in `prior_findings` but absent from `new_findings` is
    dropped — the new object's finding list is authoritative for which
    findings exist at all; only the disposition survives across the merge.
    """
    prior_by_id = {f.get("id"): f for f in prior_findings if isinstance(f, dict)}
    merged = []
    for f in new_findings:
        fid = f.get("id")
        prior = prior_by_id.get(fid)
        new_disp = f.get("disposition")
        prior_disp = (prior or {}).get("disposition")
        if prior_disp and (not new_disp or _newer(prior_disp.get("updated_at"), new_disp.get("updated_at"))):
            merged.append({**f, "disposition": prior_disp})
        else:
            merged.append(f)
    return merged


def merge_latest(new_evidence: dict, prior: dict | None) -> dict:
    """Build the `latest.json` content: `new_evidence` with disposition state
    merged in from `prior` (the object currently at `<uri>/<pr>/latest.json`).

    `high_water` never decreases (same invariant as the composer's counter,
    see README.md "Finding IDs") — take the max of the two.
    """
    if not prior:
        return new_evidence
    merged_findings = merge_dispositions(
        new_evidence.get("findings") or [], prior.get("findings") or []
    )
    high_water = max(
        int(new_evidence.get("high_water") or 0),
        int(prior.get("high_water") or 0),
    )
    return {**new_evidence, "findings": merged_findings, "high_water": high_water}


# ---- S3 --------------------------------------------------------------------


def s3_key(uri: str, *parts: str) -> str:
    return "/".join([uri.rstrip("/"), *parts])


def load_prior(pr: int, uri: str) -> dict | None:
    """The current content of `<uri>/<pr>/latest.json`, read back before this
    run's write overwrites it. Returns None on any failure — no aws CLI, no
    object yet, unreadable JSON — mirroring
    `scripts/content-review/record-review.py`'s `load_prior`: a genuine 404
    is the normal first-record case and stays quiet; anything else (a broken
    credential, a permissions error) is loud, because that failure mode
    silently discards a real disposition mirror rather than finding none.
    """
    key = s3_key(uri, str(pr), "latest.json")
    try:
        out = subprocess.run(["aws", "s3", "cp", key, "-"],
                             capture_output=True, text=True, check=False)
    except OSError:
        log("aws CLI not available; no prior latest.json to merge against")
        return None
    if out.returncode != 0:
        err = (out.stderr or "").strip()
        if re.search(r"\b(404|Not Found|NoSuchKey)\b", err, re.I):
            log(f"no prior latest.json at {key} (first record for this PR)")
        else:
            warn(f"could not read prior latest.json at {key}; merging nothing forward, "
                 f"which may drop a mirrored disposition: {err[:200]}")
        return None
    try:
        rec = json.loads(out.stdout)
    except json.JSONDecodeError:
        warn(f"prior latest.json at {key} is unreadable; not merging it forward")
        return None
    return rec if isinstance(rec, dict) else None


def upload(record: dict, key: str) -> bool:
    """Upload `record` to the S3 `key` via the aws CLI (stdin). Returns True
    on success. Best-effort by design (see module docstring step 4) — the
    caller warns and continues on failure rather than failing the run.
    """
    try:
        subprocess.run(
            ["aws", "s3", "cp", "-", key],
            input=json.dumps(record, indent=2) + "\n",
            text=True, check=True,
        )
        log(f"uploaded {key}")
        return True
    except FileNotFoundError:
        warn("aws CLI not available; record not uploaded")
        return False
    except subprocess.CalledProcessError as e:
        warn(f"upload failed for {key} ({e})")
        return False


# ---- main -------------------------------------------------------------------


def run(args) -> int:
    try:
        evidence = json.loads(Path(args.evidence).read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"record-evidence: unreadable evidence file: {e}", file=sys.stderr)
        return 1

    errors = validate_evidence(evidence)
    if evidence.get("pr") != args.pr:
        errors.append(
            f"evidence.pr ({evidence.get('pr')!r}) does not match --pr ({args.pr!r})"
        )
    if evidence.get("head_sha") != args.head_sha:
        errors.append(
            f"evidence.head_sha ({evidence.get('head_sha')!r}) does not match "
            f"--head-sha ({args.head_sha!r})"
        )
    if errors:
        for e in errors:
            print(f"record-evidence: {e}", file=sys.stderr)
        print("record-evidence: refusing to record an invalid evidence object", file=sys.stderr)
        return 1

    pr = args.pr
    sha = args.head_sha
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    uri = os.environ.get("PR_REVIEW_EVIDENCE_URI", "").strip()
    prior = load_prior(pr, uri) if uri else None
    latest = merge_latest(evidence, prior)

    sha_path = out_dir / f"{pr}-{sha}.json"
    latest_path = out_dir / f"{pr}-latest.json"
    sha_path.write_text(json.dumps(evidence, indent=2) + "\n")
    latest_path.write_text(json.dumps(latest, indent=2) + "\n")
    log(f"wrote {sha_path} and {latest_path}")

    if not uri:
        warn("PR_REVIEW_EVIDENCE_URI unset; evidence recorded locally only")
        return 0

    upload(evidence, s3_key(uri, str(pr), f"{sha}.json"))
    upload(latest, s3_key(uri, str(pr), "latest.json"))
    return 0


# ---- self-test ---------------------------------------------------------


def _fixture_evidence(pr=21300, sha="a" * 40, high_water=2, findings=None) -> dict:
    return {
        "schema_version": 1,
        "repo": "pulumi/docs",
        "pr": pr,
        "head_sha": sha,
        "run_id": "run-1",
        "generated_at": "2026-08-31T17:00:00Z",
        "high_water": high_water,
        "findings": findings if findings is not None else [
            {
                "id": "F1", "bucket": "outstanding",
                "file": "content/docs/iac/get-started/aws.md",
                "text": "Broken link", "origin": "verdict:contradicted", "status": "open",
            },
        ],
        "trail": [],
        "investigation_log": {},
        "history": [{"ts": "2026-08-31T17:00:00Z", "summary": "compose", "sha": "a" * 7}],
    }


def self_test() -> int:
    import tempfile
    from types import SimpleNamespace

    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    # ---- merge_dispositions, both directions ----
    older = {"disposition": "accepted", "actor": "a", "note": "old note",
             "updated_at": "2026-08-31T10:00:00Z"}
    newer = {"disposition": "refuted", "actor": "b",
             "updated_at": "2026-08-31T12:00:00Z"}

    new_findings = [{"id": "F1", "bucket": "outstanding", "file": "x", "text": "t",
                     "origin": "o", "status": "open", "disposition": older}]
    prior_findings = [{"id": "F1", "bucket": "outstanding", "file": "x", "text": "t",
                       "origin": "o", "status": "open", "disposition": newer}]
    merged = merge_dispositions(new_findings, prior_findings)
    check("prior (newer) disposition survives over new (older) one",
          merged[0]["disposition"] == newer)

    new_findings2 = [{"id": "F1", "bucket": "outstanding", "file": "x", "text": "t",
                      "origin": "o", "status": "open", "disposition": newer}]
    prior_findings2 = [{"id": "F1", "bucket": "outstanding", "file": "x", "text": "t",
                        "origin": "o", "status": "open", "disposition": older}]
    merged2 = merge_dispositions(new_findings2, prior_findings2)
    check("new (newer) disposition wins over prior (older) one",
          merged2[0]["disposition"] == newer)

    new_no_disp = [{"id": "F1", "bucket": "outstanding", "file": "x", "text": "t",
                    "origin": "o", "status": "open"}]
    prior_with_disp = [{"id": "F1", "bucket": "outstanding", "file": "x", "text": "t",
                        "origin": "o", "status": "open", "disposition": older}]
    merged3 = merge_dispositions(new_no_disp, prior_with_disp)
    check("prior disposition survives when the new render carries none",
          merged3[0]["disposition"] == older)

    missing_from_new = merge_dispositions([], prior_with_disp)
    check("a finding absent from the new render is dropped, not resurrected",
          missing_from_new == [])

    check("high_water never decreases across a merge",
          merge_latest(_fixture_evidence(high_water=2),
                       {"findings": [], "high_water": 9})["high_water"] == 9)

    # ---- degradation path: no URI set, local-only write ----
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        evidence_path = d / "evidence.json"
        evidence = _fixture_evidence()
        evidence_path.write_text(json.dumps(evidence))
        out_dir = d / "out"

        env_backup = os.environ.pop("PR_REVIEW_EVIDENCE_URI", None)
        upload_calls = []
        orig_upload = globals()["upload"]

        def stub_upload_should_not_be_called(record, key):
            upload_calls.append(key)
            return True

        globals()["upload"] = stub_upload_should_not_be_called
        try:
            args = SimpleNamespace(evidence=str(evidence_path), pr=evidence["pr"],
                                    head_sha=evidence["head_sha"], out_dir=str(out_dir))
            rc = run(args)
        finally:
            globals()["upload"] = orig_upload
            if env_backup is not None:
                os.environ["PR_REVIEW_EVIDENCE_URI"] = env_backup

        check("degradation path exits 0", rc == 0)
        check("degradation path never calls upload", upload_calls == [])
        sha_file = out_dir / f"{evidence['pr']}-{evidence['head_sha']}.json"
        latest_file = out_dir / f"{evidence['pr']}-latest.json"
        check("local per-sha file written", sha_file.is_file())
        check("local latest file written", latest_file.is_file())
        check("local latest file matches the evidence (no prior to merge)",
              json.loads(latest_file.read_text()) == evidence)

    # ---- full merge path via run(), stubbed uploader + prior loader ----
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        new_ev = _fixture_evidence(high_water=1, findings=[
            {"id": "F1", "bucket": "outstanding", "file": "x", "text": "t",
             "origin": "o", "status": "open",
             "disposition": {"disposition": "accepted", "actor": "a", "note": "n",
                             "updated_at": "2026-08-31T10:00:00Z"}},
        ])
        prior_latest = {
            "findings": [
                {"id": "F1", "disposition": {"disposition": "refuted", "actor": "b",
                                             "updated_at": "2026-08-31T12:00:00Z"}},
            ],
            "high_water": 5,
        }
        evidence_path = d / "evidence.json"
        evidence_path.write_text(json.dumps(new_ev))
        out_dir = d / "out"

        os.environ["PR_REVIEW_EVIDENCE_URI"] = "s3://bucket/pr-review"
        uploaded = {}
        orig_upload = globals()["upload"]
        orig_load_prior = globals()["load_prior"]
        globals()["upload"] = lambda record, key: uploaded.__setitem__(key, record) or True
        globals()["load_prior"] = lambda pr, uri: prior_latest
        try:
            args = SimpleNamespace(evidence=str(evidence_path), pr=new_ev["pr"],
                                    head_sha=new_ev["head_sha"], out_dir=str(out_dir))
            rc = run(args)
        finally:
            globals()["upload"] = orig_upload
            globals()["load_prior"] = orig_load_prior
            del os.environ["PR_REVIEW_EVIDENCE_URI"]

        check("merge-path run exits 0", rc == 0)
        check("both keys uploaded", len(uploaded) == 2)
        sha_key = s3_key("s3://bucket/pr-review", str(new_ev["pr"]), f"{new_ev['head_sha']}.json")
        latest_key = s3_key("s3://bucket/pr-review", str(new_ev["pr"]), "latest.json")
        check("per-sha upload is the evidence verbatim, unmerged",
              uploaded.get(sha_key) == new_ev)
        check("latest upload carries the merged (newer prior) disposition",
              uploaded.get(latest_key, {}).get("findings", [{}])[0].get("disposition", {}).get("disposition")
              == "refuted")
        check("latest upload's high_water is the max of both",
              uploaded.get(latest_key, {}).get("high_water") == 5)

        latest_file = out_dir / f"{new_ev['pr']}-latest.json"
        check("local latest file mirrors the uploaded (merged) content",
              json.loads(latest_file.read_text()) == uploaded.get(latest_key))

    # ---- invalid evidence: nothing is written, exit 1 ----
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        bad_path = d / "bad.json"
        bad_path.write_text(json.dumps({"not": "an evidence object"}))
        out_dir = d / "out"
        args = SimpleNamespace(evidence=str(bad_path), pr=1, head_sha="a" * 40, out_dir=str(out_dir))
        env_backup = os.environ.pop("PR_REVIEW_EVIDENCE_URI", None)
        try:
            rc = run(args)
        finally:
            if env_backup is not None:
                os.environ["PR_REVIEW_EVIDENCE_URI"] = env_backup
        check("invalid evidence exits 1", rc == 1)
        check("invalid evidence writes nothing locally", not out_dir.exists())

    # ---- pr/head_sha mismatch is fatal, same as an invalid object ----
    with tempfile.TemporaryDirectory() as d:
        d = Path(d)
        evidence = _fixture_evidence()
        evidence_path = d / "evidence.json"
        evidence_path.write_text(json.dumps(evidence))
        out_dir = d / "out"
        args = SimpleNamespace(evidence=str(evidence_path), pr=999999,
                               head_sha=evidence["head_sha"], out_dir=str(out_dir))
        env_backup = os.environ.pop("PR_REVIEW_EVIDENCE_URI", None)
        try:
            rc = run(args)
        finally:
            if env_backup is not None:
                os.environ["PR_REVIEW_EVIDENCE_URI"] = env_backup
        check("pr mismatch exits 1", rc == 1)

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall record-evidence self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Record a pr-review evidence object to S3.")
    p.add_argument("--evidence", help="composed evidence JSON file")
    p.add_argument("--pr", type=int, help="PR number")
    p.add_argument("--head-sha", help="head commit sha the evidence was composed at")
    p.add_argument("--out-dir", default=DEFAULT_OUT_DIR, help="local record artifact directory")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.evidence or args.pr is None or not args.head_sha:
        p.error("--evidence, --pr, and --head-sha are required")
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
