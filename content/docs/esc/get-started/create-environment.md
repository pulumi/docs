---
title_tag: Create a New Environment | Pulumi ESC
title: Create environment
h1: "Pulumi ESC: Create a New Environment"
meta_desc: This page provides an overview on how to create a new Pulumi ESC environment.
weight: 3
menu:
  esc:
    parent: esc-get-started
    identifier: esc-get-started-create-environment
aliases:
---

## Overview

In Pulumi ESC, an environment is a collection of configuration intended to capture the configuration values needed to work with a particular environment.
Environments belong to a Project, which is a collection of related environments.

An environment can be created one of two ways:

- via the Pulumi Cloud console
- via the CLI

This tutorial will walk you through how to create a new environment.

## Create an environment

### Create via the console

To create an environment via the console, navigate to [Pulumi Cloud](https://app.pulumi.com) and select the **Environments** link in the left-hand menu.

You will be directed to the Environments landing page. Select the **Create Environment** button to open the Create Environment flyout panel. Ensure the **Start from scratch** tab is selected and the **New Environment** option is chosen. Enter a project name (e.g., `my-project`) and an environment name (e.g., `dev-environment`), then select **Create Environment**. You will be directed to the environment definition page.

![Create Environment flyout panel showing Start from scratch tab with New Environment option selected, project name field containing 'my-project', and environment name field containing 'dev-environment'](/docs/esc/assets/esc-create-environment.png)

### Create via the CLI

To create an environment via the CLI, use the `esc env init` command as shown below, where `<org-name>` is optional and defaults to your Pulumi Cloud username.

```bash
esc env init [<org-name>/]<project-name>/<environment-name>
```

Note that environment names must be unique within a project and may only contain alphanumeric characters, hyphens, underscores, and periods. If you specify
an existing project the new environment will be created within it, otherwise a new project will be created.

```bash
$ esc env init my-project/dev-environment
Environment created.
```

You can validate that your environment was created by running the `esc env ls` command which will list all of the environments that you have access to.

```bash
$ esc env ls
myorg/my-project/dev-environment
```

In the next section, you will learn how to store configuration values and secrets in your environment.

{{< get-started-stepper >}}
