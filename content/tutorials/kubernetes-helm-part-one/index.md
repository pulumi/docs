---
title_tag: How to Install Helm Charts on Kubernetes with Pulumi - Part 1
allow_long_title: true
title: How to Install Helm Charts on Kubernetes with Pulumi - Part 1
layout: single
description: |
  Using Pulumi to install Helm Charts on Kubernetes is a great way to manage to install third-party applications on your Kubernetes cluster.
meta_desc: Using Pulumi to install Helm Charts on Kubernetes is a great way to manage to install third-party applications on your Kubernetes cluster.
meta_image: meta.png
weight: 999
summary: |
  If you worked with Pulumi and [Kubernetes](https://kubernetes.io/), you probably know that Pulumi has a [Kubernetes provider](/docs/iac/get-started/kubernetes/) that allows you to deploy Kubernetes resources.

  In this tutorial, we will learn how to install Helm on Kubernetes using Pulumi. [Helm](https://helm.sh/) is a package manager for Kubernetes that allows you to install and manage applications on your Kubernetes cluster.

  Most of the third-party applications that you want to install on your Kubernetes cluster, like whole monitoring stacks, databases, and other applications, are most likely available as Helm charts.

  On services like [Artifact Hub](https://artifacthub.io/), you can find a lot of Helm charts that you can use to install applications on your Kubernetes cluster.

  The Pulumi Kubernetes provider offers two different ways to install Helm on Kubernetes:

  - Using the `Release` resource
  - Using the `Chart` resource

  The Helm [Chart](/registry/packages/kubernetes/api-docs/helm/v4/chart) resource renders the templates from your chart and then manages the objects directly with the Pulumi Kubernetes provider.

  The Helm [Release](/registry/packages/kubernetes/api-docs/helm/v4/release) resource uses the Helm SDK to install the Helm chart on your Kubernetes cluster.
youll_learn:
- How to install Helm on Kubernetes using Pulumi

estimated_time: 10
collections_weight: 2
prereqs:
- "A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)"
- "The [Pulumi CLI](/docs/install/)"
- "A Kubernetes cluster (for example, [kind](https://kind.sigs.k8s.io/))"
- "[kubectl](https://kubernetes.io/releases/download/#kubectl)"
- "[helm](https://helm.sh/docs/intro/install/)"
---

## Never heard of Helm?

What is Helm? Helm is a package manager for Kubernetes and a Helm chart is a collection of different Kubernetes (like Deployment, Service, Ingress, etc.) resources that are bundled together and can be deployed as a unit.

There are many ways to share Helm charts, but the most popular way is by using a Helm repository. Recently Helm supports also OCI registries as a way to share the Helm chart as an OCI artifact.

Additionally, Helm has a templating engine that allows you to customize the Helm chart before you deploy it. It is based on the go templating engine (plus Sprig functions) and allows you to customize the Helm chart based on your needs.

> This templating engine is also the reason why some folks are avoiding Helm. Things can get pretty complex if not taken care.

## Deploying a Helm chart with Pulumi

To start, [login to the Pulumi CLI](/tutorials/cli-authentication/) and create a new Pulumi project. You can use the following command to create a new Pulumi project and select from the list of templates the `helm-kubernetes-<your-programming-language>` template.

```bash
# Choose your favorite Pulumi supported language
pulumi new helm-kubernetes-<your-programming-language>
```

This will create a new Pulumi project with the necessary files to deploy Kubernetes resources and some example resources.

{{< chooser language "typescript,python,go,csharp,yaml" />}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const config = new pulumi.Config();
const k8sNamespace = config.get("k8sNamespace") || "nginx-ingress";
const appLabels = {
    app: "nginx-ingress",
};

// Create a namespace (user supplies the name of the namespace)
const ingressNs = new kubernetes.core.v1.Namespace("ingressns", {metadata: {
    labels: appLabels,
    name: k8sNamespace,
}});

// Use Helm to install the Nginx ingress controller
const ingressController = new kubernetes.helm.v3.Release("ingresscontroller", {
    chart: "nginx-ingress",
    namespace: ingressNs.metadata.name,
    repositoryOpts: {
        repo: "https://helm.nginx.com/stable",
    },
    skipCrds: true,
    values: {
        controller: {
            enableCustomResources: false,
            appprotect: {
                enable: false,
            },
            appprotectdos: {
                enable: false,
            },
            service: {
                extraLabels: appLabels,
            },
        },
    },
    version: "0.14.1",
});

// Export some values for use elsewhere
export const name = ingressController.name;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_kubernetes as kubernetes

config = pulumi.Config()
k8s_namespace = config.get("k8sNamespace", "default")
app_labels = {
    "app": "nginx-ingress",
}

# Create a namespace (user supplies the name of the namespace)
ingress_ns = kubernetes.core.v1.Namespace(
    "ingressns",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels=app_labels,
        name=k8s_namespace,
    )
)

# Use Helm to install the Nginx ingress controller
ingresscontroller = kubernetes.helm.v3.Release(
    "ingresscontroller",
    chart="nginx-ingress",
    namespace=ingress_ns.metadata.name,
    repository_opts={
        "repo": "https://helm.nginx.com/stable",
    },
    skip_crds=True,
    values={
        "controller": {
            "enableCustomResources": False,
            "appprotect": {
                "enable": False,
            },
            "appprotectdos": {
                "enable": False,
            },
            "service": {
                "extraLabels": app_labels,
            },
        },
    },
    version="0.14.1"
)

# Export some values for use elsewhere
pulumi.export("name", ingresscontroller.name)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		cfg := config.New(ctx, "")
		k8sNamespace, err := cfg.Try("k8sNamespace")
		if err != nil {
			k8sNamespace = "nginx-ingress"
		}
		appLabels := pulumi.StringMap{
			"app": pulumi.String("nginx-ingress"),
		}

		// Create a new namespace (user supplies the name of the namespace)
		ingressNs, err := corev1.NewNamespace(ctx, "ingressns", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Labels: pulumi.StringMap(appLabels),
				Name:   pulumi.String(k8sNamespace),
			},
		})
		if err != nil {
			return err
		}

		// Use Helm to install the Nginx ingress controller
		ingresscontroller, err := helmv3.NewRelease(ctx, "ingresscontroller", &helmv3.ReleaseArgs{
			Chart:     pulumi.String("nginx-ingress"),
			Namespace: ingressNs.Metadata.Name(),
			RepositoryOpts: &helmv3.RepositoryOptsArgs{
				Repo: pulumi.String("https://helm.nginx.com/stable"),
			},
			SkipCrds: pulumi.Bool(true),
			Values: pulumi.Map{
				"controller": pulumi.Map{
					"enableCustomResources": pulumi.Bool(false),
					"appprotect": pulumi.Map{
						"enable": pulumi.Bool(false),
					},
					"appprotectdos": pulumi.Map{
						"enable": pulumi.Bool(false),
					},
					"service": pulumi.Map{
						"extraLabels": appLabels,
					},
				},
			},
			Version: pulumi.String("0.14.1"),
		})
		if err != nil {
			return err
		}

		// Export some values for use elsewhere
		ctx.Export("name", ingresscontroller.Name)
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var config = new Config();
    var k8sNamespace = config.Get("k8sNamespace") ?? "nginx-ingress";
    var appLabels = new InputMap<string>
    {
        { "app", "nginx-ingress" },
    };

    var ingressns = new Kubernetes.Core.V1.Namespace("ingressns", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels = appLabels,
            Name = k8sNamespace,
        },
    });

    var ingresscontroller = new Kubernetes.Helm.V3.Release("ingresscontroller", new()
    {
        Chart = "nginx-ingress",
        Namespace = ingressns.Metadata.Apply(m => m.Name),
        RepositoryOpts = new Kubernetes.Types.Inputs.Helm.V3.RepositoryOptsArgs
        {
            Repo = "https://helm.nginx.com/stable",
        },
        SkipCrds = true,
        Values = new Dictionary<string, object>
        {
            ["controller"] = new Dictionary<string, object>
            {
                ["enableCustomResources"] = "false",
                ["appprotect"] = new Dictionary<string, object>
                {
                    ["enable"] = "false"
                },
                ["appprotectdos"] = new Dictionary<string, object>
                {
                    ["enable"] = "false"
                },
                ["service"] = new Dictionary<string, object>
                {
                    ["extraLabels"] = appLabels
                },
            },
        },
        Version = "0.14.1",
    });

    return new Dictionary<string, object?>
    {
        ["name"] = ingresscontroller.Name,
    };
});
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: ${PROJECT}
description: ${DESCRIPTION}
runtime: yaml
template:
  description: A Pulumi YAML program to deploy a Helm chart onto a Kubernetes cluster
  config:
    k8sNamespace:
      default: nginx-ingress
      description: The Kubernetes namespace to deploy into

