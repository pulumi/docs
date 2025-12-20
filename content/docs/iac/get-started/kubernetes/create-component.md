---
title_tag: Create a component | Kubernetes
title: Create a component
h1: "Get started with Pulumi and Kubernetes"
meta_desc: This page provides an overview on how to create infrastructure abstractions with Pulumi.
weight: 7
menu:
    iac:
        name: Create a component
        identifier: kubernetes-get-started.create-component
        parent: kubernetes-get-started
        weight: 7

aliases:
    - /docs/quickstart/kubernetes/create-component/
---

## Create a component

[**Components**](/docs/iac/concepts/resources/components/) are infrastructure abstractions that encapsulate
complexity and enable sharing and reuse. Instead of copy-pasting common patterns, you can encode them as components.

You will now create your first component that packages up your Kubernetes NGINX deployment so you can easily stamp out
entire NGINX services in just a few lines of code:

{{% choosable language typescript %}}

```typescript
const nginx = new KubernetesNginxService("my-nginx", {
    isMinikube: config.requireBoolean("isMinikube")
});
export const ip = nginx.ip;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
nginx = KubernetesNginxService('my-nginx', is_minikube=config.require_bool("isMinikube"))
pulumi.export("ip", nginx.ip)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
nginx, err := NewKubernetesNginxService(ctx, "my-nginx", KubernetesNginxServiceArgs{
    IsMinikube: config.GetBool(ctx, "isMinikube"),
})
if err != nil {
    return err
}
ctx.Export("ip", nginx.Ip)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
var nginx = new KubernetesNginxService("my-nginx", new KubernetesNginxServiceArgs()
{
    IsMinikube = config.GetBoolean("isMinikube") ?? false
});

return new Dictionary<string, object?>
{
    ["ip"] = nginx.Ip
};
```

{{% /choosable %}}

{{% choosable language java %}}

