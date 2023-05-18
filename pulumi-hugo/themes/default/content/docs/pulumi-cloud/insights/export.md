---
title_tag: "Pulumi Insights: Data export"
meta_desc: Documentation and schema for the Pulumi Insights CSV Data Export feature.
title: Data export
h1: Data export
menu:
  pulumicloud:
    parent: insights
    weight: 2
aliases:
  - /docs/intro/insights/export/
---

## CSV Format

The CSV (comma separated values) format is composed of the following fields:

```
created, custom, delete, id, modified, module, name, package, parent_urn, pending, project, protected, provider_urn, stack, type, urn
```

| Field        | Description                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| created      | The UTC time when the resource was created.                                                                        |
| custom       | Whether the resource is a CustomResource.                                                                          |
| delete       | Whether the resource is marked for deletion in the next update.                                                    |
| id           | The physical name of the resource, as assigned by the resource's provider.                                         |
| modified     | The UTC time when the resource's state was last modified during an update, refresh or import.                      |
| module       | The module component of the resource's type. This is `s3` for a resource of type `aws:s3/bucket:Bucket`.           |
| name         | The logical name of the resource. Typically the first parameter provided to the resource when it was instantiated. |
| package      | The package component of the resource's type. This is `aws` for a resource of type `aws:s3/bucket:Bucket`.         |
| parent_urn   | The URN of the resource's parent, if it has one.                                                                   |
| pending      | The state of the resource if it is pending. Typically indicates an operation that was interrupted due to an error. |
| project      | The project the resource belongs to.                                                                               |
| protected    | Whether the resource is protected from deletion.                                                                   |
| provider_urn | The URN of the resource's provider.                                                                                |
| stack        | The stack the resource belongs to.                                                                                 |
| type         | The type of the resource.                                                                                          |
| urn          | The URN of the resource.                                                                                           |

See the [API specification](/docs/pulumi-cloud/cloud-rest-api/#data-export) for a more complete description of what these fields represent.