config:
  # Use this user-supplied value to create a Kubernetes namespace later
  k8sNamespace:
    default: nginx-ingress
    type: string

variables:
  # Define some labels that will be applied to resources
  appLabels:
    app: nginx-ingress

resources:
  # Create a namespace (name of the namespace supplied by the user)
  ingressns:
    type: kubernetes:core/v1:Namespace
    properties:
      metadata:
        labels: ${appLabels}
        name: ${k8sNamespace}
  # Use Helm to install the Nginx ingress controller
  ingresscontroller:
    type: kubernetes:helm.sh/v3:Release
    properties:
      chart: nginx-ingress
      namespace: ${ingressns.metadata.name}
      repositoryOpts:
        repo: https://helm.nginx.com/stable
      skipCrds: true
      values:
        controller:
          enableCustomResources: false
          appprotect:
            enable: false
          appprotectdos:
            enable: false
          service:
            extraLabels: ${appLabels}
      version: "0.14.1"

# Export some values for use elsewhere
outputs:
    name: ${ingresscontroller.name}
```

{{% /choosable %}}

## Deploying the Helm chart

Now run the `pulumi up` command to preview and deploy the resources you’ve just defined in your project.

```bash
pulumi up
Please choose a stack, or create a new one: dev
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/dirien/helm/dev/previews/88cf6d4c-d4a4-401f-9b25-cedd50146545

     Type                              Name               Plan
 +   pulumi:pulumi:Stack               helm-dev           create
 +   ├─ kubernetes:core/v1:Namespace   ingressns          create
 +   └─ kubernetes:helm.sh/v3:Release  ingresscontroller  create

