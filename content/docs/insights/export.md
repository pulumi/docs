---
title: Data export
title_tag: Data export | Pulumi Insights
h1: Data export
meta_desc: Documentation and schema for the Pulumi Insights CSV Data Export feature.
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  insights:
    parent: insights-home
    weight: 60
aliases:
  - /docs/intro/insights/export/
  - /docs/pulumi-cloud/insights/export/
---

Pulumi Insights data export allows you to export any set of Pulumi Insights search results to a CSV file. You can, in turn, use this CSV file to join to any external data in a data warehouse, perform ETL transforms, etc.

There are two ways to perform a data export:

1. Point-and-click, via the Pulumi Cloud web UI, by clicking the Export CSV menu item:

    ![a screenshot of the Pulumi Cloud web UI showing the drop-down for Pulumi Insights results and the Export CSV command highlighted](../assets/data-export-pulumi-cloud-ui.png)

1. Programmatically, by calling the [Pulumi Cloud REST API](/docs/pulumi-cloud/reference/cloud-rest-api/#data-export)

## CSV Format

The CSV (comma separated values) format is composed of the following fields:

```plain
created, custom, delete, id, modified, module, name, package, parent_urn, pending, project, protected, provider_urn, stack, type, urn, teams, properties, category
```

| Field        | Description                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------ |
| created      | The UTC time when the resource was created.                                                                        |
| custom       | Whether the resource is a CustomResource.                                                                          |
| delete       | Whether the resource is marked for deletion in the next update.                                                    |
| id           | The physical name of the resource, as assigned by the resource's provider.                                         |
| modified     | The UTC time when the resource's state was last modified during an update, refresh or import.                      |
| module       | The module component of the resource's type. This is `s3` for a resource of type `aws:s3/bucketv2:BucketV2`.       |
| name         | The logical name of the resource. Typically the first parameter provided to the resource when it was instantiated. |
| package      | The package component of the resource's type. This is `aws` for a resource of type `aws:s3/bucketv2:BucketV2`.     |
| parent_urn   | The URN of the resource's parent, if it has one.                                                                   |
| pending      | The state of the resource if it is pending. Typically indicates an operation that was interrupted due to an error. |
| project      | The project the resource belongs to.                                                                               |
| protected    | Whether the resource is protected from deletion.                                                                   |
| provider_urn | The URN of the resource's provider.                                                                                |
| stack        | The stack the resource belongs to.                                                                                 |
| type         | The type of the resource.                                                                                          |
| urn          | The URN of the resource.                                                                                           |
| teams        | The teams that have access to this resource                                                                       |
| properties   | The metadata properties of this resource                                                                    |
| category     | The category this resource is a part of                                                                        |

See the [API specification](/docs/pulumi-cloud/cloud-rest-api/#data-export) for a more complete description of what these fields represent.
