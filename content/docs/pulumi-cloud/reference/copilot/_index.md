---
title: Copilot
title_tag: "Pulumi Cloud REST API: Copilot"
meta_desc: Learn about the Pulumi Copilot REST API endpoints for integrating AI-powered infrastructure assistance with your applications.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 2
aliases:
    - /docs/pulumi-cloud/copilot/api/
---

The Pulumi Copilot API provides endpoints for integrating Pulumi's AI-powered infrastructure assistance capabilities with your applications and platforms. It allows you to programmatically access Pulumi Copilot's natural language understanding to analyze infrastructure, answer questions about Pulumi, and even generate infrastructure as code.

{{% notes "info" %}}
Pulumi Copilot's API is currently in preview and subject to change.
{{% /notes %}}

## Start Conversation

Starts a new conversation with Pulumi Copilot with a query.

```plain
POST /api/ai/chat/preview
```

### Parameters

| Parameter             | Type   | In   | Description                                                                      |
|-------------------- |------- |------|----------------------------------------------------------------------------------|
| `query`             | string | body | The natural language query to process (e.g., "Who are the users in my org?").    |
| `state.client.cloudContext.orgId` | string | body | The identifier for your Pulumi organization (e.g., "acme").         |
| `state.client.cloudContext.url`   | string | body | The URL of the resource in Pulumi Cloud. Must start with "https://app.pulumi.com". |

### Request Body Schema

```json
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

### Response Format

#### Response Body Schema

```json
{
    "conversationId": string,
    "messages": [
        {
            "role": string,
            "kind": string,
            "content": string | object
        }
    ]
}
```

#### Response Fields

- `conversationId`: Unique identifier for the conversation started by the call.
- `messages`: Array of message objects containing the conversation history and system events.

Each message in the messages array contains:

- `role`: The sender of the message ("assistant" or "user").
- `kind`: The type of message:
    - `trace`: Debug or system information (this data is not sent to the LLM and is only used for debugging).
    - `response`: User queries or assistant responses.
    - `status`: Status updates about operations being performed.
    - `program`: Generated code when requested by the user.
- `content`: The actual message content. Can be either a string or an object, depending on the message kind:
  - For messages of kind `trace`, `response`, and `status`, content is a string.
  - For messages of kind `program`, content is an object containing program details (see below).

#### Program Content Object

When the message `kind` is `program`, the `content` field is an object with the following structure:

```json
{
    "code": string,
    "plan": {
        "instructions": string
    },
    "language": string,
    "programId": string
}
```

- `code`: The generated program code.
- `plan.instructions`: A description of the steps to implement the code.
- `language`: The programming language of the generated code (e.g., "typescript").
- `programId`: A unique identifier for the generated program.

### Example

#### Request

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

#### Response

```json
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

### Example Request to Generate a Program

```bash
curl -L https://api.pulumi.com/api/ai/chat/preview \
-H "Authorization: token $PULUMI_ACCESS_TOKEN" \
-H "Content-Type: application/json" \
-d '{
    "query": "Write code to create an S3 bucket",
    "state": {
        "client": {
            "cloudContext": {
                "orgId": "myorg",
                "url": "https://app.pulumi.com"
            }
        }
    }
}'
```

### Example Program Generation Response

Note that the `content` field is now an object containing program code and other elements:

```json
{
  "conversationId": "a1b2c3d4-e5f6-7g8h-9i0j-k1l2m3n4o5p6",
  "messages": [
    {
      "role": "assistant",
      "kind": "program",
      "content": {
        "code": "import * as pulumi from \"@pulumi/pulumi\";\nimport * as aws from \"@pulumi/aws\";\n\n// Create an S3 bucket\nconst bucket = new aws.s3.Bucket(\"my-bucket\", {\n    bucket: \"my-unique-bucket-name\",\n    acl: \"private\",\n});\n\n// Export the name of the bucket\nexport const bucketName = bucket.bucket;",
        "plan": {
          "instructions": "1. Install Pulumi CLI and AWS SDK.\n2. Create a new Pulumi project.\n3. Write the Pulumi program to define an S3 bucket resource.\n4. Deploy the stack using `pulumi up`.\n\nHere is the code to create an S3 bucket using Pulumi in TypeScript:"
        },
        "language": "typescript",
        "programId": "pn7Gfod"
      }
    }
  ]
}
```

## Post Message to Conversation

Posts a new message to an existing conversation. The request format is identical to the "Start Conversation", with the addition of the `conversationId` field returned from that call.

```plain
POST /api/ai/chat/preview
```

### Parameters

| Parameter             | Type   | In   | Description                                                                                                         |
|-------------------- |------- |------|--------------------------------------------------------------------------------------------------------------------|
| `query`             | string | body | The natural language query to process (e.g., "Who are the users in my org?").                                       |
| `state.client.cloudContext.orgId` | string | body | The identifier for your Pulumi organization (e.g., "acme").                                            |
| `state.client.cloudContext.url`   | string | body | The URL of the resource in the Pulumi Cloud that provides context to the Pulumi Copilot. |
| `conversationId`    | string | body | The conversation ID to post the message to. |

### Request Body Schema

```json
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

### Response Format

Same as in the "Start conversation" request.

### Example

#### Request

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

#### Response

```json
{
  "conversationId": "522e0fdb-e992-4be4-9937-37249ed93289",
  "messages": [
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
```
