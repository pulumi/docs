---
title: Bring your own model provider
title_tag: Bring your own model provider for Pulumi Neo
h1: Bring your own model provider
meta_desc: Run Pulumi Neo with Anthropic's Claude models through your own Anthropic account, Azure Foundry deployment, or compatible endpoint.
menu:
    ai:
        name: Model providers (BYOK)
        parent: ai-neo
        weight: 52
        identifier: ai-neo-model-providers
---

{{< pulumi-cloud "neo-byok" >}}
Organizations on the legacy Business Critical edition also have access to BYOK.
{{< /pulumi-cloud >}}

With bring your own key (BYOK), Pulumi Neo uses your organization's existing model provider account for inference. Your provider bills you directly for that usage.

Neo currently supports Anthropic's Claude models. You can access these models through Anthropic, Azure Foundry, or a custom endpoint that supports the Anthropic Messages API. To request support for other models or providers, [contact Pulumi support](/support/).

## Before you begin

You need permission to manage your organization's integrations, such as the Admin role, and credentials for your model provider.

## Add a model provider

1. In the Pulumi Cloud console, open your organization's **Neo Settings**.
1. Select **Model provider**, then **Add model provider**.
1. Enter a unique **Name** using lowercase letters, numbers, and hyphens.
1. Select a **Provider** and enter the connection details for [Anthropic](#anthropic), [Azure Foundry](#azure-foundry), or a [custom endpoint](#custom-anthropic-compatible-endpoint).
1. Select **Save**. If this is your organization's first provider, Neo starts using it for tasks.
1. Select **Test connection** to check that the provider works before you start a task.
1. After the test succeeds, select **Set as default** if another provider is already active.

### Anthropic

Use an [Anthropic API key](https://platform.claude.com/docs/en/get-api-key) scoped to the workspace Neo should use.

Select **Anthropic** and enter your Anthropic API key in the **Value** field under **Auth headers**. The base URL and `x-api-key` header name are preset.

Neo uses its configured Claude models through your Anthropic account. You do not need to enter a model mapping. Your account must have access to the models Neo uses.

### Azure Foundry

Use a Foundry resource with a Claude model deployment and an API key. If you need to create a deployment, follow [Microsoft's deployment instructions](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude). Open the deployment's **Details** tab to get its key and endpoint.

Select **Azure Foundry** and enter the following details:

- **Azure resource or endpoint**: Enter either:
    - Your Foundry resource name, such as `my-resource`.
    - The endpoint's base URL, such as `https://my-resource.services.ai.azure.com/anthropic`. Do not include `/v1/messages`.
- **Auth headers**: Enter the resource's API key in **Value**. The header name is preset to `x-api-key`.
- **Default model**: The Claude deployment name in your Azure Foundry resource, such as `neo-sonnet-prod`.
- **Fast model (recommended)**: The deployment name for a Claude Haiku model, such as `neo-haiku-prod`.

Use your Azure deployment names in the model fields. These can differ from the underlying Claude model IDs.

### Custom Anthropic-compatible endpoint

Use an endpoint that serves Claude models through the Anthropic Messages API and supports streaming responses. The endpoint must use a public HTTPS address that Pulumi Cloud can reach. Private IP addresses are not supported.

Select **Custom (Anthropic-compatible endpoint)** and enter the following details:

- **Base URL**: Your endpoint's HTTPS base URL. Neo appends `/v1/messages`, so omit that suffix. For example, `https://gateway.example.com/anthropic` sends requests to `https://gateway.example.com/anthropic/v1/messages`.
- **Auth headers**: The header names and secret values your endpoint requires. For example, use `x-api-key` with an API key, or `Authorization` with `Bearer <your-api-key>`. Use **Add header** if the endpoint requires more than one header.
- **Default model**: The model ID or alias your endpoint expects for Neo's main Claude model.
- **Fast model (recommended)**: The model ID or alias your endpoint expects for a Claude Haiku model.

For Azure Foundry and custom endpoints, the default model is required. If you omit the fast model, Neo routes those requests to the default model too.

## Test and update a provider

Select a saved provider, then select **Test connection**. The results show whether each model is reachable and, when available, the model that the endpoint reports serving. The test does not change the default provider.

To rotate a key, select **Replace credentials**, enter the new values, and select **Save**. If your endpoint uses multiple auth headers, enter the complete set. Pulumi stores the values encrypted and does not display them after saving.

## Switch or remove a provider

You can save multiple providers, but Neo uses one default provider for the organization. Select a saved provider and choose **Set as default** to switch to it.

To remove a provider, select **Remove**, then **Confirm remove**. If you remove the default provider while others remain, Neo selects another saved provider as the default. Removing the last provider returns Neo to Pulumi's default model provider and standard Neo token billing.

## Billing

Your model provider bills you for requests served through BYOK. Pulumi does not charge Neo tokens for those requests. Other Pulumi usage, such as deployments that Neo starts, remains subject to your edition's pricing and contract.

## Next steps

- [Start a Neo task](/docs/ai/neo/tasks/).
- [Configure Neo settings](/docs/ai/neo/settings/).
- [Manage Neo usage limits](/docs/ai/neo/usage-limits/).
