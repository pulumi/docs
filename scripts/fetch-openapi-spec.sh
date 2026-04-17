#!/usr/bin/env bash
# Downloads the Pulumi Cloud OpenAPI spec and renames x- extension keys
# so Hugo can access them (Hugo strips keys starting with "x-" during unmarshal).

set -euo pipefail

SPEC_URL="https://api.pulumi.com/api/openapi/pulumi-spec.json"
OUTPUT="data/openapi-spec.json"

mkdir -p "$(dirname "$OUTPUT")"

echo "Fetching OpenAPI spec from ${SPEC_URL}..."
curl -sfL --retry 3 --retry-all-errors --connect-timeout 10 --max-time 60 "$SPEC_URL" \
  | sed 's/"x-pulumi-route-property"/"pulumiRouteProperty"/g' \
  | sed 's/"x-order"/"pulumiOrder"/g' \
  > "$OUTPUT"

echo "Wrote $(wc -c < "$OUTPUT" | tr -d ' ') bytes to ${OUTPUT}"
