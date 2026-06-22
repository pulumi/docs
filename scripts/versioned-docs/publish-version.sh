#!/usr/bin/env bash
#
# publish-version.sh — publish one immutable docset snapshot to the permanent archive
# bucket and update the per-tool manifest.
#
# Steps:
#   1. Refuse if docs/versioned/{tool}/{version}/ already has objects (unless --force).
#   2. Inject archive tags (noindex + canonical + loader) onto a COPY of --src.
#   3. Sync the copy to the bucket with immutable Cache-Control (1 year).
#   4. Read-modify-write versions.json (insert/dedupe the entry, set `latest`,
#      sort newest-first), upload it with Cache-Control max-age=300.
#   5. Invalidate the manifest (and, with --force, the version prefix) in CloudFront.
#
# Requires AWS credentials with write access to the bucket (the versioned-docs-publisher
# role in CI, or a local admin profile) plus jq and the AWS CLI.
#
# Usage:
#   publish-version.sh --tool python --version v3.150.0 --src ./out \
#       --live-root /docs/reference/pkg/python/pulumi/ \
#       --bucket pulumi-docs-versioned-testing \
#       [--label "Python SDK"] [--distribution-id E123ABC] \
#       [--site https://www.pulumi.com] [--date 2026-06-10T00:00:00Z] \
#       [--no-mark-latest] [--force]
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

TOOL=""; VERSION=""; SRC=""; LIVE_ROOT=""; BUCKET=""; LABEL=""
DISTRIBUTION_ID=""; SITE="https://www.pulumi.com"; DATE=""
MARK_LATEST="true"; FORCE="false"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --tool)            TOOL="$2"; shift 2;;
    --version)         VERSION="$2"; shift 2;;
    --src)             SRC="$2"; shift 2;;
    --live-root)       LIVE_ROOT="$2"; shift 2;;
    --bucket)          BUCKET="$2"; shift 2;;
    --label)           LABEL="$2"; shift 2;;
    --distribution-id) DISTRIBUTION_ID="$2"; shift 2;;
    --site)            SITE="$2"; shift 2;;
    --date)            DATE="$2"; shift 2;;
    --no-mark-latest)  MARK_LATEST="false"; shift;;
    --force)           FORCE="true"; shift;;
    *) echo "publish-version: unknown arg: $1" >&2; exit 2;;
  esac
done

[[ -n "$TOOL" && -n "$VERSION" && -n "$SRC" && -n "$LIVE_ROOT" && -n "$BUCKET" ]] \
  || { echo "publish-version: --tool, --version, --src, --live-root, --bucket are required" >&2; exit 2; }
[[ -d "$SRC" ]] || { echo "publish-version: src dir not found: $SRC" >&2; exit 2; }

# Normalize: version carries a leading "v"; live root has leading + trailing slash.
[[ "$VERSION" == v* ]] || VERSION="v$VERSION"
[[ "$LIVE_ROOT" == /* ]] || LIVE_ROOT="/$LIVE_ROOT"
[[ "$LIVE_ROOT" == */ ]] || LIVE_ROOT="$LIVE_ROOT/"
[[ -n "$LABEL" ]] || LABEL="$TOOL"
[[ -n "$DATE" ]] || DATE="$(date -u +%Y-%m-%dT%H:%M:%SZ)"

VERSIONED_ROOT="/docs/versioned/${TOOL}/"
PREFIX="docs/versioned/${TOOL}/${VERSION}/"          # S3 key prefix (mirrors the URL, no leading slash)
VERSION_PATH="/docs/versioned/${TOOL}/${VERSION}/"   # URL path
MANIFEST_KEY="docs/versioned/${TOOL}/versions.json"
IMMUTABLE_CC="public, max-age=31536000, immutable"
MANIFEST_CC="public, max-age=300"

echo "publish-version: tool=$TOOL version=$VERSION bucket=$BUCKET prefix=$PREFIX mark_latest=$MARK_LATEST force=$FORCE"

# 1. Refuse to overwrite an existing immutable snapshot unless --force.
existing_count="$(aws s3api list-objects-v2 --bucket "$BUCKET" --prefix "$PREFIX" --max-items 1 \
  --query 'length(Contents || `[]`)' --output text 2>/dev/null || echo 0)"
if [[ "$existing_count" != "0" && "$existing_count" != "None" ]]; then
  if [[ "$FORCE" != "true" ]]; then
    echo "publish-version: REFUSING — objects already exist under $PREFIX (pass --force to overwrite)" >&2
    exit 1
  fi
  echo "publish-version: --force set; overwriting existing $PREFIX"
fi

# 2. Inject archive tags onto a copy (never mutate the caller's --src).
WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT
cp -a "$SRC/." "$WORKDIR/"

