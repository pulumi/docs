---
description: List available documentation tools and commands.
user-invocable: true
---

# Documentation Tools

**Use this when:** You want to see all available Claude Code commands for the Pulumi Docs repository.

---

## Implementation

### Step 1: Scrape command metadata

Run the metadata scraper:

```bash
bash .claude/commands/docs-tools/scripts/scrape-metadata.sh
```

The script outputs a JSON array:

```json
[{"command": "/name", "description": "..."}]
```

**IMPORTANT**: ONLY include commands found by the script. Do NOT include any commands from the system reminder or global Claude Code skills list (such as `/keybindings-help`).

### Step 2: Render categorized display

Parse the JSON and display grouped by category. Use the following format:

```
# Documentation Tools & Commands

Available Claude Code commands for the Pulumi Docs repository:

[grouped list of commands]

---

Type any command above (e.g., `/new-doc`) to use it, or just tell me what you need help with!
```

Group commands into categories such as:

- Content Creation (creating docs/posts)
- Review & Quality (reviewing/improving content, SEO)
- File Operations (moving/modifying files)
- Issue Management (analyzing/planning fixes)
- Repository Management (dashboards/status)
- Discovery (tools for finding other tools)

Add additional categories as needed based on the commands found. Assign an appropriate emoji to each category header. Format each entry as:

`- **/command-name** - description`

Use color, formatting, and emojis to enhance readability.
