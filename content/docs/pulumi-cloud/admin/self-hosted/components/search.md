---
title_tag: Resource Search Cluster | Self-Hosting Pulumi
meta_desc: An OpenSearch cluster is required for Resource Search features. Self-hosting
  is available as part of the Pulumi Business Critical Edition.
title: OpenSearch cluster
h1: Pulumi Cloud self-hosted OpenSearch cluster
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: OpenSearch cluster
    parent: pulumi-cloud-admin-self-hosted-components
    weight: 3
    identifier: pulumi-cloud-admin-self-hosted-components-search
aliases:
  - /docs/guides/self-hosted/components/search/
  - /docs/pulumi-cloud/self-hosted/components/search/
search:
  keywords:
    - OpenSearch
    - cluster
    - OpenSearch cluster
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the Self-Hosted Pulumi Cloud, sign up for the [30 day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).

To manage your state with a self-managed backend, such as a cloud storage bucket, see [State and Backends](/docs/concepts/state/).
{{% /notes %}}

Pulumi Cloud provides resource search features that require an OpenSearch cluster. Self-hosted installations require a compatible OpenSearch cluster and changes to the API container configuration to enable these features.

When the service container is launched with a valid search configuration, it will connect to the OpenSearch cluster and automatically index any existing resources managed by the self-hosted Pulumi installation.
If the OpenSearch cluster is not reachable, then the Pulumi Console will display an error message on the Resources page indicating that the search cluster is unavailable, but will otherwise operate normally.
It is important to note that the search cluster is not in the critical path of Pulumi operations, so an unavailable search cluster will not prevent users from updating Pulumi stacks, and search data can be backfilled easily once the search cluster is available.

## Prerequisites

* Provide a compatible OpenSearch cluster (see Minimum System Requirements below).
* Update the API container to set environment variables for the OpenSearch cluster.

## Minimum System Requirements

| Type       | Properties   | Notes                                                                                                                                                                                                                                                                 |
|------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OpenSearch | v2.x cluster | Pulumi Cloud has been tested with OpenSearch v2.9 and v2.11                                                                                                                                                                                                           |

## API Environment Variables

The following environment variables must be set on the API container for Pulumi Cloud.

| Variable Name          | Description                                                 |
|------------------------|-------------------------------------------------------------|
| PULUMI_SEARCH_DOMAIN   | The URL of the OpenSearch cluster API, including the port.  |
| PULUMI_SEARCH_USER     | The administrator user for the OpenSearch cluster.          |
| PULUMI_SEARCH_PASSWORD | The administrator password for the OpenSearch cluster.      |

## OpenSearch Cluster Administration

### Index Rotation

The Pulumi service automatically triggers the OpenSearch cluster to reindex resource search results on a weekly basis.

### Backfilling Data

If a reindex operation is needed outside the normal weekly rotation, users with an `admin` role in a self-hosted
organization have access to a menu under `Settings -> Self-hosted`. This menu contains a `Reindex search cluster`
button to manually trigger a backfill/reindex operation for the OpenSearch cluster.

It can be useful to run a manual backfill when an OpenSearch cluster is first added to the Pulumi service configuration,
or to bring things back in sync in case of operational issues. The backfill operation iterates over all Pulumi stacks, finds their latest checkpoints, and indexes the resources.
It will also ensure any soft-deleted stacks do not have resources in the search index. As a rule of thumb, if there are every any serious issues with the cluster -- indexing is broken or delayed, the cluster is wiped out, etc. -- it's always safest and easiest to rebuild the search data from scratch using this command.
