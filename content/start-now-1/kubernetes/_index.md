---
title: Get Started with Pulumi and Kubernetes
meta_desc: Deploy your first Kubernetes applications with Pulumi in under 5 minutes
type: page
layout: cloud-unified
no_on_this_page: true

cloud_name: Kubernetes
subtitle: Deploy your first Kubernetes applications in under 5 minutes
---

## Quick Setup

### 1. Sign up for Pulumi (Free)

Get started with Pulumi Cloud for free. Includes state management, secrets, and more.

<a href="https://app.pulumi.com/signup" class="btn-primary">Create Free Account</a>

### 2. Install Pulumi CLI

{{< chooser os "macos,linux,windows" >}}

{{% choosable os macos %}}
```bash
brew install pulumi/tap/pulumi
```
{{% /choosable %}}

{{% choosable os linux %}}
```bash
curl -fsSL https://get.pulumi.com | sh
```
{{% /choosable %}}

{{% choosable os windows %}}
```powershell
choco install pulumi
```
{{% /choosable %}}

{{< /chooser >}}

### 3. Configure Kubernetes Access

Ensure you have `kubectl` configured to connect to your cluster:
```bash
kubectl cluster-info
```

Pulumi uses the same configuration as `kubectl` from `~/.kube/config`.

### 4. Deploy Your First Application

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

Create a new project:
```bash
mkdir my-k8s-app && cd my-k8s-app
pulumi new kubernetes-typescript
```

Example: Deploy an NGINX application
```typescript
import * as k8s from "@pulumi/kubernetes";

// Create a Kubernetes Deployment
const appLabels = { app: "nginx" };
const deployment = new k8s.apps.v1.Deployment("nginx-deployment", {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 2,
        template: {
            metadata: { labels: appLabels },
            spec: {
                containers: [{
                    name: "nginx",
                    image: "nginx:latest",
                    ports: [{ containerPort: 80 }],
                }],
            },
        },
    },
});

// Create a Service
const service = new k8s.core.v1.Service("nginx-service", {
    spec: {
        selector: appLabels,
        ports: [{ port: 80 }],
        type: "LoadBalancer",
    },
});

// Export the Service endpoint
export const url = service.status.loadBalancer.ingress[0].hostname;
```

Deploy your application:
```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language python %}}

Create a new project:
```bash
mkdir my-k8s-app && cd my-k8s-app
pulumi new kubernetes-python
```

Example: Deploy an NGINX application
```python
import pulumi
import pulumi_kubernetes as kubernetes

# Create a Kubernetes Deployment
app_labels = {"app": "nginx"}
deployment = kubernetes.apps.v1.Deployment(
    "nginx-deployment",
    spec=kubernetes.apps.v1.DeploymentSpecArgs(
        selector=kubernetes.meta.v1.LabelSelectorArgs(
            match_labels=app_labels
        ),
        replicas=2,
        template=kubernetes.core.v1.PodTemplateSpecArgs(
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels=app_labels
            ),
            spec=kubernetes.core.v1.PodSpecArgs(
                containers=[kubernetes.core.v1.ContainerArgs(
                    name="nginx",
                    image="nginx:latest",
                    ports=[kubernetes.core.v1.ContainerPortArgs(
                        container_port=80
                    )],
                )],
            ),
        ),
    ),
)

# Create a Service
service = kubernetes.core.v1.Service(
    "nginx-service",
    spec=kubernetes.core.v1.ServiceSpecArgs(
        selector=app_labels,
        ports=[kubernetes.core.v1.ServicePortArgs(port=80)],
        type="LoadBalancer",
    ),
)

# Export the Service endpoint
pulumi.export("url", service.status.load_balancer.ingress[0].hostname)
```

Deploy your application:
```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language go %}}

Create a new project:
```bash
mkdir my-k8s-app && cd my-k8s-app
pulumi new kubernetes-go
```

Example: Deploy an NGINX application
```go
package main

import (
    appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apps/v1"
    corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
    metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Create a Kubernetes Deployment
        appLabels := pulumi.StringMap{
            "app": pulumi.String("nginx"),
        }

        deployment, err := appsv1.NewDeployment(ctx, "nginx-deployment", &appsv1.DeploymentArgs{
            Spec: &appsv1.DeploymentSpecArgs{
                Selector: &metav1.LabelSelectorArgs{
                    MatchLabels: appLabels,
                },
                Replicas: pulumi.Int(2),
                Template: &corev1.PodTemplateSpecArgs{
                    Metadata: &metav1.ObjectMetaArgs{
                        Labels: appLabels,
                    },
                    Spec: &corev1.PodSpecArgs{
                        Containers: corev1.ContainerArray{
                            &corev1.ContainerArgs{
                                Name:  pulumi.String("nginx"),
                                Image: pulumi.String("nginx:latest"),
                                Ports: corev1.ContainerPortArray{
                                    &corev1.ContainerPortArgs{
                                        ContainerPort: pulumi.Int(80),
                                    },
                                },
                            },
                        },
                    },
                },
            },
        })
        if err != nil {
            return err
        }

        // Create a Service
        service, err := corev1.NewService(ctx, "nginx-service", &corev1.ServiceArgs{
            Spec: &corev1.ServiceSpecArgs{
                Selector: appLabels,
                Ports: corev1.ServicePortArray{
                    &corev1.ServicePortArgs{
                        Port: pulumi.Int(80),
                    },
                },
                Type: pulumi.String("LoadBalancer"),
            },
        })
        if err != nil {
            return err
        }

        ctx.Export("name", deployment.Metadata.Name())
        ctx.Export("service", service.Metadata.Name())
        return nil
    })
}
```

