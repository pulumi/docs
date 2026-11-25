---
title: Bring your own model provider
title_tag: Bring your own model provider for Pulumi Agents
h1: Bring your own model provider
meta_desc: Run Pulumi Agents on models from your own Anthropic, OpenAI, Google, Azure Foundry, or Amazon Bedrock account, or from any compatible endpoint.
menu:
    ai:
        name: Model providers
        parent: ai-agents
        weight: 80
        identifier: ai-agents-model-providers
menu_overview_label: Overview
aliases:
- /docs/ai/concepts/neo/model-providers/
- /docs/ai/neo/model-providers/
---

{{< pulumi-cloud "neo-byok" >}}
Organizations on the legacy Business Critical edition also have access to BYOK.
{{< /pulumi-cloud >}}

Connect your organization's model provider account so [Pulumi Agents](/docs/ai/agents/) sends model requests through that account. Your provider bills you directly for the usage. Pulumi also calls this feature bring your own key (BYOK).

To connect a provider, you need permission to manage your organization's integrations, such as the Admin role. You can save multiple providers, set an organization default, and [choose a different provider for an individual agent](#choose-a-model-for-an-agent).

<span id="before-you-begin"></span>
<span id="add-a-model-provider"></span>
<span id="workload-identity"></span>

## Supported providers and APIs

Choose the guide for the account that serves your model. For example, if you use Claude through AWS, follow the Amazon Bedrock guide.

| Provider | API formats | Authentication |
| --- | --- | --- |
| <span id="anthropic"></span>[Anthropic](/docs/ai/agents/model-providers/anthropic/) | Anthropic Messages | API key |
| <span id="openai"></span>[OpenAI](/docs/ai/agents/model-providers/openai/) | OpenAI Chat Completions, OpenAI Responses | API key |
| <span id="google"></span>[Google](/docs/ai/agents/model-providers/google/) | OpenAI Chat Completions | API key |
| <span id="azure-foundry-with-workload-identity"></span><span id="azure-foundry"></span>[Azure Foundry](/docs/ai/agents/model-providers/azure-foundry/) | Anthropic Messages, OpenAI Chat Completions, OpenAI Responses | API key or [workload identity](/docs/ai/agents/model-providers/azure-foundry/#configure-workload-identity) |
| <span id="amazon-bedrock-with-workload-identity"></span><span id="amazon-bedrock"></span>[Amazon Bedrock](/docs/ai/agents/model-providers/amazon-bedrock/) | Anthropic Messages, OpenAI Chat Completions, OpenAI Responses | [Workload identity](/docs/ai/agents/model-providers/amazon-bedrock/#create-the-iam-role) |
| <span id="custom-endpoint"></span><span id="custom-anthropic-compatible-endpoint"></span>[Custom endpoint](/docs/ai/agents/model-providers/custom-endpoint/) | Anthropic Messages, OpenAI Chat Completions, OpenAI Responses | One or more authentication headers |

## Models

For every provider except Anthropic, choose the models the agent uses:

- **Default model** is required and carries out the task.
- **Fast model** is optional and handles short requests, such as naming a task. If you omit it, these requests use the default model.

### Context window

By default, an agent uses the full context window Pulumi has verified for the default model. To reduce cost and latency, set a lower **Context window** limit on the provider. The limit must be at least 32,000 tokens and cannot exceed the model's verified limit.

### Thinking

**Thinking** controls how much effort the models spend on reasoning. The provider form offers these choices:

| Provider and API format | Thinking options |
| --- | --- |
| OpenAI | **Off**, **Low**, **Medium**, or **High**. **Off** selects OpenAI Chat Completions. The other levels select OpenAI Responses. |
| Azure Foundry, Amazon Bedrock, or Custom with OpenAI Responses | **Model default**, **Low**, **Medium**, or **High**. **Model default** uses the model's default effort. |
| Other provider and API combinations | No provider-level Thinking setting. |

Higher effort uses more tokens and time. Some models, such as `gpt-6-astra` and `gpt-6.1-sol`, call tools only with reasoning on, so they need a level other than **Off**.

You can also [set a thinking level for one agent](#choose-a-model-for-an-agent).

## Test a provider

<span id="test-and-update-a-provider"></span>

When you save a provider, Pulumi sends a test request to each model with your settings. If a model cannot be reached, the form shows the error for that model. Fix the settings and save again, or select **Save anyway** to store them as they are. Tasks that use a provider with invalid settings fail until you correct those settings.

To rerun a successful connection test, open the provider and select **Test connection**. The results show whether each model is reachable and, when available, the model the endpoint reports serving. Save your changes before you test. The test does not change the default provider.

To rotate a key, select **Replace credentials**, enter the new values, and select **Save**. If your endpoint uses multiple auth headers, enter the complete set. Pulumi stores the values encrypted and does not display them after saving.

## The default provider

The organization default determines which provider new tasks use. You can [choose a different provider for an individual agent](#choose-a-model-for-an-agent).

- The first provider you add becomes the default when it serves the Anthropic Messages API.
- A provider that serves an OpenAI API format becomes the default only when you select **Set as default**.
- Later providers are saved as alternatives. Select **Set as default** on a provider to switch to it.

A task keeps the provider it started on. A change of the default applies to new tasks.

## Disable or remove a provider

<span id="switch-or-remove-a-provider"></span>

Disable a provider to stop agents from using it without deleting its configuration. In the provider's actions menu, select **Disable**. When a provider is disabled:

- Users can no longer select it when creating or editing an agent.
- New tasks for agents set to it use the organization's default instead.
- Running tasks that use it stop and show an error.

You cannot disable the default provider. Set another default first. Select **Enable** to make the provider available again.

To remove a provider, open it and select **Remove**, then **Confirm remove**. If you remove the default provider, no other provider takes its place. New tasks that follow the organization default use Pulumi's models, with standard billing, until you set another default. Agents configured to use another provider continue to use that provider.

## Choose a model for an agent

By default, every agent uses the organization's default provider. When you [create or edit an agent](/docs/ai/agents/configure/), you can select a different **Model**:

- **Org default** follows the organization's default provider, including later changes to it.
- **Claude** uses Pulumi's built-in models.
- A saved provider uses that provider's default and fast models.

For a provider that serves the Anthropic Messages or OpenAI Responses API, you can also set **Thinking** for the agent. On an OpenAI Responses provider it overrides the provider's level. On an Anthropic Messages provider it sets the thinking effort of models that support adaptive thinking. A thinking level is not available on Pulumi's built-in models or on an OpenAI Chat Completions provider.

Changing an agent's model provider or choosing a thinking level requires permission to manage your organization's integrations, the same permission that manages model providers. Other members can edit the rest of the agent, and its model settings stay as they are.

When you [update an agent through the REST API](/docs/reference/cloud-rest-api/neo/#put-apipreviewagentsorgnamedefinitionsdefinitionid), omit `modelProvider` or `reasoningEffort` to keep the saved value. Send an empty string to return to the default.

## Billing

Your provider bills you for model requests it serves. Set budgets and rate limits in your provider account to control that spend. Pulumi's [usage limits](/docs/ai/concepts/neo/usage-limits/) apply only to requests billed by Pulumi.

For agent worker charges, see **What are workflow minutes?** in the [pricing FAQ](/pricing/#faq).

<span id="next-steps"></span>
