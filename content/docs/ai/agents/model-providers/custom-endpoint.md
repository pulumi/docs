---
title: Use a custom model endpoint with Pulumi Agents
h1: Use a custom model endpoint with Pulumi Agents
meta_desc: Connect Pulumi Agents to a streaming model endpoint or LLM gateway using Anthropic or OpenAI APIs and authentication headers.
pulumi_cloud_feature: neo-byok
menu:
    ai:
        name: Custom endpoint
        parent: ai-agents-model-providers
        identifier: ai-model-provider-custom-endpoint
        weight: 50
---

Connect an LLM gateway or another endpoint that serves the Anthropic Messages, OpenAI Chat Completions, or OpenAI Responses API. The endpoint must support streaming and have a public HTTPS address that Pulumi Cloud can reach. Private IP addresses are unsupported.

## Connect your endpoint

{{% agent-model-provider-setup "open" "Custom" %}}

Enter the connection details for your endpoint.

- **API format**: The API your endpoint serves.
- **Base URL**: Your endpoint's HTTPS base URL. The form shows the full URL that requests go to.
    - For Anthropic Messages, agents append `/v1/messages`. For example, `https://gateway.example.com/anthropic` sends requests to `https://gateway.example.com/anthropic/v1/messages`.
    - For the OpenAI formats, include the version segment. Agents append `/chat/completions` or `/responses`. For example, `https://gateway.example.com/v1` sends requests to `https://gateway.example.com/v1/chat/completions`.
- **Auth headers**: The header names and secret values your endpoint requires. For example, use `x-api-key` with an API key, or `Authorization` with `Bearer <your-api-key>`. Use **Add header** if the endpoint requires more than one header.
- **Default model**: The model ID or alias your endpoint expects for agent tasks.
- **Fast model (recommended)**: The model ID or alias for a smaller, faster model.

With **OpenAI Responses**, you can also set [Thinking](/docs/ai/agents/model-providers/#thinking) for the provider.

## Test and use the provider

{{% agent-model-provider-setup "finish" %}}
