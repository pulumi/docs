---
title: FAQ
title_tag: Neo FAQ
h1: Neo FAQ
meta_desc: Frequently asked questions about Pulumi Neo covering security, data handling, model providers, and organizational controls.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    ai:
        name: FAQ
        parent: ai-home
        weight: 80
        identifier: ai-faq
aliases:
- /docs/pulumi-cloud/copilot/faq/
---

## What model does Neo use?

Neo uses Anthropic Claude models hosted on [Amazon Bedrock](https://aws.amazon.com/bedrock/) in a Pulumi-managed AWS account. The specific models may change over time to improve answer quality and task performance.

## Will my data be used to train Neo?

No. Amazon Bedrock does not use customer data to train foundation models. Pulumi does not fine-tune or train models on customer data.

## How does Neo handle identity and access?

Neo uses Pulumi Cloud's [role-based access control](/docs/pulumi-cloud/access-management/) model. It only has access to the data and operations that the requesting user has access to. Behind the scenes, Neo makes API calls on the user's behalf, so it does not expose information the user cannot already see.

## What actions can Neo perform?

By default, Neo operates through [pull requests](/docs/ai/pull-requests/), making it effectively read-only. All proposed infrastructure changes are submitted as PRs for review before merging.

Users can opt in to running [`pulumi up`](/docs/ai/running-previews/) directly, which is controlled through [task modes](/docs/ai/settings/#task-modes). Organization administrators set the default task mode, and individual users can adjust it per task.

## What data is sent to the model provider?

Neo transmits conversation context and relevant infrastructure data to Amazon Bedrock to generate responses. All data is encrypted in transit with TLS and at rest by Amazon Bedrock. No third-party MCP servers or external services receive your data as part of Neo's processing.

## Are my secrets exposed?

No. Neo cannot decrypt [secrets](/docs/concepts/secrets/). Secret values remain encrypted and are never exposed to the model provider or included in conversation context.

## What data does Neo store?

Pulumi stores conversation data, including model responses, for debugging and measuring quality. This data is used only for operational purposes and handled in accordance with [Pulumi's privacy policy](https://www.pulumi.com/privacy/), consistent with other Pulumi Cloud product telemetry.

## Can I control Neo access for my organization?

Yes. Organization administrators can enable or disable Neo from the Neo Settings page in the left navigation of Pulumi Cloud. Access can be toggled on or off at any time. See [Neo settings](/docs/ai/settings/#neo-access) for details.
