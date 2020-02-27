---
title: "Announcing Pulumi 0.15"
date: "2018-08-15"
meta_desc: "Pulumi can now deploy and manage Kubernetes resources using the same familiar programming model supported for AWS, Azure, and Google Cloud Platform."
authors: ["luke-hoban"]
tags: ["Pulumi", "New-Features", "CI/CD"]
---


Just over a month ago we publicly launched
Pulumi, a new cloud native development
platform.  The response has been overwhelming and we've been hard at
work responding to your feedback ever since.

Today, we are excited to release [Pulumi 0.15](https://github.com/pulumi/pulumi/blob/master/CHANGELOG.md#0150-2018-08-13) and make
it [available to download]({{< relref "/docs/get-started/install" >}}).  This release
includes improvements across the entire Pulumi development experience.
Pulumi supports more platforms
([Kubernetes]({{< relref "/docs/get-started/kubernetes" >}}) and
[OpenStack]({{< relref "/docs/intro/cloud-providers/openstack" >}})), is faster
(Parallelism, simpler (native
TypeScript support), richer
(serverless frameworks for Azure and
GCP),  and is more deeply
integrated into the application lifecycle
([GitHub App for CI/CD integration]({{< relref "/docs/guides/continuous-delivery/github-app" >}})).

In this post, we'll take a quick tour of these new features. Stay tuned
for follow up blog posts to dive deeper into individual topics.

## Kubernetes

Pulumi can now deploy and manage Kubernetes resources using the same
familiar programming model supported for AWS, Azure, and Google Cloud
Platform. It's also possible to mix resources from multiple clouds in
the same program, such as using an S3 Bucket or RDS database from your
Kubernetes-managed containers.

This release includes dozens of features that make it simple and
productive to create and manage Kubernetes applications and resources
and to perform production-grade deployments.  The `@pulumi/kubernetes`
package provides access to the full Kubernetes API, ensuring you can
deploy any Kubernetes application with Pulumi.

New support for `new helm.v2.Chart(...)` allows deploying existing
[Helm](https://helm.sh/) charts via Pulumi, ensuring you can coordinate
deployment of charts as part of a larger Pulumi deployment.

Complex Kubernetes resources (like Deployments and Services) also
provide rich status updates so that you have complete visibility into
the state of a deployment while it is in progress, including incremental
progress reporting, and significant work was put into making it easy to
diagnose and robustly recover from deployment failures.

The Pulumi Kubernetes provider can be used to deploy to any Kubernetes
cluster, whether cloud hosted (EKS, AKS, GKE) or local (Minikube, Docker
for Mac) or on-premise.  And because Pulumi is already great at
deploying cloud resources, the Pulumi Kubernetes provider can be
combined with, for example, the Pulumi Azure provider to deploy and
manage both the cluster and Kubernetes resources that should be
installed into the cluster.

```typescript
import * as azure from "@pulumi/azure";
import * as k8s from "@pulumi/kubernetes";
import * as helm from "@pulumi/kubernetes/helm";

// Create an Azure Kubernetes Service cluster
const resourceGroup = new azure.core.ResourceGroup("aks", { location: "West US" });
const kubernetesService = new azure.containerservice.KubernetesCluster("kubernetes", {
/* ... */
});

// Create a Pulumi Kubernetes provider configured to deploy to the AKS cluster above
export const azk8s = new k8s.Provider("azk8s", {
    kubeconfig: kubernetesService.kubeConfigRaw,
});

// Deploy a Helm chart into the cluster
const kibana = new helm.v2.Chart("kibana", {
    repo: "stable",
    chart: "kibana",
    version: "0.8.0",
    values: { service: { type: "LoadBalancer" } },
}, { providers: { kubernetes: azk8s } });
```

Check out the [Kubernetes
overview]({{< relref "/docs/get-started/kubernetes" >}}) docs, the [API
documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/kubernetes" >}})
and the [pulumi-kubernetes](https://github.com/pulumi/pulumi-kubernetes)
GitHub project for additional details.

## Parallelism

Pulumi now runs deployments in parallel by default. To accomplish this,
the Pulumi engine tracks all dependencies across cloud resources in your
program, maximizing the amount of work that can proceed in parallel,
while also ensuring all resource are created, updated, replaced, or
destroyed in the correct order.

In some extreme cases, this new parallelism support can improve
performance by 2-10x, but even more importantly, parallelism provides a
performance boost for practically every Pulumi deployment.

## First Class Providers

Pulumi programs can now create multiple instances of a resource
provider, and can initialize an instance of a resources provider using
outputs of other resources.

For example, a Pulumi program can now deploy resources into multiple AWS
regions by creating providers targeting each region. This can be used
for resources that must be deployed in a certain region (e.g.
Lambda@Edge or ACM certificates), or just for managing multi-region
deployments from a single Pulumi program.

This also enables scenarios where a Pulumi program deploys some base
infrastructure, and then wants to manage resources deployed on top of
that using a different provider. For example, deploy a GKE cluster, and
then configure a Kubernetes provider to deploy Kubernetes resources on
top of the cluster. Or even then deploy OpenFaaS into the Kubernetes
cluster, and use the Pulumi OpenFaaS provider to deploy functions.

You might have already noticed, however we already used this feature in
the Kubernetes example earlier!

## Native TypeScript Support

Pulumi has supported JavaScript since inception, and as a result, it's
been possible to use Pulumi via TypeScript to get the benefits of
earlier error checking and richer tooling for cloud infrastructure and
application development. However, TypeScript code had to previously be
manually compiled to JavaScript prior to doing a Pulumi deployment,
which added some friction for users who wanted to use TypeScript with
Pulumi.

In this release, Pulumi now natively supports TypeScript, so you do not
need to run `tsc` explicitly before deploying. (We often forget to do
this too!) Simply run `pulumi up`, and the program will be recompiled on
the fly before running it.

New templates are now available via `pulumi new` which use the new,
simpler, TypeScript support.

## Using Imports from Runtime Functions

Pulumi supports creating cloud functions (Lambdas, Azure Functions,
Google Cloud Functions) using JavaScript callbacks in your Pulumi
application. This provides a nice and simple way to write the little
pieces of code that you need to integrate into your cloud application
and version with your infrastructure using real functions.

We heard feedback from early adopters who wanted to be able to import
NPM packages in their Pulumi program more easily, and then use them
within one of these cloud functions. We've enabled this now, so that the
common way of structuring code works as expected, and so that writing
idiomatic JavaScript or TypeScript "just works."

For example, the code below uses the `axios` NPM package to make an HTTP
request inside an AWS Lambda invoked by an AWS API Gateway (in just a
few lines of code!).

```typescript
import * as axios from "axios";
import * as cloud from "@pulumi/cloud-aws";

const api = new cloud.API("api");
api.get("/", async (req, res) => {
    const statusText = (await axios.default.get("https://www.pulumi.com")).statusText;
    res.write(`GET https://www.pulumi.com/ == ${statusText}`).end();
});

export const url = api.publish().url;
```

## OpenStack

Thanks to a contribution by Fraser Waters
([@Frassle](https://github.com/Frassle)), Pulumi now also supports
OpenStack. This allows users targeting an OpenStack API from their
public or private cloud provider to use Pulumi to author and manage
infrastructure deployments.

For example, a VM can be deployed to OVH with just the following:

```typescript
const os = require("@pulumi/openstack");
const instance = new os.compute.Instance("test", {
    flavorName: "s1-2",
    imageName: "Ubuntu 16.04",
});

exports.instanceIP = instance.accessIpV4;
```

Check out the [API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/openstack" >}})
and the [pulumi-openstack](https://github.com/pulumi/pulumi-openstack)
GitHub project for additional details. Huge thanks to Fraser for his
work on this!

## Serverless Functions in GCP and Azure

Particularly with serverless functions being real functions, we had a
lot of interest in broadening our existing support beyond [just AWS
serverless](https://github.com/pulumi/pulumi-aws-serverless).  We are
happy to announce better serverless functionality for GCP and Azure.

On Azure, the new `@pulumi/azure-serverless` package makes it easy to
work with serverless functions, and has initial support for hooking up
to Blob storage event sources:

```typescript
import * as azure from "@pulumi/azure";
import * as serverless from "@pulumi/azure-serverless";

const storageAccount = new azure.storage.Account("images-container", { /* ... */ });
serverless.storage.onBlobEvent("newImage", storageAccount, (context, blob) => {
    context.log(context);
    context.log(blob);
    context.done();
}, { containerName: "folder", filterSuffix: ".png" });

export let storageAccountName = storageAccount.name;
```

On Google Cloud, the new `gcp.serverless.Function` provides an easy way
to create a Google Cloud Function from a JavaScript callback in a Pulumi
program. Thanks to Mikhail Shilkov
([@mikhailshilkov](https://github.com/mikhailshilkov)) for contributing
this feature!

```typescript
import * as gcp from "@pulumi/gcp";
let f = new gcp.serverless.Function("f", {}, (req, res) => {
    res.send(`Hello ${req.body.name || 'World'}!`);
});

export let url = f.function.httpsTriggerUrl;
```

## GitHub App for CI/CD Integration

Pulumi already works with [your favorite CI/CD systems]({{< relref "/docs/guides/continuous-delivery" >}})
to accomplish automated
and continuous deployments of cloud infrastructure and applications.
This is how Pulumi deploys and manages our own infrastructure that runs
<pulumi.com>, and is how our most engaged users adopt
Pulumi in their own teams.

Our mission is to make Pulumi the easiest way to get code to the cloud.
To that end, we are launching a new [Pulumi GitHub
App](https://github.com/apps/pulumi) which bridges the gap between
GitHub (source code, pull requests) and Pulumi (cloud resources, stack
updates).  By installing the Pulumi GitHub App into your GitHub
organization , and then running Pulumi as part of your existing CI/CD
process, you will receive integrated stack updates and previews in your
pull requests. This allows you to see the potential impact a change
would have on your cloud infrastructure before merging the code, and
collaborate with your teammates when deploying application and
infrastructure changes.

The Pulumi GitHub App is still in preview as we work to support more CI
systems and extend its capabilities. For information on how to install
it and configure it with your CI system, please [read the
documentation]({{< relref "/docs/guides/continuous-delivery/github-app" >}}).

## Summary

We're excited about all the new features in this release and the new
scenarios they enable for the Pulumi community . If you are new to
Pulumi, [download the tools and get started
today]({{< relref "/docs/get-started" >}}), or [join us in Slack](https://slack.pulumi.com). A big thanks to all the users and
contributors who have helped shape this release -- we can't wait to see
what you build next !

### Special Thanks

- Fraser Waters
  ([@Frassle](https://github.com/pulls?utf8=%E2%9C%93&q=is%3Apr+author%3AFrassle+archived%3Afalse+user%3Apulumi+is%3Aclosed+))
- Mikhail Shilkov
  ([@mikhailshilkov](https://github.com/pulls?q=is%3Apr+author%3Amikhailshilkov+archived%3Afalse+user%3Apulumi+is%3Aclosed))
- James Nugent
  ([@jen20](https://github.com/pulls?utf8=%E2%9C%93&q=is%3Apr+author%3Ajen20+archived%3Afalse+user%3Apulumi+is%3Aclosed+))
- Thomas Schersach
  ([@Tirke](https://github.com/pulls?utf8=%E2%9C%93&q=is%3Apr+author%3Atirke+archived%3Afalse+user%3Apulumi+is%3Aclosed+))
- JT
  ([@Jtango18](https://github.com/pulls?utf8=%E2%9C%93&q=is%3Apr+author%3Ajtango18+archived%3Afalse+user%3Apulumi+is%3Aclosed+))
- Itay Maman
  ([@imaman](https://github.com/pulls?utf8=%E2%9C%93&q=is%3Apr+author%3Aimaman+archived%3Afalse+user%3Apulumi+is%3Aclosed+))
