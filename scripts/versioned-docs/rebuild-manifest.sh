#!/usr/bin/env bash
#
# rebuild-manifest.sh — regenerate a tool's versions.json from what's actually in the
# archive bucket, instead of the incremental read-modify-write that publish-version.sh does.
#
# Why: a parallel back-corpus backfill has many publish jobs racing on the same versions.json
# (last-write-wins drops entries). Letting each job publish its archive and then reconciling
# the manifest ONCE from the bucket listing sidesteps the race entirely. Because ordering is
# by semver (not date), no per-version release-date lookup is needed.
#
# It lists every docs/versioned/<tool>/v*/ archive prefix and writes a semver-sorted manifest.
# EVERY version — including the live "latest" (--latest-version) — is emitted pointing at its
# own immutable /vX/ archive path; the entry matching --latest-version just carries latest:true.
# The loader (versioned-docs.js baseFor) routes the latest entry to the liveRoot for freshness
# and every other entry to its archive path, so a version keeps a real archive to fall back to
# the moment it stops being latest (otherwise the demoted entry would alias the now-newer live
# docs — the dropdown-serves-wrong-version bug). If the latest version has no archive in the
# bucket yet, it is still emitted as a liveRoot/latest:true fallback so the selector never loses
# its live option. Existing per-version dates are preserved when present; otherwise left empty
# (unused — the UI sorts and labels by version, not date).
#
# Usage:
#   rebuild-manifest.sh --tool pulumi-cli --bucket pulumi-docs-versioned-testing \
#       --live-root /docs/iac/cli/commands/ --label "Pulumi CLI" \
#       --latest-version v3.247.0 [--distribution-id E6LY02AG7JXEZ]
#
set -euo pipefail

TOOL=""; BUCKET=""; LIVE_ROOT=""; LABEL=""; LATEST_VERSION=""; DISTRIBUTION_ID=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool)            TOOL="$2"; shift 2;;
    --bucket)          BUCKET="$2"; shift 2;;
    --live-root)       LIVE_ROOT="$2"; shift 2;;
    --label)           LABEL="$2"; shift 2;;
    --latest-version)  LATEST_VERSION="$2"; shift 2;;
    --distribution-id) DISTRIBUTION_ID="$2"; shift 2;;
    *) echo "rebuild-manifest: unknown arg: $1" >&2; exit 2;;
  esac
done

[[ -n "$TOOL" && -n "$BUCKET" && -n "$LIVE_ROOT" && -n "$LATEST_VERSION" ]] \
  || { echo "rebuild-manifest: --tool, --bucket, --live-root, --latest-version are required" >&2; exit 2; }

[[ "$LATEST_VERSION" == v* ]] || LATEST_VERSION="v$LATEST_VERSION"
[[ "$LIVE_ROOT" == /* ]] || LIVE_ROOT="/$LIVE_ROOT"
[[ "$LIVE_ROOT" == */ ]] || LIVE_ROOT="$LIVE_ROOT/"
[[ -n "$LABEL" ]] || LABEL="$TOOL"

VERSIONED_ROOT="/docs/versioned/${TOOL}/"
PREFIX="docs/versioned/${TOOL}/"
MANIFEST_KEY="${PREFIX}versions.json"

# Existing manifest — kept only to preserve any per-version dates already recorded.
existing="$(aws s3 cp "s3://${BUCKET}/${MANIFEST_KEY}" - 2>/dev/null || echo '{}')"
[[ -n "$existing" ]] || existing='{}'

# Archive version prefixes: the "PRE vX.Y.Z/" sub-prefixes directly under the tool root.
mapfile -t ARCHIVES < <(aws s3 ls "s3://${BUCKET}/${PREFIX}" \
  | awk '/ PRE v[0-9]/{sub(/\/$/,"",$2); print $2}')

echo "rebuild-manifest: tool=$TOOL archives=${#ARCHIVES[@]} latest=$LATEST_VERSION"

versions_json="$(printf '%s\n' "${ARCHIVES[@]}" | jq -R 'select(length>0)' | jq -s \
  --arg latest "$LATEST_VERSION" --arg liveRoot "$LIVE_ROOT" --arg vroot "$VERSIONED_ROOT" \
  --argjson existing "$existing" '
  ( ($existing.versions // []) | map({ (.version): (.date // "") }) | add // {} ) as $dates
  | ( map({ version: ., date: ($dates[.] // ""), path: ($vroot + . + "/"), latest: (. == $latest) }) ) as $entries
  | ( if ($entries | any(.version == $latest)) then $entries
      else $entries + [ { version: $latest, date: ($dates[$latest] // ""), path: $liveRoot, latest: true } ] end )
  | sort_by(.version | ltrimstr("v") | (try (split(".") | map(tonumber)) catch [.])) | reverse
')"

manifest="$(jq -n \
  --arg tool "$TOOL" --arg label "$LABEL" --arg liveRoot "$LIVE_ROOT" \
  --arg vroot "$VERSIONED_ROOT" --argjson versions "$versions_json" \
  '{ tool: $tool, label: $label, liveRoot: $liveRoot, versionedRoot: $vroot, versions: $versions }')"

printf '%s' "$manifest" | jq -e . >/dev/null   # validate before upload
echo "rebuild-manifest: writing $(printf '%s' "$manifest" | jq '.versions | length') versions"
printf '%s' "$manifest" | jq -r '.versions[] | "  \(.version)\(if .latest then "  (latest)" else "" end)"'

printf '%s' "$manifest" | aws s3 cp - "s3://${BUCKET}/${MANIFEST_KEY}" \
  --content-type "application/json" --cache-control "public, max-age=300"

if [[ -n "$DISTRIBUTION_ID" ]]; then
  aws cloudfront create-invalidation --distribution-id "$DISTRIBUTION_ID" \
    --paths "/${MANIFEST_KEY}" --query 'Invalidation.Id' --output text \
    | sed 's/^/rebuild-manifest: invalidation /'
fi

echo "rebuild-manifest: DONE — $TOOL"
