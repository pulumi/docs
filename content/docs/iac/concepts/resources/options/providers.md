---
title_tag: "providers | Resource Options"
meta_desc: The providers resource option specifies a set of explicitly configured providers to be used for a resource and all of its children.
title: "providers"
h1: "Resource option: providers"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  iac:
    identifier: providers
    parent: options-concepts
    weight: 150
aliases:
  - /docs/iac/concepts/options/providers/
  - /docs/concepts/resources/options/providers/
  - /docs/concepts/options/providers/
---

The `providers` resource option is supported only on [component resources](/docs/iac/concepts/components/). It sets a map of providers (keyed by package name) for the component and its child resources — the map flows from the component to every child via parent inheritance. To pass an explicit provider to a single custom resource, use the [`provider`](/docs/iac/concepts/resources/options/provider/) option instead.

{{< resource-option-scope "providers" >}}

When the SDK creates a resource it picks a provider by checking, in order:

1. The explicit `provider` option, if set.
1. A matching provider in the resource's `providers` map (looked up by package name).
1. A matching provider inherited from the parent's `providers` map.

The first match wins. So a child resource created with a component as its parent automatically picks up the matching provider from the component's inherited map — a child `aws.s3.Bucket` picks up the `aws` provider, a child `kubernetes.helm.v3.Chart` picks up the `kubernetes` provider, and so on. If a component is itself a child of another component, its providers are inherited from that parent in turn.

## Example

A component can be instantiated multiple times against different sets of providers. Suppose `MyComponent` deploys a regional AWS database alongside a Helm chart on a Kubernetes cluster in the same region. To run the component in two regions from a single Pulumi program, declare a separate AWS provider and Kubernetes provider for each region, then pass the matching pair into each component instance via the `providers` map.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";
import * as k8s from "@pulumi/kubernetes";

const awsEast = new aws.Provider("aws-east", { region: "us-east-1" });
const awsWest = new aws.Provider("aws-west", { region: "us-west-2" });

const k8sEast = new k8s.Provider("k8s-east", { kubeconfig: kubeconfigEast });
const k8sWest = new k8s.Provider("k8s-west", { kubeconfig: kubeconfigWest });

const east = new MyComponent("east", {}, {
    providers: { aws: awsEast, kubernetes: k8sEast },
});

const west = new MyComponent("west", {}, {
    providers: { aws: awsWest, kubernetes: k8sWest },
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_kubernetes as k8s

aws_east = aws.Provider("aws-east", region="us-east-1")
aws_west = aws.Provider("aws-west", region="us-west-2")

k8s_east = k8s.Provider("k8s-east", kubeconfig=kubeconfig_east)
k8s_west = k8s.Provider("k8s-west", kubeconfig=kubeconfig_west)

east = MyComponent("east", MyComponentArgs(), pulumi.ResourceOptions(providers={
    "aws": aws_east,
    "kubernetes": k8s_east,
}))

west = MyComponent("west", MyComponentArgs(), pulumi.ResourceOptions(providers={
    "aws": aws_west,
    "kubernetes": k8s_west,
}))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
awsEast, err := aws.NewProvider(ctx, "aws-east", &aws.ProviderArgs{
    Region: pulumi.String("us-east-1"),
})
if err != nil {
    return err
}
awsWest, err := aws.NewProvider(ctx, "aws-west", &aws.ProviderArgs{
    Region: pulumi.String("us-west-2"),
})
if err != nil {
    return err
}

k8sEast, err := k8s.NewProvider(ctx, "k8s-east", &k8s.ProviderArgs{
    Kubeconfig: pulumi.String(kubeconfigEast),
})
if err != nil {
    return err
}
k8sWest, err := k8s.NewProvider(ctx, "k8s-west", &k8s.ProviderArgs{
    Kubeconfig: pulumi.String(kubeconfigWest),
})
if err != nil {
    return err
}

_, err = NewMyComponent(ctx, "east", &MyComponentArgs{},
    pulumi.ProviderMap(map[string]pulumi.ProviderResource{
        "aws":        awsEast,
        "kubernetes": k8sEast,
    }))
if err != nil {
    return err
}

_, err = NewMyComponent(ctx, "west", &MyComponentArgs{},
    pulumi.ProviderMap(map[string]pulumi.ProviderResource{
        "aws":        awsWest,
        "kubernetes": k8sWest,
    }))
if err != nil {
    return err
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var awsEast = new Pulumi.Aws.Provider("aws-east",
    new Pulumi.Aws.ProviderArgs { Region = "us-east-1" });
var awsWest = new Pulumi.Aws.Provider("aws-west",
    new Pulumi.Aws.ProviderArgs { Region = "us-west-2" });

var k8sEast = new Pulumi.Kubernetes.Provider("k8s-east",
    new Pulumi.Kubernetes.ProviderArgs { KubeConfig = kubeconfigEast });
var k8sWest = new Pulumi.Kubernetes.Provider("k8s-west",
    new Pulumi.Kubernetes.ProviderArgs { KubeConfig = kubeconfigWest });

var east = new MyComponent("east", new MyComponentArgs(),
    new ComponentResourceOptions {
        Providers = { awsEast, k8sEast },
    });

var west = new MyComponent("west", new MyComponentArgs(),
    new ComponentResourceOptions {
        Providers = { awsWest, k8sWest },
    });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var awsEast = new com.pulumi.aws.Provider("aws-east",
    com.pulumi.aws.ProviderArgs.builder().region("us-east-1").build());
var awsWest = new com.pulumi.aws.Provider("aws-west",
    com.pulumi.aws.ProviderArgs.builder().region("us-west-2").build());

var k8sEast = new com.pulumi.kubernetes.Provider("k8s-east",
    com.pulumi.kubernetes.ProviderArgs.builder()
        .kubeconfig(kubeconfigEast).build());
var k8sWest = new com.pulumi.kubernetes.Provider("k8s-west",
    com.pulumi.kubernetes.ProviderArgs.builder()
        .kubeconfig(kubeconfigWest).build());

var east = new MyComponent("east", new MyComponentArgs(),
    ComponentResourceOptions.builder().providers(awsEast, k8sEast).build());

var west = new MyComponent("west", new MyComponentArgs(),
    ComponentResourceOptions.builder().providers(awsWest, k8sWest).build());
```

{{% /choosable %}}

{{< /chooser >}}
