---
title_tag: "Pulumi HCL Reference | Languages & SDKs"
meta_desc: Specification for the Pulumi HCL format, blocks, expressions, and built-in functions.
title: Reference
h1: Pulumi HCL reference
meta_image: /images/docs/meta-images/docs-meta.png
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

Pulumi programs can be defined in many languages, and the Pulumi HCL dialect offers an additional language for authoring Pulumi programs using [Terraform](https://developer.hashicorp.com/terraform)-like HCL syntax.

A Pulumi HCL program consists of one or more `.hcl` files in a directory whose `Pulumi.yaml` specifies `runtime: hcl`:

```yaml
name: my-project
runtime: hcl
```

HCL files declare infrastructure using the top-level blocks listed below. The full set of HCL [expressions](#expressions) and Terraform [built-in functions](#built-in-functions) is supported, along with Pulumi-specific asset and archive functions. See [Terraform compatibility](#terraform-compatibility) for the small number of differences.

### Top-level blocks

| Block       | Purpose                                           |
| - | - |
| `variable`  | Declare input variables                           |
| `resource`  | Manage cloud resources                            |
| `data`      | Read external data via provider invocations       |
| `provider`  | Configure provider instances                      |
| `output`    | Export values from the stack                      |
| `locals`    | Define reusable intermediate values               |
| `module`    | Invoke local or remote modules as components      |
| `call`      | Invoke methods on resources                       |
| `moved`     | Rename resources without recreation               |
| `import`    | Import existing cloud resources                   |
| `pulumi`    | Required providers, version constraints, and component declarations |

In many locations within these blocks, values are HCL expressions that reference variables, locals, resources, data sources, or modules. See [Expressions](#expressions) for the supported forms.

### Variables

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

| Attribute     | Type       | Required | Description |
| - | - | - | - |
| `type`        | type expression | No  | Type constraint (for example, `string`, `number`, `bool`, `list(string)`, `map(number)`, `object({...})`). |
| `default`     | expression | No  | Default value when the variable is not configured. |
| `description` | string     | No  | Human-readable description. |
| `sensitive`   | bool       | No  | When `true`, the value becomes a [Pulumi secret](/docs/iac/concepts/secrets/). |
| `nullable`    | bool       | No  | When `false`, rejects null values. Defaults to `true`. |
| `validation`  | block      | No  | One or more validation rules (see below). |

Each `validation` block has the following attributes:

| Attribute       | Type       | Required | Description |
| - | - | - | - |
| `condition`     | expression | Yes      | Expression that must evaluate to `true`. |
| `error_message` | expression | Yes      | Error message shown when the condition is `false`. |

Variables are set through Pulumi's config system, in priority order:

1. Environment variables: `TF_VAR_<name>=<value>` (highest priority).
1. Stack config: `pulumi config set <project>:<varName> <value>`.
1. Default values in `variable` blocks (lowest priority).

### Resources

`resource` blocks declare managed infrastructure. The first label is the resource type (Terraform-like, for example `aws_instance`); the second label is the logical name; the body contains the resource's input properties.

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"

  tags = {
    Name = "web-server"
  }
}
```

`resource` blocks support the full set of Pulumi [resource options](/docs/iac/concepts/resources/options/) as top-level attributes (with `snake_case` names — for example `retain_on_delete`, `parent`, `aliases`). See [Resource options](#resource-options) for the HCL surface and [the canonical resource-options reference](/docs/iac/concepts/resources/options/) for full semantics. Some options are also reachable via the [`lifecycle` block](#lifecycle-block) under their Terraform-like names (for example `prevent_destroy` → `protect`, `ignore_changes`).

#### Meta-arguments

| Argument     | Type       | Description |
| - | - | - |
| `count`      | number     | Create multiple instances indexed by `count.index`. |
| `for_each`   | map or set | Create instances keyed by `each.key` with `each.value`. |
| `depends_on` | list       | Explicit dependencies on other resources. |
| `provider`   | reference  | Specific provider configuration to use. |
| `providers`  | list       | Explicit provider resources (component resources only). |

#### Lifecycle block

```hcl
resource "aws_instance" "web" {
  # ...

  lifecycle {
    create_before_destroy = true
    prevent_destroy       = true
    ignore_changes        = [tags]
  }
}
```

| Attribute               | Type | Description |
| - | - | - |
| `create_before_destroy` | bool | When `false`, deletes the old resource before creating the replacement (Pulumi creates first by default). |
| `prevent_destroy`       | bool | Protect the resource from accidental deletion. Maps to Pulumi's `protect` option. |
| `ignore_changes`        | list | Property paths to exclude from diff detection. |

The `lifecycle` block also supports `precondition` and `postcondition` blocks, each of which takes a `condition` expression and an `error_message` expression:

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

#### Timeouts block

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
| `update`  | string | Timeout for update operations. |
| `delete`  | string | Timeout for delete operations. |

#### Provisioners

Provisioners run commands during resource lifecycle events. They map to the [Pulumi Command provider](/registry/packages/command/).

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

Provisioner blocks accept `when` (`"create"` or `"destroy"`) and `on_failure` (`"continue"` or `"fail"`) attributes. The `self` reference inside a provisioner refers to the parent resource. `connection` blocks support SSH only; WinRM is not supported.

#### Referencing resources

Resources are referenced by `<type>.<name>`:

```hcl
output "instance_id" {
  value = aws_instance.web.id
}
```

When using `count`, instances are indexed: `aws_instance.web[0].id`, or `aws_instance.web[*].id` for the splat form. When using `for_each`, instances are keyed: `aws_instance.web["key"].id`.

### Resource options

In addition to the Terraform-like meta-arguments above, resource blocks accept Pulumi-specific [resource options](/docs/iac/concepts/resources/options/) as top-level attributes.

```hcl
resource "aws_instance" "web" {
  # ...

  parent                     = module.my_component
  additional_secret_outputs  = ["password"]
  retain_on_delete           = true
  deleted_with               = aws_vpc.main
  replace_on_changes         = ["ami"]
  replace_with               = [aws_instance.replacement]
  hide_diffs                 = ["user_data"]
  replacement_trigger        = var.force_replace
  import_id                  = "i-1234567890abcdef0"
  aliases                    = ["old-name"]
  version                    = "6.0.0"
  plugin_download_url        = "https://example.com/plugins"
}
```

| Attribute                   | Type         | Description |
| - | - | - |
| `parent`                    | reference    | Parent resource for component hierarchy. |
| `additional_secret_outputs` | list(string) | Output properties to encrypt in state. |
| `retain_on_delete`          | bool         | Keep the cloud resource when removed from the program. |
| `deleted_with`              | reference    | Cascade deletion when the referenced resource is deleted. |
| `replace_with`              | list         | Resources whose replacement triggers replacement of this one. |
| `hide_diffs`                | list(string) | Property paths whose diffs should not be displayed. |
| `replace_on_changes`        | list(string) | Property paths that force replacement when changed. |
| `replacement_trigger`       | expression   | Expression whose change triggers replacement. |
| `import_id`                 | string       | Cloud resource ID to import. |
| `aliases`                   | list         | Alternative names for this resource (used during renames). |
| `version`                   | string       | Provider plugin version. |
| `plugin_download_url`       | string       | URL to download the provider plugin from. |

Provider resources (with type `pulumi_providers_<name>`) additionally accept an `env_var_mappings` attribute, which remaps environment variables for the provider.

### Data sources

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

### Providers

Providers supply the implementation for resources and data sources.

#### Required providers

Declare provider requirements inside the `pulumi` block:

```hcl
pulumi {
  required_providers {
    aws = {
      source  = "pulumi/aws"
      version = ">= 6.0"
    }
    random = {
      source  = "pulumi/random"
      version = "4.16.0"
    }
  }
}
```

Provider sources must use the `pulumi/` namespace, not `hashicorp/`.

#### Provider configuration

Configure providers with `provider` blocks:

```hcl
provider "aws" {
  region = "us-west-2"
}
```

#### Multiple provider configurations

Use `alias` to create multiple configurations of the same provider:

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

#### Provider resources

Providers can also be declared as `resource` blocks for use with component resources:

```hcl
resource "pulumi_providers_aws" "explicit" {
  region = "us-west-2"
}

resource "aws_instance" "web" {
  providers = [pulumi_providers_aws.explicit]
  # ...
}
```

The `pulumi_providers_<name>` resource type creates an explicit provider instance. Pass it to component resources via the `providers` meta-argument.

### Outputs

`output` blocks export values from the stack via [`pulumi stack output`](/docs/iac/cli/commands/pulumi_stack_output/).

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
| `sensitive`    | bool       | No       | When `true`, the output becomes a Pulumi secret. |
| `depends_on`   | list       | No       | Explicit dependencies. |
| `precondition` | block      | No       | Validation checks before export. |

### Locals

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

### Modules

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

#### Module sources

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

#### Module meta-arguments

| Argument     | Type       | Description |
| - | - | - |
| `source`     | string     | Module source (required). |
| `version`    | string     | Version constraint (for registry modules). |
| `count`      | number     | Create multiple module instances. |
| `for_each`   | map or set | Create keyed module instances. |
| `depends_on` | list       | Explicit dependencies. |
| `providers`  | map        | Provider configuration mappings for the module. |

### Call blocks

`call` blocks invoke methods on existing resources. This is a Pulumi-specific extension with no Terraform equivalent.

```hcl
resource "aws_instance" "web" {
  ami           = "ami-12345678"
  instance_type = "t3.micro"
}

call "web" "get_password_data" {
}

output "password_data" {
  value = call.web.get_password_data.password_data
}
```

The first label is the logical name of a declared resource. The second label is the method name. The body contains arguments to the method. Results are referenced as `call.<resource_name>.<method_name>.<attribute>`.

### Moved and import blocks

#### Moved blocks

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

#### Import blocks

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

### Expressions

Pulumi HCL supports the full HCL expression language.

#### Literals

```hcl
"hello"           # string
42                # number
3.14              # number
true              # bool
null              # null
["a", "b", "c"]   # list
{key = "value"}   # map
```

#### String interpolation

```hcl
"Hello, ${var.name}!"
"prefix-${local.env}-suffix"
```

#### Heredocs

```hcl
<<-EOF
  multi-line
  string content
EOF
```

#### References

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

#### Operators

| Category   | Operators |
| - | - |
| Arithmetic | `+`, `-`, `*`, `/`, `%` |
| Comparison | `==`, `!=`, `<`, `<=`, `>`, `>=` |
| Logical    | `&&`, `\|\|`, `!` |

#### Conditional expression

```hcl
condition ? true_value : false_value
```

#### For expressions

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

#### Splat expressions

```hcl
# Equivalent to [for r in aws_instance.web : r.id]
aws_instance.web[*].id
```

#### Property access

```hcl
resource.name.property
resource.name["key"]
resource.name[0]
```

#### `try` and `can`

```hcl
try(var.optional.nested.value, "default")
can(var.optional.nested.value)  # returns true or false
```

### Built-in functions

Pulumi HCL supports nearly all Terraform built-in functions, grouped by category below.

| Category | Functions |
| - | - |
| Numeric          | `abs`, `ceil`, `floor`, `log`, `max`, `min`, `pow`, `signum`, `parseint` |
| String           | `chomp`, `endswith`, `format`, `formatlist`, `indent`, `join`, `lower`, `regex`, `regexall`, `replace`, `split`, `startswith`, `strcontains`, `strrev`, `substr`, `title`, `trim`, `trimprefix`, `trimsuffix`, `trimspace`, `upper` |
| Collection       | `alltrue`, `anytrue`, `chunklist`, `coalesce`, `coalescelist`, `compact`, `concat`, `contains`, `distinct`, `element`, `entries`, `flatten`, `index`, `keys`, `length`, `list`, `lookup`, `map`, `matchkeys`, `merge`, `one`, `range`, `reverse`, `setintersection`, `setproduct`, `setsubtract`, `setunion`, `slice`, `sort`, `sum`, `transpose`, `values`, `zipmap` |
| Encoding         | `base64decode`, `base64encode`, `base64gzip`, `csvdecode`, `jsondecode`, `jsonencode`, `textdecodebase64`, `textencodebase64`, `urlencode`, `yamldecode`, `yamlencode` |
| Filesystem       | `abspath`, `basename`, `dirname`, `file`, `filebase64`, `fileexists`, `fileset`, `pathexpand`, `templatefile` |
| Date and time    | `formatdate`, `timeadd`, `timecmp`, `timestamp` |
| Hash and crypto  | `base64sha256`, `base64sha512`, `bcrypt`, `filebase64sha256`, `filebase64sha512`, `filemd5`, `filesha1`, `filesha256`, `filesha512`, `md5`, `rsadecrypt`, `sha1`, `sha256`, `sha512`, `uuid`, `uuidv5` |
| IP network       | `cidrhost`, `cidrnetmask`, `cidrsubnet`, `cidrsubnets` |
| Type conversion  | `can`, `issensitive`, `nonsensitive`, `sensitive`, `tobool`, `tolist`, `tomap`, `tonumber`, `toset`, `tostring`, `try`, `type` |

#### Pulumi-specific functions

| Function                       | Description |
| - | - |
| `fileAsset(path)`              | Create a Pulumi `FileAsset` from a local file path. |
| `stringAsset(text)`            | Create a Pulumi `StringAsset` from a string value. |
| `remoteAsset(uri)`             | Create a Pulumi `RemoteAsset` from a URL. |
| `fileArchive(path)`            | Create a Pulumi `FileArchive` from a local path. |
| `remoteArchive(uri)`           | Create a Pulumi `RemoteArchive` from a URL. |
| `assetArchive(map)`            | Create a Pulumi `AssetArchive` from a map of assets or archives. |
| `pulumiResourceName(resource)` | Get the logical name from a resource's URN. |
| `pulumiResourceType(resource)` | Get the type token from a resource's URN. |

#### Functions not supported

These Terraform functions have no equivalent in Pulumi HCL:

| Function          | Reason |
| - | - |
| `templatestring`  | Inline template-string rendering is not supported. |
| `plantimestamp`   | No Pulumi equivalent for plan-time timestamps. |
| `ephemeralasnull` | Pulumi has no ephemeral value concept. |

The `provider::terraform::*` provider functions and `terraform.applying` are Terraform-internal and have no equivalent.

### Stack references

Access outputs from other Pulumi stacks using the `pulumi_stackreference` resource:

```hcl
resource "pulumi_stackreference" "network" {
  name = "myorg/networking/prod"
}

output "vpc_id" {
  value = pulumi_stackreference.network.outputs["vpc_id"]
}
```

### Pulumi block

The `pulumi` block configures Pulumi-specific settings.

#### Version constraints

```hcl
pulumi {
  required_version_range = ">= 3.0.0"
}
```

#### Multi-language components

The `component` and `package` blocks declare an HCL module as a reusable Pulumi component consumable from any Pulumi language. See the [Pulumi HCL component reference](/docs/iac/languages-sdks/hcl/hcl-component-reference/) for details.

```hcl
pulumi {
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

### Terraform compatibility

Pulumi HCL is broadly compatible with Terraform-like HCL syntax. This section covers the differences.

#### Required changes

The top-level `terraform` block is not supported. Move provider requirements into the `pulumi` block, and use the `pulumi/` namespace for provider sources instead of `hashicorp/`:

```hcl
pulumi {
  required_providers {
    aws = {
      source  = "pulumi/aws"  # not "hashicorp/aws"
      version = ">= 6.0"
    }
  }
}
```

Terraform's `backend`, `cloud`, and `required_version` are not modeled — Pulumi manages state independently and uses `pulumi { required_version_range = "..." }` for its own version constraints.

#### Behavioral differences

**Resource replacement order.** Pulumi creates the new resource before deleting the old one (the opposite of Terraform). Set `create_before_destroy = false` in the `lifecycle` block to opt into delete-first behavior.

**Sensitive values.** Variables and outputs marked `sensitive = true` become [Pulumi secrets](/docs/iac/concepts/secrets/), encrypted at rest in state.

**Property names.** HCL uses `snake_case`. The plugin automatically converts to Pulumi's `camelCase` for the engine. Map keys are not translated.

#### Feature mappings

| Terraform feature       | Pulumi equivalent      | Notes |
| - | - | - |
| `prevent_destroy`       | `protect`              | Same behavior. |
| `ignore_changes`        | `ignoreChanges`        | Same behavior. |
| `create_before_destroy` | `deleteBeforeReplace`  | Inverted logic. |
| `moved` blocks          | `aliases`              | Renames without recreation. |
| `import` blocks         | Import resource option | Imports existing resources. |
| `timeouts`              | `customTimeouts`       | Same duration format. |
| Modules                 | Component resources    | All source types supported. |
| Provisioners            | Command provider       | `local-exec`, `remote-exec`, `file`. |

#### Unsupported features

- **`replace_triggered_by`** — Terraform cascades replacement when *other* resources change. Use Pulumi HCL's `replace_with` resource option for the same effect; the Terraform-like `replace_triggered_by` attribute on a `lifecycle` block produces an error.
- **`dynamic` blocks** — Dynamic block generation is not implemented.
- **WinRM connections** — `connection` blocks support `type = "ssh"` only.
