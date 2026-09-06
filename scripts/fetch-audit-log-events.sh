#!/usr/bin/env bash
# Fetches the catalog of Pulumi Cloud audit log event types from the Pulumi
# Cloud REST API, groups each event into a documentation category, and writes
# the result to data/audit_log_events.json -- the single source of truth for
# the audit log events reference page
# (content/docs/administration/reference/audit-log-events.md).
#
# The categories, and the rules that assign events to them, live in
# data/audit_log_event_categories.yaml; that file's header comment is the
# authoritative reference for changing them.
#
# The endpoint is org-scoped but its response is not: every organization gets
# the same catalog, because it describes what Pulumi Cloud can emit rather than
# what any one org has emitted. PULUMI_ORG therefore only decides which org's
# permissions the request is checked against.
#
# This endpoint requires authentication, so this script is NOT part of the
# normal `make ensure` build (which must work without a token). It is run by the
# .github/workflows/update-audit-log-events.yml GitHub Action, which supplies a
# token and opens a PR when the committed data changes. Run it locally only for
# testing, with PULUMI_ACCESS_TOKEN set.
#
# Needs PyYAML. The workflow installs it; locally, either `pip install pyyaml`
# or point PYTHON at an interpreter that already has it.

set -euo pipefail

API="${PULUMI_API:-https://api.pulumi.com}"
ORG="${PULUMI_ORG:-pulumi}"
PYTHON="${PYTHON:-python3}"
CATEGORIES="data/audit_log_event_categories.yaml"
OUTPUT="data/audit_log_events.json"

if [[ -z "${PULUMI_ACCESS_TOKEN:-}" ]]; then
  echo "error: PULUMI_ACCESS_TOKEN is not set. This script calls an authenticated" >&2
  echo "       Pulumi Cloud endpoint and cannot run without a token." >&2
  exit 1
fi

if ! "$PYTHON" -c "import yaml" 2>/dev/null; then
  echo "error: PyYAML is not available to '${PYTHON}'. Install it with" >&2
  echo "       '${PYTHON} -m pip install pyyaml', or set PYTHON to an" >&2
  echo "       interpreter that has it." >&2
  exit 1
fi

WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

echo "Fetching audit log event types from ${API} (org: ${ORG})..."
curl -sfL --retry 3 --retry-all-errors --connect-timeout 10 --max-time 60 \
  -H "Authorization: token ${PULUMI_ACCESS_TOKEN}" \
  "${API}/api/orgs/${ORG}/auditlogs/event-types" -o "$WORKDIR/event-types.json"

"$PYTHON" - "$WORKDIR/event-types.json" "$CATEGORIES" "$OUTPUT" <<'PY'
import json
import sys

import yaml

source, categories_path, output = sys.argv[1], sys.argv[2], sys.argv[3]

with open(source) as f:
    payload = json.load(f)

events = payload.get("eventTypes")
if not events:
    # An empty or reshaped response would silently publish an empty reference
    # page, so refuse it rather than committing the result.
    sys.exit(
        "error: %s response has no non-empty 'eventTypes' array" % source
    )

with open(categories_path) as f:
    categories = yaml.safe_load(f)

# Build the lookup tables. Exact ids always win; among prefixes, the longest
# match wins, which is what keeps `organization-token-created` in access-tokens
# rather than organization. See the header comment in the categories file.
exact = {}
prefixes = []
for category in categories:
    cid = category["id"]
    match = category.get("match") or {}
    for event in match.get("events") or []:
        exact[event] = cid
    for prefix in match.get("prefixes") or []:
        prefixes.append((prefix, cid))
prefixes.sort(key=lambda pair: len(pair[0]), reverse=True)


def categorize(event):
    if event in exact:
        return exact[event]
    for prefix, cid in prefixes:
        if event.startswith(prefix):
            return cid
    return None


result = []
unmapped = []
for event in events:
    cid = categorize(event["event"])
    if cid is None:
        unmapped.append(event["event"])
        continue
    result.append(dict(event, category=cid))

if unmapped:
    # Deliberately fatal. Filing a new event under a catch-all "Other" bucket
    # would ship it undocumented-in-practice and nobody would ever come back to
    # it; a failed nightly run posts to #docs-ops and gets a one-line fix.
    sys.exit(
        "error: %d audit log event(s) match no category rule in %s:\n  %s\n"
        "Add them to the appropriate category's `match` block (see that file's "
        "header comment) and rerun." % (
            len(unmapped), categories_path, "\n  ".join(sorted(unmapped))
        )
    )

# Sort by event id and sort keys within each object so the committed file is a
# stable, reviewable diff: an added event shows up as an added block, not as a
# reshuffle of the whole file.
result.sort(key=lambda event: event["event"])

with open(output, "w") as f:
    json.dump({"eventTypes": result}, f, indent=2, sort_keys=True)
    f.write("\n")

print("Categorized %d audit log events into %d categories." % (
    len(result), len({event["category"] for event in result})
))
PY

echo "Wrote audit log events to ${OUTPUT}"
