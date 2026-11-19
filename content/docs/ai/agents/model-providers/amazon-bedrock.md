---
title: Use Amazon Bedrock with Pulumi Agents
h1: Use Amazon Bedrock with Pulumi Agents
meta_desc: Configure an AWS IAM role so Pulumi Agents can invoke models or inference profiles in your Amazon Bedrock account.
pulumi_cloud_feature: neo-byok
menu:
    ai:
        name: Amazon Bedrock
        parent: ai-agents-model-providers
        identifier: ai-model-provider-amazon-bedrock
        weight: 40
---

Run Pulumi Agents against models in your AWS account. Your account needs access to the models or inference profiles you want to use in the selected region. Pulumi assumes an IAM role using workload identity, so you can connect Bedrock without storing an AWS access key.

## Connect Amazon Bedrock

{{% agent-model-provider-setup "open" "Amazon Bedrock" %}}

Copy the **Issuer**, **Subject**, and **Audience** shown in the Pulumi form. The subject identifies your organization as `pulumi:agents:pulumi.organization.id:<organization-id>`, and the audience is `aws:agents:<organization-id>`. Use the values from your form in the trust policy below.

### Create the IAM role

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

### Choose the region and models

Return to the Pulumi form and complete these fields.

- **API format**: **Anthropic Messages** for Claude models, or **OpenAI Chat Completions** or **OpenAI Responses** for models Bedrock serves over those APIs.
- **AWS region**: The region Pulumi calls Bedrock in, such as `us-west-2`. GovCloud and China regions are not supported.
- **IAM role ARN**: The role Pulumi assumes, such as `arn:aws:iam::123456789012:role/PulumiAgentBedrock`.
- **Default model**: A Bedrock model ID or inference profile ID that your region serves, such as `us.anthropic.claude-sonnet-4-5-20250929-v1:0`.
- **Fast model (recommended)**: The ID of a smaller, faster model.

With **OpenAI Responses**, you can also set [Thinking](/docs/ai/agents/model-providers/#thinking) for the provider.

## Test and use the provider

{{% agent-model-provider-setup "finish" %}}
