---
title_tag: Deploy a Web Application to a Kubernetes Cluster
title: Web Application on Kubernetes
layout: template
schema_type: howto
meta_desc: Deploy a web application to an existing Kubernetes cluster with Pulumi in TypeScript, Python, Go, C#, or YAML.
meta_image: meta.png
card_desc: Deploy a web application to a Kubernetes cluster with Pulumi.
template:
  prefix: webapp-kubernetes
  dirname: my-k8s-app
  languages:
    - typescript
    - python
    - go
    - csharp
    - yaml
cloud:
  name: Web Application
  slug: web-application
---

The Kubernetes Web Application template scaffolds a Pulumi project that deploys a web application to an existing Kubernetes cluster using Pulumi's [Kubernetes provider](/registry/packages/kubernetes). The template creates a new namespace, a Deployment to run the application, and a Service that exposes it outside the cluster. It ships with placeholder app content so the project deploys end to end out of the box.

![An architecture diagram of the Kubernetes Web Application template](/templates/kubernetes-application/web-application/architecture.png)

## Using this template

To use this template, make sure you've already provisioned a [Kubernetes cluster](/templates/kubernetes), [installed Pulumi](/docs/install/) and [`kubectl`](https://kubernetes.io/docs/tasks/tools/install-kubectl/), and [configured your kubeconfig file](/registry/packages/kubernetes/installation-configuration#setup). Then create a new [project](/docs/iac/concepts/projects/) using the template in the language of your choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

The template requires no additional configuration. By default, it will deploy an Nginx container. Once the new project is created, you can deploy it with [`pulumi up`](/docs/iac/cli/commands/pulumi_up):

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output](/docs/iac/concepts/stacks/#outputs) values:

deploymentName
: The name of your new Kubernetes Deployment.

serviceName
: The name of your new Kubernetes Service.

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources.

## Customizing the project

Projects created with the Kubernetes Application template expose the following [configuration](/docs/iac/concepts/config/) settings:

namespace
: The name of the namespace to be created in your existing cluster. Defaults to `default`.

replicas
: The number of replicated Pods to be created in your new Deployment. Defaults to `1`.

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set):

```bash
$ pulumi config set replicas 3
$ pulumi up
```

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
