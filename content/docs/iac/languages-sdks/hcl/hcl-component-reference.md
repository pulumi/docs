---
title_tag: "Pulumi HCL Component Reference | Languages & SDKs"
meta_desc: Specification for authoring Pulumi multi-language components in HCL.
title: Component Reference
h1: Pulumi HCL component reference
meta_image: /images/docs/meta-images/docs-meta.png
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

An HCL module becomes an MLC when it has a `PulumiPlugin.yaml` containing `runtime: hcl` and declares a `component` block (and optionally a `package` block) inside the module's `terraform` block. The rest of the module is an ordinary Pulumi HCL program — see the [Pulumi HCL reference](/docs/iac/languages-sdks/hcl/hcl-language-reference/) for the full program model.

## Example

`PulumiPlugin.yaml`:

```yaml
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
      version = ">= 6.0"
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

The module's [`variable`](/docs/iac/languages-sdks/hcl/hcl-language-reference/#variables) blocks become the component's inputs and its [`output`](/docs/iac/languages-sdks/hcl/hcl-language-reference/#outputs) blocks become the component's outputs.

## Component definition

### `component` block

Declares the HCL module as a component resource.

| Field    | Type   | Required | Default   | Description |
| - | - | - | - | - |
| `name`   | string | Yes      | —         | Component name. Must be a valid Pulumi name (alphanumeric, hyphens, underscores; must start with a letter or underscore). |
| `module` | string | No       | `"index"` | Module segment of the component's resource token. Must be a valid Pulumi name. |

### `package` block

Declares the package identity for the component.

| Field     | Type   | Required | Default                         | Description |
| - | - | - | - | - |
| `name`    | string | No       | Directory name of the module    | Package name. Must be a valid Pulumi name when specified. |
| `version` | string | No       | `"0.0.0-dev"`                   | Package version. Must be a valid [semver](https://semver.org/) string when specified. |

Only one `component` block and one `package` block are allowed per `terraform` block. Using `component` or `package` in a regular Pulumi program (one invoked directly via `pulumi up`) produces an error.

## Resource token

The component's Pulumi resource token is formed as:

```
{package.name}:{component.module}:{component.name}
```

For the example above the token is `my-networking:index:VpcNetwork`.

## PulumiPlugin.yaml

The `PulumiPlugin.yaml` file tells the Pulumi engine how to run the component provider. For HCL MLCs it should specify the `hcl` runtime:

```yaml
runtime: hcl
```

The `component` and `package` blocks in the HCL source supply the provider name and version, so they do not need to be hardcoded elsewhere.
