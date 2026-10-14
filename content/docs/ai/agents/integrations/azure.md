---
title: Connect Azure
title_tag: Connect Azure | Pulumi Agents
h1: Connect Azure
meta_desc: Connect Azure to Pulumi Agents using credentials managed by Pulumi ESC.
menu:
    ai:
        name: Azure
        parent: ai-integrations-cli
        weight: 12
---

Connect Azure so an agent can use the Azure CLI with credentials from Pulumi ESC.

## Choose the service principal

Use a service principal with access to the Azure resources the agent needs. Assign roles at the narrowest scope that covers its work, such as a resource group. See [Design access around the job](/docs/ai/agents/permissions/#design-access-around-the-job) for guidance on credential scope and lifecycle.

## Prepare an ESC environment

The Azure CLI integration expects an ESC environment that supplies these [environment variables](/docs/esc/concepts/outputs/#environmentvariables):

| Variable | Value |
| --- | --- |
| `AZURE_CLIENT_ID` | The service principal's application ID |
| `AZURE_CLIENT_SECRET` | The service principal's client secret |
| `AZURE_TENANT_ID` | The Microsoft Entra tenant ID |
| `AZURE_SUBSCRIPTION_ID` | The subscription the agent should use |

Store the client secret as a secret in ESC. The agent also needs [permission to open the environment](/docs/ai/agents/permissions/#scope-pulumi-cloud-access).

## Connect the environment

As an organization administrator:

{{% agent-cli-connection tool="Azure" %}}

Give the connection a name that identifies its purpose, such as `staging-azure`. Include the subscription ID and relevant resource groups in its notes.

## Use the connection

Select the connection in the task composer's **CLI integrations** menu. In the task, identify the subscription and resources the agent should work with. See [Tasks and collaboration](/docs/ai/agents/tasks/) to assign work and review the results.
