---
title: Use Anthropic with Pulumi Agents
h1: Use Anthropic with Pulumi Agents
meta_desc: Connect your Anthropic workspace to run Pulumi Agents on Claude models and bill model requests to your Anthropic account.
pulumi_cloud_feature: neo-byok
menu:
    ai:
        name: Anthropic
        parent: ai-agents-model-providers
        identifier: ai-model-provider-anthropic
        weight: 10
---

Connect your Anthropic workspace to run Pulumi Agents on Claude and have Anthropic bill the workspace for usage. Create an [Anthropic API key](https://platform.claude.com/docs/en/get-api-key) in the workspace you want Pulumi to use. The workspace needs access to the same Claude models as Pulumi's built-in provider.

If you access Claude through [Amazon Bedrock](/docs/ai/agents/model-providers/amazon-bedrock/) or [Azure Foundry](/docs/ai/agents/model-providers/azure-foundry/), follow the guide for that account.

## Connect Anthropic

{{% agent-model-provider-setup "open" "Anthropic" %}}

Enter your workspace's **API key**. Pulumi supplies the base URL, the `x-api-key` header name, and the model mapping.

## Test and use the provider

{{% agent-model-provider-setup "finish" %}}
