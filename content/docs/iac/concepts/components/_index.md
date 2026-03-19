---
title_tag: "Component Resources"
meta_desc: Learn what Pulumi component resources are, how to consume them, and how to author your own reusable infrastructure building blocks.
title: Components
h1: Component resources
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Components
        parent: iac-concepts
        weight: 100
        identifier: iac-concepts-components
aliases:
- /docs/intro/concepts/resources/components/
- /docs/concepts/resources/components/
- /docs/iac/concepts/resources/components/
---

A component is a logical grouping of Pulumi resources that is exposed as a single Pulumi resource. Components encapsulate related resources and their configuration, letting consumers create complex infrastructure through a simple, well-defined interface—without needing to know the implementation details.

Components are part of [packages](/docs/iac/concepts/packages/), which are the distributable unit. A single package can contain multiple components alongside other resources and utilities.

For example, the [AWSx](/registry/packages/awsx/) package contains many components, including:

- `awsx.ec2.Vpc` — creates a complete VPC with subnets, route tables, and gateways preconfigured to AWS best practices.
- `awsx.ecs.FargateService` — creates an ECS service with a load balancer and all required networking.
- `awsx.ecr.Repository` — creates an ECR repository with image scanning and lifecycle policies.

Your organization might publish a package that contains components like:

- An `AcmeCorpVirtualMachine` component that enforces your company's tagging requirements on every VM it creates.
- A `SecureS3Bucket` component that bakes in encryption, versioning, and access logging so consumers get a compliant bucket by default.

Platform teams can use components to codify infrastructure best practices, security policies, and compliance requirements as reusable building blocks. When published to the [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/), packages containing components become discoverable across the organization and can be consumed by any team without needing to understand the underlying implementation.

