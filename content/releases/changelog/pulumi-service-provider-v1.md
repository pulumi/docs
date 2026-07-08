---
title: Pulumi Service Provider v1.0
date: 2026-05-20
meta_desc: "The Pulumi Service Provider reaches v1.0, generated from the public Pulumi Cloud OpenAPI spec, with new RBAC-as-code and StackTags resources."
---

The Pulumi Service Provider reaches v1.0, now generated from the public Pulumi Cloud OpenAPI specification — which commits to a stable contract for the existing resource surface and keeps the provider up to date automatically. The release adds RBAC-as-code with new `OrganizationRole`, `OrganizationMember`, and `TeamRoleAssignment` resources plus helper data sources for common permission-scoping patterns, and a `StackTags` resource for managing multiple stack tags as one resource. The release is live on npm, PyPI, NuGet, Maven, and Go modules.

See the [package in the registry](/registry/packages/pulumiservice/) or the [v1.0.0 release notes](https://github.com/pulumi/pulumi-pulumiservice/releases/tag/v1.0.0).
