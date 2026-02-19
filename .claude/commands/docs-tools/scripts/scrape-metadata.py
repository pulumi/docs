#!/usr/bin/env python3
# Scrape command metadata from .claude/commands/ and output JSON.
#
# Discovers user-invocable commands:
#   - Top-level .md files  → command name = filename without extension
#   - SKILL.md in subdirs  → command name = parent directory name
#
# Skips: references/, _common/, commands with user-invocable: false

import json
import os
import re
import sys

COMMANDS_DIR = ".claude/commands"
SKIP_DIRS = {"references", "_common"}


def get_frontmatter_field(key, path):
    """Extract a field value from YAML frontmatter (between first pair of --- lines)."""
    try:
        with open(path, encoding="utf-8") as f:
            content = f.read()
    except OSError:
        return ""

    # Find frontmatter block
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not match:
        return ""

    fm = match.group(1)
    for line in fm.splitlines():
        m = re.match(rf"^{re.escape(key)}:\s*(.*)", line)
        if m:
            value = m.group(1).strip()
            # Strip surrounding quotes
            if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
                value = value[1:-1]
            return value
    return ""


def is_invocable(val):
    """Empty (key absent) defaults to true."""
    return val in ("", "true", "yes", "1")


results = []

# Top-level .md files
for entry in sorted(os.listdir(COMMANDS_DIR)):
    if not entry.endswith(".md"):
        continue
    path = os.path.join(COMMANDS_DIR, entry)
    if not os.path.isfile(path):
        continue

    command_name = entry[:-3]  # strip .md
    invocable = get_frontmatter_field("user-invocable", path)
    if not is_invocable(invocable):
        continue

    description = get_frontmatter_field("description", path)
    if not description:
        continue

    results.append({"command": f"/{command_name}", "description": description})

# Subdirectories with SKILL.md
for entry in sorted(os.listdir(COMMANDS_DIR)):
    dir_path = os.path.join(COMMANDS_DIR, entry)
    if not os.path.isdir(dir_path):
        continue
    if entry in SKIP_DIRS:
        continue

    skill_file = os.path.join(dir_path, "SKILL.md")
    if not os.path.isfile(skill_file):
        continue

    invocable = get_frontmatter_field("user-invocable", skill_file)
    if not is_invocable(invocable):
        continue

    description = get_frontmatter_field("description", skill_file)
    if not description:
        continue

    results.append({"command": f"/{entry}", "description": description})

print(json.dumps(results, indent=2))
