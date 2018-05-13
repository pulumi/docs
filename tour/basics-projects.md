---
title: Projects
---

To get started with Pulumi, you'll need a project.

A project is a directory that contains a `Pulumi.yaml` manifest, telling Pulumi about its name and language.  A project
is just a place to put your Pulumi program and its stacks.  We'll soon see what those mean.

Creating a project manually is really simple.  Just make a new directory:

```bash
$ mkdir ahoy-pulumi/
$ cd ahoy-pulumi/
```

And create a `Pulumi.yaml` file in its root:

```yaml
name: ahoy-pulumi
description: Ahoy, Pulumi!
runtime: nodejs
```

Now that we have a project, let's create a program for it.

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-pulumi.html" title="Pulumi">◀</a>
    <span class="tour-index"><strong>3</strong>/8</span>
    <a class="tour-button enabled" href="basics-programs.html" title="Programs">▶</a>
</div>
