---
title: API Basics
title_tag: "Pulumi Cloud REST API: API Basics"
meta_desc: Learn about the Pulumi Cloud REST API endpoint, authentication, and required headers for making API requests.
menu:
    cloud:
        parent: pulumi-cloud-reference
        weight: 1
---

This page covers the fundamental requirements for using the Pulumi Cloud REST API, including endpoint URLs, authentication, and required headers.

## Endpoint URL

For the Managed Pulumi Cloud (i.e. [app.pulumi.com](https://app.pulumi.com/)), API endpoints are prefixed with the following url:

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

To view your access tokens, or create a new one, view the <a href="https://app.pulumi.com/account/tokens" target="_blank">Access Tokens</a> page. You will see a list of past tokens, when they were last used, and have the ability to revoke them.

The Pulumi Cloud REST API will return a 401 status code if the token is missing or invalid.

## Required Request Headers

The following headers are required for all operations except where explicitly noted:

```plain
Accept: application/vnd.pulumi+8
Content-Type: application/json
```
