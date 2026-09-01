#!/usr/bin/env python3
"""Validate a pr-review evidence object against `evidence-schema.json`.

This is the deterministic gate between the composer's evidence object and
the S3 ledger: `record-evidence.py` runs in the credentialed job and refuses
to upload anything this rejects (see README.md "The evidence object"). A bad
object must never land — not a malformed shape, not an open enum value, not
a disposition asserted without the note the closed set requires.

Hand-rolled against the schema (stdlib only, no jsonschema dependency),
mirroring `scripts/blog-review/validate-findings.py`: closed sets as module
constants, one flat list of human-readable errors, `additionalProperties:
false` enforced by hand via an explicit key-set check at every object level
the schema declares one for.

Beyond structural shape, this enforces invariants the schema's JSON Schema
subset can't express on its own:

  * every finding id matches `^F[0-9]+$` and is unique within the object
  * `high_water` is at least the highest finding index ever assigned —
    the composer's next id (`F<high_water+1>`) must never collide
  * an `outstanding` or `author-answer` finding — the two buckets that
    block merge — carries non-empty `text` and `file` (the schema already
    requires these for every finding; this re-asserts it specifically for
    the buckets a reviewer can least afford to see empty)
  * a disposition note is REQUIRED when the disposition is
    `deferred` / `accepted` / `not-applicable` — the same closed set and
    same rule as `review-worklist.py`'s `NOTE_REQUIRED`, so "accepted"
    can never become an unaudited way to close a finding
  * `trail` verdicts are drawn from the closed verification vocabulary
  * `history` is non-empty and every entry is sha-stamped

Importable (`validate_evidence`) and runnable:

    validate-evidence.py FILE

Exit 0 when valid; exit 1 with one problem per line on stderr otherwise.
Run the built-in smoke checks with `validate-evidence.py --self-test`.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCHEMA_VERSION = 1

# ---- closed sets (must stay in sync with evidence-schema.json) -------------

BUCKETS = {"outstanding", "author-answer", "reviewer-check", "preexisting"}
STATUSES = {"open", "resolved", "conceded", "disputed-held", "accepted-as-is"}
DISPOSITIONS = {"fixed", "refuted", "deferred", "accepted", "not-applicable"}
# Same rule, same set, as review-worklist.py's NOTE_REQUIRED: these three
# dispositions record a judgment call, not a fact the diff or a dispute
# comment already proves — the note is the audit trail for that call.
NOTE_REQUIRED_DISPOSITIONS = {"deferred", "accepted", "not-applicable"}
BLOCKING_BUCKETS = {"outstanding", "author-answer"}
VERDICTS = {
    "verified", "matches", "not-a-claim", "unverifiable",
    "contradicted", "mismatch", "framing-drift", "flagged",
}
ROUTES = {"pass0", "pass1", "pass2", "pass3", "preflight"}

# ---- key sets, one per object shape the schema pins additionalProperties:false ----

TOP_REQUIRED = {
    "schema_version", "repo", "pr", "head_sha", "run_id", "generated_at",
    "findings", "trail", "investigation_log", "history", "high_water",
}
TOP_OPTIONAL = {
    "editorial_balance", "triaged", "style_suggestions_count", "confidence", "summary",
    # Present when the object was assembled without its full inputs (e.g.
    # "prior-evidence-unavailable" on an update-lane run that couldn't fetch
    # the prior object, so trail/investigation_log are empty, not carried).
    "degraded",
}

FINDING_REQUIRED = {"id", "bucket", "file", "text", "origin", "status"}
# `detail` is the author card's `#### F<n> · Do this` block body, mirrored
# verbatim for the evidence page (persona-pass round, 2026-09-01).
FINDING_OPTIONAL = {"lines", "disposition", "detail"}

DISPOSITION_REQUIRED = {"disposition", "actor", "updated_at"}
DISPOSITION_OPTIONAL = {"note", "sha", "bulk"}

TRAIL_REQUIRED = {"file", "claim", "verdict"}
TRAIL_OPTIONAL = {"line", "evidence", "source", "route"}

HISTORY_REQUIRED = {"ts", "summary", "sha"}

FINDING_ID_RE = re.compile(r"^F[0-9]+$")
SHA_RE = re.compile(r"^[0-9a-f]{7,40}$")
HEAD_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
REPO_RE = re.compile(r"^[^/]+/[^/]+$")
# Lenient RFC3339-ish check — the schema says "format": "date-time" but we
# don't pull in a jsonschema/date library for one field shape; this catches
# the actual failure mode (a model emitting a bare date or a human string).
DATETIME_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")


def _nonempty_str(v) -> bool:
    return isinstance(v, str) and bool(v.strip())


def _check_keys(obj: dict, required: set, optional: set, where: str) -> list[str]:
    """additionalProperties:false, hand-rolled: missing required + unknown keys."""
    errors = []
    missing = required - obj.keys()
    for k in sorted(missing):
        errors.append(f"{where}.{k} is required")
    unknown = obj.keys() - required - optional
    for k in sorted(unknown):
        errors.append(f"{where} has unexpected property {k!r}")
    return errors


def _finding_index(fid: str) -> int | None:
    m = FINDING_ID_RE.match(fid or "")
    return int(fid[1:]) if m else None


def _validate_disposition(disp, where: str) -> list[str]:
    if disp is None:
        return []
    if not isinstance(disp, dict):
        return [f"{where} must be an object or null"]
    errors = _check_keys(disp, DISPOSITION_REQUIRED, DISPOSITION_OPTIONAL, where)
    d = disp.get("disposition")
    if "disposition" in disp and d not in DISPOSITIONS:
        errors.append(
            f"{where}.disposition {d!r} must be one of {', '.join(sorted(DISPOSITIONS))}"
        )
    if not _nonempty_str(disp.get("actor")):
        errors.append(f"{where}.actor must be a non-empty string")
    updated_at = disp.get("updated_at")
    if not _nonempty_str(updated_at) or not DATETIME_RE.match(updated_at):
        errors.append(f"{where}.updated_at must be a date-time string")
    sha = disp.get("sha")
    if sha is not None and not (isinstance(sha, str) and SHA_RE.match(sha)):
        errors.append(f"{where}.sha must be 7-40 lowercase hex characters")
    bulk = disp.get("bulk")
    if bulk is not None and not isinstance(bulk, bool):
        errors.append(f"{where}.bulk must be a boolean")
    # The load-bearing check: a disposition in the note-required set with no
    # note (or a blank one) is an unaudited close.
    if d in NOTE_REQUIRED_DISPOSITIONS and not _nonempty_str(disp.get("note")):
        errors.append(
            f"{where}.note is required and non-empty when disposition is {d!r}"
        )
    return errors


def validate_evidence(obj) -> list[str]:
    """Return a list of validation errors (empty when `obj` is a valid evidence object)."""
    errors: list[str] = []
    if not isinstance(obj, dict):
        return ["evidence object must be a JSON object"]

    errors += _check_keys(obj, TOP_REQUIRED, TOP_OPTIONAL, "evidence")

    if obj.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            f"evidence.schema_version must be {SCHEMA_VERSION}, got {obj.get('schema_version')!r}"
        )

    repo = obj.get("repo")
    if not (_nonempty_str(repo) and REPO_RE.match(repo)):
        errors.append("evidence.repo must be an 'owner/name' string")

    pr = obj.get("pr")
    if not (isinstance(pr, int) and not isinstance(pr, bool) and pr >= 1):
        errors.append("evidence.pr must be an integer >= 1")

    head_sha = obj.get("head_sha")
    if not (isinstance(head_sha, str) and HEAD_SHA_RE.match(head_sha)):
        errors.append("evidence.head_sha must be a 40-character hex commit sha")

    if not _nonempty_str(obj.get("run_id")):
        errors.append("evidence.run_id must be a non-empty string")

    generated_at = obj.get("generated_at")
    if not (_nonempty_str(generated_at) and DATETIME_RE.match(generated_at)):
        errors.append("evidence.generated_at must be a date-time string")

    high_water = obj.get("high_water")
    if not (isinstance(high_water, int) and not isinstance(high_water, bool) and high_water >= 0):
        errors.append("evidence.high_water must be an integer >= 0")
        high_water = None

    # ---- findings ----
    findings = obj.get("findings")
    if not isinstance(findings, list):
        errors.append("evidence.findings must be a list")
        findings = []

    seen_ids: set[str] = set()
    max_index = 0
    for i, f in enumerate(findings):
        where = f"evidence.findings[{i}]"
        if not isinstance(f, dict):
            errors.append(f"{where} must be an object")
            continue
        errors += _check_keys(f, FINDING_REQUIRED, FINDING_OPTIONAL, where)

        fid = f.get("id")
        if not (_nonempty_str(fid) and FINDING_ID_RE.match(fid)):
            errors.append(f"{where}.id must match ^F[0-9]+$")
        elif fid in seen_ids:
            errors.append(f"{where}.id {fid!r} is duplicated")
        else:
            seen_ids.add(fid)
            idx = _finding_index(fid)
            if idx is not None:
                max_index = max(max_index, idx)

        bucket = f.get("bucket")
        if bucket not in BUCKETS:
            errors.append(
                f"{where}.bucket {bucket!r} must be one of {', '.join(sorted(BUCKETS))}"
            )

        # Required for every finding by schema; re-asserted here specifically
        # for the two blocking buckets, since those are the ones a reviewer
        # cannot afford to see rendered empty.
        text_ok = _nonempty_str(f.get("text"))
        file_ok = _nonempty_str(f.get("file"))
        if not text_ok:
            errors.append(f"{where}.text must be a non-empty string")
        if not file_ok:
            errors.append(f"{where}.file must be a non-empty string")
        if bucket in BLOCKING_BUCKETS:
            if not text_ok:
                errors.append(f"{where}.text is required (non-empty) for bucket {bucket!r}")
            if not file_ok:
                errors.append(f"{where}.file is required (non-empty) for bucket {bucket!r}")

        lines = f.get("lines")
        if lines is not None:
            if not (isinstance(lines, list) and 1 <= len(lines) <= 2
                    and all(isinstance(n, int) and not isinstance(n, bool) and n >= 1 for n in lines)):
                errors.append(f"{where}.lines must be [start] or [start, end], each >= 1")

        if not _nonempty_str(f.get("origin")):
            errors.append(f"{where}.origin must be a non-empty string")

        if f.get("status") not in STATUSES:
            errors.append(
                f"{where}.status {f.get('status')!r} must be one of {', '.join(sorted(STATUSES))}"
            )

        errors += _validate_disposition(f.get("disposition"), f"{where}.disposition")

    if high_water is not None and high_water < max_index:
        errors.append(
            f"evidence.high_water ({high_water}) must be >= the highest finding "
            f"index in use (F{max_index})"
        )

    # ---- trail ----
    trail = obj.get("trail")
    if not isinstance(trail, list):
        errors.append("evidence.trail must be a list")
        trail = []
    for i, t in enumerate(trail):
        where = f"evidence.trail[{i}]"
        if not isinstance(t, dict):
            errors.append(f"{where} must be an object")
            continue
        errors += _check_keys(t, TRAIL_REQUIRED, TRAIL_OPTIONAL, where)
        if not _nonempty_str(t.get("file")):
            errors.append(f"{where}.file must be a non-empty string")
        if not _nonempty_str(t.get("claim")):
            errors.append(f"{where}.claim must be a non-empty string")
        if t.get("verdict") not in VERDICTS:
            errors.append(
                f"{where}.verdict {t.get('verdict')!r} must be one of {', '.join(sorted(VERDICTS))}"
            )
        line = t.get("line")
        if line is not None and not (isinstance(line, int) and not isinstance(line, bool) and line >= 1):
            errors.append(f"{where}.line must be an integer >= 1")
        route = t.get("route")
        if route is not None and route not in ROUTES:
            errors.append(f"{where}.route {route!r} must be one of {', '.join(sorted(ROUTES))}")

    # ---- investigation_log ----
    ilog = obj.get("investigation_log")
    if not isinstance(ilog, dict):
        errors.append("evidence.investigation_log must be an object")
    else:
        for k, v in ilog.items():
            if not isinstance(v, str):
                errors.append(f"evidence.investigation_log[{k!r}] must be a string")

    # ---- history ----
    history = obj.get("history")
    if not isinstance(history, list):
        errors.append("evidence.history must be a list")
        history = []
    if not history:
        errors.append("evidence.history must be non-empty (at least the composing run)")
    for i, h in enumerate(history):
        where = f"evidence.history[{i}]"
        if not isinstance(h, dict):
            errors.append(f"{where} must be an object")
            continue
        errors += _check_keys(h, HISTORY_REQUIRED, set(), where)
        if not (_nonempty_str(h.get("ts")) and DATETIME_RE.match(h.get("ts"))):
            errors.append(f"{where}.ts must be a date-time string")
        if not _nonempty_str(h.get("summary")):
            errors.append(f"{where}.summary must be a non-empty string")
        sha = h.get("sha")
        if not (isinstance(sha, str) and SHA_RE.match(sha)):
            errors.append(f"{where}.sha must be 7-40 lowercase hex characters (every entry is sha-stamped)")

    # ---- optional top-level fields ----
    if "editorial_balance" in obj and obj["editorial_balance"] is not None \
            and not isinstance(obj["editorial_balance"], dict):
        errors.append("evidence.editorial_balance must be an object or null")

    if "triaged" in obj:
        triaged = obj["triaged"]
        if not isinstance(triaged, list) or not all(isinstance(t, dict) for t in triaged):
            errors.append("evidence.triaged must be a list of objects")

    if "style_suggestions_count" in obj:
        c = obj["style_suggestions_count"]
        if not (isinstance(c, int) and not isinstance(c, bool) and c >= 0):
            errors.append("evidence.style_suggestions_count must be an integer >= 0")

    if "confidence" in obj and obj["confidence"] is not None:
        conf = obj["confidence"]
        if not isinstance(conf, dict) or not all(isinstance(v, str) for v in conf.values()):
            errors.append("evidence.confidence must be an object of strings, or null")

    if "summary" in obj and obj["summary"] is not None and not isinstance(obj["summary"], str):
        errors.append("evidence.summary must be a string or null")

    if "degraded" in obj and not _nonempty_str(obj["degraded"]):
        errors.append("evidence.degraded must be a non-empty string when present")

    return errors


# ---- fixtures / self-test ---------------------------------------------------


def _valid_fixture() -> dict:
    return {
        "schema_version": 1,
        "repo": "pulumi/docs",
        "pr": 21300,
        "head_sha": "a" * 40,
        "run_id": "run-1",
        "generated_at": "2026-08-31T17:00:00Z",
        "high_water": 3,
        "findings": [
            {
                "id": "F1",
                "bucket": "outstanding",
                "file": "content/docs/iac/get-started/aws.md",
                "lines": [12, 14],
                "text": "Broken link to the retired page",
                "origin": "verdict:contradicted",
                "status": "open",
            },
            {
                "id": "F2",
                "bucket": "reviewer-check",
                "file": "content/docs/iac/get-started/aws.md",
                "text": "Framing drift on the pricing claim",
                "origin": "verdict:framing-drift",
                "status": "resolved",
                "disposition": {
                    "disposition": "accepted",
                    "note": "acceptable simplification for a get-started page",
                    "actor": "cnunciato",
                    "sha": "abc1234",
                    "bulk": False,
                    "updated_at": "2026-08-31T17:05:00Z",
                },
            },
        ],
        "trail": [
            {"file": "content/docs/iac/get-started/aws.md", "line": 12,
             "claim": "The free tier includes 3 stacks", "verdict": "contradicted",
             "evidence": "pricing page shows unlimited stacks on Individual",
             "route": "pass1"},
        ],
        "investigation_log": {"changelog_scan": "checked releases/changelog for aws.md"},
        "editorial_balance": None,
        "triaged": [],
        "style_suggestions_count": 2,
        "confidence": {"overall": "high"},
        "summary": "One outstanding link break; one accepted framing note.",
        "history": [
            {"ts": "2026-08-31T17:00:00Z", "summary": "initial composition", "sha": "a" * 7},
        ],
    }


def self_test() -> int:
    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    good = _valid_fixture()
    check("valid fixture passes", validate_evidence(good) == [])

    check("non-dict rejected", validate_evidence([]) != [])

    check("missing top-level key rejected",
          any("history is required" in e for e in
              validate_evidence({k: v for k, v in good.items() if k != "history"})))

    check("unexpected top-level key rejected",
          any("unexpected property" in e for e in validate_evidence({**good, "bogus": 1})))

    check("schema_version enforced",
          any("schema_version" in e for e in validate_evidence({**good, "schema_version": 2})))

    check("bad repo shape rejected",
          any("evidence.repo" in e for e in validate_evidence({**good, "repo": "no-slash"})))

    check("bad head_sha rejected",
          any("head_sha" in e for e in validate_evidence({**good, "head_sha": "short"})))

    dup = {**good, "findings": [good["findings"][0], {**good["findings"][0]}]}
    check("duplicate finding id rejected",
          any("is duplicated" in e for e in validate_evidence(dup)))

    bad_id = {**good, "findings": [{**good["findings"][0], "id": "42"}]}
    check("malformed finding id rejected",
          any("must match" in e for e in validate_evidence(bad_id)))

    low_hw = {**good, "high_water": 0}
    check("high_water below max finding index rejected",
          any("high_water" in e for e in validate_evidence(low_hw)))

    empty_text = {**good, "findings": [{**good["findings"][0], "text": "  "}]}
    check("empty text on outstanding finding rejected",
          any(".text" in e for e in validate_evidence(empty_text)))

    outstanding_empty_file = {**good, "findings": [{**good["findings"][0], "file": ""}]}
    check("empty file on outstanding finding rejected",
          any(".file" in e for e in validate_evidence(outstanding_empty_file)))

    for disp in ("deferred", "accepted", "not-applicable"):
        missing_note = {**good, "findings": [{
            **good["findings"][1],
            "disposition": {**good["findings"][1]["disposition"], "disposition": disp, "note": ""},
        }]}
        check(f"disposition {disp!r} requires a note",
              any(".note is required" in e for e in validate_evidence(missing_note)))

    for disp in ("fixed", "refuted"):
        no_note_ok = {**good, "findings": [{
            **good["findings"][1],
            "disposition": {**good["findings"][1]["disposition"], "disposition": disp, "note": ""},
        }]}
        check(f"disposition {disp!r} does not require a note",
              not any(".note is required" in e for e in validate_evidence(no_note_ok)))

    check("unknown disposition value rejected",
          any(".disposition" in e for e in validate_evidence({
              **good, "findings": [{**good["findings"][1], "disposition":
                  {**good["findings"][1]["disposition"], "disposition": "wontfix"}}]})))

    check("unknown bucket rejected",
          any(".bucket" in e for e in validate_evidence({
              **good, "findings": [{**good["findings"][0], "bucket": "vibes"}]})))

    check("unknown status rejected",
          any(".status" in e for e in validate_evidence({
              **good, "findings": [{**good["findings"][0], "status": "closed"}]})))

    check("unknown trail verdict rejected",
          any(".verdict" in e for e in validate_evidence({
              **good, "trail": [{**good["trail"][0], "verdict": "definitely-true"}]})))

    check("empty history rejected",
          any("history must be non-empty" in e for e in validate_evidence({**good, "history": []})))

    check("history entry without sha rejected",
          any(".sha must be" in e for e in validate_evidence({
              **good, "history": [{"ts": good["history"][0]["ts"], "summary": "x", "sha": "zz"}]})))

    check("investigation_log with non-string value rejected",
          any("investigation_log" in e for e in validate_evidence({
              **good, "investigation_log": {"k": 5}})))

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall validate-evidence self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Validate a pr-review evidence object.")
    p.add_argument("file", nargs="?", help="evidence JSON file")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.file:
        p.error("FILE is required")

    try:
        obj = json.loads(Path(args.file).read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"validate-evidence: unreadable evidence file: {e}", file=sys.stderr)
        return 1

    errors = validate_evidence(obj)
    for e in errors:
        print(f"validate-evidence: {e}", file=sys.stderr)
    if errors:
        return 1
    print("validate-evidence: evidence object is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
