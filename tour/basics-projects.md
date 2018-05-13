---
title: Projects
---

To get started with Pulumi, you'll need a project.

A project is defined by a directory that contains a `Pulumi.yaml` project file.

This is a place to put your Pulumi program and its stacks.  We'll explore what these are soon -- for now, just
remember that your `Pulumi.yaml` defines a scope in the filesystem, and some important metadata.

Creating a project manually is quite easy.  Simply make a new directory:

```bash
$ mkdir ahoy-pulumi/
```

And create a `Pulumi.yaml` file inside of it:

```bash
$ cd ahoy-pulumi/
$ echo > Pulumi.yaml <<EOF
name: ahoy-pulumi
description: Ahoy, Pulumi!
runtime: nodejs
EOF
```

The are [more properties](/reference/yaml.html) you can put in your `Pulumi.yaml`, but `name`, `description`, and
`runtime` are good enough for most cases.

Now that we have a project, let's create a program for it!

<div class="tour-nav">
    <a class="tour-button enabled" href="basics-pulumi.html" title="Pulumi">◀</a>
    <span class="tour-index"><strong>3</strong>/9</span>
    <a class="tour-button enabled" href="basics-programs.html" title="Programs">▶</a>
</div>
