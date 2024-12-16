---
title_tag: Deployments | Self-Hosting Pulumi
meta_desc: Deployments are available on Self-hosting. Self-hosting is available as part of the Pulumi Business Critical Edition.
title: Deployments
h1: Pulumi Cloud self-hosted Deployments
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    cloud:
        name: Pulumi Deployments
        parent: pulumi-cloud-admin-self-hosted-components
        weight: 4
        identifier: pulumi-cloud-admin-self-hosted-components-deployments
aliases:
  - /docs/guides/self-hosted/components/deployments/
  - /docs/pulumi-cloud/self-hosted/components/deployments/
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the Self-Hosted Pulumi Cloud, sign up for the [30 day trial](/product/self-hosted#self-hosted-trial) or [contact us](/contact/).

To manage your state with a self-managed backend, such as a cloud storage bucket, see [State and Backends](/docs/concepts/state/).
{{% /notes %}}

[Pulumi Deployments](/docs/pulumi-cloud/deployments/) is fully supported in Kubernetes-managed self-hosted environments. If you're using Kubernetes to manage your self-hosted Pulumi Cloud installation, you can enable Pulumi Deployments features by configuring a Kubernetes-native deployment pool in Pulumi Cloud and installing one or more [customer-managed agents](/docs/pulumi-cloud/deployments/customer-managed-agents/) into your installation's Kubernetes cluster.

To do so, follow these steps:

1. Create a new deployment pool. Navigate to **Settings** then **Deployment runners** in the left-hand menu of your Pulumi Cloud organization, click **Add new pool**, and copy the generated access token.

1. Select the **Kubernetes** tab and follow the on-screen instructions to install and configure your Kubernetes-native deployment agent.

1. Set any environment variables directly on your Kubernetes deployment. The following environment variables are supported and may be set on the container running the Pulumi Cloud API service:

    | Variable Name                           | Description                            | Default         |
    |-----------------------------------------|-----------------------------------------| --------------- |
    | `PULUMI_DEPLOY_DEFAULT_IMAGE_REFERENCE` | The Docker image to use for the runner. | `pulumi/pulumi` |

1. Configure your stacks individually to use the deployment pool by navigating to **Settings > Deploy** and choosing the pool from the **Deployment runner pools** list. Click **Save deployment configuration** to apply your settings.
