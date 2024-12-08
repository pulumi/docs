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
    twitter:
    linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---
Since its initial release in June 2024, Pulumi Copilot has seen strong adoption, helping teams understand and manage their cloud infrastructure more effectively. Today, we're excited to announce the availability of the Pulumi Copilot REST API in preview. This release enables developers to integrate Pulumi Copilot's powerful capabilities directly into their own tools, applications, and workplace collaboration platforms. While currently in preview, we plan to quickly move the API to production as we gather feedback from early adopters and ensure it meets our community's needs.

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

As we continue to evole our AI efforts, your feedback is essential. We are particularly interested in hearing about your implementation experiences, including features that work well, areas that need improvement, or capabilities you'd like to see added. Please submit any feedback by opening an [issue](https://github.com/pulumi/copilot-api-samples/issues) or reaching out to us via our [Community Slack](https://pulumi-community.slack.com/archives/C055KGGFB1N)

For additional implementation examples, please refer to the [samples](https://github.com/pulumi/copilot-api-samples/tree/main/samples) directory in our samples repo.

We can't wait to see what you can build with Pulumi Copilot REST API!
