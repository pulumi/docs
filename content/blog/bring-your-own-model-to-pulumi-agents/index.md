---
title: "Bring your own model to Pulumi Agents"
date: 2026-11-18
draft: false
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

Pulumi Agents can now run on the models your team already uses. Model requests go through your organization’s provider account, so your provider bills you directly.

<!--more-->

In Pulumi Cloud, open your organization’s **Agent Settings** and select **Model provider**. Choose **Add model provider** to connect OpenAI, Amazon Bedrock, Anthropic, Google (for Gemini models), Azure Foundry, or a compatible endpoint.

Name the connection and enter the details for your provider. When you select **Save**, Pulumi sends a test request to each model you configured.

Use that name when you define an agent in TypeScript. This infrastructure review agent uses the model configured on the `openai-platform` connection.

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
