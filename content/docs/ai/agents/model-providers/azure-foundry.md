---
title: Use Azure Foundry with Pulumi Agents
h1: Use Azure Foundry with Pulumi Agents
meta_desc: Connect an Azure Foundry model deployment to Pulumi Agents using an API key or Microsoft Entra workload identity.
pulumi_cloud_feature: neo-byok
menu:
    ai:
        name: Azure Foundry
        parent: ai-agents-model-providers
        identifier: ai-model-provider-azure-foundry
        weight: 30
---

Run Pulumi Agents against model deployments in your Azure Foundry resource. You need the resource name or endpoint and the names of the deployments you want to use. If you need to deploy Claude, follow [Microsoft's deployment instructions](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude).

## Connect Azure Foundry

{{% agent-model-provider-setup "open" "Azure Foundry" %}}

Choose the **API format** your deployment serves: **Anthropic Messages**, **OpenAI Chat Completions**, or **OpenAI Responses**. For **Authentication**, select **API key** and enter the resource's key, or select **Workload identity (Entra ID)** and configure the trust relationship below.

### Configure workload identity

With workload identity, Pulumi exchanges an OpenID Connect (OIDC) token for short-lived Azure credentials. If you selected API key authentication, continue to [enter your model deployments](#enter-your-model-deployments).

1. Copy the **Issuer**, **Subject**, and **Audience** shown in the Pulumi form. The subject identifies your organization as `pulumi:agents:pulumi.organization.id:<organization-id>`, and the audience is `azure:agents:<organization-id>`.
1. In Microsoft Entra ID, create or choose an app registration and add a federated credential with those three values.
1. Assign the app the **Cognitive Services User** role on your Foundry resource.
1. Return to Pulumi and enter the app's **Directory (tenant) ID** and **Application (client) ID**.

### Enter your model deployments

- **Azure resource or endpoint**: Enter either:
    - Your Foundry resource name, such as `my-resource`.
    - The endpoint's base URL. For Anthropic Messages, this ends in `/anthropic`, such as `https://my-resource.services.ai.azure.com/anthropic`. For the OpenAI formats, it ends in `/openai/v1`.
- **Default model**: The deployment name in your Foundry resource, such as `agents-sonnet-prod`.
- **Fast model (recommended)**: The deployment name for a smaller, faster model.

Use the deployment names from your Foundry resource. These can differ from the underlying model IDs. With **OpenAI Responses**, you can also set [Thinking](/docs/ai/agents/model-providers/#thinking) for the provider.

## Test and use the provider

{{% agent-model-provider-setup "finish" %}}
