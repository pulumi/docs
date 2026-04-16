#!/usr/bin/env bash
# Downloads the Pulumi Cloud OpenAPI spec and renames x- extension keys
# so Hugo can access them (Hugo strips keys starting with "x-" during unmarshal).

set -euo pipefail

# TEMPORARY: pointing at a public gist of openapi_public.json from the
# pulumi/pulumi-service tag-split PR (pulumi/pulumi-service#41439) so CI can
# test the new tag pages end-to-end. pulumi/pulumi-service is private, so the
# gist is the portable way to make the spec reachable from public CI.
# Revert to the prod URL before merging:
#   https://api.pulumi.com/api/openapi/pulumi-spec.json
SPEC_URL="https://gist.githubusercontent.com/djgrove/d2b675b48f819bc08e1dd3009a393d0a/raw/openapi_public.json"
OUTPUT="data/openapi-spec.json"

mkdir -p "$(dirname "$OUTPUT")"

echo "Fetching OpenAPI spec from ${SPEC_URL}..."
curl -sf "$SPEC_URL" \
  | sed 's/"x-pulumi-route-property"/"pulumiRouteProperty"/g' \
  | sed 's/"x-order"/"pulumiOrder"/g' \
  > "$OUTPUT"

echo "Wrote $(wc -c < "$OUTPUT" | tr -d ' ') bytes to ${OUTPUT}"
