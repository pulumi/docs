---
title: Pulumi Kubernetes Operator
meta_desc: This page details how to use the Pulumi Kubernetes Operator to manage deploying
           stacks based on commits to specific Git branches.
menu:
    userguides:
        parent: cont_delivery
        weight: 1
---

This page details how to use the [Pulumi Kubernetes Operator](https://github.com/pulumi/pulumi-kubernetes-operator) to manage deploying
[Stacks][stack] based on commits to specific Git branches.

## Overview

The Pulumi Kubernetes Operator is an [extension pattern][k8s-ext-pattern] that
enables Kuberentes users to create a `Stack` as a first-class API
resource, and use the `StackController` to drive the updates of the Stack until
success.

Deploying Pulumi Stacks in Kubernetes provides the capability to build
out CI/CD and automation systems into your clusters, creating native support to manage your infrastructure alonside your Kubernetes workloads.

To work with the operator, we'll need to follow these steps.

- [Deploy the Pulumi Kubernetes Operator](#deploy-the-pulumi-kubernetes-operator)
- [Create a Stack CustomResource](#create-a-stack-customresource)

[k8s-ext-pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[stack]: {{< relref "/docs/intro/concepts/stack" >}}

## Deploy the Pulumi Kubernetes Operator

The operator is composed of:

- A ServiceAccount for identity,
- A Role and RoleBinding to the ServiceAccount for RBAC, and
- A Deployment to manage the controler.

To create the operator, choose an installation preference using Pulumi
with a supported programming language, or `kubectl` with YAML.

- [Installing the Operator with Pulumi in Typescript, Python, C#, and Go][use-pulumi]
- [Installing the Operator with kubectl][use-kubectl]

[use-pulumi]: https://github.com/pulumi/pulumi-kubernetes-operator#using-pulumi
[use-kubectl]: https://github.com/pulumi/pulumi-kubernetes-operator#using-kubectl

When launched, the operator invokes the `StackController` to manages updates to
`Stack` CustomResources created, updated, or deleted in Kubernetes.

These updates are run in the form of reconcilation loops that attempt to update a Stack until success
is reached for the Git commit SHA provided, also known as the `desired state`.

## Create a Stack CustomResource

The `Stack` CustomResource (CR) encapsulates a Pulumi project that creates any set of
infrastructure resources such as cloud VMs, object storage, Kubernetes
clusters, or Kubernetes workloads through API resources.

The Stack uses an existing Git repo, and checks out a specific Git commit SHA of the repo to deploy a `pulumi up`.

In the example below, we're creating a Stack for an existing Pulumi project that provisions
a simple [NGINX][nginx-stack] Deployment in Kubernetes.

When the Stack is processed and deployed by the operator, NGINX will be created
in the same cluster as the operator. This is because the NGINX Pulumi program does not
explicitly use a [Kubernetes Provider resource][k8s-provider], and the Operator
makes it's ServiceAccount credentials available to Stacks that rely on
the [default, ambient kubeconfig credentials][default-kubeconfig].

To adjust what in-cluster API resource provisioning is or is not allowed
is simply a matter of adjusting the role permissions for the operator.

[nginx-stack]: https://github.com/metral/pulumi-nginx/blob/master/index.ts
[k8s-provider]: {{< relref "/docs/reference/pkg/kubernetes/provider" >}}
[default-kubeconfig]: {{< relref "/docs/intro/cloud-providers/kubernetes/setup#steps" >}}

Choose your preferred language below, or check out [Create Pulumi Stacks using kubectl][stacks-use-kubectl].

{{< chooser language "typescript,python,go,csharp" >}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";
import * as kx from "@pulumi/kubernetesx";

// Get the Pulumi API token.
const pulumiConfig = new pulumi.Config();
const pulumiAccessToken = pulumiConfig.requireSecret("pulumiAccessToken")

// Create the API token as a Kubernetes Secret.
const accessToken = new kx.Secret("accesstoken", {
    stringData: { accessToken: pulumiAccessToken},
});

// Create an NGINX deployment in-cluster.
const mystack = new k8s.apiextensions.CustomResource("my-stack", {
    apiVersion: 'pulumi.com/v1alpha1',
    kind: 'Stack',
    spec: {
        accessTokenSecret: accessToken.metadata.name,
        stack: "<YOUR_ORG>/nginx/dev",
        initOnCreate: true,
        projectRepo: "https://github.com/metral/pulumi-nginx",
        commit: "2b0889718d3e63feeb6079ccd5e4488d8601e353",
        destroyOnFinalize: true,
    }
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
from pulumi_kubernetes import core, apiextensions

# Get the Pulumi API token.
pulumi_config = pulumi.Config()
pulumi_access_token = pulumi_config.require_secret("pulumiAccessToken")

# Create the API token as a Kubernetes Secret.
access_token = core.v1.Secret("accesstoken", string_data={ "access_token": pulumi_access_token })

# Create an NGINX deployment in-cluster.
my_stack = apiextensions.CustomResource("my-stack",
    api_version="pulumi.com/v1alpha1",
    kind="Stack",
    spec={
        "access_token_secret": access_token.metadata["name"],
        "stack": "<YOUR_ORG>/nginx/dev",
        "init_on_create": True,
        "project_repo": "https://github.com/metral/pulumi-nginx",
        "commit": "2b0889718d3e63feeb6079ccd5e4488d8601e353",
        "destroy_on_finalize": True,
    }
)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
Coming Soon
```

{{% /choosable %}}

{{% choosable language go %}}

```go
Coming Soon
```

{{% /choosable %}}
{{% /chooser %}}

[stacks-use-kubectl]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/create-stacks-using-kubectl.md

### Stack Settings

Stack CustomResources can have the following properties configured that
influence the Stack update run:

- The first is the access token secret, better known as `PULUMI_ACCESS_TOKEN`, which is required to authenticate with pulumi.com in order to
  perform the update. You can create a new Pulumi access token specifically for your
  CI/CD job on your [Pulumi Account page](https://app.pulumi.com/account/tokens).
- Environment variables to make available to the Stack that are sourced from Kubernetes ConfigMaps and/or Secrets. Examples include
  cloud provider credentials, and other application settings.
- Pulumi Stack configs and secrets that can complement or override settings
  in the repo for use within the Stack.
- Project repo settings like the repo URL, the commit to deploy, and a repo
  access token for private repos or rate-limiting.
- And, lifecyle control such as creating the stack if it does not exist,
  issuing a refresh before the update, and destroying the Stack's resources
  and stack itself upon deletion of the CR.

### Extended Examples

Check out how to [manage a Kubernetes Blue/Green Deployment][blue-green-demo]
using the Operator and a Stack CR.

[blue-green-demo]: https://github.com/pulumi/pulumi-kubernetes-operator/tree/master/examples/blue-green

## Concurrency

When using the operator to continuously deploy your Pulumi stacks, you may run into a problem. What
happens if multiple reconcilation loops are run for the same commit in succession?

Operators by definition will invoke a reconcilation loop for the creation, update, or deletion of a Stack CR.

Pulumi blocks any stack updates while one is already in progress. (To avoid conflicting resource
updates or corrupting resource state.) So the stack and its resources won't be harmed by the
concurrent update. By default, the operator is informed if a conflicting
update is already in progress and will not spawn another reconcilation loop to
give the current update in progress sole control of the update run.

You can optionally retry on update conflicts rather than the operator default of
not retrying, by using the `RetryOnUpdateConflict` toggle in the Stack.

> Note: This is only recommended if you are sure that the stack updates are idempotent, and if you are willing to accept retry loops until
> all spawned retries succeed. This will also create a more populated, and randomized activity timeline for the stack in the Pulumi Service.

Check out [troubleshooting](https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/troubleshooting.md) for more details, or
open a [new issue](https://github.com/pulumi/pulumi-kubernetes-operator/issues/new) in GitHub.
