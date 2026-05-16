#!/bin/bash
# Source this file (don't execute it) at the top of any script that needs
# pinned build tools (Node, Yarn, Go, Vale). If mise is installed locally,
# it prepends mise's tool bin paths to PATH so subsequent `node`, `yarn`,
# etc. calls resolve to the versions pinned in mise.toml. If mise isn't
# installed (the default in CI), this is a no-op — tools resolve from
# system PATH as they did before.

if command -v mise &> /dev/null; then
    _mise_bin_paths="$(mise bin-paths 2>/dev/null || true)"
    if [ -n "$_mise_bin_paths" ]; then
        export PATH="$(echo "$_mise_bin_paths" | tr '\n' ':')${PATH}"
    fi
    unset _mise_bin_paths
fi
