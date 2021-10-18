---
title: Guestbook App with Redis and Nginx
meta_desc: How to create a guestbook application with Redis and Nginx powered by Docker and
           deployed with Kubernetes.
aliases: ["/docs/reference/tutorials/kubernetes/tutorial-guestbook/"]
layout: how-to-guide
---

{{< github-buttons "kubernetes-ts-guestbook" "kubernetes-py-guestbook" "kubernetes-go-guestbook" "kubernetes-cs-guestbook" >}}

In this tutorial, we'll build and deploy
[the standard Kubernetes Guestbook example](https://github.com/kubernetes/examples/tree/master/guestbook) using Pulumi.

The guestbook is a simple, multi-tier web application that uses Redis and Nginx, powered by Docker containers and
Kubernetes. The primary difference between this example and the standard Kubernetes one is that we'll be authoring it in
TypeScript instead of YAML, and we'll deploy it using `pulumi` rather than `kubectl`. This gives us the full power of
general-purpose languages, combined with immutable infrastructure, delivering a robust and repeatable update experience.

The code for this tutorial is available on GitHub.

* [TypeScript](https://github.com/pulumi/examples/tree/master/kubernetes-ts-guestbook)
* [Python](https://github.com/pulumi/examples/tree/master/kubernetes-py-guestbook)
* [Go](https://github.com/pulumi/examples/tree/master/kubernetes-go-guestbook)
* [C#](https://github.com/pulumi/examples/tree/master/kubernetes-cs-guestbook)

## Objectives

* Start up a Redis leader
* Start up Redis replicas
* Start up the guestbook frontend
* Expose and view the frontend service
* Clean up

## Before you begin

You need to have the Pulumi CLI and a working Kubernetes cluster.

1. [Install Pulumi]({{< relref "/docs/get-started/install" >}})
2. [Connect Pulumi to a Kubernetes Cluster]({{< relref "/registry/packages/kubernetes/installation-configuration" >}})

## Running the Guestbook

The guestbook application uses Redis to store its data. It writes its data to a Redis leader instance and reads data
from multiple Redis replica instances.

Normally we would write YAML files to configure them, and then run `kubectl` commands to create and manage the services.
Instead of doing that, we will author our program in code and deploy it with `pulumi`.

To start, we'll need to create a project and stack (a deployment target) for our new project:

### Create and Configure a Project

1. To create a new Pulumi project, let's use a template:

    {{< chooser language "typescript,python,go,csharp" >}}

    {{% choosable language typescript %}}

```shell
$ mkdir k8s-guestbook && cd k8s-guestbook
$ pulumi new kubernetes-typescript
```

    {{% /choosable %}}

    {{% choosable language python %}}

```shell
$ mkdir k8s-guestbook && cd k8s-guestbook
$ pulumi new kubernetes-python
```

    {{% /choosable %}}

    {{% choosable language go %}}

```shell
$ mkdir k8s-guestbook && cd k8s-guestbook
$ pulumi new kubernetes-go
```

    {{% /choosable %}}

    {{% choosable language csharp %}}

```shell
$ mkdir k8s-guestbook && cd k8s-guestbook
$ pulumi new kubernetes-csharp
```

    {{% /choosable %}}

    {{< /chooser >}}

    This command will initialize a fresh project in the `k8s-guestbook` newly-created directory.

1. Next, replace the minimal contents of the template's main file with the full guestbook code:

    {{< chooser language "typescript,python,go,csharp" >}}

    {{% choosable language typescript %}}

```typescript
// index.ts

import * as k8s from "@pulumi/kubernetes";
import * as pulumi from "@pulumi/pulumi";

// Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
// running on minikube, and if so, create only services of type ClusterIP.
const config = new pulumi.Config();
const isMinikube = config.getBoolean("isMinikube");

//
// REDIS LEADER.
//

const redisLeaderLabels = { app: "redis-leader" };
const redisLeaderDeployment = new k8s.apps.v1.Deployment("redis-leader", {
    spec: {
        selector: { matchLabels: redisLeaderLabels },
        template: {
            metadata: { labels: redisLeaderLabels },
            spec: {
                containers: [
                    {
                        name: "redis-leader",
                        image: "redis",
                        resources: { requests: { cpu: "100m", memory: "100Mi" } },
                        ports: [{ containerPort: 6379 }],
                    },
                ],
            },
        },
    },
});
const redisLeaderService = new k8s.core.v1.Service("redis-leader", {
    metadata: {
        name: "redis-leader",
        labels: redisLeaderDeployment.metadata.labels,
    },
    spec: {
        ports: [{ port: 6379, targetPort: 6379 }],
        selector: redisLeaderDeployment.spec.template.metadata.labels,
    },
});

//
// REDIS REPLICA.
//

const redisReplicaLabels = { app: "redis-replica" };
const redisReplicaDeployment = new k8s.apps.v1.Deployment("redis-replica", {
    spec: {
        selector: { matchLabels: redisReplicaLabels },
        template: {
            metadata: { labels: redisReplicaLabels },
            spec: {
                containers: [
                    {
                        name: "replica",
                        image: "pulumi/guestbook-redis-replica",
                        resources: { requests: { cpu: "100m", memory: "100Mi" } },
                        // If your cluster config does not include a dns service, then to instead access an environment
                        // variable to find the leader's host, change `value: "dns"` to read `value: "env"`.
                        env: [{ name: "GET_HOSTS_FROM", value: "dns" }],
                        ports: [{ containerPort: 6379 }],
                    },
                ],
            },
        },
    },
});
const redisReplicaService = new k8s.core.v1.Service("redis-replica", {
    metadata: {
        name: "redis-replica",
        labels: redisReplicaDeployment.metadata.labels
    },
    spec: {
        ports: [{ port: 6379, targetPort: 6379 }],
        selector: redisReplicaDeployment.spec.template.metadata.labels,
    },
});

//
// FRONTEND
//

const frontendLabels = { app: "frontend" };
const frontendDeployment = new k8s.apps.v1.Deployment("frontend", {
    spec: {
        selector: { matchLabels: frontendLabels },
        replicas: 3,
        template: {
            metadata: { labels: frontendLabels },
            spec: {
                containers: [
                    {
                        name: "frontend",
                        image: "pulumi/guestbook-php-redis",
                        resources: { requests: { cpu: "100m", memory: "100Mi" } },
                        // If your cluster config does not include a dns service, then to instead access an environment
                        // variable to find the leader's host, change `value: "dns"` to read `value: "env"`.
                        env: [{ name: "GET_HOSTS_FROM", value: "dns" /* value: "env"*/ }],
                        ports: [{ containerPort: 80 }],
                    },
                ],
            },
        },
    },
});
const frontendService = new k8s.core.v1.Service("frontend", {
    metadata: {
        labels: frontendDeployment.metadata.labels,
        name: "frontend",
    },
    spec: {
        type: isMinikube ? "ClusterIP" : "LoadBalancer",
        ports: [{ port: 80 }],
        selector: frontendDeployment.spec.template.metadata.labels,
    },
});

// Export the frontend IP.
export let frontendIp: pulumi.Output<string>;
if (isMinikube) {
    frontendIp = frontendService.spec.clusterIP;
} else {
    frontendIp = frontendService.status.loadBalancer.ingress[0].ip;
}
```

    {{% /choosable %}}

    {{% choosable language python %}}

```python
# __main__.py

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service, Namespace

# Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
# running on minikube, and if so, create only services of type ClusterIP.
config = pulumi.Config()
isMinikube = config.get_bool("isMinikube")

redis_leader_labels = {
    "app": "redis-leader",
}

redis_leader_deployment = Deployment(
    "redis-leader",
    spec={
        "selector": {
            "match_labels": redis_leader_labels,
        },
        "replicas": 3,
        "template": {
            "metadata": {
                "labels": redis_leader_labels,
            },
            "spec": {
                "containers": [{
                    "name": "redis-leader",
                    "image": "redis",
                    "resources": {
                        "requests": {
                            "cpu": "100m",
                            "memory": "100Mi",
                        },
                    },
                    "ports": [{
                        "container_port": 6379,
                    }],
                }],
            },
        },
    })

redis_leader_service = Service(
    "redis-leader",
    metadata={
        "name": "redis-leader",
        "labels": redis_leader_labels
    },
    spec={
        "ports": [{
            "port": 6379,
            "target_port": 6379,
        }],
        "selector": redis_leader_labels
    })

redis_replica_labels = {
    "app": "redis-replica",
}

redis_replica_deployment = Deployment(
    "redis-replica",
    spec={
        "selector": {
            "match_labels": redis_replica_labels
        },
        "replicas": 3,
        "template": {
            "metadata": {
                "labels": redis_replica_labels,
            },
            "spec": {
                "containers": [{
                    "name": "redis-replica",
                    "image": "pulumi/guestbook-redis-replica",
                    "resources": {
                        "requests": {
                            "cpu": "100m",
                            "memory": "100Mi",
                        },
                    },
                    "env": [{
                        "name": "GET_HOSTS_FROM",
                        "value": "dns",
                        # If your cluster config does not include a dns service, then to instead access an environment
                        # variable to find the leader's host, comment out the 'value: dns' line above, and
                        # uncomment the line below:
                        # value: "env"
                    }],
                    "ports": [{
                        "container_port": 6379,
                    }],
                }],
            },
        },
    })

redis_replica_service = Service(
    "redis-replica",
    metadata={
        "name": "redis-replica",
        "labels": redis_replica_labels
    },
    spec={
        "ports": [{
            "port": 6379,
            "target_port": 6379,
        }],
        "selector": redis_replica_labels
    })

# Frontend
frontend_labels = {
    "app": "frontend",
}

frontend_deployment = Deployment(
    "frontend",
    spec={
        "selector": {
            "match_labels": frontend_labels,
        },
        "replicas": 3,
        "template": {
            "metadata": {
                "labels": frontend_labels,
            },
            "spec": {
                "containers": [{
                    "name": "php-redis",
                    "image": "pulumi/guestbook-php-redis",
                    "resources": {
                        "requests": {
                            "cpu": "100m",
                            "memory": "100Mi",
                        },
                    },
                    "env": [{
                        "name": "GET_HOSTS_FROM",
                        "value": "dns",
                        # If your cluster config does not include a dns service, then to instead access an environment
                        # variable to find the leader's host, comment out the 'value: dns' line above, and
                        # uncomment the line below:
                        # "value": "env"
                    }],
                    "ports": [{
                        "container_port": 80,
                    }],
                }],
            },
        },
    })

frontend_service = Service(
    "frontend",
    metadata={
        "name": "frontend",
        "labels": frontend_labels,
    },
    spec={
        "type": "ClusterIP" if isMinikube else "LoadBalancer",
        "ports": [{
            "port": 80
        }],
        "selector": frontend_labels,
    })

frontend_ip = ""
if isMinikube:
    frontend_ip = frontend_service.spec.apply(lambda spec: spec.get("cluster_ip", ""))
else:
    ingress = frontend_service.status.apply(lambda status: status["load_balancer"]["ingress"][0])
    frontend_ip = ingress.apply(lambda ingress: ingress.get("ip", ingress.get("hostname", "")))
pulumi.export("frontend_ip", frontend_ip)
```

    {{% /choosable %}}

    {{% choosable language go %}}

```go
// main.go


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
        // Initialize config
        conf := config.New(ctx, "")

        // Minikube does not implement services of type `LoadBalancer`; require the user to specify if we're
        // running on minikube, and if so, create only services of type ClusterIP.
        isMinikube := conf.GetBool("isMinikube")

        redisLeaderLabels := pulumi.StringMap{
            "app": pulumi.String("redis-leader"),
        }

        // Redis leader Deployment
        _, err := appsv1.NewDeployment(ctx, "redis-leader", &appsv1.DeploymentArgs{
            Metadata: &metav1.ObjectMetaArgs{
                Labels: redisLeaderLabels,
            },
            Spec: appsv1.DeploymentSpecArgs{
                Selector: &metav1.LabelSelectorArgs{
                    MatchLabels: redisLeaderLabels,
                },
                Replicas: pulumi.Int(1),
                Template: &corev1.PodTemplateSpecArgs{
                    Metadata: &metav1.ObjectMetaArgs{
                        Labels: redisLeaderLabels,
                    },
                    Spec: &corev1.PodSpecArgs{
                        Containers: corev1.ContainerArray{
                            corev1.ContainerArgs{
                                Name:  pulumi.String("redis-leader"),
                                Image: pulumi.String("redis"),
                                Resources: &corev1.ResourceRequirementsArgs{
                                    Requests: pulumi.StringMap{
                                        "cpu":    pulumi.String("100m"),
                                        "memory": pulumi.String("100Mi"),
                                    },
                                },
                                Ports: corev1.ContainerPortArray{
                                    &corev1.ContainerPortArgs{
                                        ContainerPort: pulumi.Int(6379),
                                    },
                                },
                            }},
                    },
                },
            },
        })
        if err != nil {
            return err
        }

        // Redis leader Service
        _, err = corev1.NewService(ctx, "redis-leader", &corev1.ServiceArgs{
            Metadata: &metav1.ObjectMetaArgs{
                Name:   pulumi.String("redis-leader"),
                Labels: redisLeaderLabels,
            },
            Spec: &corev1.ServiceSpecArgs{
                Ports: corev1.ServicePortArray{
                    corev1.ServicePortArgs{
                        Port:       pulumi.Int(6379),
                        TargetPort: pulumi.Int(6379),
                    },
                },
                Selector: redisLeaderLabels,
            },
        })
        if err != nil {
            return err
        }

        redisReplicaLabels := pulumi.StringMap{
            "app": pulumi.String("redis-replica"),
        }

        // Redis replica Deployment
        _, err = appsv1.NewDeployment(ctx, "redis-replica", &appsv1.DeploymentArgs{
            Metadata: &metav1.ObjectMetaArgs{
                Labels: redisReplicaLabels,
            },
            Spec: appsv1.DeploymentSpecArgs{
                Selector: &metav1.LabelSelectorArgs{
                    MatchLabels: redisReplicaLabels,
                },
                Replicas: pulumi.Int(2),
                Template: &corev1.PodTemplateSpecArgs{
                    Metadata: &metav1.ObjectMetaArgs{
                        Labels: redisReplicaLabels,
                    },
                    Spec: &corev1.PodSpecArgs{
                        Containers: corev1.ContainerArray{
                            corev1.ContainerArgs{
                                Name:  pulumi.String("redis-replica"),
                                Image: pulumi.String("pulumi/guestbook-redis-replica"),
                                Resources: &corev1.ResourceRequirementsArgs{
                                    Requests: pulumi.StringMap{
                                        "cpu":    pulumi.String("100m"),
                                        "memory": pulumi.String("100Mi"),
                                    },
                                },
                                Env: corev1.EnvVarArray{
                                    corev1.EnvVarArgs{
                                        Name:  pulumi.String("GET_HOSTS_FROM"),
                                        Value: pulumi.String("dns"),
                                    },
                                },
                                Ports: corev1.ContainerPortArray{
                                    &corev1.ContainerPortArgs{
                                        ContainerPort: pulumi.Int(6379),
                                    },
                                },
                            }},
                    },
                },
            },
        })
        if err != nil {
            return err
        }

        // Redis replica Service
        _, err = corev1.NewService(ctx, "redis-replica", &corev1.ServiceArgs{
            Metadata: &metav1.ObjectMetaArgs{
                Name:   pulumi.String("redis-replica"),
                Labels: redisReplicaLabels,
            },
            Spec: &corev1.ServiceSpecArgs{
                Ports: corev1.ServicePortArray{
                    corev1.ServicePortArgs{
                        Port: pulumi.Int(6379),
                    },
                },
                Selector: redisReplicaLabels,
            },
        })
        if err != nil {
            return err
        }

        frontendLabels := pulumi.StringMap{
            "app": pulumi.String("frontend"),
        }

        // Frontend Deployment
        _, err = appsv1.NewDeployment(ctx, "frontend", &appsv1.DeploymentArgs{
            Metadata: &metav1.ObjectMetaArgs{
                Labels: frontendLabels,
            },
            Spec: appsv1.DeploymentSpecArgs{
                Selector: &metav1.LabelSelectorArgs{
                    MatchLabels: frontendLabels,
                },
                Replicas: pulumi.Int(1),
                Template: &corev1.PodTemplateSpecArgs{
                    Metadata: &metav1.ObjectMetaArgs{
                        Labels: frontendLabels,
                    },
                    Spec: &corev1.PodSpecArgs{
                        Containers: corev1.ContainerArray{
                            corev1.ContainerArgs{
                                Name:  pulumi.String("php-redis"),
                                Image: pulumi.String("pulumi/guestbook-php-redis"),
                                Resources: &corev1.ResourceRequirementsArgs{
                                    Requests: pulumi.StringMap{
                                        "cpu":    pulumi.String("100m"),
                                        "memory": pulumi.String("100Mi"),
                                    },
                                },
                                Env: corev1.EnvVarArray{
                                    corev1.EnvVarArgs{
                                        Name:  pulumi.String("GET_HOSTS_FROM"),
                                        Value: pulumi.String("dns"),
                                    },
                                },
                                Ports: corev1.ContainerPortArray{
                                    &corev1.ContainerPortArgs{
                                        ContainerPort: pulumi.Int(80),
                                    },
                                },
                            }},
                    },
                },
            },
        })
        if err != nil {
            return err
        }

        // Frontend Service
        var frontendServiceType string
        if isMinikube {
            frontendServiceType = "ClusterIP"
        } else {
            frontendServiceType = "LoadBalancer"
        }
        frontendService, err := corev1.NewService(ctx, "frontend", &corev1.ServiceArgs{
            Metadata: &metav1.ObjectMetaArgs{
                Labels: frontendLabels,
                Name:   pulumi.String("frontend"),
            },
            Spec: &corev1.ServiceSpecArgs{
                Type: pulumi.String(frontendServiceType),
                Ports: corev1.ServicePortArray{
                    corev1.ServicePortArgs{
                        Port: pulumi.Int(80),
                    },
                },
                Selector: frontendLabels,
            },
        })
        if err != nil {
            return err
        }

        if isMinikube {
            ctx.Export("frontendIP", frontendService.Spec.ApplyT(func(spec *corev1.ServiceSpec) *string {
                return spec.ClusterIP
            }))
        } else {
            ctx.Export("frontendIP", frontendService.Status.ApplyT(func(status *corev1.ServiceStatus) *string {
                ingress := status.LoadBalancer.Ingress[0]
                if ingress.Hostname != nil {
                    return ingress.Hostname
                }
                return ingress.Ip
            }))
        }

        return nil
    })
}
```

    {{% /choosable %}}

    {{% choosable language csharp %}}

```csharp
//MyStack.cs

using Pulumi;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

class Guestbook : Stack
{
    public Guestbook()
    {
        // Minikube does not implement services of type `LoadBalancer`; require the user to
        // specify if we're running on minikube, and if so, create only services of type
        // ClusterIP.
        var config = new Config();
        var isMiniKube = config.GetBoolean("isMiniKube") ?? false;

        //
        // REDIS LEADER.
        //

        var redisLeaderLabels = new InputMap<string>
        {
            {"app", "redis-leader"}
        };

        var redisLeaderDeployment = new Pulumi.Kubernetes.Apps.V1.Deployment("redis-leader", new DeploymentArgs
        {
            Spec = new DeploymentSpecArgs
            {
                Selector = new LabelSelectorArgs
                {
                    MatchLabels = redisLeaderLabels
                },
                Template = new PodTemplateSpecArgs
                {
                    Metadata = new ObjectMetaArgs
                    {
                        Labels = redisLeaderLabels
                    },
                    Spec = new PodSpecArgs
                    {
                        Containers =
                        {
                            new ContainerArgs
                            {
                                Name = "redis-leader",
                                Image = "redis",
                                Resources = new ResourceRequirementsArgs
                                {
                                    Requests =
                                    {
                                        {"cpu", "100m"},
                                        {"memory", "100Mi"}
                                    }
                                },
                                Ports =
                                {
                                    new ContainerPortArgs {ContainerPortValue = 6379}
                                }
                            }
                        }
                    }
                }
            }
        });

        var redisLeaderService = new Pulumi.Kubernetes.Core.V1.Service("redis-leader", new ServiceArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Name = "redis-leader",
                Labels = redisLeaderDeployment.Metadata.Apply(metadata => metadata.Labels),
            },
            Spec = new ServiceSpecArgs
            {
                Ports =
                {
                    new ServicePortArgs
                    {
                        Port = 6379,
                        TargetPort = 6379
                    },
                },
                Selector = redisLeaderDeployment.Spec.Apply(spec => spec.Template.Metadata.Labels)
            }
        });

        //
        // REDIS REPLICA.
        //

        var redisReplicaLabels = new InputMap<string>
        {
            {"app", "redis-replica"}
        };

        var redisReplicaDeployment = new Pulumi.Kubernetes.Apps.V1.Deployment("redis-replica", new DeploymentArgs
        {
            Spec = new DeploymentSpecArgs
            {
                Selector = new LabelSelectorArgs
                {
                    MatchLabels = redisReplicaLabels
                },
                Template = new PodTemplateSpecArgs
                {
                    Metadata = new ObjectMetaArgs
                    {
                        Labels = redisReplicaLabels
                    },
                    Spec = new PodSpecArgs
                    {
                        Containers =
                        {
                            new ContainerArgs
                            {
                                Name = "redis-replica",
                                Image = "pulumi/guestbook-redis-replica",
                                Resources = new ResourceRequirementsArgs
                                {
                                    Requests =
                                    {
                                        {"cpu", "100m"},
                                        {"memory", "100Mi"}
                                    }
                                },
                                // If your cluster config does not include a dns service, then to instead access an environment
                                // variable to find the leader's host, change `value: "dns"` to read `value: "env"`.
                                Env =
                                {
                                    new EnvVarArgs
                                    {
                                        Name = "GET_HOSTS_FROM",
                                        Value = "dns"
                                    },
                                },
                                Ports =
                                {
                                    new ContainerPortArgs {ContainerPortValue = 6379}
                                }
                            }
                        }
                    }
                }
            }
        });

        var redisReplicaService = new Pulumi.Kubernetes.Core.V1.Service("redis-replica", new ServiceArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Name = "redis-replica",
                Labels = redisReplicaDeployment.Metadata.Apply(metadata => metadata.Labels)
            },
            Spec = new ServiceSpecArgs
            {
                Ports =
                {
                    new ServicePortArgs
                    {
                        Port = 6379,
                        TargetPort = 6379
                    },
                },
                Selector = redisReplicaDeployment.Spec.Apply(spec => spec.Template.Metadata.Labels)
            }
        });

        //
        // FRONTEND
        //

        var frontendLabels = new InputMap<string>
        {
            {"app", "frontend"},
        };

        var frontendDeployment = new Pulumi.Kubernetes.Apps.V1.Deployment("frontend", new DeploymentArgs
        {
            Spec = new DeploymentSpecArgs
            {
                Selector = new LabelSelectorArgs
                {
                    MatchLabels = frontendLabels
                },
                Replicas = 3,
                Template = new PodTemplateSpecArgs
                {
                    Metadata = new ObjectMetaArgs
                    {
                        Labels = frontendLabels
                    },
                    Spec = new PodSpecArgs
                    {
                        Containers =
                        {
                            new ContainerArgs
                            {
                                Name = "php-redis",
                                Image = "pulumi/guestbook-php-redis",
                                Resources = new ResourceRequirementsArgs
                                {
                                    Requests =
                                    {
                                        {"cpu", "100m"},
                                        {"memory", "100Mi"},
                                    },
                                },
                                // If your cluster config does not include a dns service, then to instead access an environment
                                // variable to find the leaders's host, change `value: "dns"` to read `value: "env"`.
                                Env =
                                {
                                    new EnvVarArgs
                                    {
                                        Name = "GET_HOSTS_FROM",
                                        Value = "dns", /* Value = "env"*/
                                    }
                                },
                                Ports =
                                {
                                    new ContainerPortArgs {ContainerPortValue = 80}
                                }
                            }
                        }
                    }
                }
            }
        });

        var frontendService = new Pulumi.Kubernetes.Core.V1.Service("frontend", new ServiceArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Name = "frontend",
                Labels = frontendDeployment.Metadata.Apply(metadata => metadata.Labels)
            },
            Spec = new ServiceSpecArgs
            {
                Type = isMiniKube ? "ClusterIP" : "LoadBalancer",
                Ports =
                {
                    new ServicePortArgs
                    {
                        Port = 80,
                        TargetPort = 80
                    }
                },
                Selector = frontendDeployment.Spec.Apply(spec => spec.Template.Metadata.Labels)
            }
        });

        if (isMiniKube)
        {
            this.FrontendIp = frontendService.Spec.Apply(spec => spec.ClusterIP);
        }
        else
        {
            this.FrontendIp = frontendService.Status.Apply(status => status.LoadBalancer.Ingress[0].Ip ?? status.LoadBalancer.Ingress[0].Hostname);
        }
    }

    [Output] public Output<string> FrontendIp { get; set; }
}
```

    {{% /choosable %}}

    {{< /chooser >}}

    This code creates three Kubernetes Services, each with an associated Deployment. The full Kubernetes object model is
    available to us, giving us the full power of Kubernetes right away.

1. (Optional) By default, our frontend Service will be of type `ClusterIP`. This will work on Minikube, but for most
    production Kubernetes clusters, we will want it to be of type `LoadBalancer`, ensuring that a load balancer in your
    target cloud environment is allocated.

    The above code uses [configuration]({{< relref "/docs/intro/concepts/config" >}}) to make this parameterizable.
    If you'd like our program to use a load balancer, simply run:

    ```shell
    $ pulumi config set useLoadBalancer true
    ```

    If you're not sure, it's safe to skip this step.

    ### Deploying

1. Now we're ready to deploy our code. To do so, simply run `pulumi up`:

    ```
    $ pulumi up
    ```

    The command will first show us a complete preview of what will take place, with a confirmation prompt. No changes
    will have been made yet. It should look something like this:

        Previewing update of stack 'k8s-guestbook-dev'
        Previewing changes:

            Type                           Name                             Plan       Info
        +   pulumi:pulumi:Stack            k8s-guestbook-k8s-guestbook-dev  create
        +   ├─ kubernetes:core:Service     redis-leader                     create
        +   ├─ kubernetes:core:Service     redis-replica                    create
        +   ├─ kubernetes:core:Service     frontend                         create
        +   ├─ kubernetes:apps:Deployment  redis-leader                     create
        +   ├─ kubernetes:apps:Deployment  redis-replica                    create
        +   └─ kubernetes:apps:Deployment  frontend                         create

        info: 7 changes previewed:
            + 7 resources to create

        Do you want to perform this update?
        > yes
        no
        details

    Let's select "yes" and hit enter. The deployment will proceed, and the output will look like this:

        Updating stack 'k8s-guestbook-dev'
        Performing changes:

            Type                           Name                             Status      Info
        +   pulumi:pulumi:Stack            k8s-guestbook-k8s-guestbook-dev  created
        +   ├─ kubernetes:core:Service     redis-replica                    created     1 info message
        +   ├─ kubernetes:core:Service     frontend                         created     1 info message
        +   ├─ kubernetes:core:Service     redis-leader                     created     1 info message
        +   ├─ kubernetes:apps:Deployment  redis-leader                     created
        +   ├─ kubernetes:apps:Deployment  redis-replica                    created
        +   └─ kubernetes:apps:Deployment  frontend                         created

        Diagnostics:
        kubernetes:core:Service: redis-replica
            info: ✅ Service 'redis-replica' successfully created endpoint objects

        kubernetes:core:Service: frontend
            info: ✅ Service 'frontend' successfully created endpoint objects

        kubernetes:core:Service: redis-leader
            info: ✅ Service 'redis-leader' successfully created endpoint objects

        ---outputs:---
        frontendIP: "10.102.193.86"

        info: 7 changes performed:
            + 7 resources created
        Update duration: 16.226520447s

        Permalink: https://app.pulumi.com/joeduffy/k8s-guestbook-dev/updates/1

    ### Viewing the Guestbook

1. The application is now running in our cluster. Let's inspect our cluster state to validate the deployment.

    Use `kubectl` to see the deployed services:

    ```shell
    $ kubectl get services
    ```

    We should see entries for each of the four Services we've created in our program:

    ```
    NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
    frontend       ClusterIP   10.102.193.86   <none>        80/TCP     2m
    kubernetes     ClusterIP   10.96.0.1       <none>        443/TCP    1d
    redis-leader   ClusterIP   10.98.205.37    <none>        6379/TCP   2m
    redis-replica  ClusterIP   10.96.9.70      <none>        6379/TCP   2m
    ```

    The `pulumi stack output` command prints exported program variables:

    ```shell
    $ pulumi stack output frontendIP
    ```

    The value of the `frontendIP` variable matches either `frontend`'s `CLUSTER-IP` (if you're
    deploying with `useLoadBalancer` set to `false`) or `frontend`'s `EXTERNAL-IP` (if you're
    deploying with `useLoadBalancer` set to `true`). For example:

    ```
    10.102.193.86
    ```

1. Now let's see our guestbook application in action.

    ![Guestbook in browser](/images/docs/quickstart/kubernetes/guestbook.png)

    **No Load Balancer (Minikube):**

    Because Minikube doesn't support the `LoadBalancer` type, our example above uses `ClusterIP`. In order to
    browse to it, we will first need to forward a port on `localhost` to it. To do so, run:

    ```shell
    $ kubectl port-forward svc/frontend 8765:80
    ```

    At this point, we can view our running guestbook application:

    ```shell
    $ curl localhost:8765
    ```

    The HTML from the guestbook will be fetched and printed:

    ```
    <html ng-app="redis">
      <head>
      <title>Guestbook</title>
      ...
    </html>
    ```

    **Using a Load Balancer:**

    If you are instead running this program in a real cluster, and set `useLoadBalancer` to `true` in step 3,
    then you can simply access your guestbook application with:

    ```shell
    $ curl $(pulumi stack output frontendIP)
    ```

    The HTML from the guestbook will be fetched and printed:

    ```
    <html ng-app="redis">
      <head>
      <title>Guestbook</title>
      ...
    </html>
    ```

1. We're almost done. To demonstrate incremental updates, however, Let's make an update to our program to scale
    the frontend from 3 replicas to 5. Find the line:

    {{< chooser language "typescript,python,go,csharp" >}}

    {{% choosable language typescript %}}

```typescript
        replicas: 3,
```

and change it to:

```typescript
        replicas: 5,
```

Or simply run `sed -i "s/replicas: 3/replicas: 5/g" index.ts`.

    {{% /choosable %}}

    {{% choosable language python %}}

```python
        "replicas": 3,
```

and change it to:

```python
        "replicas": 5,
```

Or simply run `sed -i "s/\"replicas\": 3/\"replicas\": 5/g" __main__.py`.

    {{% /choosable %}}

    {{% choosable language go %}}

```go
        Replicas: pulumi.Int(3),
```

and change it to:

```go
        Replicas: pulumi.Int(5),
```

Or simply run `sed -i "s/Replicas = pulumi\.Int(3)/Replicas = pulumi\.Int(5)/g" main.go`.

    {{% /choosable %}}

    {{% choosable language csharp %}}

```csharp
        Replicas = 3,
```

and change it to:

```csharp
        Replicas = 5,
```

Or simply run `sed -i "s/Replicas = 3/Replicas = 5/g" MyStack.cs`.

    {{% /choosable %}}

    {{< /chooser >}}

    Now all we need to do is run `pulumi up`, and Pulumi will figure out the minimal set of changes to make:

    ```shell
    $ pulumi up -y --skip-preview
    ```

    The output from running this command should look something like this:

        Updating stack 'k8s-guestbook-dev'
        Performing changes:

                Type                           Name                             Plan          Info
            *   pulumi:pulumi:Stack            k8s-guestbook-k8s-guestbook-dev  no change
            ~   └─ kubernetes:apps:Deployment  frontend                         updated       changes: ~ spec

        info: 1 change performed:
            ~ 1 resource updated
              6 resources unchanged

    ### Cleaning Up

1. Feel free to experiment. As soon as you're done, let's clean up and destroy the resources and remove our stack:

    ```shell
    $ pulumi destroy --yes
    $ pulumi stack rm --yes
    ```

    Afterwards, query the list of pods to verify that none are remaining:

    ```shell
    $ kubectl get pods
    ```

    If your cluster is empty, you will see output along the following lines:

    ```
    No resources found.
    ```

    Of course, if you have other applications deployed, you should still see them, but not the guestbook.
