---
title: "New: Use Terraform Modules in Pulumi Without Conversion"
allow_long_title: true
date: 2025-06-23
draft: false
meta_desc: "Pulumi can now execute Terraform modules within Pulumi directly, making migration from Terraform to Pulumi simpler than ever for complex infrastructure projects."
meta_image: "meta.png"
authors:
  - anton-tayanovskyy
tags:
  - terraform
  - features
  - migration
  - infrastructure-as-code
social:
  twitter: |
    Pulumi now supports executing Terraform modules directly! No more complex conversions for module-heavy projects. Migrate from Terraform to Pulumi with ease.
  linkedin: |
    We're excited to announce that Pulumi can now execute Terraform modules directly, addressing one of the biggest challenges in migrating complex infrastructure from Terraform to Pulumi.

    This new capability eliminates the need to convert module sources, allowing teams to immediately manage everything with Pulumi while maintaining the exact Terraform semantics they're familiar with.

    Key benefits:
    • Seamless migration for module-heavy projects
    • Type-safe integration with Pulumi programming languages
    • Automatic state management in Pulumi Cloud
    • Full support for Terraform and OpenTofu registries

    This represents a significant step forward in making infrastructure migration accessible to teams of all sizes.
---

Today, we're excited to announce a major advancement in Pulumi's mission to make modern infrastructure as code accessible to every developer: **direct support for executing Terraform modules**. This new capability addresses one of the most significant challenges our users face when migrating from Terraform to Pulumi—complex projects with extensive module dependencies.

<!--more-->

## The Path to Modern Infrastructure as Code

At Pulumi, we believe the ideal infrastructure as code experience leverages the full power of modern programming languages, AI-assisted development, and cloud-native tooling. Our vision is that every team should be able to write infrastructure code in their preferred language—TypeScript, Python, Go, C#, or Java—with full IntelliSense, testing capabilities, and AI-powered assistance.

However, we also understand the reality that many organizations have invested years building extensive Terraform module estates. These modules often contain critical business logic, compliance configurations, and battle-tested patterns that teams can't always rewrite overnight.

This new capability bridges that gap, giving you the best of both worlds: **the ability to start new projects in Pulumi immediately while preserving your existing Terraform modules until you're ready to migrate them**.

## Strategic Migration Approach

Here's how we recommend teams approach this transition:

**Phase 1: New Projects in Pulumi**
Start all new infrastructure projects in Pulumi to immediately gain the benefits of modern IaC—better developer experience, AI assistance, and cloud-native tooling.

**Phase 2: Incremental Module Migration**
Use the new Terraform module support to bring existing modules into Pulumi projects without rewriting them. This gives you immediate access to Pulumi Cloud's state management, deployment workflows, and team collaboration features across all your IaC.

**Phase 3: Full Migration (When Ready)**
Gradually migrate your Terraform modules to native Pulumi components as time and resources permit. With AI-assisted development tools making this easier than ever, you can modernize at your own pace.

This approach eliminates the "big bang" migration risk while ensuring you're not stuck with legacy tooling for new projects.

## What This Means for Your Team

This isn't just a technical feature—it's a strategic enabler for teams looking to modernize their infrastructure practices. Here's what this announcement means:

**For Terraform Users**: You can now migrate to Pulumi incrementally, keeping your existing modules intact while gaining access to Pulumi's powerful programming language features, better state management, and enhanced developer experience.

**For Platform Teams**: You can standardize on Pulumi for new infrastructure while seamlessly incorporating existing Terraform modules, reducing migration risk and accelerating adoption.

**For DevOps Engineers**: You get the best of both worlds—the reliability of proven Terraform modules with Pulumi's superior tooling, testing capabilities, and deployment workflows.

## How It Works

The new feature consists of three key components:

### 1. Direct Module Execution

