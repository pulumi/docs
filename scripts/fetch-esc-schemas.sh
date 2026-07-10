#!/usr/bin/env bash
# Fetches the JSON schemas for every ESC provider and rotator from the Pulumi
# Cloud REST API and writes them to data/esc_schemas.json, the single source of
# truth for the auto-generated schema-reference tables on the ESC provider and
# rotator pages (content/docs/esc/providers/**).
#
# These endpoints require authentication, so this script is NOT part of the
# normal `make ensure` build (which must work without a token). It is run by the
# .github/workflows/esc-update-schemas.yml GitHub Action, which supplies a token
# and opens a PR when the committed data changes. Run it locally only for
# testing, with PULUMI_ACCESS_TOKEN set.

set -euo pipefail

API="${PULUMI_API:-https://api.pulumi.com}"
OUTPUT="data/esc_schemas.json"

if [[ -z "${PULUMI_ACCESS_TOKEN:-}" ]]; then
  echo "error: PULUMI_ACCESS_TOKEN is not set. This script calls authenticated" >&2
  echo "       ESC schema endpoints and cannot run without a token." >&2
  exit 1
fi

WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

# Fetch a JSON document from the API into a file. Retries transient failures.
fetch() {
  curl -sfL --retry 3 --retry-all-errors --connect-timeout 10 --max-time 60 \
    -H "Authorization: token ${PULUMI_ACCESS_TOKEN}" \
    "${API}$1" -o "$2"
}

echo "Fetching ESC provider and rotator lists from ${API}..."
fetch /api/esc/providers "$WORKDIR/providers.json"
fetch /api/esc/rotators "$WORKDIR/rotators.json"

# Fetch each individual schema into $WORKDIR/<kind>/<name>.json.
for kind in providers rotators; do
  mkdir -p "$WORKDIR/$kind"
  # `.providers` / `.rotators` is the JSON array key on each list response.
  names="$(python3 -c "import json,sys;print('\n'.join(json.load(open(sys.argv[1]))['$kind']))" "$WORKDIR/$kind.json")"
  singular="${kind%s}"
  while IFS= read -r name; do
    [[ -z "$name" ]] && continue
    echo "  ${kind}/${name}"
    fetch "/api/esc/${kind}/${name}/schema" "$WORKDIR/$kind/$name.json"
  done <<< "$names"
done

# Assemble the combined, sorted, pretty-printed data file for stable diffs.
python3 - "$WORKDIR" "$OUTPUT" <<'PY'
import json
import os
import sys

workdir, output = sys.argv[1], sys.argv[2]
result = {}
for kind in ("providers", "rotators"):
    schemas = {}
    for fname in sorted(os.listdir(os.path.join(workdir, kind))):
        name = fname[:-len(".json")]
        with open(os.path.join(workdir, kind, fname)) as f:
            schemas[name] = json.load(f)
    result[kind] = schemas

os.makedirs(os.path.dirname(output), exist_ok=True)
with open(output, "w") as f:
    json.dump(result, f, indent=2, sort_keys=True)
    f.write("\n")
PY

echo "Wrote ESC schemas to ${OUTPUT}"