# 2a. DocFX/Javadoc SDKs (.NET, Java) ship NO root index.html — their landing page is
# Hugo-generated and absent from the prebuilt output, so the bare version root would 404,
# breaking both the entry URL and the version-selector's root fallback. Synthesize a small
# landing that links each top-level namespace entry. Run BEFORE injection so the landing
# also gets the loader/noindex/canonical. SDKs that already ship a root index.html (TypeDoc,
# Sphinx) skip this block untouched.
if [[ ! -f "$WORKDIR/index.html" ]]; then
  links=""
  for d in "$WORKDIR"/*/; do
    [[ -d "$d" ]] || continue
    name="$(basename "$d")"
    case "$name" in _vassets|fonts|styles|_static|css|js|images|search) continue;; esac
    if [[ -f "${d}index.html" ]]; then target="${name}/"
    elif [[ -f "${d}${name}.html" ]]; then target="${name}/${name}.html"
    else continue
    fi
    links+="    <li><a href=\"${target}\">${name}</a></li>"$'\n'
  done
  if [[ -n "$links" ]]; then
    echo "publish-version: synthesizing root landing (prebuilt has no index.html)"
    cat > "$WORKDIR/index.html" <<HTML
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>${LABEL} ${VERSION} — API Reference</title>
<style>
  body { font: 16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; max-width: 48rem; margin: 3rem auto; padding: 0 1.25rem; color: #2b2235; }
  h1 { font-size: 1.5rem; margin-bottom: .25rem; } h1 small { color: #6b6477; font-weight: 400; }
  ul { padding-left: 1.2rem; } li { margin: .35rem 0; } a { color: #8b5cf6; }
</style>
</head>
<body>
<h1>${LABEL} <small>${VERSION}</small></h1>
<p>Archived API reference. Select a namespace:</p>
<ul>
${links}</ul>
</body>
</html>
HTML
  else
    echo "publish-version: WARNING — no root index.html and no namespace entries found; bare version root will 404" >&2
  fi
fi

"$SCRIPT_DIR/inject-version-switcher.sh" --mode archive --tool "$TOOL" --version "$VERSION" \
  --live-root "$LIVE_ROOT" --src "$WORKDIR" --site "$SITE"

# 3. Sync to the bucket with immutable Cache-Control. aws s3 sync infers Content-Type
#    from file extensions and is available everywhere (CI + local), so we use it rather
#    than depending on s5cmd being installed in the doc-gen workflows.
sync_args=(--no-progress --cache-control "$IMMUTABLE_CC")
[[ "$FORCE" == "true" ]] && sync_args+=(--delete)
aws s3 sync "$WORKDIR/" "s3://${BUCKET}/${PREFIX}" "${sync_args[@]}"

# 4. Manifest read-modify-write.
existing_manifest="$(aws s3 cp "s3://${BUCKET}/${MANIFEST_KEY}" - 2>/dev/null || true)"
[[ -n "$existing_manifest" ]] || existing_manifest='{}'

updated_manifest="$(printf '%s' "$existing_manifest" | jq \
  --arg tool "$TOOL" --arg label "$LABEL" --arg liveRoot "$LIVE_ROOT" \
  --arg versionedRoot "$VERSIONED_ROOT" --arg version "$VERSION" \
  --arg date "$DATE" --arg path "$VERSION_PATH" --arg markLatest "$MARK_LATEST" '
  ( . // {} ) as $m
  | {
      tool: $tool, label: $label, liveRoot: $liveRoot, versionedRoot: $versionedRoot,
      versions: (
        ( [ { version: $version, date: $date, path: $path, latest: ($markLatest == "true") } ]
          + ( ($m.versions // []) | map(select(.version != $version)) ) )
        | ( if $markLatest == "true" then map(.latest = (.version == $version)) else . end )
        | sort_by(.date) | reverse
      )
    }
')"

printf '%s' "$updated_manifest" | jq -e . >/dev/null  # validate JSON before upload
printf '%s' "$updated_manifest" | aws s3 cp - "s3://${BUCKET}/${MANIFEST_KEY}" \
  --content-type "application/json" --cache-control "$MANIFEST_CC"

# 5. CloudFront invalidation (belt-and-braces; the 300s manifest TTL already bounds staleness).
if [[ -n "$DISTRIBUTION_ID" ]]; then
  paths=("/${MANIFEST_KEY}")
  [[ "$FORCE" == "true" ]] && paths+=("${VERSION_PATH}*")
  aws cloudfront create-invalidation --distribution-id "$DISTRIBUTION_ID" \
    --paths "${paths[@]}" --query 'Invalidation.Id' --output text \
    | sed 's/^/publish-version: invalidation /'
else
  echo "publish-version: no --distribution-id; skipping invalidation (manifest TTL is 300s)"
fi

echo "publish-version: DONE — $VERSION available at https://www.pulumi.com${VERSION_PATH}"
