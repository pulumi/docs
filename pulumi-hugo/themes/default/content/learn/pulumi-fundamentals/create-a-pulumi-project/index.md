---
title_tag: Creating a Pulumi Project | Learn Pulumi
title: "Creating a Pulumi Project"
layout: topic
date: 2021-09-10T12:00:00-05:00
draft: false
description: To get started, create your first Pulumi project using the CLI.
meta_desc: Learn how to get started with Pulumi by creating your first Pulumi project using the Pulumi CLI in this tutorial.
index: 0
estimated_time: 5
meta_image: meta.png
authors:
    - sophia-parafina
    - laura-santamaria
tags:
    - fundamentals
    - projects
    - docker
---

Infrastructure in Pulumi is organized into _projects_. In the Pulumi ecosystem,
a project represents a Pulumi _program_ that, when run, declares the desired
infrastructure for Pulumi to manage. The program has corresponding _stacks_, or
isolated, independently configurable instances of your Pulumi program. We'll
talk more about stacks later in the [Building with
Pulumi](/learn/building-with-pulumi) pathway.

## Create a directory

Each Pulumi project lives in its own directory. Create one now and change into
it by running these commands in your terminal:

```bash
mkdir my_first_app
cd my_first_app
```

Pulumi will use the directory name as your project name by default. To create an
independent project, name the directory differently.

## Initialize your project

Since a Pulumi project is just a directory with some files in it, it is possible
for you to create a new one by hand. The `pulumi new` command-line interface
(CLI) command, however, automates the process and ensures you have everything
you need, so let's use that command. The `-y` flag answers "yes" to the prompts to
create a default project:

{{< chooser language "typescript,python,go,csharp,java,yaml" / >}}

{{% choosable language typescript %}}

```bash
$ pulumi new typescript -y
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ pulumi new python -y
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ pulumi new go -y
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ pulumi new csharp -y
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
$ pulumi new java-gradle --dir my_first_app --name my_first_app -y
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ pulumi new yaml -y
```

{{% /choosable %}}

This command prints output similar to the following example with a bit more
information and status as it goes:

{{% choosable language typescript %}}

```bash
Created project 'my_first_app'
# ...

Installing dependencies...
# ...

Finished installing dependencies

Your new project is ready to go! ✨

To perform an initial deployment, run 'pulumi up'
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
Created project 'my_first_app'
# ...
Created stack 'dev'

Creating virtual environment...
# ...
Finished creating virtual environment

Updating pip, setuptools, and wheel in virtual environment...
# ...
Your new project is ready to go! ✨

To perform an initial deployment, run 'pulumi up'
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
Created project 'my-first-app'
# ...

Installing dependencies...
# ...

Finished installing dependencies

Your new project is ready to go! ✨

To perform an initial deployment, run 'pulumi up'
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
Created project 'my_first_app'

Created stack 'dev'

Installing dependencies...

#...

Finished installing dependencies

Your new project is ready to go! ✨

To perform an initial deployment, run 'pulumi up'
```

{{% /choosable %}}

{{% choosable language java %}}

```bash
Created project 'my_first_app'
# ...
Created stack 'dev'

Your new project is ready to go! ✨

To perform an initial deployment, run 'cd my_first_app', then, run 'pulumi up'
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
Created project 'my_first_app'
# ...
Created stack 'dev'

Your new project is ready to go! ✨

To perform an initial deployment, run 'pulumi up'
```

{{% /choosable %}}

This command creates all the files we need, initializes a new stack named `dev`
(an instance of our project), and installs any necessary dependencies.

## Inspect your new project

The basic project created by `pulumi new` is comprised of multiple files:

<!-- This section uses HTML due to an issue with langfile shortcode -->
<ul>
<li><code>Pulumi.yaml</code>: your project's metadata, containing its name and language</li>

{{< choosable language typescript >}}

<li>{{< langfile >}}: your program's main entrypoint file</li>
<li><code>package.json</code>: your project's Node.js dependency information</li>

{{< /choosable >}}

{{< choosable language python >}}

<li>{{< langfile >}}: your program's main entrypoint file</li>
<li><code>requirements.txt</code>: your project's Python dependency information</li>
<li><code>venv</code>: a <a href="https://pypi.org/project/virtualenv/">virtualenv</a> for your project</li>

{{< /choosable >}}

{{< choosable language go >}}

<li><code>go.mod</code>: a file that describes the Go program's properties</li>
<li><code>go.sum</code>: a generated file that maintains the checksums for the packages imported by the Go program</li>
<li>{{< langfile >}}: your program's main entrypoint file</li>

{{< /choosable >}}

{{< choosable language java >}}

<li>{{< langfile >}}: your program's main entrypoint file</li>
<li><code>settings.gradle</code>: your project's Gradle settings</li>
<li><code>app/</code>: the app directory generated for Java, which includes the following files:
<ul>
<li><code>build.gradle</code>: your project's build information for Gradle</li>
<li><code>src/main/java/my_first_app/</code>: the directory that holds your main entrypoint file</li>
</ul>
</li>

{{< /choosable >}}
</ul>

{{% choosable language yaml %}}

For YAML, your {{< langfile >}} is also your program's main entrypoint file.

{{% /choosable %}}

Use the command <code>cat</code>{{< langfile >}} to explore the contents of your
project's empty program:

{{< chooser language "typescript,python,go,java,yaml" / >}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
```

{{% /choosable %}}

{{% choosable language python %}}

```python
"""A Python Pulumi program"""

import pulumi
```

{{% /choosable %}}

{{% choosable language go %}}

```go
package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		return nil
	})
}
```

{{% /choosable %}}

{{% choosable language java %}}

```java
package my_first_app;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            ctx.export("exampleOutput", Output.of("example"));
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
name: my_first_app
runtime: yaml
description: A minimal Pulumi YAML program

configuration: {}
variables:     {}
resources:     {}
outputs:       {}
```

{{% /choosable %}}

Feel free to explore the other files.

Let's move on to creating your first real bit of infrastructure with Pulumi:
some Docker images.

<!-- [^1]: [project](https://www.pulumi.com/docs/concepts/glossary/#project) -->
<!-- [^2]: [program](https://www.pulumi.com/docs/concepts/glossary/#program) -->
<!-- [^3]: [stack](https://www.pulumi.com/docs/concepts/glossary/#stack) -->
