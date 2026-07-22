---
title_tag: "Projects | Pulumi Concepts"
meta_desc: A Pulumi project is any folder which contains a Pulumi.yaml file. Learn about how to use Pulumi projects, as well as example use cases.
title: Projects
h1: Projects
menu:
    iac:
        name: Projects
        parent: iac-concepts
        weight: 20
        identifier: iac-concepts-projects
    concepts:
        identifier: projects
        weight: 1

aliases:
- /docs/reference/project/
- /docs/tour/basics-projects/
- /docs/tour/programs/
- /docs/intro/concepts/project/
- /docs/concepts/projects/
---

A Pulumi project is any folder that contains a `Pulumi.yaml` project file. At runtime, the nearest parent folder containing a `Pulumi.yaml` file determines the current project. Projects are created with the [`pulumi new`](/docs/iac/cli/commands/pulumi_new/) command.

## The project file (Pulumi.yaml) {#pulumi-yaml}

The project file specifies which runtime to use and determines where to look for the program that should be executed during deployments. Supported runtimes are `nodejs`, `python`, `dotnet`, `go`, `java`, and `yaml`.

Project files also contain metadata about your project. The project file must begin with a capital `P`, although either `.yml` or `.yaml` extension will work.

A typical `Pulumi.yaml` file looks like the following. The `runtime` value depends on the language you choose:

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

{{% choosable language typescript %}}

```yaml
name: webserver
runtime: nodejs
description: A minimal Pulumi program.
```

{{% /choosable %}}
{{% choosable language python %}}

```yaml
name: webserver
runtime: python
description: A minimal Pulumi program.
```

{{% /choosable %}}
{{% choosable language go %}}

```yaml
name: webserver
runtime: go
description: A minimal Pulumi program.
```

{{% /choosable %}}
{{% choosable language csharp %}}

```yaml
name: webserver
runtime: dotnet
description: A minimal Pulumi program.
```

{{% /choosable %}}
{{% choosable language java %}}

```yaml
name: webserver
runtime: java
description: A minimal Pulumi program.
```

{{% /choosable %}}
{{% choosable language yaml %}}

```yaml
name: webserver
runtime: yaml
description: A minimal Pulumi program.
```

{{% /choosable %}}

{{< /chooser >}}

Each language has its own conventions for locating the program's entrypoint. For TypeScript, the working directory should contain a `package.json` file that points to an entrypoint such as `index.ts`. For Python, the presence of a `__main__.py` or `setup.py` file defines the entrypoint. Go, .NET, and Java follow the conventions of their respective build tools.

The following are other examples of `Pulumi.yaml` files that define project configurations for other use cases.

### Compiled languages with a pre-built executable

For Go, .NET, and Java, you can point the runtime at a pre-built executable or assembly with the `binary` option. This skips the build step at deployment time:

{{< chooser language "go,csharp,java" >}}

{{% choosable language go %}}

```yaml
name: my-project
description: A precompiled Go Pulumi program.
runtime:
  name: go
  options:
    binary: mybinary
```

{{% /choosable %}}
{{% choosable language csharp %}}

```yaml
name: my-project
description: A precompiled .NET Pulumi program.
runtime:
  name: dotnet
  options:
    binary: bin/MyInfra.dll
```

{{% /choosable %}}
{{% choosable language java %}}

```yaml
name: my-project
description: A precompiled Java Pulumi program.
runtime:
  name: java
  options:
    binary: target/my-project-1.0-SNAPSHOT-jar-with-dependencies.jar
```

{{% /choosable %}}

{{< /chooser >}}

### Inline resources with the YAML runtime

A `Pulumi.yaml` file for a YAML program can include its resources inline:

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

## Root-relative paths

You can get the directory containing the `Pulumi.yaml` file, which may differ from your working directory if the project sets a `main` option (see [main attribute](/docs/reference/pulumi-yaml/#attributes)). Each language provides its own function to retrieve this path, as shown in the example below.

The path returned is an absolute path. When using this in resource properties, ensure it's relative to the working directory. This prevents diffs from running the project on multiple machines with different roots.

{{< example-program path="awsx-root-directory" >}}

## Getting the current project programmatically

The {{< pulumi-getproject >}} function returns the name of the currently deploying project. This can be useful for naming or tagging resources.

{{< chooser language "typescript,python,go,csharp,java,yaml" >}}

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

To get the name of the currently deploying stack instead, see [Getting the current stack programmatically](/docs/iac/concepts/stacks/#getting-the-current-stack-programmatically).

## Stack settings files {#stack-settings-file}

Each stack that is created in a project will have a file named `Pulumi.<stackname>.yaml` that contains the configuration specific to this stack. This file typically resides in the root of the project directory.

For stacks that are actively developed by multiple members of a team, the recommended practice is to check them into source control as a means of collaboration. Since secret values are encrypted, it is safe to check in these stack settings. When using ephemeral stacks, the stack settings are typically not checked into source control.

For more information about configuration and how to manage these files on the command line and programmatically, refer to the [Configuration](/docs/concepts/config/) and [Secrets](/docs/concepts/secrets/) documentation.
