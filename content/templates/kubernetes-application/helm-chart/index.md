---
title_tag: Deploy a Helm Chart to a Kubernetes Cluster
title: Helm Chart on Kubernetes
layout: template
schema_type: howto
meta_desc: Deploy a Helm chart to an existing Kubernetes cluster with Pulumi in TypeScript, Python, Go, C#, YAML, or HCL.
meta_image: meta.png
card_desc: Deploy a Helm chart to a Kubernetes cluster with Pulumi.
template:
  prefix: helm-kubernetes
  dirname: my-k8s-app
  languages:
    - typescript
    - python
    - go
    - csharp
    - yaml
    - hcl
cloud:
  name: Helm Chart
  slug: helm-chart
---

The Helm Chart template scaffolds a Pulumi project that deploys a [Helm chart](/registry/packages/kubernetes/api-docs/helm/v3) to an existing Kubernetes cluster using Pulumi's [Kubernetes provider](/registry/packages/kubernetes). The template creates a new namespace in the cluster and installs an Nginx ingress controller as the default chart, so the project deploys end to end out of the box.

![An architecture diagram of the Helm Chart template](/templates/kubernetes-application/helm-chart/architecture.png)

## Using this template

To use this template, make sure you've already provisioned a [Kubernetes cluster](/templates/kubernetes), [installed Pulumi](/docs/install/) and [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/), and [configured your kubeconfig file](/registry/packages/kubernetes/installation-configuration#setup). Then create a new [project](/docs/iac/concepts/projects/) using the template in the language of your choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

The template requires no additional configuration. By default, it will install an Nginx ingress controller with Helm. Once the new project is created, you can deploy it with [`pulumi up`](/docs/iac/cli/commands/pulumi_up):

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output](/docs/iac/concepts/stacks/#outputs) values:

name
: The name of your new Helm chart deployment.

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources.

## Customizing the project

Projects created with the Helm Chart template expose the following [configuration](/docs/iac/concepts/config/) settings:

{{% choosable language "typescript,python,go,csharp,yaml" %}}

k8sNamespace
: The name of the namespace to be created in your existing cluster. Defaults to `nginx-ingress`.

{{% /choosable %}}

{{% choosable language hcl %}}

k8s_namespace
: The name of the namespace to be created in your existing cluster. Defaults to `nginx-ingress`.

{{% /choosable %}}

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set):

{{% choosable language "typescript,python,go,csharp,yaml" %}}

```bash
$ pulumi config set k8sNamespace my-namespace
$ pulumi up
```

{{% /choosable %}}

{{% choosable language hcl %}}

```bash
$ pulumi config set k8s_namespace my-namespace
$ pulumi up
```

{{% /choosable %}}

You can customize the Helm chart by passing values to it in your Pulumi code. An example of passing a few values to the chart is included in the template for reference.

## Cleaning up

You can cleanly destroy the stack and all of its infrastructure with [`pulumi destroy`](/docs/iac/cli/commands/pulumi_destroy):

```bash
$ pulumi destroy
```

## Learn more

* Browse other architecture templates in the [Templates gallery](/templates).
* Explore the [Kubernetes provider API docs](/registry/packages/kubernetes) in the Pulumi Registry.
* Walk through Pulumi from the ground up in [Pulumi Tutorials](/tutorials/).
* Read the latest [Kubernetes posts on the Pulumi blog](/blog/tag/kubernetes).
