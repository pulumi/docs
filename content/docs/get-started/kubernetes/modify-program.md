---
title: Modify the Program | Kubernetes
h1: Modify the Program
linktitle: Modify the Program
meta_desc: This page provides an overview on how to update Kubernetes project from a Pulumi program.
weight: 8
menu:
  getstarted:
    parent: kubernetes
    identifier: kubernetes-modify-program

aliases: ["/docs/quickstart/kubernetes/modify-program/"]
---

Now that we have an instance of our Pulumi program deployed, let's update it to do something a little more interesting.

Replace the entire contents of {{< langfile >}} with the following:

{{< langchoose nogo csharp >}}

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
    : frontend.status.loadBalancer.ingress[0].ip;
```

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
    : frontend.status.loadBalancer.ingress[0].ip;
```

```python
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
if is_minikube:
    pulumi.export("ip", frontend.spec.apply(lambda v: v["cluster_ip"] if "cluster_ip" in v else None))
else:
    pulumi.export("ip", frontend.status.apply(lambda v: v["load_balancer"]["ingress"][0]["ip"] if "load_balancer" in v else None))
```

```csharp
using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

class Program
{
    static Task<int> Main()
    {
        return Pulumi.Deployment.RunAsync(() =>
        {
            var config = new Pulumi.Config();
            var isMinikube = config.GetBoolean("isMinikube") ?? false;

            var appName = "nginx";

            var appLabels = new InputMap<string>{
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
                { "ip", ip },
            };
        });
    }
}
```

Our program now creates a service to access the NGINX deployment, and requires a new [config]({{< relref "/docs/intro/concepts/config" >}}) value to indicate whether the program is being deployed to Minikube or not.

The required config value must be set for the stack using `pulumi config set isMinikube <true|false>`:

```bash
$ pulumi config set isMinikube false
```

Next, we'll deploy the changes.

{{< get-started-stepper >}}
