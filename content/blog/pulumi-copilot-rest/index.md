---
title: "Announcing the Pulumi Copilot REST API Preview"
date: 2024-12-12T15:15:42-05:00
draft: false
meta_desc: Explore Pulumi Copilot's new REST API preview for IaC.
meta_image: meta.png
authors:
    - artur-laksberg
tags:
    - features
    - ai
    - llm
    - copilot
social:
    twitter: |
        The Pulumi Copilot REST API is here! Integrate Copilot’s AI-powered cloud management into your tools, apps, and workflows. Automate tasks, streamline processes, and build smarter cloud solutions. Learn more: https://www.pulumi.com/blog/pulumi-copilot-rest/
    linkedin: |
        The Pulumi Copilot REST API is now available. It allows you to integrate Copilot’s AI-powered cloud management into your own tools, apps, and workflows. Automate tasks, streamline processes, and extend cloud management capabilities to fit your needs. With features like multi-turn conversations and the ability to query specific resources, the API is built for flexibility and ease of integration. If you're looking to bring AI-driven infrastructure management into your stack, this API is a great starting point. Learn more and get started: https://www.pulumi.com/blog/pulumi-copilot-rest/

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---
We built Pulumi Copilot to automate a broad spectrum of cloud management activities using the power of LLMs. Since its initial release earlier this year, hundreds of customers have used Pulumi Copilot to understand and manage cloud infrastructure more effectively and securely, and it is only getting better by the day.

Today, we're excited to announce the availability of the Pulumi Copilot REST API. This new API exposes the full power of Pulumi Copilot, enabling you to integrate infrastructure AI into your own tools, applications, and platforms. While currently in preview, we are eager to get your feedback to ensure it works for anything you can dream up.

<!--more-->

## Enhancing Copilot Capabilities

With the Copilot REST API, you can extend the Copilot capabilities available in the Pulumi Console in the following ways:

- Build Copilot capabilities into your platforms and tools, such as the CLI, development portals, Github actions and so on.
- Support multi-user interaction in workplace collaboration platforms such as Slack and Teams.
- Automate execution of Copilot queries based on scheduled triggers or events, such as deployment completions.
- Access Copilot from mobile clients through platforms like Slack or Teams.

## Implementation Guide

### Initial Configuration

To begin using the Copilot API, set up the following environment variables:

```bash
export PULUMI_COPILOT_URL="https://api.pulumi.com/api/ai/chat/preview"
export PULUMI_ACCESS_TOKEN="pul-..."
```

Note: You can obtain your `PULUMI_ACCESS_TOKEN` from the Pulumi Console.

### Understanding Cloud Context

All Copilot API interactions require two essential parameters:

1. Organization context through the `orgId` field - this is conceptually similar to the organization you select in the dropdown menu on the left-hand side of the Pulumi Console
2. Resource URL from the Pulumi Console, which must begin with `https://app.pulumi.com` - think of this as the browser URL you see when navigating the Pulumi Console. This URL helps Copilot understand the context of your query. While you can provide the base URL (`https://app.pulumi.com`), you can also point to specific resources or updates for more targeted queries. For example, `https://app.pulumi.com/myorg/my-demo-project/my-stack/updates/5` would allow you to ask questions about that specific update

These parameters provide the necessary context for queries about specific resources or updates, allowing Copilot to respond with relevant information just as it would in the Console interface.

### Making API Requests

Here's an example of a basic API request:

```bash
curl -L "$PULUMI_COPILOT_URL" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "query": "Who are the users in my org?",
    "state": {
        "client": {
            "cloudContext": {
                "orgId": "pulumi",
                "url": "https://app.pulumi.com"
            }
        }
    }
}'
```

### Supporting Multi-turn Conversations

The API supports continuous dialogues, in which participants can refer to information shared earlier in the chat. This is supported through conversation IDs that are received with the response:

```json
"conversationId":"369a280c-63f3-4ee6-a13d-c1035a3d05de"
```

This ID enables follow-up queries that maintain context:

```bash
curl -L "$PULUMI_COPILOT_URL" \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "conversationId":"369a280c-63f3-4ee6-a13d-c1035a3d05de",
    "query": "Who of them are admins?",
    "state": {
        "client": {
            "cloudContext": {
                "orgId": "pulumi",
                "url": "https://app.pulumi.com"
            }
        }
    }
}'
```

## Moving Forward

As we continue to evole our AI efforts, your feedback is essential. We are particularly interested in hearing about your implementation experiences, including features that work well, areas that need improvement, or capabilities you'd like to see added. You can consult the [documentation](https://www.pulumi.com/docs/pulumi-cloud/copilot/api) and peruse the [samples](https://github.com/pulumi/copilot-api-samples/tree/main/samples). Please submit any feedback by opening an [issue](https://github.com/pulumi/copilot-api-samples/issues) or by reaching out to us via our [Community Slack](https://pulumi-community.slack.com/archives/C055KGGFB1N)

We can't wait to see what you can build with Pulumi Copilot REST API!
