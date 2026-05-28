---
title: "Generating a Pulumi Provider from an OpenAPI Spec"
date: 2026-05-28
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

Today, we are announcing v1.0 of the Pulumi Service Provider: a major milestone in managing Pulumi Cloud with Pulumi itself. The provider is now generated directly from the Pulumi Cloud OpenAPI specification, unlocking a dramatically expanded pulumiservice:api/* resource surface and enabling Pulumi Cloud capabilities to become available in the provider faster than ever before.

This release also brings several major new capabilities to infrastructure as code, including fine-grained RBAC as code, Pulumi IDP as code, and audit log export as IaC. Together, these changes make the Pulumi Service Provider the most powerful and extensible way yet to manage and automate your Pulumi Cloud infrastructure.

<!--more-->

## Why this matters for users

Historically, every new Pulumi Cloud feature implied a follow-up PR in the provider before that feature could be used from a Pulumi program. The provider was always slightly behind the API it wrapped, and entirely new capability areas could take months to land.

The `api/*` surface changes both timelines. Because the schema is derived from the OpenAPI spec at runtime:

1. Whole new resource families land in the provider the same release they reach Pulumi Cloud.
1. New fields, features, and enum values on existing resources show up across all five language SDKs the soon after they appear in the spec.

## What's new in v1.0

v1.0 lifts whole capability areas of Pulumi Cloud into the `api/*` surface, not just incremental field additions. None of it required bespoke provider code.

1. **Fine-grained RBAC as code.** Custom roles, organization membership, and team role assignments are now managed resources. For example, defining a read-only role and assigning it to a team:

    {{< chooser language "typescript,python,go,csharp,java,yaml" >}}
    {{% choosable language typescript %}}

```typescript
const readOnly = new ps.api.Role("readOnly", {
    orgName: "acme",
    name: "stack-reader",
    description: "Read-only access to stacks across the org.",
    uxPurpose: "role",
    details: {
        __type: "PermissionDescriptorAllow",
        permissions: ["stack:read", "stack:list"],
    },
});

new ps.api.teams.Role("readOnlyForPlatform", {
    orgName: "acme",
    teamName: "platform",
    roleID: readOnly.roleID,
});
```

    {{% /choosable %}}
    {{% choosable language python %}}

```python
read_only = pulumiservice.api.Role("readOnly",
    org_name="acme",
    name="stack-reader",
    description="Read-only access to stacks across the org.",
    ux_purpose="role",
    details={
        "__type": "PermissionDescriptorAllow",
        "permissions": ["stack:read", "stack:list"],
    })

pulumiservice.api.teams.Role("readOnlyForPlatform",
    org_name="acme",
    team_name="platform",
    role_id=read_only.role_id)
```

    {{% /choosable %}}
    {{% choosable language go %}}

```go
readOnly, _ := api.NewRole(ctx, "readOnly", &api.RoleArgs{
    OrgName:     pulumi.String("acme"),
    Name:        pulumi.String("stack-reader"),
    Description: pulumi.String("Read-only access to stacks across the org."),
    UxPurpose:   pulumi.String("role"),
    Details: pulumi.Map{
        "__type":      pulumi.String("PermissionDescriptorAllow"),
        "permissions": pulumi.StringArray{pulumi.String("stack:read"), pulumi.String("stack:list")},
    },
})

teams.NewRole(ctx, "readOnlyForPlatform", &teams.RoleArgs{
    OrgName:  pulumi.String("acme"),
    TeamName: pulumi.String("platform"),
    RoleID:   readOnly.RoleID,
})
```

    {{% /choosable %}}
    {{% choosable language csharp %}}

```csharp
var readOnly = new Ps.Api.Role("readOnly", new()
{
    OrgName = "acme",
    Name = "stack-reader",
    Description = "Read-only access to stacks across the org.",
    UxPurpose = "role",
    Details = ImmutableDictionary.CreateRange(new[]
    {
        new KeyValuePair<string, object>("__type", "PermissionDescriptorAllow"),
        new KeyValuePair<string, object>("permissions", new[] { "stack:read", "stack:list" }),
    }),
});

new Ps.Api.Teams.Role("readOnlyForPlatform", new()
{
    OrgName = "acme",
    TeamName = "platform",
    RoleID = readOnly.RoleID,
});
```

    {{% /choosable %}}
    {{% choosable language java %}}

```java
var readOnly = new Role("readOnly", RoleArgs.builder()
    .orgName("acme")
    .name("stack-reader")
    .description("Read-only access to stacks across the org.")
    .uxPurpose("role")
    .details(Map.of(
        "__type", "PermissionDescriptorAllow",
        "permissions", List.of("stack:read", "stack:list")))
    .build());

new com.pulumi.pulumiservice.api_teams.Role("readOnlyForPlatform",
    com.pulumi.pulumiservice.api_teams.RoleArgs.builder()
        .orgName("acme")
        .teamName("platform")
        .roleID(readOnly.roleID())
        .build());
```

    {{% /choosable %}}
    {{% choosable language yaml %}}

```yaml
resources:
  readOnly:
    type: pulumiservice:api:Role
    properties:
      orgName: acme
      name: stack-reader
      description: Read-only access to stacks across the org.
      uxPurpose: role
      details:
        __type: PermissionDescriptorAllow
        permissions:
          - stack:read
          - stack:list
  readOnlyForPlatform:
    type: pulumiservice:api/teams:Role
    properties:
      orgName: acme
      teamName: platform
      roleID: ${readOnly.roleID}
```

    {{% /choosable %}}
    {{< /chooser >}}

1. **Pulumi IDP as code.** `services:Service` makes the [Pulumi IDP](/docs/idp/) catalog manageable from your Pulumi programs, surfaced the same release IDP ships in Pulumi Cloud. Platform teams can publish service definitions as code rather than only through the IDP console.
1. **Audit-log export as IaC.** `AuditLogExportConfiguration` brings audit-log export sinks under Pulumi management with a real destroy path.

## How it works

Pulumi Cloud's OpenAPI document (published at <https://api.pulumi.com/api/openapi/pulumi-spec.json>) is embedded in the provider binary at build time, so the provider version you pin is the API surface you get. Preview and update are deterministic, and a version released today will still behave the same way years from now. Alongside the spec, the runtime loads a small companion metadata file that captures the Pulumi-specific semantics OpenAPI can't express: which endpoints pair into a single resource, what a resource's ID looks like, and which response fields are secrets that arrive exactly once at create time. That metadata is what lets `api/*` resources behave as expected.

Most of that metadata is auto-derived by a scaffolder, but the editorial layer, including resource descriptions, examples, and the v0 aliases that make migration safe, stays handmade. Any human override is pinned across regeneration so a future spec change can't quietly override it. The language SDKs are still generated against the runtime schema, so new fields and enum values reach typed SDKs in all five languages the moment the spec ships.

## What the api namespace covers

The `api` namespace already spans most of Pulumi Cloud's resource model.

For resources that have an ancestor under `pulumiservice:index:*`, the mapping lives in [`docs/v0-api-coverage.md`](https://github.com/pulumi/pulumi-pulumiservice/blob/main/docs/v0-api-coverage.md). That file is auto-generated, so it stays in sync. Each `api/*` resource ships hand-maintained per-language examples in TypeScript, Python, Go, C#, Java, and YAML.

## What to know before adopting the preview

> The pulumiservice:api:* resource surface is in preview. Resource shape and module layout may change before GA.

**The existing `pulumiservice:index:*` resources remain supported.** They are not being deprecated as part of v1.0 and continue to be supported. Migration to `api/*` is opt-in via Pulumi `aliases`.

## Try it

If you want to take the expanded provider for a spin:

1. The [Pulumi Registry page for `pulumiservice`](/registry/packages/pulumiservice/) has install instructions for every language.
1. The [`examples/api/`](https://github.com/pulumi/pulumi-pulumiservice/tree/main/examples/api) directory has runnable programs for each resource, in every supported language.
1. The [`pulumi-pulumiservice` repo](https://github.com/pulumi/pulumi-pulumiservice) is open source if you want to read the runtime, the embedded spec, or the metadata file directly.

Feedback during preview is very beneficial.  Please open an issue [here](https://github.com/pulumi/pulumi-pulumiservice/issues) if you run into any problems.
