---
title: "Providers"
meta_desc: The providers resource option specifies a set of explicitly configured providers to be used for a resource and all of its children.
menu:
  intro:
    identifier: providers
    parent: options
    weight: 11
---

The `providers` resource option sets a map of providers for the resource and its children. This map is combined with resource parent's `providers` map. If no value is provided, the providers map is identical to the parent's providers map. When determining which provider to use for a resource, the `providers` map is used if [provider]({{< relref "provider" >}}) is not supplied.

{{< chooser language "javascript,typescript,python,go,yaml" >}}

{{% choosable language javascript %}}

```javascript
let awsProvider = new aws.Provider("awsProvider", { region: "us-west-2" });
let kubeProvider = new kubernetes.Provider("kubernetesProvider", {
    kubeconfig: "./kubeconfig" });

let opts = { providers: [awsProvider, kubeProvider] };

let vpc = new aws.ec2.Vpc("vpc", {}, opts);
let namespace = new kubernetes.v1.Namespace("namespace", {}, opts);
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let awsProvider = new aws.Provider("awsProvider", { region: "us-west-2" });
let kubeProvider = new kubernetes.Provider("kubeProvider", {
    kubeconfig: "./kubeconfig" });

let opts = { providers: [awsProvider, kubeProvider] };

let vpc = new aws.ec2.Vpc("vpc", {}, opts);
let k8_namespace = new kubernetes.v1.Namespace("namespace", {}, opts);
```

{{% /choosable %}}
{{% choosable language python %}}

```python
aws_provider = aws.Provider("awsProvider", region="us-west-2")
kube_provider = kubernetes.Provider("kubeProvider", kubeconfig="./kubeconfig)

opts = ResourceOptions(providers=[aws_provder, kube_provider])

vpc = aws.ec2.Vpc("vpc", opts=opts)
namespace = kubernetes.v1.Namespace("namespace", opts=opts)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
awsProvider, _ := aws.NewProvider(ctx, "awsProvider", &aws.ProviderArgs{
	Region: pulumi.StringPtr("us-west-2"),
})
kubeProvider, _ := kubernetes.NewProvider(ctx, "kubeProvider", &kubernetes.ProviderArgs{
	Kubeconfig: pulumi.StringPtr("./kubeconfig"),
})

providers := pulumi.Providers(awsProvider, kubeProvider)

vpc, _ := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{}, providers)
namespace, _ := v1.NewNamespace(ctx, "namespace", &v1.NamespaceArgs{}, providers)
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
  providers:
    - ${awsProvider}
    - ${kubeProvider}
resources:
  awsProvider:
    type: pulumi:providers:aws
    properties:
      region: us-west-2
  kubeProvider:
    type: pulumi:providers:kubernetes
    properties:
      kubeconfig: ./kubeconfig
  vpc:
    type: aws:ec2:Vpc
    options:
      providers: ${providers}
  namespace:
    options:
      providers: ${providers}
```

{{% /choosable %}}

{{< /chooser >}}
