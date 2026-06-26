---
title_tag: "Pulumi Cloud: REST API Reference"
meta_desc: Overview of the Pulumi Cloud REST API. Query organization, stack, and state data; call any endpoint from the pulumi api CLI.
title: "REST API Docs"
h1: Pulumi Cloud REST API
menu:
    reference:
        name: REST API Docs
        parent: reference-home
        weight: 6
        identifier: cloud-rest-api
aliases:
  - /docs/reference/service-rest-api/
  - /docs/intro/insights/api/
  - /docs/pulumi-cloud/cloud-rest-api/
  - /docs/pulumi-cloud/reference/
  - /docs/pulumi-cloud/reference/cloud-rest-api/
  - /docs/reference/cloud-rest-api/cloud-rest-api/
  - /docs/reference/service-rest-openapi/
  - /docs/intro/insights/openapi/
  - /docs/reference/cloud-rest-openapi/
  - /docs/pulumi-cloud/cloud-rest-openapi/
  - /docs/pulumi-cloud/reference/cloud-rest-openapi/
---

{{% cloud-rest-api-intro %}}

## Calling the API

You can call any endpoint two ways:

* **From the CLI** — use [`pulumi api`](/docs/iac/cli/api/), which inherits your existing CLI credentials, fills `{orgName}`/`{projectName}`/`{stackName}` from the selected stack, and returns a stable JSON error envelope and exit codes that scripts and agents can rely on. Run `pulumi api list` to browse endpoints and `pulumi api describe <path-or-operation-id>` to inspect a specific operation.
* **Directly over HTTPS** — pair an [access token](/docs/administration/access-identity/access-tokens/) with the standard `Accept` and `Content-Type` headers and call the endpoint with `curl` or any HTTP client.

## API documentation by category

The Pulumi Cloud REST API is organized into the following categories. Each page is generated from the live [OpenAPI spec](https://api.pulumi.com/api/openapi/pulumi-spec.json).

{{< openapi-tag-list >}}
