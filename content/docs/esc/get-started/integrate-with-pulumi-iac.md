---
title_tag: Integrate with Pulumi IaC | Pulumi ESC
title: Integrate with Pulumi IaC
h1: "Pulumi ESC: Integrate with Pulumi IaC"
meta_desc: This page provides an overview on how to use Pulumi ESC with Pulumi IaC.
weight: 8
menu:
  pulumiesc:
    parent: esc-get-started
    identifier: esc-get-started-integrate-with-pulumi-iac
---

## Overview

Pulumi ESC works independently of [Pulumi Infrastructure as Code (IaC)](/docs/get-started/), providing developers the flexibility to centrally manage their environment configuration regardless of how or where those environments are created.

Pulumi ESC also integrates seamlessly with Pulumi IaC, and this tutorial will demonstrate how to leverage Pulumi ESC in your own Pulumi programs. This works everywhere, including Pulumi Deployments and GitHub Actions, without any additional work or changes.

## Prerequisites

To complete the steps in this tutorial, you will need to install the following prerequisites:

- the [Pulumi IaC CLI](/docs/cli/)
- one of [Pulumi's supported language runtimes](/docs/languages-sdks/)

### Create and Configure a New Project

Once the prerequisites are installed, run the `pulumi new <language>` command in an empty folder to [create a new Pulumi project](/docs/cli/commands/pulumi_new/), making sure to replace `<language>` with the supported language of your choice:

```bash
# example using python
$ pulumi new python
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name (pulumi-esc-iac):  
project description (A minimal Python Pulumi program):  
Created project 'pulumi-esc-iac'

Please enter your desired stack name.
To create a stack in an organization, use the format <org-name>/<stack-name> (e.g. `acmecorp/dev`).
stack name (dev): pulumi/dev
Created stack 'dev'

Installing dependencies...

Creating virtual environment...
Finished creating virtual environment
Updating pip, setuptools, and wheel in virtual environment...
...
...
Finished installing dependencies

Your new project is ready to go!

To perform an initial deployment, run `pulumi up`
```

## Access configuration locally

In a Pulumi project, you can locally [store and retrieve configuration values](/docs/concepts/config/) using the `pulumi config set <key> [value]` command. Run the following command to create a config value with a key of `myEnvironment` and a value of `development`:

```bash
$ pulumi config set myEnvironment development
```

This value will be stored in your project's stack settings file `Pulumi.<your-stack-name>.yaml` as shown below:

```yaml
# Contents of Pulumi.<your-stack-name>.yaml file
config:
  pulumi-esc-iac:myEnvironment: development
```

You can retrieve the value of this configuration via the CLI by running the `pulumi config get <key>` command as shown below:

```bash
# example output
$ pulumi config get myEnvironment
development
```

You can also import and access this configuration value from directly within your Pulumi program as shown below:

{{< example-program path="aws-import-export-pulumi-config" >}}

Run the `pulumi preview` command as shown below to validate the retrieval of the configuration:

```bash
$ pulumi preview
Previewing update (dev)

Loading policy packs...

     Type                 Name                Plan
 +   pulumi:pulumi:Stack  pulumi-esc-iac-dev  create

Policies:
    ✅ pulumi-internal-policies@v0.0.6

Outputs:
    Value: "development" # the outputted config value

Resources:
    + 1 to create
```

Defining the configuration via the project stack settings file may be fine when dealing with a singular project, but it can become very challenging to maintain securely and consistently across multiple projects. Centralizing these configuration values using Pulumi ESC provides more scalability without increasing administrative overhead along the way.

## Access configuration from ESC

To centralize this configuration and make it accessible to your Pulumi program, you will need to add a second-level key named `pulumiConfig` in your environment file that will expose the values nested underneath it to Pulumi IaC. Add the following configuration to your environment file:

```yaml
values:
  pulumiConfig:
    myEnvironment: development
```

From here, you will need to import your environment file into your Pulumi project. To do this, return to your `Pulumi.<your-stack-name>.yaml` file and update it to import your environment as shown below, making sure to replace the value of `<your-environment-name>` with the name of your own environment:

```yaml
environment:
  - <your-environment-name>
```

This will import any configuration values that you have defined under the `pulumiConfig` key in your environment file and make them accessible to your Pulumi project.

Save the file and then run the `pulumi config get <key>` command as shown below to quickly test that the import is working:

```bash
# example output
$ pulumi config get myEnvironment
development
```

Now run the `pulumi preview` command again to test that the imported configuration value is accessible from within your Pulumi program:

```bash
$ pulumi preview
Previewing update (dev)

Loading policy packs...

     Type                 Name                Plan
 +   pulumi:pulumi:Stack  pulumi-esc-iac-dev  create

Policies:
    ✅ pulumi-internal-policies@v0.0.6

Outputs:
    Value: "development"

Resources:
    + 1 to create
```

See the Pulumi documentation on [Accessing Configuration from Code](/docs/concepts/config/#code) for more details.

{{< get-started-stepper >}}
