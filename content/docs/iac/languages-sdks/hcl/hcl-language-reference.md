---
title_tag: "Pulumi HCL Reference | Languages & SDKs"
meta_desc: Specification for the Pulumi HCL format, blocks, expressions, built-in functions, and Terraform compatibility.
title: Reference
h1: Pulumi HCL reference
menu:
    iac:
        identifier: hcl-language-reference
        name: Reference
        parent: iac-languages-hcl
        weight: 1
    languages:
        identifier: hcl-language-reference
        parent: hcl-language
        weight: 1
aliases:
- /docs/reference/hcl/
- /docs/languages-sdks/hcl/hcl-language-reference/
---

Pulumi programs can be defined in many languages, and the Pulumi HCL dialect offers an additional language for authoring Pulumi programs using [Terraform](https://developer.hashicorp.com/terraform)'s HCL syntax. You get familiar HCL blocks, expressions, and functions while using Pulumi's state management, secrets, and deployment engine.

A Pulumi HCL program consists of one or more `.tf` files in a directory whose `Pulumi.yaml` specifies `runtime: hcl`:

```yaml
name: my-project
runtime: hcl
```

HCL files declare infrastructure using the top-level blocks listed below. The full set of HCL [expressions](#expressions) and Terraform [built-in functions](#built-in-functions) is supported, along with Pulumi-specific asset and archive functions. See [Terraform compatibility](#terraform-compatibility) for the small number of differences.

## Top-level blocks

| Block       | Purpose                                        |
|-------------|------------------------------------------------|
| `variable`  | Declare input variables                        |
| `resource`  | Manage cloud resources                         |
| `data`      | Read external data via provider invocations    |
| `provider`  | Configure provider instances                   |
| `output`    | Export values from the stack                   |
| `locals`    | Define reusable intermediate values            |
| `module`    | Invoke local or remote modules as components   |
| `call`      | Invoke methods on resources                    |
| `moved`     | Rename resources without recreation            |
| `removed`   | Destroy resources dropped from the program     |
| `import`    | Import existing cloud resources                |
| `check`     | Non-blocking assertions about infrastructure   |
| `terraform` | Version constraints and component declarations |

In many locations within these blocks, values are HCL expressions that reference variables, locals, resources, data sources, or modules. See [Expressions](#expressions) for the supported forms.

## Variables

`variable` blocks declare input values for the program. Each block has one label, the variable name, which is referenced in expressions as `var.<name>`.

```hcl
variable "region" {
  type        = string
  default     = "us-west-2"
  description = "AWS region to deploy into"
}

variable "instance_count" {
  type    = number
  default = 1
}

variable "name" {
  type = string

  validation {
    condition     = length(var.name) > 0
    error_message = "Name must not be empty."
  }
}
```

| Attribute     | Type            | Required | Description |
| - | - | - | - |
| `type`        | type expression | No       | Type constraint (for example, `string`, `number`, `bool`, `list(string)`, `map(number)`, `object({...})`). |
| `default`     | expression      | No       | Default value when the variable is not configured. |
| `description` | string          | No       | Human-readable description. |
| `sensitive`   | bool            | No       | When `true`, the value becomes a [Pulumi secret](/docs/iac/concepts/secrets/). |
| `ephemeral`   | bool            | No       | Ephemeral value; see [Ephemeral values](#ephemeral-values). |
| `nullable`    | bool            | No       | When `false`, rejects null values. Defaults to `true`. |
| `validation`  | block           | No       | One or more validation rules (see below). |

Each `validation` block has the following attributes:

| Attribute       | Type       | Required | Description |
| - | - | - | - |
| `condition`     | expression | Yes      | Expression that must evaluate to `true`. |
| `error_message` | expression | Yes      | Error message shown when the condition is `false`. |

A variable declared without a `default` is required.

### Setting variable values

Variables are set from the following sources, in priority order:

1. **Stack config**: `pulumi config set <project>:<varName> <value>` (highest priority), which takes the place of Terraform's `-var`.
1. **Variable-value files** in the program directory, applied in this order, with later files winning: `terraform.tfvars`, `terraform.tfvars.json`, then every `*.auto.tfvars` and `*.auto.tfvars.json` in lexical order by file name.
1. **Environment variables**: `TF_VAR_<name>=<value>`. A variable set to the empty string is set, and still outranks the default.
1. **Default values** in `variable` blocks (lowest priority).

A variable-value file assigns values to variable names, and its values are literals — they may not refer to anything else in the program:

```hcl
# terraform.tfvars
instance_type = "t3.micro"
tags          = { Name = "web-server" }
```

Only the root module loads these files. A file shipped inside a module is never read, and a value for a name the root module does not declare reaches nothing and is reported as a warning.

Reference variables in expressions as `var.<name>`:

```hcl
resource "aws_instance" "web" {
  instance_type = var.instance_type
}
```

## Resources

`resource` blocks declare managed infrastructure. The first label is the resource type (Terraform-style, for example `aws_instance`); the second label is the logical name; the body contains the resource's input properties.

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

### Meta-arguments

| Argument     | Type       | Description |
| - | - | - |
| `count`      | number     | Create multiple instances indexed by `count.index`. |
| `for_each`   | map or set | Create instances keyed by `each.key` with `each.value`. |
| `depends_on` | list       | Explicit dependencies on other resources. |
| `provider`   | reference  | Specific provider configuration to use. |
| `providers`  | list       | Explicit provider configurations (modules and components only). |

### Lifecycle block

```hcl
resource "aws_instance" "web" {
  # ...

  lifecycle {
    create_before_destroy = true
    prevent_destroy       = true
    ignore_changes        = [tags]
    replace_triggered_by  = [aws_instance.other]
  }
}
```

| Attribute               | Type | Description |
| - | - | - |
| `create_before_destroy` | bool | When `true`, creates the replacement before destroying the old resource. |
| `prevent_destroy`       | bool | Refuse plans that would destroy this resource. |
| `ignore_changes`        | list | Property paths to exclude from diff detection. |
| `replace_triggered_by`  | list | Replace this resource when any referenced resource or attribute changes. |

### Timeouts block

```hcl
resource "aws_instance" "web" {
  # ...

  timeouts {
    create = "60m"
    update = "30m"
    delete = "2h"
  }
}
```

| Attribute | Type   | Description |
| - | - | - |
| `create`  | string | Timeout for create operations. |
| `read`    | string | Timeout for read operations. |
| `update`  | string | Timeout for update operations. |
| `delete`  | string | Timeout for delete operations. |

### Preconditions and postconditions

Preconditions and postconditions are nested inside the `lifecycle` block:

```hcl
resource "aws_instance" "web" {
  # ...

  lifecycle {
    precondition {
      condition     = var.instance_type != ""
      error_message = "Instance type must be specified."
    }

    postcondition {
      condition     = self.public_ip != ""
      error_message = "Instance must have a public IP."
    }
  }
}
```

### Provisioners

Provisioners run commands during a resource's lifecycle. They map to the [Pulumi Command provider](/registry/packages/command/).

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"

  provisioner "local-exec" {
    command = "echo ${self.public_ip} >> hosts.txt"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get update",
      "sudo apt-get install -y nginx",
    ]
  }

  provisioner "file" {
    source      = "config.txt"
    destination = "/tmp/config.txt"
  }

  connection {
    type        = "ssh"
    user        = "ubuntu"
    private_key = file("~/.ssh/id_rsa")
    host        = self.public_ip
  }
}
```

| Provisioner type | Pulumi equivalent             |
| - | - |
| `local-exec`     | `command:local:Command`       |
| `remote-exec`    | `command:remote:Command`      |
| `file`           | `command:remote:CopyToRemote` |

Provisioner blocks accept the following options:

| Attribute    | Values                  | Description |
| - | - | - |
| `when`       | `"create"`, `"destroy"` | When the provisioner runs. |
| `on_failure` | `"continue"`, `"fail"`  | Behavior on failure. |

`connection` blocks support SSH only; WinRM is not supported. The `self` reference inside a provisioner refers to the current resource.

### Dynamic blocks

Dynamic blocks generate repeated nested blocks from a collection:

```hcl
resource "aws_security_group" "web" {
  name = "web-sg"

  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.from_port
      to_port     = ingress.value.to_port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
}
```

The label on the `dynamic` block becomes the iterator variable name. Inside the `content` block, `<label>.value` refers to the current element and `<label>.key` refers to its key or index.

### Referencing resources

Resources are referenced by `<type>.<name>`:

```hcl
output "instance_id" {
  value = aws_instance.web.id
}
```

When using `count`, instances are indexed: `aws_instance.web[0].id`, or `aws_instance.web[*].id` for the splat form. When using `for_each`, instances are keyed: `aws_instance.web["key"].id`.

## Resource options

Pulumi-specific [resource options](/docs/iac/concepts/resources/options/) live in a nested `pulumi` block. Keeping them in a nested block ensures they never collide with a resource's own provider-specific attributes, which may themselves be named, for example, `version` or `parent`.

```hcl
resource "aws_instance" "web" {
  # ...

  pulumi {
    name                      = "web-primary"
    parent                    = module.my_component
    additional_secret_outputs = ["password"]
    protect                   = true
    retain_on_delete          = true
    deleted_with              = aws_vpc.main
    replace_on_changes        = ["ami"]
    replace_with              = [aws_instance.replacement]
    hide_diffs                = ["user_data"]
    import_id                 = "i-1234567890abcdef0"
    aliases                   = ["old-name"]
    version                   = "6.0.0"
    plugin_download_url       = "https://example.com/plugins"
  }
}
```

The `pulumi` block accepts exactly the following attributes:

| Attribute                   | Type         | Description |
| - | - | - |
| `name`                      | string       | Override the Pulumi logical name. |
| [`parent`](/docs/iac/concepts/resources/options/parent/) | reference | Parent resource for component hierarchy. |
| [`additional_secret_outputs`](/docs/iac/concepts/resources/options/additionalsecretoutputs/) | list(string) | Output properties to encrypt in state. |
| [`protect`](/docs/iac/concepts/resources/options/protect/) | bool | Mark the resource protected in state; deleting it requires unprotecting first. |
| [`retain_on_delete`](/docs/iac/concepts/resources/options/retainondelete/) | bool | Keep the cloud resource when removed from the program. |
| [`deleted_with`](/docs/iac/concepts/resources/options/deletedwith/) | reference | Cascade deletion when the referenced resource is deleted. |
| [`replace_with`](/docs/iac/concepts/resources/options/replacewith/) | list | Resources whose replacement triggers replacement of this one. |
| [`hide_diffs`](/docs/iac/concepts/resources/options/hidediffs/) | list(string) | Property paths whose diffs should not be displayed. |
| [`replace_on_changes`](/docs/iac/concepts/resources/options/replaceonchanges/) | list(string) | Property paths that force replacement when changed. |
| [`import_id`](/docs/iac/concepts/resources/options/import/) | string | Cloud resource ID to import. |
| [`aliases`](/docs/iac/concepts/resources/options/aliases/) | list | Alternative names for this resource (used during renames). |
| [`env_var_mappings`](/docs/iac/concepts/resources/options/envvarmappings/) | expression | Environment variable remappings for the provider. |
| [`version`](/docs/iac/concepts/resources/options/version/) | string | Provider plugin version. |
| `plugin_download_url`       | string       | URL to download the provider plugin from. |

Terraform's `lifecycle` arguments cover the remaining Pulumi options: `create_before_destroy` lowers onto [`deleteBeforeReplace`](/docs/iac/concepts/resources/options/deletebeforereplace/) (inverted), `ignore_changes` onto [`ignoreChanges`](/docs/iac/concepts/resources/options/ignorechanges/), `replace_triggered_by` onto [`replacementTrigger`](/docs/iac/concepts/resources/options/replacementtrigger/), and `timeouts` onto [`customTimeouts`](/docs/iac/concepts/resources/options/customtimeouts/). `prevent_destroy` is enforced natively rather than mapped to an option; see [Feature mappings](#feature-mappings).

Data sources accept a narrower `pulumi` block — only the options the invoke path honors: `parent`, `version`, and `plugin_download_url`. Module blocks accept `name` and `protect`; see [Modules](#modules).

## Data sources

`data` blocks read information from providers via invocations. They use the same type-naming convention as resources, and results are referenced as `data.<type>.<name>.<attribute>`.

```hcl
data "aws_ami" "ubuntu" {
  most_recent = true
  owners      = ["099720109477"]

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*-amd64-server-*"]
  }
}

output "ami_id" {
  value = data.aws_ami.ubuntu.id
}
```

Data sources support the same meta-arguments as resources: `count`, `for_each`, `depends_on`, and `provider`.

## Providers

Providers supply the implementation for resources and data sources.

### Required providers

Providers resolve the same way as OpenTofu. By default they are looked up in the [OpenTofu registry](https://opentofu.org/registry/), so an unqualified `aws` resolves to `registry.opentofu.org/hashicorp/aws` and is bridged into Pulumi automatically. Declaring `required_providers` is only necessary to pin a source or a version. Requirements go inside the `terraform` block:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 6.0"
    }
    random = {
      source  = "pulumi/random"
      version = "4.16.0"
    }
  }
}
```

A version-only shorthand is also supported. Assigning a string instead of an object sets the version constraint and assumes the `source` is the same as the name:

```hcl
terraform {
  required_providers {
    mycloud = "~> 1.0"
  }
}
```

Sources prefixed with `pulumi/` consume a native Pulumi provider; any other source is bridged from its Terraform provider using [`pulumi-terraform-provider`](/registry/packages/terraform-provider/). Pulumi providers require an exact semver version rather than a version constraint. After changing the set of providers, run `pulumi install`.

### Provider configuration

Configure providers with `provider` blocks:

```hcl
provider "aws" {
  region = "us-west-2"
}
```

Pulumi-specific provider options go in a nested `pulumi` block so they cannot collide with the provider's own configuration attributes:

```hcl
provider "aws" {
  region = "us-west-2"

  pulumi {
    version             = "6.0.0"
    plugin_download_url = "https://example.com/plugins"
    env_var_mappings    = { AWS_REGION = "region" }
  }
}
```

| Option                      | Description |
| - | - |
| `version`                   | Provider plugin version. |
| `plugin_download_url`       | URL to download the provider plugin from. |
| `env_var_mappings`          | Environment variable remappings for the provider. |
| `additional_secret_outputs` | Provider output properties to encrypt in state. |

### Multiple provider configurations

Use `alias` to create multiple configurations of the same provider, then select one on a resource with the `provider` meta-argument or on a module with `providers`:

```hcl
provider "aws" {
  region = "us-west-2"
}

provider "aws" {
  alias  = "east"
  region = "us-east-1"
}

resource "aws_instance" "web" {
  provider = aws.east
  # ...
}
```

A `provider` block also accepts `for_each`, which declares one configuration per element of a collection.

## Outputs

`output` blocks export values from the stack for access via [`pulumi stack output`](/docs/iac/cli/commands/pulumi_stack_output/).

```hcl
output "instance_ip" {
  value       = aws_instance.web.public_ip
  description = "Public IP of the web server"
}

output "db_password" {
  value     = random_password.db.result
  sensitive = true
}

output "vpc_id" {
  value      = aws_vpc.main.id
  depends_on = [aws_internet_gateway.gw]

  precondition {
    condition     = aws_vpc.main.id != ""
    error_message = "VPC must have an ID."
  }
}
```

| Attribute      | Type       | Required | Description |
| - | - | - | - |
| `value`        | expression | Yes      | The value to export. |
| `description`  | string     | No       | Human-readable description. |
| `sensitive`    | bool       | No       | When `true`, the output becomes a [Pulumi secret](/docs/iac/concepts/secrets/). |
| `ephemeral`    | bool       | No       | Ephemeral value; see [Ephemeral values](#ephemeral-values). |
| `depends_on`   | list       | No       | Explicit dependencies. |
| `precondition` | block      | No       | Validation checks before export. |

## Locals

`locals` blocks define reusable intermediate values. Multiple `locals` blocks are allowed in a program; reference locals as `local.<name>`.

```hcl
locals {
  common_tags = {
    Environment = "dev"
    Project     = "my-project"
  }

  name_prefix = "myapp-${var.environment}"

  user_data = <<-EOF
    #!/bin/bash
    echo "Hello, World!" > index.html
    nohup python3 -m http.server 80 &
  EOF
}

resource "aws_instance" "web" {
  tags      = local.common_tags
  user_data = local.user_data
}
```

## Modules

`module` blocks invoke reusable configurations as Pulumi component resources. Module outputs are referenced as `module.<name>.<output_name>`.

```hcl
module "vpc" {
  source     = "./modules/vpc"
  cidr_block = "10.0.0.0/16"
}

output "vpc_id" {
  value = module.vpc.vpc_id
}
```

### Module sources

| Source type           | Example |
| - | - |
| Local path            | `./modules/vpc` |
| Git                   | `git::https://github.com/org/repo.git?ref=v1.0.0` |
| Git with subdirectory | `git::https://github.com/org/repo.git//modules/vpc?ref=v1.0.0` |
| GitHub shorthand      | `github.com/org/repo` |
| Bitbucket shorthand   | `bitbucket.org/org/repo` |
| Terraform Registry    | `terraform-aws-modules/vpc/aws` |
| HTTP archive          | `https://example.com/module.zip` |

Remote modules are cached in `~/.pulumi/modules/`.

### Module meta-arguments

| Argument     | Type       | Description |
| - | - | - |
| `source`     | string     | Module source (required). |
| `version`    | string     | Version constraint (for registry modules). |
| `count`      | number     | Create multiple module instances. |
| `for_each`   | map or set | Create keyed module instances. |
| `depends_on` | list       | Explicit dependencies. |
| `providers`  | map        | Provider configuration mappings for the module. |

Like resources, a module block accepts a nested `pulumi` block. Its `name` attribute overrides the Pulumi logical name of each module instance, evaluated per instance with `count.index` or `each.key` in scope. The overridden name also prefixes the derived names of everything inside the instance, and is visible to the module source as `pulumi.module.name`. Its `protect` attribute marks each instance's component resource protected in state.

```hcl
module "vpc" {
  source = "./modules/vpc"

  pulumi {
    name = "vpc-primary"
  }
}
```

## Call blocks

`call` blocks invoke methods on existing resources. This is a Pulumi-specific extension with no Terraform equivalent, used to call [resource methods](/docs/iac/concepts/functions/resource-methods/).

```hcl
resource "call_custom" "my_resource" {
  value = "hello"
}

call "my_resource" "provider_value" {
}

output "result" {
  value = call.my_resource.provider_value.result
}
```

The first label is the logical name of a declared resource. The second label is the method name. The body contains arguments to the method. Results are referenced as `call.<resource_name>.<method_name>.<attribute>`.

## Moved, removed, and import blocks

### Moved blocks

`moved` blocks rename resources without recreating them. They map to Pulumi's `aliases` resource option.

```hcl
moved {
  from = aws_instance.old_name
  to   = aws_instance.new_name
}
```

| Attribute | Type      | Required | Description |
| - | - | - | - |
| `from`    | reference | Yes      | Original resource address. |
| `to`      | reference | Yes      | New resource address. |

### Removed blocks

`removed` blocks declare that the resource or module at `from` has been deleted from the configuration and its remote objects should be destroyed. The address carries no instance keys — a `removed` block applies to every instance.

```hcl
removed {
  from = aws_instance.example

  lifecycle {
    destroy = true
  }
}
```

| Attribute      | Type      | Required | Description |
| - | - | - | - |
| `from`         | reference | Yes      | Address of the removed resource or module. |
| `lifecycle`    | block     | Yes      | Must set `destroy = true`. |
| `provisioner`  | block     | No       | Destroy-time provisioners to run as the orphaned instances are deleted. Only `when = "destroy"` provisioners are allowed. |

Only `destroy = true` is supported. A resource absent from the program is destroyed by the Pulumi engine on its own, while `destroy = false` — Terraform's "forget" behavior — has no engine mapping and is reported as an error.

### Import blocks

`import` blocks import existing cloud resources into Pulumi state.

```hcl
import {
  to       = aws_instance.web
  id       = "i-1234567890abcdef0"
  provider = aws.east
}
```

| Attribute  | Type      | Required | Description |
| - | - | - | - |
| `to`       | reference | Yes      | Target resource address. |
| `id`       | string    | Yes      | Cloud resource ID to import. |
| `provider` | reference | No       | Provider configuration to use. |
| `for_each` | map or set | No      | Import one resource per element of a collection. |

To bring in a whole existing deployment at once, use [`pulumi import --from hcl`](#state-migration) with a Terraform or OpenTofu state file instead.

## Check blocks

`check` blocks make non-blocking assertions about your infrastructure. Unlike a resource precondition or postcondition, a failed `assert` reports a warning and the operation continues rather than aborting.

```hcl
check "health" {
  data "http" "status" {
    url = "https://example.com"
  }

  assert {
    condition     = data.http.status.status_code == 200
    error_message = "${data.http.status.url} returned an unhealthy status."
  }
}
```

Each check block has a name (its label) and one or more `assert` blocks:

| Attribute       | Type       | Required | Description |
| - | - | - | - |
| `condition`     | expression | Yes      | Expression that must evaluate to `true`. |
| `error_message` | expression | Yes      | Warning shown when the condition is `false`. |

A check may also declare a single nested `data` source — a *scoped data source* — read fresh on every operation and visible only to that check's assertions.

## Override files

A file named `override.tf`, or any file whose name ends in `_override.tf`, is an override file. Its blocks amend blocks of the same address declared in the directory's other files instead of declaring new ones.

```hcl
# main.tf
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"
}
```

```hcl
# dev_override.tf
resource "aws_instance" "web" {
  instance_type = "t3.large"
}
```

`locals` and `terraform` blocks — neither of which is addressable by a label — merge after the primary blocks are parsed. `moved`, `import`, and `removed` blocks may appear only in normal files; overriding them is an error.

## Escaping meta-arguments

The special block type `_` forces arguments to be interpreted as ordinary configuration rather than as meta-arguments. Use it when a provider defines an attribute whose name collides with a meta-argument such as `count`, `for_each`, `provider`, or `depends_on`. Each `resource`, `data`, `module`, `provider`, and `provisioner` block may contain at most one escaping block.

```hcl
resource "example_thing" "a" {
  _ {
    count = 3 # the provider's own "count" attribute, not the meta-argument
  }
}
```

## Expressions

Pulumi HCL supports the full HCL expression language.

### Literals

```hcl
"hello"           # string
42                # number
3.14              # number
true              # bool
null              # null
["a", "b", "c"]   # list
{key = "value"}   # map
```

### String interpolation

```hcl
"Hello, ${var.name}!"
"prefix-${local.env}-suffix"
```

### Heredocs

```hcl
<<-EOF
  multi-line
  string content
EOF
```

### References

| Reference                | Description |
| - | - |
| `var.<name>`             | Input variable. |
| `local.<name>`           | Local value. |
| `<type>.<name>`          | Resource attribute. |
| `<type>.<name>[<index>]` | Counted resource instance. |
| `<type>.<name>["<key>"]` | For-each resource instance. |
| `data.<type>.<name>`     | Data source attribute. |
| `module.<name>`          | Module output. |
| `call.<res>.<method>`    | Call block result. |
| `self`                   | Current resource (in provisioners). |
| `count.index`            | Current count iteration index. |
| `each.key`               | Current `for_each` key. |
| `each.value`             | Current `for_each` value. |
| `path.module`            | Path to the current module. |
| `path.root`              | Path to the root module. |
| `path.cwd`               | Current working directory. |
| `pulumi.stack`           | Current stack name. |
| `pulumi.project`         | Current project name. |
| `pulumi.organization`    | Current organization name. |
| `pulumi.module.name`     | Pulumi logical name of the enclosing module instance (null at the root). |

### Operators

| Category   | Operators |
| - | - |
| Arithmetic | `+`, `-`, `*`, `/`, `%` |
| Comparison | `==`, `!=`, `<`, `<=`, `>`, `>=` |
| Logical    | `&&`, `\|\|`, `!` |

### Conditional expression

```hcl
condition ? true_value : false_value
```

### For expressions

```hcl
# List comprehension
[for name in var.names : upper(name)]

# With index
[for i, name in var.names : "${i}-${name}"]

# Map comprehension
{for k, v in var.tags : k => upper(v)}

# With filter
[for name in var.names : name if name != ""]
```

### Splat expressions

```hcl
# Equivalent to [for r in aws_instance.web : r.id]
aws_instance.web[*].id
```

### Property access

```hcl
resource.name.property
resource.name["key"]
resource.name[0]
```

### `try` and `can`

```hcl
try(var.optional.nested.value, "default")
can(var.optional.nested.value)  # returns true or false
```

## Built-in functions

Pulumi HCL supports nearly all Terraform built-in functions, grouped by category below.

| Category | Functions |
| - | - |
| Numeric         | `abs`, `ceil`, `floor`, `log`, `max`, `min`, `pow`, `signum`, `parseint` |
| String          | `chomp`, `endswith`, `format`, `formatlist`, `indent`, `join`, `lower`, `regex`, `regexall`, `replace`, `split`, `startswith`, `strcontains`, `strrev`, `substr`, `title`, `trim`, `trimprefix`, `trimsuffix`, `trimspace`, `upper` |
| Collection      | `alltrue`, `anytrue`, `chunklist`, `coalesce`, `coalescelist`, `compact`, `concat`, `contains`, `distinct`, `element`, `entries`, `flatten`, `index`, `keys`, `length`, `list`, `lookup`, `map`, `matchkeys`, `merge`, `one`, `range`, `reverse`, `setintersection`, `setproduct`, `setsubtract`, `setunion`, `slice`, `sort`, `sum`, `transpose`, `values`, `zipmap` |
| Encoding        | `base64decode`, `base64encode`, `base64gzip`, `base64gunzip`, `csvdecode`, `jsondecode`, `jsonencode`, `textdecodebase64`, `textencodebase64`, `urlencode`, `urldecode`, `yamldecode`, `yamlencode` |
| Filesystem      | `abspath`, `basename`, `dirname`, `file`, `filebase64`, `fileexists`, `fileset`, `pathexpand`, `templatefile`, `templatestring` |
| Date and time   | `formatdate`, `plantimestamp`, `timeadd`, `timecmp`, `timestamp` |
| Hash and crypto | `base64sha256`, `base64sha512`, `bcrypt`, `filebase64sha256`, `filebase64sha512`, `filemd5`, `filesha1`, `filesha256`, `filesha512`, `md5`, `rsadecrypt`, `sha1`, `sha256`, `sha512`, `uuid`, `uuidv5` |
| IP network      | `cidrcontains`, `cidrhost`, `cidrnetmask`, `cidrsubnet`, `cidrsubnets` |
| Type conversion | `can`, `ephemeralasnull`, `issensitive`, `nonsensitive`, `recover`, `sensitive`, `tobool`, `tolist`, `tomap`, `tonumber`, `toset`, `tostring`, `try`, `type` |

Pulumi has no plan/apply split, so `plantimestamp` resolves to the current time exactly as `timestamp` does.

The `provider::terraform::` namespace provides `decode_tfvars`, `encode_expr`, and `encode_tfvars`.

### Pulumi-specific functions

These functions have no Terraform equivalent. The asset and archive functions create the intrinsic Pulumi types described in [Assets and archives](/docs/iac/concepts/assets-archives/), which some resources take as inputs or return as outputs:

| Function                       | Description |
| - | - |
| `fileasset(path)`              | Create a Pulumi `FileAsset` from a local file path. |
| `stringasset(text)`            | Create a Pulumi `StringAsset` from a string value. |
| `remoteasset(uri)`             | Create a Pulumi `RemoteAsset` from a URL. |
| `filearchive(path)`            | Create a Pulumi `FileArchive` from a local path. |
| `remotearchive(uri)`           | Create a Pulumi `RemoteArchive` from a URL. |
| `assetarchive(map)`            | Create a Pulumi `AssetArchive` from a map of assets or archives. |
| `pulumiresourcename(resource)` | Get the logical name from a resource's URN. |
| `pulumiresourcetype(resource)` | Get the type token from a resource's URN. |
| `pulumiresourceurn(resource)`  | Get a resource's URN. |
| `entries(map)`                 | Convert a map or object to a list of `{key, value}` objects. |
| `recover(value, recovery)`     | Return `value`, or evaluate `recovery` if `value` fails to evaluate. |

### Functions not supported

`terraform.applying` is Terraform-internal — Pulumi has no plan/apply split for it to report on — and has no equivalent.

## Stack references

Access outputs from other Pulumi stacks using the `pulumi_stack_reference` resource:

```hcl
resource "pulumi_stack_reference" "network" {
  name = "myorg/networking/prod"
}

output "vpc_id" {
  value = pulumi_stack_reference.network.outputs["vpc_id"]
}
```

## Terraform built-in resources

Terraform's two built-in types are supported:

- **`terraform_data`** — a managed resource with no cloud counterpart, used to store values and to attach provisioners or `triggers_replace` to. It lowers onto the Pulumi engine's built-in stash resource.
- **`terraform_remote_state`** — a data source that reads another Terraform or OpenTofu state file, served by the external [`terraform`](/registry/packages/terraform/) provider.

## Terraform block

The top-level `terraform` block holds [required providers](#required-providers) and version constraints, exactly as it does in Terraform and OpenTofu. In Pulumi HCL it additionally holds [component declarations](#multi-language-components), a Pulumi-specific extension.

### Version constraints

Pulumi HCL uses `required_version_range` to declare a supported Pulumi version range. Terraform's `required_version` is accepted but ignored with a warning.

```hcl
terraform {
  required_version_range = ">= 3.0.0"
}
```

### Multi-language components

The `component` block, optionally with a `package` block, declares an HCL module as a reusable Pulumi component consumable from any Pulumi language. See the [Pulumi HCL component reference](/docs/iac/languages-sdks/hcl/hcl-component-reference/) for details.

```hcl
terraform {
  component {
    name   = "VpcNetwork"
    module = "index"
  }
  package {
    name    = "my-networking"
    version = "1.0.0"
  }
}
```

## Terraform compatibility

Pulumi HCL aims to run valid Terraform configurations without changes — the same `.tf` files, the same `terraform` block, and the same provider sources. This section covers the behavioral differences and the few unsupported features. If you find a case where `tofu` works and `pulumi` does not, please [open an issue](https://github.com/pulumi/pulumi-hcl/issues/new).

### Behavioral differences

**Sensitive values.** Variables and outputs marked `sensitive = true` become [Pulumi secrets](/docs/iac/concepts/secrets/), encrypted at rest in state.

**Property names.** HCL uses `snake_case`. The plugin automatically converts to Pulumi's `camelCase` for the engine. Map keys are not translated.

**Ephemeral values.** See [Ephemeral values](#ephemeral-values) below.

### Ephemeral values

Terraform's ephemeral values exist to keep a value out of state and plan files entirely. Pulumi's state model already encrypts secrets at rest, so Pulumi HCL interprets `ephemeral = true` through that lens instead of reproducing Terraform's persistence rules:

- **Persisted as secrets.** A value from an ephemeral variable or output is stored in state, but encrypted, exactly like `sensitive = true`. It is masked in CLI output and in the Pulumi Console.
- **Diffs are hidden.** An ephemeral value is free to differ on every run, so the resource property it flows into is registered with its diff hidden (the [`hideDiffs`](/docs/iac/concepts/resources/options/hidediffs/) resource option), down to the exact property path — an ephemeral value inside one block of a repeated block hides only that block's attribute.
- **Not sensitive.** Ephemerality and sensitivity are tracked separately: `issensitive` returns `false` for a purely ephemeral value, matching Terraform.
- **`ephemeralasnull` is supported** and behaves as in Terraform: it replaces the ephemeral parts of a value with typed nulls, preserving sensitivity marks, making the result usable anywhere.

Differences from Terraform to be aware of:

- Terraform rejects an ephemeral value used in a non-ephemeral context, such as a regular resource argument or a non-ephemeral output. Pulumi HCL accepts it and persists the value encrypted; there is no flow validation.
- Terraform re-prompts for a required ephemeral variable on every run. Pulumi HCL reads it from stack configuration like any other variable, so set it once with `pulumi config set --secret`.
- A root-level ephemeral output becomes a secret stack output rather than being omitted.

### Feature mappings

| Terraform feature       | Pulumi equivalent      | Notes |
| - | - | - |
| `prevent_destroy`       | (native)               | Enforced by Pulumi HCL itself, re-evaluated each run; the guard lifts when the argument is removed from the program. |
| `ignore_changes`        | `ignoreChanges`        | Same behavior. |
| `create_before_destroy` | `deleteBeforeReplace`  | Inverted; defaults to Terraform's delete-first order. |
| `replace_triggered_by`  | `replacementTrigger`   | Replaces when a referenced value changes. |
| `moved` blocks          | `aliases`              | Renames without recreation. |
| `import` blocks         | Import resource option | Imports existing resources. |
| `timeouts`              | `customTimeouts`       | Same duration format. |
| Modules                 | Component resources    | All source types supported. |
| Provisioners            | Command provider       | `local-exec`, `remote-exec`, `file`. |

`prevent_destroy` is separate from Pulumi's [`protect`](/docs/iac/concepts/resources/options/protect/) option, which is set explicitly in the `pulumi` block and recorded in state.

### State migration

Pulumi cannot read a Terraform state file as its own, but you do not have to import resources one at a time. Point the converter at an existing Terraform or OpenTofu state file to import everything it describes in bulk:

```bash
pulumi import --from hcl terraform.tfstate
```

This reads the state file, maps each Terraform resource type to its Pulumi token, and imports the resources into your stack.

### Unsupported features

- **`backend`, `required_version`, `provider_meta`, and `experiments`** — accepted inside the `terraform` block but ignored with a warning. Pulumi manages state independently and tracks its own version constraints via `required_version_range`, and language experiments have no Pulumi HCL equivalent.
- **`cloud`** — not accepted inside the `terraform` block at all. It is absent from the block's schema, so a `cloud` block is a parse error rather than a warning. Remove it; Pulumi's own backend configuration lives outside the program.
- **WinRM connections** — `connection` blocks support `type = "ssh"` only.
- **`List<Object>` empty versus null** — HCL block syntax cannot distinguish an empty `List<Object>` from a null one, a known incompatibility with some Pulumi programs.
- **Resource-wide destroy ordering of late-created instances** — Terraform rebuilds destroy-time dependencies from configuration, so every instance of a `count` or `for_each` resource waits for a consumer's delete even when the consumer referenced only one instance (`depends_on = [a["x"]]`). Pulumi records each resource's dependencies once, when it is created, and cannot depend on an instance that registers later. A sibling instance created *after* the consumer is therefore not held back by it during destroy and may be deleted first.
- **`ignore_changes` on `terraform_data`'s `triggers_replace`** — honored only when it is present from the resource's creation. Adding `ignore_changes = [triggers_replace]` in the same update that changes `triggers_replace`, on a resource first created without it, still forces one replacement: `triggers_replace` is carried as a replacement trigger rather than a stored input, so it cannot be reconciled against the prior state the way an ignored input is.

### CLI equivalents

| Terraform           | Pulumi           |
|---------------------|------------------|
| `terraform plan`    | `pulumi preview` |
| `terraform apply`   | `pulumi up`      |
| `terraform destroy` | `pulumi destroy` |
| `terraform state`   | `pulumi state`   |
| `terraform import`  | `pulumi import`  |
| Workspaces          | Stacks           |
