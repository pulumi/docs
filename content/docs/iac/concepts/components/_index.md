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
- /docs/iac/concepts/components/cross-language-components/
---

<script>
    // The following list maps the headings that previously appeared on this page to their new locations.
    // We use this list to determine whether we can redirect visitors from the old content to the new.
    var redirects = {
        "#authoring-a-new-component-resource": "/docs/iac/guides/building-extending/components/build-a-component/",
        "#component-arguments-and-type-requirements": "/docs/iac/guides/building-extending/components/build-a-component/#component-arguments-and-type-requirements",
        "#creating-child-resources": "/docs/iac/guides/building-extending/components/build-a-component/#creating-child-resources",
        "#registering-component-outputs": "/docs/iac/guides/building-extending/components/build-a-component/#registering-component-outputs",
        "#inheriting-resource-providers": "/docs/iac/guides/building-extending/components/build-a-component/#inheriting-resource-providers",
    };

    var redirect = redirects[location.hash];
    if (redirect) {
        location.href = redirect;
    }
</script>

A component is a logical grouping of Pulumi resources that is exposed as a single Pulumi resource. Components encapsulate related resources and their configuration, letting consumers create complex infrastructure through a simple, well-defined interface—without needing to know the implementation details.

A component can live anywhere code lives: defined inline in a Pulumi program, shared through a language-ecosystem library, or distributed as part of a [Pulumi package](/docs/iac/concepts/packages/) whose [plugin](/docs/iac/concepts/plugins/) lets it be consumed from any Pulumi language. Pulumi packages are the most common distribution format for components intended for broad reuse, and a single package can contain multiple components alongside custom resources and functions — but a component is not required to be part of a package.

For example, the [AWSx](/registry/packages/awsx/) package contains many components, including:

- `awsx.ec2.Vpc` — creates a complete VPC with subnets, route tables, and gateways preconfigured to AWS best practices.
- `awsx.ecs.FargateService` — creates an ECS service with a load balancer and all required networking.
- `awsx.ecr.Repository` — creates an ECR repository with image scanning and lifecycle policies.

Your organization might publish a package that contains components like:

- An `AcmeCorpVirtualMachine` component that enforces your company's tagging requirements on every VM it creates.
- A `SecureS3Bucket` component that bakes in encryption, versioning, and access logging so consumers get a compliant bucket by default.

Platform teams can use components to codify infrastructure best practices, security policies, and compliance requirements as reusable building blocks. When published to the [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/), packages containing components become discoverable across the organization and can be consumed by any team without needing to understand the underlying implementation.

{{< notes type="info" >}}
Components are analogous to [Terraform modules](https://developer.hashicorp.com/terraform/language/modules) and [AWS CDK Constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html). Pulumi also lets you consume Terraform modules and CDK constructs directly in your Pulumi programs. See [Use a Terraform Module](/docs/iac/guides/building-extending/using-existing-tools/use-terraform-module/) and [Pulumi CDK Adapter](/docs/iac/guides/clouds/aws/cdk/).
{{< /notes >}}

## Consuming components

How you consume a component depends on how it has been distributed.

### Local components

Components that live in the same repository as your Pulumi program are consumed by importing or referencing the class using your language's standard import mechanism—no additional installation steps are needed.

### Native language packages

Some components are distributed as native language packages—standard packages published to a language registry (npm, PyPI, NuGet, Maven, etc.) without a Pulumi plugin. Because they have no cross-language support, they can only be consumed in the language in which they were authored. Add them to your project via your native package manager:

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

### Pulumi packages without pre-published SDKs

Components distributed as Pulumi packages can be consumed in any language using the `pulumi package add` command. Pulumi generates an SDK for your language on-the-fly and wires it into your project:

```bash
pulumi package add github.com/my-org/my-component@v1.0.0
```

This pattern is common for components your organization publishes for internal consumption via a Git repository or the [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/). It is also how components from a [source-based plugin package](#authoring-components) are consumed across languages — the SDK is generated in your program's language regardless of the language the component was authored in.

Under the hood, Pulumi fetches the package source (e.g. from GitHub), generates a [local package](/docs/iac/guides/building-extending/packages/local-packages/) SDK from the component's schema, and makes the generated SDK available for import in your program.

{{< notes type="info" >}}
**Runtime requirements:** because Pulumi generates the SDK from a live plugin, the plugin must be executable on your machine. The requirements are the same as for any Pulumi program written in the plugin's authoring language — see the [language SDK docs](/docs/iac/languages-sdks/) for the toolchain each language expects.
{{< /notes >}}

You can also point `pulumi package add` at a local directory instead of a Git URL — useful for monorepos, rapid iteration, or components that don't need to be published:

```bash
pulumi package add /path/to/local/secure-s3-component
```

Pulumi identifies the folder as a component package, generates a local SDK, and makes it available in your program — even if your program is written in a different language from the component.

### Pulumi packages with pre-published SDKs

Some Pulumi packages have pre-generated SDKs published for each language, allowing consumers to install them directly via their native package manager without running `pulumi package add`. Because the SDK is already compiled and published, no additional runtime is required beyond your own language toolchain. Pulumi-published packages such as [AWSx](/registry/packages/awsx/) are distributed this way. Your organization may also opt to publish SDKs for each language.

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

## Authoring components

You author a component by extending the `ComponentResource` class. The guides below walk through building, packaging, and testing components:

- [Build a Component](/docs/iac/guides/building-extending/components/build-a-component/) — define the class, structure arguments, create child resources, register outputs, and configure provider inheritance.
- [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) — compare the three distribution options and package a component for sharing.
- [Testing Components](/docs/iac/guides/building-extending/components/testing-components/) — write tests for component resources.
- [Pulumi IDP Private Registry](/docs/idp/concepts/private-registry/) — publish and discover components within your organization.