{{< notes type="info" >}}
Components are analogous to [Terraform modules](https://developer.hashicorp.com/terraform/language/modules) and [AWS CDK Constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html). Pulumi also lets you consume Terraform modules and CDK constructs directly in your Pulumi programs. See [Use a Terraform Module](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) and [Pulumi CDK Adapter](/docs/iac/clouds/aws/guides/cdk/).
{{< /notes >}}

## Consuming components

How you consume a component depends on how it has been distributed.

### Local components

Components that live in the same repository as your Pulumi program are consumed by importing or referencing the class using your language's standard import mechanism—no additional installation steps are needed.

### Single-language packages

Some components are distributed as standard language packages without cross-language support. Add them to your project via your native package manager:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```bash
npm install @my-org/my-component
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
pip install my-org-my-component
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
go get github.com/my-org/my-component
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
dotnet add package MyOrg.MyComponent
```

{{% /choosable %}}
{{% choosable language java %}}

```xml
<dependency>
    <groupId>com.my-org</groupId>
    <artifactId>my-component</artifactId>
    <version>1.0.0</version>
</dependency>
```

{{% /choosable %}}

{{< /chooser >}}

### Cross-language packages without pre-published SDKs

Components distributed as Pulumi packages can be consumed in any language using the `pulumi package add` command. Pulumi generates an SDK for your language on-the-fly and wires it into your project:

```bash
pulumi package add github.com/my-org/my-component@v1.0.0
```

This pattern is common for components your organization publishes for internal consumption via a Git repository or the [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/).

### Cross-language packages with pre-published SDKs

Some packages with components have pre-generated SDKs published for each language, allowing consumers to install them directly via their native package manager without running `pulumi package add`. Pulumi-published packages such as [AWSx](/registry/packages/awsx/) are distributed this way. Your organization may also opt to publish SDKs for each language.

Add the package to your project using your native package manager:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```bash
npm install @pulumi/awsx
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
pip install pulumi-awsx
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
go get github.com/pulumi/pulumi-awsx/sdk/v3/go/awsx
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
dotnet add package Pulumi.Awsx
```

{{% /choosable %}}
{{% choosable language java %}}

```xml
<dependency>
    <groupId>com.pulumi</groupId>
    <artifactId>awsx</artifactId>
    <version>3.0.0</version>
</dependency>
```

{{% /choosable %}}

{{< /chooser >}}

{{< notes type="info" >}}
The [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/) provides a browsable gallery of all packages in use across your Pulumi Cloud organization, including packages containing components.
{{< /notes >}}

## Example: consuming a component

The `awsx.ec2.Vpc` component from the [AWSx](/registry/packages/awsx/) package is a good example of a component resource. It creates a complete VPC—including subnets, route tables, and internet gateways—behind a simple interface.

After adding the AWSx package (see above), instantiate the component like any other Pulumi resource, passing arguments and resource options:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```typescript
import * as awsx from "@pulumi/awsx";

const vpc = new awsx.ec2.Vpc("vpc", {
    subnetSpecs: [
        { type: awsx.ec2.SubnetType.Public, cidrMask: 22 },
        { type: awsx.ec2.SubnetType.Private, cidrMask: 20 },
    ],
}, { protect: true });

export const vpcId = vpc.vpcId;
export const privateSubnetIds = vpc.privateSubnetIds;
export const publicSubnetIds = vpc.publicSubnetIds;
```

{{% /choosable %}}
{{% choosable language python %}}

```python
import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("vpc",
    awsx.ec2.VpcArgs(
        subnet_specs=[
            awsx.ec2.SubnetSpecArgs(type=awsx.ec2.SubnetType.PUBLIC, cidr_mask=22),
            awsx.ec2.SubnetSpecArgs(type=awsx.ec2.SubnetType.PRIVATE, cidr_mask=20),
        ],
    ),
    opts=pulumi.ResourceOptions(protect=True),
)

pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
    "github.com/pulumi/pulumi-awsx/sdk/v3/go/awsx/ec2"
    "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        vpc, err := ec2.NewVpc(ctx, "vpc", &ec2.VpcArgs{
            SubnetSpecs: []ec2.SubnetSpecArgs{
                {Type: ec2.SubnetTypePublic, CidrMask: pulumi.IntRef(22)},
                {Type: ec2.SubnetTypePrivate, CidrMask: pulumi.IntRef(20)},
            },
        }, pulumi.Protect(true))
        if err != nil {
            return err
        }

        ctx.Export("vpcId", vpc.VpcId)
        ctx.Export("privateSubnetIds", vpc.PrivateSubnetIds)
        ctx.Export("publicSubnetIds", vpc.PublicSubnetIds)
        return nil
    })
}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
using Pulumi;
using System.Collections.Generic;
using Pulumi.Awsx.Ec2.Inputs;
using Ec2 = Pulumi.Awsx.Ec2;

return await Deployment.RunAsync(() =>
{
    var vpc = new Ec2.Vpc("vpc", new()
    {
        SubnetSpecs =
        {
            new SubnetSpecArgs { Type = Ec2.SubnetType.Public, CidrMask = 22 },
            new SubnetSpecArgs { Type = Ec2.SubnetType.Private, CidrMask = 20 },
        },
    }, new ComponentResourceOptions { Protect = true });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
        ["privateSubnetIds"] = vpc.PrivateSubnetIds,
        ["publicSubnetIds"] = vpc.PublicSubnetIds,
    };
});
```

{{% /choosable %}}
{{% choosable language java %}}

```java
package myproject;

import java.util.Arrays;
import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.enums.SubnetType;
import com.pulumi.awsx.ec2.inputs.SubnetSpecArgs;
import com.pulumi.resources.ComponentResourceOptions;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var vpc = new Vpc("vpc",
                VpcArgs.builder()
                    .subnetSpecs(Arrays.asList(
                        SubnetSpecArgs.builder().type(SubnetType.Public).cidrMask(22).build(),
                        SubnetSpecArgs.builder().type(SubnetType.Private).cidrMask(20).build()
                    ))
                    .build(),
                ComponentResourceOptions.builder().protect(true).build());

            ctx.export("vpcId", vpc.vpcId());
            ctx.export("privateSubnetIds", vpc.privateSubnetIds());
            ctx.export("publicSubnetIds", vpc.publicSubnetIds());
        });
    }
}
```

{{% /choosable %}}

{{< /chooser >}}

Notice that components are instantiated exactly like any other Pulumi resource: with a name, arguments defined by the component author, and resource options like `protect`.

### Components in `pulumi up` output

When you run `pulumi up`, components appear as a resource tree in the CLI output. Child resources are displayed nested under their parent component, giving you visibility into everything the component created on your behalf:

```output
Updating (dev):
     Type                            Name              Status
 +   pulumi:pulumi:Stack             my-stack          created
 +   └─ awsx:ec2:Vpc                 vpc               created
 +      └─ aws:ec2:Vpc               vpc               created
 +         ├─ aws:ec2:Subnet         vpc-private-1     created
 +         │  └─ aws:ec2:RouteTable  vpc-private-1     created
 +         │     ├─ aws:ec2:Route    vpc-private-1     created
 +         │     └─ aws:ec2:RouteTableAssociation  vpc-private-1  created
 +         └─ aws:ec2:Subnet         vpc-public-1      created
 +            └─ aws:ec2:RouteTable  vpc-public-1      created
 +               ├─ aws:ec2:Route    vpc-public-1      created
 +               └─ aws:ec2:RouteTableAssociation  vpc-public-1   created
```

This tree makes it clear that a single `awsx:ec2:Vpc` component encapsulates multiple AWS resources—subnets, route tables, routes, and associations—that would otherwise need to be defined and managed individually.

### Resource options and component resources

Resource options passed to a component resource do not always behave the same as they do for custom resources. For example, the `provider` option has no effect on a component—use `providers` instead to pass explicit provider configuration to a component's child resources. For a complete list of which options apply to component resources, see [Resource options and component resources](/docs/iac/concepts/resources/options/#resource-options-and-component-resources).

## Authoring a component

For a complete guide to writing a component—including how to define the component class, structure arguments, create child resources, register outputs, and configure provider inheritance—see [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/).

## Cross-language components

By default, components are authored and consumed in the same programming language by extending the `ComponentResource` class. However, components can also be made available to programs written in other languages. When configured for cross-language support, Pulumi can introspect your component class and automatically generate SDKs for consumption in any Pulumi language.

For detailed information on setting up and using cross-language components, including how to configure `PulumiPlugin.yaml`, define entry points, publish, and consume components, see [Cross-language Components](/docs/iac/concepts/components/cross-language-components/).

For a comparison of all component packaging approaches (single-language, cross-language, and provider-based), see [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/).

## Additional resources

- [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/) — Step-by-step guide to authoring a component from scratch, including setup, implementation, and publishing.
- [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) — How to package and distribute components for use by others.
- [Testing Components](/docs/iac/guides/building-extending/components/testing-components/) — How to write tests for your component resources.
- [Cross-language Components](/docs/iac/concepts/components/cross-language-components/) — How to make your component consumable in any Pulumi language.
- [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/) — How to publish and discover components within your organization.
