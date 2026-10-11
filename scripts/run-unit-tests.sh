#!/bin/bash

# Unit tests that need no network and no Hugo build.
#
# This previously ran `yarn --cwd components test`, against a `components/` directory that
# no longer exists — the script had been broken and unreferenced for some time, which is
# why nothing noticed. It is now wired into `make test` (see the Makefile).

set -o errexit -o pipefail

# Node's built-in runner, so scripts/ tests need no new dependency.
node --test scripts/*.test.js
