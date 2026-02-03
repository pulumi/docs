---
title: "Announcing OpenAPI support for the Pulumi Cloud API"
date: "2026-02-02"
meta_desc: "The Pulumi Service REST API now has an OpenAPI 3.0 specification you can fetch at runtime. Use it for client generation, validation, and discovery."
authors:
  - arun-loganathan
  - davide-massarenti
  - devon-grove
  - zac-cook
tags:
  - features
  - pulumi-cloud
  - api
---

We're excited to announce that the Pulumi Service REST API is now described by an OpenAPI 3.0 specification!

This is a feature that has been a long time coming. We have heard your requests for OpenAPI support [loud and clear](https://github.com/pulumi/pulumi-cloud-requests/issues/100), and are thrilled to be able to announce that not only do we have a published specification for consumption, but that our API code is now building from this specification as well.

You can fetch the spec directly from the API at runtime or use it for client generation, validation, and documentation—all from a single, machine-readable contract.

## A single contract for the Pulumi Cloud API

The Pulumi Service API powers the Pulumi CLI, the Pulumi Console, and third-party integrations. Until now, there was no single, published machine-readable description of that API. We've changed that. The API is now defined and served as a standard OpenAPI 3.0.3 document.

### Runtime discovery

You can retrieve the spec from the API itself, so your tooling always sees the same surface the service implements.

### Client generation

Use your favorite OpenAPI tooling (e.g. OpenAPI Generator, Swagger Codegen) to generate API clients in the language of your choice.

### Validation and testing

Validate requests and responses, or build mocks and tests, from the same spec the service uses.

### Documentation

The spec is the source of truth; no separate, hand-maintained API doc that can drift from reality.

## How to get the spec

Send a GET request to:

```
https://api.pulumi.com/api/openapi/pulumi-spec.json
```

No authentication is required. The response is the OpenAPI 3.0 document for the Pulumi Cloud API, describing the supported, documented API surface.

## Source of truth and stability

The OpenAPI spec is not hand-written. It is generated from the same API definition that drives our backend and console code. When we add or change API routes or models, the spec is regenerated, so the published document stays in sync with what the service actually implements. That gives you a clear, stable contract for the Pulumi Cloud API.

## What you can do next

### Fetch the spec

Send `GET https://api.pulumi.com/api/openapi/pulumi-spec.json` and plug it into your favorite OpenAPI tooling.

### Generate a client

Use the spec to generate type-safe API clients in Go, TypeScript, Python, or any language your OpenAPI toolchain supports.

### Validate and test

Use the spec to validate requests and responses or to build mocks for tests and local development.

### Explore the API

Load the spec into Swagger UI, Redoc, or another viewer to browse the Pulumi Cloud API interactively.

## What's next

We are using this spec as the foundation for our own tooling, and have plans to continue leveraging the spec in our toolchain longer-term.

* **CLI**: We plan to drive the Pulumi CLI’s API client from the OpenAPI spec so that CLI and API stay in lockstep.
* **Pulumi Service Provider**: We are also building towards day 1 updates to the [Pulumi Service Provider](https://www.pulumi.com/registry/packages/pulumi-service/) so that new and changed API resources are generated from the spec and ship in sync with the service.
* **Docs Enhancements**: Although you can load the spec using Swagger UI for your own browsing, we are intent on shipping enhancements to our public REST API docs that will keep them up-to-date according to the OpenAPI spec.

As we ship those updates, you will get a single source of truth from API to CLI to provider.

If you have questions or feedback about the OpenAPI spec or the Pulumi Cloud API, reach out in our [Community Slack](https://pulumi-community.slack.com/join/shared_invite/zt-2amio1u4h-5Y35enT27Y0dk4N8ZYHbMg#/shared_invite/email) or open an issue in the [Pulumi repository](https://github.com/pulumi/pulumi). We're excited to see what you build with it.
