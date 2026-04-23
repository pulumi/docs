#!/bin/bash
# Usage: run_docfx

set -o nounset -o errexit -o pipefail

# Build the .NET projects first so that protobuf-generated types (Pulumirpc) are
# present in the obj/ directories before docfx tries to compile them.
dotnet build ../pulumi-dotnet/sdk/Pulumi/Pulumi.csproj
dotnet build ../pulumi-dotnet/sdk/Pulumi.Automation/Pulumi.Automation.csproj

cd docfx
docfx

# Post-process DocFX output: lowercase all paths for case-insensitive URL serving.
# Requires GNU sed (\L...\E syntax) — available on Ubuntu GitHub Actions runners.
# This script is intended to run only in CI. If you need to run it locally on macOS,
# install GNU sed first: brew install gnu-sed && export PATH="$(brew --prefix)/opt/gnu-sed/libexec/gnubin:$PATH"
if ! sed --version 2>/dev/null | grep -q 'GNU sed'; then
    echo "Error: GNU sed is required for post-processing (.NET SDK docs lowercase step)." >&2
    echo "On macOS: brew install gnu-sed && export PATH=\"\$(brew --prefix)/opt/gnu-sed/libexec/gnubin:\$PATH\"" >&2
    exit 1
fi

DOTNET_OUT="../static-prebuilt/docs/reference/pkg/dotnet"

echo "Post-processing DocFX output: lowercasing filenames and rewriting hrefs..."

# 1. Rename directories to lowercase (bottom-up to avoid path conflicts).
#    If the lowercase target already exists (e.g. DocFX wrote both case
#    variants, or stale committed content overlaps with a fresh build),
#    merge the source into the existing target instead of failing.
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

# 2. Rename files to lowercase. Overwrite is expected here: DocFX writes
#    PascalCase filenames that may already exist in lowercase from a
#    previous commit or build.
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
find "$DOTNET_OUT" -type f -name '*.html' -exec sed -i -E \
    's/href="([^"#:]+)(#[^"]*)?"/href="\L\1\E\2"/g' {} +

# 4. Rewrite xrefmap.yml: lowercase the path portion of href values (before #).
sed -i -E 's/^(  href: )([^#]+)(#.*)?$/\1\L\2\E\3/' "$DOTNET_OUT/xrefmap.yml"

# 5. Rewrite manifest.json: lowercase relative_path values.
sed -i -E 's/"relative_path": "([^"]+)"/"relative_path": "\L\1\E"/g' "$DOTNET_OUT/manifest.json"

echo "Post-processing complete."
