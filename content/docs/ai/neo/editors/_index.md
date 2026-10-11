---
title: Neo in Your Editor (ACP)
title_tag: Neo in Your Editor (ACP)
h1: Neo in Your Editor (ACP)
meta_desc: Use Pulumi Neo directly inside Zed, JetBrains IDEs, VS Code, and Cursor through the Agent Client Protocol (ACP).
menu:
    ai:
        name: Neo in your editor (ACP)
        identifier: ai-editors
        parent: ai-neo
        weight: 16
---

Neo can run directly inside your editor's agent panel. You chat with Neo, review its plans, and watch its edits in the same window as your code, with no separate terminal session or browser tab.

Editors connect to Neo through the [Agent Client Protocol (ACP)](https://agentclientprotocol.com), the same open standard they use to host agents like Claude Code and Gemini CLI. Zed and JetBrains IDEs support ACP natively; VS Code and Cursor support it through an extension.

Like [Neo in the CLI](/docs/ai/neo/pulumi-cli/), an editor session runs locally and inherits your setup: your `pulumi login`, the CLIs you've authenticated, your environment variables and kubeconfigs, and the project you have open. Neo edits your local files directly, so its changes show up in your working tree as it makes them.

## Prerequisites

1. [Pulumi CLI](/docs/install/) v3.254.0 or later
1. Authenticate to Pulumi Cloud with `pulumi login`

## Zed

Zed supports ACP agents natively. Navigate to **Settings** > **AI** > **External Agents** > **Configure**, then select **Add Agent** > **Add Custom Agent** and fill in:

- **Name**: `Pulumi Neo`
- **Command**: `pulumi`
- **Arguments**: `neo acp`

Open the Agent Panel, start a new thread, and select **Pulumi Neo** as the agent.

## JetBrains IDEs

JetBrains IDEs (IntelliJ IDEA, GoLand, PyCharm, WebStorm, and the rest of the lineup) support ACP agents through JetBrains AI Assistant 2026.2 or later. Open the **AI Chat** tool window, open the chat menu, and select **Add Custom Agent**. The IDE opens `~/.jetbrains/acp.json` for editing; add Neo under `agent_servers`:

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

The controls you have elsewhere apply in your editor, exposed as session options in the agent UI:

- **[Permission modes](/docs/ai/neo/permissions/#permission-mode-and-approval-mode)** (default, read-only) govern what Neo can change
- **[Plan mode](/docs/ai/neo/tasks/#plan-mode)** lets Neo research and agree on a plan with you before executing

Tool call approvals surface in the editor's agent panel, so you review Neo's actions the same way you review those of any other agent you run there.

## How permissions work

An editor session uses your existing `pulumi login` and the [RBAC permissions](/docs/administration/concepts/rbac/) of your Pulumi user. Identity, RBAC, and audit all run through your Pulumi Cloud login, the same way they do in the console.
