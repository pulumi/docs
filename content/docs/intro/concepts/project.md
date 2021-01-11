---
title: "Projects"
meta_desc: An in depth look at Pulumi projects and their usage.
menu:
  intro:
    parent: concepts
    weight: 1

aliases: ["/docs/reference/project/"]
---

A Pulumi project is any folder which contains a `Pulumi.yaml` file.  When in a subfolder, the closest enclosing folder with a `Pulumi.yaml` file determines the current project. A new project can be created with `pulumi new`. A project specifies which runtime to use and determines where to look for the program that should be executed during deployments. Supported runtimes are `nodejs`, `python`, `dotnet`, and `go`.

## Project file {#pulumi-yaml}

The `Pulumi.yaml` project file specifies metadata about your project.

{{% notes "info" %}}
The project file must begin with a capitalized `P`, although either `.yml` or `.yaml` extension will work.
{{% /notes %}}

A typical `Pulumi.yaml` file looks like the following:

```yaml
name: webserver
runtime: nodejs
description: Basic example of an AWS web server accessible over HTTP.
```

In addition, when using JavaScript, the working directory for the project should contain a `package.json` that points to a file such as `index.js`. In Python, there should either be a `__main__.py` file or a file `setup.py` that defines the entry point.

The following are other examples of `Pulumi.yaml` files that define project configurations for other use cases:

A `Pulumi.yaml` file for a `nodejs` program that does not execute TypeScript natively using `ts-node`.

```yaml
name: minimal
description: A minimal Pulumi program.
runtime:
  name: nodejs
  options:
    typescript: false
```

A `Pulumi.yaml` file for a `go` program that will only use a pre-built executable by the name `mybinary`.

```yaml
name: ls
runtime:
    name: go
    options:
        binary: mybinary
description: A minimal Go Pulumi program
```

A `Pulumi.yaml` file for a `dotnet` program that will use a pre-built assembly `MyInfra.dll` under the `bin` directory.

```yaml
name: ls
runtime:
    name: dotnet
    options:
        binary: bin/MyInfra.dll
description: A precompiled .NET Pulumi program
```

For more information on valid Pulumi project metadata, see [Pulumi Configuration Reference]({{< relref "/docs/reference/pulumi-yaml">}}).

## Paths

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

Each stack that is created in a project will have a file named `Pulumi.<stackname>.yaml` that contains the configuration specific to this stack. This file typically resides in the root of the project directory.

For stacks that are actively developed by multiple members of a team, the recommended practice is to check them into source control as a means of collaboration. Since secret values are encrypted, it is safe to check in these stack settings.

When using ephemeral stacks, the stack settings are typically not checked into source control.

For more information about configuration and how this file is managed using the CLI and programming model, refer to [Configuration]({{< relref "/docs/intro/concepts/config" >}}).
