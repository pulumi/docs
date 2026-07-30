#!/bin/bash

# Posts a Slack warning when the "Build and deploy" step of a successful run
# exceeds BUILD_DURATION_THRESHOLD_MINUTES. This is a guardrail against silent
# build-time regressions (in July 2026 the build grew ~60% over three weeks
# before anyone noticed): it never fails the build, and it stays quiet when the
# build is healthy.
#
# Expects:
#   CI_BUILD_START_EPOCH               epoch seconds recorded just before the build step
#   SLACK_WEBHOOK_URL                  incoming webhook for the alert channel (docs-ops)
#   BUILD_DURATION_THRESHOLD_MINUTES   alert threshold (default 15)

set -o nounset

if [ -z "${CI_BUILD_START_EPOCH:-}" ]; then
    echo "CI_BUILD_START_EPOCH not set; skipping build-duration check."
    exit 0
fi

threshold_minutes="${BUILD_DURATION_THRESHOLD_MINUTES:-15}"
elapsed_seconds=$(( $(date +%s) - CI_BUILD_START_EPOCH ))
elapsed_minutes=$(( elapsed_seconds / 60 ))

echo "Build step took ${elapsed_minutes}m ($((elapsed_seconds))s); threshold is ${threshold_minutes}m."

if [ "$elapsed_seconds" -le $(( threshold_minutes * 60 )) ]; then
    exit 0
fi

if [ -z "${SLACK_WEBHOOK_URL:-}" ]; then
    echo "Slow build detected but SLACK_WEBHOOK_URL is not set; cannot alert."
    exit 0
fi

run_url="${GITHUB_SERVER_URL:-https://github.com}/${GITHUB_REPOSITORY:-pulumi/docs}/actions/runs/${GITHUB_RUN_ID:-}"
message=":hourglass_flowing_sand: Build and deploy took *${elapsed_minutes}m* (threshold: ${threshold_minutes}m). Build time may be regressing — check Hugo's --templateMetrics output in the job log. <${run_url}|View run>"

payload=$(printf '{"channel": "docs-ops", "username": "docsbot", "icon_url": "https://www.pulumi.com/logos/brand/avatar-on-white.png", "text": "%s"}' "$message")

# Best-effort: an alert failure must never fail the deploy.
curl -sS -X POST -H "Content-Type: application/json" -d "$payload" "$SLACK_WEBHOOK_URL" || true
