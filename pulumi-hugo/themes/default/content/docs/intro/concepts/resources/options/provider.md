---
title: "Provider"
meta_desc: The provider resource option passes an explicitly configured provider to be used instead of the global or ambient provider.
menu:
  intro:
    identifier: provider
    parent: options
    weight: 10
---

The `provider` resource option sets a provider for the resource. For more information, see [Providers]({{< relref "../providers" >}}). The default is to inherit this value from the parent resource, and to use the ambient provider specified by Pulumi configuration for resources without a parent.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let provider = new aws.Provider("provider", { region: "us-west-2" });
let vpc = new aws.ec2.Vpc("vpc", {}, { provider: provider });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let provider = new aws.Provider("provider", { region: "us-west-2" });
let vpc = new aws.ec2.Vpc("vpc", {}, { provider: provider });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
provider = Provider("provider", region="us-west-2")
vpc = ec2.Vpc("vpc", opts=ResourceOptions(provider=provider))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
provider, _ := aws.NewProvider(ctx, "provider", &aws.ProviderArgs{Region: pulumi.StringPtr("us-west-2")})
vpc, _ := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{}, pulumi.Provider(provider))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var provider = new Aws.Provider("provider", new Aws.ProviderArgs { Region = "us-west-2" });
var vpc = new Aws.Ec2.Vpc("vpc", new Aws.Ec2.VpcArgs(),
    new CustomResourceOptions { Provider = provider });
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var provider = new Provider("provider",
    ProviderArgs.builder()
        .region("us-west-2")
        .build();

var vpc = new Vpc("vpc",
    VpcArgs.Empty,
    CustomResourceOptions.builder()
        .provider(provider)
        .build());
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  provider:
    type: pulumi:providers:aws
    properties:
      region: us-west-2
  vpc:
    type: aws:ec2:Vpc
    options:
      provider: ${provider}
```

{{% /choosable %}}

{{< /chooser >}}
