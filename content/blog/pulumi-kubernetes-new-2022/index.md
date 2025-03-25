---
date: "2022-10-23"
title: "Pulumi+Kubernetes: New Flux Integration and Inline Programs"
authors: ["luke-hoban", "michael-bridgen"]
tags: ["Kubernetes", "Continuous-Delivery", "operators"]
meta_desc: "Pulumi Kubernetes Operator v1.10, New Pulumi Provider for Flux, Pulumi
  Kubernetes Provider v3.22"
meta_image: meta.png
search:
  keywords:
    - kubernetes
    - flux
    - inline
    - operator
    - programs
    - integration
    - '22'
---

Pulumi’s Universal Infrastructure as Code platform works with all major clouds and over 100 cloud and SaaS providers, but among all its uses one of the most important is the ability to bring rich Infrastructure as Code tools and practices to Kubernetes projects and teams.

Kubernetes is one of the most used platforms in Pulumi, second only to AWS, with thousands of organizations using Pulumi to manage clusters at scale.  Pulumi supports a wide variety of use cases around Kubernetes - from cluster creation and management, to rich and expressive workload definition, to continuous delivery and infrastructure GitOps.

<!--more-->

{{% notes type="info" %}}
Check out version 2.0 of the [Pulumi Kubernetes Operator](/blog/pulumi-kubernetes-operator-2-0/).
{{% /notes %}}

Today we are announcing a set of major updates which deepen and extend Pulumi’s support for Kubernetes and the Kubernetes ecosystem. In this post, we’ll highlight a few of these exciting enhancements:

