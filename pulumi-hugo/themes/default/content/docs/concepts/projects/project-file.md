---
title_tag: Project File Reference
meta_desc: Documentation of the settings that are valid for the Pulumi project file.
title: Project file
h1: Pulumi project file
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    parent: projects
    weight: 1

aliases:
- /docs/reference/pulumi-yaml/
- /docs/reference/project-file/
---

The `Pulumi.yaml` project file specifies metadata about your project, such as the project name and language runtime for your project.

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
  description: An example template
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-east-1
      secret: true
plugins:
  providers:
    - name: aws
      path: ../../bin
  languages:
    - name: yaml
      path: ../../../pulumi-yaml/bin
      version: 1.2.3
```

## Attributes

### All attributes

| Name | Required | Description | Options |
| - | - | - | - |
| `name` | required | Name of the project containing alphanumeric characters, hyphens, underscores, and periods. | None. |
| `runtime` | required | Installed language runtime of the project: `nodejs`, `python`, `go`, `dotnet`, `java` or `yaml`. | [runtime options](#runtime-options)
| `description` | optional | A brief description of the project. | None. |
| `config` | optional | Project level config (Added in v3.44). | [config options](#config-options) |
| `main` | optional | Path to the Pulumi program. The default is the working directory. | None. |
| `stackConfigDir` | optional | Config directory location relative to the location of `Pulumi.yaml`. | None. |
| `backend` | optional | [Backend](/docs/concepts/state/) of the project. | [backend options](#backend-options) |
| `options` | optional | Additional project options. | [options options](#options-options) |
| `template` | optional | Config to be used when creating new stacks in the project. | [template options](#template-options) |
| `plugins` | optional | Override for the plugin selection. Intended for use in developing pulumi plugins.  | [plugins options](#plugins-options) |

#### About `main`

For all languages `main` can point to a directory to tell Pulumi to use that directory to load the program from instead of the directory with the `Pulumi.yaml` file. Some languages also support `main` pointing to a file to change what the runtime considers the entrypoint.

- For NodeJS `main` can point to a ts or js file and behaves similarly to setting the main attribute in `package.json`.
- For .NET `main` can point at a project file (e.g. `example.csproj`) and will pass that project to `dotnet run`.
- For other languages if a file is specified it is ignored and the system behaves as if the files directory was given to `main` instead.

### `runtime` options

The runtime attribute has an additional property called options where you can further specify runtime configuration.

| Name | Use case | Description |
| - | - | - |
| `typescript` | Only applicable for the **nodejs** runtime | Boolean indicating whether to use `ts-node` or not. |
| `nodeargs` | Only applicable for the **nodejs** runtime | Arguments to pass to `node`. |
| `buildTarget` | Only applicable for the **go** runtime | Path to save the compiled go binary to. |
| `binary` | Applicable for the **go**, **.net**, and **java** runtimes | Path to pre-built executable. |
| `virtualenv` | Ony applicable for the **python** runtime | Virtual environment path. |
| `compiler` | Only applicable for **YAML** projects | Executable and arguments issued to standard out. |

#### About `nodeargs`

Arguments specified here are passed to `node` when running the Pulumi program. For example, `nodeargs: "--trace-warnings"` will result in `node` being invoked as `node --trace-warnings`.

#### About `buildTarget`

- For Go
  - If specified, go sources in `$CWD` will be compiled via `go build` to the specified path before being run.
  - If unspecified, go sources in `$CWD` will be compiled via `go build` to a temporary executable that is deleted after running.
  - Cannot be specified with the `binary` runtime option.

#### About `binary`

- For Go, cannot be specified with the `buildTarget` runtime option.
- For .NET, if not specified, a .NET project in `$CWD` will be invoked via `dotnet run`.

#### About `virtualenv`

New Python projects created with `pulumi new` have this option set by default. If not specified, Pulumi will invoke the `python3` command it finds on `$PATH` (falling back to `python`) to run the Python program. To use a virtual environment without the `virtualenv` option, run `pulumi` commands (such as `pulumi up`) from an activated virtual environment shell. Or, if using a tool like [Pipenv](https://github.com/pypa/pipenv), prefix `pulumi` commands with `pipenv run pulumi ...`.

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
| `description` | optional | Description of the template. |
| `config` | required | Config to request when using this template with `pulumi new`. |

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
