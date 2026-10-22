---
title: Concepts
title_tag: Infrastructure AI concepts
h1: Concepts
meta_desc: How AI agents work with Pulumi, including Agent Skills, the Pulumi CLI for agents, and Pulumi Neo's tasks, permissions, automations, and settings.
menu:
    ai:
        name: Concepts
        parent: ai-home
        identifier: ai-concepts
        weight: 10
---

These pages explain how AI agents work with Pulumi. To set something up, see [Guides](/docs/ai/guides/). To try it end to end, start with [Get started](/docs/ai/get-started/).

## Agents and Pulumi

- [Agent Skills](/docs/ai/concepts/agent-skills/): Packaged Pulumi workflows that teach coding agents how to work with Pulumi.
- [CLI for agents](/docs/ai/concepts/cli-for-agents/): How the Pulumi CLI is built for agents, from `npx pulumi` to structured `--json` output.

## Pulumi Neo

- [Pulumi Neo](/docs/ai/concepts/neo/): What Neo does, where you can use it, and how much autonomy you give it.
  - [Tasks](/docs/ai/concepts/neo/tasks/): The unit of work in Neo, including Plan Mode, task modes, and approvals.
  - [Permissions model](/docs/ai/concepts/neo/permissions/): Which identity Neo acts as on each surface, and how permission and approval modes constrain it.
  - [Automations](/docs/ai/concepts/neo/automations/): Scheduled Neo tasks that deliver their results as pull requests.
  - [Neo in the CLI](/docs/ai/concepts/neo/neo-in-the-cli/): Interactive Neo sessions in your terminal with your local project and credentials.
  - [Neo in your editor](/docs/ai/concepts/neo/neo-in-your-editor/): Neo inside Zed, JetBrains IDEs, VS Code, and Cursor through the Agent Client Protocol.
  - [Pull requests](/docs/ai/concepts/neo/pull-requests/): How Neo opens and updates pull requests through your existing review process.
  - [Code reviews](/docs/ai/concepts/neo/code-reviews/): How Neo reviews pull requests against what Pulumi Cloud knows about your infrastructure.
  - [Previews](/docs/ai/concepts/neo/previews/): How Neo runs `pulumi preview` to validate changes before opening a pull request.
  - [Instructions](/docs/ai/concepts/neo/instructions/): Organization-wide custom instructions and per-repository `AGENTS.md` instructions.
  - [Slash commands](/docs/ai/concepts/neo/slash-commands/): Built-in and custom shortcuts for proven prompts.
  - [Model providers](/docs/ai/concepts/neo/model-providers/): Running Neo with your own model provider credentials.
  - [Settings](/docs/ai/concepts/neo/settings/): Access controls, the default task mode, and notifications.
  - [Usage limits](/docs/ai/concepts/neo/usage-limits/): Spend limits for your organization and its members.
