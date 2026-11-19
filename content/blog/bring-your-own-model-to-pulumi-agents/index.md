---
title: "Bring Your Own Model to Pulumi Agents"
date: 2026-11-18
draft: true
meta_desc: Use models from your organization's provider account with Pulumi Agents, and choose a provider for each agent in TypeScript or the Pulumi Cloud console.
canonical_url: https://www.pulumi.com/docs/ai/concepts/neo/model-providers/
feature_image: feature.png
authors:
    - mark-huber
tags:
    - ai
    - pulumi-cloud
category: product
---

Your team can run Pulumi Agents on models you already use through your organization’s provider account. You can use OpenAI models through your OpenAI account or models available in your AWS account through Amazon Bedrock.

<!--more-->

You can connect Anthropic, OpenAI, Azure Foundry, Amazon Bedrock, or a compatible endpoint. Your provider bills you directly for model requests your agents make through that account.

In Pulumi Cloud, open your organization’s **Agent Settings**. Under **Model provider**, choose **Add model provider**. Give the connection a name, select your provider, and enter its connection details. When you select **Save**, Pulumi sends a test request to each model you configured.

If you define your agents in TypeScript, use the connection name in your Pulumi program. Here, `openai-platform` is the name of a saved connection. The infrastructure review agent uses the model configured on that connection.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as pulumiservice from "@pulumi/pulumiservice";

new pulumiservice.api.agents.Definition("infra-review", {
    orgName: pulumi.getOrganization(),
    name: "infra-review",
    displayName: "Infrastructure Review",
    customInstructions: "Review proposed infrastructure changes and summarize their impact.",
    modelProvider: "openai-platform",
});
```

To use a provider as your organization’s default for new tasks, choose **Set as default**. To select one for an individual agent, set `modelProvider` in code or choose **Model** when you create or edit the agent in the console. For the connection details each provider requires, see the [model provider guide](/docs/ai/concepts/neo/model-providers/).
