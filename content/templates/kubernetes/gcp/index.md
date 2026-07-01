---
title_tag: Deploy a Managed Kubernetes Cluster to Google Cloud
title: Kubernetes Cluster on Google Cloud
layout: template
schema_type: howto
meta_desc: Deploy a managed Kubernetes cluster on Google Cloud with Pulumi and Google Kubernetes Engine (GKE) in TypeScript, Python, Go, C#, YAML, or HCL.
meta_image: meta.png
card_desc: Deploy a Kubernetes cluster on Google Cloud with Pulumi and Google Kubernetes Engine (GKE).
template:
  prefix: kubernetes-gcp
  dirname: my-k8s-cluster
  languages:
    - typescript
    - python
    - go
    - csharp
    - yaml
    - hcl
cloud:
  name: Google Cloud
  slug: gcp
---

The Google Cloud Kubernetes Cluster template scaffolds a Pulumi project that provisions a managed [Google Kubernetes Engine (GKE) cluster](/registry/packages/gcp/api-docs/container/cluster) and a [node pool](/registry/packages/gcp/api-docs/container/nodepool) inside a new [VPC network](/registry/packages/gcp/api-docs/compute/network) with a [subnet](/registry/packages/gcp/api-docs/compute/subnetwork). Worker nodes are deployed with private IP addresses for improved security.

![An architecture diagram of the Google Cloud Kubernetes Cluster template](/templates/kubernetes/gcp/architecture.png)

## Using this template

To use this template to deploy your own Kubernetes cluster, make sure you've [installed Pulumi](/docs/install/) and [configured your Google Cloud credentials](/registry/packages/gcp/installation-configuration#credentials), then create a new [project](/docs/iac/concepts/projects/) using the template in the language of your choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

{{% choosable language "typescript,python,go,csharp,yaml" %}}

You must supply an existing Google Cloud project ID to deploy the cluster. You can input it through the new-project wizard. Once the project is created, you can deploy it with [`pulumi up`](/docs/iac/cli/commands/pulumi_up):

{{% /choosable %}}

{{% choosable language hcl %}}

The template deploys into your active Google Cloud project (read from your gcloud credentials) and defaults to the `us-central1` region, which you can change with the `region` setting. Once the new project is created, you can deploy it with [`pulumi up`](/docs/iac/cli/commands/pulumi_up):

{{% /choosable %}}

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output](/docs/iac/concepts/stacks/#outputs) values:

{{% choosable language "typescript,python,go,csharp,yaml" %}}

networkName
: The name of the VPC network containing the Kubernetes cluster resources.

networkId
: The unique ID of the VPC network containing the Kubernetes cluster resources.

clusterName
: The name of the GKE cluster.

clusterId
: The unique ID of the GKE cluster.

kubeconfig
: The cluster's kubeconfig file, which you can use with `kubectl` to access and communicate with your cluster.

{{% /choosable %}}

{{% choosable language hcl %}}

network_name
: The name of the VPC network containing the Kubernetes cluster resources.

cluster_name
: The name of the GKE cluster.

kubeconfig
: The cluster's kubeconfig file, which you can use with `kubectl` to access and communicate with your cluster.

{{% /choosable %}}

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources.

## Customizing the project

Projects created with the Kubernetes Cluster template expose the following [configuration](/docs/iac/concepts/config/) settings:

{{% choosable language "typescript,python,go,csharp,yaml" %}}

gcp:project
: The Google Cloud project ID to deploy into.

gcp:region
: The Google Cloud region to deploy into. Defaults to `us-central1`.

nodesPerZone
: The desired number of nodes per zone in the node pool. Defaults to `1`.

{{% /choosable %}}

{{% choosable language hcl %}}

region
: The Google Cloud region to deploy into. Defaults to `us-central1`.

nodes_per_zone
: The desired number of nodes per zone in the node pool. Defaults to `1`.

{{% /choosable %}}

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set):

{{% choosable language "typescript,python,go,csharp,yaml" %}}

```bash
$ pulumi config set nodesPerZone 2
$ pulumi up
```

{{% /choosable %}}

{{% choosable language hcl %}}

```bash
$ pulumi config set nodes_per_zone 2
$ pulumi up
```

{{% /choosable %}}

## Cleaning up

You can cleanly destroy the stack and all of its infrastructure with [`pulumi destroy`](/docs/iac/cli/commands/pulumi_destroy):

```bash
$ pulumi destroy
```

## Learn more

* Browse other architecture templates in the [Templates gallery](/templates).
* Explore the [Google Cloud provider API docs](/registry/packages/gcp) in the Pulumi Registry.
* Walk through Pulumi from the ground up in [Pulumi Tutorials](/tutorials/).
* Read the latest [Google Cloud posts on the Pulumi blog](/blog/tag/google-cloud).
