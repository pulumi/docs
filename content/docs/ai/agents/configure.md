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

Pre-built agents include instructions for common infrastructure work. You can edit those instructions and choose which tools and resources the agent can access.

## Before you begin

You need permission to create agents in your Pulumi Cloud organization. [Connect your version control provider](/docs/integrations/version-control/) and grant access to the relevant repositories. You can connect other tools as you configure the agent.

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

See [Build a custom agent](/docs/ai/agents/custom/) to define its job and write its instructions.

## Customize the instructions

In **System prompt**, describe the agent's job, the information it should use, and the result it should produce. Include your team's conventions and when the agent should ask for help.

Keep details for individual assignments in the task. An upgrade agent's instructions might specify compatibility requirements; the task names the dependency and target version.

Saved agent instructions replace the organization's AI preference instructions. Include any organization-wide requirements the agent must follow. Instructions guide its work; roles and credentials determine what it can access.

## Connect the tools it needs

Expand the integrations selector beside **System prompt** and select the connected MCP services the agent needs. Deselect integrations unrelated to its responsibility.

Creating an agent saves the selected MCP integrations. To give it access to an integration connected later, edit the agent and add that integration to its selection.

If a service is missing, select **Manage integrations**, or ask an administrator to connect it. Return to the setup form and select the integration. See [Integrations](/docs/ai/agents/integrations/) for setup requirements.

CLI integrations, such as AWS, are available from the organization's connections without a per-task selection. The agent's role must allow it to open each connection's ESC environment. See [CLI integrations](/docs/ai/neo/integrations/cli/) for setup and access requirements.

Reference documents in the instructions by path or URL. The agent also needs access to the repository or tool that holds them; a link alone does not grant access.

## Set its access

| Setting | What to check |
| --- | --- |
| **Role** | Select a Pulumi Cloud role whose grants cover the agent's responsibility |
| **Default mode** | Choose when the agent asks for approval. In **Auto** mode, actions do not require your approval |

Give the agent only the permissions it needs for its work. Apply this to its Pulumi Cloud role and every integration you connect, limiting both the resources it can access and the actions it can perform.

If you leave **Role** at **Agent Read Only**, Pulumi creates or reuses that role when you save. You can instead select **Member** or a custom role, provided its permissions do not exceed your own. Check the role's grants rather than relying on its name. See [Permissions](/docs/ai/agents/permissions/) for access and approval controls.

## Choose how the agent starts

Under **How do you want to invoke this agent?**, choose:

- **Manually** to assign tasks directly. You can add events and schedules later.
- **Configure a trigger** to start tasks from Pulumi operations, external webhooks, or a recurring schedule. Select **Continue** to configure the trigger.

On the trigger step, choose a **Trigger preset**. Set the event filters or schedule, then expand **Task instructions and context** to review the **Trigger name** and **Prompt**. The prompt is the assignment for each run. Select **Create agent** when you finish.

To add an event or schedule to an agent you have already saved, follow [Events and schedules](/docs/ai/agents/triggers/).

## Save and assign a task

Select **Create agent** after completing the configuration. For a webhook trigger, finish the connection steps shown after saving.

On the agent's page, enter an assignment in **Describe the task for this agent**. Include the repository URL or stack name when relevant. Check the response for access errors or missing information.

See [Tasks and collaboration](/docs/ai/agents/tasks/) to continue the assignment and collaborate with teammates.

## Change an existing agent

Select **Edit** on the agent's page. See [Change saved configuration](/docs/ai/agents/manage/#change-saved-configuration) for when changes take effect. Add information to the task conversation when it applies only to that assignment.

For lifecycle controls and troubleshooting, see [Manage and troubleshoot](/docs/ai/agents/manage/).
