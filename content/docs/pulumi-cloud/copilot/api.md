---
title_tag: "Pulumi Copilot API"
meta_desc: Learn about Pulumi Copilot REST APIs for integrating Pulumi Copilot capabilities
  into your applications and workplace platforms.
title: Pulumi Copilot API
h1: Pulumi Copilot API Overview
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Pulumi Copilot API
    parent: pulumi-cloud-copilot
    weight: 1
    identifier: pulumi-cloud-copilot-api
search:
  keywords:
    - copilot
    - integrating
    - apis
    - api
    - workplace
    - platforms
    - rest
---

{{% notes "info" %}}
Pulumi Copilot's API is currently in preview and subject to change. It is not currently suitable for production use.
{{% /notes %}}

The Pulumi Copilot REST API (currently in Preview) is part of the [Pulumi Cloud REST API](https://www.pulumi.com/docs/pulumi-cloud/reference/cloud-rest-api) that is used to integrate Pulumi Copilot capabilities with other applications or tools.

## Endpoint URL

For the Managed Pulumi Cloud (i.e. [app.pulumi.com](https://app.pulumi.com/)), API endpoints are prefixed with the following url:

```
https://api.pulumi.com
```

Currently, [Self-Hosted Pulumi Cloud](/docs/pulumi-cloud/self-hosted/) is not supported by the Pulumi Copilot REST API.

## Authentication

All requests must be authenticated using a token via the `Authorization` HTTP header.

The `Authorization` header must be in the form below with the literal string `token`, then a space, then your access token value.

```
Authorization: token {token}
```

To view your access tokens, or create a new one, view the [Access Tokens](https://app.pulumi.com/user/settings/tokens) page. You will see a list of past tokens, when they were last used, and have the ability to revoke them.

The Pulumi Copilot REST API will return a 401 status code if the token is missing or invalid.

## Required request headers

The following header is required:

```
Content-Type: application/json
```

## Start conversation

Starts a new conversation with Pulumi Copilot with a query.

```
POST /api/ai/chat/preview
```

### Request format

#### Request body schema

```JSON
{
    "query": string,
    "state": {
        "client": {
            "cloudContext": {
                "orgId": string,
                "url": string
            }
        }
    }
}
```

#### Fields description

- `query`: The natural language query to process (e.g., "Who are the users in my org?").
- `orgId`: The identifier for your Pulumi organization (e.g., "acme").
- `url`: The URL of the resource in the Pulumi Cloud that provides context to the Pulumi Copilot (e.g., "https://app.pulumi.com/myorg/project1/dev/updates/4"). This parameter must start with "https://app.pulumi.com".

### Response format

#### Response body schema

```JSON
{
    "conversationId": string,
    "messages": [
        {
            "role": string,
            "kind": string,
            "content": string
        }
    ]
}
```

#### Response fields description

- `conversationId`: Unique identifier for the conversation started by the call.
- `messages`: Array of message objects containing the conversation history and system events.

Each message in the messages array contains:

- `role`: The sender of the message ("assistant" or "user").
- `kind`: The type of message:
    - `trace`: Debug or system information (this data is not sent to the LLM and it only used to debugging).
    - `response`: User queries or assistant responses.
    - `status`: Status updates about operations being performed.
    - `program`: Generated code when requested by the user.
- `content`: The actual message content.

Messages returned by the "assistant" of type "response" represent the responses from the Copilot to the user query.

### Example request

```bash
curl -L https://api.pulumi.com/api/ai/chat/preview \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "query": "Analyze this update. If it failed, tell me how to resolve the issues.",
    "state": {
        "client": {
            "cloudContext": {
                "orgId": "myorg",
                "url": "https://app.pulumi.com/myorg/project1/dev/updates/4"
            }
        }
    }
}'
```

### Example response

```JSON
{
  "conversationId": "522e0fdb-e992-4be4-9937-37249ed93289",
  "messages": [
    {
      "role": "user",
      "kind": "response",
      "content": "Analyze this update. If it failed, tell me how to resolve the issues."
    },
    {
      "role": "assistant",
      "kind": "trace",
      "content": "Conversation with user 'john' in org 'myorg' from console (rest-api-v2)"
    },
    {
      "role": "assistant",
      "kind": "status",
      "content": "Executing Pulumi Cloud skill"
    },
    {
      "role": "assistant",
      "kind": "response",
      "content": "The update for the stack 'project1/dev' has failed. The failure is due to an error in creating a Virtual Network resource in Azure. The specific error is related to the incorrect handling of an Output<T> type in Pulumi. The error message indicates that calling 'ToString' on an Output<T> is not supported, which leads to a bad request error (HTTP 400) when trying to create the resource.\n\n**How to resolve the issue:**\n- Review the code where the resourceGroupName is being set. Ensure that you are not directly converting an Output<T> to a string using 'ToString'.\n- Use the 'Apply' method or 'Output.Format' to correctly handle the Output<T> type. For example, use `o.Apply(v => $\"prefix{v}suffix\")` or `Output.Format($\"prefix{hostname}suffix\")`.\n- Refer to the Pulumi documentation on [Inputs and Outputs](https://www.pulumi.com/docs/concepts/inputs-outputs) for more guidance on handling Output<T> types properly."
    }
  ]
}
```

## Post message to conversation

Posts a new message to an existing conversation. The request format is identical to the "Start Conversation", with the addition of the `conversationId` field returned from that call.

```
POST /api/ai/chat/preview
```

### Request format

#### Request body schema

```JSON
{
    "query": string,
    "state": {
        "client": {
            "cloudContext": {
                "orgId": string,
                "url": string
            }
        }
    },
    "conversationId": string
}
```

#### Fields description

- `query`, `orgId`, `url`: Same as in the "Start conversation" request, see above.
- `conversationId`: conversation to post the message to.

### Response format

Same as in the "Start conversation" request, see above.

### Example request

```bash
curl -L https://api.pulumi.com/api/ai/chat/preview \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "query": "Why can I not directly convert an Output<T> to a string?",
    "state": {
        "client": {
            "cloudContext": {
                "orgId": "myorg",
                "url": "https://app.pulumi.com/myorg/project1/dev/updates/4"
            }
        }
    },
    "conversationId":"522e0fdb-e992-4be4-9937-37249ed93289"
}'
```

### Example response

````JSON
{
  "conversationId": "522e0fdb-e992-4be4-9937-37249ed93289",
  "messages": [
    // omitted for brevity
    // ...
    {
      "role": "assistant",
      "kind": "status",
      "content": "Executing Pulumi Docs skill"
    },
    {
      "role": "assistant",
      "kind": "response",
      "content": "In Pulumi, an `Output<T>` represents a value that is computed asynchronously, which means the actual value isn't available until the resource is provisioned. This is why you can't directly convert an `Output<T>` to a string. Instead, you should use the `apply` method to specify a function that will be executed once the value is available. This ensures that any code dependent on the `Output`'s value only runs after the value is resolved.\n\nHere's a brief example in TypeScript:\n\n```typescript\nimport * as pulumi from \"@pulumi/pulumi\";\n\nconst bucket = new aws.s3.Bucket(\"my-bucket\");\n\nconst bucketNameString: pulumi.Output<string> = bucket.id.apply(id => {\n    if (typeof id === 'string') return id;\n    throw new Error(`Expected a string but got: ${id}`);\n});\n```\n\nIn this example, `bucket.id` is an `Output`. The `apply` method is used to transform it into a string. For more information, you can refer to Pulumi's documentation on [Outputs](https://www.pulumi.com/docs/intro/concepts/inputs-outputs/)."
    }
  ]
}
````
