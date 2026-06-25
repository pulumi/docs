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
DATE=""; MARK_LATEST="true"

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
    --date)            DATE="$2"; shift 2;;
    --no-mark-latest)  MARK_LATEST="false"; shift;;
    --force)           FORCE="--force"; shift;;
    --out-dir)         OUT_DIR="$2"; shift 2;;
    *) echo "snapshot-cli-docs: unknown arg: $1" >&2; exit 2;;
  esac
done
OUT_DIR="${OUT_DIR:-}"

[[ -n "$VERSION" ]] || { echo "snapshot-cli-docs: --version is required" >&2; exit 2; }
[[ -n "$BUCKET" || -n "$OUT_DIR" ]] || { echo "snapshot-cli-docs: --bucket is required (or --out-dir for a local dry run)" >&2; exit 2; }
[[ "$VERSION" == v* ]] || VERSION="v$VERSION"
[[ -n "$LIVE_ROOT" ]] || LIVE_ROOT="/${COMMANDS_PATH}/"
SRC_DIR="${PUBLIC%/}/${COMMANDS_PATH}"
[[ -d "$SRC_DIR" ]] || { echo "snapshot-cli-docs: built docs not found at $SRC_DIR (run make build first)" >&2; exit 2; }

VERSION_ROOT="/docs/versioned/${TOOL}/${VERSION}"   # no trailing slash; used as a URL prefix

SNAP="$(mktemp -d)"
trap 'rm -rf "$SNAP"' EXIT
cp -a "$SRC_DIR/." "$SNAP/"

# 2. KEEP the markdown content-negotiation outputs (*.md, one per command + the index) so the
# archived version is consumable by LLMs/agents exactly like the live docs. Their frontmatter
# `url:` and intra-doc links are rewritten to the versioned prefix in step 4.

# Literal-string replacement across snapshot files. Uses find+sed (no grep) so it's robust to
# grep variants — notably ugrep, where -Z means fuzzy-match and --include is read as a
# filename. sed_escape_lhs/rhs keep the needle/replacement literal.
sed_escape_lhs() { printf '%s' "$1" | sed 's/[][\\.*^$#]/\\&/g'; }
sed_escape_rhs() { printf '%s' "$1" | sed 's/[\\&#]/\\&/g'; }
replace_in_html() { # $1=needle $2=replacement — HTML only (css/js asset refs)
  local n r; n="$(sed_escape_lhs "$1")"; r="$(sed_escape_rhs "$2")"
  find "$SNAP" -type f -name '*.html' -exec sed -i "s#${n}#${r}#g" {} +
}
replace_in_content() { # $1=needle $2=replacement — HTML links AND the .md url:/cross-links
  local n r; n="$(sed_escape_lhs "$1")"; r="$(sed_escape_rhs "$2")"
  find "$SNAP" -type f \( -name '*.html' -o -name '*.md' \) -exec sed -i "s#${n}#${r}#g" {} +
}

# 3a. Theme: point the archive at the SHARED, stable archive theme bundle — a permanent
# contract URL (/css/versioned-docs-archive.css) served from the main site and refreshed on
# every site build (see scripts/build-site.sh). The fingerprinted /css/bundle.<id>.css the
# page was built with lives only in the current atomic origin and vanishes at the next
# deploy, so it MUST be swapped — and by pointing every version at one shared bundle instead
# of vendoring a frozen per-version copy, the entire CLI back-catalog re-themes at once when
# the site does. The bundle's own url(/fonts/…) / url(/images/…) refs stay absolute and
# resolve against the live site (those paths are stable across deploys).
ARCHIVE_CSS="/css/versioned-docs-archive.css"
mapfile -t CSS_REFS < <(find "$SNAP" -type f -name '*.html' -exec cat {} + \
  | grep -oE 'href="/css/bundle\.[^"]+\.css"' | sed -E 's/.*"(\/[^"]+)".*/\1/' | sort -u)
for a in "${CSS_REFS[@]}"; do
  replace_in_html "\"${a}\"" "\"${ARCHIVE_CSS}\""
done

# 3b. Drop the site JS <script src="/js/…"> bundles. CLI archives are static frozen pages:
# the left nav is trimmed to a static version list (step 4b), so the dynamic nav/search the
# site bundle drives is unnecessary — and that bundle lazy-loads fingerprinted /js/chunk-*.js
# that the snapshot never vendors, so it would 404 once the main site rotates. Stripping ALL
# /js/ src tags (not a fixed name list) keeps future-added bundles from sneaking back in. The
# evergreen selector loader (/js/versioned-docs.js) is added LATER by publish-version.sh, so
# it isn't present here to strip; external CDN scripts use absolute URLs and are left intact.
# (A consent-manager script is injected by inline JS rather than a src tag; it simply no-ops
# if its fingerprinted file 404s, so it's harmless to leave.)
find "$SNAP" -type f -name '*.html' -exec sed -i -E \
  's#<script[^>]*\ssrc="/js/[^"]+\.js"[^>]*>\s*</script>##g' {} +

# 4. Rewrite intra-snapshot command links to the versioned prefix — in the HTML AND in the
# kept .md files (their frontmatter `url:` and cross-command links), so the archived markdown
# self-references the versioned paths instead of pointing back at the live docs.
replace_in_content "${LIVE_ROOT}" "${VERSION_ROOT}/"

# 4b. Strip the borrowed live-site chrome so the archive is a self-contained, JS-free page:
# (1) replace the full-site docs mega-menu left-nav with this version's command list (synthetic
# "Docs Home" + "Latest Version" on top, pointing live); (2) drop the right-rail Edit/Request/
# feedback widgets + dead web components (meaningless on a frozen snapshot); (3) statically
# rebuild the "On this page" ToC, which the site JS normally fills at runtime — see the script
# header for the full rationale of each pass.
python3 "$SCRIPT_DIR/trim-cli-nav.py" --src "$SNAP" \
  --version-root "${VERSION_ROOT}/" --live-root "${LIVE_ROOT}"

# 5. Either write the finished snapshot to a local dir for inspection (--out-dir dry run,
# injecting the selector tags itself so the preview matches what gets published), or hand it
# to publish-version.sh (selector/noindex/canonical inject + upload + manifest).
if [[ -n "$OUT_DIR" ]]; then
  "$SCRIPT_DIR/inject-version-switcher.sh" --mode archive --tool "$TOOL" --version "$VERSION" \
    --live-root "$LIVE_ROOT" --src "$SNAP" --site "$SITE"
  mkdir -p "$OUT_DIR"
  cp -a "$SNAP/." "$OUT_DIR/"
  echo "snapshot-cli-docs: DRY RUN — wrote snapshot to $OUT_DIR (no publish)"
else
  "$SCRIPT_DIR/publish-version.sh" --tool "$TOOL" --version "$VERSION" --src "$SNAP" \
    --live-root "$LIVE_ROOT" --bucket "$BUCKET" --label "$LABEL" --site "$SITE" \
    ${DATE:+--date "$DATE"} $([[ "$MARK_LATEST" == "false" ]] && echo --no-mark-latest) \
    ${DISTRIBUTION_ID:+--distribution-id "$DISTRIBUTION_ID"} ${FORCE:+$FORCE}
fi

echo "snapshot-cli-docs: DONE — $TOOL $VERSION"
