---
title: Create and configure an agent
title_tag: Create and configure an agent | Pulumi Agents
h1: Create and configure an agent
pulumi_cloud_feature: pulumi-agents
meta_desc: Start with a pre-built agent or build your own, connect the tools it needs, and configure its instructions and access.
menu:
    ai:
        name: Configure a pre-built agent
        parent: ai-agents-create-manage
        identifier: ai-agents-configure
        weight: 20
---

Choose a pre-built agent, tailor its instructions, and give it access to the tools it needs. Then assign a task to check that it can do the work. To define a new responsibility from scratch, [build a custom agent](/docs/ai/agents/custom/).

## Before you begin

You need permission to create agents in your Pulumi Cloud organization. If the agent will read code or prepare pull requests, [connect your version control provider](/docs/integrations/version-control/) and grant access to the relevant repositories. You can connect other tools as you configure the agent.

## Start with a pre-built agent

In the agent catalog, choose an agent and select **Set up agent**. The form opens with its name, description, instructions, and suggested settings.

| Pre-built agent | What it does |
| --- | --- |
| Incident investigation | Investigates outages and service degradation, explains likely causes, and prepares fixes |
| Deployment troubleshooting | Diagnoses failed Pulumi previews, updates, and deployments, including operations in external pipelines |
| Drift response | Compares drift with declared configuration and helps resolve the difference |
| Upgrade maintenance | Assesses provider and infrastructure-component upgrades and prepares code changes |
| Security remediation | Investigates security findings and prepares infrastructure fixes |
| Infrastructure migration | Maps dependencies and prepares migration changes |

## Build your own agent

See [Build a custom agent](/docs/ai/agents/custom/) to define its job and write its instructions, then use the setup steps below to connect tools and assign access.

## Customize the instructions

In **System prompt**, describe the agent's job, the information it should use, and the result it should produce. Include your team's conventions and when the agent should ask for help.

Keep details for individual assignments in the task. An upgrade agent's instructions might specify compatibility requirements; the task names the dependency and target version.

Saved agent instructions replace the organization's AI preference instructions. Include any organization-wide requirements the agent must follow. Instructions guide its work; roles and credentials determine what it can access.

## Connect the tools it needs

Expand the integrations selector beside **System prompt** and select the connected MCP services the agent needs. Deselect integrations unrelated to its responsibility.

By default, agents can use all MCP and CLI integrations connected to your organization, including ones added later. Selecting or deselecting an MCP integration saves a fixed list for that agent's tasks. Update that list when the agent needs another MCP integration.

If a service is missing, select **Manage integrations**, or ask an administrator to connect it. Return to the setup form and select the integration. See [Integrations](/docs/ai/agents/integrations/) for setup requirements.

CLI integrations, such as AWS, are selected separately for each task. The saved MCP selection does not restrict them. See [CLI integrations](/docs/ai/neo/integrations/cli/) for setup.

Reference documents in the instructions by path or URL. The agent also needs access to the repository or tool that holds them; a link alone does not grant access.

## Set its access

Review these settings before saving:

| Setting | What to check |
| --- | --- |
| **Role** | Select a custom Pulumi Cloud role whose grants cover the agent's responsibility |
| **Default mode** | Choose when actions require approval. Automatic approval does not grant additional access |

Give the agent only the permissions it needs for its work. Apply this to its Pulumi Cloud role and every integration you connect, limiting both the resources it can access and the actions it can perform.

Choose a role to limit Pulumi Cloud access. A suggested role must already exist; check its grants rather than relying on its name. See [Permissions](/docs/ai/agents/permissions/) for the relationship between roles, permission modes, and external credentials.

## Choose how the agent starts

Under **How do you want to invoke this agent?**, choose:

- **Manually** to assign tasks directly. You can add events and schedules later.
- **Configure a trigger** to start tasks from Pulumi operations, external webhooks, or a recurring schedule. Select **Continue** to configure the trigger. See [Events and schedules](/docs/ai/agents/triggers/) for the setup steps.

## Save and assign a task

Select **Create agent** after completing the configuration. For a webhook trigger, finish the connection steps shown after saving.

On the agent's page, enter an assignment in **Describe the task for this agent** and select the relevant repository or stack context. Check the response for access errors or missing information.

See [Tasks and collaboration](/docs/ai/agents/tasks/) to continue the assignment and collaborate with teammates.

## Change an existing agent

Select **Edit** on the agent's page. See [Change saved configuration](/docs/ai/agents/manage/#change-saved-configuration) for when changes take effect. Add information to the task conversation when it applies only to that assignment.

For lifecycle controls and troubleshooting, see [Manage and troubleshoot](/docs/ai/agents/manage/).
