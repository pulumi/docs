#!/usr/bin/env python3
"""Validate a blog-review findings sentinel against the index contract.

The review model's ONLY structured output is `.blog-review-findings.json`
(shape documented in `.claude/commands/blog-review-index/SKILL.md` and
`references/findings-schema.json`). This script is the deterministic gate
between that model-written file and the S3 index: schema shape, the CLOSED
issue taxonomy, evidence-required-per-issue, and agreement with the trusted
queue entry. Invalid findings never reach the index — record-findings.py
records the post `incomplete` instead (burning an attempt), so a model that
free-styles the schema is retried rather than trusted.

Importable (validate_findings) and runnable:

    validate-findings.py --findings .blog-review-findings.json \
        --queue .blog-review-queue.json

Exit 0 when valid; exit 1 with one error per line on stderr otherwise.
Run the built-in smoke checks with --self-test.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCHEMA_VERSION = 1

# The closed issue taxonomy. Definitions and the severity rubric live in
# `.claude/commands/blog-review-index/references/issue-taxonomy.md`; the two
# files must stay in sync — the reference documents what the model may emit,
# this set is what the gate accepts.
CATEGORIES = {
    "factual-rot",
    "dead-link",
    "broken-code",
    "deprecated-product",
    "seo-thin",
    "ai-positioning",
    "frontmatter",
    "rendering",
}

SEVERITIES = {"blocker", "major", "minor"}

# Advisory noindex assessments (see references/noindex-rubric.md). The model
# recommends; the future noindex process — with traffic thresholds a model
# can't see — decides.
ASSESSMENTS = {"keep", "candidate", "strong-candidate"}


def _nonempty_str(v) -> bool:
    return isinstance(v, str) and bool(v.strip())


def validate_findings(findings, queue_post: dict) -> list[str]:
    """Return a list of validation errors (empty when the findings are valid)."""
    errors: list[str] = []
    if not isinstance(findings, dict):
        return ["findings must be a JSON object"]

    if findings.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {SCHEMA_VERSION}, got {findings.get('schema_version')!r}"
        )

    # The path/slug must agree with the trusted queue entry — a findings file
    # about a different post than the one selected is a broken run.
    for key in ("path", "slug"):
        if findings.get(key) != queue_post.get(key):
            errors.append(
                f"{key} mismatch: findings say {findings.get(key)!r}, "
                f"queue says {queue_post.get(key)!r}"
            )

    issues = findings.get("issues")
    if not isinstance(issues, list):
        errors.append("issues must be a list")
        issues = []

    seen_ids: set[str] = set()
    for i, issue in enumerate(issues):
        where = f"issues[{i}]"
        if not isinstance(issue, dict):
            errors.append(f"{where} must be an object")
            continue
        iid = issue.get("id")
        if not _nonempty_str(iid):
            errors.append(f"{where}.id must be a non-empty string")
        elif iid in seen_ids:
            errors.append(f"{where}.id {iid!r} is duplicated")
        else:
            seen_ids.add(iid)
        if issue.get("category") not in CATEGORIES:
            errors.append(
                f"{where}.category {issue.get('category')!r} is not in the "
                f"closed taxonomy ({', '.join(sorted(CATEGORIES))})"
            )
        if issue.get("severity") not in SEVERITIES:
            errors.append(
                f"{where}.severity {issue.get('severity')!r} must be one of "
                f"{', '.join(sorted(SEVERITIES))}"
            )
        if not _nonempty_str(issue.get("summary")):
            errors.append(f"{where}.summary must be a non-empty string")
        # Evidence is REQUIRED: an issue the model can't evidence is an
        # opinion, and opinions don't get to drive noindex decisions.
        if not _nonempty_str(issue.get("evidence")):
            errors.append(f"{where}.evidence must be a non-empty string")
        if not _nonempty_str(issue.get("location")):
            errors.append(f"{where}.location must be a non-empty string")

    clean = findings.get("clean")
    if not isinstance(clean, bool):
        errors.append("clean must be a boolean")
    elif clean and issues:
        errors.append("clean is true but issues is non-empty")
    elif clean is False and not issues:
        errors.append("clean is false but issues is empty")

    signal = findings.get("noindex_signal")
    if not isinstance(signal, dict):
        errors.append("noindex_signal must be an object")
    else:
        if signal.get("assessment") not in ASSESSMENTS:
            errors.append(
                f"noindex_signal.assessment {signal.get('assessment')!r} must be "
                f"one of {', '.join(sorted(ASSESSMENTS))}"
            )
        if not _nonempty_str(signal.get("rationale")):
            errors.append("noindex_signal.rationale must be a non-empty string")
        # A keep-worthy post shouldn't need a stronger-than-keep assessment
        # with zero recorded issues: the assessment must be grounded in the
        # issue list, not free-floating vibes.
        if signal.get("assessment") == "strong-candidate" and not issues:
            errors.append("noindex_signal.assessment strong-candidate requires issues")

    return errors


def load_queue_post(queue_path: Path) -> dict:
    data = json.loads(queue_path.read_text())
    posts = data.get("posts") or []
    if not posts:
        raise SystemExit(f"validate-findings: no posts in {queue_path}")
    return posts[0]


def self_test() -> int:
    failures = []

    def check(name, cond):
        if not cond:
            failures.append(name)
            print(f"FAIL: {name}", file=sys.stderr)
        else:
            print(f"ok: {name}")

    post = {"path": "content/blog/p/index.md", "slug": "p"}
    good = {
        "schema_version": 1,
        "path": "content/blog/p/index.md",
        "slug": "p",
        "issues": [{
            "id": "dead-link-01", "category": "dead-link", "severity": "major",
            "summary": "Link to example.com/docs 404s",
            "evidence": "curl returns HTTP 404 as of the review run",
            "location": "## Getting started, line 42",
        }],
        "clean": False,
        "noindex_signal": {"assessment": "keep", "rationale": "content still current"},
    }
    check("valid findings pass", validate_findings(good, post) == [])

    clean = {**good, "issues": [], "clean": True}
    check("clean findings pass", validate_findings(clean, post) == [])

    check("non-dict rejected", validate_findings([], post) != [])
    check("schema_version enforced",
          any("schema_version" in e for e in validate_findings({**good, "schema_version": 2}, post)))
    check("path mismatch rejected",
          any("path mismatch" in e for e in validate_findings({**good, "path": "content/blog/x/index.md"}, post)))
    bad_cat = {**good, "issues": [{**good["issues"][0], "category": "vibes"}]}
    check("open taxonomy rejected",
          any("closed taxonomy" in e for e in validate_findings(bad_cat, post)))
    bad_sev = {**good, "issues": [{**good["issues"][0], "severity": "catastrophic"}]}
    check("unknown severity rejected",
          any("severity" in e for e in validate_findings(bad_sev, post)))
    no_evidence = {**good, "issues": [{**good["issues"][0], "evidence": "  "}]}
    check("evidence required",
          any("evidence" in e for e in validate_findings(no_evidence, post)))
    dup = {**good, "issues": [good["issues"][0], good["issues"][0]]}
    check("duplicate ids rejected",
          any("duplicated" in e for e in validate_findings(dup, post)))
    check("clean/issues consistency (clean+issues)",
          any("clean is true" in e for e in validate_findings({**good, "clean": True}, post)))
    check("clean/issues consistency (dirty+empty)",
          any("clean is false" in e for e in validate_findings({**good, "issues": [], "clean": False}, post)))
    check("noindex assessment enforced",
          any("assessment" in e for e in validate_findings(
              {**good, "noindex_signal": {"assessment": "nuke", "rationale": "r"}}, post)))
    check("strong-candidate requires issues",
          any("strong-candidate requires issues" in e for e in validate_findings(
              {**clean, "noindex_signal": {"assessment": "strong-candidate", "rationale": "r"}}, post)))

    if failures:
        print(f"\n{len(failures)} failure(s)", file=sys.stderr)
        return 1
    print("\nall validate-findings self-tests passed")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Validate a blog-review findings sentinel.")
    p.add_argument("--findings", help="model findings sentinel (.blog-review-findings.json)")
    p.add_argument("--queue", help="single-post queue JSON (.blog-review-queue.json)")
    p.add_argument("--self-test", action="store_true", help="run built-in smoke checks")
    args = p.parse_args()

    if args.self_test:
        return self_test()
    if not args.findings or not args.queue:
        p.error("--findings and --queue are required")

    try:
        findings = json.loads(Path(args.findings).read_text())
    except (OSError, json.JSONDecodeError) as e:
        print(f"validate-findings: unreadable findings file: {e}", file=sys.stderr)
        return 1
    errors = validate_findings(findings, load_queue_post(Path(args.queue)))
    for e in errors:
        print(f"validate-findings: {e}", file=sys.stderr)
    if errors:
        return 1
    print("validate-findings: findings are valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
