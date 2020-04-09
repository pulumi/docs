---
title: "Projects"
meta_desc: An in depth look at Pulumi Projects and their usage.
menu:
  intro:
    parent: concepts
    weight: 2

aliases: ["/docs/reference/project/"]
---

A Pulumi project is any folder which contains a `Pulumi.yaml` file.  When in a subfolder, the closest enclosing folder with a `Pulumi.yaml` file determines the current project.  A new project can be created with `pulumi new`.  A project specifies which runtime to use, which determines where to look for the program that should be executed during deployments.  Currently, `nodejs` and `python` are supported runtimes.

## Project file {#pulumi-yaml}

The `Pulumi.yaml` project file specifies metadata about your project.

> This file must begin with a capitalized `P`, although either `.yml` or `.yaml` extension will work.

A typical `Pulumi.yaml` file looks like the following:

```yaml
name: webserver
runtime: nodejs
description: Basic example of an AWS web server accessible over HTTP.
```

A project file contains the following attributes:

* `name`: (required) a name for your project.  This shows up in the Pulumi dashboard and is used to aggregate the
  associated stacks and their resources underneath the project, as a simple kind of hierarchy.

* `runtime`: (required) (`string`|`object`) the language runtime configuration to use for your program.  Possible string options are `nodejs`
  (for JavaScript and TypeScript), `python` (for Python),`go` (for Go), and `dotnet` (for Dotnet).  At the moment, Pulumi doesn't depend on specific versions
  of these runtimes, and will simply use whatever version you have installed on your machine.
    * `name`: `runtime` can either be specified as a string, or a complex object with additional configuration. If you need to include additional configuration, specify language information (`nodejs`, `python`, `go`, or `dotnet`) in this property.
    * `options`: (optional) a property bag that has various configuration options that apply to different language runtimes.
        * `typescript`: applies to nodejs projects only. A boolean (`true` | `false`) controls whether to use ts-node to execute sources. Defaults to `true`.
        * `prebuilt`: applies to Go projects only. A string that specifies the name of a pre-built executable to look for on your path. If not specified, go sources in $CWD will be invoked via `go run`.

* `description`: (optional) a friendly description about your project.

* `main`: (optional) an override for the main program's location. By default, the program's working directory is assumed to be the location of `Pulumi.yaml`. To choose a different location, use the `main` property. For example, if your Pulumi program is in a subdirectory `infra/`, use `main: infra/`.

* `config`: (optional) directory to store stack-specific configuration files, relative to location of `Pulumi.yaml`.

* `backend`: (optional) configuration for project state [backend]({{< relref "state#config-stack" >}}). Supports this options:
    * `url`: explicitly specify backend url like `https://pulumi.acmecorp.com`, `file:///app/data`, etc.

When using JavaScript, the working directory for the project should contain a `package.json` that points to a file such as `index.js`. In Python, there should either be a `__main__.py` file or a file `setup.py` that defines the entry point.

A `Pulumi.yaml` file for a `nodejs` program that does not execute typescript natively via `ts-node`:

```yaml
name: minimal
description: A minimal Pulumi program.
runtime:
  name: nodejs
  options:
    typescript: false
```

A `Pulumi.yaml` file for a `go` program that will only use a pre-built executable by the name `myprebuilt`:

```yaml
name: ls
runtime:
    name: go
    options:
        prebuilt: myprebuilt
description: A minimal Go Pulumi program
```

### Paths

When your Pulumi program references resources in the local filesystem, they are always relative to the working directory. The following example code references a subfolder `app` of the working directory, which would contain a `Dockerfile` and application code:

{{< chooser language "javascript,typescript,python,csharp" >}}

{{% choosable language javascript %}}

```javascript
const myTask = new cloud.Task("myTask", {
    build: "./app", // subfolder of working directory
    ...
});
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const myTask = new cloud.Task("myTask", {
    build: "./app", // subfolder of working directory
    ...
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
myTask = Task('myTask',
    spec={
        'build': './app' # subfolder of working directory
        ...
    }
)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var myTask = new Task("myTask", new TaskArgs
{
    Build = "./app", // subfolder of working directory
    ...
});
```

{{% /choosable %}}

{{< /chooser >}}

## Stack Settings Files {#stack-settings-file}

Each stack that is created in a project will have a file named `Pulumi.<stackname>.yaml` which contains the configuration specific to this stack.

For stacks that are actively developed by multiple members of a team, the recommended practice is to check them into source control as a means of collaboration. Since secret values are encrypted, it is safe to check in these stack settings.

For stacks that are ephemeral or are used in "inner loop" development, the stack settings are typically not checked into source control.

For more information about configuration and how this file is managed using the CLI and programming model, refer to [Configuration and Secrets]({{< relref "config" >}}).
