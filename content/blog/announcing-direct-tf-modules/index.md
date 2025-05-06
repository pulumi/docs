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
pulumi package add terraform-module terraform-aws-modules/vpc/aws 5.18.1 vpcmod
```

While the example uses a well-known module from the registry, but a local path will also work to point to an in-house
or locally maintained module.

// What will this do.

// Make a simpler example.

// Cool if we could configure AWS Provider?

```typescript

import * as vpcmod from '@pulumi/vpcmod';
import * as std from '@pulumi/std';

const prefix = cfg.get("prefix") ?? pulumi.getStack();

const vpc = new vpcmod.Module("test-vpc", {
  azs: azs,
  name: `test-vpc-${prefix}`,
  cidr,
  private_subnets: azs.apply(azs => azs.map((_, i) =>
    std.cidrsubnetOutput({input: cidr, newbits: 8, netnum: i+1}).result
    return getCidrSubnet(cidr, 8, i+1);
  })),
  public_subnets: azs.apply(azs => azs.map((_, i) => {
    return getCidrSubnet(cidr, 8, i+1+4);
  })),
  intra_subnets: azs.apply(azs => azs.map((_, i) => {
    return getCidrSubnet(cidr, 8, i+1 + 8);
  })),


  enable_nat_gateway: true,
  single_nat_gateway: true,

  public_subnet_tags: {
    'kubernetes.io/role/elb': '1',
  },
  private_subnet_tags: {
    'kubernetes.io/role/internal-elb': '1',
  },
});

// export private subnets vpc.private_subnets.apply(subnets => subnets![0]),
```

// Show pulumi preview and pulumi up here.

// Note that pulumi preview and up explain what is changing inside the module.


## Supported Features

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

Pulumi's capability to infer accurate types for module inptus and outputs is also currently limited and will sometimes
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
