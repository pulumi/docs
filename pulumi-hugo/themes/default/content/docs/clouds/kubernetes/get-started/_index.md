---
title_tag: Kubernetes get started
meta_desc: This page provides an overview and guide on how to get started with Kubernetes.
title: Get started
h1: Get Started with Kubernetes & Pulumi
menu:
  clouds:
    identifier: kubernetes-get-started
    parent: kube
    weight: 4
aliases:
- /docs/quickstart/kubernetes/
- /docs/get-started/kubernetes/
- /docs/get-started/kubernetes/begin/
- /docs/quickstart/kubernetes/create-project/
- /docs/get-started/kubernetes/create-project/
- /docs/quickstart/kubernetes/review-project/
- /docs/get-started/kubernetes/review-project/
- /docs/quickstart/kubernetes/deploy-stack/
- /docs/get-started/kubernetes/deploy-stack/
- /docs/quickstart/kubernetes/modify-program/
- /docs/get-started/kubernetes/modify-program/
- /docs/quickstart/kubernetes/deploy-changes/
- /docs/get-started/kubernetes/deploy-changes/
- /docs/quickstart/kubernetes/destroy-stack/
- /docs/get-started/kubernetes/destroy-stack/
- /docs/quickstart/kubernetes/next-steps/
- /docs/get-started/kubernetes/next-steps/
---

Pulumi's infrastructure-as-code SDK helps you create, deploy, and manage AWS containers, serverless functions, and infrastructure using familiar programming languages.

Pulumi supports programming against Kubernetes---Minikube, on-premises and
cloud-hosted custom Kubernetes clusters, and the managed services from Google
(GKE), Azure (AKS), and Amazon (EKS).

