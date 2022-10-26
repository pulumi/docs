---
title: Modify the Program | Kubernetes
h1: Modify the Program
linktitle: Modify the Program
meta_desc: This page provides an overview on how to update Kubernetes project from a Pulumi program.
weight: 6
menu:
  getstarted:
    parent: kubernetes
    identifier: kubernetes-modify-program

aliases: ["/docs/quickstart/kubernetes/modify-program/"]
---

Now that we have an instance of our Pulumi program deployed, let's update it to do something a little more interesting.

Replace the entire contents of {{< langfile >}} with the following:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" / >}}

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

Our program now creates a service to access the NGINX deployment, and requires a new [config](/docs/intro/concepts/config/) value to indicate whether the program is being deployed to Minikube or not.

The configuration value can be set for the stack using `pulumi config set isMinikube <true|false>` command.

If you are currently using Minikube, set `isMinikube` to `true`, otherwise, set `isMinikube` to `false` as shown in the following command.

```bash
$ pulumi config set isMinikube false
```

Next, we'll deploy the changes.

{{< get-started-stepper >}}