```java
var nginx = new KubernetesNginxService("my-nginx",
    new KubernetesNginxServiceArgs(config.requireBoolean("isMinikube")));
ctx.export("ip", nginx.ip);
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/kubernetes/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

Using components here also has the benefit that, as the requirements for your NGINX service change, you can
update the one component definition and have all uses of it benefit.

### Define a new component

To define a new component, create a class called `KubernetesNginxService` that derives from `ComponentResource`. It'll have a mostly-empty
constructor to start with but you will add the Kubernetes resources to it in the next step. You'll also define the inputs for the
component -- the `isMinikube` flag to determine service type -- and outputs -- a single property with the service `ip`.

To get going, create a new file {{< compfile >}} alongside {{< langfile >}} and add the following:

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

// Arguments for the Kubernetes NGINX service component.
export interface KubernetesNginxServiceArgs {
    isMinikube: boolean; // whether running on minikube.
}

// A component that encapsulates creating a Kubernetes NGINX deployment and service.
export class KubernetesNginxService extends pulumi.ComponentResource {
    public readonly ip: pulumi.Output<string>; // the service ip.

    constructor(name: string, args: KubernetesNginxServiceArgs, opts?: pulumi.ComponentResourceOptions) {
        super("quickstart:index:KubernetesNginxService", name, args, opts);

        // Component initialization will go here next...

        this.registerOutputs({}); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service

# A component that encapsulates creating a Kubernetes NGINX deployment and service.
class KubernetesNginxService(pulumi.ComponentResource):
    def __init__(self, name: str, is_minikube: bool = False, opts = None):
        super().__init__('quickstart:index:KubernetesNginxService', name, { 'isMinikube': is_minikube }, opts)

        # Component initialization will go here next...

        self.register_outputs({}) # Signal component completion.
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type KubernetesNginxService struct {
    pulumi.ResourceState
    Ip pulumi.StringOutput // the service ip.
}

type KubernetesNginxServiceArgs struct {
    IsMinikube bool // whether running on minikube.
}

func NewKubernetesNginxService(ctx *pulumi.Context, name string, args KubernetesNginxServiceArgs, opts ...pulumi.ResourceOption) (*KubernetesNginxService, error) {
    self := &KubernetesNginxService{}
    err := ctx.RegisterComponentResource("quickstart:index:KubernetesNginxService", name, self, opts...)
    if err != nil {
        return nil, err
    }

    // Component initialization will go here next...

    ctx.RegisterResourceOutputs(self, pulumi.Map{}) // Signal component completion.
    return self, nil
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

public class KubernetesNginxServiceArgs
{
    public bool IsMinikube { get; set; }
}

public class KubernetesNginxService : Pulumi.ComponentResource
{
    public Output<string> Ip { get; private set; }

    public KubernetesNginxService(string name, KubernetesNginxServiceArgs args, ComponentResourceOptions? opts = null)
        : base("quickstart:index:KubernetesNginxService", name, opts)
    {
        // Component initialization will go here next...

        this.RegisterOutputs(new Dictionary<string, object>{}); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.resources.ComponentResource;
import com.pulumi.resources.ComponentResourceOptions;
import com.pulumi.core.Output;

public class KubernetesNginxServiceArgs {
    public boolean isMinikube;
    public KubernetesNginxServiceArgs(boolean isMinikube) {
        this.isMinikube = isMinikube;
    }
}

public class KubernetesNginxService extends ComponentResource {
    public Output<String> ip;

    public KubernetesNginxService(String name, KubernetesNginxServiceArgs args, ComponentResourceOptions opts) {
        super("quickstart:index:KubernetesNginxService", name, args, opts);

        // Component initialization will go here next...

        this.registerOutputs(java.util.Map.of());
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/kubernetes/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

This defines a component but it doesn't do much yet.

### Refactor your code into the component

Next, make three changes:

1. Move all resources from {{< langfile >}} into the component's constructor
2. Change each resource to use the component [as the `parent`](/docs/iac/concepts/options/parent/)
3. Assign the service output to the `ip` property of the component

The resulting {{< compfile >}} file will look like this; you can make each edit one at a time if preferred
to get a feel for things, or simply paste the contents of this into {{< compfile >}}:

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

// Arguments for the Kubernetes NGINX service component.
export interface KubernetesNginxServiceArgs {
    isMinikube: boolean; // whether running on minikube.
}

// A component that encapsulates creating a Kubernetes NGINX deployment and service.
export class KubernetesNginxService extends pulumi.ComponentResource {
    public readonly ip: pulumi.Output<string>; // the service ip.

    constructor(name: string, args: KubernetesNginxServiceArgs, opts?: pulumi.ComponentResourceOptions) {
        super("quickstart:index:KubernetesNginxService", name, args, opts);

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
        }, {
            parent: this,
        });

        // Allocate an IP to the Deployment.
        const frontend = new k8s.core.v1.Service(appName, {
            metadata: { labels: deployment.spec.template.metadata.labels },
            spec: {
                type: args.isMinikube ? "ClusterIP" : "LoadBalancer",
                ports: [{ port: 80, targetPort: 80, protocol: "TCP" }],
                selector: appLabels
            }
        }, {
            parent: this,
        });

        // Capture the IP and make it available as a component property and output:
        this.ip = args.isMinikube
            ? frontend.spec.clusterIP
            : frontend.status.loadBalancer.apply(
                  (lb) => lb.ingress[0].ip || lb.ingress[0].hostname
              );
        this.registerOutputs({ ip: this.ip }); // Signal component completion.
    }
}
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
from pulumi_kubernetes.apps.v1 import Deployment
from pulumi_kubernetes.core.v1 import Service

# A component that encapsulates creating a Kubernetes NGINX deployment and service.
class KubernetesNginxService(pulumi.ComponentResource):
    def __init__(self, name: str, is_minikube: bool = False, opts = None):
        super().__init__('quickstart:index:KubernetesNginxService', name, { 'isMinikube': is_minikube }, opts)

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
            },
            opts=pulumi.ResourceOptions(parent=self))

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
            },
            opts=pulumi.ResourceOptions(parent=self))

        # Capture the IP and make it available as a component property and output
        result = None
        if is_minikube:
            result = frontend.spec.apply(lambda v: v["cluster_ip"] if "cluster_ip" in v else None)
        else:
            ingress = frontend.status.load_balancer.apply(lambda v: v["ingress"][0] if "ingress" in v else "output<string>")
            result = ingress.apply(lambda v: v["ip"] if v and "ip" in v else (v["hostname"] if v and "hostname" in v else "output<string>"))

        self.ip = result
        self.register_outputs({ 'ip': self.ip }) # Signal component completion.
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apps/v1"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type KubernetesNginxService struct {
    pulumi.ResourceState
    Ip pulumi.StringOutput // the service ip.
}

type KubernetesNginxServiceArgs struct {
    IsMinikube bool // whether running on minikube.
}

func NewKubernetesNginxService(ctx *pulumi.Context, name string, args KubernetesNginxServiceArgs, opts ...pulumi.ResourceOption) (*KubernetesNginxService, error) {
    self := &KubernetesNginxService{}
    err := ctx.RegisterComponentResource("quickstart:index:KubernetesNginxService", name, self, opts...)
    if err != nil {
        return nil, err
    }

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
    }, pulumi.Parent(self))
    if err != nil {
        return nil, err
    }

    feType := "LoadBalancer"
    if args.IsMinikube {
        feType = "ClusterIP"
    }

    template := deployment.Spec.ApplyT(func(v appsv1.DeploymentSpec) *corev1.PodTemplateSpec {
        return &v.Template
    }).(corev1.PodTemplateSpecPtrOutput)

    meta := template.ApplyT(func(v *corev1.PodTemplateSpec) *metav1.ObjectMeta { return v.Metadata }).(metav1.ObjectMetaPtrOutput)

    frontend, _ := corev1.NewService(ctx, appName, &corev1.ServiceArgs{
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
    }, pulumi.Parent(self))

    var ip pulumi.StringOutput

    if args.IsMinikube {
        ip = frontend.Spec.ApplyT(func(val corev1.ServiceSpec) string {
            if val.ClusterIP != nil {
                return *val.ClusterIP
            }
            return ""
        }).(pulumi.StringOutput)
    } else {
      ip = frontend.Status.ApplyT(func(val *corev1.ServiceStatus) string {
          if val.LoadBalancer.Ingress != nil && len(val.LoadBalancer.Ingress) > 0 {
              ingress := val.LoadBalancer.Ingress[0]
              if ingress.Ip != nil {
                  return *ingress.Ip
              }
              if ingress.Hostname != nil {
                  return *ingress.Hostname
              }
          }
          return ""
      }).(pulumi.StringOutput)
    }

    self.Ip = ip
    ctx.RegisterResourceOutputs(self, pulumi.Map{"ip": ip}) // Signal component completion.
    return self, nil
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

public class KubernetesNginxServiceArgs
{
    public bool IsMinikube { get; set; }
}

public class KubernetesNginxService : Pulumi.ComponentResource
{
    public Output<string> Ip { get; private set; }

    public KubernetesNginxService(string name, KubernetesNginxServiceArgs args, ComponentResourceOptions? opts = null)
        : base("quickstart:index:KubernetesNginxService", name, opts)
    {
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
        }, new CustomResourceOptions
        {
            Parent = this,
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
                Type = args.IsMinikube
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
        }, new CustomResourceOptions
        {
            Parent = this,
        });

        this.Ip = args.IsMinikube
            ? frontend.Spec.Apply(spec => spec.ClusterIP)
            : frontend.Status.Apply(status =>
            {
                var ingress = status.LoadBalancer.Ingress[0];
                return ingress.Ip ?? ingress.Hostname;
            });

        this.RegisterOutputs(new Dictionary<string, object?>{
            ["ip"] = this.Ip
        });
    }
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.*;
import com.pulumi.core.*;
import com.pulumi.resources.*;

import com.pulumi.kubernetes.apps.v1.Deployment;
import com.pulumi.kubernetes.apps.v1.DeploymentArgs;
import com.pulumi.kubernetes.apps.v1.inputs.DeploymentSpecArgs;
import com.pulumi.kubernetes.core.v1.*;
import com.pulumi.kubernetes.core.v1.ServiceArgs;
import com.pulumi.kubernetes.core.v1.enums.ServiceSpecType;
import com.pulumi.kubernetes.core.v1.inputs.*;
import com.pulumi.kubernetes.meta.v1.inputs.LabelSelectorArgs;
import com.pulumi.kubernetes.meta.v1.inputs.ObjectMetaArgs;
import java.util.Map;

class KubernetesNginxServiceArgs extends ResourceArgs {
    public boolean isMinikube;
    public KubernetesNginxServiceArgs(boolean isMinikube) {
        this.isMinikube = isMinikube;
    }
}

class KubernetesNginxService extends ComponentResource {
    public Output<String> ip;

    public KubernetesNginxService(String name, KubernetesNginxServiceArgs args) {
        this(name, args, null);
    }

    public KubernetesNginxService(String name, KubernetesNginxServiceArgs args, ComponentResourceOptions opts) {
        super("quickstart:index:KubernetesNginxService", name, args, opts);

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
            .build(), CustomResourceOptions.builder().parent(this).build());

        var frontend = new Service("nginx", ServiceArgs.builder()
            .metadata(ObjectMetaArgs.builder()
                .labels(labels)
                .build())
            .spec(ServiceSpecArgs.builder()
                .type(args.isMinikube ? ServiceSpecType.ClusterIP : ServiceSpecType.LoadBalancer)
                .selector(labels)
                .ports(ServicePortArgs.builder()
                    .port(80)
                    .targetPort(80)
                    .protocol("TCP")
                    .build())
                .build())
            .build(), CustomResourceOptions.builder().parent(this).build());

        // Export the service cluster IP (available for both ClusterIP and LoadBalancer types)
        this.ip = frontend.spec().applyValue(spec -> spec.clusterIP().orElse("pending"));
        this.registerOutputs(Map.of("ip", this.ip));
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/kubernetes/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

### Instantiate the component

Now go back to your original file {{< langfile >}}. Now that you have moved all of the resources, you can start over with a clean slate.
Ensure the file is empty and we will build it back up by simply importing and instantiating our new component.

Add this to your now-empty {{< langfile >}}:

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";

// Import from our new component module:
import { KubernetesNginxService } from "./nginx";

// Read the configuration value:
const config = new pulumi.Config();

// Create an instance of our component:
const nginx = new KubernetesNginxService("my-nginx", {
    isMinikube: config.requireBoolean("isMinikube")
});

// And export its autoassigned IP:
export const ip = nginx.ip;
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi

# Import from our new component module:
from nginx import KubernetesNginxService

# Read the configuration value:
config = pulumi.Config()

# Create an instance of our component:
nginx = KubernetesNginxService('my-nginx', is_minikube=config.require_bool("isMinikube"))

# And export its autoassigned IP:
pulumi.export("ip", nginx.ip)
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        // Read the configuration value:
        isMinikube := config.GetBool(ctx, "isMinikube")

        // Create an instance of our component:
        nginx, err := NewKubernetesNginxService(ctx, "my-nginx", KubernetesNginxServiceArgs{
            IsMinikube: isMinikube,
        })
        if err != nil {
            return err
        }

        // And export its autoassigned IP:
        ctx.Export("ip", nginx.Ip)
        return nil
    })
}

```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using Pulumi;
using System.Collections.Generic;