The `pulumi package add terraform-module` command now supports modules from Terraform and OpenTofu registries, as well as locally managed modules. This is powered by our new [terraform-module provider](https://github.com/pulumi/pulumi-terraform-module), which orchestrates Terraform execution while maintaining the full Pulumi lifecycle.

### 2. Enhanced Conversion Support

Our `pulumi convert --from terraform` tool now supports a special annotation `// @pulumi-terraform-module <pulumi-package-name>` that tells the converter to execute modules directly rather than attempting to translate them. This preserves your existing module logic while enabling Pulumi's benefits.

### 3. Configuration Synchronization

Pulumi providers now expose helper methods like `awsProvider.terraformConfig()` to keep configuration consistent between Pulumi and Terraform providers, eliminating the need to maintain duplicate configuration.

## Real-World Impact

Let me walk you through a practical example that demonstrates the power of this integration.

First, [install the latest version of the Pulumi CLI](/docs/install/) (v3.178.0 or later is required) and create a new Pulumi project using `pulumi new $language` such as `pulumi new typescript`.

### Setting Up a VPC Module

Next, add a Terraform module to your Pulumi project:

{{% chooser language "typescript,python,go,csharp,yaml" %}}

{{% choosable language typescript %}}

```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpcmod
Successfully generated a Nodejs SDK for the vpcmod package at /Users/anton/tmp/2025-06-23/blog/sdks/vpcmod
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpcmod

Successfully generated a Python SDK for the vpcmod package at /workdir/vpcmod

Resolved 13 packages in 111ms
      Built pulumi-vpcmod @ file:///workdir/sdks/vpcmod
Prepared 4 packages in 297ms
Installed 4 packages in 1ms
 + arpeggio==2.0.2
 + attrs==25.3.0
 + parver==0.5
 + pulumi-vpcmod==6.0.0 (from file:///workdir/sdks/vpcmod)

You can then import the SDK in your Python code with:

  import pulumi_vpcmod as vpcmod
```

{{% /choosable %}}

{{% choosable language go %}}
```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpcmod

Using Terraform CLI for schema inference
Successfully generated a Go SDK for the vpcmod package at /workdir/sdks/vpcmod
Go mod file updated to use local sdk for vpcmod
To use this package, import github.com/pulumi/pulumi-terraform-module/sdks/go/vpcmod/v6/vpcmod
Added package "vpcmod" to Pulumi.yaml
```
{{% /choosable %}}

{{% choosable language csharp %}}
```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpcmod

Using Terraform CLI for schema inference
Successfully generated a .NET SDK for the vpcmod package at /workdir/sdks/vpcmod

Reference `sdks\vpcmod\Pulumi.Vpcmod.csproj` added to the project.
You also need to add the following to your .csproj file of the program:

  <DefaultItemExcludes>$(DefaultItemExcludes);sdks/**/*.cs</DefaultItemExcludes>

You can then use the SDK in your .NET code with:

  using Pulumi.Vpcmod;

Added package "vpcmod" to Pulumi.yaml
```
{{% /choosable %}}

{{% choosable language yaml %}}
```bash
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 6.0.0 vpcmod

Added package "vpcmod" to Pulumi.yaml
```
{{% /choosable %}}

{{% /chooser %}}

Pulumi automatically generates a local SDK with full support for your language:

{{% chooser language "typescript,python,go,yaml" %}}

{{% choosable language typescript %}}
```bash
$ ls sdks/vpcmod
README.md       index.ts        node_modules    provider.ts     tsconfig.json   utilities.ts
bin             module.ts       package.json    scripts         types
```
{{% /choosable %}}

{{% choosable language python %}}
```bash
$ ls sdks/vpcmod
build                   pulumi_vpcmod           pulumi_vpcmod.egg-info  setup.py
```
{{% /choosable %}}

{{% choosable language go %}}
```bash
$ ls sdks/vpcmod
go.mod  vpcmod
```
{{% /choosable %}}

{{% choosable language csharp %}}
```bash
$ ls sdks/vpcmod
Inputs                  Provider.cs             README.md
logo.png                pulumi-plugin.json      Utilities.cs
Module.cs               Pulumi.Vpcmod.csproj    version.txt
```
{{% /choosable %}}

{{% choosable language yaml %}}
```bash
$ ls sdks/vpcmod
vpcmod-6.0.0.yaml
```
{{% /choosable %}}

{{% /chooser %}}

Pulumi automatically links the generated SDK into your project.

### Using the Module in Your Code

Now you can use the module with full IntelliSense support:

{{% chooser language "typescript,python,go,yaml" %}}

{{% choosable language typescript %}}
```typescript
import * as pulumi from "@pulumi/pulumi";
import * as vpcmod from '@pulumi/vpcmod';

const vpc = new vpcmod.Module("test-vpc", {
    azs: ["us-west-2a", "us-west-2b"],
    name: `test-vpc-${pulumi.getStack()}`,
    cidr: "10.0.0.0/16",
    public_subnets: [
        "10.0.1.0/24",
        "10.0.2.0/24",
    ],
    private_subnets: [
        "10.0.3.0/24",
        "10.0.4.0/24",
    ],
    enable_nat_gateway: true,
    single_nat_gateway: true,
});

export const publicSubnets = vpc.public_subnets;
export const privateSubnets = vpc.private_subnets;
```
{{% /choosable %}}

{{% choosable language python %}}
```python
import pulumi
import pulumi_aws as aws
import pulumi_vpcmod as vpcmod

aws_provider = aws.Provider("awsprovider", region="us-east-1")

vpcmod_provider = vpcmod.Provider("vpcprovider", aws=aws_provider.terraform_config().result)

vpc = vpcmod.Module(
    "test-vpc",
    azs=["us-west-2a", "us-west-2b"],
    name=f"test-vpc{pulumi.get_stack()}",
    cidr="10.0.0.0/16",
    public_subnets=[
        "10.0.1.0/24",
        "10.0.2.0/24",
    ],
    private_subnets=[
        "10.0.3.0/24",
        "10.0.4.0/24",
    ],
    enable_nat_gateway=True,
    single_nat_gateway=True,
)

pulumi.export("publicSubnets", vpc.public_subnets)
pulumi.export("privateSubnets", vpc.private_subnets)
```
{{% /choosable %}}

{{% choosable language go %}}

``` go
package main

import (
	"fmt"

	"github.com/pulumi/pulumi-terraform-module/sdks/go/vpcmod/v6/vpcmod"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func run(ctx *pulumi.Context) error {
	stack := ctx.Stack()

	vpc, err := vpcmod.NewModule(ctx, "test-vpc", &vpcmod.ModuleArgs{
		Azs: pulumi.StringArray{
			pulumi.String("us-west-2a"),
			pulumi.String("us-west-2b"),
		},
		Name: pulumi.String(fmt.Sprintf("test-vpc-%s", stack)),
		Cidr: pulumi.String("10.0.0.0/16"),
		Public_subnets: pulumi.StringArray{
			pulumi.String("10.0.1.0/24"),
			pulumi.String("10.0.2.0/24"),
		},
		Private_subnets: pulumi.StringArray{
			pulumi.String("10.0.3.0/24"),
			pulumi.String("10.0.4.0/24"),
		},
		Enable_nat_gateway: pulumi.Bool(true),
		Single_nat_gateway: pulumi.Bool(true),
	})
	if err != nil {
		return err
	}

	ctx.Export("publicSubnets", vpc.Public_subnets)
	ctx.Export("privateSubnets", vpc.Private_subnets)

	return nil
}

func main() {
	pulumi.Run(run)
}
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
using System.Collections.Generic;
using Pulumi;
using Vpc = Pulumi.Vpcmod;

return await Deployment.RunAsync(() =>
{
    var vpc = new Vpc.Module("test-vpc", new Vpc.ModuleArgs
    {
        Azs = new string [] {
            "us-west-2a",
            "us-west-2b",
        },
        Cidr = "10.0.0.0/16",
        Public_subnets = new string[] {
            "10.0.1.0/24",
            "10.0.2.0/24"
        },
        Private_subnets = new string[] {
            "10.0.1.0/24",
            "10.0.2.0/24"
        },
        Enable_nat_gateway=true,
        Single_nat_gateway=true
    });

    return new Dictionary<string, object?>
    {
        ["publicSubnets"] = vpc.Public_subnets,
        ["privateSubnets"] = vpc.Private_subnets
    };
});
```
{{% /choosable %}}

{{% choosable language yaml %}}

``` yaml
name: my-program

runtime: yaml

resources:
  vpc:
    type: vpcmod:index:Module
    properties:
      azs:
        - us-west-2a
        - us-west-2b
      name: test-vpc-${pulumi.stack}
      cidr: 10.0.0.0/16
      public_subnets:
        - 10.0.1.0/24
        - 10.0.2.0/24
      private_subnets:
        - 10.0.3.0/24
        - 10.0.4.0/24
      enable_nat_gateway: true
      single_nat_gateway: true

outputs:
  publicSubnets: ${vpc.public_subnets}
  privateSubnets: ${vpc.private_subnets}

packages:
  vpcmod:
    source: terraform-module
    version: 0.1.7
    parameters:
      - terraform-aws-modules/vpc/aws
      - 6.0.0
      - vpcmod
```

{{% /choosable %}}

{{% /chooser %}}


### Seamless Deployment

When you run `pulumi up`, Pulumi orchestrates the Terraform module execution while providing its signature preview and deployment experience:

```bash
Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/anton-pulumi-corp/anton-blog/dev/previews/5851682a-a3e3-4f47-a50e-3d7b4f4e6c34

     Type                                         Name                                                    Plan
 +   pulumi:pulumi:Stack                          anton-blog-dev                                          create
 +   └─ vpcmod:index:Module                       test-vpc                                                create
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.private[0]  create
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.private[1]                   create
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.public[1]   create
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.private[0]                   create
 +      ├─ vpcmod:tf:aws_route_table              module.test-vpc.aws_route_table.private[0]              create
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.public[1]                    create
 +      ├─ vpcmod:tf:aws_nat_gateway              module.test-vpc.aws_nat_gateway.this[0]                 create
 +      ├─ vpcmod:tf:aws_route                    module.test-vpc.aws_route.public_internet_gateway[0]    create
 +      ├─ vpcmod:tf:aws_route                    module.test-vpc.aws_route.private_nat_gateway[0]        create
 +      ├─ vpcmod:tf:aws_default_network_acl      module.test-vpc.aws_default_network_acl.this[0]         create
 +      ├─ vpcmod:tf:aws_default_route_table      module.test-vpc.aws_default_route_table.default[0]      create
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.public[0]                    create
 +      ├─ vpcmod:tf:aws_internet_gateway         module.test-vpc.aws_internet_gateway.this[0]            create
 +      ├─ vpcmod:tf:aws_vpc                      module.test-vpc.aws_vpc.this[0]                         create
 +      ├─ vpcmod:tf:aws_default_security_group   module.test-vpc.aws_default_security_group.this[0]      create
 +      ├─ vpcmod:tf:aws_route_table              module.test-vpc.aws_route_table.public[0]               create
 +      ├─ vpcmod:tf:aws_eip                      module.test-vpc.aws_eip.nat[0]                          create
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.public[0]   create
 +      └─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.private[1]  create

Resources:
 + 21 to create
```

The infrastructure deploys successfully, and the Terraform state is automatically stored securely in Pulumi Cloud with full [secret encryption](/docs/iac/concepts/secrets/) support.

## Migration Made Simple

For teams starting with existing Terraform code, the migration process is straightforward. Simply annotate your modules with a special comment:

```terraform
// @pulumi-terraform-module vpcmod
module "my-vpc" {
  source             = "terraform-aws-modules/vpc/aws"
  version            = "6.0.0"
  azs                = ["us-west-2a", "us-west-2b"]
  name               = "test-vpc-123"
  public_subnets     = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets    = ["10.0.3.0/24", "10.0.4.0/24"]
  enable_nat_gateway = true
  single_nat_gateway = true
}
```

Then run the conversion (replace `typescript` with your language of choice):

```bash
pulumi convert --from terraform --language typescript --out my-pulumi-project
```

The resulting project is ready to deploy with full Pulumi functionality.

## Configuration Management

One of the key benefits is seamless configuration management. Instead of maintaining separate configurations for Pulumi and Terraform providers, you can reuse your existing Pulumi provider configuration:

{{% chooser language "typescript,python,go" %}}

{{% choosable language typescript %}}

```typescript
const awsProvider = new aws.Provider("awsprovider", {
    region: "us-west-2",
    // more configuration
});

// Pass the AWS configuration to your VPC module provider
const vpcmodProvider = new vpcmod.Provider("vpcprovider", {
    "aws": awsProvider.terraformConfig().result
});

// Use the VPC module provider in your Module
const vpc = new vpcmod.Module("test-vpc", {...},
    {provider: vpcmodProvider}
);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi
import pulumi_aws as aws
import pulumi_vpcmod as vpcmod

aws_provider = aws.Provider("awsprovider", region="us-west-2")

# Pass the AWS configuration to your VPC module provider
vpcmod_provider = vpcmod.Provider("vpcprovider", aws=aws_provider.terraform_config().result)

# Use the VPC module provider in your Module
vpc = vpcmod.Module("test-vpc", ..., opts=pulumi.ResourceOptions(provider=vpcmod_provider))
```

{{% /choosable %}}

{{% choosable language go %}}

```go
func run(ctx *pulumi.Context) error {
	stack := ctx.Stack()

	awsProvider, err := aws.NewProvider(ctx, "awsprovider", &aws.ProviderArgs{
		Region: pulumi.String("us-west-2"),
	})
	if err != nil {
		return err
	}

	awsProviderTfConfig, err := awsProvider.TerraformConfig(ctx)
	if err != nil {
		return err
	}

	// Pass the AWS configuration to your VPC module provider
	vpcProvider, err := vpcmod.NewProvider(ctx, "vpcprovider", &vpcmod.ProviderArgs{
		Aws: awsProviderTfConfig.Result(),
	})
	if err != nil {
		return err
	}

	// Use the VPC module provider in your Module
	vpc, err := vpcmod.NewModule(ctx, "test-vpc", &vpcmod.ModuleArgs{...}, pulumi.Provider(vpcProvider))
	if err != nil {
		return err
	}

	ctx.Export("publicSubnets", vpc.Public_subnets)
	ctx.Export("privateSubnets", vpc.Private_subnets)

	return nil
}
```

{{% /choosable %}}


{{% /chooser %}}

This demonstrates how Terraform modules integrate seamlessly with existing Pulumi programs, allowing you to compose infrastructure components naturally.

## What's Supported

The integration provides comprehensive support for Pulumi's core features:

- **Full Lifecycle Management**: Preview, update, refresh, and destroy operations work exactly as expected
- **Resource Visibility**: The entire resource tree is visible in Pulumi's UI and CLI
- **Type Safety**: Generated TypeScript interfaces provide IntelliSense and compile-time checking
- **Secret Management**: First-class support for Pulumi's secret encryption
- **Provider Configuration**: Full control over Terraform provider settings

## Current Limitations

As with any new technology integration, there are some current limitations to be aware of:

- [Transforms](/docs/iac/concepts/options/transforms/) resource options are not supported
- Targeted operations like `pulumi up --target` are not available
- The [protect](/docs/iac/concepts/options/protect/) resource option is not supported
- Dependent resources may have limited support in some scenarios

## Looking Ahead

This release represents a significant milestone in our journey to make infrastructure as code accessible to every developer. We're already working on the next phase, which includes:

- Enhanced state import capabilities for seamless Terraform-to-Pulumi migrations
- Improved type inference for complex module schemas
- Expanded support for additional Terraform features

## The Path Forward

While this capability enables you to preserve your existing Terraform modules, we encourage teams to view this as a stepping stone rather than a final destination. The full benefits of modern infrastructure as code—including AI-assisted development, advanced testing capabilities, and seamless integration with modern development workflows—are best realized with native Pulumi components.

With AI developer tools making code conversion easier than ever, we're committed to helping teams migrate their Terraform modules to native Pulumi when they're ready. This capability ensures you can start your modernization journey today without being blocked by existing technical debt.

## Get Started Today

The Terraform module support is available immediately. [Install the latest Pulumi CLI](/docs/install/) and try it out with your existing Terraform modules. We've prepared comprehensive [examples](https://github.com/pulumi/pulumi-terraform-module/tree/main/examples) showcasing real-world scenarios, from simple VPC deployments to complex multi-module architectures.

If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/pulumi/pulumi-terraform-module/issues/new/choose) or reach out in our [Community Slack](https://slack.pulumi.com/). Your feedback is invaluable as we continue to evolve this capability.

This release embodies our commitment to meeting developers where they are while providing a clear path forward to modern infrastructure practices. We're excited to see how teams use this capability to accelerate their infrastructure modernization journey.
