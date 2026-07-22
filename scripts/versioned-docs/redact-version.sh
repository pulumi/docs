#!/usr/bin/env bash
#
# redact-version.sh — remove a published version from the archive bucket and manifest.
#
# An auditable ~2-minute operation. Deletes every S3 object version under the
# {tool}/{version}/ prefix (bucket versioning is on), drops the entry from versions.json
# (promoting the next-newest to `latest` if the redacted version was latest), and
# invalidates the prefix + manifest in CloudFront.
#
# Requires ADMIN AWS credentials (s3:DeleteObjectVersion + s3:ListBucketVersions on the bucket).
# The CI publisher role deliberately does NOT have these — it can publish and invalidate, but
# cannot permanently destroy archived object versions. Redaction is a rare, deliberate admin
# operation, so immutable archives can't be wiped by an automated or compromised CI run.
#
# Usage:
#   redact-version.sh --tool T --version vX.Y.Z --bucket B [--distribution-id D] [--yes]
#
set -euo pipefail

TOOL=""; VERSION=""; BUCKET=""; DISTRIBUTION_ID=""; ASSUME_YES="false"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool)            TOOL="$2"; shift 2;;
    --version)         VERSION="$2"; shift 2;;
    --bucket)          BUCKET="$2"; shift 2;;
    --distribution-id) DISTRIBUTION_ID="$2"; shift 2;;
    --yes)             ASSUME_YES="true"; shift;;
    *) echo "redact-version: unknown arg: $1" >&2; exit 2;;
  esac
done

[[ -n "$TOOL" && -n "$VERSION" && -n "$BUCKET" ]] \
  || { echo "redact-version: --tool, --version, --bucket are required" >&2; exit 2; }
[[ "$VERSION" == v* ]] || VERSION="v$VERSION"

PREFIX="docs/versioned/${TOOL}/${VERSION}/"
MANIFEST_KEY="docs/versioned/${TOOL}/versions.json"

echo "redact-version: tool=$TOOL version=$VERSION bucket=$BUCKET prefix=$PREFIX"
if [[ "$ASSUME_YES" != "true" ]]; then
  read -r -p "Permanently delete all objects under $PREFIX and remove it from the manifest? [y/N] " ans
  [[ "$ans" == "y" || "$ans" == "Y" ]] || { echo "redact-version: aborted"; exit 1; }
fi

# 1. Delete every object version + delete marker under the prefix, paginating until clean.
while :; do
  page="$(aws s3api list-object-versions --bucket "$BUCKET" --prefix "$PREFIX" --max-items 1000 --output json)"
  del="$(printf '%s' "$page" | jq -c '{Objects: ([ (.Versions // [])[], (.DeleteMarkers // [])[] ] | map({Key:.Key, VersionId:.VersionId})), Quiet: true}')"
  n="$(printf '%s' "$del" | jq '.Objects | length')"
  [[ "$n" -eq 0 ]] && break
  printf '%s' "$del" | aws s3api delete-objects --bucket "$BUCKET" --delete file:///dev/stdin >/dev/null
  echo "redact-version: deleted $n object version(s)"
done

# 2. Drop the entry from the manifest; promote the next-newest to latest if needed.
existing_manifest="$(aws s3 cp "s3://${BUCKET}/${MANIFEST_KEY}" - 2>/dev/null || true)"
if [[ -n "$existing_manifest" ]]; then
  updated="$(printf '%s' "$existing_manifest" | jq --arg v "$VERSION" '
    ( .versions // [] ) as $vs
    | ( $vs | any(.version == $v and (.latest == true)) ) as $wasLatest
    | .versions = ( $vs | map(select(.version != $v)) )
    | ( if $wasLatest and ((.versions | length) > 0) then .versions[0].latest = true else . end )
  ')"
  printf '%s' "$updated" | jq -e . >/dev/null
  printf '%s' "$updated" | aws s3 cp - "s3://${BUCKET}/${MANIFEST_KEY}" \
    --content-type "application/json" --cache-control "public, max-age=300"
  echo "redact-version: manifest updated"
else
  echo "redact-version: no manifest found; nothing to update"
fi

# 3. Invalidate the prefix + manifest.
if [[ -n "$DISTRIBUTION_ID" ]]; then
  aws cloudfront create-invalidation --distribution-id "$DISTRIBUTION_ID" \
    --paths "/${PREFIX}*" "/${MANIFEST_KEY}" --query 'Invalidation.Id' --output text \
    | sed 's/^/redact-version: invalidation /'
else
  echo "redact-version: no --distribution-id; skipping invalidation"
fi

echo "redact-version: DONE — $TOOL $VERSION redacted"
