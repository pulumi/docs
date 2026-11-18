---
title: Agent Skills
title_tag: Pulumi Agent Skills
h1: Pulumi Agent Skills
meta_desc: Install Pulumi skills in your coding agent, verify that a skill is loaded, and find workflows for infrastructure code and migrations.
menu:
    ai:
        name: Install Pulumi skills
        parent: ai-coding-agents
        weight: 10
aliases:
- /docs/ai/agent-skills/
- /docs/ai/skills/
---

<span id="what-are-agent-skills"></span>

Install Pulumi skills to give your coding agent instructions for writing Pulumi programs, migrating infrastructure, and configuring Pulumi ESC. The agent loads the relevant instructions when you ask it to work on your repository. Pulumi skills follow the [Agent Skills standard](https://agentskills.io).

<span id="how-neo-uses-agent-skills"></span>

## Installation

<span id="claude-code-plugin-system"></span>

### Claude Code

In Claude Code, add the marketplace and install the Pulumi plugin:

```bash
/plugin marketplace add pulumi/agent-skills
/plugin install pulumi                        # Authoring, migration, and handoff skills
```

If you only need migration or delegation, install the corresponding plugin instead of `pulumi`:

```bash
/plugin install pulumi-migration              # Migration skills only
/plugin install pulumi-delegation             # Handoff skill only
```

Provider authors can also install `pulumi-package-maintenance` alongside any of these plugins:

```bash
/plugin install pulumi-package-maintenance
```

### OpenAI Codex

Register the marketplace, then install plugins from the Codex TUI:

```bash
codex plugin marketplace add pulumi/agent-skills
```

Run `codex`, open the plugin marketplace, and select `pulumi` for authoring, migration, and delegation skills. If you only need migration or delegation, select `pulumi-migration` or `pulumi-delegation` instead. Provider authors can also install `pulumi-package-maintenance`.

### Gemini CLI

Install the latest published Pulumi extension, which includes authoring, migration, and delegation skills:

```bash
gemini extensions install https://github.com/pulumi/agent-skills
```

To update the extension:

```bash
gemini extensions update pulumi
```

<span id="universal-installation"></span>

### Other coding agents

Use the `skills` installer to add the groups you need:

```bash
npx skills add pulumi/agent-skills/pulumi --skill '*'       # Pulumi skills
npx skills add pulumi/agent-skills/migration --skill '*'    # Migration skills
npx skills add pulumi/agent-skills/delegation --skill '*'   # Handoff skill
```

Provider authors can also install the separate package-maintenance group:

```bash
npx skills add pulumi/agent-skills/package-maintenance --skill '*'
```

The installer supports Claude Code, Cursor, GitHub Copilot, Codex, Junie, and other coding agents. To install a group for a specific agent, use the `--agent` flag:

```bash
npx skills add pulumi/agent-skills/pulumi --skill '*' --agent junie
```

<span id="usage-examples"></span>

## Use an installed skill

After installation, check that your coding agent lists the Pulumi skills in its available skills or plugin details. If they do not appear, follow your agent's instructions for enabling the plugin or reloading the session.

For example, open a Terraform project and ask:

```text
Use the pulumi-terraform-to-pulumi skill to review this Terraform project
and propose a migration to Pulumi TypeScript. Identify the resources,
state, and dependencies to preserve before making changes.
```

Check the agent's activity for the skill it loaded. How it displays the loaded skill depends on the coding agent.

## Available skills

Skills are organized into four plugin groups: Migration, Pulumi, Package Maintenance, and Delegation.

<span id="terraform-to-pulumi-migration"></span>
<span id="cdk-to-pulumi-migration"></span>

### Migration plugin

Convert and import infrastructure from other tools to Pulumi:

| Skill | Description |
|-------|-------------|
| pulumi-terraform-to-pulumi | Migrate Terraform projects to Pulumi |
| pulumi-cdk-to-pulumi | Migrate AWS CDK applications to Pulumi |
| cloudformation-to-pulumi | Migrate AWS CloudFormation stacks/templates to Pulumi |
| pulumi-arm-to-pulumi | Migrate Azure ARM templates and Bicep to Pulumi |
| pulumi-migrate-from-discovered-stack | Migrate a CloudFormation or ARM stack that Pulumi Cloud's Discovery feature has already found, using the discovered-stacks API |

<span id="general-pulumi-infrastructure"></span>
<span id="managing-secrets-with-esc"></span>
<span id="writing-components"></span>
<span id="upgrading-providers"></span>

### Pulumi plugin

Write Pulumi programs, work with secrets, and diagnose failed operations:

| Skill | Description |
|-------|-------------|
| pulumi-overview | Choose a Pulumi workflow and load the skills needed to complete it |
| pulumi-best-practices | Best practices for writing reliable Pulumi programs |
| pulumi-component | Write reusable infrastructure components with `ComponentResource` |
| pulumi-automation-api | Best practices for using Pulumi Automation API |
| pulumi-esc | Guidance for working with Pulumi ESC (Environments, Secrets, and Configuration) |
| pulumi-debug-failed-operation | Diagnose a failed `pulumi up` or `pulumi preview` using its recorded errors |
| package-usage | Audit which stacks across an organization use a package and at what versions |
| provider-upgrade | Upgrade a Pulumi provider and review the resulting infrastructure changes |

### Package maintenance plugin

These skills help provider authors and bridge maintainers update Pulumi provider repositories:

| Skill | Description |
|-------|-------------|
| pulumi-upgrade-provider | Automate Pulumi provider repo upgrades with the `upgrade-provider` tool |
| upstream-patches | Manage upstream Terraform patch stacks in provider repos |

<span id="handing-off-work-to-pulumi-neo"></span>

### Delegation plugin

Delegate work from your coding agent to Neo in Pulumi Cloud:

| Skill | Description |
|-------|-------------|
| pulumi-neo-handoff | Transfer the current work to a Neo task with its goal, repository details, and conversation summary |

## Contributing

To report a problem, improve a workflow, or add a skill, see the [agent-skills contribution guide](https://github.com/pulumi/agent-skills/blob/main/CONTRIBUTING.md).

<span id="see-also"></span>
