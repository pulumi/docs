---
title_tag: "Projects | Pulumi Concepts"
meta_desc: A Pulumi project is any folder which contains a Pulumi.yaml file. Learn about how to use Pulumi projects, as well as example use cases.
title: Projects
h1: Projects
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: projects
    weight: 1

aliases:
- /docs/reference/project/
- /docs/tour/basics-projects/
- /docs/tour/programs/
- /docs/intro/concepts/project/
---

A Pulumi project is any folder that contains a `Pulumi.yaml` project file. At runtime, the nearest parent folder containing a `Pulumi.yaml` file determines the current project. Projects are created with the [`pulumi new`](/docs/cli/commands/pulumi_new/) command.

## The project file (Pulumi.yaml) {#pulumi-yaml}

The project file specifies which runtime to use and determines where to look for the program that should be executed during deployments. Supported runtimes are `nodejs`, `python`, `dotnet`, `go`, `java`, and `yaml`.

Project files also contain metadata about your project. The project file must begin with a capital `P`, although either `.yml` or `.yaml` extension will work.

A typical `Pulumi.yaml` file looks like the following:

```yaml
name: webserver
runtime: nodejs
description: A minimal JavaScript Pulumi program.
```

In addition, when using JavaScript or TypeScript, the working directory for the project should contain a `package.json` file that points to an entrypoint such as `index.js`. In Python, the presence of a `__main__.py` or `setup.py` file defines the entrypoint.

The following are other examples of `Pulumi.yaml` files that define project configurations for other use cases:

* A `Pulumi.yaml` file for a Node.js program that uses JavaScript rather than TypeScript:

    ```yaml
    name: my-project
    runtime:
      name: nodejs
      options:
        typescript: false
    ```

* A `Pulumi.yaml` file for a Go program that uses a pre-built executable named `mybinary`:

    ```yaml
    name: my-project
    description: A precompiled Go Pulumi program.
    runtime:
      name: go
      options:
        binary: mybinary
    ```

* A `Pulumi.yaml` file for a .NET program that uses a pre-built assembly named `MyInfra.dll` in the `bin` directory:

    ```yaml
    name: my-project
    description: A precompiled .NET Pulumi program.
    runtime:
      name: dotnet
      options:
        binary: bin/MyInfra.dll

    ```

* A `Pulumi.yaml` file for a Java program that uses a pre-built JAR file:

    ```yaml
    name: my-project
    description: A precompiled Java Pulumi program.
    runtime:
        name: java
        options:
            binary: target/my-project-1.0-SNAPSHOT-jar-with-dependencies.jar
    ```

* A `Pulumi.yaml` file for a `YAML` program that includes its resources inline:

    ```yaml
    name: my-project
    runtime: yaml
    resources:
      bucket:
        type: aws:s3:Bucket
    ```

For more information on valid Pulumi project metadata, see the [Pulumi.yaml reference](/docs/reference/pulumi-yaml/).

## Project-relative paths

When your Pulumi program refers to resources in the local filesystem, paths are always relative to the working directory. In the following example, the `aws.ecr.Image` resource refers to a subfolder of the working directory named `app` that contains a `Dockerfile`:

{{< example-program path="awsx-ecr-image" >}}

## Getting the current project programmatically

The {{< pulumi-getproject >}} function returns the name of the currently deploying project. This can be useful for naming or tagging resources.

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
const project = pulumi.getProject();
```

{{% /choosable %}}
{{% choosable language typescript %}}

```typescript
const project = pulumi.getProject();
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

## Stack settings files {#stack-settings-file}

Each stack that is created in a project will have a file named `Pulumi.<stackname>.yaml` that contains the configuration specific to this stack. This file typically resides in the root of the project directory.

For stacks that are actively developed by multiple members of a team, the recommended practice is to check them into source control as a means of collaboration. Since secret values are encrypted, it is safe to check in these stack settings. When using ephemeral stacks, the stack settings are typically not checked into source control.

For more information about configuration and how to manage these files on the command line and programmatically, refer to the [Configuration](/docs/concepts/config/) and [Secrets](/docs/concepts/secrets/) documentation.
