#!/usr/bin/env bash
#
# Sync the canonical PR-triage label set to a target repo.
#
# Reads scripts/labels/labels.json (the declarative state) and:
#   1. Renames legacy labels in-place where the new name is free
#      (preserves PR associations).
#   2. Creates or edits each canonical label so name/color/description match.
#   3. Reports orphaned legacy labels still present after rename.
#      Pass --prune to delete them.
#
# Usage:
#   scripts/labels/sync-labels.sh --repo OWNER/REPO [--dry-run] [--prune]
#
# Examples:
#   scripts/labels/sync-labels.sh --repo CamSoper/pulumi.docs --dry-run
#   scripts/labels/sync-labels.sh --repo pulumi/docs

set -euo pipefail

REPO=""
DRY_RUN=false
PRUNE=false

while [[ $# -gt 0 ]]; do
    case "$1" in
        --repo) REPO="$2"; shift 2 ;;
        --dry-run) DRY_RUN=true; shift ;;
        --prune) PRUNE=true; shift ;;
        -h|--help)
            sed -n '3,18p' "$0" | sed 's/^# \{0,1\}//'
            exit 0 ;;
        *) echo "unknown arg: $1" >&2; exit 2 ;;
    esac
done

if [[ -z "$REPO" ]]; then
    echo "usage: sync-labels.sh --repo OWNER/REPO [--dry-run] [--prune]" >&2
    exit 2
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
LABELS_JSON="$SCRIPT_DIR/labels.json"

[[ -f "$LABELS_JSON" ]] || { echo "missing $LABELS_JSON" >&2; exit 1; }

run() {
    if $DRY_RUN; then
        echo "DRY  $*"
    else
        echo "RUN  $*"
        "$@"
    fi
}

echo "Target repo:      $REPO"
echo "Dry run:          $DRY_RUN"
echo "Prune orphans:    $PRUNE"
echo

EXISTING="$(gh label list --repo "$REPO" --limit 200 --json name,color,description)"

echo "=== Phase 1: rename legacy labels in place where safe ==="
COLLISIONS=()
mapfile -t RENAME_PAIRS < <(jq -r '.renames | to_entries[] | "\(.key)\t\(.value)"' "$LABELS_JSON")
for pair in "${RENAME_PAIRS[@]}"; do
    old="${pair%%$'\t'*}"
    new="${pair##*$'\t'}"
    has_old=$(jq --arg n "$old" 'any(.[]; .name == $n)' <<<"$EXISTING")
    has_new=$(jq --arg n "$new" 'any(.[]; .name == $n)' <<<"$EXISTING")
    if [[ "$has_old" == "true" && "$has_new" == "false" ]]; then
        echo "rename: $old -> $new (preserves PR associations)"
        run gh label edit "$old" --repo "$REPO" --name "$new"
        # Reflect the rename in the in-memory snapshot so Phase 2 sees the
        # new name as already-existing (real run) or as planned (dry run).
        EXISTING=$(jq --arg old "$old" --arg new "$new" \
            '(.[] | select(.name == $old) | .name) |= $new' <<<"$EXISTING")
    elif [[ "$has_old" == "true" && "$has_new" == "true" ]]; then
        echo "skip:   $old exists alongside $new — rename impossible (collision)"
        COLLISIONS+=("$old")
    fi
done

echo
echo "=== Phase 2: create or update each canonical label ==="
mapfile -t CANONICAL < <(jq -c '.labels[]' "$LABELS_JSON")
for label in "${CANONICAL[@]}"; do
    name=$(jq -r '.name' <<<"$label")
    color=$(jq -r '.color' <<<"$label")
    description=$(jq -r '.description' <<<"$label")

    existing_color=$(jq -r --arg n "$name" '.[] | select(.name == $n) | .color // ""' <<<"$EXISTING")
    existing_description=$(jq -r --arg n "$name" '.[] | select(.name == $n) | .description // ""' <<<"$EXISTING")

    if [[ -z "$existing_color" ]]; then
        echo "create: $name"
        run gh label create "$name" --repo "$REPO" --color "$color" --description "$description"
    elif [[ "$existing_color" != "$color" || "$existing_description" != "$description" ]]; then
        echo "update: $name"
        [[ "$existing_color" != "$color" ]] && \
            echo "        color:       $existing_color -> $color"
        [[ "$existing_description" != "$description" ]] && \
            echo "        description: $existing_description"$'\n'"                  -> $description"
        run gh label edit "$name" --repo "$REPO" --color "$color" --description "$description"
    else
        echo "ok:     $name"
    fi
done

echo
echo "=== Phase 3: orphaned legacy labels (collisions only) ==="
if [[ ${#COLLISIONS[@]} -eq 0 ]]; then
    echo "(none)"
else
    for orphan in "${COLLISIONS[@]}"; do
        if $PRUNE; then
            echo "delete: $orphan"
            run gh label delete "$orphan" --repo "$REPO" --yes
        else
            echo "orphan: $orphan (re-run with --prune to delete; PRs tagged with this label will lose it)"
        fi
    done
fi

echo
echo "Done."
