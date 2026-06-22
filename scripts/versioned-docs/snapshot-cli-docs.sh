#!/usr/bin/env bash
#
# snapshot-cli-docs.sh — turn a freshly built CLI command docset into a self-contained,
# immutable snapshot and publish it to the versioned-docs archive bucket.
#
# Historical CLI docs never enter Hugo or the repo. Instead, the CLI release workflow
# runs a full `make build`, and this script:
#   1. extracts public/<commands-path>/ (the rendered CLI command pages),
#   2. strips per-page markdown outputs (latest-only content-negotiation convenience),
#   3. VENDORS the fingerprinted CSS/JS into _vassets/ and rewrites the references —
#      essential, because /css/<bundle>.<hash>.css and /js/<bundle>.<hash>.js live only in
#      the current atomic origin bucket and vanish at the next deploy. Stable, un-hashed
#      assets the CSS points at (/fonts/…, /images/…) are deliberately LEFT absolute: they
#      keep the same paths across deploys, so leaving them live keeps snapshots lean.
#   4. rewrites intra-snapshot links (/docs/iac/cli/commands/… → the versioned prefix) so
#      navigation stays within the version. Site chrome (header/footer) links elsewhere
#      and is deliberately left pointing at the live site.
#   5. hands the snapshot to publish-version.sh, which injects the selector/noindex/
#      canonical tags, uploads with immutable Cache-Control, and updates the manifest.
#
# Usage:
#   snapshot-cli-docs.sh --version vX.Y.Z --bucket B \
#       [--public ./public] [--tool pulumi-cli] [--commands-path docs/iac/cli/commands] \
#       [--live-root /docs/iac/cli/commands/] [--label "Pulumi CLI"] \
#       [--distribution-id D] [--site https://www.pulumi.com] [--force]
#
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

VERSION=""; BUCKET=""; PUBLIC="./public"; TOOL="pulumi-cli"
COMMANDS_PATH="docs/iac/cli/commands"; LIVE_ROOT=""; LABEL="Pulumi CLI"
DISTRIBUTION_ID=""; SITE="https://www.pulumi.com"; FORCE=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --version)         VERSION="$2"; shift 2;;
    --bucket)          BUCKET="$2"; shift 2;;
    --public)          PUBLIC="$2"; shift 2;;
    --tool)            TOOL="$2"; shift 2;;
    --commands-path)   COMMANDS_PATH="$2"; shift 2;;
    --live-root)       LIVE_ROOT="$2"; shift 2;;
    --label)           LABEL="$2"; shift 2;;
    --distribution-id) DISTRIBUTION_ID="$2"; shift 2;;
    --site)            SITE="$2"; shift 2;;
    --force)           FORCE="--force"; shift;;
    *) echo "snapshot-cli-docs: unknown arg: $1" >&2; exit 2;;
  esac
done

[[ -n "$VERSION" && -n "$BUCKET" ]] || { echo "snapshot-cli-docs: --version and --bucket are required" >&2; exit 2; }
[[ "$VERSION" == v* ]] || VERSION="v$VERSION"
[[ -n "$LIVE_ROOT" ]] || LIVE_ROOT="/${COMMANDS_PATH}/"
SRC_DIR="${PUBLIC%/}/${COMMANDS_PATH}"
[[ -d "$SRC_DIR" ]] || { echo "snapshot-cli-docs: built docs not found at $SRC_DIR (run make build first)" >&2; exit 2; }

VERSION_ROOT="/docs/versioned/${TOOL}/${VERSION}"   # no trailing slash; used as a URL prefix

SNAP="$(mktemp -d)"
trap 'rm -rf "$SNAP"' EXIT
cp -a "$SRC_DIR/." "$SNAP/"

# 2. Strip markdown content-negotiation outputs (latest-only; avoids stale scraping).
find "$SNAP" -type f -name '*.md' -delete

# Literal-string replacement across all snapshot HTML. Uses find+sed (no grep) so it's
# robust to grep variants — notably ugrep, where -Z means fuzzy-match and --include is
# read as a filename. sed_escape_lhs/rhs keep the needle/replacement literal.
sed_escape_lhs() { printf '%s' "$1" | sed 's/[][\\.*^$#]/\\&/g'; }
sed_escape_rhs() { printf '%s' "$1" | sed 's/[\\&#]/\\&/g'; }
replace_in_html() { # $1=needle $2=replacement
  local n r; n="$(sed_escape_lhs "$1")"; r="$(sed_escape_rhs "$2")"
  find "$SNAP" -type f -name '*.html' -exec sed -i "s#${n}#${r}#g" {} +
}

# 3a. Vendor fingerprinted CSS/JS referenced from the HTML.
mapfile -t ASSETS < <(find "$SNAP" -type f -name '*.html' -exec cat {} + \
  | grep -oE '(href|src)="(/css/[^"]+\.css|/js/[^"]+\.js)"' \
  | sed -E 's/.*"(\/[^"]+)".*/\1/' | sort -u)
for a in "${ASSETS[@]}"; do
  src="${PUBLIC%/}${a}"
  if [[ -f "$src" ]]; then
    dest="${SNAP}/_vassets${a}"
    mkdir -p "$(dirname "$dest")"
    cp "$src" "$dest"
    replace_in_html "\"${a}\"" "\"${VERSION_ROOT}/_vassets${a}\""
  else
    echo "snapshot-cli-docs: WARNING asset not found, leaving reference live: $a" >&2
  fi
done

# Note: the vendored CSS keeps its url(/fonts/…) and url(/images/…) refs absolute on
# purpose — those paths are stable across deploys, so they resolve against the live site
# and we avoid re-copying identical font/icon sets into every version.

# 4. Rewrite intra-snapshot command links to the versioned prefix.
replace_in_html "${LIVE_ROOT}" "${VERSION_ROOT}/"

# 4b. CLI command pages borrow the entire site docs mega-menu as their left-nav. Trim it
# to just this version's command list, with synthetic "Docs Home" + "Latest Version" items
# on top (pointing live). This makes the CLI archive self-contained, like the SDK docs.
python3 "$SCRIPT_DIR/trim-cli-nav.py" --src "$SNAP" \
  --version-root "${VERSION_ROOT}/" --live-root "${LIVE_ROOT}"

# 5. Publish (publish-version.sh injects selector/noindex/canonical + uploads + manifest).
"$SCRIPT_DIR/publish-version.sh" --tool "$TOOL" --version "$VERSION" --src "$SNAP" \
  --live-root "$LIVE_ROOT" --bucket "$BUCKET" --label "$LABEL" --site "$SITE" \
  ${DISTRIBUTION_ID:+--distribution-id "$DISTRIBUTION_ID"} ${FORCE:+$FORCE}

echo "snapshot-cli-docs: DONE — $TOOL $VERSION"
