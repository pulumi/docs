#!/usr/bin/env bash
# Run every test suite belonging to the review pipelines (pre-merge PR review,
# daily content review, blog known-issues index).
#
# These suites were all green but nothing ran them: `make test` covers only the
# example programs, and no workflow invoked pytest or a --self-test. That gap
# is how a selector bot-list omission and a pytest-red test file both survived
# in master. This script is the single entry point; review-pipeline-tests.yml
# runs it on any PR that touches the pipeline.
#
# Three suite kinds, discovered rather than enumerated so a new script is
# covered the day it lands:
#   1. pytest over .claude/commands/docs-review/scripts/
#   2. standalone test_*.py harnesses (module-level check() style, not pytest)
#   3. every script exposing a --self-test flag
set -uo pipefail

cd "$(dirname "$0")/.."

FAILED=0
run() {
    local label="$1"; shift
    if "$@" >/tmp/rpt-out.txt 2>&1; then
        echo "  PASS  $label"
    else
        echo "  FAIL  $label"
        sed 's/^/        /' /tmp/rpt-out.txt | tail -25
        FAILED=1
    fi
}

echo "== pytest: docs-review scripts"
run "pytest .claude/commands/docs-review/scripts/" \
    python3 -m pytest .claude/commands/docs-review/scripts/ -q

echo "== standalone harnesses"
for f in scripts/content-review/test_*.py scripts/blog-review/test_*.py; do
    [ -e "$f" ] || continue
    run "$f" python3 "$f"
done

echo "== --self-test suites"
for f in scripts/content-review/*.py scripts/blog-review/*.py \
         .claude/commands/docs-review/scripts/*.py; do
    [ -e "$f" ] || continue
    grep -q -- '--self-test' "$f" || continue
    run "$(basename "$f") --self-test" python3 "$f" --self-test
done

if [ "$FAILED" -ne 0 ]; then
    echo
    echo "review-pipeline tests FAILED"
    exit 1
fi
echo
echo "review-pipeline tests passed"
