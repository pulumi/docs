---
title: "Projects"
---

A Pulumi project is any folder which contains a `Pulumi.yaml` file.  When in a subfolder, the closest enclosing folder with a `Pulumi.yaml` file determines the current project.  A new project can be created with `pulumi new`.  A project specifies which runtime to use, which determines where to look for the program that should be executed during deployments.  Currently, `nodejs` and `python` are supported runtimes.

## Project file {#pulumi-yaml}

The `Pulumi.yaml` file looks like the following:

```yaml
name: webserver
runtime: nodejs
description: Basic example of an AWS web server accessible over HTTP.
```

The `name` property is a string indicating which project name should be associated with stacks created within this project folder.

The `description` property is a helpful string of text to describe the contents of the project.

The `runtime` property tells Pulumi what language runtime to use.  Currently `nodejs` (for JavaScript and TypeScript) and `python` (for Python) are supported.

🚧 TODO: document `entrypoint` property.

## Stack settings files {#stack-settings-file}

Each stack that is created in a project will have a file named `Pulumi.<stackname>.yaml` which contains the configuration specific to this stack.

