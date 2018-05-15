---
title: "Projects"
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

A project file may contain the following attributes:

* `name`: a required name for your project.  This shows up in the Pulumi dashboard and is used to aggregate the
  associated stacks and their resources underneath the project, as a simple kind of hierarchy.

* `description`: an optional friendly description about your project.

* `runtime`: the language runtime to use for your program.  This is required and must currently be one of `nodejs`
  (for JavaScript and TypeScript) or `python` (for Python).  At the moment, Pulumi doesn't depend on specific versions
  of these runtimes, and will simply use whatever version you have installed on your machine.

* `main`: an optional override for the main program's location.  Per the above section about Filesystem Scope, the
  location of the `Pulumi.yaml` by default determines both the program's working directory -- expected to contain its
  entry point -- in addition to things like the default container build scope.  In the event that you want to point
  Pulumi at a different program entry point, while keeping the filesystem scope broader, you can use the `main` element.

  For instance, let's say I want my Docker container built out of my entire repo, but my Pulumi program is underneath
  a subdirectory called `infra/`.  I can put `Pulumi.yaml` at the root and simply say `main: infra/`.

Note that a project file is required for projects that will be deployed directly.  Packages containing reusable
components do not necessarily need a project file; instead, just use your package manager's standard metadata format.

### Scoping

This file also defines the filesystem scope for your project.  This is used as the working directory when running
your program, in addition to defining things like the default container build scope.

Because `Pulumi.yaml` defines the working directory, your program's entry point is expected to be in the same directory
as the file.  This means `index.js` in JavaScript/Node.js and `__main__.py` in Python.  These can be overridden in the
usual ways in the chosen language (e.g., the `main` directive in `package.json` for Node.js, and `setup.py` for Python).

## Stack settings files {#stack-settings-file}

Each stack that is created in a project will have a file named `Pulumi.<stackname>.yaml` which contains the configuration specific to this stack.
