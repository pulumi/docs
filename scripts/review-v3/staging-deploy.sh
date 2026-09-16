#!/usr/bin/env bash
# Dispatch a pulumi-test.io staging deploy of a PR head and record the
# outcome as the `staging/pulumi-test-io` commit status at that head SHA —
# the evidence Sentinel gate G4 verifies.
#
# Two callers, one behaviour:
#   - staging-deploy-pr.yml   `/deploy-staging`, a tools-team member asking
#                             (passes --announce, because they're waiting on it,
#                             and watches the run so the status is final when
#                             the job ends)
#   - staging-deploy-auto.yml every infra PR on open/push, unattended
#                             (--dispatch-only: fire the deploy and get out.
#                             Nobody is watching, so holding a runner for
#                             45 minutes buys nothing, and a job that lives
#                             that long is a job that shows up cancelled on
#                             the PR when a newer push displaces it. The
#                             dispatched run finalizes its own status.)
#
# This script never checks out or executes the PR's code. It dispatches the
# existing "Build and deploy testing" workflow at the head BRANCH — that
# workflow does the checkout and build, in the testing account, exactly as
# it does for master — then polls, watches, and writes the status. Keep it
# that way: both callers run with write permissions.
#
# G4 also accepts the deploy RUN as evidence, so a lost status write no
# longer silently costs a PR its green gate. The status is still written
# because it is what shows in the merge box with a link to the run.
#
# Requires: gh (authenticated via GH_TOKEN), a checkout of nothing in
# particular. Exits non-zero only when the dispatch itself could not be
# located — a FAILED deploy is a successful run of this script that records
# `failure`.

set -euo pipefail

REPO=""; PR=""; HEAD_SHA=""; HEAD_REF=""; ANNOUNCE="false"; DISPATCH_ONLY="false"
while [ $# -gt 0 ]; do
  case "$1" in
    --repo)     REPO="$2"; shift 2 ;;
    --pr)       PR="$2"; shift 2 ;;
    --head-sha) HEAD_SHA="$2"; shift 2 ;;
    --head-ref) HEAD_REF="$2"; shift 2 ;;
    --announce) ANNOUNCE="true"; shift ;;
    --dispatch-only) DISPATCH_ONLY="true"; shift ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done
for required in REPO PR HEAD_SHA HEAD_REF; do
  if [ -z "${!required}" ]; then
    echo "missing required argument: --$(echo "$required" | tr '[:upper:]_' '[:lower:]-')" >&2
    exit 2
  fi
done

# The dispatch API returns nothing. Stamp the time first and select the
# first workflow_dispatch run on this branch created after it — `--limit 1`
# on the branch would happily pick up an earlier push or /deploy-staging run
# and post ITS outcome as this head's status. Backed off 2 s: both sides are
# whole seconds and the compare is strict, so a run created in the stamp's
# own second would otherwise be excluded by its own timestamp.
SINCE=$(date -u -d '2 seconds ago' +%FT%TZ)
gh workflow run testing-build-and-deploy.yml --repo "$REPO" --ref "$HEAD_REF"

RUN_ID=""
for _ in $(seq 1 12); do
  sleep 5
  RUN_ID=$(gh run list --repo "$REPO" --workflow testing-build-and-deploy.yml \
             --branch "$HEAD_REF" --event workflow_dispatch --limit 10 \
             --json databaseId,createdAt \
             --jq "[.[] | select(.createdAt > \"$SINCE\")] | sort_by(.createdAt) | first | .databaseId // empty")
  # `if … break` rather than `[ … ] && break`: under set -e the falsy
  # AND-list as the loop's last command would make the `for` exit non-zero
  # and skip the diagnostic below.
  if [ -n "$RUN_ID" ]; then break; fi
done
if [ -z "$RUN_ID" ]; then
  echo "::error::could not locate the dispatched testing deploy run (no workflow_dispatch run on $HEAD_REF created after $SINCE within 60 s)"
  exit 1
fi
RUN_URL="https://github.com/$REPO/actions/runs/$RUN_ID"

gh api --method POST "repos/$REPO/statuses/$HEAD_SHA" \
  -f state=pending -f context="staging/pulumi-test-io" \
  -f target_url="$RUN_URL" \
  -f description="staging deploy running" >/dev/null

if [ "$ANNOUNCE" = "true" ]; then
  gh api --method POST "repos/$REPO/issues/$PR/comments" \
    -f body="🚀 Staging deploy of \`$HEAD_REF\` @ \`${HEAD_SHA:0:9}\` started: $RUN_URL — the \`staging/pulumi-test-io\` status lands here when it finishes. (Next merge to master resets pulumi-test.io. Requests queue one deep on the shared stack: a \`/deploy-staging\` that never gets this comment was displaced by a newer one — re-run it once the current deploy finishes.)" >/dev/null
fi

if [ "$DISPATCH_ONLY" = "true" ]; then
  # The run writes its own final status (see the `staging status` job in
  # testing-build-and-deploy.yml), so the pending status above always
  # resolves without anyone holding a runner open to watch it.
  echo "staging deploy dispatched for $HEAD_REF @ ${HEAD_SHA:0:9}: $RUN_URL"
  exit 0
fi

if gh run watch "$RUN_ID" --repo "$REPO" --exit-status; then
  STATE=success; DESC="staging deploy green"
else
  STATE=failure; DESC="staging deploy failed"
fi
gh api --method POST "repos/$REPO/statuses/$HEAD_SHA" \
  -f state="$STATE" -f context="staging/pulumi-test-io" \
  -f target_url="$RUN_URL" -f description="$DESC" >/dev/null

echo "staging deploy $STATE for $HEAD_REF @ ${HEAD_SHA:0:9}: $RUN_URL"
