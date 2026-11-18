#!/usr/bin/env bash
# Dispatch a staging deploy of a PR head to that PR's own stack (www-pr-<n>,
# see scripts/pr-stack.sh) — the deploy whose run record (and the
# `staging/pulumi-test-io` status written from it) is the evidence Sentinel
# gate G4 verifies. The status keeps its old context name so the Sentinel,
# branch protection, and open PRs don't have to change with it.
#
# Two callers: staging-deploy-command.yml (`/deploy-staging`), and
# staging-deploy-auto.yml, for every infra PR on open/push,
# unattended. It fires the deploy and gets out. Nobody is watching, so
# holding a runner for 45 minutes buys nothing, and a job that lives that
# long is a job that shows up cancelled on the PR when a newer push
# displaces it. A retry is a re-run of the dispatched "Build and deploy
# testing" run, or a fresh dispatch of that workflow at the head branch.
#
# ONE WRITER OF THE TERMINAL STATUS, AND IT IS NOT THIS SCRIPT.
# `.github/workflows/staging-status.yml` — a `workflow_run` listener on
# "Build and deploy testing" — writes success/failure/error when the
# dispatched run completes. Two writers of one context is noise, and the
# one that used to live inside the dispatched run was worse than noise,
# because a `workflow_dispatch` executes the workflow file from the ref it
# is dispatched at — so it silently did not exist for any PR branch cut
# before it merged. See that file's header for the rule.
#
# This script never checks out or executes the PR's code. It dispatches the
# existing "Build and deploy testing" workflow at the head BRANCH — that
# workflow does the checkout and build, in the testing account, exactly as
# it does for master. Keep it that way: the caller runs with write
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

REPO=""; HEAD_SHA=""; HEAD_REF=""; PR=""
while [ $# -gt 0 ]; do
  case "$1" in
    --repo)     REPO="$2"; shift 2 ;;
    --head-sha) HEAD_SHA="$2"; shift 2 ;;
    --head-ref) HEAD_REF="$2"; shift 2 ;;
    # Names the PR whose own stack (www-pr-<n>, scripts/pr-stack.sh) gets the
    # deploy. Optional: looked up from the head branch when a caller doesn't
    # pass it, which an open PR's older copy of staging-deploy-auto.yml won't.
    --pr)            PR="$2"; shift 2 ;;
    # Accepted and ignored: a branch cut before the watch mode went away
    # still passes it.
    --dispatch-only) shift ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done
for required in REPO HEAD_SHA HEAD_REF; do
  if [ -z "${!required}" ]; then
    echo "missing required argument: --$(echo "$required" | tr '[:upper:]_' '[:lower:]-')" >&2
    exit 2
  fi
done

# The dispatch API returns nothing. Stamp the time first and select the
# first workflow_dispatch run on this branch created after it — `--limit 1`
# on the branch would happily pick up an earlier push or re-dispatched run
# and post ITS outcome as this head's status. Backed off 2 s: both sides are
# whole seconds and the compare is strict, so a run created in the stamp's
# own second would otherwise be excluded by its own timestamp.
if [ -z "$PR" ]; then
  PR=$(gh pr list --repo "$REPO" --head "$HEAD_REF" --state open \
         --json number --jq '.[0].number // empty') || PR=""
fi
if [ -n "$PR" ] && ! [[ "$PR" =~ ^[0-9]+$ ]]; then
  echo "::error::--pr must be a PR number, got '$PR'" >&2
  exit 2
fi

# The deploy goes to the PR's own stack, never to pulumi-test.io, which only
# takes master. A `workflow_dispatch` runs the workflow file from the ref it
# targets, so a branch cut before testing-build-and-deploy.yml grew its
# `pr_number` input rejects the input (HTTP 422, "Unexpected inputs"). Such a
# branch still gets a deploy, to pulumi-test.io as before, until it's rebased.
SINCE=$(date -u -d '2 seconds ago' +%FT%TZ)
DISPATCH_LOG=$(mktemp)
if [ -z "$PR" ]; then
  echo "::warning::no open PR for $HEAD_REF; deploying it to pulumi-test.io instead of a PR stack"
  gh workflow run testing-build-and-deploy.yml --repo "$REPO" --ref "$HEAD_REF"
elif ! gh workflow run testing-build-and-deploy.yml --repo "$REPO" --ref "$HEAD_REF" \
       -f pr_number="$PR" 2> "$DISPATCH_LOG"; then
  cat "$DISPATCH_LOG" >&2
  if ! grep -qi "unexpected inputs" "$DISPATCH_LOG"; then
    exit 1
  fi
  echo "::warning::$HEAD_REF predates PR stacks, so it deploys to pulumi-test.io. Merge master into it to get its own stack."
  gh workflow run testing-build-and-deploy.yml --repo "$REPO" --ref "$HEAD_REF"
fi
rm -f "$DISPATCH_LOG"

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

# NO PENDING STATUS. This used to post `staging/pulumi-test-io` = pending,
# "staging deploy running", for `staging-status.yml` to finalize when the
# run completed. Twice now the finalizer has not run and the status stayed
# pending forever, telling every reader of the merge box that a deploy
# finished 40 minutes ago was still going:
#
#   1. #21676 — the finalizer was a job inside the dispatched run, and
#      `workflow_dispatch` executes the file from the ref it is dispatched
#      at, so a branch cut before that job merged never had it.
#   2. #21696 — the finalizer moved to a `workflow_run` listener, which
#      fixed (1). But GitHub does not emit a `workflow_run` cascade for a
#      run dispatched with GITHUB_TOKEN, which is what the auto lane
#      dispatches with. Every one of that listener's runs was a master
#      push; not one of the six dispatched PR-branch deploys after it
#      landed produced one.
#
# The status was never the deploy — it is a *report* of the deploy, written
# by a separate API call that can always be the thing that fails. The deploy
# itself is the run record, and `sentinel._staging_evidence` already reads
# it as witness (2), so nothing downstream needs this write. An absent
# status honestly says "no evidence recorded"; a stuck pending one says
# something false, and says it indefinitely. The terminal (green/failed)
# status is still written by `staging-status.yml` when its cascade does
# fire, which is upside without a failure mode: a status that never appears
# costs a reader nothing, and G4 falls through to the run record.
#
# If a pending status ever comes back, it needs a writer that CANNOT miss —
# a `schedule` sweep that finalizes any pending status whose run has
# completed, not an event cascade. Branch age and token provenance both
# have to stop mattering.

# Nothing is left pending on the PR. `staging-status.yml` writes a green
# `staging/pulumi-test-io` if its cascade fires; if it doesn't, Sentinel G4
# reads this run record directly and the merge box simply shows one check
# fewer. Either way nobody holds a runner open to watch.
echo "staging deploy dispatched for $HEAD_REF @ ${HEAD_SHA:0:9}: $RUN_URL"
