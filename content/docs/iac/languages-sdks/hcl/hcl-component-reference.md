---
title_tag: "Pulumi HCL Component Reference | Languages & SDKs"
meta_desc: Specification for authoring Pulumi multi-language components in HCL.
title: Component Reference
h1: Pulumi HCL component reference
menu:
    iac:
        identifier: hcl-component-reference
        name: Component Reference
        parent: iac-languages-hcl
        weight: 2
    languages:
        identifier: hcl-component-reference
        parent: hcl-language
        weight: 2
---

Pulumi HCL modules can be authored as reusable Pulumi components consumable from any Pulumi language (TypeScript, Python, Go, .NET, Java, YAML, or HCL). This is known as a multi-language component (MLC).

Any directory of `.tf` files with a `PulumiPlugin.yaml` containing `runtime: hcl` is an MLC — no extra declaration is required. The `component` and `package` blocks inside the module's `terraform` block are optional refinements that set the component's name and the package's name and version. The rest of the module is an ordinary Pulumi HCL program — see the [Pulumi HCL reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/) for the full program model.

## Example

`PulumiPlugin.yaml`:

```yaml
name: my-networking
runtime: hcl
```

`main.tf`:

```hcl
terraform {
  component {
    name = "VpcNetwork"
  }
  package {
    name    = "my-networking"
    version = "1.0.0"
  }
  required_providers {
    aws = {
      source  = "pulumi/aws"
      version = "6.0.0"
    }
  }
}

variable "cidr_block" {
  type    = string
  default = "10.0.0.0/16"
}

resource "aws_vpc" "vpc" {
  cidr_block = var.cidr_block
}

output "vpc_id" {
  value = aws_vpc.vpc.id
}
```

The module's [`variable`](/docs/iac/languages-sdks/hcl/hcl-language-reference/#variables) blocks become the component's inputs and its [`output`](/docs/iac/languages-sdks/hcl/hcl-language-reference/#outputs) blocks become the component's outputs. A component's inputs are also echoed back as outputs, so a consumer of the example above can read both `vpcId` and `cidrBlock` off the component instance.

## Name translation

HCL names are snake_case, while Pulumi schemas are camelCase, so variable and output names are translated at the component boundary. Consumers written in TypeScript, Python, Go, .NET, Java, or YAML see the camelCase form: the example's `cidr_block` input is `cidrBlock` and its `vpc_id` output is `vpcId`. The translation applies recursively to object fields at every depth. Map keys are user data and are never renamed.

HCL consumers keep the module's original snake_case names.

## Component definition

### `component` block

Declares the HCL module as a component resource.

| Field    | Type   | Required | Default   | Description |
| - | - | - | - | - |
| `name`   | string | Yes      | —         | Component name. Must be a valid Pulumi name (alphanumerics, hyphens, underscores, and periods). |
| `module` | string | No       | `"index"` | Module segment of the component's resource token. Must be a valid Pulumi name. |

### `package` block

Declares the package identity for the component.

| Field     | Type   | Required | Default                         | Description |
| - | - | - | - | - |
| `name`    | string | No       | Derived from the module source  | Package name. Must be a valid Pulumi name (alphanumerics, hyphens, underscores, and periods) when specified. |
| `version` | string | No       | `"0.0.0-dev"`                   | Package version. Must be a full `X.Y.Z` [semver](https://semver.org/) version when specified — `"1.0"` is rejected. |

When `package.name` is omitted, the package name is derived from the module source. For a local module it is the module's directory name. For a remote module it is the last segment of the source — a registry module name or a repository name — lowercased and reduced to `[a-z0-9-]`, so a source ending in `My_VPC` yields the package name `my-vpc`.

Only one `component` block and one `package` block are allowed per `terraform` block. Using `component` or `package` in a regular Pulumi program (one invoked directly via `pulumi up`) produces an error.

## Resource token

The component's Pulumi resource token is formed as:

```
{package.name}:{component.module}:{component.name}
```

For the example above the token is `my-networking:index:VpcNetwork`.

A module with no `component` or `package` block takes the default for every segment, so a module in a directory named `randommodule` yields the token `randommodule:index:Module`, which an HCL consumer references as `randommodule_module`.

## Consuming a component

Add the component to a Pulumi project with `pulumi package add`, which generates a typed SDK for the project's language.

For a module on the local filesystem, pass its directory:

```bash
pulumi package add ../randommodule
```

For a remote module — a Git repository or a Terraform registry module — parameterize the `hcl` provider with the module source and an optional version:

```bash
pulumi package add hcl module terraform-aws-modules/vpc/aws 5.0.0
```

Pulumi downloads the module and every module it references, bundles the tree into the package so it resolves without further network access, and generates the SDK.

Once added, the component is instantiated like any other Pulumi component resource, from TypeScript, Python, Go, .NET, Java, YAML, or HCL. Non-HCL languages use the camelCase property names described in [Name translation](#name-translation); HCL programs use the module's snake_case names.

## Publishing

An HCL component package is distributed and published like a component authored in any other language — it is a [source-based plugin package](/docs/iac/guides/building-extending/components/packaging-components/#source-based-plugin-packages), and nothing about the workflow is HCL-specific. Pulumi Cloud customers can publish versions to the Pulumi IDP Private Registry with [`pulumi package publish`](/docs/iac/cli/commands/pulumi_package_publish/). See [Packaging Components](/docs/iac/guides/building-extending/components/packaging-components/) for the packaging options and their trade-offs.

## PulumiPlugin.yaml

The `PulumiPlugin.yaml` file tells the Pulumi engine how to run the component provider. For HCL MLCs it specifies the `hcl` runtime and the package name:

```yaml
name: my-networking
runtime: hcl
```

The `component` and `package` blocks in the HCL source supply the component's token and version. When the `package` block is omitted, the package name falls back to the name derived from the module source.
