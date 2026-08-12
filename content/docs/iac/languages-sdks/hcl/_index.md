---
title_tag: "HCL | Languages & SDKs"
meta_desc: An overview of Pulumi HCL, a language plugin for writing infrastructure as code in Terraform-like HCL syntax on any cloud.
title: HCL
h1: Pulumi & HCL
menu:
    iac:
        name: HCL
        parent: iac-languages
        weight: 7
        identifier: iac-languages-hcl
    languages:
        identifier: hcl-language
        weight: 7

aliases:
- /docs/languages-sdks/hcl/
---

Pulumi supports writing your infrastructure as code using Pulumi HCL, a language plugin that lets you author Pulumi programs with [Terraform](https://developer.hashicorp.com/terraform)'s HCL syntax. You get familiar HCL blocks, expressions, and built-in functions while using Pulumi's state management, secrets handling, and deployment engine.

Pulumi HCL is developed in the [pulumi/pulumi-hcl](https://github.com/pulumi/pulumi-hcl) repository.

## Prerequisites

All you need to use Pulumi HCL is the [Pulumi CLI](/docs/install/), version 3.256.0 or later. The CLI downloads the HCL language and converter plugins automatically the first time you run an HCL project.

## Example

Pulumi HCL runs the same `.tf` files you would write for Terraform or OpenTofu. A project consists of a `Pulumi.yaml` with `runtime: hcl` and one or more `.tf` files in the project directory. Variable values load from `terraform.tfvars` and `*.auto.tfvars` files, stack configuration, and `TF_VAR_` environment variables, just as you'd expect.

`Pulumi.yaml`:

```yaml
name: simple-hcl
runtime: hcl
description: A simple Pulumi HCL project
```

`main.tf`:

```hcl
terraform {
  required_providers {
    random = {
      source  = "hashicorp/random"
      version = ">= 3.0.0"
    }
  }
}

variable "prefix" {
  type    = string
  default = "test"
}

resource "random_pet" "my_pet" {
  prefix = var.prefix
  length = 2
}

output "pet_name" {
  value = random_pet.my_pet.id
}
```

{{% notes type="info" %}}
Providers resolve the same way as OpenTofu: an unqualified source such as `random` (or a fully-qualified `hashicorp/random`) is looked up in the [OpenTofu registry](https://opentofu.org/registry/) and bridged into Pulumi automatically — no `required_providers` entry is required. Prefix a source with `pulumi/` (for example, `pulumi/aws`) to consume a native Pulumi provider instead.
{{% /notes %}}

Run `pulumi install` to fetch the SDKs for the providers your program uses, then `pulumi up` to deploy:

```bash
$ pulumi install
$ pulumi up
```

Re-run `pulumi install` whenever you change the set of providers your program uses.

`pulumi install` writes each provider's descriptor to `sdks/<provider>/hcl.sdk.json` in your project directory. Check the `sdks` directory into version control along with the rest of your program. A committed descriptor lets teammates and CI/CD run `pulumi preview` or `pulumi up` right away, without a `pulumi install` step first, and it keeps everyone resolving the same provider version. Without it, Pulumi reports unresolved package specs and stops until `pulumi install` runs. Unlike the [local SDKs generated for other languages](/docs/iac/concepts/providers/any-terraform-provider/#version-control-considerations), an `hcl.sdk.json` descriptor is a small, portable JSON file with no host-specific paths, so there's no repository-size tradeoff to weigh.

When you re-run `pulumi install` after changing providers, commit the updated descriptor too; the diff is a normal part of code review, the same way you'd review a lockfile change.

Further examples are available in the [Pulumi HCL GitHub repository](https://github.com/pulumi/pulumi-hcl/tree/master/examples). The specification for Pulumi HCL programs is in the [Pulumi HCL reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/).

## Pulumi programming model

The Pulumi programming model defines the core concepts you will use when creating infrastructure as code programs using Pulumi. [Concepts](/docs/iac/concepts/) describes these concepts with examples available in all supported languages.

To learn how the Pulumi programming model is implemented for Pulumi HCL, refer to the [Pulumi HCL reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/).

## Terraform compatibility

Pulumi HCL aims to run valid Terraform configurations without changes. Resources, data sources, variables, locals, outputs, modules, expressions, and most built-in functions work as documented by HashiCorp. A small number of behaviors differ:

- `backend`, `provider_meta`, `required_version`, and `experiments` in the `terraform` block are accepted but ignored with a warning — Pulumi manages state independently. A `cloud` block is an error.
- Terraform state files are not read or written. Bring existing resources into Pulumi with `pulumi import --from hcl <statefile>` rather than reusing a Terraform state file.
- Provisioner `connection` blocks support SSH only; WinRM is not supported.

For the full list of differences and unsupported features, see the [Terraform compatibility section](/docs/iac/languages-sdks/hcl/hcl-language-reference/#terraform-compatibility) of the reference.

## HCL packages

By default, providers resolve against the [OpenTofu registry](https://opentofu.org/registry/) and are bridged into Pulumi automatically, just as they are in OpenTofu. Pin a source and version with a `terraform` `required_providers` block when you need to.

The [Pulumi Registry](/registry/) also houses 100+ native Pulumi packages. Consume one instead of the bridged Terraform provider by declaring its source with the `pulumi/` namespace (for example, `pulumi/kubernetes`) in a `required_providers` block. Pulumi-sourced packages take an exact version such as `6.0.0` rather than a version constraint.
