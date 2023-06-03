---
title_tag: "Using Pulumi Kubernetes Operator | CI/CD"
meta_desc: This page details how to use the Pulumi Kubernetes Operator to manage deploying
           stacks based on commits in git, Kubernetes objects, or Flux sources.
title: Pulumi Kubernetes Operator
h1: Pulumi Kubernetes Operator
menu:
    usingpulumi:
        parent: cont_delivery
        weight: 1
aliases:
- /docs/guides/continuous-delivery/pulumi-kubernetes-operator/
---

This page details how to use the [Pulumi Kubernetes
Operator](https://github.com/pulumi/pulumi-kubernetes-operator) to manage deploying
[Stacks][stack]. The Pulumi program for a Stack can come from a [Program resource][], from git, or from a [Flux source][flux-source].

[Program resource]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/programs.md
[flux-source]: https://fluxcd.io/flux/components/source/

## Overview

The Pulumi Kubernetes Operator is an [extension pattern][k8s-ext-pattern] that
enables Kubernetes users to create a `Stack` as a first-class API
resource, and use the `StackController` to drive the updates of the Stack until
success.

Deploying Pulumi Stacks in Kubernetes provides the capability to build
out CI/CD and automation systems into your clusters, creating native support to manage your infrastructure alongside your Kubernetes workloads.

To work with the operator, we'll need to follow these steps.

- [Overview](#overview)
- [Deploy the Pulumi Kubernetes Operator](#deploy-the-pulumi-kubernetes-operator)
- [Create a Stack CustomResource](#create-a-stack-customresource)
  - [Using a git repository](#using-a-git-repository)
  - [Using a Flux source](#using-a-flux-source)
  - [Using a Program object](#using-a-program-object)
  - [Stack Settings](#stack-settings)
  - [Extended Examples](#extended-examples)
- [Concurrent Updates on the Same Stack](#concurrent-updates-on-the-same-stack)

[k8s-ext-pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[stack]: /docs/concepts/stack/

## Deploy the Pulumi Kubernetes Operator

The operator configuration is composed of:

- A ServiceAccount for identity,
- A Role and RoleBinding to the ServiceAccount for RBAC, and
- A Deployment to manage the controller.

To create the operator, choose an installation preference using Pulumi
with a supported programming language or `kubectl` with YAML.

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

### Using a git repository

In this scenario, the Stack points at an existing Git repo, and checks out the repo to deploy a `pulumi up`. The Stack configuration can specify a specific commit SHA or a reference to a branch or tag to track. If a commit is specified, the operator will try to reify the desired state of the stack in the commit until it succeeds. If a branch reference is specified, the Pulumi Kubernetes Operator will periodically poll the branch for any new commits and roll out updates as they are found.

In the example below, we're creating a Stack for an existing Pulumi project that provisions
a simple [NGINX][nginx-stack] Deployment in Kubernetes.

When the Stack is processed and deployed by the operator, NGINX will be created
in the same cluster as the operator. This is because the NGINX Pulumi program does not
explicitly use a [Kubernetes Provider resource][k8s-provider], and the Operator
makes its ServiceAccount credentials available to Stacks that rely on
the [default, ambient kubeconfig credentials][default-kubeconfig].

The role permissions for the operator can be adjusted to control what in-cluster API resources are allowed.

[nginx-stack]: https://github.com/pulumi/examples/blob/master/kubernetes-ts-nginx/index.ts
[k8s-provider]: /registry/packages/kubernetes/api-docs/provider/
[default-kubeconfig]: /registry/packages/kubernetes/installation-configuration/#setup

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
    stringData: { accessToken: pulumiAccessToken },
});

// Create an NGINX deployment in-cluster.
const mystack = new k8s.apiextensions.CustomResource("my-stack", {
    apiVersion: 'pulumi.com/v1',
    kind: 'Stack',
    spec: {
        envRefs: {
            PULUMI_ACCESS_TOKEN: {
                type: "Secret",
                secret: {
                    name: accessToken.metadata.name,
                    key: "accessToken"
                },
            },
        },
        stack: "<YOUR_ORG>/k8s-nginx/dev",
        projectRepo: "https://github.com/pulumi/examples",
        repoDir: "kubernetes-ts-nginx",
        commit: "e2e5eb426dbf5b57c50bba0f8eb54fe982ceddb1",
        // branch: "refs/heads/master", // Alternatively, track master branch.
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
    api_version="pulumi.com/v1",
    kind="Stack",
    spec={
        "envRefs": {
            "PULUMI_ACCESS_TOKEN": {
                "type": "Secret",
                "secret": {
                    "name": access_token.metadata.name,
                    "key": "access_token",
                }
            },
        },
        "stack": "<YOUR_ORG>/k8s-nginx/dev",
        "projectRepo": "https://github.com/pulumi/examples",
        "repoDir": "kubernetes-ts-nginx",
        "commit": "e2e5eb426dbf5b57c50bba0f8eb54fe982ceddb1",
        # branch: "refs/heads/master", # Alternatively, track master branch.
        "destroyOnFinalize": True,
    }
)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Kubernetes.ApiExtensions;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;

class StackArgs : CustomResourceArgs
{
    [Input("spec")]
    public Input<StackSpecArgs>? Spec { get; set; }

    public StackArgs() : base("pulumi.com/v1", "Stack")
    {
    }
}

class StackSpecArgs : ResourceArgs
{
    [Input("accessTokenSecret")]
    public Input<string>? AccessTokenSecret { get; set; }

    [Input("stack")]
    public Input<string>? Stack { get; set; }

    [Input("projectRepo")]
    public Input<string>? ProjectRepo { get; set; }

    [Input("commit")]
    public Input<string>? Commit { get; set; }

    [Input("destroyOnFinalize")]
    public Input<bool>? DestroyOnFinalize { get; set; }
}

class MyStack : Stack
{
    public MyStack()
    {
        // Get the Pulumi API token.
        var config = new Config();
        var pulumiAccessToken = config.RequireSecret("pulumiAccessToken");

        // Create the API token as a Kubernetes Secret.
        var accessToken = new Secret("accesstoken", new SecretArgs
        {
            StringData =
            {
                {"accessToken", pulumiAccessToken}
            }
        });

        // Create an NGINX deployment in-cluster.
        var myStack = new Pulumi.Kubernetes.ApiExtensions.CustomResource("nginx", new StackArgs
        {
            Spec = new StackSpecArgs
            {
                AccessTokenSecret = accessToken.Metadata.Apply(m => m.Name),
                Stack = "<YOUR_ORG>/k8s-nginx/dev",
                InitOnCreate = true,
                ProjectRepo = "https://github.com/pulumi/examples",
                RepoDir = "kubernetes-ts-nginx",
                Commit = "e2e5eb426dbf5b57c50bba0f8eb54fe982ceddb1",
                // branch: "refs/heads/master", // Alternatively, track master branch.
                DestroyOnFinalize = true,
            }
        });
    }
}
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
	apiextensions "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apiextensions"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Get the Pulumi API token.
		c := config.New(ctx, "")
		pulumiAccessToken := c.Require("pulumiAccessToken")

		// Create the API token as a Kubernetes Secret.
		accessToken, err := corev1.NewSecret(ctx, "accesstoken", &corev1.SecretArgs{
			StringData: pulumi.StringMap{"accessToken": pulumi.String(pulumiAccessToken)},
		})
		if err != nil {
			return err
		}

		// Create an NGINX deployment in-cluster.
		_, err = apiextensions.NewCustomResource(ctx, "my-stack", &apiextensions.CustomResourceArgs{
			ApiVersion: pulumi.String("pulumi.com/v1"),
			Kind:       pulumi.String("Stack"),
			OtherFields: kubernetes.UntypedArgs{
				"spec": map[string]interface{}{
					"envRefs": pulumi.Map{
						"PULUMI_ACCESS_TOKEN": pulumi.Map{
							"type": pulumi.String("Secret"),
							"secret": pulumi.Map{
								"name": accessToken.Metadata.Name(),
								"key":  pulumi.String("accessToken"),
							},
						},
					},
					"stack":             "<YOUR_ORG>/k8s-nginx/dev",
					"projectRepo":       "https://github.com/pulumi/examples",
                    "repoDir":           "kubernetes-ts-nginx",
					"commit":            "e2e5eb426dbf5b57c50bba0f8eb54fe982ceddb1",
					// "branch":         "refs/heads/master", // Alternatively, track master branch.
					"destroyOnFinalize": true,
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{accessToken}))
		return err
	})
}

```

{{% /choosable %}}
{{% /chooser %}}

[stacks-use-kubectl]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/create-stacks-using-kubectl.md

### Using a Flux source

To refer to a [Flux source][flux-source] rather than polling git directly, use the field
`.spec.fluxSource` and leave empty all of `.spec.projectRepo`, `.spec.commit`, `.spec.branch`, and
`.spec.gitAuth`. Here is the TypeScript example from above, adjusted to create a Flux source for the
git repo, then refer to it from the Stack object. The example assumes you have installed Flux into
the cluster beforehand.

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";
import * as kx from "@pulumi/kubernetesx";

// Get the Pulumi API token.
const pulumiConfig = new pulumi.Config();
const pulumiAccessToken = pulumiConfig.requireSecret("pulumiAccessToken")

// Create the API token as a Kubernetes Secret.
const accessToken = new kx.Secret("accesstoken", {
    stringData: { accessToken: pulumiAccessToken },
});

// Create a GitRepository
const gitrepo = new k8s.apiextensions.CustomResource("nginx-repo", {
    apiVersion: "toolkit.source.fluxcd.io/v1beta2",
    kind: "GitRepository",
    metadata: {},
    spec: {
        interval: '5m0s',
        url: "https://github.com/pulumi/examples",
        ref: { commit: "e2e5eb426dbf5b57c50bba0f8eb54fe982ceddb1" },
    },
});

// Create an NGINX deployment in-cluster.
const mystack = new k8s.apiextensions.CustomResource("my-stack", {
    apiVersion: 'pulumi.com/v1',
    kind: 'Stack',
    spec: {
        envRefs: {
            PULUMI_ACCESS_TOKEN: {
                type: "Secret",
                secret: {
                    name: accessToken.metadata.name,
                    key: "accessToken"
                },
            },
        },
        stack: "<YOUR_ORG>/k8s-nginx/dev",
        fluxSource: {
            sourceRef: {
                apiVersion: "source.toolkit.fluxcd.io/v1beta2",
                kind: "GitRepository",
                name: gitrepo.metadata.name,
            },
        },
        destroyOnFinalize: true,
    }
});
```

### Using a Program object

It is also possible to supply a Pulumi YAML program directly as a Kubernetes resource. A Program
resource is a Pulumi YAML program, wrapped up as a Kubernetes object. The reference for the [Program
custom resource definition][] details the wrapping; the [reference for Pulumi YAML][] gives all the
fields that are part of the program itself.

[Program custom resource definition]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/programs.md
[reference for Pulumi YAML]: /docs/languages-sdks/yaml/yaml-language-reference/

Here is an example as a YAML file:

```yaml
---
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
```

You can then create a Stack object to deploy the program, by referring to it in the field
`programRef`:

```yaml
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: staticwebsite
spec:
  stack: <YOUR ORG>/staticwebsite/dev
  programRef:
    name: staticwebsite
  destroyOnFinalize: true
  config:
    aws:region: us-east-1
```

### Stack Settings

Stack CustomResources provide the following properties to configure the Stack update run:

- The first is the access token secret (`PULUMI_ACCESS_TOKEN`), which is required to authenticate with pulumi.com to
  perform the update. You can create a new [Pulumi access token](/docs/pulumi-cloud/accounts#access-tokens)
  specifically for your CI/CD job on your [Pulumi Account page](https://app.pulumi.com/account/tokens).
- Environment variables for the Stack that are sourced from Kubernetes ConfigMaps and/or Secrets. Examples include
  cloud provider credentials and other application settings.
- Pulumi Stack configs and secrets that can complement or override settings
  in the repo for use within the Stack.
- Project repo settings like the repo URL, the commit to deploy, and a repo
  access token for private repos or rate-limiting.
- Lifecyle control such as creating the stack if it does not exist,
  issuing a refresh before the update, and destroying the Stack's resources
  and stack itself upon deletion of the CR.
- Switching to an open source backend.

Detailed documentation on Stack CR configuration is available [here](https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/stacks.md).

### Extended Examples

Check out how to [manage a Kubernetes Blue/Green Deployment][blue-green-demo],
or how to create [AWS S3 buckets][aws-s3-demo] using the Operator and a Stack CR.

You can watch a demo below for a complete walkthrough.

{{< youtube "nQZr3uquc-c" >}}

[blue-green-demo]: https://github.com/pulumi/pulumi-kubernetes-operator/tree/master/examples/blue-green
[aws-s3-demo]: https://github.com/pulumi/pulumi-kubernetes-operator/tree/master/examples/aws-s3

## Concurrent Updates on the Same Stack

Operators, by definition, will invoke a reconciliation loop for the creation, update, or deletion of a Stack CR.

To avoid conflicting resource updates or corrupting resource state, Pulumi only
runs one update at a time per stack. By default, the operator checks for updates
already in progress, and will not spawn another reconciliation loop if one is already
running, blocking that stack. We strongly advice against running external updates on stacks controlled by the operator.

You can optionally choose to retry on update conflicts by using the
`RetryOnUpdateConflict` field in the Stack.

> Note: This is only recommended if you are sure that the stack updates are idempotent, and if you are willing to accept retry loops until
> all spawned retries succeed. This will also create a more populated, and randomized activity timeline for the stack in the Pulumi Cloud.

Check out [troubleshooting](https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/troubleshooting.md) for more details, look at [known issues](https://github.com/pulumi/pulumi-kubernetes-operator/issues/) or
open a [new issue](https://github.com/pulumi/pulumi-kubernetes-operator/issues/new) in GitHub.