Deploy your application:
```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language csharp %}}

Create a new project:
```bash
mkdir my-k8s-app && cd my-k8s-app
pulumi new kubernetes-csharp
```

Example: Deploy an NGINX application
```csharp
using Pulumi;
using Pulumi.Kubernetes.Apps.V1;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;

class MyStack : Stack
{
    public MyStack()
    {
        var appLabels = new InputMap<string>
        {
            { "app", "nginx" }
        };

        // Create a Kubernetes Deployment
        var deployment = new Deployment("nginx-deployment", new DeploymentArgs
        {
            Spec = new DeploymentSpecArgs
            {
                Selector = new LabelSelectorArgs
                {
                    MatchLabels = appLabels
                },
                Replicas = 2,
                Template = new PodTemplateSpecArgs
                {
                    Metadata = new ObjectMetaArgs
                    {
                        Labels = appLabels
                    },
                    Spec = new PodSpecArgs
                    {
                        Containers = new[]
                        {
                            new ContainerArgs
                            {
                                Name = "nginx",
                                Image = "nginx:latest",
                                Ports = new[]
                                {
                                    new ContainerPortArgs
                                    {
                                        ContainerPort = 80
                                    }
                                }
                            }
                        }
                    }
                }
            }
        });

        // Create a Service
        var service = new Service("nginx-service", new ServiceArgs
        {
            Spec = new ServiceSpecArgs
            {
                Selector = appLabels,
                Ports = new[]
                {
                    new ServicePortArgs
                    {
                        Port = 80
                    }
                },
                Type = "LoadBalancer"
            }
        });

        this.ServiceName = service.Metadata.Apply(m => m.Name);
    }

    [Output]
    public Output<string> ServiceName { get; set; }
}
```

Deploy your application:
```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language java %}}

Create a new project:
```bash
mkdir my-k8s-app && cd my-k8s-app
pulumi new kubernetes-java
```

Example: Deploy an NGINX application
```java
package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.kubernetes.apps.v1.Deployment;
import com.pulumi.kubernetes.apps.v1.DeploymentArgs;
import com.pulumi.kubernetes.apps.v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.core.v1.Service;
import com.pulumi.kubernetes.core.v1.ServiceArgs;
import com.pulumi.kubernetes.core.v1.inputs.*;
import com.pulumi.kubernetes.meta.v1.inputs.*;

import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var appLabels = Map.of("app", "nginx");

        // Create a Kubernetes Deployment
        var deployment = new Deployment("nginx-deployment", DeploymentArgs.builder()
            .spec(DeploymentSpecArgs.builder()
                .selector(LabelSelectorArgs.builder()
                    .matchLabels(appLabels)
                    .build())
                .replicas(2)
                .template(PodTemplateSpecArgs.builder()
                    .metadata(ObjectMetaArgs.builder()
                        .labels(appLabels)
                        .build())
                    .spec(PodSpecArgs.builder()
                        .containers(ContainerArgs.builder()
                            .name("nginx")
                            .image("nginx:latest")
                            .ports(ContainerPortArgs.builder()
                                .containerPort(80)
                                .build())
                            .build())
                        .build())
                    .build())
                .build())
            .build());

        // Create a Service
        var service = new Service("nginx-service", ServiceArgs.builder()
            .spec(ServiceSpecArgs.builder()
                .selector(appLabels)
                .ports(ServicePortArgs.builder()
                    .port(80)
                    .build())
                .type("LoadBalancer")
                .build())
            .build());

        ctx.export("serviceName", service.metadata()
            .applyValue(metadata -> metadata.name().orElse("")));
    }
}
```

Deploy your application:
```bash
pulumi up
```

{{% /choosable %}}

{{% choosable language yaml %}}

Create a new project:
```bash
mkdir my-k8s-app && cd my-k8s-app
pulumi new kubernetes-yaml
```

Example: Deploy an NGINX application
```yaml
name: my-k8s-app
runtime: yaml

resources:
  # Create a Kubernetes Deployment
  nginx-deployment:
    type: kubernetes:apps/v1:Deployment
    properties:
      spec:
        selector:
          matchLabels:
            app: nginx
        replicas: 2
        template:
          metadata:
            labels:
              app: nginx
          spec:
            containers:
              - name: nginx
                image: nginx:latest
                ports:
                  - containerPort: 80

  # Create a Service
  nginx-service:
    type: kubernetes:core/v1:Service
    properties:
      spec:
        selector:
          app: nginx
        ports:
          - port: 80
        type: LoadBalancer

outputs:
  serviceName: ${nginx-service.metadata.name}
```

Deploy your application:
```bash
pulumi up
```

{{% /choosable %}}

## What's Next?

- [**Follow the complete Kubernetes tutorial →**](/docs/iac/get-started/kubernetes/)  
  Learn how to deploy and manage applications on Kubernetes

- [**Explore Kubernetes examples →**](https://github.com/pulumi/examples#kubernetes)  
  Browse production-ready examples for Kubernetes workloads

- [**Learn about Helm integration →**](/docs/iac/concepts/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-kubernetes/#helm-charts)  
  Deploy existing Helm charts with Pulumi

- [**Join the community →**](https://slack.pulumi.com)  
  Get help and share knowledge with other Pulumi users