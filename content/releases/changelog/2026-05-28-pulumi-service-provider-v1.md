---
title: Pulumi Service Provider v1.0
date: 2026-05-28
aliases:
    - /releases/changelog/pulumi-service-provider-v1/
meta_desc: The Pulumi Service Provider has reached v1.0 and is now generated from the public Pulumi Cloud OpenAPI specification.
authors:
    - christian-nunciato
---

The [Pulumi Service Provider](/registry/packages/pulumiservice/) has officially [reached v1.0](/blog/generating-a-pulumi-provider-from-an-openapi-spec/#whats-new-in-v10) and is now generated from the public Pulumi Cloud [OpenAPI specification](/docs/reference/cloud-rest-api/), which commits to a stable contract for the existing resource surface and keeps the provider up to date automatically.

This release also adds:

* Fine-grained RBAC as code
* Pulumi IDP (internal developer platform) as code
* Audit-log export as code

The release is live on [npm](https://www.npmjs.com/package/@pulumi/pulumiservice), [PyPI](https://pypi.org/project/pulumi-pulumiservice/), [NuGet](https://www.nuget.org/packages/Pulumi.PulumiService), [Maven Central](https://central.sonatype.com/artifact/com.pulumi/pulumiservice), and [pkg.go.dev](https://pkg.go.dev/github.com/pulumi/pulumi-pulumiservice).

To learn more about this release, read the [announcement post](/blog/generating-a-pulumi-provider-from-an-openapi-spec/#whats-new-in-v10), and check out the provider's documentation in the [Pulumi Registry](/registry/packages/pulumiservice/). See the [v1.0.0 release notes](https://github.com/pulumi/pulumi-pulumiservice/releases/tag/v1.0.0) for additional details.
