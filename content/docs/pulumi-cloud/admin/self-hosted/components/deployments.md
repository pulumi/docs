---
title_tag: Deployments | Self-Hosting Pulumi
meta_desc: Deployments are available on Self-hosting. Self-hosting is available as part of the Pulumi Business Critical Edition.
title: Deployments
h1: Pulumi Cloud self-hosted Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    cloud:
        name: Deployments
        parent: pulumi-cloud-admin-self-hosted-components
        weight: 1
        identifier: pulumi-cloud-admin-self-hosted-components-deployments
    pulumicloud:
        parent: self-hosted-components
        weight: 1
aliases:
  - /docs/guides/self-hosted/components/deployments/
  - /docs/pulumi-cloud/self-hosted/components/deployments/
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the Self-Hosted Pulumi Cloud, sign up for the [30 day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).

To manage your state with a self-managed backend, such as a cloud storage bucket, see [State and Backends](/docs/concepts/state/).
{{% /notes %}}

Pulumi Cloud provides deployments features that require an agnent. Self-hosted installations allow you to run the agent in the same kubernetes cluster using the Pulumi program located [here](https://github.com/pulumi/customer-managed-deployment-agent/tree/main/kubernetes).

For Google Cloud Service Accounts are supported with the Pulumi worker pods.

<!-- ## Prerequisites

* Provide a compatible OpenSearch cluster (see Minimum System Requirements below).
* Update the API container to set environment variables for the OpenSearch cluster.

## Minimum System Requirements

| Type       | Properties   | Notes                                                                                                                                                                                                                                                                 |
|------------|--------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OpenSearch | v2.x cluster | Pulumi Cloud has been tested with OpenSearch v2.9 and v2.11                                                                                                                                                                                                           | -->

## API Environment Variables

The following environment variables can be set on the API container for Pulumi Cloud.

| Variable Name                           | Description                                |
|-----------------------------------------|--------------------------------------------|
| PULUMI_DEPLOY_DEFAULT_IMAGE_REFERENCE   | The custom image for the pulumi worker     |