* [Pulumi Kubernetes Operator v1.10](https://github.com/pulumi/pulumi-kubernetes-operator/#readme): New integration with Flux for richer GitOps support, and ability to deploy Pulumi stacks from directly within the Kubernetes resource model
* [New Pulumi Provider for Flux](https://www.pulumi.com/registry/packages/flux/): Manage Flux with Infrastructure as Code
* [Pulumi Kubernetes Provider v3.22](https://www.pulumi.com/registry/packages/kubernetes/): Server Side Apply and Resource Patch

You can [learn more about Pulumi and Kubernetes](https://www.pulumi.com/registry/packages/kubernetes/) or jump in and [get started](https://www.pulumi.com/docs/iac/get-started/kubernetes/) right away, or read on to learn more about what’s new for Pulumi and Kubernetes!

## Pulumi Kubernetes Operator v1.10: Flux Integration and Inline Infrastructure support

The Pulumi Kubernetes Operator provides a cloud-native way to manage and deploy cloud infrastructure using Pulumi from within your Kubernetes environment.  Infrastructure as Code defined in Pulumi can be automatically deployed using a GitOps model driven from within a Kubernetes environment - leveraging existing Kubernetes-based orchestration, RBAC, policy and resource model investments.  We released [Pulumi Kubernetes Operator 1.0](https://www.pulumi.com/blog/pulumi-kubernetes-operator-1-0/) last year, and since then have seen users scale up usage of the Operator to drive hundreds of thousands of Pulumi infrastructure updates.

Pulumi Kubernetes Operator v1.10 expands the ways that Pulumi infrastructure can be defined.  In addition to the existing Git-based source that has been supported to date, this release adds two new ways to define your infrastructure:

* Integration with Flux Sources - enabling any Flux Source to provide the Pulumi program that defines your cloud infrastructure.
* Support for Inline Infrastructure sources - a new `pulumi.com/v1/Program` Custom Resource that can be used to describe cloud infrastructure directly within the Kubernetes resource model.

Together, these open up a wide variety of new ways to apply the Kubernetes Operator as an interface for defining and delivering cloud infrastructure.

### Integration with Flux Sources

<img align="right" width="120" src="flux-icon.png">

We’re excited to work with [Flux](https://fluxcd.io/), a CNCF project, to bring even richer GitOps support to the Pulumi Kubernetes Operator.  While the Pulumi Kubernetes Operator offers basic GitOps and branch tracking support, it supports only a fraction of the features that Flux’s SourceController provides. Instead of rebuilding all of these features, we chose to provide rich integration with Flux Sources, enabling Pulumi programs to be provided via Flux, and then handed off to drive infrastructure deployments using the Pulumi Kubernetes Operator `Stack` resource.

Using Flux offers a variety of important new features to Pulumi Kubernetes Operator users:

1. Support for Flux’s [Notification Controller](https://fluxcd.io/flux/components/notification/) and webhooks to drive highly responsive updates when new commits are pushed
2. Access to sources other than Git repositories: [S3 buckets](https://fluxcd.io/flux/components/source/buckets/) and [OCI repositories](https://fluxcd.io/flux/components/source/ocirepositories/)
3. Support for platforms like Azure DevOps that require specific Git implementations
4. Sources and Stacks can be defined by different teams, since they are separate resources which can have independent RBAC rules applied.
5. Many advanced Git features including: following semver ranges, excluding files from source, recursively cloning submodules, verifying revision signatures, and more.

To use the Pulumi Kubernetes Operator with Flux, install each of the necessary controllers for Flux and the Pulumi Kubernetes Operator, and then the necessary `Role` and `RoleBindings` to allow the Pulumi Kubernetes Operator to read from Flux sources.

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: flux-source-access
rules:
- apiGroups:
  - source.toolkit.fluxcd.io
  resources:
  - "*"
  verbs:
  - get
  - list
  - watch
---
kind: RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
metadata:
  name: pulumi-flux-source-access
subjects:
- kind: ServiceAccount
  name: pulumi-kubernetes-operator
roleRef:
  kind: Role
  name: flux-source-access
  apiGroup: rbac.authorization.k8s.io
```

Once those pre-requisites have been met, simply deploy the Flux Source (in this case a `GitRepository`) and Pulumi `Stack` resource that define your infrastructure delivery:

```yaml
---
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: GitRepository
metadata:
  name: pkodev
spec:
  interval: 30s
  ref:
    branch: main
  url: https://github.com/lukehoban/pko-dev
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: pkodev
spec:
  stack: lukehoban/pkodev/test
  fluxSource:
    sourceRef:
      apiVersion: source.toolkit.fluxcd.io/v1beta2
      kind: GitRepository
      name: pkodev
    dir: basic/
  destroyOnFinalize: true
```

Note that by using the new `fluxSource` property on a `pulumi.com/v1/Stack` resource, you can configure it to use the corresponding source instead of an inline definition of the target Git repo and branch.  The `GitRepository` could be replaced with any other Flux Source.  For example, to pull our source code from an S3 bucket, use this instead:

```yaml
---
apiVersion: source.toolkit.fluxcd.io/v1beta2
kind: Bucket
metadata:
  name: pkodev
spec:
  interval: 5m0s
  provider: aws
  bucketName: podinfo
  endpoint: s3.amazonaws.com
  region: us-east-1
  timeout: 30s
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: pkodev
spec:
  stack: lukehoban/pkodev/test
  fluxSource:
    sourceRef:
      apiVersion: source.toolkit.fluxcd.io/v1beta2
      kind: Bucket
      name: pkodev
    dir: basic/
  destroyOnFinalize: true
```

If we are using the `GitRepository` source along with GitHub, we can use Flux features like [WebHook Recievers](https://fluxcd.io/flux/guides/webhook-receivers/) to expose a webhook that GitHub can trigger on pushes so that updates will be pushed into Flux and the Pulumi Kubernetes Operator directly (instead of waiting to pull them):

```yaml
---
apiVersion: notification.toolkit.fluxcd.io/v1beta1
kind: Receiver
metadata:
  name: webapp
  namespace: flux-system
spec:
  type: github
  events:
    - "ping"
    - "push"
  secretRef:
    name: webhook-token
  resources:
    - kind: GitRepository
      name: pkodev
```

For users who need any of these additional GitOps capabilities, you can now use the best of Pulumi and the best of Flux together with ease.

This integration is made possible by the excellent “open and extensible” GitOps toolkit that Flux v2 provides. We’re excited to work with the Flux community and the team at Weaveworks to help end-users accelerate their GitOps projects:

> _"When we donated Flux to the CNCF we wanted to empower teams to easily build GitOps automations with the best tools. We’re excited to welcome Pulumi to the Flux and Weave GitOps ecosystem."_
>
> _-- **Alexis Richardson, CEO – Weaveworks**_

### Define Pulumi Cloud Infrastructure Directly in the Kubernetes Resource Model

<img align="right" width="120" src="yaml.svg">

One of the important benefits of the Pulumi Kubernetes Operator is that it provides the Kubernetes resource model as an interface for defining and managing cloud infrastructure expressed via Pulumi.  However, to date, the cloud infrastructure definition itself still has to be stored in Git (or, with the Flux integration above, an S3 bucket or OCI repository).  Many users have asked for a model where the Pulumi cloud infrastructure definition itself is provided directly within the Kubernetes resource model as well.  With the new `pulumi.com/v1/Program` custom resource, this is now possible!

This support is enabled by Pulumi’s [introduction of Pulumi YAML](https://www.pulumi.com/blog/pulumi-yaml/) - the ability to describe cloud infrastructure with access to the entire Pulumi ecosystem of cloud providers and components via simple YAML programs.  Importantly, those YAML programs can now be defined directly inside the Kubernetes cluster itself.

Because Pulumi offers access to over 100 cloud providers and components, with thousands of infrastructure resources available across them, the `pulumi.com/v1/Program` resource offers access to defining rich and complex cloud infrastructure directly from within Kubernetes.  And because Pulumi YAML infrastructure definitions support all the same reliable dependency tracking and rich IaC features as any other Pulumi programs, users get all of these benefits from within Kubernetes as well.

To deploy cloud infrastructure directly from within Kubernetes, install the Pulumi Kubernetes Operator and then deploy the `Program` and `Stack` resources below with `kubectl apply` (or via a Pulumi program!):

```yaml
apiVersion: pulumi.com/v1
kind: Program
metadata:
  name: staticwebsite
program:
  resources:
    bucket:
      type: aws:s3:Bucket
      properties:
        website:
          indexDocument: index.html
    index.html:
      type: aws:s3:BucketObject
      properties:
        bucket: ${bucket.id}
        content: <h1>Hello, world!</h1>
        contentType: text/html
        acl: public-read
  outputs:
    url: http://${bucket.websiteEndpoint}
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: staticwebsite
spec:
  stack: lukehoban/staticwebsite/test
  programRef:
    name: staticwebsite
  destroyOnFinalize: true
  config:
    aws:region: us-east-1
```

The result will be to deploy an S3 Bucket and BucketObject exposing a static website into AWS. The `Program` resource defines a Pulumi program written in Pulumi YAML using [any cloud provider resources Pulumi supports](https://www.pulumi.com/registry/index.html), ready to be deployed into as many Pulumi stacks as needed.  The program declares an S3 Bucket with website configured, and an `index.html` file in a BucketObject which will be served from that website.  The `Stack` resource deploys an instance of this program, using the configuration (`us-east-1` region) specified.

You can access the URL of the deployed website defined as a program output `url` via:

```shell
$ kubectl get stack staticwebsite -o jsonpath={.status.outputs}
```

Of course, this could be used to define *any* cloud infrastructure - an [AWS RDS Database](https://www.pulumi.com/registry/packages/aws/api-docs/rds/instance/), an [Azure KeyVault](https://www.pulumi.com/registry/packages/azure-native/api-docs/keyvault/vault/), a [CloudFlare DNS Record](https://www.pulumi.com/registry/packages/cloudflare/api-docs/record/), a [Google Cloud Function](https://www.pulumi.com/registry/packages/gcp/api-docs/cloudfunctions/function/), or even another Kubernetes Cluster via [EKS](https://www.pulumi.com/registry/packages/eks/api-docs/cluster/), [AKS](https://www.pulumi.com/registry/packages/azure-native/api-docs/containerservice/managedcluster/), [GKE](https://www.pulumi.com/registry/packages/gcp/api-docs/container/cluster/), [Oracle Cloud](https://www.pulumi.com/registry/packages/oci/api-docs/containerengine/cluster/), [Civo](https://www.pulumi.com/registry/packages/civo/api-docs/kubernetescluster/), [Digital Ocean](https://www.pulumi.com/registry/packages/digitalocean/api-docs/kubernetescluster/) and more.

Updating the `Program` resource will immediately drive an update to the associated Pulumi `Stack`, incrementally updating the managed infrastructure and maintaining the desired cloud infrastructure state.

## New Pulumi Provider for Flux

In addition to Flux integration with the Pulumi Kubernetes Operator, we've also added a new [Flux Provider](https://www.pulumi.com/registry/packages/flux/) to the Pulumi Registry.  This provider, built by Pulumi community member [@oun](https://github.com/oun),  enables managing Flux directly via Pulumi Infrastructure as Code.

The Flux provider can be used along with the Kubernetes provider and GitHub provider to stand up and manage a complete E2E GitOps solution from within a single deployment - no need for manual bash, Helm, or runbooks - just simple reliable Infrastructure as Code.

```ts
import * as kubernetes from "@pulumi/kubernetes";
import * as flux from "@worawat/flux";

// Get the manifests needed to install Flux with the given components and policies
const fluxManifests = flux.getFluxInstallOutput({
    targetPath: "local",
    components: ['source-controller'],
    networkPolicy: true,
});

// Deploy the manifests into our cluster
const fluxGroup = fluxManifests.content.apply(fluxYaml => {
  new kubernetes.yaml.ConfigGroup("flux-install", {
    yaml: fluxYaml,
  });
});
```

## Pulumi Kubernetes Provider v3.22: Server Side Apply and Resource Patch

In July, we released preview [support for Server-Side Apply](https://www.pulumi.com/blog/kubernetes-server-side-apply/) in the Pulumi Kubernetes provider.  We highlighted the benefits and needs that led to adding Server-Side Apply support:

> We first launched the Pulumi Kubernetes provider in 2018, and it has grown to be one of the most used providers across the Pulumi ecosystem. Many of our customers rely on this provider to manage critical production workloads, and a common request was for an easier way to manage shared Kubernetes resources with Pulumi. We’ve been listening, and are grateful to everyone who took the time to share their feedback with us!
>
> A lot has changed since 2018, and our provider continues to evolve to support new use cases and the ever-growing richness of the Kubernetes ecosystem. One such development is Server-Side Apply (SSA), which is a resource management strategy that was introduced in Kubernetes v1.18. Kubernetes clients that use SSA can safely share the management of Kubernetes resources by making the API Server responsible for computing diffs and resolving conflicts.
>
> We have kept a close eye on the SSA feature since it was announced and have been waiting patiently for its broad availability in production clusters. The wait is over, and we are excited to bring the power of SSA to Pulumi users!

With the most recent v3.22 release of the Kubernetes provider, Server-Side Apply support is now out of preview and enabled by default for all Kubernetes resources.

This makes several important new features available across the breadth of the Kubernetes provider:

* New Patch resource types corresponding to every Kubernetes resource kind. (e.g., NamespacePatch, DeploymentPatch)
* “Upsert” support; create a resource if it does not exist, or update the existing resource with specified changes.
* Diffs no longer depend on the last-applied-configuration annotation, which fixes a number of subtle issues that users of the provider previously could run into.

These features bring Pulumi and Kubernetes even closer together, enabling Pulumi’s rich Infrastructure as Code to fit even more naturally into the Kubernetes desired state and shared ownership model.

Check out the [Managing Resources with Server Side Apply](https://www.pulumi.com/registry/packages/kubernetes/how-to-guides/managing-resources-with-server-side-apply/) article for more details on these new features.

## Conclusion

At Pulumi, we are passionate about pushing the state of the art of Infrastructure as Code forward, and applying modern Infrastructure as Code to support Kubernetes projects and teams is a critical component of that vision.  All of these new features around Pulumi and Kubernetes help to further empower teams to build scalable and robust solutions around Kubernetes and Pulumi IaC.

We’re so happy to be able to work with the Flux project to bring all of the benefits of its composable GitOps toolkit to Pulumi users. We’re excited about the new use cases that Inline Infrastructure support in the Pulumi Kubernetes Operator enables. And we’re thrilled to bring Server Side Apply and Patch support to the Pulumi Kubernetes Provider.

You can [learn more about Pulumi and Kubernetes](https://www.pulumi.com/registry/packages/kubernetes/) or jump in right away by following the [getting started guide](https://www.pulumi.com/docs/iac/get-started/kubernetes/).
