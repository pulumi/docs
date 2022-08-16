---
title: Project File Reference
linktitle: Project File
meta_desc: Documentation of the settings that are valid for the Pulumi project file.
menu:
  reference:
    name: Project File
    weight: 5
---

The `Pulumi.yaml` project file specifies metadata about your project, such as the project name and language runtime for your project.

## Example project files

### Example project file with only required attributes

```yaml
name: Example Pulumi project file with only requires attributes
runtime: nodejs
```

### Example project file with all possible attributes

```yaml
name: Example Pulumi project file will all possible attributes
runtime: yaml
description: An example project
main: example-project/
stackConfigDir: config/
backend:
  url: https://pulumi.example.com
options:
  refresh: true
template:
  description: An example template
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-east-1
      secret: true
plugins:
  providers:
    name: aws
    path: ../.../bin
  languages:
    name: yaml
    path: ../../../pulumi-yaml/bin
    version: 1.2.3
```

## Attributes

### All attributes

| Name | Required | Description | Options |
| - | - | - | - |
| `name` | required | Name of the project containing alphanumeric characters, hyphens, underscores, and periods. | None. |
| `runtime` | required | Installed language runtime of the project: `nodejs`, `python`, `go`, `dotnet`, `java` or `yaml`. | [runtime options](#runtime-options)
| `description` | optional | Description of the project. | None. |
| `main` | optional | Path to the Pulumi program. The default is the working directory. | None. |
| `stackConfigDir` | optional | Config directory location relative to the location of `Pulumi.yaml`. | None. |
| `backend` | optional | [Backend]({{< relref "/docs/intro/concepts/state" >}}) of the project. | None. |
| `options` | optional | Additional project options. | [options options](#options-options) |
| `template` | optional | Config to be used when creating new stacks in the project. | [template options](#template-options) |
| `plugins` | optional | Override for the plugin selection. Intended for use in developing pulumi plugins.  | [plugins options](#plugins-options) |

### `runtime` options

The runtime attribute has an additional property called options where you can further specify runtime configuration.

| Name | Use case | Description |
| - | - | - |
| `typescript` | Only applicable for the nodejs runtime | Boolean indicating whether to use `ts-node` or not. |
| `binary` | Applicable for the go, .net, and java runtimes | Path to pre-built executable. |
| `virtualenv` | Ony applicable for the python runtime | Virtual environment path. |
| `compiler` | Only applicable for YAML projects | Executable and arguments that emit to standard out. |

#### About `binary`

- For Go, if not specified, go sources in `$CWD` will be invoked via `go run`.
- For .NET, if not specified, a .NET project in `$CWD` will be invoked via `dotnet run`.

#### About `virtualenv`

New Python projects created with `pulumi new` have this option set by default. If not specified, Pulumi will invoke the `python3` command it finds on `$PATH` (falling back to `python`) to run the Python program. To use a virtual environment without the `virtualenv` option, run `pulumi` commands (such as `pulumi up`) from an activated virtual environment shell. Or, if using a tool like [Pipenv](https://github.com/pypa/pipenv), prefix `pulumi` commands with `pipenv run pulumi ...`.

### `options` options

| Name | Required | Description | Default |
| - | - | - | - |
| `refresh` | optional | Boolean indicating whether to refresh the state before performing a Pulumi operation. | `true` |

### `template` options

| Name | Required | Description |
| - | - | - |
| `description` | optional | Description of the template. |
| `config` | required | Config to apply to each stack in the project. |

#### `config` options

| Name | Required | Description |
| - | - | - |
| `description` | optional | Description of the config. |
| `default` | optional | Default value of the config. |
| `secret` | optional | Boolean indicating if the configuration is labeled as a secret. |

### `plugins` options

Use this option to link to local plugin binaries. This option is intended for use in developing pulumi plugins.

| Name | Required | Description |
| - | - | - |
| `providers` | optional | Plugin for the provider. |
| `analyzers` | optional | Plugin for the policy. |
| `languages` | optional | Plugin in for the language. |

#### Options for `providers`, `analyzers`, and `languages`

| Name | Required | Description |
| - | - | - |
| `name` | required | Name of the plugin. |
| `path` | optional | Path to the plugin folder. |
| `version` | optional | Version of the plugin, if not set, will match any version the engine requests. |

### Deprecated attributes

| Name | Required | Description |
| - | - | - |
| `config` | optional | Config directory relative to the location of `Pulumi.yaml`. |