Outputs:
    name: "ingresscontroller-7e4b854f"

Resources:
    + 3 to create

Do you want to perform this update? yes
Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/dirien/helm/dev/updates/1

     Type                              Name               Status
 +   pulumi:pulumi:Stack               helm-dev           created (15s)
 +   ├─ kubernetes:core/v1:Namespace   ingressns          created (0.32s)
 +   └─ kubernetes:helm.sh/v3:Release  ingresscontroller  created (7s)

Outputs:
    name: "ingresscontroller-b5455c41"

Resources:
    + 3 created

Duration: 17s
```

After the deployment is complete, you can check the resources in your Kubernetes cluster.

```bash
kubectl get all -n nginx-ingress
```

And you should see the resources that were created by the Helm chart.

```bash
NAME                                                            READY   STATUS    RESTARTS   AGE
pod/ingresscontroller-b5455c41-nginx-ingress-5987c7bd56-57bph   1/1     Running   0          104s

NAME                                               TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
service/ingresscontroller-b5455c41-nginx-ingress   LoadBalancer   10.103.162.34   localhost     80:30725/TCP,443:31959/TCP   105s

NAME                                                       READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/ingresscontroller-b5455c41-nginx-ingress   1/1     1            1           104s

NAME                                                                  DESIRED   CURRENT   READY   AGE
replicaset.apps/ingresscontroller-b5455c41-nginx-ingress-5987c7bd56   1         1         1       104s
```

## Deploying a OCI Helm chart with Pulumi

In the previous example, we deployed a Helm chart from a Helm repository. Helm supports also [OCI registries](https://helm.sh/blog/storing-charts-in-oci/) as a way to share Helm charts. The changes in the Pulumi program are minimal.

```typescript
// omitting the namespace creation for brevity
const nodered = new k8s.helm.v3.Release("node-red", {
    name: "node-red",
    chart: "oci://ghcr.io/schwarzit/charts/node-red",
    namespace: "node-red",
    createNamespace: true,
});
```

The `chart` property now points to the OCI registry where the Helm chart is stored and you add the `oci://` prefix to the chart URL. You can also drop the `repositoryOpts` property since it is not needed when you deploy a Helm chart from an OCI registry.

## Housekeeping

Before moving on, tear down the resources that are part of your stack to avoid incurring any charges.

1. Run `pulumi destroy` to tear down all resources. You'll be prompted to make sure you really want to delete these resources. A destroy operation may take some time, since Pulumi waits for the resources to finish shutting down before it considers the destroy operation to be complete.
2. To delete the stack itself, run `pulumi stack rm`. Note that this command deletes all deployment history from the Pulumi Service.

## Next steps

In this tutorial, you learned how to install Helm on Kubernetes using the Kubernetes provider from Pulumi and the `Release` resource.
