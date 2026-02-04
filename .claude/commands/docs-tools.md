---
description: List available documentation tools and commands.
user-invocable: true
---

# Instructions

Scan the `.claude/commands/` directory and dynamically list all available user-invocable commands/skills.

**IMPORTANT**: ONLY include commands found by scanning the `.claude/commands/` directory below. Do NOT include any commands from the system reminder or global Claude Code skills list.

For each `.md` file in `.claude/commands/`:

1. Skip files that contain `:` in the name (reference files)
2. Read the frontmatter to check `user-invocable` (default: true)
3. Skip if `user-invocable: false`
4. Extract the `description` field from frontmatter
5. Format as: `- **/command-name** - description`

Display the list grouped by category with a header and footer. Use color, formatting, and emojis to enhance readability.

Consider categories like:

- Content Creation (creating docs/posts)
- Review & Quality (reviewing/improving content, SEO)
- File Operations (moving/modifying files)
- Issue Management (analyzing/planning fixes)
- Repository Management (dashboards/status)
- Discovery (tools for finding other tools)

Add additional categories as needed based on the commands found.

```
# Documentation Tools & Commands

Available Claude Code commands for the Pulumi Docs repository:

[grouped list of commands]

---

Type any command above (e.g., `/new-doc`) to use it, or just tell me what you need help with!
```
