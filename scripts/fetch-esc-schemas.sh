#!/usr/bin/env bash
# Fetches the JSON schemas for every ESC provider and rotator, plus the schema
# for the built-in `context` object, from the Pulumi Cloud REST API and writes
# them to data/esc_schemas.json, the single source of truth for the
# auto-generated schema-reference tables on the ESC provider and rotator pages
# (content/docs/esc/providers/**) and for the built-in properties reference
# (content/docs/esc/concepts/builtin-properties.md).
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

# The built-in `context` object is a singleton: there is no list endpoint and no
# name, so it gets its own fetch rather than joining the loop above.
echo "Fetching ESC context schema..."
fetch /api/esc/context/schema "$WORKDIR/context.json"

# Assemble the combined, sorted, pretty-printed data file for stable diffs.
python3 - "$WORKDIR" "$OUTPUT" <<'PY'
import json
import os
import sys


def normalize(node):
    """Impose a total order on the schema so equal content serializes equally.

    The API returns order-insignificant arrays in a nondeterministic order --
    `rotateOnly` on the mysql and postgres rotators has been observed to flip
    between runs. Left alone that produces a nightly diff when nothing actually
    changed, which auto-merges a no-op PR and falsely advances the "last
    updated" date the provider pages render.

    Arrays whose elements are all strings (`required`, `enum`, `rotateOnly`,
    and JSON Schema's array form of `type`) are sets, so sorting them loses
    nothing. Arrays of objects (`examples`, `oneOf`, `anyOf`) carry presentation
    order that the docs templates render as written, so they are left alone --
    and their nesting is still normalized.

    Dict key order is handled separately, by json.dump(sort_keys=True).
    """
    if isinstance(node, dict):
        return {key: normalize(value) for key, value in node.items()}
    if isinstance(node, list):
        items = [normalize(value) for value in node]
        if items and all(isinstance(item, str) for item in items):
            return sorted(items)
        return items
    return node


workdir, output = sys.argv[1], sys.argv[2]
result = {}
for kind in ("providers", "rotators"):
    schemas = {}
    for fname in sorted(os.listdir(os.path.join(workdir, kind))):
        name = fname[:-len(".json")]
        with open(os.path.join(workdir, kind, fname)) as f:
            schemas[name] = json.load(f)
    result[kind] = schemas

# Unlike the provider/rotator endpoints, which return the schema document
# directly, the context endpoint wraps it as {"schema": {...}}. Unwrap it so all
# three top-level keys are shaped alike, and fail loudly if it's missing — a
# silently empty object would render an empty properties reference.
with open(os.path.join(workdir, "context.json")) as f:
    context = json.load(f)
if "schema" not in context:
    sys.exit("error: /api/esc/context/schema response has no 'schema' key")
result["context"] = context["schema"]

os.makedirs(os.path.dirname(output), exist_ok=True)
with open(output, "w") as f:
    json.dump(normalize(result), f, indent=2, sort_keys=True)
    f.write("\n")
PY

echo "Wrote ESC schemas to ${OUTPUT}"
