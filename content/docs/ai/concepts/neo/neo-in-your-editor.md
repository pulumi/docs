---
title: Use Neo in your editor
title_tag: Use Neo in your editor | Pulumi Agents
h1: Use Neo in your editor
meta_desc: Use Neo inside Zed, JetBrains IDEs, VS Code, and Cursor through the Agent Client Protocol (ACP).
menu:
    ai:
        name: Use your editor
        identifier: ai-editors
        parent: ai-agents-tasks
        weight: 40
aliases:
- /docs/ai/neo/editors/
---

Use Neo from your editor's agent panel to work on your local project.

Editors connect to Neo through the [Agent Client Protocol (ACP)](https://agentclientprotocol.com). Zed and JetBrains IDEs support ACP natively; VS Code and Cursor support it through an extension.

<span id="how-permissions-work"></span>

Like a [CLI session](/docs/ai/concepts/neo/neo-in-the-cli/), an editor session can read and change your local files. It uses your `pulumi login` account for Pulumi Cloud and your local CLI logins, environment variables, and Kubernetes configuration for other systems.

## Prerequisites

1. Install [Pulumi CLI](/docs/install/) v3.254.0 or later.
1. Authenticate to Pulumi Cloud with `pulumi login`.

## Zed

Zed supports ACP agents natively. Navigate to **Settings** > **AI** > **External Agents** > **Configure**, then select **Add Agent** > **Add Custom Agent** and fill in:

- **Name**: `Pulumi Neo`
- **Command**: `pulumi`
- **Arguments**: `neo acp`

Open the Agent Panel, start a new thread, and select **Pulumi Neo** as the agent.

## JetBrains IDEs

JetBrains AI Assistant 2026.2 or later supports ACP agents in JetBrains IDEs. Open the **AI Chat** tool window, open the chat menu, and select **Add Custom Agent**. The IDE opens `~/.jetbrains/acp.json` for editing; add Neo under `agent_servers`:

```json
{
    "agent_servers": {
        "Pulumi Neo": {
            "command": "pulumi",
            "args": ["neo", "acp"]
        }
    }
}
```

If the IDE doesn't inherit your shell's `PATH`, use the full path to the `pulumi` binary in `command`. Restart the IDE after editing the file, then select **Pulumi Neo** from the agent selector in AI Chat.

## VS Code and Cursor

VS Code doesn't support ACP natively, so install the open source [ACP Client](https://marketplace.visualstudio.com/items?itemName=formulahendry.acp-client) extension. In Cursor (and other VS Code-compatible editors), install the same extension from the [Open VSX registry](https://open-vsx.org/extension/formulahendry/acp-client).

Add Neo as a custom agent in your `settings.json`:

```json
{
    "acp.agents": {
        "Pulumi Neo": {
            "command": "pulumi",
            "args": ["neo", "acp"]
        }
    }
}
```

Open the **ACP Client** panel from the Activity Bar and select **Pulumi Neo** to start a session.

## Controls

Your editor exposes these session options:

- **[Permission modes](/docs/ai/agents/permissions/#permission-mode-and-approval-mode)** (`default`, `read-only`) control whether the session can write to Pulumi Cloud. They do not restrict local file changes or the credentials used by local commands.
- **[Plan mode](/docs/ai/agents/tasks/#plan-mode)** lets the agent propose a plan for you to review before changing files.

Review and respond to tool approval requests in the editor's agent panel.
