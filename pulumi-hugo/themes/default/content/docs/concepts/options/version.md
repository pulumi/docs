---
title_tag: "version | Resource Options"
meta_desc: The version resource option specifies a provider version to use when operating on a resource.
title: "version"
h1: "Resource option: version"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: version
    parent: options
    weight: 15
aliases:
- /docs/intro/concepts/resources/options/version/
---

The `version` resource option specifies a provider version to use when operating on a resource. This version overrides the version information inferred from the current package. This option was built to be used directly by the Pulumi SDK. `version` should not be used directly during normal operations.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

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
{{% choosable language java %}}

```java
var vpc = new com.pulumi.aws.ec2.Vpc("vpc",
    com.pulumi.aws.ec2.VpcArgs.Empty,
    CustomResourceOptions.builder()
        .version("2.10.0" )
        .build();
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  vpc:
    type: aws:ec2:Vpc
    options:
      version: "2.10.0"
```

{{% /choosable %}}

{{< /chooser >}}
