#!/bin/bash
# Usage: run_docfx
#
# Configurable via environment variables (defaults preserve the IaC .NET build):
#   DOCFX_CONFIG          docfx config file name inside docfx/ (default: docfx.json)
#   DOCFX_BUILD_PROJECTS  space-separated csproj paths to `dotnet build` first
#   DOCFX_OUT             post-processing target dir (default: the IaC dotnet output)
#   DOCFX_SDK_VERSION     optional SDK version string to surface on generated pages

set -o nounset -o errexit -o pipefail

DOCFX_CONFIG="${DOCFX_CONFIG:-docfx.json}"
DOCFX_BUILD_PROJECTS="${DOCFX_BUILD_PROJECTS:-../pulumi-dotnet/sdk/Pulumi/Pulumi.csproj ../pulumi-dotnet/sdk/Pulumi.Automation/Pulumi.Automation.csproj}"
DOCFX_OUT="${DOCFX_OUT:-../static-prebuilt/docs/reference/pkg/dotnet}"
DOCFX_SDK_VERSION="${DOCFX_SDK_VERSION:-}"

# --- Diagnostics ---------------------------------------------------------
# Print a banner before each stage so CI logs make it obvious which step
# failed when something goes wrong. Show the failing line + command on
# any error, since several tools in this pipeline (notably docfx) can
# exit with non-zero codes and minimal stderr output.

step() {
    echo
    echo "==> [run_docfx] $*"
}

on_error() {
    local exit_code=$?
    local line=$1
    echo >&2
    echo "ERROR: run_docfx.sh failed at line ${line} (exit code ${exit_code})" >&2
    echo "       last command: ${BASH_COMMAND}" >&2
    echo "       pwd:          $(pwd)" >&2
    exit "${exit_code}"
}
trap 'on_error ${LINENO}' ERR

step "Configuration"
echo "  DOCFX_CONFIG=${DOCFX_CONFIG}"
echo "  DOCFX_BUILD_PROJECTS=${DOCFX_BUILD_PROJECTS}"
echo "  DOCFX_OUT=${DOCFX_OUT}"
echo "  DOCFX_SDK_VERSION=${DOCFX_SDK_VERSION:-<unset>}"
echo "  pwd=$(pwd)"

step "Tool versions"
echo "  dotnet:   $(dotnet --version 2>&1 || echo MISSING)"
echo "  docfx:    $(docfx --version 2>&1 | head -1 || echo MISSING)"
echo "  jq:       $(jq --version 2>&1 || echo MISSING)"
echo "  sed:      $(sed --version 2>&1 | head -1 || echo MISSING)"

# Fail fast with a clear message if anything required is missing or
# misconfigured, rather than letting a downstream tool crash silently.
step "Preflight checks"
for tool in dotnet docfx jq sed find; do
    if ! command -v "$tool" >/dev/null 2>&1; then
        echo "ERROR: required tool '$tool' not found on PATH" >&2
        exit 1
    fi
done
if ! sed --version 2>/dev/null | grep -q 'GNU sed'; then
    echo "ERROR: GNU sed is required for post-processing (.NET SDK docs lowercase step)." >&2
    echo "  On macOS: brew install gnu-sed && export PATH=\"\$(brew --prefix)/opt/gnu-sed/libexec/gnubin:\$PATH\"" >&2
    exit 1
fi
if [ ! -f "docfx/${DOCFX_CONFIG}" ]; then
    echo "ERROR: docfx config not found: docfx/${DOCFX_CONFIG}" >&2
    exit 1
fi
for proj in $DOCFX_BUILD_PROJECTS; do
    if [ ! -f "$proj" ]; then
        echo "ERROR: project file not found: $proj (cwd: $(pwd))" >&2
        exit 1
    fi
done
echo "  ok"

# --- Build .NET projects -------------------------------------------------
# Build first so protobuf-generated types (Pulumirpc) are in the obj/
# directories before docfx tries to compile them.
for proj in $DOCFX_BUILD_PROJECTS; do
    step "dotnet build $proj"
    dotnet build "$proj"
done

