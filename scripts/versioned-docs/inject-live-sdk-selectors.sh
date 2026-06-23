#!/usr/bin/env bash
#
# inject-live-sdk-selectors.sh — at SITE BUILD TIME, add the version-selector loader
# (latest mode) to the live SDK reference docsets in public/. This gives the *current*
# SDK pages the same version dropdown the archives have, WITHOUT committing a <script>
# into the thousands of generated files under static-prebuilt/ (zero commit churn).
#
# Nested policy/ESC subtrees are injected FIRST with their own tool id; inject-version-
# switcher.sh is idempotent (skips any file already carrying data-vdocs-tool), so the
# parent docset pass leaves those subtree pages with their correct tool. The loader fails
# silent when a tool has no published versions yet, so this is safe before any backfill.
#
# Fail-safe: a missing docset is skipped, never fatal — the site build must not break if a
# docset is absent in a given build.
#
set -uo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PUBLIC="${1:-public}"
INJ="$SCRIPT_DIR/inject-version-switcher.sh"
REF="${PUBLIC%/}/docs/reference/pkg"

inject() { # tool  on-disk-subdir(relative to REF)  live-root
  local tool="$1" sub="$2" live="$3" dir="$REF/$2"
  [[ -d "$dir" ]] || { echo "inject-live-sdk: skip $tool (no $dir)"; return 0; }
  "$INJ" --mode latest --tool "$tool" --live-root "$live" --src "$dir" \
    || echo "inject-live-sdk: WARNING inject failed for $tool (continuing)" >&2
}

# Most-specific subtrees FIRST so the idempotent injector tags them with their own tool
# before the parent docset pass runs.
inject nodejs-policy    nodejs/pulumi/policy    /docs/reference/pkg/nodejs/pulumi/policy/
inject nodejs-esc-sdk   nodejs/pulumi/esc-sdk   /docs/reference/pkg/nodejs/pulumi/esc-sdk/
inject nodejs           nodejs/pulumi           /docs/reference/pkg/nodejs/pulumi/
inject python-policy    python/pulumi_policy    /docs/reference/pkg/python/pulumi_policy/
inject python-esc-sdk   python/pulumi_esc_sdk   /docs/reference/pkg/python/pulumi_esc_sdk/
inject python           python/pulumi           /docs/reference/pkg/python/pulumi/
inject dotnet-esc-sdk   dotnet/esc-sdk          /docs/reference/pkg/dotnet/esc-sdk/
inject dotnet           dotnet                  /docs/reference/pkg/dotnet/
inject java             java                    /docs/reference/pkg/java/

# Some docset liveRoots are bare DocFX/TypeDoc container dirs with no index.html (the site
# links to a deeper entry, so the bare path 404s — and so does the version selector's "View
# latest"). Drop a small redirect landing at those roots, pointing at the real entry, when
# one isn't already present.
redirect_landing() { # dir-under-REF  relative-target
  local dir="$REF/$1" target="$2"
  [[ -d "$dir" ]] || return 0
  [[ -f "$dir/index.html" ]] && return 0
  cat > "$dir/index.html" <<HTML
<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta http-equiv="refresh" content="0; url=$target">
<title>Redirecting…</title></head>
<body>Redirecting to <a href="$target">the API reference</a>.</body></html>
HTML
  echo "inject-live-sdk: redirect landing -> $1"
}
redirect_landing nodejs/pulumi  pulumi/
redirect_landing dotnet/esc-sdk pulumi.esc.sdk/pulumi.esc.sdk.html

echo "inject-live-sdk: done"
