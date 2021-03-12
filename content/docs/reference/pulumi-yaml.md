---
title: Project Configuration Reference
linktitle: Project Configuration
meta_desc: A list of configuration settings for the Pulumi project file.
menu:
  reference:
    name: Project Configuration
    weight: 3
---

The `Pulumi.yaml` project file specifies metadata about your project, such as the project name, applicable runtime for your program, and other higher-level information.

It contains the following required and optional attributes:

- `name`: (required) a name for your project.  This shows up in the Pulumi dashboard and is used to aggregate the
  associated stacks and their resources underneath the project, as a simple kind of hierarchy.  Project names may only contain alphanumeric characters, hyphens, underscores, or periods.

- `runtime`: (required) (`string`|`object`) the language runtime configuration to use for your program.  Possible string options are `nodejs`
  (for JavaScript and TypeScript), `python` (for Python),`go` (for Go), and `dotnet` (for .NET).  At the moment, Pulumi doesn't depend on specific versions
  of these runtimes, and will simply use whatever version you have installed on your machine.
    - `name`: `runtime` can either be specified as a string, or a complex object with additional configuration. If you need to include additional configuration, specify language information (`nodejs`, `python`, `go`, or `dotnet`) in this property.
    - `options`: (optional) a property bag that has various configuration options that apply to different language runtimes.
        - `typescript`: applies to Node.js projects only. A boolean (`true` | `false`) controls whether to use ts-node to execute sources. Defaults to `true`.
        - `binary`: applies to Go and .NET projects only
            - **Go**: A string that specifies the name of a pre-built executable to look for on your path. If not specified, go sources in $CWD will be invoked via `go run`.
            - **.NET**: A string that specifies the path of a pre-built .NET assembly. If not specified, a .NET project in $CWD will be invoked via `dotnet run`.
        - `virtualenv`: applies to Python projects only. A string that specifies the path to a virtual environment to use when running the program. New Python projects created with `pulumi new` have this option set by default. If not specified, Pulumi will invoke the `python3` command it finds on $PATH (falling back to `python`) to run the Python program. If you'd like to use a virtual environment without the `virtualenv` option, you'll need to run any `pulumi` commands (such as `pulumi up`) from an activated virtual environment shell (or, if using a tool like [Pipenv](https://github.com/pypa/pipenv), prefix any `pulumi` commands with `pipenv run pulumi ...`).

- `description`: (optional) a friendly description about your project.

- `main`: (optional) an override for the main program's location. By default, the program's working directory is assumed to be the location of `Pulumi.yaml`. To choose a different location, use the `main` property. For example, if your Pulumi program is in a subdirectory `infra/`, use `main: infra/`.

- `config`: (optional) directory to store stack-specific configuration files, relative to location of `Pulumi.yaml`.

- `backend`: (optional) configuration for project state [backend]({{< relref "/docs/intro/concepts/state" >}}). Supports these options:
    - `url`: explicitly specify backend URL like `https://pulumi.acmecorp.com`, `file:///app/data`, etc.

- `template`: (optional) provides configuration settings that will be used when initializing a new stack from a project file using `pulumi new`. Currently these values are *only- used by `pulumi new`, and not by `pulumi stack init` or as default configuration for existing stacks.
    - `description`: (optional) a description for the template itself.
    - `config`: (required) the map of configuration values keyed by the name of the config setting - such as `aws:region`.  The value of each key includes:
        - `description`: (optional) a description for the config setting.
        - `default`: (optional) the default value of the config setting - which will be presented to the user as a default.
        - `secret`: (optional) if `true` indicates that this configration value should be marked as secret.
