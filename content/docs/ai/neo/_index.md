---
title: Pulumi Neo
title_tag: Pulumi Neo | Pulumi Agents
h1: Pulumi Neo
meta_desc: Neo is the pre-built personal agent in Pulumi Agents. Investigate infrastructure and make changes from Pulumi Cloud, your terminal, or your editor.
aliases:
- /docs/pulumi-cloud/neo/
- /docs/iac/neo/
- /docs/neo/
menu:
    ai:
        name: Neo
        parent: ai-guides
        identifier: ai-neo
        weight: 20
---

Neo is the pre-built personal agent in Pulumi Agents. Use it to investigate infrastructure, preview changes, and update your Pulumi code with your own Pulumi Cloud permissions. Work in Pulumi Cloud, your terminal, or your editor.

These guides cover Neo's tasks, controls, and supported interfaces. To set up an agent with saved instructions and its own role, see [Create and manage agents](/docs/ai/agents/create-and-manage/).

## What Neo does

- **Answers questions about your infrastructure.** Ask which resources are
  running an outdated provider, why a stack failed, or what a change will do,
  and Neo searches your real state to answer. [Tasks](/docs/ai/neo/tasks/)
  covers how it investigates.
- **Proposes changes to your code.** When a task calls for changing
  infrastructure, Neo changes the IaC code rather than clicking in a console.
  The usual way it hands that back is a
  [pull request](/docs/ai/neo/pull-requests/) describing the problem, the
  resources affected, and a preview summary, so your branch protection rules
  and reviewers still gate what ships.
- **Runs previews before anything lands.** Neo can
  [run `pulumi preview`](/docs/ai/neo/running-previews/) to validate a change,
  surface policy violations, and show the resource diff.
- **Reviews your pull requests.** Neo
  [comments on PRs](/docs/ai/neo/code-reviews/) using what Pulumi Cloud knows
  about your running infrastructure, flagging issues inline. It never blocks
  the merge.
- **Takes on recurring maintenance.** Turn any task into
  [an automation](/docs/ai/neo/automations/) that runs on a schedule: provider
  freshness checks, encryption and backup audits, activity digests. Some
  automations report what they found; others open a pull request when there's
  work to do.
- **Applies Pulumi best practices.** Neo ships with the
  [Pulumi Agent Skills](/docs/ai/skills/) catalog built in, so it already knows
  proven workflows for components, ESC, migrations, and provider upgrades.

## Where to use Neo

Neo is one agent reachable from several places. Your permissions, approval
controls, and integrations carry over whichever surface you start from.

- **Pulumi Cloud console.** The Neo section in Pulumi Cloud is the main home for
  tasks, automations, and settings. [Get started](/docs/ai/neo/get-started/).
- **Your terminal.** Run [`pulumi neo`](/docs/ai/neo/pulumi-cli/) for an
  interactive session that inherits your local setup: the CLIs you've
  authenticated, your environment variables and kubeconfigs, and the project
  you're editing.
- **Your editor.** Use [Neo in your editor's agent panel](/docs/ai/neo/editors/)
  in Zed, JetBrains IDEs, VS Code, and Cursor through the Agent Client
  Protocol, working on the project you have open.
- **Slack.** Mention [`@Neo`](/docs/ai/neo/integrations/slack/) in any channel
  and it replies in the thread, so you can check stack state or investigate a
  failure without leaving the conversation.
- **Pull requests.** Neo reviews PRs automatically, and you can mention
  `@pulumi-neo` in a PR description, a review comment, or an issue to ask for
  something specific. See [code reviews](/docs/ai/neo/code-reviews/).
- **From another AI agent.** Claude Code, Codex, Cursor, and other agents can
  hand long-running infrastructure work to Neo through the
  [Pulumi MCP server](/docs/ai/mcp-server/) or the
  [Neo handoff skill](/docs/ai/skills/), then keep working while Neo runs.

Neo also reaches outward: [integrations](/docs/ai/neo/integrations/mcp/) connect
it to services like Datadog, PagerDuty, Linear, and Atlassian so it can pull in
the context a task needs.

## How much autonomy you give it

[Plan Mode](/docs/ai/neo/tasks/#plan-mode) makes Neo agree on a plan with you
before it acts, [task modes](/docs/ai/neo/tasks/#task-modes) control which steps
need your approval, and
[read-only mode](/docs/ai/neo/get-started/#read-only-mode) restricts Pulumi Cloud writes. Credentials for connected tools govern access to those tools separately; see [Neo permissions](/docs/ai/neo/permissions/).