# --- Run docfx -----------------------------------------------------------
cd docfx
if [ -n "$DOCFX_SDK_VERSION" ]; then
    # Surface the SDK version on generated pages by injecting _appVersion into
    # the config's build.globalMetadata. We modify the config in place rather
    # than passing --globalMetadataFiles on the CLI: docfx 2.78.x ignores that
    # flag when invoked as `docfx <config>` (no explicit `build` subcommand)
    # and exits 255 without output.
    step "Injecting _appVersion=${DOCFX_SDK_VERSION} into ${DOCFX_CONFIG}"
    jq --arg v "$DOCFX_SDK_VERSION" \
        '.build.globalMetadata._appVersion = $v' \
        "$DOCFX_CONFIG" > "$DOCFX_CONFIG.tmp"
    mv "$DOCFX_CONFIG.tmp" "$DOCFX_CONFIG"
    echo "  build.globalMetadata is now:"
    jq '.build.globalMetadata' "$DOCFX_CONFIG" | sed 's/^/  /'
fi
step "docfx ${DOCFX_CONFIG}"
docfx "$DOCFX_CONFIG"

# --- Post-process docfx output ------------------------------------------
# Lowercase all paths for case-insensitive URL serving. Requires GNU sed
# (\L...\E syntax) — already checked above.

DOTNET_OUT="$DOCFX_OUT"
step "Post-processing docfx output in ${DOTNET_OUT}"

if [ ! -d "$DOTNET_OUT" ]; then
    echo "ERROR: docfx output directory not found: $DOTNET_OUT" >&2
    echo "       (docfx may have failed silently to produce output)" >&2
    exit 1
fi

# 1. Rename directories to lowercase (bottom-up to avoid path conflicts).
#    If the lowercase target already exists (e.g. docfx wrote both case
#    variants, or stale committed content overlaps with a fresh build),
#    merge the source into the existing target instead of failing.
echo "  [1/5] lowercasing directory names"
find "$DOTNET_OUT" -depth -type d -name '*[A-Z]*' | while read -r dir; do
    parent="$(dirname "$dir")"
    base="$(basename "$dir")"
    lower="$(echo "$base" | tr '[:upper:]' '[:lower:]')"
    if [ "$base" = "$lower" ]; then
        continue
    fi
    target="$parent/$lower"
    if [ -e "$target" ]; then
        cp -a "$dir"/. "$target"/
        rm -rf "$dir"
    else
        mv "$dir" "$target"
    fi
done

# 2. Rename files to lowercase. Overwrite is expected here: docfx writes
#    PascalCase filenames that may already exist in lowercase from a
#    previous commit or build.
echo "  [2/5] lowercasing file names"
find "$DOTNET_OUT" -type f -name '*[A-Z]*' | while read -r file; do
    parent="$(dirname "$file")"
    base="$(basename "$file")"
    lower="$(echo "$base" | tr '[:upper:]' '[:lower:]')"
    if [ "$base" != "$lower" ]; then
        mv "$file" "$parent/$lower"
    fi
done

# 3. Rewrite href attributes in HTML files to lowercase the path portion
#    but NOT the fragment (after #). Fragment anchors must stay PascalCase
#    because they must match id= attributes in the HTML.
echo "  [3/5] lowercasing href paths in HTML"
find "$DOTNET_OUT" -type f -name '*.html' -exec sed -i -E \
    's/href="([^"#:]+)(#[^"]*)?"/href="\L\1\E\2"/g' {} +

# 4. Rewrite xrefmap.yml: lowercase the path portion of href values (before #).
echo "  [4/5] lowercasing xrefmap.yml hrefs"
sed -i -E 's/^(  href: )([^#]+)(#.*)?$/\1\L\2\E\3/' "$DOTNET_OUT/xrefmap.yml"

# 5. Rewrite manifest.json: lowercase relative_path values.
echo "  [5/5] lowercasing manifest.json relative_path"
sed -i -E 's/"relative_path": "([^"]+)"/"relative_path": "\L\1\E"/g' "$DOTNET_OUT/manifest.json"

step "Done"
