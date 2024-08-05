---
title_tag: Creating a Pulumi Project | Pulumi Tutorials
title: "Creating a Pulumi Project"
layout: topic
description: To get started, create your first Pulumi project using the CLI.
meta_desc: Learn how to get started with Pulumi by creating your first Pulumi project using the Pulumi CLI in this tutorial.
weight: 1
estimated_time: 5
meta_image: meta.png
aliases:
    - /learn/pulumi-fundamentals/create-a-pulumi-project/
---

Infrastructure in Pulumi is organized into _projects_. In the Pulumi ecosystem,
a project represents a Pulumi _program_ that, when run, declares the desired
infrastructure for Pulumi to manage. The program has corresponding _stacks_, or
isolated, independently configurable instances of your Pulumi program. We'll
talk more about stacks later in the [Building with
Pulumi](/tutorials/building-with-pulumi) tutorial.

## Create a directory

Each Pulumi project lives in its own directory. Create one now and change into
it by running these commands in your terminal:

```bash
$ mkdir my-first-app
$ cd my-first-app
```

Pulumi will use the directory name as your project name by default. To create an
independent project, name the directory differently.

## Initialize your project

Since a Pulumi project is just a directory with some files in it, it is possible
for you to create a new one by hand. The `pulumi new` command-line interface
(CLI) command, however, automates the process and ensures you have everything
you need, so let's use that command. The `-y` flag answers "yes" to the prompts to
create a default project:

{{% chooser language "typescript,python" / %}}

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

This command creates all of the files you need, initializes a new stack named `dev`
(an instance of the project), and installs any necessary dependencies:

{{% choosable language typescript %}}

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

{{% choosable language python %}}

```bash
Created project 'my-first-app'
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

Open {{< langfile >}} in your editor of choice to have a look at its contents:

{{< chooser language "typescript,python" />}}

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

Feel free to explore the other files as well.

Now let's move on to creating your first real bit of infrastructure with Pulumi:
some Docker images!

<!-- [^1]: [project](https://www.pulumi.com/docs/concepts/glossary/#project) -->
<!-- [^2]: [program](https://www.pulumi.com/docs/concepts/glossary/#program) -->
<!-- [^3]: [stack](https://www.pulumi.com/docs/concepts/glossary/#stack) -->

{{< tutorials/stepper >}}
