---
title: Use Neo in the CLI
title_tag: Use Neo in the CLI | Pulumi Agents
h1: Use Neo in the CLI
meta_desc: Run pulumi neo to start a Neo session in your terminal with access to your local project, credentials, and stacks.
aliases:
- /docs/ai/pulumi-cli/
- /docs/ai/neo/pulumi-cli/
menu:
    ai:
        name: Use the CLI
        identifier: ai-pulumi-cli
        parent: ai-agents-tasks
        weight: 30
---

Run `pulumi neo` to work with Neo from the terminal in your local project. You can also [use your editor's agent panel](/docs/ai/concepts/neo/neo-in-your-editor/).

## Work in your local environment {#what-local-execution-unlocks}

<span id="how-permissions-work"></span>

The agent can read and change local files and run installed CLIs. It uses your `pulumi login` account for Pulumi Cloud and credentials from your environment variables, CLI logins, and Kubernetes configuration for other systems. Sign in to the tools the task needs before starting a session. See [Permissions and approvals](/docs/ai/agents/permissions/) for access and approval controls.

## Get started

1. Authenticate to Pulumi Cloud with `pulumi login`.
1. Run `pulumi neo` from a directory containing a `Pulumi.yaml` file.
1. Describe the change you want or the problem to solve. Include the stack name and any relevant error output.

See the [`pulumi neo` command reference](/docs/iac/cli/commands/pulumi_neo/) for the full list of flags and options.

## Controls

Choose approval, permission, and plan settings for the session:

- **[Approval modes](/docs/ai/agents/permissions/#separate-approvals-from-access)** (manual, balanced, auto) control when the session pauses for confirmation. `manual` is the same mode the console calls **Review**.
- **[Permission modes](/docs/ai/agents/permissions/#permission-mode-and-approval-mode)** (`default`, `read-only`) control whether the session can write to Pulumi Cloud. They do not restrict local file changes or the credentials used by local commands.
- **[Plan mode](/docs/ai/agents/tasks/#plan-mode)** lets the agent propose a plan before changing files (toggle with **Shift+Tab** before sending your first message).

<span id="integrations"></span>

For connections configured in Pulumi Cloud, see [Integrations](/docs/ai/agents/integrations/).

## Agent handoff

Install the [delegation skill](/docs/ai/concepts/agent-skills/#delegation-plugin) in your coding agent to transfer work to a Neo task. When you explicitly request a handoff, the skill summarizes the goal, repository state, and conversation, then passes that summary to `pulumi neo`.

The handoff session can read your local working tree, including uncommitted changes. You do not need to commit or push them for the handoff.

The skill returns a task URL and instructs the original coding agent to stop. Continue the work in that task. This is a one-way transfer; the original coding agent does not wait for a result and resume automatically.
