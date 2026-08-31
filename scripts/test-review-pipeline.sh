#!/usr/bin/env bash
# Run every test suite belonging to the review pipelines (pre-merge PR review,
# daily content review, blog known-issues index).
#
# These suites were all green but nothing ran them: `make test` covers only the
# example programs, and no workflow invoked pytest or a --self-test. Unrun
# tests rot — test_select_posts.py had been erroring under pytest collection
# and nobody saw it. This script is the single entry point;
# review-pipeline-tests.yml runs it on any PR that touches the pipeline.
#
# Three suite kinds, discovered rather than enumerated so a new script is
# covered the day it lands:
#   1. pytest over .claude/commands/docs-review/scripts/
#   2. standalone test_*.py harnesses (module-level check() style, not pytest)
#   3. every script exposing a --self-test flag
set -uo pipefail

cd "$(dirname "$0")/.."

OUT=$(mktemp -t review-pipeline-tests.XXXXXX)
trap 'rm -f "$OUT"' EXIT

FAILED=0
run() {
    local label="$1"; shift
    if "$@" >"$OUT" 2>&1; then
        echo "  PASS  $label"
    else
        echo "  FAIL  $label"
        sed 's/^/        /' "$OUT" | tail -25
        FAILED=1
    fi
}

command -v python3 >/dev/null || { echo "python3 not found"; exit 1; }
python3 -c 'import pytest' 2>/dev/null || {
    echo "pytest is not installed — install it with: python3 -m pip install pytest pyyaml"
    exit 1
}

echo "== pytest: docs-review scripts"
# -p no:cacheprovider: without it pytest drops a .pytest_cache/ into the tests'
# own directory, and agent skill discovery walks every *.md under
# .claude/commands/ — so the cache's README.md registers as a bogus skill for
# anyone who has run the tests locally. Nothing here uses --last-failed.
run "pytest .claude/commands/docs-review/scripts/" \
    python3 -m pytest .claude/commands/docs-review/scripts/ -q -p no:cacheprovider

echo "== pytest: review-v3 scripts"
run "pytest scripts/review-v3/" \
    python3 -m pytest scripts/review-v3/ -q

echo "== pytest: review-admin"
run "pytest scripts/review-admin/" \
    python3 -m pytest scripts/review-admin/ -q

echo "== standalone harnesses"
for f in scripts/content-review/test_*.py scripts/blog-review/test_*.py; do
    [ -e "$f" ] || continue
    run "$f" python3 "$f"
done

echo "== --self-test suites"
for f in scripts/content-review/*.py scripts/blog-review/*.py \
         scripts/review-v3/*.py \
         .claude/commands/docs-review/scripts/*.py; do
    [ -e "$f" ] || continue
    # Match the argparse registration, not any mention of the flag — a script
    # that merely documents --self-test in a docstring must not be invoked
    # with it and then reported FAIL.
    grep -qE '(add_argument\(|")--self-test' "$f" || continue
    run "$(basename "$f") --self-test" python3 "$f" --self-test
done

if [ "$FAILED" -ne 0 ]; then
    echo
    echo "review-pipeline tests FAILED"
    exit 1
fi
echo
echo "review-pipeline tests passed"
