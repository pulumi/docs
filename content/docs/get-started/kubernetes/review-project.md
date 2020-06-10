---
title: Review the New Project | Kubernetes
h1: Review the New Project
linktitle: Review the New Project
meta_desc: This page provides an overview on how to review a new Kubernetes project.
weight: 4
menu:
  getstarted:
    parent: kubernetes
    identifier: kubernetes-review-project

aliases: ["/docs/quickstart/kubernetes/review-project/"]
---

Let's review some of the generated project files:

- `Pulumi.yaml` defines the [project]({{< relref "/docs/intro/concepts/project" >}}).
- `Pulumi.dev.yaml` contains [configuration]({{< relref "/docs/intro/concepts/config" >}}) values for the [stack]({{< relref "/docs/intro/concepts/stack" >}}) we initialized.

{{% choosable language csharp %}}

- `Program.cs` with a simple entry point.

{{% /choosable %}}

- {{< langfile >}} is the Pulumi program that defines our stack resources. Let's examine it.

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const k8s = require("@pulumi/kubernetes");

const appLabels = { app: "nginx" };
const deployment = new k8s.apps.v1.Deployment("nginx", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: { containers: [{ name: "nginx", image: "nginx" }] }
        }
    }
});
exports.name = deployment.metadata.name;
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as k8s from "@pulumi/kubernetes";

const appLabels = { app: "nginx" };
const deployment = new k8s.apps.v1.Deployment("nginx", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: { containers: [{ name: "nginx", image: "nginx" }] }
        }
    }
});
export const name = deployment.metadata.name;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
"""
Creating a Kubernetes Deployment
"""
import pulumi
from pulumi_kubernetes.apps.v1 import Deployment

app_labels = { "app": "nginx" }

deployment = Deployment(
    "nginx",
    spec={
        "selector": { "match_labels": app_labels },
        "replicas": 1,
        "template": {
            "metadata": { "labels": app_labels },
            "spec": { "containers": [{ "name": "nginx", "image": "nginx" }] }
        }
    })

pulumi.export("name", deployment.metadata["name"])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/apps/v1"
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/core/v1"
    metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v2/go/kubernetes/meta/v1"
    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {

        appLabels := pulumi.StringMap{
            "app": pulumi.String("nginx"),
        }
        deployment, err := appsv1.NewDeployment(ctx, "app-dep", &appsv1.DeploymentArgs{
            Spec: appsv1.DeploymentSpecArgs{
                Selector: &metav1.LabelSelectorArgs{
                    MatchLabels: appLabels,
                },
                Replicas: pulumi.Int(1),
                Template: &corev1.PodTemplateSpecArgs{
                    Metadata: &metav1.ObjectMetaArgs{
                        Labels: appLabels,
                    },
                    Spec: &corev1.PodSpecArgs{
                        Containers: corev1.ContainerArray{
                            corev1.ContainerArgs{
                                Name:  pulumi.String("nginx"),
                                Image: pulumi.String("nginx"),
                            }},
                    },
                },
            },
        })
        if err != nil {
            return err
        }

        ctx.Export("name", deployment.Metadata.Elem().Name())

        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Kubernetes.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

class MyStack : Stack
{
    public MyStack()
    {
        var appLabels = new InputMap<string>
        {
            { "app", "nginx" }
        };

        var deployment = new Pulumi.Kubernetes.Apps.V1.Deployment("nginx", new DeploymentArgs
        {
            Spec = new DeploymentSpecArgs
            {
                Selector = new LabelSelectorArgs
                {
                    MatchLabels = appLabels
                },
                Replicas = 1,
                Template = new PodTemplateSpecArgs
                {
                    Metadata = new ObjectMetaArgs
                    {
                        Labels = appLabels
                    },
                    Spec = new PodSpecArgs
                    {
                        Containers =
                        {
                            new ContainerArgs
                            {
                                Name = "nginx",
                                Image = "nginx",
                                Ports =
                                {
                                    new ContainerPortArgs
                                    {
                                        ContainerPortValue = 80
                                    }
                                }
                            }
                        }
                    }
                }
            }
        });

        this.Name = deployment.Metadata.Apply(m => m.Name);
    }

    [Output]
    public Output<string> Name { get; set; }
}
```

{{% /choosable %}}

This Pulumi program creates an NGINX deployment and exports the name of the deployment.

Next, we'll deploy the stack.

{{< get-started-stepper >}}
