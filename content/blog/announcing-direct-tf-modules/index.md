---
title: "Introducing Pulumi Support for Executing Terraform Modules"
allow_long_title: true
date: 2024-06-05T00:00:00-04:00
draft: false
meta_desc: "Pulumi can now execute Terraform modules directly"
meta_image: "meta.png"
authors:
  - anton-tayanovskyy
tags:
  - terraform
  - features
---

Today Pulumi is introducing the capability to execute
[Terraform modules directly](https://www.pulumi.com/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/).
This makes migrating complex infrastructure from Terraform to Pulumi us now simpler than ever.

<!--more-->

We are releasing this feature in response to user feedback: our users tell us that while Pulumi's [pulumi convert
--from terraform](https://www.pulumi.com/blog/converting-full-terraform-programs-to-pulumi/) is very useful for small
programs, it runs into challenges on more complex projects, especially ones involving modules. With the new feature you
no longer need to convert module sources, and can immediately manage everything with Pulumi.

What is included in the launch:

- `pulumi package add terraform-module <module-source> [<version>] <pulumi-package-name>` command can now run modules
  from Terraform and OpenTofu registries as well as locally managed modules under Pulumi. This is enabled by the new
  [terraform-module](https://github.com/pulumi/pulumi-terraform-module) provider.

- `pulumi convert --from terraform` now supports a `// @pulumi-terraform-module <pulumi-package-name>` annotation to
  avoid translating a module recursively and instead execute it directly.

- Pulumi providers expose helper methods to assist with keeping config consistent across Pulumi and Terraform providers
  required to run modules. For example, [AWS provider](https://github.com/pulumi/pulumi-aws) allows to query
  `awsProvider.terraformConfig()`.

## How it works

Under the hood Pulumi orchestrates an configurable executor such as `tofu` or `terraform` CLI to run updates against
your infrastructure. Module code executes under exact Terraform semantics, but participates in Pulumi lifecycle with
`pulumi {preview,up,refresh,destroy}`. Module inputs and outputs are exposed in a type-safe manner to your favorite
Pulumi programming language, to be freely composed with other Pulumi components. Finally, Terraform state is
automatically [stored in Pulumi](https://www.pulumi.com/docs/iac/concepts/state-and-backends/) and takes full advantage
of proper [secret encryption](https://www.pulumi.com/docs/iac/concepts/secrets/).

## Walkthrough

To get started, run the following command in an existing Pulumi directory, linking a module as a package and giving it
a friendly name "vpcmod":

```
$ pulumi package add terraform-module terraform-aws-modules/vpc/aws 5.18.1 vpcmod
Successfully generated a Nodejs SDK for the vpcmod package at /Users/anton/tmp/2025-05-14/blog/sdks/vpcmod
```

Notice that Pulumi generated a local SDK for the module:

```
$ ls sdks/vpcmod
README.md       index.ts        node_modules    provider.ts     tsconfig.json   utilities.ts
bin             module.ts       package.json    scripts         types
```

And linked it into your project in `package.json`:


```
    "dependencies": {
        ...,
        "@pulumi/vpcmod": "file:sdks/vpcmod"
    }
```

You can now reference the module from your code with full code completion support. For example:

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

If you have AWS credentials set up, you can now do `pulumi up` and it will show all the resources being created:

TODO: the preview update section looks different with views.

```

Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/anton-pulumi-corp/anton-blog/dev/previews/5851682a-a3e3-4f47-a50e-3d7b4f4e6c34

     Type                                         Name                                                    Plan
 +   pulumi:pulumi:Stack                          anton-blog-dev                                          create
 +   └─ vpcmod:index:Module                       test-vpc                                                create
 +      ├─ vpcmod:index:ModuleState               test-vpc-state                                          create
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
 + 22 to create

Previewing update (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/anton-pulumi-corp/anton-blog/dev/previews/faab8c4d-3a86-42f6-9685-ef36ece68652

     Type                                         Name                                                    Plan
 +   pulumi:pulumi:Stack                          anton-blog-dev                                          create
 +   └─ vpcmod:index:Module                       test-vpc                                                create
 +      ├─ vpcmod:index:ModuleState               test-vpc-state                                          create
 +      ├─ vpcmod:tf:aws_route                    module.test-vpc.aws_route.private_nat_gateway[0]        create
 +      ├─ vpcmod:tf:aws_default_route_table      module.test-vpc.aws_default_route_table.default[0]      create
 +      ├─ vpcmod:tf:aws_route_table              module.test-vpc.aws_route_table.public[0]               create
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.private[1]                   create
 +      ├─ vpcmod:tf:aws_default_network_acl      module.test-vpc.aws_default_network_acl.this[0]         create
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.private[0]                   create
 +      ├─ vpcmod:tf:aws_route                    module.test-vpc.aws_route.public_internet_gateway[0]    create
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.public[0]   create
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.private[0]  create
 +      ├─ vpcmod:tf:aws_route_table              module.test-vpc.aws_route_table.private[0]              create
 +      ├─ vpcmod:tf:aws_eip                      module.test-vpc.aws_eip.nat[0]                          create
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.public[1]                    create
 +      ├─ vpcmod:tf:aws_internet_gateway         module.test-vpc.aws_internet_gateway.this[0]            create
 +      ├─ vpcmod:tf:aws_default_security_group   module.test-vpc.aws_default_security_group.this[0]      create
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.public[1]   create
 +      ├─ vpcmod:tf:aws_vpc                      module.test-vpc.aws_vpc.this[0]                         create
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.public[0]                    create
 +      ├─ vpcmod:tf:aws_nat_gateway              module.test-vpc.aws_nat_gateway.this[0]                 create
 +      └─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.private[1]  create

Resources:
    + 22 to create

Updating (dev)

View in Browser (Ctrl+O): https://app.pulumi.com/anton-pulumi-corp/anton-blog/dev/updates/1

     Type                                         Name                                                    Status
 +   pulumi:pulumi:Stack                          anton-blog-dev                                          created (145s)
 +   └─ vpcmod:index:Module                       test-vpc                                                created (143s)
 +      ├─ vpcmod:index:ModuleState               test-vpc-state                                          created (133s)
 +      ├─ vpcmod:tf:aws_route_table              module.test-vpc.aws_route_table.private[0]              created (1s)
 +      ├─ vpcmod:tf:aws_internet_gateway         module.test-vpc.aws_internet_gateway.this[0]            created (0.58s)
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.public[1]   created (0.76s)
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.public[1]                    created (1.00s)
 +      ├─ vpcmod:tf:aws_route_table              module.test-vpc.aws_route_table.public[0]               created (1s)
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.private[1]                   created (2s)
 +      ├─ vpcmod:tf:aws_route                    module.test-vpc.aws_route.public_internet_gateway[0]    created (1s)
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.public[0]                    created (3s)
 +      ├─ vpcmod:tf:aws_default_security_group   module.test-vpc.aws_default_security_group.this[0]      created (4s)
 +      ├─ vpcmod:tf:aws_default_route_table      module.test-vpc.aws_default_route_table.default[0]      created (4s)
 +      ├─ vpcmod:tf:aws_default_network_acl      module.test-vpc.aws_default_network_acl.this[0]         created (2s)
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.public[0]   created (2s)
 +      ├─ vpcmod:tf:aws_eip                      module.test-vpc.aws_eip.nat[0]                          created (3s)
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.private[1]  created (3s)
 +      ├─ vpcmod:tf:aws_subnet                   module.test-vpc.aws_subnet.private[0]                   created (1s)
 +      ├─ vpcmod:tf:aws_nat_gateway              module.test-vpc.aws_nat_gateway.this[0]                 created (1s)
 +      ├─ vpcmod:tf:aws_route_table_association  module.test-vpc.aws_route_table_association.private[0]  created (2s)
 +      ├─ vpcmod:tf:aws_vpc                      module.test-vpc.aws_vpc.this[0]                         created (2s)
 +      └─ vpcmod:tf:aws_route                    module.test-vpc.aws_route.private_nat_gateway[0]        created (3s)

Resources:
    + 22 created

Duration: 2m26s
```

The infrastructure has now provisioned and the corresponding Terraform state is stored securely inside the Pulumi
state, which can be verified with `pulumi stack export`.

The above program is very simple. To take it further, check out
[examples](https://github.com/pulumi/pulumi-terraform-module/tree/main/examples) for more realistic programs showcasing
features such as computing subnets dynamically with Pulumi `aws.getAvailabilityZonesOutput` function or passing the
results of the VPC module to an EKS module.

### convert

If you are instead starting from a Terraform program, you can use `pulumi convert` instead. Just make sure to annotate
the modules with a special comment marker `// @pulumi-terraform-module`. For example, given this `infra.tf`:

```terraform
// @pulumi-terraform-module vpcmod
module "my-vpc" {
  source             = "terraform-aws-modules/vpc/aws"
  version            = "5.18.1"
  azs                = ["us-west-2a", "us-west-2b"]
  name               = "test-vpc-123"
  public_subnets     = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets    = ["10.0.3.0/24", "10.0.4.0/24"]
  enable_nat_gateway = true
  single_nat_gateway = true
}
```

Run `pulumi convert` as follows:

``` shell
pulumi convert --from terraform --language typescript --out my-pulumi-project
```

The resulting `my-pulumi-project` folder will have the project setup correctly for executing the `my-vpc` module.

### terraformConfig

A quick note on configuration. It can be confusing that modules need Terraform providers to execute and those are
distinct from Pulumi providers that may also be needed in your program. Fortunately there is a simple way to keep your
configuration in sync. For example, if you already have configured an AWS provider in your program, you can reuse its
`terraformConfig` to configure the matching Terraform AWS provider:

```typescript
const awsProvider = new aws.Provider("awsprovider", {
    region: "us-east-1",
    // more configuration
})

// Pass the AWS configuration to your VPC module provider instead of re-entering config settings in TF notation
const vpcmodProvider = new vpcmod.Provider("vpcprovider", {
    "aws": awsProvider.terraformConfig().result
})

// Use the VPC module provider in your Module as before
const vpc = new vpcmod.Module("test-vpc", {...},
    {provider: vpcmodProvider}
);
```

This is also a great example of how the Pulumi Terraform Module fits into existing Pulumi programs - you can pass inputs
and outputs from one resource into the other.


## Supported Features

The power of Pulumi is that all components can be composed seamlessly with modules, including chaining and wrapping.

All the regular operations are supported:

- Pulumi executes preview/update/refresh as expected
- The entire resource tree being constructed is made visible
- Updates detail which concrete module-managed resources are changing
- Pulumi generates typed input and output accessors to interop with the module
- Pulumi handles first-class secrets and unknown values seamlessly
- Pulumi supports configuring the Terraform providers powering the module execution

## Limitations

As of today some Pulumi features will not work as expected with resources managed by a directly executed Terraform
module:

- using the [transformations](https://www.pulumi.com/docs/iac/concepts/options/transformations/) resource option
- using targeted operations such as `pulumi up --target`
- the [protect](https://www.pulumi.com/docs/iac/concepts/options/protect/) resource option

Pulumi's capability to infer accurate types for module inputs and outputs is also currently limited and will sometimes
infer sub-optimal or even unusable types. See [README](https://github.com/pulumi/pulumi-terraform-module) for
configuration options.

## What's next

We are working on enhancing state import from Terraform into Pulumi to work in tandem with source conversion and
provide a seamless migration experience.

## Get Started

Support for modules is available as of today. Download the latest Pulumi CLI and it a try. If you run into any issues
or have suggestions and feedback, please
[let us know](https://github.com/pulumi/pulumi-terraform-module/issues/new/choose) or reach out in the
[Pulumi Community Slack](https://slack.pulumi.com/).
