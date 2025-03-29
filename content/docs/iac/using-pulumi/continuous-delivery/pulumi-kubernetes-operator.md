---
title_tag: "Using Pulumi Kubernetes Operator | CI/CD"
meta_desc: This page details how to use the Pulumi Kubernetes Operator to manage deploying
  stacks based on commits in git, Kubernetes objects, or Flux sources.
title: Pulumi Kubernetes Operator
h1: Pulumi Kubernetes Operator
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    name: Pulumi Kubernetes Operator
    parent: iac-using-pulumi-cicd
    weight: 13
aliases:
  - /docs/guides/continuous-delivery/pulumi-kubernetes-operator/
  - /docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/
  - /docs/iac/packages-and-automation/continuous-delivery/pulumi-kubernetes-operator/
search:
  keywords:
    - Kubernetes
    - Operator
    - Kubernetes Operator
    - Service Account
---

This page details how to use the [Pulumi Kubernetes
Operator](https://github.com/pulumi/pulumi-kubernetes-operator) (PKO) to automate the deployment of Pulumi [stacks][stack]. The Pulumi program for a stack can come from a [Program resource][], from a Git repository, or from a [Flux source][flux-source], and may be authored in any supported Pulumi language (TypeScript, Python, Go, .NET, Java, YAML).

[Program resource]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/programs.md
[flux-source]: https://fluxcd.io/flux/components/source/

## Overview

The Pulumi Kubernetes Operator provides [custom resources][k8s-ext-pattern] to:

- Provision a workspace (an execution environment) for a Pulumi project
- Keep a Pulumi stack up-to-date using gitops
- Write [Pulumi YAML][] programs as Kubernetes objects
- Run Pulumi deployment operations

Deploying Pulumi stacks using Kubernetes provides the capability to build
out CI/CD and other automation systems, and to manage your infrastructure alongside your Kubernetes workloads or in dedicated control-plane clusters.

To work with the operator, we'll need to follow these steps.

- [Overview](#overview)
- [Install the Pulumi Kubernetes Operator](#install-the-pulumi-kubernetes-operator)
  - [Using Helm](#using-helm)
  - [Dev Install](#dev-install)
- [Create a Service Account](#create-a-service-account)
- [Configure Pulumi Cloud Access](#configure-pulumi-cloud-access)
- [Create a Stack Resource](#create-a-stack-resource)
  - [Using a Git repository](#using-a-git-repository)
  - [Using a Flux source](#using-a-flux-source)
  - [Using a Program object](#using-a-program-object)
- [Explore other Features](#explore-other-features)
  - [Stack Configuration Values](#stack-configuration-values)
  - [Environment Variables](#environment-variables)
  - [Drift Detection](#drift-detection)
  - [State Refresh](#state-refresh)
  - [Stack Cleanup](#stack-cleanup)
  - [Stack Prerequisites](#stack-prerequisites)
  - [External Triggers](#external-triggers)
- [Use With Argo CD](#use-with-argo-cd)
- [More Information](#more-information)
  - [Examples](#examples)
  - [Getting Help](#getting-help)

[k8s-ext-pattern]: https://kubernetes.io/docs/concepts/extend-kubernetes/operator/
[stack]: /docs/concepts/stack/
[Pulumi YAML]: /docs/iac/languages-sdks/yaml/

## Install the Pulumi Kubernetes Operator

### Using Helm

Use [Helm 3.x][helm] to install the Pulumi Kubernetes Operator into your cluster.

```bash
helm install --create-namespace -n pulumi-kubernetes-operator pulumi-kubernetes-operator \
    oci://ghcr.io/pulumi/helm-charts/pulumi-kubernetes-operator --version 2.0.0
```

[helm]: https://helm.sh/

### Dev Install

A simple "quickstart" installation manifest is provided for non-production environments.

Install with `kubectl`:

```bash
kubectl apply -f https://raw.githubusercontent.com/pulumi/pulumi-kubernetes-operator/refs/tags/v2.0.0/deploy/quickstart/install.yaml
```

Note: the installation manifest creates a usable Kubernetes service account named `default/pulumi`
for your convenience.

## Create a Service Account

The operator uses Kubernetes pods as the execution environment for Pulumi stack operations,
with each Stack having a dedicated pod. A pod service account is needed to serve as the stack's identity
and to authenticate users.

Create a `ServiceAccount` named `default/pulumi` and grant the `system:auth-delegator` cluster role:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  namespace: default
  name: pulumi
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: default:pulumi:system:auth-delegator
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator # permissions: TokenReview, SubjectAccessReview
subjects:
- kind: ServiceAccount
  namespace: default
  name: pulumi
```

 If your Pulumi program uses the [Kubernetes Provider][] to manage resources within the cluster, the stack’s service account will need extra permissions, e.g. a `ClusterRoleBinding` to the `cluster-admin` cluster role.

 See [“Kubernetes: Service Accounts”][service-accounts] for more information.

[Kubernetes Provider]: https://www.pulumi.com/registry/packages/kubernetes/
[service-accounts]: https://kubernetes.io/docs/concepts/security/service-accounts/

## Configure Pulumi Cloud Access

By default, the operator uses Pulumi Cloud as the state backend for your stacks.
Please create a `Secret` containing a Pulumi access token to be used to authenticate to Pulumi Cloud. Follow [these instructions][tokens] to create a personal, organization, or team access token.

Here’s an easy way to create a secret named `default/pulumi-api-secret`:

```bash
kubectl create secret generic -n default pulumi-api-secret \
  --from-literal=accessToken=$PULUMI_ACCESS_TOKEN
```

In the Stack specification, use `spec.envRefs` to reference the secret:

```yaml
spec:
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-api-secret
        key: accessToken
```

To use a DIY state backend, set the `spec.backend` field to a storage endpoint URL.
Use `spec.envRefs` to attach credentials and to set environment variables for the backend as necessary.

See ["States & Backends"][states-backends] for more information.

[tokens]: https://www.pulumi.com/docs/pulumi-cloud/access-management/access-tokens/
[states-backends]: https://www.pulumi.com/docs/iac/concepts/state-and-backends/

## Create a Stack Resource

The `Stack` Resource encapsulates a Pulumi project to provision infrastructure resources such as cloud VMs, object storage, and Kubernetes clusters and their workloads.

Set the `spec.serviceAccountName` field to the name of a `ServiceAccount` with the requisite permissions.

Set the `spec.stack` field to a unique Pulumi stack name, using a [supported format][].

[supported format]: https://www.pulumi.com/docs/iac/concepts/stacks/#create-stack

### Using a Git repository

In this scenario, the stack draws on a Git repository for the program source code.

The `Stack` specification can specify a commit SHA (`spec.commit`) or a branch reference (`spec.branch`). The repository URL is specified with `spec.projectRepo` plus an optional `spec.repoDir`.

If a branch reference is specified, the operator will periodically poll the branch for any new commits
and roll out updates as they are found. Use the `spec.resyncFrequencySeconds` field to set the polling frequency.

Specify Git authentication options with the `spec.gitAuth` field.

In the example below, we're creating a `Stack` for a Pulumi project called `kubernetes-ts-nginx` to deploy a simple [NGINX][nginx-stack] server to your cluster. Without any configuration, the [Kubernetes Provider][k8s-provider] uses the in-cluster Kubernetes context.

[nginx-stack]: https://github.com/pulumi/examples/blob/master/kubernetes-ts-nginx/index.ts
[k8s-provider]: /registry/packages/kubernetes/api-docs/provider/
[default-kubeconfig]: /registry/packages/kubernetes/installation-configuration/#setup

{{< chooser language "typescript,python,go,csharp" >}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

// Get the Pulumi API token.
const pulumiConfig = new pulumi.Config();
const pulumiAccessToken = pulumiConfig.requireSecret("pulumiAccessToken")

// Create the API token as a Kubernetes Secret.
const accessToken = new k8s.core.v1.Secret("accessToken", {
    stringData: { accessToken: pulumiAccessToken },
});

// Create an NGINX deployment in-cluster.
const mystack = new k8s.apiextensions.CustomResource("my-stack", {
    apiVersion: 'pulumi.com/v1',
    kind: 'Stack',
    spec: {
        serviceAccountName: "pulumi",
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
        repoDir: "kubernetes-ts-nginx/",
        commit: "03658b5514f08970f350618a6e6fdf1bd75f45d0",
        // branch: "master", // Alternatively, track master branch.
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
access_token = core.v1.Secret("accessToken", string_data={ "access_token": pulumi_access_token })

# Create an NGINX deployment in-cluster.
my_stack = apiextensions.CustomResource("my-stack",
    api_version="pulumi.com/v1",
    kind="Stack",
    spec={
        "serviceAccountName": "pulumi",
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
        "repoDir": "kubernetes-ts-nginx/",
        "commit": "03658b5514f08970f350618a6e6fdf1bd75f45d0",
        # branch: "master", # Alternatively, track master branch.
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
    [Input("serviceAccountName")]
    public Input<string>? ServiceAccountName { get; set; }

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
        var accessToken = new Secret("accessToken", new SecretArgs
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
                ServiceAccountName = "pulumi",
                AccessTokenSecret = accessToken.Metadata.Apply(m => m.Name),
                Stack = "<YOUR_ORG>/k8s-nginx/dev",
                InitOnCreate = true,
                ProjectRepo = "https://github.com/pulumi/examples",
                RepoDir = "kubernetes-ts-nginx/",
                Commit = "03658b5514f08970f350618a6e6fdf1bd75f45d0",
                // branch: "master", // Alternatively, track master branch.
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
		accessToken, err := corev1.NewSecret(ctx, "accessToken", &corev1.SecretArgs{
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
					"serviceAccountName": "pulumi",
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
					"repoDir":           "kubernetes-ts-nginx/",
					"commit":            "03658b5514f08970f350618a6e6fdf1bd75f45d0",
					// "branch":         "master", // Alternatively, track master branch.
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

### Using a Flux source

[Flux][] offers a powerful alternative for fetching Pulumi program source code from
a variety of sources, including OCI repositories and cloud storage buckets.
Flux also supports some advanced Git options. Flux sources are specified as Custom Resources in a Kubernetes cluster; examples of sources are `GitRepository`, `OCIRepository`, and `Bucket` resources.

To refer to a [Flux source object][flux-source], use the `spec.fluxSource` field.  Use `spec.fluxSource.dir` to refer to a program directory within the source artifact.

Here is the TypeScript example from above, adjusted to create a Flux source for the
Git repo and then use it in the Stack specification. This example assumes you've already installed Flux into your cluster (see ["Flux installation"][flux-install]).

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

// Get the Pulumi API token.
const pulumiConfig = new pulumi.Config();
const pulumiAccessToken = pulumiConfig.requireSecret("pulumiAccessToken")

// Create the API token as a Kubernetes Secret.
const accessToken = new k8s.core.v1.Secret("accessToken", {
    stringData: { accessToken: pulumiAccessToken },
});

// Create a GitRepository
const gitrepo = new k8s.apiextensions.CustomResource("nginx-repo", {
    apiVersion: "source.toolkit.fluxcd.io/v1",
    kind: "GitRepository",
    metadata: {},
    spec: {
        interval: '5m0s',
        url: "https://github.com/pulumi/examples",
        ref: { commit: "03658b5514f08970f350618a6e6fdf1bd75f45d0" },
    },
});

// Create an NGINX deployment in-cluster.
const mystack = new k8s.apiextensions.CustomResource("my-stack", {
    apiVersion: 'pulumi.com/v1',
    kind: 'Stack',
    spec: {
        serviceAccountName: "pulumi",
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
                apiVersion: "source.toolkit.fluxcd.io/v1",
                kind: "GitRepository",
                name: gitrepo.metadata.name,
            },
        },
        destroyOnFinalize: true,
    }
});
```

[flux]: https://fluxcd.io/
[flux-install]: https://fluxcd.io/flux/installation/

### Using a Program object

With the `Program` resource, you can define a Pulumi YAML program directly as a Kubernetes resource.
The reference docs for the [Program
Custom Resource][program-crd] details the wrapping; the [reference docs for Pulumi YAML][pulumi-yaml-ref]
gives all the fields that are part of the program code.

[program-crd]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/programs.md
[pulumi-yaml-ref]: /docs/languages-sdks/yaml/yaml-language-reference/

Here is an example as a YAML manifest file:

```yaml
---
apiVersion: pulumi.com/v1
kind: Program
metadata:
  name: staticwebsite
program:
  resources:
    my-bucket:
      type: aws:s3:BucketV2
    my-bucket-ownership-controls:
      type: aws:s3:BucketOwnershipControls
      properties:
        bucket: ${my-bucket.id}
        rule:
          objectOwnership: ObjectWriter
    my-bucket-acl:
      type: aws:s3:BucketAclV2
      properties:
        bucket: ${my-bucket.bucket}
        acl: public-read
      options:
        dependsOn:
          - ${my-bucket-ownership-controls}
    my-bucket-public-access-block:
      type: aws:s3:BucketPublicAccessBlock
      properties:
        bucket: ${my-bucket.id}
        blockPublicAcls: false
    my-bucket-website:
      type: aws:s3:BucketWebsiteConfigurationV2
      properties:
        bucket: ${my-bucket.bucket}
        indexDocument:
          suffix: index.html
    index.html:
      type: aws:s3:BucketObject
      properties:
        bucket: ${my-bucket}
        source:
          fn::stringAsset: <h1>Hello, world!</h1>
        acl: public-read
        contentType: text/html
  outputs:
    bucketEndpoint: http://${my-bucket-website.websiteEndpoint}
```

You can then create a Stack object to deploy the program, by referring to it in the `spec.programRef` field:

```yaml
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: staticwebsite
spec:
  serviceAccountName: pulumi
  stack: <YOUR ORG>/staticwebsite/dev
  programRef:
    name: staticwebsite
  destroyOnFinalize: true
  config:
    aws:region: us-east-1
```

## Explore other Features

Here's some advanced options provided by the `Stack` resource.
Detailed documentation on the Stack API is available [here][pko-stacks].

[pko-stacks]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/stacks.md

### Stack Configuration Values

In many cases, different stacks for a single project will need differing values.
For instance, you may want to use a different size for your AWS EC2 instance, or a different number of replicas
for a particular Kubernetes deployment. Pulumi offers a configuration system for managing such differences;
see ["Configuration"][iac-config] for more information.

Use the `spec.config` block to set stack configuration values. The values are merged
into your project’s stack settings file.

Use the `spec.secretsRef` block to set configuration values containing secrets.
The value may be a literal value or may be a reference to a Kubernetes `Secret`.

Use the `spec.secretsProvider` field to use an alternative encryption provider.
See ["Initializing a stack with alternative encryption"][iac-secrets-provider] for more information.

[iac-config]: https://www.pulumi.com/docs/iac/concepts/config/

[iac-secrets-provider]: https://www.pulumi.com/docs/intro/concepts/secrets/#initializing-a-stack-with-alternative-encryption

### Environment Variables

Use the `spec.envRefs` field to set environment variables for the Pulumi program,
such as `PULUMI_ACCESS_TOKEN` or `AWS_SECRET_ACCESS_KEY`.

Values may be literals or based on the contents of a `ConfigMap` or `Secret` object.

### Drift Detection

Drift detection means to detect unwanted changes to your provisioned infrastructure.
The operator supports drift detection and remediation by periodically running `pulumi up`. This is referred to as re-synchronization.

Use the `spec.continueResyncOnCommitMatch` field to enable periodic resyncs. Use the `spec.resyncFrequencySeconds` field to set the resync frequency.

### State Refresh

Use the `spec.refresh` field to refresh the state of the stack's resources before each update.

{{< notes type="info" >}}
  It is recommended that `spec.refresh` be enabled.
{{< /notes >}}

### Stack Cleanup

Use the `spec.destroyOnFinalize` field to automatically destroy the Pulumi stack (i.e. `pulumi destroy -f`)
when the `Stack` object is deleted. Enable this option to link the lifecycle of the Pulumi stack, and the resources it contains, to its `Stack` object.

{{< notes type="info" >}}
  Stack object deletion is slower when this option is enabled, because a Pulumi deployment operation
  must be run during object finalization.
{{< /notes >}}

### Stack Prerequisites

It is possible to declare that a particular `Stack` be dependent on another `Stack`.
The dependent stack waits for the other stack to be successfully deployed.
Use the `succeededWithinDuration` field to set a duration within which the prerequisite must have reached success; otherwise the dependency is automatically re-synced.

### External Triggers

It is possible to trigger a stack update for a stack at any time by applying
the `pulumi.com/reconciliation-request` annotation:

```bash
kubectl annotate stack $STACK_NAME "pulumi.com/reconciliation-request=$(date)" --overwrite  
```

The value of the annotation is arbitrary, and we recommend using a timestamp.

## Use With Argo CD

We can use ArgoCD in combination with PKO to manage the lifetime of the Stack via the GitOps paradigm. This gives you the ability to use the ArgoCD UI or CLI to interact with the Stack, and to allow ArgoCD to reconcile changes to the Stack specification. The Pulumi Kubernetes Operator handles the details.

First, we need to define a Pulumi stack as a Kubernetes manifest that ArgoCD can deploy. We assume here that this manifest lives in the same repository as the Pulumi program, in the subfolder `deploy/`.  However, this manifest could live in a separate repository, such as an "app-of-apps" repo. In this example, the manifest declares a service account and cluster role bindings to allow the stack to create resources in the cluster. Additionally, we expect a Secret to exist on the cluster containing a Pulumi access token.

Note that the Stack's `projectRepo` and `branch` point to the location of the Pulumi program to be executed by the Pulumi Kubernetes Operator.

```yaml
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-app:system:auth-delegator
  annotations:
    argocd.argoproj.io/sync-wave: "2"
  labels:
    app.kubernetes.io/instance: my-app
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: system:auth-delegator
subjects:
- kind: ServiceAccount
  name: my-app
  namespace: some-namepace
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: my-app:cluster-admin
  annotations:
    argocd.argoproj.io/sync-wave: "2"
  labels:
    app.kubernetes.io/instance: my-app
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
- kind: ServiceAccount
  name: my-app
  namespace: some-namepace
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-app-dev
  namespace: some-namepace
  labels:
    app.kubernetes.io/instance: my-app
  annotations:
    argocd.argoproj.io/sync-wave: "3"
    pulumi.com/reconciliation-request: "before-first-update"
    link.argocd.argoproj.io/external-link: http://app.pulumi.com/my-org/my-prject/dev
spec:
  serviceAccountName: my-app
  stack: my-org/my-project/dev
  projectRepo: "https://github.com/my-repo/my-app.git"
  branch: main
  refresh: true
  resyncFrequencySeconds: 60
  destroyOnFinalize: true
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-access-token-secret
        key: PULUMI_ACCESS_TOKEN
  workspaceTemplate:
    spec:
      image: pulumi/pulumi:3.134.1-nonroot
```

Next we create an ArgoCD `Application` object:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
  finalizers:
    # best practice: use background cascading deletion when destroyOnFinalize is enabled.
    - resources-finalizer.argocd.argoproj.io/background
spec:
  destination:
    namespace: default
    server: "https://kubernetes.default.svc"
  syncPolicy:
    automated:
      prune: true
  project: default
  source:
    repoURL: "https://github.com/my-repo/my-app.git"
    path: "./deploy"  # the location of the Stack maifest
    targetRevision: main
```

ArgoCD will sync the `Application` by applying the `Stack` object,
which will in turn effect a Pulumi deployment. The result will look something like this in the ArgoCD UI:

![ArgoCD PKO Example](/images/docs/reference/argocd/pko-example.png)

## More Information

### Examples

More examples are available in the [pulumi/pulumi-kubernetes-operator][pko-examples] repository.

[pko-examples]: https://github.com/pulumi/pulumi-kubernetes-operator/tree/master/examples

### Getting Help

Check out [troubleshooting](https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/troubleshooting.md) for more details, look at [known issues](https://github.com/pulumi/pulumi-kubernetes-operator/issues/) or
open a [new issue](https://github.com/pulumi/pulumi-kubernetes-operator/issues/new) in GitHub.
