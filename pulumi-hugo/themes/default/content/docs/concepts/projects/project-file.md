---
title_tag: Project File Reference
meta_desc: Documentation of the settings that are valid for the Pulumi project file.
title: Project file reference
h1: Pulumi project file reference
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    parent: projects
    weight: 1

aliases:
- /docs/reference/pulumi-yaml/
- /docs/reference/project-file/
---

Every Pulumi program has a project file, `Pulumi.yaml`, which specifies metadata about your project, such as the project name and language runtime. The project file must begin with a capital `P` and have an extension of either `.yml` or `.yaml`. For more information about Pulumi projects, see the following [Pulumi projects overview](/docs/intro/concepts/project/).

{{< notes >}}
For Pulumi programs specifically written in Pulumi YAML, the project file not only serves as a configuration and metadata repository but also contains the program's infrastructure definition itself. To learn more, see [Pulumi YAML](/docs/intro/languages/yaml/).
{{< /notes >}}

## Attributes

| Name | Required | Description | Options |
| - | - | - | - |
| `name` | required | Name of the project containing alphanumeric characters, hyphens, underscores, and periods. | None |
| `runtime` | required | Installed language runtime of the project: `nodejs`, `python`, `go`, `dotnet`, `java` or `yaml`. | [runtime options](#runtime-options)
| `description` | optional | A brief description of the project. | None |
| `config` | optional | Project level config (Added in v3.44). | [config options](#config-options) |
| `main` | optional | Path to the Pulumi program, relative to the location of `Pulumi.yaml`. The default is the current working directory. | None |
| `stackConfigDir` | optional | Config directory location relative to the location of `Pulumi.yaml`. | None |
| `backend` | optional | [Backend](/docs/concepts/state/) of the project. | [backend options](#backend-options) |
| `options` | optional | Additional project options. | [options options](#options-options) |
| `template` | optional | Config to be used when creating new stacks in the project. | [template options](#template-options) |
| `plugins` | optional | Override for the plugin selection. Intended for use in developing pulumi plugins.  | [plugins options](#plugins-options) |

### About `main`

For all languages, `main` can point to a directory to have Pulumi load the program from that directory instead of the directory containing `Pulumi.yaml`.

Some languages also support using `main` to point to a specific file to change what the runtime considers the program entrypoint.

- For Node.js projects, `main` can point to a `.ts` or `.js` file and behaves similarly to setting the `main` attribute in `package.json`. When the `main` property is set in `Pulumi.yaml`, it may be omitted from `package.json` (and vice-versa). When it exists in both `Pulumi.yaml` and `package.json`, the value in `Pulumi.yaml` takes precedence.

- For Python projects, `main` can point to a module file (e.g., `example.py`) and the file will be passed to `python`.

- For .NET projects, `main` can point to a .NET project file (e.g., `example.csproj`) and the file will be passed to `dotnet run`.

For all other languages, the actual filename is ignored, and the system behaves as though `main` referred to the file's containing directory.

### `runtime` options

The runtime attribute has an additional property called `options` where you can further specify runtime configuration.

| Name | Use case | Description |
| - | - | - |
| `typescript` | Only applies to the `nodejs` runtime | Boolean indicating whether to use `ts-node` or not. |
| `nodeargs` | Only applies to the `nodejs` runtime | Arguments to pass to `node`. |
| `buildTarget` | Only applies to the `go` runtime | Path to save the compiled go binary to. |
| `binary` | applies to the `go`, `dotnet`, and `java` runtimes | Path to a pre-built executable. |
| `virtualenv` | Only applies to the `python` runtime | Virtual environment path. |
| `typechecker` | Only applies to the `python` runtime | Type checker library to use. |
| `compiler` | Only applies to the `yaml` runtime | Executable and arguments issued to standard out. |

#### About `nodeargs`

Arguments specified here are passed to `node` when running the Pulumi program. For example, `nodeargs: "--trace-warnings"` will result in `node` being invoked as `node --trace-warnings`.

#### About `buildTarget`

- For Go
  - If specified, Go sources in `$CWD` will be compiled with `go build` to the specified path before being run.
  - If unspecified, Go sources in `$CWD` will be compiled with `go build` to a temporary executable that is deleted after running.
  - Cannot be specified with the `binary` runtime option.

#### About `binary`

- For Go, cannot be specified with the `buildTarget` runtime option.
- For .NET, if not specified, a .NET project in `$CWD` will be invoked with `dotnet run`.

#### About `virtualenv`

New Python projects created with `pulumi new` have this option set by default. If not specified, Pulumi will invoke the `python3` command it finds on `$PATH` (falling back to `python`) to run the Python program. To use a virtual environment without the `virtualenv` option, run `pulumi` commands (such as `pulumi up`) from an activated virtual environment shell. Or, if using a tool like [Pipenv](https://github.com/pypa/pipenv), prefix `pulumi` commands with `pipenv run pulumi ...`.

#### About `typechecker`

This option can be set to `mypy` or `pyright`. (For additional type checkers, file an issue at [https://github.com/pulumi/pulumi/issues](https://github.com/pulumi/pulumi/issues).). If set, the given type checker will be invoked to check the Python code before running the Pulumi program.

### `config` options

`config` is a map of config property keys to either values or structured declarations.

Non-object values are allowed to be set directly. Anything more complex must be defined using the structured
schema declaration, or the nested value declaration both shown below.

#### Values

| Name | Required | Description |
| - | - | - |
| `value` | required | The value of this configuration property. |

#### Schemas

Schemas are only valid for project property keys. For setting the value of a provider configuration either use a direct value, or the nested value declaration shown above.

| Name | Required | Description |
| - | - | - |
| `type` | required | The type of this config property, either `string`, `boolean`, `integer`, or `array`. |
| `description` | optional | A description for this config property. |
| `secret` | optional | True if this config property should be a secure secret value. |
| `default` | optional | The default value for this config property, must match the given type. |
| `items` | required if `type` is `array` | A nested structured declaration of the type of the items in the array. |

### `backend` options

| Name | Required | Description |
| - | - | - |
| `url` | optional | URL is optional field to explicitly set backend url. |

### `options` options

| Name | Required | Description |
| - | - | - |
| `refresh` | optional | Set to `always` to refresh the state before performing a Pulumi operation. |

### `template` options

| Name | Required | Description |
| - | - | - |
| `displayName` | optional | A user-friendly name for the template. This should follow `Title Case` format and be succinct. This field is only supported by Pulumi CLI >= 3.95. |
| `description` | optional | Description of the template. |
| `config` | required | Config to request when using this template with `pulumi new`. |
| `metadata` | optional | A map of user-defined tags to attach to the template. This field is only supported by Pulumi CLI >= 3.95. |

#### `config`

| Name | Required | Description |
| - | - | - |
| `description` | optional | Description of the config. |
| `default` | optional | Default value of the config. |
| `secret` | optional | Boolean indicating if the configuration is labeled as a secret. |

### `plugins` options

Use this option to link to local plugin binaries. This option is intended for use in developing pulumi plugins.

| Name | Required | Description |
| - | - | - |
| `providers` | optional | List of provider plugins. |
| `analyzers` | optional | List of policy plugins. |
| `languages` | optional | List of language plugins. |

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

## Example project files

### Example project file with only required attributes

```yaml
name: Example Pulumi project file with only required attributes
runtime: nodejs
```

### Example project file with all possible attributes

```yaml
name: Example Pulumi project file with all possible attributes
runtime: yaml
description: An example project with all attributes
main: example-project/
stackConfigDir: config/
backend:
  url: https://pulumi.example.com
options:
  refresh: always
template:
  displayName: Example Template
  description: An example template
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-east-1
      secret: true
  metadata:
    cloud: aws
plugins:
  providers:
    - name: aws
      path: ../../bin
  languages:
    - name: yaml
      path: ../../../pulumi-yaml/bin
      version: 1.2.3
```
