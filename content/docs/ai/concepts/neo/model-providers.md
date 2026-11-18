---
title: Bring your own model provider
title_tag: Bring your own model provider for Pulumi Agents
h1: Bring your own model provider
meta_desc: Run Pulumi Agents on models from your own Anthropic, OpenAI, Azure Foundry, or Amazon Bedrock account, or from any compatible endpoint.
menu:
    ai:
        name: Model providers
        parent: ai-agents-administration
        weight: 10
        identifier: ai-neo-model-providers
aliases:
- /docs/ai/neo/model-providers/
---

{{< pulumi-cloud "neo-byok" >}}
Organizations on the legacy Business Critical edition also have access to BYOK.
{{< /pulumi-cloud >}}

Connect your organization's model provider account so [Pulumi Agents](/docs/ai/agents/) sends model requests through that account. Your provider bills you directly for the usage. This option is called bring your own key (BYOK).

You can connect Anthropic, OpenAI, Azure Foundry, Amazon Bedrock, or a custom endpoint, and you can save more than one provider. Set an organization default, then [choose a different provider for individual agents](#choose-a-model-for-an-agent) as needed.

## Supported providers and APIs

Choose the API format and authentication method your provider supports.

| Provider | API formats | Authentication |
| --- | --- | --- |
| Anthropic | Anthropic Messages | API key |
| OpenAI | OpenAI Chat Completions, OpenAI Responses | API key |
| Azure Foundry | Anthropic Messages, OpenAI Chat Completions, OpenAI Responses | API key or [workload identity](#workload-identity) |
| Amazon Bedrock | Anthropic Messages, OpenAI Chat Completions, OpenAI Responses | [Workload identity](#workload-identity) |
| Custom | Anthropic Messages, OpenAI Chat Completions, OpenAI Responses | One or more authentication headers |

Pulumi regularly evaluates Pulumi Agents on Claude Opus and Claude Sonnet models. Agents also run on OpenAI models and on other models your provider serves, but quality, speed, and cost can differ. The console shows a note when a provider's default model is not one Pulumi evaluates.

## Before you begin

You need permission to manage your organization's integrations, such as the Admin role, and credentials for your model provider.

## Add a model provider

1. In the Pulumi Cloud console, open your organization's **Agent Settings**.
1. Select **Model provider**, then **Add model provider**.
1. Enter a unique **Name** using lowercase letters, numbers, and hyphens. You cannot change the name later, and the name `pulumi` is reserved.
1. Select a **Provider** and enter the connection details for [Anthropic](#anthropic), [OpenAI](#openai), [Azure Foundry](#azure-foundry), [Amazon Bedrock](#amazon-bedrock), or a [custom endpoint](#custom-endpoint).
1. Select **Save**. Saving [tests the connection](#test-a-provider) first.
1. If the provider is not the default yet, select **Set as default** to use it for new tasks that follow the organization default. See [how the default is chosen](#the-default-provider).

### Anthropic

Use an [Anthropic API key](https://platform.claude.com/docs/en/get-api-key) scoped to the workspace your agents should use.

Select **Anthropic** and enter your API key. The base URL and the `x-api-key` header name are preset.

Agents use the same Claude models as Pulumi's built-in provider. You do not enter a model mapping, and your account must have access to those models.

### OpenAI

Select **OpenAI** and enter the following details:

- **API key**: Your OpenAI API key.
- **Thinking**: How much the models reason before they act. See [Thinking](#thinking).
- **Default model**: The model that carries out agent tasks. Pick a suggested model or enter a model ID.
- **Fast model (recommended)**: A small, fast model for lightweight calls, such as naming tasks.

### Azure Foundry

Use a Foundry resource with a model deployment. If you need to create a Claude deployment, follow [Microsoft's deployment instructions](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/how-to/use-foundry-models-claude).

Select **Azure Foundry** and enter the following details:

- **API format**: The API your deployment serves: **Anthropic Messages**, **OpenAI Chat Completions**, or **OpenAI Responses**.
- **Authentication**: **API key**, or **Workload identity (Entra ID)** to sign in without a stored key. See [Azure Foundry with workload identity](#azure-foundry-with-workload-identity).
- **Azure resource or endpoint**: Enter either:
    - Your Foundry resource name, such as `my-resource`.
    - The endpoint's base URL. For Anthropic Messages, this ends in `/anthropic`, such as `https://my-resource.services.ai.azure.com/anthropic`. For the OpenAI formats, it ends in `/openai/v1`.
- **API key**: The resource's API key, when you authenticate with a key.
- **Default model**: The deployment name in your Foundry resource, such as `agents-sonnet-prod`.
- **Fast model (recommended)**: The deployment name for a smaller, faster model.

Use your Azure deployment names in the model fields. These can differ from the underlying model IDs.

### Amazon Bedrock

Pulumi calls Amazon Bedrock in your AWS account by assuming an IAM role you create. No AWS access key is stored. Set up the role first by following [Amazon Bedrock with workload identity](#amazon-bedrock-with-workload-identity).

Select **Amazon Bedrock** and enter the following details:

- **API format**: **Anthropic Messages** for Claude models, or **OpenAI Chat Completions** or **OpenAI Responses** for models Bedrock serves over those APIs.
- **AWS region**: The region Pulumi calls Bedrock in, such as `us-west-2`. GovCloud and China regions are not supported.
- **IAM role ARN**: The role Pulumi assumes, such as `arn:aws:iam::123456789012:role/PulumiAgentBedrock`.
- **Default model**: A Bedrock model ID or inference profile ID that your region serves, such as `us.anthropic.claude-sonnet-4-5-20250929-v1:0`.
- **Fast model (recommended)**: The ID of a smaller, faster model.

### Custom endpoint

<span id="custom-anthropic-compatible-endpoint"></span>

Use any endpoint that serves the Anthropic Messages, OpenAI Chat Completions, or OpenAI Responses API and supports streaming responses, such as an LLM gateway. The endpoint must use a public HTTPS address that Pulumi Cloud can reach. Private IP addresses are not supported.

Select **Custom** and enter the following details:

- **API format**: The API your endpoint serves.
- **Base URL**: Your endpoint's HTTPS base URL. The form shows the full URL that requests go to.
    - For Anthropic Messages, agents append `/v1/messages`. For example, `https://gateway.example.com/anthropic` sends requests to `https://gateway.example.com/anthropic/v1/messages`.
    - For the OpenAI formats, include the version segment. Agents append `/chat/completions` or `/responses`. For example, `https://gateway.example.com/v1` sends requests to `https://gateway.example.com/v1/chat/completions`.
- **Auth headers**: The header names and secret values your endpoint requires. For example, use `x-api-key` with an API key, or `Authorization` with `Bearer <your-api-key>`. Use **Add header** if the endpoint requires more than one header.
- **Default model**: The model ID or alias your endpoint expects for agent tasks.
- **Fast model (recommended)**: The model ID or alias for a smaller, faster model.

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
| OpenAI | **Off**, **Low**, **Medium**, or **High**. **Off** selects OpenAI Chat Completions; the other levels select OpenAI Responses. |
| Azure Foundry, Amazon Bedrock, or Custom with OpenAI Responses | **Model default**, **Low**, **Medium**, or **High**. **Model default** uses the model's default effort. |
| Other provider and API combinations | No provider-level Thinking setting. |

Higher effort uses more tokens and time. Some models, such as `gpt-6-astra` and `gpt-6.1-sol`, call tools only with reasoning on, so they need a level other than **Off**.

You can also [set a thinking level for one agent](#choose-a-model-for-an-agent).

## Workload identity

With workload identity, Pulumi signs a short-lived OpenID Connect (OIDC) token for your organization and exchanges it for cloud credentials. You do not store a long-lived key in Pulumi Cloud.

When you select Amazon Bedrock, or Azure Foundry with workload identity, the form shows three values to use in your cloud account:

- **Issuer**: Pulumi Cloud's OIDC issuer URL.
- **Subject**: Identifies your organization's agents. It has the form `pulumi:agents:pulumi.organization.id:<organization-id>`.
- **Audience**: `aws:agents:<organization-id>` for AWS, or `azure:agents:<organization-id>` for Azure.

Copy these values from the form. The examples below use `api.pulumi.com/oidc` as the issuer.

### Amazon Bedrock with workload identity

1. In the IAM console, add an OpenID Connect identity provider. Use the **Issuer** as the provider URL and the **Audience** as the audience.
1. Create an IAM role for that identity provider with a trust policy that requires the **Audience** and the **Subject**:

    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "Federated": "arn:aws:iam::<account-id>:oidc-provider/api.pulumi.com/oidc"
          },
          "Action": "sts:AssumeRoleWithWebIdentity",
          "Condition": {
            "StringEquals": {
              "api.pulumi.com/oidc:aud": "aws:agents:<organization-id>",
              "api.pulumi.com/oidc:sub": "pulumi:agents:pulumi.organization.id:<organization-id>"
            }
          }
        }
      ]
    }
    ```

1. Give the role permission to invoke the models you use. The **OpenAI Responses** format also needs `bedrock:InvokeModel` on the account's `project/default` resource:

    ```json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Action": [
            "bedrock:InvokeModel",
            "bedrock:InvokeModelWithResponseStream"
          ],
          "Resource": [
            "arn:aws:bedrock:*::foundation-model/*",
            "arn:aws:bedrock:*:*:inference-profile/*",
            "arn:aws:bedrock:*:*:project/default"
          ]
        }
      ]
    }
    ```

    Narrow the resources to the models and regions your agents use.

1. Enter the role's ARN in **IAM role ARN** and save the provider.

Your AWS account must also have access to each model in Amazon Bedrock.

### Azure Foundry with workload identity

1. In Microsoft Entra ID, create or choose an app registration.
1. On the app registration, add a federated credential with the **Issuer**, **Subject**, and **Audience** from the form.
1. Assign the app the **Cognitive Services User** role on your Azure AI Foundry resource.
1. In the provider form, set **Authentication** to **Workload identity (Entra ID)** and enter the app's **Directory (tenant) ID** and **Application (client) ID**.

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

Your model provider bills you for requests served through BYOK. Pulumi does not charge Neo tokens for those requests. Other Pulumi usage remains subject to your edition's pricing and contract.

BYOK does not change how agent workers are billed. When an agent task runs on an agent worker, the worker's run time is billed as [workflow minutes](/pricing/), with or without BYOK.

<span id="next-steps"></span>

See [Usage limits](/docs/ai/concepts/neo/usage-limits/) for spending controls on Pulumi-billed model requests.
