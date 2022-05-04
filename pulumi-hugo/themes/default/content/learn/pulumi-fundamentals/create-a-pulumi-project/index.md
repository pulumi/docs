---
title: "Creating a Pulumi Project"
layout: topic
date: 2021-09-10T12:00:00-05:00
draft: false
description: To get started, create your first Pulumi project using the CLI.
meta_desc: To get started, create your first Pulumi project using the CLI.
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
Pulumi]({{< relref "/learn/building-with-pulumi" >}}) pathway.

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

{{< chooser language "typescript,python,java,yaml" / >}}

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

- `Pulumi.yaml`: your project's metadata, containing its name and language
- {{< langfile >}}: your program's main entrypoint file

{{% choosable language typescript %}}

- `package.json`: your project's Node.js dependency information

{{% /choosable %}}

{{% choosable language python %}}

- `requirements.txt`: your project's Python dependency information
- `venv`: a [virtualenv](https://pypi.org/project/virtualenv/) for your project

{{% /choosable %}}

{{% choosable language java %}}

- `settings.gradle`: your project's Gradle settings
- `app/`: the app directory generated for Java, which includes the following files:
    - `build.gradle`: your project's build information for Gradle
    - `src/main/java/my_first_app/`: the directory that holds your main entrypoint file

{{% /choosable %}}

{{% choosable language yaml %}}
{{% /choosable %}}

Use the command <code>cat</code>{{< langfile >}} to explore the contents of your
project's empty program:

{{< chooser language "typescript,python,java,yaml" / >}}

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

{{% choosable language java %}}

```java
package my_first_app;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            ctx.export("exampleOutput", Output.of("example"));
            return ctx.exports();
        });
    }
}
```

{{% /choosable %}}

{{% choosable language yaml %}}

```yaml
description: ${DESCRIPTION}
runtime: yaml
template:
    description: A minimal Pulumi YAML program
configuration: {}
variables: {}
resources: {}
outputs: {}
```

{{% /choosable %}}

Feel free to explore the other files.

Let's move on to creating your first real bit of infrastructure with Pulumi:
some Docker images.

<!-- [^1]: [project](https://www.pulumi.com/docs/reference/glossary/#project) -->
<!-- [^2]: [program](https://www.pulumi.com/docs/reference/glossary/#program) -->
<!-- [^3]: [stack](https://www.pulumi.com/docs/reference/glossary/#stack) -->
