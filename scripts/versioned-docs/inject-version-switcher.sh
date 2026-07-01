#!/usr/bin/env bash
#
# inject-version-switcher.sh — insert the versioned-docs selector loader (and, for
# archived snapshots, noindex + canonical tags) into generated SDK/CLI HTML before it
# is published to the permanent archive bucket.
#
# A single post-processor handles all four generator dialects — Sphinx dirhtml, docfx,
# TypeDoc, and javadoc — because every one of them emits a literal "</head>". (A CI
# assertion, scripts/versioned-docs/assert-head-tag.sh, keeps that invariant honest.)
#
# Modes:
#   --mode archive   3 insertions: <meta robots noindex>, <link rel=canonical> to the
#                    live-equivalent URL, and the evergreen loader <script>. Used on a
#                    COPY of a historical snapshot.
#   --mode latest    loader <script> only. Used on the freshly generated static-prebuilt
#                    output so the canonical/latest SDK pages also get the selector.
#
# Idempotent: any file already carrying `data-vdocs-tool` is skipped, so re-running is
# safe.
#
# Usage:
#   inject-version-switcher.sh --mode archive --tool python --version v3.150.0 \
#       --live-root /docs/reference/pkg/python/pulumi/ --src ./snapshot [--site https://www.pulumi.com]
#
set -euo pipefail

MODE=""; TOOL=""; VERSION=""; LIVE_ROOT=""; SRC=""; SITE="https://www.pulumi.com"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --mode)      MODE="$2"; shift 2;;
    --tool)      TOOL="$2"; shift 2;;
    --version)   VERSION="$2"; shift 2;;
    --live-root) LIVE_ROOT="$2"; shift 2;;
    --src)       SRC="$2"; shift 2;;
    --site)      SITE="$2"; shift 2;;
    *) echo "inject-version-switcher: unknown arg: $1" >&2; exit 2;;
  esac
done

[[ "$MODE" == "archive" || "$MODE" == "latest" ]] || { echo "inject-version-switcher: --mode must be archive|latest" >&2; exit 2; }
[[ -n "$TOOL" && -n "$LIVE_ROOT" && -n "$SRC" ]]   || { echo "inject-version-switcher: --tool, --live-root, --src are required" >&2; exit 2; }
[[ -d "$SRC" ]]                                    || { echo "inject-version-switcher: src dir not found: $SRC" >&2; exit 2; }
[[ "$MODE" == "latest" || -n "$VERSION" ]]         || { echo "inject-version-switcher: --version is required in archive mode" >&2; exit 2; }

# Normalize the live root to a leading + trailing slash so URL joins are clean.
[[ "$LIVE_ROOT" == /* ]]  || LIVE_ROOT="/$LIVE_ROOT"
[[ "$LIVE_ROOT" == */ ]]  || LIVE_ROOT="$LIVE_ROOT/"
SITE="${SITE%/}"

processed=0; skipped=0
while IFS= read -r -d '' f; do
  if grep -q 'data-vdocs-tool' "$f"; then
    skipped=$((skipped + 1)); continue
  fi

  # rel = path of this file relative to the snapshot root. For directory-index pages
  # (foo/index.html) the page's URL is the directory, so strip the trailing index.html;
  # non-index pages (e.g. javadoc Foo.html) keep their filename.
  rel="${f#"$SRC"/}"
  page_rel="$rel"
  case "$page_rel" in
    index.html)    page_rel="" ;;
    */index.html)  page_rel="${page_rel%index.html}" ;;
  esac

  loader="<script async src=\"/js/versioned-docs.js\" data-vdocs-tool=\"$TOOL\" data-vdocs-mode=\"$MODE\""
  [[ -n "$VERSION" ]] && loader="$loader data-vdocs-version=\"$VERSION\""
  loader="$loader data-vdocs-live-root=\"$LIVE_ROOT\" data-vdocs-rel=\"$page_rel\"></script>"

  if [[ "$MODE" == "archive" ]]; then
    canonical="${SITE}${LIVE_ROOT}${page_rel}"
    snippet="<meta name=\"robots\" content=\"noindex\"><link rel=\"canonical\" href=\"$canonical\">$loader"
  else
    snippet="$loader"
  fi

  # In archive mode, first strip any pre-existing canonical / robots tags: the original
  # build emits its own canonical (pointing at the live URL) and rewritten copies would
  # collide with the archive's noindex + canonical that we add below. Then insert the
  # snippet before the first </head> (case-insensitive; robust to minified heads since we
  # slurp the whole file with -0777 and substitute once). Fall back to </body> if a
  # dialect ever omits </head>. \x22/\x27 are " and ' — used to dodge shell quote escaping.
  SNIPPET="$snippet" VMODE="$MODE" perl -0777 -i -pe '
    if ($ENV{VMODE} eq "archive") {
      s{<link\b[^>]*\brel=[\x22\x27]canonical[\x22\x27][^>]*>}{}gi;
      s{<meta\b[^>]*\bname=[\x22\x27]robots[\x22\x27][^>]*>}{}gi;
    }
    my $s = $ENV{SNIPPET};
    s{</head>}{$s</head>}i or s{</body>}{$s</body>}i;
  ' "$f"
  processed=$((processed + 1))
done < <(find "$SRC" -type f -name '*.html' -print0)

echo "inject-version-switcher: mode=$MODE tool=$TOOL processed=$processed skipped=$skipped"