This tutorial takes you through the steps to easily deploy an [NGINX](https://www.nginx.com/) web server:

## Install Pulumi

{{< install-pulumi >}}
{{% notes "info" %}}
All Windows examples in this tutorial assume you are running in PowerShell.
{{% /notes %}}
{{< /install-pulumi >}}

### Install language runtime

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language "javascript,typescript" %}}
Install [Node.js](https://nodejs.org/en/download).
{{% /choosable %}}

{{% choosable language python %}}
{{< install-python >}}
{{% /choosable %}}

{{% choosable language go %}}
{{< install-go >}}
{{% /choosable %}}

{{% choosable language "csharp,fsharp,visualbasic" %}}
{{< install-dotnet >}}
{{% /choosable %}}

{{% choosable language "java" %}}
{{< install-java >}}
{{% /choosable %}}

{{% choosable language "yaml" %}}
{{< install-yaml >}}
{{% /choosable %}}

{{< /chooser >}}

### Configure Kubernetes

<a href="/registry/packages/kubernetes/installation-configuration" target="_blank">Configure Kubernetes</a> so the Pulumi CLI can connect to a Kubernetes cluster. If you have previously configured `kubectl`, Pulumi will respect and use your configuration settings.

## Create project

Let's create your first Pulumi project, stack, and program. Pulumi [projects](/docs/concepts/projects/) and [stacks](/docs/concepts/stack/) organize Pulumi code. Projects are similar to GitHub repos and stacks are an instance of code with separate configuration. Projects can have multiple stacks for different development environments or for different cloud configurations.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-javascript
```

{{% /choosable %}}
{{% choosable language typescript %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-typescript
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-python
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-go
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-csharp
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-java
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ mkdir quickstart && cd quickstart
$ pulumi new kubernetes-yaml
```

{{% /choosable %}}
{{< /chooser >}}

You will be asked for a **project name** and **project description**.

```
This command will walk you through creating a Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name: (quickstart)
project description: (A minimal Kubernetes Pulumi program)
Created project 'quickstart'
```

Then you will be asked for a **stack name**.

```
Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name: (dev)
Created stack 'dev'
```

## Review project

Let's review some of the generated project files:

{{% choosable language "javascript,typescript,python,go,csharp,java" %}}

- `Pulumi.yaml` defines the [project](/docs/concepts/projects/).

{{% /choosable %}}

{{% choosable language yaml %}}

- `Pulumi.yaml` defines both the [project](/docs/concepts/projects/) and the program that manages your stack resources.

{{% /choosable %}}

- `Pulumi.dev.yaml` contains [configuration](/docs/concepts/config/) values for the [stack](/docs/concepts/stack/) we initialized.

{{% choosable language java %}}

- `src/main/java/myproject` defines the project's Java package root.

{{% /choosable %}}

{{% choosable language "javascript,typescript,python,go,csharp,java" %}}

<!-- The wrapping spans are infortunately necessary here; without them, the renderer gets confused and generates invalid markup. -->
- <span>{{< langfile >}}</span> is the Pulumi program that defines your stack resources.

{{% /choosable %}}

Let's examine {{< langfile >}}.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs
from pulumi_kubernetes.core.v1 import ContainerArgs, PodSpecArgs, PodTemplateSpecArgs

app_labels = { "app": "nginx" }

deployment = Deployment(
    "nginx",
    spec=DeploymentSpecArgs(
        selector=LabelSelectorArgs(match_labels=app_labels),
        replicas=1,
        template=PodTemplateSpecArgs(
            metadata=ObjectMetaArgs(labels=app_labels),
            spec=PodSpecArgs(containers=[ContainerArgs(name="nginx", image="nginx")])
        ),
    ))

pulumi.export("name", deployment.metadata["name"])
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
    metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
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
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
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

    // export the deployment name
    return new Dictionary<string, object?>
    {
        ["name"] =  deployment.Metadata.Apply(m => m.Name)
    };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.kubernetes.apps_v1.Deployment;
import com.pulumi.kubernetes.apps_v1.DeploymentArgs;
import com.pulumi.kubernetes.apps_v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.core_v1.inputs.ContainerArgs;
import com.pulumi.kubernetes.core_v1.inputs.ContainerPortArgs;
import com.pulumi.kubernetes.core_v1.inputs.PodSpecArgs;
import com.pulumi.kubernetes.core_v1.inputs.PodTemplateSpecArgs;
import com.pulumi.kubernetes.meta_v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaArgs;

import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var labels = Map.of("app", "nginx");

            var deployment = new Deployment("nginx", DeploymentArgs.builder()
                    .spec(DeploymentSpecArgs.builder()
                            .selector(LabelSelectorArgs.builder()
                                    .matchLabels(labels)
                                    .build())
                            .replicas(1)
                            .template(PodTemplateSpecArgs.builder()
                                    .metadata(ObjectMetaArgs.builder()
                                            .labels(labels)
                                            .build())
                                    .spec(PodSpecArgs.builder()
                                            .containers(ContainerArgs.builder()
                                                    .name("nginx")
                                                    .image("nginx")
                                                    .ports(ContainerPortArgs.builder()
                                                            .containerPort(80)
                                                            .build())
                                                    .build())
                                            .build())
                                    .build())

                            .build())
                    .build());

            var name = deployment.metadata()
                .applyValue(m -> m.orElseThrow().name().orElse(""));

            ctx.export("name", name);
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: quickstart
runtime: yaml
description: A minimal Kubernetes Pulumi YAML program

variables:
  appLabels:
    app: nginx

resources:
  deployment:
    name: nginx
    type: kubernetes:apps/v1:Deployment
    properties:
      spec:
        selector:
          matchLabels: ${appLabels}
        replicas: 1
        template:
          metadata:
            labels: ${appLabels}
          spec:
            containers:
              - name: nginx
                image: nginx

outputs:
  name: ${deployment.metadata.name}
```

{{% /choosable %}}
{{< /chooser >}}

This Pulumi program creates an NGINX deployment and exports the name of the deployment.

## Deploy stack

Let's deploy the stack:

```bash
$ pulumi up
```

This command evaluates the program and determines what resources need updates. A preview is shown that outlines the changes that will be made when you run the update:

```
Previewing update (dev):

     Type                           Name            Plan
 +   pulumi:pulumi:Stack            quickstart-dev  create
 +   └─ kubernetes:apps:Deployment  nginx           create

Resources:
    + 2 to create

Do you want to perform this update?
  yes
> no
  details
```

Choosing `yes` will create resources in Kubernetes.

```
Do you want to perform this update? yes
Updating (dev):

     Type                           Name            Status
 +   pulumi:pulumi:Stack            quickstart-dev  created
 +   └─ kubernetes:apps:Deployment  nginx           created

Outputs:
    name: "nginx-xw231xdt"

Resources:
    + 2 created

Duration: 11s
```

The name of the deployment that we exported is shown as a [stack output](/docs/concepts/stack#outputs).

## Modify program

Now that we have an instance of our Pulumi program deployed, let's update it. Replace the contents of {{< langfile >}} with the following:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
"use strict";
const pulumi = require("@pulumi/pulumi");
const k8s = require("@pulumi/kubernetes");

// Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
// running on minikube, and if so, create only services of type ClusterIP.
const config = new pulumi.Config();
const isMinikube = config.requireBoolean("isMinikube");

const appName = "nginx";
const appLabels = { app: appName };
const deployment = new k8s.apps.v1.Deployment(appName, {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: { containers: [{ name: appName, image: "nginx" }] }
        }
    }
});

// Allocate an IP to the Deployment.
const frontend = new k8s.core.v1.Service(appName, {
    metadata: { labels: deployment.spec.template.metadata.labels },
    spec: {
        type: isMinikube ? "ClusterIP" : "LoadBalancer",
        ports: [{ port: 80, targetPort: 80, protocol: "TCP" }],
        selector: appLabels
    }
});

// When "done", this will print the public IP.
exports.ip = isMinikube
    ? frontend.spec.clusterIP
    : frontend.status.loadBalancer.apply(
          (lb) => lb.ingress[0].ip || lb.ingress[0].hostname
      );
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

// Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
// running on minikube, and if so, create only services of type ClusterIP.
const config = new pulumi.Config();
const isMinikube = config.requireBoolean("isMinikube");

const appName = "nginx";
const appLabels = { app: appName };
const deployment = new k8s.apps.v1.Deployment(appName, {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: { containers: [{ name: appName, image: "nginx" }] }
        }
    }
});

// Allocate an IP to the Deployment.
const frontend = new k8s.core.v1.Service(appName, {
    metadata: { labels: deployment.spec.template.metadata.labels },
    spec: {
        type: isMinikube ? "ClusterIP" : "LoadBalancer",
        ports: [{ port: 80, targetPort: 80, protocol: "TCP" }],
        selector: appLabels
    }
});

// When "done", this will print the public IP.
export const ip = isMinikube
    ? frontend.spec.clusterIP
    : frontend.status.loadBalancer.apply(
          (lb) => lb.ingress[0].ip || lb.ingress[0].hostname
      );
```

{{% /choosable %}}
{{% choosable language python %}}

```python
"""
Creating a Kubernetes Deployment
"""
import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service

# Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
# running on minikube, and if so, create only services of type ClusterIP.
config = pulumi.Config()
is_minikube = config.require_bool("isMinikube")

app_name = "nginx"
app_labels = { "app": app_name }

deployment = Deployment(
    app_name,
    spec={
        "selector": { "match_labels": app_labels },
        "replicas": 1,
        "template": {
            "metadata": { "labels": app_labels },
            "spec": { "containers": [{ "name": app_name, "image": "nginx" }] }
        }
    })

# Allocate an IP to the Deployment.
frontend = Service(
    app_name,
    metadata={
        "labels": deployment.spec["template"]["metadata"]["labels"],
    },
    spec={
        "type": "ClusterIP" if is_minikube else "LoadBalancer",
        "ports": [{ "port": 80, "target_port": 80, "protocol": "TCP" }],
        "selector": app_labels,
    })

# When "done", this will print the public IP.
result = None
if is_minikube:
    result = frontend.spec.apply(lambda v: v["cluster_ip"] if "cluster_ip" in v else None)
else:
    ingress = frontend.status.apply(lambda v: v["load_balancer"]["ingress"][0] if "load_balancer" in v else None)
    if ingress is not None:
        result = ingress.apply(lambda v: v["ip"] if "ip" in v else v["hostname"])

pulumi.export("ip", result)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
    metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        isMinikube := config.GetBool(ctx, "isMinikube")
        appName := "nginx"
        appLabels := pulumi.StringMap{
            "app": pulumi.String(appName),
        }
        deployment, err := appsv1.NewDeployment(ctx, appName, &appsv1.DeploymentArgs{
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

        feType := "LoadBalancer"
        if isMinikube {
            feType = "ClusterIP"
        }

        template := deployment.Spec.ApplyT(func(v *appsv1.DeploymentSpec) *corev1.PodTemplateSpec {
            return &v.Template
        }).(corev1.PodTemplateSpecPtrOutput)

        meta := template.ApplyT(func(v *corev1.PodTemplateSpec) *metav1.ObjectMeta { return v.Metadata }).(metav1.ObjectMetaPtrOutput)

        frontend, err := corev1.NewService(ctx, appName, &corev1.ServiceArgs{
            Metadata: meta,
            Spec: &corev1.ServiceSpecArgs{
                Type: pulumi.String(feType),
                Ports: &corev1.ServicePortArray{
                    &corev1.ServicePortArgs{
                        Port:       pulumi.Int(80),
                        TargetPort: pulumi.Int(80),
                        Protocol:   pulumi.String("TCP"),
                    },
                },
                Selector: appLabels,
            },
        })

        var ip pulumi.StringOutput

        if isMinikube {
            ip = frontend.Spec.ApplyT(func(val *corev1.ServiceSpec) string {
                if val.ClusterIP != nil {
                    return *val.ClusterIP
                }
                return ""
            }).(pulumi.StringOutput)
        } else {
            ip = frontend.Status.ApplyT(func(val *corev1.ServiceStatus) string {
                if val.LoadBalancer.Ingress[0].Ip != nil {
                    return *val.LoadBalancer.Ingress[0].Ip
                }
                return *val.LoadBalancer.Ingress[0].Hostname
            }).(pulumi.StringOutput)
        }

        ctx.Export("ip", ip)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var config = new Pulumi.Config();
    var isMinikube = config.GetBoolean("isMinikube") ?? false;

    var appName = "nginx";
    var appLabels = new InputMap<string>
    {
        { "app", appName },
    };

    var deployment = new Pulumi.Kubernetes.Apps.V1.Deployment(appName, new DeploymentArgs
    {
        Spec = new DeploymentSpecArgs
        {
            Selector = new LabelSelectorArgs
            {
                MatchLabels = appLabels,
            },
            Replicas = 1,
            Template = new PodTemplateSpecArgs
            {
                Metadata = new ObjectMetaArgs
                {
                    Labels = appLabels,
                },
                Spec = new PodSpecArgs
                {
                    Containers =
                    {
                        new ContainerArgs
                        {
                            Name = appName,
                            Image = "nginx",
                            Ports =
                            {
                                new ContainerPortArgs
                                {
                                    ContainerPortValue = 80
                                },
                            },
                        },
                    },
                },
            },
        },
    });

    var frontend = new Service(appName, new ServiceArgs
    {
        Metadata = new ObjectMetaArgs
        {
            Labels = deployment.Spec.Apply(spec =>
                spec.Template.Metadata.Labels
            ),
        },
        Spec = new ServiceSpecArgs
        {
            Type = isMinikube
                ? "ClusterIP"
                : "LoadBalancer",
            Selector = appLabels,
            Ports = new ServicePortArgs
            {
                Port = 80,
                TargetPort = 80,
                Protocol = "TCP",
            },
        }
    });

    var ip = isMinikube
        ? frontend.Spec.Apply(spec => spec.ClusterIP)
        : frontend.Status.Apply(status =>
        {
            var ingress = status.LoadBalancer.Ingress[0];
            return ingress.Ip ?? ingress.Hostname;
        });

    return new Dictionary<string, object?>
    {
        ["ip"] = ip
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.kubernetes.apps_v1.Deployment;
import com.pulumi.kubernetes.apps_v1.DeploymentArgs;
import com.pulumi.kubernetes.apps_v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.core_v1.*;
import com.pulumi.kubernetes.core_v1.ServiceArgs;
import com.pulumi.kubernetes.core_v1.enums.ServiceSpecType;
import com.pulumi.kubernetes.core_v1.inputs.*;
import com.pulumi.kubernetes.meta_v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaArgs;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var config = ctx.config();
            var isMinikube = config.requireBoolean("isMinikube");
            var labels = Map.of("app", "nginx");

            var deployment = new Deployment("nginx", DeploymentArgs.builder()
                .spec(DeploymentSpecArgs.builder()
                    .selector(LabelSelectorArgs.builder()
                        .matchLabels(labels)
                        .build())
                    .replicas(1)
                    .template(PodTemplateSpecArgs.builder()
                        .metadata(ObjectMetaArgs.builder()
                            .labels(labels)
                            .build())
                        .spec(PodSpecArgs.builder()
                            .containers(ContainerArgs.builder()
                                .name("nginx")
                                .image("nginx")
                                .ports(ContainerPortArgs.builder()
                                    .containerPort(80)
                                    .build())
                                .build())
                            .build())
                        .build())
                    .build())
                .build());

            var name = deployment.metadata()
                .applyValue(m -> m.orElseThrow().name().orElse(""));

            var frontend = new Service("nginx", ServiceArgs.builder()
                .metadata(ObjectMetaArgs.builder()
                    .labels(deployment.spec().applyValue(spec -> spec.get().template().metadata().get().labels()))
                    .build())
                .spec(ServiceSpecArgs.builder()
                    .type(isMinikube ? ServiceSpecType.ClusterIP : ServiceSpecType.LoadBalancer)
                    .selector(labels)
                    .ports(ServicePortArgs.builder()
                        .port(80)
                        .targetPort(80)
                        .protocol("TCP")
                        .build())
                    .build())
                .build());

            ctx.export("ip", isMinikube
                ? frontend.spec().applyValue(spec -> spec.get().clusterIP())
                : Output.tuple(frontend.status(), frontend.spec()).applyValue(t -> {
                    var status = t.t1;
                    var spec = t.t2;
                    var ingress = status.get().loadBalancer().get().ingress().get(0);
                    return ingress.ip().orElse(ingress.hostname().orElse(spec.get().clusterIP().get()));
                })
            );
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: quickstart
runtime: yaml
description: A minimal Kubernetes Pulumi YAML program

variables:
  appLabels:
    app: nginx

resources:
  deployment:
    type: kubernetes:apps/v1:Deployment
    properties:
      spec:
        selector:
          matchLabels: ${appLabels}
        replicas: 1
        template:
          metadata:
            labels: ${appLabels}
          spec:
            containers:
              - name: nginx
                image: nginx
  service:
    type: kubernetes:core/v1:Service
    properties:
      metadata:
        labels: ${appLabels}
      spec:
        type: ClusterIP
        selector: ${appLabels}
        ports:
          - port: 80
            targetPort: 80
            protocol: TCP

outputs:
  ip: ${service.spec.clusterIP}
```

{{% /choosable %}}
{{< /chooser >}}

Our program now creates a service to access the NGINX deployment, and requires a new [config](/docs/concepts/config/) value to indicate whether the program is being deployed to Minikube or not.

The configuration value can be set for the stack using `pulumi config set isMinikube <true|false>` command.

If you are currently using Minikube, set `isMinikube` to `true`, otherwise, set `isMinikube` to `false` as shown in the following command.

```bash
$ pulumi config set isMinikube false
```

## Deploy changes

Deploy your changes by running `pulumi up` again.

```bash
$ pulumi up
```

Pulumi computes the minimally disruptive change to achieve the desired state described by the program.

```
Previewing update (dev):

     Type                        Name            Plan
     pulumi:pulumi:Stack         quickstart-dev
 +   └─ kubernetes:core:Service  nginx           create

 Outputs:
  + ip  : output<string>
  - name: "nginx-xw231xdt"

Resources:
    + 1 to create
    2 unchanged

Do you want to perform this update?
  yes
> no
  details
```

Pulumi will create the service since it is now defined in the program.

```
Do you want to perform this update? yes
Updating (dev):

     Type                        Name            Status
     pulumi:pulumi:Stack         quickstart-dev
 +   └─ kubernetes:core:Service  nginx           created

Outputs:
  + ip  : "10.100.249.54"
  - name: "nginx-xw231xdt"

Resources:
    + 1 created
    2 unchanged

Duration: 12s
```

We now have an `ip` [stack output](/docs/concepts/stack#outputs) that we can `curl` to get the output from the service.

> **Using Minikube:** Note that Minikube does not support type `LoadBalancer`. If you are deploying to Minikube, see the following example to run the `kubectl port-forward service/YOUR_SERVICE_NAME 8080:80` command to forward the cluster port to the local machine. Then, the service can be accessed via `curl http://localhost:8080`, which will get the same result as `curl $(pulumi stack output ip)` as in the environment without using Minikube.
>
>
>  ```bash
>  $ kubectl get service
>  NAME             TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)   AGE
>  kubernetes       ClusterIP   10.96.0.1       <none>        443/TCP   26h
>  nginx-3hq3kux6   ClusterIP   10.96.185.206   <none>        80/TCP    15m
>  ```
>
> ```bash
> $ kubectl port-forward service/nginx-3hq3kux6 8080:80
> Forwarding from 127.0.0.1:8080 -> 80
> Forwarding from [::1]:8080 -> 80
> ```

```bash
$ curl $(pulumi stack output ip)
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
    body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
    }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

## Destroy stack

Now that we've seen how to deploy changes to our program, let's clean up and tear down the resources that are part of our stack.

To destroy resources, run the following:

```bash
$ pulumi destroy
```

You'll be prompted to make sure you really want to delete these resources.

```
Previewing destroy (dev):

     Type                           Name            Plan
 -   pulumi:pulumi:Stack            quickstart-dev  delete
 -   ├─ kubernetes:core:Service     nginx           delete
 -   └─ kubernetes:apps:Deployment  nginx           delete

Outputs:
  - ip: "10.105.234.140"

Resources:
    - 3 to delete

Do you want to perform this destroy? yes
Destroying (dev):

     Type                           Name            Status
 -   pulumi:pulumi:Stack            quickstart-dev  deleted
 -   ├─ kubernetes:core:Service     nginx           deleted
 -   └─ kubernetes:apps:Deployment  nginx           deleted

Outputs:
  - ip: "10.105.234.140"

Resources:
    - 3 deleted

Duration: 1s
```

To delete the stack itself, run [`pulumi stack rm`](/docs/cli/commands/pulumi_stack_rm). This removes the stack and the update history from Pulumi Cloud.

## Next steps

Congrats! You've deployed your first project on Kubernetes with Pulumi. Try a next step!

- Dive into [Learn Pulumi](/learn/pulumi-fundamentals) for a comprehensive walkthrough of key Pulumi concepts in the context of a real-life application.
- Explore how-to guides: These guides cover creating managed Kubernetes clusters across all major cloud providers: ([AWS](/registry/packages/kubernetes/how-to-guides/eks/), [Azure](/registry/packages/kubernetes/how-to-guides/aks/), [Google Cloud](/registry/packages/kubernetes/how-to-guides/gke/) as well as deploying app workloads on running Kubernetes clusters ([WordPress Helm Chart](/registry/packages/kubernetes/how-to-guides/wordpress-chart/), [Stateless App Deployment](/registry/packages/kubernetes/how-to-guides/stateless-app/)..
- Learn how Pulumi works from its architecture to key concepts, including [stacks](/docs/concepts/stack/), [state](/docs/concepts/state/), [configuration](/docs/concepts/config/), and [secrets](/docs/concepts/secrets/).
- Read through the [latest blog posts](/blog/tag/kubernetes) about using Pulumi with Kubernetes.
