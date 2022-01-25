---
title: "Version"
meta_desc: The version resource option specifies a provider version to use when operating on a resource.
menu:
  intro:
    identifier: version
    parent: options
    weight: 14
---

The `version` resource option specifies a provider version to use when operating on a resource. This version overrides the version information inferred from the current package. This option should be used rarely.

{{< chooser language "javascript,typescript,python,go,csharp" >}}

{{% choosable language javascript %}}

```javascript
let vpc = new aws.ec2.Vpc("vpc", {}, { version: "2.10.0" });
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let vpc = new aws.ec2.Vpc("vpc", {}, { version: "2.10.0" });
```

{{% /choosable %}}
{{% choosable language python %}}

```python
vpc = ec2.Vpc("vpc", opts=ResourceOptions(version="2.10.0"))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
vpc, _ := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{}, pulumi.Version("2.10.0"))
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var vpc = new Aws.Ec2.Vpc("vpc", new Aws.Ec2.VpcArgs(),
    new CustomResourceOptions { Version = "2.10.0" });
```

{{% /choosable %}}

{{< /chooser >}}
