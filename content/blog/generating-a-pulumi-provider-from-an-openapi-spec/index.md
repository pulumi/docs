---
title: "Generating a Pulumi Provider from an OpenAPI Spec"
date: 2026-05-22
draft: false
meta_desc: "Pulumi Service Provider v1.0 generates its pulumiservice:api/* surface from Pulumi Cloud's OpenAPI spec at runtime, so new features land without provider PRs."
meta_image: meta.png
feature_image: feature.png
authors:
    - luke-ward
tags:
    - pulumi-service
    - pulumi-cloud
schema_type: auto

# Social media copy is auto-posted to X, LinkedIn, and Bluesky when merged to master.
# Character limits: X ~280, Bluesky 300, LinkedIn 3000. Leave blank to skip a platform.
social:
    twitter:
    linkedin:
    bluesky:
---

The Pulumi Service Provider's new `pulumiservice:api/*` resource surface is generated directly from Pulumi Cloud's OpenAPI spec at runtime.

This is the v1.0 release of the Pulumi Service Provider, and several new Pulumi Cloud capabilities land in the provider at the same time: fine-grained RBAC as code, Pulumi IDP as code, and audit-log export as IaC. The `api` namespace is in preview, and the existing `pulumiservice:index:*` resources continue to be the production-supported path.

<!--more-->

## Why this matters for users

Historically, every new Pulumi Cloud feature implied a follow-up PR in the provider before that feature could be used from a Pulumi program. The provider was always slightly behind the API it wrapped, and entirely new capability areas could take months to land.

The `api/*` surface changes both timelines. Because the schema is derived from the OpenAPI spec at runtime:

1. Whole new resource families land in the provider the same release they reach Pulumi Cloud. v1.0 shipped fine-grained RBAC, stack config, Pulumi IDP catalog management, and audit-log exports as managed resources with no bespoke provider code.
1. New fields, features, and enum values on existing resources show up across all five language SDKs the moment they appear in the spec.

## What's new in v1.0

v1.0 lifts whole capability areas of Pulumi Cloud into the `api/*` surface, not just incremental field additions. None of it required bespoke provider code.

1. **Fine-grained RBAC as code.** Custom roles, organization membership, and team role assignments are now managed resources.
1. **Stack config as a managed resource.** `stacks:Config` lets you declare stack configuration values directly in a Pulumi program, closing a gap where stack config used to live outside IaC.
1. **Pulumi IDP as code.** `services:Service` makes the [Pulumi IDP](/docs/idp/) catalog manageable from your Pulumi programs. Platform teams can publish service definitions as code rather than only through the IDP console.
1. **Audit-log export as IaC.** `AuditLogExportConfiguration` brings audit-log export sinks under Pulumi management with a real destroy path.

## How it works

The Pulumi Service Provider bundles Pulumi Cloud's OpenAPI 3 document (published at <https://api.pulumi.com/api/openapi/pulumi-spec.json>) into the provider binary when the provider is built and released, so there is no runtime download. When the provider process starts as part of a Pulumi operation, it parses the embedded spec together with a small companion metadata file. The metadata file captures the Pulumi-specific semantics that an OpenAPI document can't express on its own: which endpoints pair up to form a single resource, what a resource's composite ID looks like, which response fields are secrets that arrive exactly once at create time, and so on.

Most of that metadata is auto-derived by a scaffolder that runs as part of `go generate`. Existing values are preserved as pins, so when a heuristic would suggest something different, the human override stays in place and the tool logs an `INFO` to keep the override visible. What stays hand-curated is the editorial layer: resource descriptions, examples, v0 aliases, and explicit exclusions.

The language SDKs are still generated (Pulumi requires typed SDKs per language), but they are built against the runtime-emitted schema rather than against hand-written Go code. No resource Go file is written to disk for the `api/*` surface.

Two CI workflows tie a spec refresh to a release tag. A manually-triggered refresh workflow pulls the latest spec, regenerates the SDKs, and opens a labeled PR. When that PR merges, a tag workflow pushes the corresponding release tag and the standard release pipeline takes over. End to end, one button click moves a spec change through to published packages and registry docs.

## What the api namespace covers

The `api` namespace already spans most of Pulumi Cloud's resource model.

For resources that have an ancestor under `pulumiservice:index:*`, the mapping lives in [`docs/v0-api-coverage.md`](https://github.com/pulumi/pulumi-pulumiservice/blob/main/docs/v0-api-coverage.md). That file is auto-generated, so it stays in sync. Each `api/*` resource ships hand-maintained per-language examples in TypeScript, Python, Go, C#, Java, and YAML.

## What to know before adopting the preview

> The pulumiservice:api:* resource surface is in preview. Resource shape and module layout may change before GA.

1. **The existing `pulumiservice:index:*` resources remain supported.** They are not being deprecated as part of v1.0 and continue to be supported. Migration to `api/*` is opt-in via Pulumi `aliases`. There is no implicit v0 to api, by design.

## Try it

If you want to take the preview for a spin:

1. The [Pulumi Registry page for `pulumiservice`](/registry/packages/pulumiservice/) has install instructions for every language.
1. The [`examples/api/`](https://github.com/pulumi/pulumi-pulumiservice/tree/main/examples/api) directory has runnable programs for each resource, in every supported language.
1. The [`pulumi-pulumiservice` repo](https://github.com/pulumi/pulumi-pulumiservice) is open source if you want to read the runtime, the embedded spec, or the metadata file directly.

Feedback during preview is very beneficial.  Please open an issue [here](https://github.com/pulumi/pulumi-pulumiservice/issues) if you run into any problems.
