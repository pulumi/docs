---
title: "Announcing OpenAPI support for the Pulumi Cloud REST API"
date: "2026-02-05"
meta_desc: "The Pulumi Cloud REST API now has an OpenAPI 3.0 specification you can fetch at runtime. Use it for client generation, validation, and discovery."
meta_image: meta.png
authors:
  - davide-massarenti
  - claire-gaestel
  - devon-grove
  - arun-loganathan
  - zachary-cook

tags:
  - features
  - pulumi-cloud
  - api
---

We're thrilled to announce that the Pulumi Cloud REST API is now described by an OpenAPI 3.0 specification, and we're just getting started.

This is a feature that has been a long time coming. We have heard your requests for OpenAPI support [loud and clear](https://github.com/pulumi/pulumi-cloud-requests/issues/100), and we're excited to share that not only do we have a published specification for consumption, but our API code is now built from this specification as well. Moving forward, this single source of truth unlocks better tooling, tighter integration, and a more predictable API experience for everyone.

You can fetch the spec directly from the API at runtime or use it for client generation, validation, and documentation, all from one machine-readable contract.

<!--more-->

## A single contract for the Pulumi Cloud REST API

The Pulumi Cloud API powers the Pulumi CLI, the Pulumi Console, and third-party integrations. Until now, there was no single, published machine-readable description of that API. We've changed that. The API is now defined and served as a standard OpenAPI 3.0.3 document.

* **Runtime discovery**: You can retrieve the spec from the API itself, so your tooling always sees the same surface the service implements.
* **Client generation**: Use your favorite OpenAPI tooling (e.g. OpenAPI Generator, Swagger Codegen) to generate API clients in the language of your choice.
* **Validation and testing**: Validate requests and responses, or build mocks and tests, from the same spec the service uses.
* **Documentation**: The spec is the source of truth, not a separate, hand-maintained API doc that can drift from reality. Load the spec into Swagger UI, Redoc, or another viewer to browse the Pulumi Cloud API interactively.

## How to get the spec

Send a GET request to:

```
https://api.pulumi.com/api/openapi/pulumi-spec.json
```

No authentication is required. The response is the OpenAPI 3.0 document for the Pulumi Cloud API, describing the supported, documented API surface.

## Source of truth and stability

We do not hand-write the OpenAPI spec. We generate it from the same API definition that drives our backend and console code. When we add or change API routes or models, we regenerate the spec so the published document stays in sync with what the service actually implements. That gives you a clear, stable contract for the Pulumi Cloud API.

## What we are building next

We are using this spec as the foundation for our own tooling, and have plans to continue leveraging the spec in our toolchain long-term.

* **CLI**: We plan to drive the Pulumi CLI’s API client from the OpenAPI spec so that CLI and API stay in lockstep.
* **Pulumi Service Provider**: We are also building towards day 1 updates to the [Pulumi Service Provider](https://www.pulumi.com/registry/packages/pulumiservice/) so that new and changed API resources are generated from the spec and ship in sync with the service.
* **Docs Enhancements**: Although you can load the spec using Swagger UI for your own browsing, we are intent on shipping enhancements to our [public REST API docs](https://www.pulumi.com/docs/reference/cloud-rest-api/) that will keep them up-to-date according to the OpenAPI spec.

As we ship those updates, you will get a single source of truth from API to CLI to provider.

If you have questions or feedback about the OpenAPI spec or the Pulumi Cloud API, reach out in our [Community Slack](https://slack.pulumi.com/) or open an issue in the [Pulumi repository](https://github.com/pulumi/pulumi). We're excited to see what you build with it.
