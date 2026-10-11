---
user-invocable: false
description: Slack MCP plugin setup instructions and troubleshooting
---

# Slack Plugin Setup

The `/slack-to-issue` skill requires the Slack MCP plugin to fetch message content. Display this when ToolSearch finds no Slack tools.

---

## Plugin Not Found

Display this message verbatim:

```
❌ Slack plugin not available

The /slack-to-issue skill requires the Slack plugin for Claude Code.

To install it:

1. Run /plugin to open the plugin manager.

2. Go to the Discover tab (press Tab to cycle between tabs).

3. Find the "slack" plugin and press Enter to install it.

   Or install directly from the command line:
   /plugin install slack@claude-plugins-official

4. Restart this session and try again.

Full documentation: https://code.claude.com/docs/en/discover-plugins

Alternatively, paste the Slack message text directly and skip to issue creation:
  /slack-to-issue (then paste the message when prompted)
```

---

## Token Setup

If the user has the plugin installed but authentication fails:

```
❌ Slack authentication failed

Verify your Slack token configuration:

1. Check that your token starts with xoxb- (bot token) or xoxp- (user token)
2. Ensure the token has the required scopes (channels:history, channels:read, etc.)
3. Confirm the token is for the correct Slack workspace
4. Refresh the token if it has expired

To update your token:
  /plugin → Installed tab → select Slack → reconfigure
```

---

## Access Errors

If authentication succeeds but message fetching fails:

| Error | Likely cause | Resolution |
|---|---|---|
| `channel_not_found` | Bot not invited to private channel | Add the Slack app to the channel: `/invite @app-name` |
| `missing_scope` | Token lacks required scope | Regenerate token with `channels:history` and `groups:history` |
| `message_not_found` | Message too old or deleted | Paste the message text manually |
| `not_in_channel` | Bot not a member | Same as `channel_not_found` |

When access errors occur, offer this fallback:

```
The message can't be fetched automatically.

Would you like to paste the Slack message text manually?
(Copy the message content from Slack and share it here — no URL needed)
```

Accept pasted text and continue the skill from Step 3.

---

## Workspace Configuration

The Slack plugin may be configured for a specific workspace. If the URL is from a different workspace than configured:

```
⚠️ Workspace mismatch

The URL is from workspace: [extracted workspace from URL]
Plugin is configured for: [configured workspace]

Options:
- Update the plugin configuration to use the correct workspace
- Paste the message text manually to continue
```
