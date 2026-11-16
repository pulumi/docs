#!/usr/bin/env bash
# Fetches Pulumi Cloud's RBAC scopes, built-in roles, and built-in permission
# sets from the REST API and writes data/rbac_scopes.json, the single source of
# truth for the RBAC scope reference
# (content/docs/administration/reference/rbac-scopes/) and the default
# permission set tables on
# content/docs/administration/concepts/rbac/permission-sets.md.
#
# scripts/build-rbac-scopes.py does the transformation; its docstring says what
# it computes. Section layout lives in data/rbac_scope_sections.yaml and
# hand-written notes in data/rbac_scope_notes.yaml.
#
# Unlike the audit log event catalog, the scope list depends on the org: a
# scope behind a feature flag is returned only to orgs that have the flag. Run
# this against an org with every customer-visible feature enabled, or flagged
# scopes will drop off the reference. PULUMI_ORG picks the org.
#
# These endpoints require authentication, so this script is NOT part of
# `make ensure`. The .github/workflows/update-rbac-scopes.yml GitHub Action
# runs it nightly and opens a PR when the data changes. Run it locally only for
# testing, with PULUMI_ACCESS_TOKEN set.
#
# Needs PyYAML. The workflow installs it; locally, either `pip install pyyaml`
# or point PYTHON at an interpreter that already has it.

set -euo pipefail

API="${PULUMI_API:-https://api.pulumi.com}"
ORG="${PULUMI_ORG:-pulumi}"
PYTHON="${PYTHON:-python3}"

if [[ -z "${PULUMI_ACCESS_TOKEN:-}" ]]; then
  echo "error: PULUMI_ACCESS_TOKEN is not set. This script calls authenticated" >&2
  echo "       Pulumi Cloud endpoints and cannot run without a token." >&2
  exit 1
fi

if ! "$PYTHON" -c "import yaml" 2>/dev/null; then
  echo "error: PyYAML is not available to '${PYTHON}'. Install it with" >&2
  echo "       '${PYTHON} -m pip install pyyaml', or set PYTHON to an" >&2
  echo "       interpreter that has it." >&2
  exit 1
fi

WORKDIR="$(mktemp -d)"
trap 'rm -rf "$WORKDIR"' EXIT

fetch() {
  curl -sfL --retry 3 --retry-all-errors --connect-timeout 10 --max-time 60 \
    -H "Authorization: token ${PULUMI_ACCESS_TOKEN}" \
    "${API}/api/orgs/${ORG}/$1" -o "$WORKDIR/$2"
}

echo "Fetching RBAC scopes, roles, and permission sets from ${API} (org: ${ORG})..."
fetch "roles/scopes" scopes.json
fetch "roles?uxPurpose=role" roles.json
fetch "roles?uxPurpose=set" sets.json

"$PYTHON" scripts/build-rbac-scopes.py \
  "$WORKDIR/scopes.json" "$WORKDIR/roles.json" "$WORKDIR/sets.json" \
  data/rbac_scope_sections.yaml data/rbac_scopes.json
