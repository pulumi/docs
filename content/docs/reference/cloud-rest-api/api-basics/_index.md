---
title: API Basics
title_tag: "Pulumi Cloud REST API: API Basics"
meta_desc: The Pulumi Cloud REST API endpoint, authentication, and required headers, plus equivalent calls from the pulumi cloud api CLI command.
menu:
    reference:
        parent: cloud-rest-api
        weight: 1
aliases:
  - /docs/reference/cloud-rest-api/api-basics/
  - /docs/pulumi-cloud/reference/api-basics/
---

This page covers the fundamental requirements for using the Pulumi Cloud REST API, including endpoint URLs, authentication, and required headers.

## Endpoint URL

For the Managed Pulumi Cloud (i.e. [app.pulumi.com](https://app.pulumi.com/signin)), API endpoints are prefixed with the following url:

```plain
https://api.pulumi.com
```

If you are using [Self-Hosted Pulumi Cloud](/docs/pulumi-cloud/self-hosted/), then use the configured endpoint for the [Pulumi API component](/docs/pulumi-cloud/self-hosted/components/api#api-service) (e.g. `https://api.pulumi.example.com`).

## Authentication

All requests must be authenticated using a token via the `Authorization` HTTP header.

The `Authorization` header must be in the form below with the literal string `token`, then a space, then your access token value.

```plain
Authorization: token {token}
```

To view your access tokens, or create a new one, view the <a href="https://app.pulumi.com/account/tokens">Access Tokens</a> page. You will see a list of past tokens, when they were last used, and have the ability to revoke them.

The Pulumi Cloud REST API will return a 401 status code if the token is missing or invalid.

## Required Request Headers

The following headers are required for all operations except where explicitly noted:

```plain
Accept: application/vnd.pulumi+8
Content-Type: application/json
```

## Calling the API from the CLI

The [`pulumi cloud api`](/docs/iac/cli/cloud-api/) command wraps the REST API so you don't have to assemble the headers, base URL, or path-template variables yourself. It uses the same credentials as the rest of the Pulumi CLI, so any token you already use with `pulumi login` is reused automatically.

For example, the following two calls are equivalent:

```bash
# Direct HTTPS request
curl -H "Authorization: token $PULUMI_ACCESS_TOKEN" \
     -H "Accept: application/vnd.pulumi+8" \
     https://api.pulumi.com/api/user

# Same call from the Pulumi CLI
pulumi cloud api /api/user
```

`pulumi cloud api list` (alias: `ls`) lists every endpoint in the OpenAPI spec, and `pulumi cloud api describe <path-or-operation-id>` prints the parameter, request, and response schemas for a single operation. See the [`pulumi cloud api` guide](/docs/iac/cli/cloud-api/) for the full set of flags, output formats, and the agent-facing error envelope.
