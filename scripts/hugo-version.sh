#!/bin/bash

# Prints the Hugo version this repo builds with, read from mise.toml -- the single
# source of truth for the pin (pulumi/docs#21106). Consumers:
#
#   - .github/actions/setup-hugo (every workflow that installs Hugo)
#   - scripts/ensure.sh          (the `make ensure` version check)
#
# To upgrade Hugo, edit the two hugo lines in mise.toml (Linux takes the bare
# version, the macOS asdf plugin takes it as `extended_<version>`) and the Hugo
# feature in .devcontainer/devcontainer.json, which is plain JSON and can't read
# the pin. `--check` (run by `make lint`) fails if those restatements disagree,
# or if a workflow installs Hugo with its own hard-coded version again.
#
# Fails loudly on a missing or unparseable pin. peaceiris/actions-hugo installs
# the *latest* Hugo when handed an empty version, so an empty answer here must
# never reach it.
#
# Usage: scripts/hugo-version.sh [--check]

set -o errexit -o pipefail

root="$(cd "$(dirname "$0")/.." && pwd)"
mise_toml="$root/mise.toml"

fail() {
    echo "hugo-version: $*" >&2
    exit 1
}

[ -f "$mise_toml" ] || fail "cannot find $mise_toml"

# -n/p so a non-match yields nothing rather than echoing the line back, which is
# what makes the emptiness check below able to fire.
versions="$(sed -nE 's/^hugo[[:space:]]*=.*version[[:space:]]*=[[:space:]]*"([0-9]+\.[0-9]+\.[0-9]+)".*$/\1/p' "$mise_toml")"
[ -n "$versions" ] || fail "no 'hugo = { version = \"X.Y.Z\", ... }' line in $mise_toml"
[ "$(printf '%s\n' "$versions" | wc -l)" -eq 1 ] || fail "more than one hugo pin in $mise_toml: $(echo $versions)"
version="$versions"

if [ "${1:-}" = "--check" ]; then
    problems=()

    mac="$(sed -nE 's/^"asdf:NeoHsu\/asdf-hugo"[[:space:]]*=.*version[[:space:]]*=[[:space:]]*"([^"]*)".*$/\1/p' "$mise_toml")"
    [ "$mac" = "extended_$version" ] ||
        problems+=("mise.toml: macOS asdf-hugo pin is '${mac:-<missing>}', expected 'extended_$version'")

    devcontainer="$root/.devcontainer/devcontainer.json"
    if [ -f "$devcontainer" ]; then
        dc="$(node -e 'const c = require(process.argv[1]); const f = Object.entries(c.features || {}).find(([k]) => k.includes("/features/hugo")); process.stdout.write(f ? String(f[1].version) : "")' "$devcontainer")"
        [ "$dc" = "$version" ] ||
            problems+=(".devcontainer/devcontainer.json: Hugo feature version is '${dc:-<missing>}', expected '$version'")
    fi

    # Workflows install Hugo only through the shared action, which reads the pin.
    while IFS= read -r hit; do
        [ -n "$hit" ] && problems+=("$hit: install Hugo with the setup-hugo action, not a hard-coded version")
    done < <(grep -rnE 'peaceiris/actions-hugo|hugo-version:' "$root/.github/workflows" | sed "s|^$root/||")

    if [ "${#problems[@]}" -gt 0 ]; then
        printf 'hugo-version: %s\n' "${problems[@]}" >&2
        exit 1
    fi
fi

echo "$version"
