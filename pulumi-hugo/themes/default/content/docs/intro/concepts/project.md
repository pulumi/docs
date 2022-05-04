---
title: "Projects"
meta_desc: An in depth look at Pulumi projects and their usage.
menu:
  intro:
    parent: concepts
    weight: 2

aliases: ["/docs/reference/project/"]
---

A Pulumi project is any folder which contains a `Pulumi.yaml` file.  When in a subfolder, the closest enclosing folder with a `Pulumi.yaml` file determines the current project. A new project can be created with `pulumi new`. A project specifies which runtime to use and determines where to look for the program that should be executed during deployments. Supported runtimes are `nodejs`, `python`, `dotnet`, `go`, `java`, and `yaml`.

## Project file {#pulumi-yaml}

The `Pulumi.yaml` project file specifies metadata about your project. The project file must begin with a capitalized `P`, although either `.yml` or `.yaml` extension will work.

A typical `Pulumi.yaml` file looks like the following:

```yaml
name: webserver
runtime: nodejs
description: Basic example of an AWS web server accessible over HTTP.
```

In addition, when using JavaScript, the working directory for the project should contain a `package.json` that points to a file such as `index.js`. In Python, there should either be a `__main__.py` file or a `setup.py` file that defines the entry point.

The following are other examples of `Pulumi.yaml` files that define project configurations for other use cases:

* A `Pulumi.yaml` file for a `nodejs` program that uses JavaScript rather than TypeScript.

    ```yaml
    name: my-project
    description: A minimal JavaScript Pulumi program.
    runtime:
        name: nodejs
        options:
            typescript: false
    ```

* A `Pulumi.yaml` file for a `go` program that will only use a pre-built executable by the name `mybinary`.

    ```yaml
    name: my-project
    runtime:
        name: go
        options:
            binary: mybinary
    description: A minimal Go Pulumi program
    ```

* A `Pulumi.yaml` file for a `dotnet` program that will use a pre-built assembly `MyInfra.dll` under the `bin` directory.

    ```yaml
    name: my-project
    runtime:
        name: dotnet
        options:
            binary: bin/MyInfra.dll
    description: A precompiled .NET Pulumi program
    ```

* A `Pulumi.yaml` file for a `java` program that will use a pre-built JAR `target/my-project-1.0-SNAPSHOT-jar-with-dependencies.jar`.

    ```yaml
    name: my-project
    runtime:
        name: java
        options:
            binary: target/my-project-1.0-SNAPSHOT-jar-with-dependencies.jar
    description: A precompiled Java Pulumi program
    ```

* A `Pulumi.yaml` file for a `YAML` program that includes its resources inline.

    ```yaml
    name: my-project
    runtime: yaml
    resources:
      bucket:
        type: aws:s3:Bucket
    ```

For more information on valid Pulumi project metadata, see [Pulumi Configuration Reference]({{< relref "/docs/reference/pulumi-yaml">}}).

## Paths

When your Pulumi program references resources in the local filesystem, they are always relative to the working directory. The following example code references a subfolder `app` of the working directory, which would contain a `Dockerfile` and application code:

{{< chooser language "javascript,typescript,python,csharp,java,yaml" >}}

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
{{% choosable language java %}}

```java
var myTask = new Task("myTask",
    TaskArgs.builder()
    .build("./app") // subfolder of working directory.
    .build()); // Java overloading handles ambiguity since the arguments are different
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
resources:
  myTask:
    type: cloud:Task
    properties:
      build: ./app # subfolder of working directory
      ...
```

{{% /choosable %}}

{{< /chooser >}}

## Getting the Current Project Programmatically

The {{< pulumi-getproject >}} function returns the name of the currently deploying project. This can be useful for naming or tagging resources.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
let project = pulumi.getProject();
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
let project = pulumi.getProject();
```

{{% /choosable %}}
{{% choosable language python %}}

```python
project = pulumi.get_project()
```

{{% /choosable %}}
{{% choosable language go %}}

```go
project := ctx.Project()
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var project = Deployment.Instance.ProjectName;
```

{{% /choosable %}}
{{% choosable language java %}}

```java
var project = ctx.projectName();
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
variables:
    project: ${pulumi.project}
```

{{% /choosable %}}

{{< /chooser >}}

## Stack Settings Files {#stack-settings-file}

Each stack that is created in a project will have a file named `Pulumi.<stackname>.yaml` that contains the configuration specific to this stack. This file typically resides in the root of the project directory.

For stacks that are actively developed by multiple members of a team, the recommended practice is to check them into source control as a means of collaboration. Since secret values are encrypted, it is safe to check in these stack settings.

When using ephemeral stacks, the stack settings are typically not checked into source control.

For more information about configuration and how this file is managed using the CLI and programming model, refer to [Configuration]({{< relref "/docs/intro/concepts/config" >}}).
