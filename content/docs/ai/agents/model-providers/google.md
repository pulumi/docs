---
title: Use Google Gemini with Pulumi Agents
h1: Use Google Gemini with Pulumi Agents
meta_desc: Connect a Google Gemini API key to Pulumi Agents, choose Gemini models, and test the connection.
pulumi_cloud_feature: neo-byok
menu:
    ai:
        name: Google
        parent: ai-agents-model-providers
        identifier: ai-model-provider-google
        weight: 25
---

Use a [Google Gemini API key](https://aistudio.google.com/app/apikey) to run Pulumi Agents on Gemini models. Google bills your account for the requests.

## Connect Google

{{% agent-model-provider-setup "open" "Google" %}}

1. Enter your Gemini **API key**.
1. For **Default model**, choose a suggested Gemini model or enter a model ID your account can use. Suggestions include `gemini-4-neon`, `gemini-4-hydrogen`, `gemini-3.8-flash`, and `gemini-flash-latest`.
1. Optionally, set **Fast model** to a smaller Gemini model for short calls such as naming a task. If you leave it blank, Pulumi uses the default model for those calls.

Pulumi Agents uses Google's OpenAI-compatible Chat Completions API. The Google provider sets the API endpoint and authentication format for you.

## Test and use the provider

{{% agent-model-provider-setup "finish" %}}
