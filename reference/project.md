---
title: "Projects"
---

A Pulumi project is any folder which contains a `Pulumi.yaml` file.  When in a subfolder, the closest enclosing folder with a `Pulumi.yaml` file determines the current project.  A new project can be created with `pulumi new`.  A project specifies which runtime to use, which determines where to look for the program that should be executed during deployments.  Currently, `nodejs` and `python` are supported runtimes.

Packages that contain [reusable components](./programming-model.html#components) do not need a project file and can simply use the package manager's standard metadata format.

## Project file {#pulumi-yaml}

The `Pulumi.yaml` project file specifies metadata about your project.

> This file must begin with a capitalized `P`, although either `.yml` or `.yaml` extension will work.

A typical `Pulumi.yaml` file looks like the following:

```yaml
name: webserver
runtime: nodejs
description: Basic example of an AWS web server accessible over HTTP.
```

A project file contains the following attributes:

* `name`: (required) a name for your project.  This shows up in the Pulumi dashboard and is used to aggregate the
  associated stacks and their resources underneath the project, as a simple kind of hierarchy.

* `runtime`: (required) the language runtime to use for your program.  Possible options are `nodejs`
  (for JavaScript and TypeScript), `python` (for Python), and `go` (for Go).  At the moment, Pulumi doesn't depend on specific versions
  of these runtimes, and will simply use whatever version you have installed on your machine.

* `description`: (optional) a friendly description about your project.

* `main`: (optional) an override for the main program's location. By default, the program's working directory is assumed to be the location of `Pulumi.yaml`. To choose a different location, use the `main` property. For example, if your Pulumi program is in a subdirectory `infra/`, use `main: infra/`.

* `config`: (optional) directory to store stack-specific configuration files, relative to location of `Pulumi.yaml`.

When using JavaScript, the working directory for the project should contain a `package.json` that points to a file such as `index.js`. In Python, there should either be a `__main__.py` file or a file `setup.py` that defines the entry point.

### Paths

When your Pulumi program references resources in the local filesystem, they are always relative to the working directory. For example, the following code references a subfolder `app` of the working directory, that contains a `Dockerfile`:

```js
const myTask = new cloud.Task("myTask", {
    build: "./app", // subfolder of working directory
    ...
});
```

## Stack settings files {#stack-settings-file}

Each stack that is created in a project will have a file named `Pulumi.<stackname>.yaml` which contains the configuration specific to this stack. To learn more, see [Adding and configuring stack settings](config.html#config-stack).
