---
title_tag: "Pulumi HCL Reference | Languages & SDKs"
meta_desc: Specification for the Pulumi HCL format and built-in functions
title: Reference
h1: Pulumi HCL reference
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Reference
        parent: iac-languages-hcl
        weight: 1
    languages:
        parent: hcl-language
        weight: 1
---

Pulumi programs can be defined in many languages, and the Pulumi HCL dialect offers an additional language for authoring Pulumi programs.

HCL programs are written in `.hcl` files. The programs include several top-level constructs:

| Type | Block or Expression | Description |
| - | - | - |
| `config` | Block | Config specifies the [Pulumi config](/docs/concepts/config/) inputs to the deployment. |
| `resources` | Block | Resources declares the [Pulumi resources](/docs/concepts/resources/) that will be deployed and managed by the program |
| `variables` | Expression | Variables specifies intermediate values of the program, the values of variables are expressions that can be re-used. |
| `outputs` | Block | Outputs specifies the [Pulumi stack outputs](/docs/concepts/stack#outputs) of the program and how they are computed from the `resources` is a value of the appropriate type for the template to use if no value is specified. |

## Config

`config` is a map of config property keys to either values or structured declarations ([see here](/docs/reference/pulumi-hcl/#config-options)).

### Basic syntax

```hcl
config name "type" {
  description = "Optional description"
  default     = value
}
```

| Property | Type | Required | Description |
| - | - | - | - |
| *name* | string | Yes | The logical name by which this config input will be referenced. |
| *type* | string | Yes | Type is the (required) data type for the parameter. |
| `description` | string | No | Human-readable description of the config value. |
| `default` | any | No | Default is a value of the appropriate type for the template to use if no value is specified. |
| `secret` | bool | No | Secret specifies if the config value should be encrypted as a secret. |

### Type specifications

PCL supports the following types:

**Primitive types:**
- `string` - Text values
- `number` - Numeric values (integers and floats)
- `bool` - Boolean values (true/false)

**Collection types:**
- `list(T)` - Ordered sequences
- `map(T)` - String key to value mappings

**Structural types:**
- `object({key=type, ...})` - Objects with specific fields

**Special types:**
- `any` - Any type (avoid when possible for type safety)

### Accessing config values

Reference configuration values directly by their name:

```hcl
resource "vpc" "aws:ec2/vpc:Vpc" {
  cidrBlock = "10.0.0.0/16"
  tags      = tags  // References config "tags"
}
```

## Resources

`resource` blocks represent a resource which will be managed by the Pulumi program.

### Resource syntax

```hcl
resource <name> "<type>" {
  __logicalName = "<terraform-name>"
  <property>    = <value>
  ...
}
```

| Component | Description |
| - | - |
| *name* | The local identifier (camelCase). |
| *type* | Fully qualified resource type in format `package:module/submodule:ResourceType`. |
| `__logicalName` | Optional original Terraform name for compatibility. |
| *properties* | Resource-specific configuration. |
| `options` | Options contains all resource options supported by Pulumi. |

#### Resource Options

The value of the `options` property of a resource is an object whose keys are [resource option names](/docs/concepts/options/) and whose values are elements of the schema below. No resource options are required.


| Property | Type | Description |
| - | - | - |
| `additionalSecretOutputs` | list(string) | AdditionalSecretOutputs specifies properties that must be encrypted as secrets |
| `aliases` | string[] | Aliases specifies names that this resource used to have, so that renaming or refactoring doesn’t replace it |
| `customTimeouts` | [Custom Timeout](#custom-timeout) | CustomTimeouts overrides the default retry/timeout behavior for resource provisioning |
| `deleteBeforeReplace` | bool | DeleteBeforeReplace  overrides the default create-before-delete behavior when replacing |
| `dependsOn` | list(any) | DependsOn makes this resource explicitly depend on another resource, by name, so that it won't be created before the dependent finishes being created (and the reverse for destruction). Normally, Pulumi automatically tracks implicit dependencies through inputs/outputs, but this can be used when dependencies aren't captured purely from input/output edges.|
| `ignoreChanges` | list(string) | IgnoreChanges declares that changes to certain properties should be ignored during diffing |
| `import` | string | Import adopts an existing resource from your cloud account under the control of Pulumi |
| `parent` | resource | Parent specifies a parent for the resource |
| `protect` | bool | Protect prevents accidental deletion of a resource |
| `provider` | resource | Provider specifies an explicitly configured provider, instead of using the default global provider |
| `providers` |  map[string]resource | Map of providers for a resource and its children. |
| `version` | string | Version specifies a provider plugin version that should be used when operating on a resource |
| `pluginDownloadURL` | string | PluginDownloadURL specifies a provider plugin download URL  |
| `replaceOnChanges` | list(string) | ReplaceOnChanges specifies if changes to certain properties on a resource should force replacement instead of an in-place update. |
| `retainOnDelete` | bool | RetainOnDelete causes a resource to be preserved in the cloud even when it is deleted from the Pulumi state. |
| `range` | list(any) or number | Create multiple instances of a resource using the `range` option. |

## Data sources (invoke)

Data sources allow you to query existing infrastructure or compute values without creating resources. In HCL, data sources use the `invoke` function.

### Basic invoke

```hcl
ami = invoke("aws:ec2/getAmi:getAmi", {
  mostRecent = true
  owners     = ["amazon"]
  filters = [{
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }]
})

resource "instance" "aws:ec2/instance:Instance" {
  ami          = ami.id
  instanceType = "t2.micro"
}
```

### Invoke syntax

The `invoke()` function takes two arguments:

1. **function name** - Fully qualified function name in format `package:module/submodule:functionName`
2. **arguments** - Map of input arguments to the function

The function returns an object with the result properties that can be accessed using dot notation.

## Outputs

Outputs export values from your program, making them available to other stacks or displaying them after deployment.

```hcl
output "bucketName" {
  value = bucket.id
}

output "bucketArn" {
  value       = bucket.arn
  description = "The ARN of the S3 bucket"
}

output "instanceIps" {
  value = [for server in webServers : server.publicIp]
}
```

| Property | Type | Required | Description |
| - | - | - | - |
| `value` | expression | Yes | The value to output. |
| `description` | string | No | Human-readable description of the output. |

Outputs are displayed after `pulumi up` completes and can be accessed via:
```bash
pulumi stack output bucketName
```

## Expressions

See the main HCL documentation for all expressions supported: https://github.com/hashicorp/hcl/blob/main/hclsyntax/spec.md

## Built-in functions

HCL provides access to functions through globally accessible function names, such as the `invoke` function from earlier.
Use standard function call syntax in any expression, for example `join("-", ["app", stack()])`.

### `element`

Returns the element at the given index from a list or tuple.

### `entries`

Converts a map or object into a list of objects with `key` and `value` fields.

### `fileArchive`

Creates an archive from a local file or directory path.

### `remoteArchive`

Creates an archive from a remote URL.

### `assetArchive`

Creates an archive from a map of assets and archives.

### `fileAsset`

Creates an asset from a local file path.

### `stringAsset`

Creates an asset from an inline string value.

### `remoteAsset`

Creates an asset from a remote URL.

### `join`

Joins a list of strings with a separator.

### `length`

Returns the length of a list, map, object, tuple, or string.

### `lookup`

Returns the value for a key in a map, with an optional default if the key is missing.

### `mimeType`

Returns the MIME type for a file path.

### `range`

Returns a list of integers from zero to `to - 1`, or from `from` to `to - 1` when two arguments are provided.

### `readDir`

Returns the entries of a directory as a list of strings.

### `readFile`

Returns the contents of a file as a string.

### `filebase64`

Returns the Base64-encoded contents of a file.

### `filebase64sha256`

Returns the Base64-encoded SHA-256 hash of a file's contents.

### `secret`

Marks a value as a secret.

### `unsecret`

Removes the secret designation from a value.

### `sha1`

Returns the SHA-1 hash of a string.

### `split`

Splits a string into a list using a separator.

### `toBase64`

Encodes a UTF-8 string as Base64.

### `fromBase64`

Decodes a Base64-encoded string to UTF-8.

### `toJSON`

Encodes a value as a JSON string.

### `stack`

Returns the name of the current stack.

### `project`

Returns the name of the current project.

### `organization`

Returns the name of the current organization.

### `cwd`

Returns the current working directory for the Pulumi program.

### `notImplemented`

Raises an error with a custom message to indicate an unsupported operation.

### `singleOrNone`

Returns the single element of a list or tuple, or null if the collection is empty.

### `getOutput`

Fetches a named output from a stack reference.

### `try`

Evaluates arguments in order and returns the first one that does not error.

### `can`

Returns whether an expression can be evaluated without error.

### `rootDirectory`

Returns the root directory of the Pulumi program.

### `pulumiResourceType`

Returns the Pulumi resource type for a resource.

### `pulumiResourceName`

Returns the Pulumi resource name for a resource.
