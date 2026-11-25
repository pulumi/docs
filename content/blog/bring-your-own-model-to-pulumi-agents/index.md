---
title: "Bring your own model to Pulumi Agents"
date: 2026-11-23
draft: false
meta_desc: Use models from your organization's provider account with Pulumi Agents, and choose a provider for each agent in TypeScript or the Pulumi Cloud console.
canonical_url: https://www.pulumi.com/docs/ai/concepts/neo/model-providers/
feature_image: feature.png
authors:
    - pulumi-ai-team
tags:
    - ai
    - pulumi-cloud
category: product
---

You can now run Pulumi Agents on the models your team already uses. Connect your organization’s model provider account, and your provider bills you directly for the requests your agents make. You can use that connection across your organization or give an individual agent its own choice of model.

<!--more-->

Pulumi Agents supports OpenAI, Amazon Bedrock, Anthropic, Google (for Gemini models), Azure Foundry, and compatible endpoints. To connect one, open **Agent Settings** in Pulumi Cloud. Under **Model provider**, choose **Add model provider**, select your provider, and enter a name and connection details. Select **Save** to test the connection.

Once you’ve named a connection, you can use it in code. Here, `modelProvider: "openai-platform"` tells the infrastructure review agent to use the model your team configured on that connection.

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

In the console, choose **Set as default** to use a connection for new tasks that follow your organization’s default. To choose one for an individual agent, use the **Model** setting when you create or edit it. The [model provider guide](/docs/ai/agents/model-providers/) has the connection details for each provider.
