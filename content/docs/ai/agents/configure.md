---
title: Create and configure an agent
title_tag: Create and configure an agent | Pulumi Agents
h1: Create and configure an agent
pulumi_cloud_feature: pulumi-agents
meta_desc: Choose an agent, tailor its instructions, connect its tools, and assign work.
aliases:
- /docs/ai/agents/custom/
menu:
    ai:
        name: Create and configure an agent
        parent: ai-agents-create-manage
        identifier: ai-agents-configure
        weight: 20
---

<span id="build-a-custom-agent"></span>
<span id="example-investigate-checkout-failures"></span>

Create an agent in Pulumi Cloud to give your team a shared place to delegate work. You can start with an agent from the catalog or supply your own instructions.

## Before you begin

You need permission to create agents in your Pulumi Cloud organization. If the agent needs to read code or open pull requests, [connect your version control provider](/docs/integrations/version-control/) and grant access to the relevant repositories. You can connect other tools during setup.

<span id="create-the-agent"></span>

## Choose an agent {#start-with-a-pre-built-agent}

1. In Pulumi Cloud, open your organization's **Agents** page and select the **Agents** tab.
1. Select **New agent** to open the catalog. If the catalog is already visible, continue to the next step.
1. Choose an agent and select **Set up agent**. The form opens with starting instructions and suggested settings.
1. Give your agent a name and description that help teammates recognize its job. For example, name an agent based on **Upgrade maintenance** “Dependency upgrades” and describe the repositories and dependencies it should maintain.

The catalog includes these agents:

| Agent | Job |
| --- | --- |
| Incident investigation | Investigate outages and service degradation, explain likely causes, and prepare fixes |
| Deployment troubleshooting | Diagnose failed Pulumi previews, updates, and deployments, including operations in external pipelines |
| Drift response | Compare drift with declared configuration and help resolve the difference |
| Upgrade maintenance | Assess provider and infrastructure-component upgrades and prepare code changes |
| Security remediation | Investigate security findings and prepare infrastructure fixes |
| Infrastructure migration | Map dependencies and prepare migration changes |

## Build your own agent

If none of these agents fits the work you need, choose **Create your own from scratch** in the catalog. You supply the name, description, and instructions.

<span id="write-its-instructions"></span>

## Customize the instructions

The **System prompt** field contains the instructions the agent follows across its tasks. Describe the work you want to delegate and the result you expect, such as a pull request with passing tests. Add any team conventions or requirements the agent should follow.

For example, a team that delegates checkout failures to an agent could give it these instructions:

> Follow the incident runbook in `runbooks/checkout.md` in the checkout repository. Compare the first errors in the logs with recent deployments. If you find a code fix, open a pull request and cite the logs that explain the change.

When you assign an incident to this agent, include the alert URL and the time the failure began.

The agent uses this system prompt instead of **Organization instructions**. Copy any organization-wide requirements it should follow into this field.

<span id="connect-the-tools-it-needs"></span>

<span id="connect-tools-and-assign-access"></span>

## Select integrations

Give the agent access to the systems it needs for its work. For example, an incident-investigation agent might need Datadog to read monitoring data. If its system prompt refers to a runbook, include the document's path or URL and make sure the agent can access the repository or tool where it is stored.

For integrations that use MCP, such as Datadog:

1. Open the integrations selector beside **System prompt**.
1. Select the integrations the agent needs and deselect the others.
1. If an integration is not listed, select **Manage integrations** to connect it, or ask an administrator to do so. Return to the form and select it.

The selection is saved with the agent. To use another MCP integration later, add it to the agent's configuration. See [Integrations](/docs/ai/agents/integrations/) for connection instructions.

Cloud CLI integrations, such as the AWS CLI, use a different setup. They obtain credentials from a [Pulumi ESC](/docs/esc/) environment and do not appear in this selector. Follow [Cloud CLI integrations](/docs/ai/integrations/cli-integrations/) to connect one, then [grant the agent access to its ESC environment](#set-its-access).

## Set its access

In **Role**, select the Pulumi Cloud role the agent uses. This choice also affects [which teammates can start tasks](/docs/ai/agents/permissions/#give-teammates-access). The default, **Reader**, can read the organization's stacks, environments, and cloud accounts. You can instead select **Builder**, **Maintainer**, or a custom role, provided its permissions do not exceed your own. If the agent needs a cloud CLI integration, choose a role with `environment:open` on the connection's environment. See [Pulumi Cloud access](/docs/ai/agents/permissions/#scope-pulumi-cloud-access) for role requirements.

In **Default mode**, choose **Manual**, **Balanced**, or **Auto** to control when the agent asks for approval. See [Approval modes](/docs/ai/agents/permissions/#separate-approvals-from-access) for the differences between modes.

## Choose a model

{{< pulumi-cloud "neo-byok" />}}

If your organization has [connected its own model providers](/docs/ai/concepts/neo/model-providers/), the form shows a **Model** setting. Keep **Org default** selected to follow the organization's default provider, or select **Claude** for Pulumi's built-in models or a saved provider by name.

For a provider that supports it, **Thinking** sets how much effort the agent's models spend on reasoning. Choose **Default** to use the model's default thinking level, or select **Low**, **Medium**, or **High**. For OpenAI Responses providers, the default option is labeled **Provider default** and uses the provider's configured thinking level. See [Choose a model for an agent](/docs/ai/concepts/neo/model-providers/#choose-a-model-for-an-agent).

Changing these settings requires permission to manage your organization's integrations. See [Model providers](/docs/ai/concepts/neo/model-providers/) for provider setup and model options.

## Choose how the agent starts

Under **How do you want to invoke this agent?**, choose:

- **Manually** to assign tasks directly. You can add events and schedules later.
- **Configure a trigger** to start tasks from Pulumi operations, external webhooks, or a recurring schedule. Select **Continue** to configure the trigger.

On the trigger step, choose a **Trigger type**. Set the event filters or schedule, then expand **Task instructions and context** to review the **Trigger name** and **Prompt**. The prompt tells the agent what to do when the trigger fires. Select **Create agent** when you finish.

To add an event or schedule to an agent you have already saved, follow [Events and schedules](/docs/ai/agents/triggers/).

<span id="assign-a-task"></span>

## Save and assign a task

If you chose **Manually**, select **Create agent**. For a webhook trigger, finish the connection steps shown after saving.

On the agent's page, describe what you want it to do in the message box, then select **Send message**. Include the repository URL or stack name if the work involves one.

[Work with tasks](/docs/ai/agents/tasks/) explains how to reply, approve a plan, and work with teammates.

## Change an existing agent

Select **Edit** on the agent's page. See [Change saved configuration](/docs/ai/agents/manage/#change-saved-configuration) for when changes take effect. For a change that applies to one task, reply in that task.

For lifecycle controls and troubleshooting, see [Manage and troubleshoot](/docs/ai/agents/manage/).
