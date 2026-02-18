#!/usr/bin/env bash
# Scrape command metadata from .claude/commands/ and output JSON.
#
# Discovers user-invocable commands:
#   - Top-level .md files  → command name = filename without extension
#   - SKILL.md in subdirs  → command name = parent directory name
#
# Skips: references/, _common/, commands with user-invocable: false

set -euo pipefail

COMMANDS_DIR=".claude/commands"
SKIP_DIRS=("references" "_common")

# Extract a field value from YAML frontmatter (between first pair of --- lines).
# Strips surrounding single or double quotes.
fm_get() {
    local key="$1"
    local file="$2"
    awk -v key="$key" '
        /^---/ { n++; if (n == 2) exit; next }
        n == 1 && $0 ~ "^" key ":" {
            sub("^" key ":[[:space:]]*", "")
            # Strip surrounding quotes
            if ((substr($0,1,1) == "\"" || substr($0,1,1) == "'"'"'") &&
                substr($0,1,1) == substr($0,length($0),1)) {
                $0 = substr($0, 2, length($0)-2)
            }
            print
            exit
        }
    ' "$file"
}

is_skip_dir() {
    local name="$1"
    for skip in "${SKIP_DIRS[@]}"; do
        [[ "$name" == "$skip" ]] && return 0
    done
    return 1
}

is_invocable() {
    local val="$1"
    # Empty means key absent → default true
    [[ -z "$val" || "$val" == "true" || "$val" == "yes" || "$val" == "1" ]]
}

json_output=$(jq -n '[]')

# Top-level .md files
for file in "$COMMANDS_DIR"/*.md; do
    [[ -f "$file" ]] || continue
    entry=$(basename "$file")
    command_name="${entry%.md}"

    invocable=$(fm_get "user-invocable" "$file")
    is_invocable "$invocable" || continue

    description=$(fm_get "description" "$file")
    [[ -n "$description" ]] || continue

    json_output=$(echo "$json_output" | jq \
        --arg cmd "/$command_name" \
        --arg desc "$description" \
        '. += [{"command": $cmd, "description": $desc}]')
done

# Subdirectories with SKILL.md
for dir in "$COMMANDS_DIR"/*/; do
    [[ -d "$dir" ]] || continue
    entry=$(basename "$dir")
    is_skip_dir "$entry" && continue

    skill_file="$dir/SKILL.md"
    [[ -f "$skill_file" ]] || continue

    invocable=$(fm_get "user-invocable" "$skill_file")
    is_invocable "$invocable" || continue

    description=$(fm_get "description" "$skill_file")
    [[ -n "$description" ]] || continue

    json_output=$(echo "$json_output" | jq \
        --arg cmd "/$entry" \
        --arg desc "$description" \
        '. += [{"command": $cmd, "description": $desc}]')
done

echo "$json_output"
