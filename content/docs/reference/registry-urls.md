---
title_tag: Registry URL Reference
meta_desc: Reference documentation for Pulumi Registry URLs used to reference templates and packages.
title: Registry URL reference
h1: Pulumi Registry URL reference
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    reference:
        name: Registry URLs
        parent: reference-home
        weight: 5
---

Pulumi uses `registry://` URLs to reference resources in the Pulumi Registry, such as templates and packages. This page documents the URL format and usage.

## URL format

```
registry://{resource-type}/{source}/{publisher}/{name}[@{version}]
```

| Component       | Description                                                              |
|-----------------|--------------------------------------------------------------------------|
| `resource-type` | The type of resource: `templates` or `packages`.                         |
| `source`        | The registry source or namespace (e.g., `pulumi`).                       |
| `publisher`     | The organization that published the resource.                            |
| `name`          | The resource name.                                                       |
| `version`       | **Optional.** Semver version. If omitted, the latest version is used.    |

## Templates

Reference templates published to the Pulumi Registry:

```
registry://templates/{source}/{publisher}/{name}[@{version}]
```

Examples:

```
registry://templates/pulumi/community/aws-static-website@1.0.0
registry://templates/pulumi/official/kubernetes-cluster
```

Templates are used in [deployment settings](/docs/deployments/deployments/using/settings/) to configure where Pulumi Deployments obtains source code. See [Organization templates](/docs/idp/concepts/organization-templates/) for more information on publishing and managing templates.

## Versioning

- **Specific version:** Append `@{version}` to pin to a specific semver version (e.g., `@1.0.0`, `@2.1.0-beta.1`)
- **Latest version:** Omit the version to use the latest published version

When omitting the version, the latest version is resolved at the time of use. For reproducible deployments, specify an explicit version.