return await Pulumi.Deployment.RunAsync(() =>
{
    // Read the configuration value:
    var config = new Pulumi.Config();

    // Create an instance of our component:
    var nginx = new KubernetesNginxService("my-nginx", new KubernetesNginxServiceArgs()
    {
        IsMinikube = config.GetBoolean("isMinikube") ?? false
    });

   // And export its autoassigned IP:
   return new Dictionary<string, object?>
   {
      ["ip"] = nginx.Ip
   };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package myproject;

import com.pulumi.Pulumi;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Read the configuration value:
            var config = ctx.config();

            // Create an instance of our component:
            var nginx = new KubernetesNginxService("my-nginx",
                new KubernetesNginxServiceArgs(config.requireBoolean("isMinikube")));

            // And export its autoassigned IP:
            ctx.export("ip", nginx.ip);
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

{{% notes type="warning" %}}

Unfortunately, YAML lacks the language facilities to author components. Feel free to [skip ahead](/docs/iac/get-started/kubernetes/destroy-stack/).

{{% /notes %}}

{{% /choosable %}}

### Deploy the component

Now deploy the resulting component instantiation. To do so, run `pulumi up` as usual:

```
$ pulumi up
Previewing update (dev)

     Type                                        Name                  Plan
     pulumi:pulumi:Stack                         quickstart-dev
 +   ├─ quickstart:index:KubernetesNginxService  my-nginx              create
 +   │  ├─ kubernetes:apps/v1:Deployment         nginx                 create
 +   │  └─ kubernetes:core/v1:Service            nginx                 create
 -   ├─ kubernetes:core/v1:Service               nginx                 delete
 -   └─ kubernetes:apps/v1:Deployment            nginx                 delete

Outputs:
  ~ ip: "10.110.183.208" => "10.96.0.0"

Resources:
    + 3 to create
    - 2 to delete
    5 changes. 1 unchanged

Do you want to perform this update?  [Use arrows to move, type to filter]
> yes
  no
  details
```

This preview shows you a few things. First, you'll see our `KubernetesNginxService` component with all of its children resources neatly parented underneath it. This helps to see what resources relate to which components. Next, you'll see that your old resources are being destroyed.

{{% notes type="info" %}}

If you're wondering why Pulumi didn't simply update the resources in place, it's because certain changes -- like
refactoring resources into a component -- fundamentally change a resource's identity. Many changes like updating
properties or moving resources between files are not disruptive like this. In such cases, you can assign
[aliases](/docs/iac/concepts/options/aliases/) to prevent deletions from happening.

{{% /notes %}}

Accept the changes by selecting `yes` and the deployment will occur:

```
Updating (dev)

     Type                                       Name                  Status
     pulumi:pulumi:Stack                        quickstart-dev
 +   ├─ quickstart:index:KubernetesNginxService  my-nginx            created (2s)
 +   │  ├─ kubernetes:apps/v1:Deployment        nginx                 created (1s)
 +   │  └─ kubernetes:core/v1:Service           nginx                 created (9s)
 -   ├─ kubernetes:core/v1:Service              nginx                 deleted (4s)
 -   └─ kubernetes:apps/v1:Deployment           nginx                 deleted (0.92s)

Outputs:
  ~ ip: "10.110.183.208" => "10.103.199.118"

Resources:
    + 3 created
    - 2 deleted
    5 changes. 1 unchanged

Duration: 13s
```

Now test out your new NGINX service -- it works like before, just with a tidier codebase now!

{{% notes type="info" %}}
**If using Minikube:** Minikube does not support type `LoadBalancer`. Instead, forward the NGINX service:

```bash
$ kubectl get service
NAME             TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)   AGE
kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP   44h
nginx-9e5d5cd4   ClusterIP   10.103.199.118   <none>        80/TCP    6m47s
```

The assigned name for this particular nginx service is `nginx-9e5d5cd4`; yours will be different. In a new terminal window, run:

```bash
$ kubectl port-forward service/nginx-9e5d5cd4 8080:80
Forwarding from 127.0.0.1:8080 -> 80
Forwarding from [::1]:8080 -> 80
```

{{% /notes %}}

You can curl NGINX to verify it is running:

{{% choosable os "macos,linux" %}}

```bash
$ $(pulumi config get isMinikube) && curl "http://localhost:8080" || curl $(pulumi stack output ip)
```

{{% /choosable %}}

{{% choosable os "windows" %}}

```powershell
> if (pulumi config get isMinikube) { curl "http://localhost:8080" } else { curl $(pulumi stack output ip) }
```

{{% /choosable %}}

Expected output:

```html
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
<style>
html { color-scheme: light dark; }
body { width: 35em; margin: 0 auto;
font-family: Tahoma, Verdana, Arial, sans-serif; }
</style>
</head>
<body>
<h1>Welcome to nginx!</h1>
<p>If you see this page, the nginx web server is successfully installed and
working. Further configuration is required.</p>

<p>For online documentation and support please refer to
<a href="http://nginx.org/">nginx.org</a>.<br/>
Commercial support is available at
<a href="http://nginx.com/">nginx.com</a>.</p>

<p><em>Thank you for using nginx.</em></p>
</body>
</html>
```

Once you are ready to move on, destroy everything you've provisioned in this tutorial.

{{< get-started-stepper >}}
