---
title: Use OpenAI with Pulumi Agents
h1: Use OpenAI with Pulumi Agents
meta_desc: Connect an OpenAI account to Pulumi Agents, choose models and reasoning effort, and test the connection.
pulumi_cloud_feature: neo-byok
menu:
    ai:
        name: OpenAI
        parent: ai-agents-model-providers
        identifier: ai-model-provider-openai
        weight: 20
---

Use an API key from your OpenAI account to run Pulumi Agents on the models you select. OpenAI bills your account for the requests. If your models are deployed in Azure, follow the [Azure Foundry guide](/docs/ai/agents/model-providers/azure-foundry/).

## Connect OpenAI

{{% agent-model-provider-setup "open" "OpenAI" %}}

1. Enter your OpenAI **API key**.
1. Choose a **Thinking** level. **Off** uses Chat Completions. **Low**, **Medium**, and **High** use the Responses API. If your model requires reasoning to call tools, choose one of those three levels.
1. For **Default model**, choose a suggested model or enter a model ID your account can use.
1. Optionally, set **Fast model** to a smaller model for short calls such as naming a task. If you leave it blank, Pulumi uses the default model for those calls.

## Test and use the provider

{{% agent-model-provider-setup "finish" %}}
