#!/usr/bin/env bash
# Dispatch a pulumi-test.io staging deploy of a PR head and record the
# outcome as the `staging/pulumi-test-io` commit status at that head SHA —
# the evidence Sentinel gate G4 verifies.
#
# Two callers:
#   - staging-deploy-pr.yml   `/deploy-staging`, a tools-team member asking
#                             (--announce, because they're waiting on it;
#                             then WATCHES the run. The watch is not how the
#                             status gets written — see below — it is what
#                             keeps that lane's `staging-stack` concurrency
#                             group held for the length of the deploy, which
#                             is the only thing serializing hand-requested
#                             deploys of a single shared stack.)
#   - staging-deploy-auto.yml every infra PR on open/push, unattended
#                             (--dispatch-only: fire the deploy and get out.
#                             Nobody is watching, so holding a runner for
#                             45 minutes buys nothing, and a job that lives
#                             that long is a job that shows up cancelled on
#                             the PR when a newer push displaces it.)
#
# ONE WRITER OF THE TERMINAL STATUS, AND IT IS NOT THIS SCRIPT.
# `.github/workflows/staging-status.yml` — a `workflow_run` listener on
# "Build and deploy testing" — writes success/failure/error when the
# dispatched run completes. This script writes only the PENDING status,
# which has to happen at dispatch time. The watch path below therefore
# records nothing: two writers of one context is noise, and the one that
# used to live inside the dispatched run was worse than noise, because a
# `workflow_dispatch` executes the workflow file from the ref it is
# dispatched at — so it silently did not exist for any PR branch cut before
# it merged. See that file's header for the rule.
#
# This script never checks out or executes the PR's code. It dispatches the
# existing "Build and deploy testing" workflow at the head BRANCH — that
# workflow does the checkout and build, in the testing account, exactly as
# it does for master. Keep it that way: both callers run with write
# permissions.
#
# G4 also accepts the deploy RUN as evidence, so a lost status write no
# longer silently costs a PR its green gate. The status is still written
# because it is what shows in the merge box, linked to the deployed site.
#
# Requires: gh (authenticated via GH_TOKEN), a checkout of nothing in
# particular. Exits non-zero only when the dispatch itself could not be
# located — a FAILED deploy is a successful run of this script, because
# reporting the deploy's outcome is the listener's job, not this one's.

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
  # `.github/workflows/staging-status.yml` finalizes the pending status
  # above when this run completes, so it always resolves without anyone
  # holding a runner open to watch it — and it resolves for a PR branch of
  # any age, which an in-run job could not do (see that file's header).
  echo "staging deploy dispatched for $HEAD_REF @ ${HEAD_SHA:0:9}: $RUN_URL"
  exit 0
fi

# Blocking mode (`/deploy-staging`). Deliberately writes NO status: the
# listener owns the terminal `staging/pulumi-test-io`. What this watch buys
# is the caller's concurrency group, held for the length of the deploy.
if gh run watch "$RUN_ID" --repo "$REPO" --exit-status; then
  STATE=success
else
  STATE=failure
fi
echo "staging deploy $STATE for $HEAD_REF @ ${HEAD_SHA:0:9}: $RUN_URL"
