#!/usr/bin/env python3
"""Stamp the authoritative `make lint` result into a content-review PR body.

The composer (`compose-pr-body.py`) leaves a `<!-- LINT-RESULT -->` placeholder
in the PR body's Verification section. The worker's re-lint gate — which re-runs
`make lint` on the pushed branch and is the authority on lint status, not the
review model — calls this to replace that placeholder with the real outcome. So
"lint passed" in the body is never the model's self-report.

Idempotent: it only edits when the placeholder is still present, so a re-run
can't double-stamp or clobber a human's later edit.

Usage:
    stamp-lint-result.py --branch content-review/<slug> --result passed|failed --sha <short-sha>
"""

from __future__ import annotations

import argparse
import subprocess
import sys

PLACEHOLDER = "<!-- LINT-RESULT -->"


def _gh(args: list[str]) -> tuple[int, str]:
    try:
        p = subprocess.run(["gh", *args], capture_output=True, text=True, check=False)
    except FileNotFoundError:
        print("stamp-lint-result: gh not available", file=sys.stderr)
        return 1, ""
    if p.returncode != 0:
        print(f"stamp-lint-result: gh {' '.join(args[:3])}… failed: {p.stderr.strip()}", file=sys.stderr)
    return p.returncode, p.stdout


def marker(result: str, sha: str) -> str:
    if result == "passed":
        return f"✅ `make lint` re-verified by the workflow on `{sha}`"
    return (
        f"❌ `make lint` FAILED on `{sha}` — PR returned to draft; "
        "see the automated lint comment on this PR"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--branch", required=True)
    ap.add_argument("--result", required=True, choices=["passed", "failed"])
    ap.add_argument("--sha", default="")
    args = ap.parse_args()

    rc, body = _gh(["pr", "view", args.branch, "--json", "body", "--jq", ".body"])
    if rc != 0:
        return 0  # best-effort; the re-lint step already wraps this in || true
    if PLACEHOLDER not in body:
        print("stamp-lint-result: placeholder absent; nothing to stamp", file=sys.stderr)
        return 0

    updated = body.replace(PLACEHOLDER, marker(args.result, args.sha))
    # gh pr edit reads --body-file from a path or '-'; pass the new body on stdin.
    try:
        p = subprocess.run(
            ["gh", "pr", "edit", args.branch, "--body-file", "-"],
            input=updated, text=True, capture_output=True, check=False,
        )
    except FileNotFoundError:
        return 0
    if p.returncode != 0:
        print(f"stamp-lint-result: gh pr edit failed: {p.stderr.strip()}", file=sys.stderr)
        return 0
    print(f"stamp-lint-result: stamped lint={args.result} into {args.branch} body")
    return 0


if __name__ == "__main__":
    sys.exit(main())
