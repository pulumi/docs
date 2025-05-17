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

We are excited to announce that Pulumi can now execute [Terraform modules
directly](https://github.com/pulumi/pulumi-terraform-module). This new capability unlocks a great option for users
contemplating migrating a large Terraform installation to Pulumi: when dealing with a complicated Terraform module, you
can now bypass translating its sources while still quickly moving its state over to Pulumi and cross-linking its inputs
and outputs with Pulumi code. Additionally, all Pulumi users can now more easily benefit from the existing awesome
modules in the Terraform registry.

<!--more-->

As organizations optimize their infrastructure management, many teams are exploring transitioning from Terraform to
Pulumi. However, migrating existing, complex Terraform configurations to Pulumi has often been cited as challenging,
especially when intricate Terraform modules are involved. Our customers tell us that Pulumi's [pulumi convert --from
terraform](https://www.pulumi.com/blog/converting-full-terraform-programs-to-pulumi/) is very useful for small to
medium programs, but runs into challenges on more complex projects, especially involving modules. Even when sources
convert successfully, full migration still requires meticulous validation to ensure production infrastructure
continuity is not affected by small differences in Pulumi and Terraform behavior.

To address this feedback, Pulumi is excited to announce new support for executing Terraform modules directly within
Pulumi. This new feature enables teams to continue utilizing their existing Terraform modules without source
modifications. Modules execute under their exact Terraform semantics powered by [OpenTofu](https://opentofu.org). Their
inputs and outputs are exposed in a type-safe manner to your favorite Pulumi programming language, to be freely
composed with other Pulumi components. Finally, Terraform state is automatically [stored in
Pulumi](https://www.pulumi.com/docs/iac/concepts/state-and-backends/) and takes full advantage of proper [secret
encryption](https://www.pulumi.com/docs/iac/concepts/secrets/).

Our hope is that this approach becomes an important part of the migration toolbox to be applied to selectively to those
parts of the codebase that have the highest migration risk and/or source complexity.

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

// TODO show-case cross-configuring the provider with a given AWS region
// TODO show-case converting TF programs with @sandbox annotation

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

As part of hardening this feature Pulumi will be looking at removing the limitations and improving error handling and
usability of the directly executed modules. Our team is currently excited about these possibilities:

- extending `pulumi convert --from terraform` to put the users in control of which modules are converted recursively to
  Pulumi source code, and which are instead converted into directly executed modules

- enhancing state import from Terraform into Pulumi to seamlessly work with directly executed modules

## Get Started

Support for modules is available as of today. Download the latest Pulumi CLI and it a try. If you run into any issues
or have suggestions and feedback, please [let us
know](https://github.com/pulumi/pulumi-terraform-module/issues/new/choose) or reach out in the [Pulumi Community
Slack](https://slack.pulumi.com/).
