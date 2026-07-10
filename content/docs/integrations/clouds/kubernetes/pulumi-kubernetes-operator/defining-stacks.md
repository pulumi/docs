---
title_tag: "Defining stacks | Pulumi Kubernetes Operator"
meta_desc: Create a Pulumi Stack resource from a Git repository, Flux source, or Program object, and set its configuration and environment variables.
title: Defining stacks
h1: "Pulumi Kubernetes Operator: Defining stacks"
menu:
    integrations:
        parent: kubernetes-clouds-operator
        identifier: kubernetes-clouds-operator-defining-stacks
        weight: 2
---

The `Stack` resource encapsulates a Pulumi project to provision infrastructure resources such as cloud VMs, object storage, and Kubernetes clusters and their workloads.

Set the `spec.serviceAccountName` field to the name of a `ServiceAccount` with the requisite permissions.

Set the `spec.stack` field to a unique Pulumi stack name, using a [supported format][].

[supported format]: https://www.pulumi.com/docs/iac/concepts/stacks/#create-stack

## Using a Git repository

In this scenario, the stack draws on a Git repository for the program source code.

The `Stack` specification can specify a commit SHA (`spec.commit`) or a branch reference (`spec.branch`). The repository URL is specified with `spec.projectRepo` plus an optional `spec.repoDir`.

If a branch reference is specified, the operator will periodically poll the branch for any new commits
and roll out updates as they are found. Use the `spec.resyncFrequencySeconds` field to set the polling frequency.

Specify Git authentication options with the `spec.gitAuth` field.

In the example below, we're creating a `Stack` for a Pulumi project called `kubernetes-ts-nginx` to deploy a simple [NGINX][nginx-stack] server to your cluster. Without any configuration, the [Kubernetes Provider][k8s-provider] uses the in-cluster Kubernetes context.

[nginx-stack]: https://github.com/pulumi/examples/blob/master/kubernetes-ts-nginx/index.ts
[k8s-provider]: /registry/packages/kubernetes/api-docs/provider/

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

## Using a Flux source

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
[flux-source]: https://fluxcd.io/flux/components/source/
[flux-install]: https://fluxcd.io/flux/installation/

## Using a Program object

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
      type: aws:s3:Bucket
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

## Stack configuration values

In many cases, different stacks for a single project will need differing values.
For instance, you may want to use a different size for your AWS EC2 instance, or a different number of replicas
for a particular Kubernetes deployment. Pulumi offers a configuration system for managing such differences;
see ["Configuration"][iac-config] for more information.

Use the `spec.config` block to set stack configuration values. The values are merged
into your project's stack settings file.

Use the `spec.secretsRef` block to set configuration values containing secrets.
The value may be a literal value or may be a reference to a Kubernetes `Secret`.

Use the `spec.secretsProvider` field to use an alternative encryption provider.
See ["Initializing a stack with alternative encryption"][iac-secrets-provider] for more information.

Use the `spec.retryMaxBackoffDurationSeconds` field to control the maximum backoff duration for failed updates. This defaults to one update attempt per day (86400 seconds) but can be adjusted for faster retry cycles during development.

To customize the retention of Update objects created by the Stack controller, use the `spec.updateTemplate` field to set labels, annotations, and TTL (time-to-live) policies. See the [Update CR documentation][pko-updates] for details.

[iac-config]: https://www.pulumi.com/docs/iac/concepts/config/
[iac-secrets-provider]: https://www.pulumi.com/docs/intro/concepts/secrets/#initializing-a-stack-with-alternative-encryption
[pko-updates]: https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/docs/updates.md

## Structured configuration

In addition to string values, Stack configuration supports complex data types including objects, arrays, numbers, and booleans. This enhancement allows you to express sophisticated configuration structures inline in your Stack manifests or load them from ConfigMaps with automatic JSON parsing.

This feature requires Pulumi CLI v3.202.0 or later in your workspace pods. The operator provides automatic version detection with clear upgrade guidance when needed.

Here's an example with inline structured configuration:

```yaml
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-app
spec:
  serviceAccountName: pulumi
  stack: my-org/my-app/prod
  projectRepo: https://github.com/example/app
  branch: main
  config:
    # String values (existing behavior)
    environment: "production"

    # Objects (NEW)
    database:
      host: "db.example.com"
      port: 5432
      ssl: true

    # Arrays (NEW)
    regions: ["us-west-2", "us-east-1", "eu-west-1"]

    # Numbers and booleans (NEW)
    maxConnections: 100
    enableCaching: true
  envRefs:
    PULUMI_ACCESS_TOKEN:
      type: Secret
      secret:
        name: pulumi-api-secret
        key: accessToken
```

You can also reference ConfigMaps for complex configurations using the `json: true` flag:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-settings
data:
  database.json: |
    {
      "host": "db.example.com",
      "port": 5432,
      "maxConnections": 100
    }
---
apiVersion: pulumi.com/v1
kind: Stack
metadata:
  name: my-app
spec:
  serviceAccountName: pulumi
  stack: my-org/my-app/prod
  projectRepo: https://github.com/example/app
  branch: main
  configRefs:
    database:
      name: app-settings
      key: database.json
      json: true  # Parse as JSON
```

Note that Secrets are not a supported source of structured configuration values.

## Environment variables

Use the `spec.envRefs` field to set environment variables for the Pulumi program,
such as `PULUMI_ACCESS_TOKEN` or `AWS_SECRET_ACCESS_KEY`.

Values may be literals or based on the contents of a `ConfigMap` or `Secret` object.

You can also set environment variables dynamically through init containers by writing to the `$PULUMI_ENV` file. Environment variables set this way affect the Pulumi CLI during deployment operations:

```yaml
spec:
  workspaceTemplate:
    spec:
      initContainers:
        - name: setup-env
          image: busybox
          command:
            - sh
            - -c
            - |
              echo "PULUMI_CONFIG_PASSPHRASE=my-passphrase" >> $PULUMI_ENV
              echo "MY_CUSTOM_VAR=value" >> $PULUMI_ENV
```
