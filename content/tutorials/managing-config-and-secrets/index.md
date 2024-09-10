---
title: "Managing Configuration and Secrets"
title_tag: "Managing Configuration and Secrets"
layout: single

# A succinct description of the tutorial. It appears on the Tutorials home and collection pages.
description: Here is a brief description of what this tutorial's all about.

# A similar description used for search results and social-media previews.
meta_desc: Here is a brief description of what this tutorial's all about.

# An image for the tutorial. It appears on tutorial page and in social-media previews.
meta_image: config-secrets-meta.png

# The order in which the tutorial appears in most lists. Order is ascending, so higher numbers
# mean the tutorial will appear further down the list. Positive integers only.
weight: 999

# A brief summary of the tutorial. It appears at the top of the tutorial page. Markdown is fine.
summary: |
    In Pulumi, each stack within your project has a settings file, and this file contains a collection of values intended to capture the configuration details needed to work with a particular environment. These can be plain-text values like server names, environment types (ex: dev, test, prod), region names and so on. They can also be sensitive values such as database passwords or service tokens.
    
    In this tutorial, we'll demonstrate how to create and utilize configuration and secret values in Pulumi.

# A list of three to five things the reader will have learned by the end of the tutorial.
youll_learn:
    - How to create a plain-text configuration value
    - How to create an encrypted secret configuration value
    - How to view configuration details in the CLI
    - How to access configuration values from within Pulumi program code

# A list of tutorial prerequisites. Markdown is fine. Keep it simple; no need to be exhaustive here.
prereqs:
    - The [Pulumi CLI](/docs/install/)
    - A [Pulumi Cloud account](https://app.pulumi.com/signup) and [access token](/docs/pulumi-cloud/accounts/#access-tokens)
    - One of Pulumi’s [supported language runtimes](/docs/languages-sdks/) installed

# The estimated time, in minutes, for new users to complete the topic.
estimated_time: 10

# # An optional list of collections this tutorial should be belong to. Collections are defined in data/tutorials/collections.yaml.
# collections:
#     - some-non-existent-collection
---

## Create a new project

To start, login to the [Pulumi CLI](/docs/cli/commands/pulumi_login/). Next, create a new project by running the `pulumi new <language>` command, making sure to replace `<language>` with the supported language of your choice:

```bash
# example using python
$ pulumi new python
This command will walk you through creating a new Pulumi project.

Enter a value or leave blank to accept the (default), and press <ENTER>.
Press ^C at any time to quit.

project name (pulumi-dev):  
project description (A minimal Python Pulumi program):  
Created project 'pulumi-dev'

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

This will create simple Pulumi program without any resources or configuration details.

## Create configuration values

In a Pulumi project, you can locally [store and retrieve configuration values](/docs/concepts/config/) using the `pulumi config set <key> [value]` command. To demonstrate, run the following command to create a configuration value with a key of `myEnvironment` and a value of `development`:

```bash
$ pulumi config set myEnvironment development
```

This value will be stored in your project's stack settings file `Pulumi.<your-stack-name>.yaml` as shown below:

```yaml
# Contents of Pulumi.<your-stack-name>.yaml file
config:
  pulumi-dev:myEnvironment: development
```

You can also list the configuration values for your stack in the command line. To do so, run the `pulumi config` command:

```bash
$ pulumi config

KEY            VALUE
myEnvironment  development
pulumi:tags    {"pulumi:template":"python"}
```

To retrieve a specific configuration value, run the `pulumi config get <key>` command as shown below:

```bash
$ pulumi config get myEnvironment
development
```

## Create secret values

Pulumi supports encrypting specific values as “secrets” for extra protection. Pulumi Cloud transmits and stores state files over a secure connection, but once received the files are viewable in plain-text. By encrypting secrets, Pulumi ensures that these values never appear as plain-text in your state file. By default, the encryption method uses automatic, per-stack encryption keys provided by Pulumi Cloud, but you can also use a [provider of your own choosing](/docs/concepts/secrets/#configuring-secrets-encryption) instead.

To encrypt a configuration value before runtime, you will need to run the `pulumi config set <key> [value] --secret` command. To demonstrate how this works, you'll create a configuration value named `myPassword`. Run the CLI command `pulumi config set myPassword <value-of-password>`, making sure to pass the `--secret` flag, and also making sure to replace `<value-of-password>` with an actual value as shown below:

```bash
pulumi config set myPassword demo-password-123 --secret
```

Now run the `pulumi config` command again, and you will see that, unlike the value for `myEnvironment`, the value for `myPassword` is hidden:

```bash
$ pulumi config get myEnvironment

KEY            VALUE
myEnvironment  development
myPassword     [secret]
pulumi:tags    {"pulumi:template":"python"}
```

If you open your project's stack settings file (e.g. `Pulumi.<your-stack-name>.yaml`), you will notice that the password value is also encrypted there:

```bash
config:
  generic-python:myEnvironment: development
  generic-python:myPassword:
    secure: AAABADd5YzRaVuzxM08i5z2CJ3LGkQau5e5Lhk+1Gtj37qv6zKkFr8KxmN6X+w/XMg==
```

## Reference values in code

Within your Pulumi program code, configuration values can be retrieved for a given stack using the following:

- `Config.get` or `Config.require` for raw configuration values
- `Config.getSecret` or `Config.requireSecret` for secret values

{{< notes type="info" >}}

You can learn more about the difference between the `get` and `require` functions by referring to the [Pulumi Configuration concept documentation](/docs/concepts/config/#code).

{{< /notes >}}

To demonstrate, update your Pulumi program code with the following:

{{< example-program path="aws-import-export-pulumi-config" >}}

Save your file and then run the `pulumi up` command.

```bash
$ pulumi up -y

     Type                 Name                Status
 +   pulumi:pulumi:Stack  python-dev  created (0.54s)

Outputs:
    ProjectName: "development"
    Password   : [secret]

Resources:
    + 1 created

Duration: 2s
```

You can see that the configuration values were successfully imported into the program and exported as outputs, and you can see that the value of `Password`, which comes from the secret configuration value `myPassword`, is still not visible.

## Clean Up

{{< cleanup >}}

## Next Steps

In this tutorial, you created raw and secret configuration values in your project's stack. You also accessed these values via your Pulumi program code.

To learn more about managing and utilizing configuration and secrets in Pulumi, take a look at the following resources:

- Learn more about more about how to centralize your configuration and secrets in the [Pulumi ESC](/docs/esc/) documentation.
- Learn more about stack outputs and references in the [Stack Outputs and References](/docs/using-pulumi/stack-outputs-and-references/) tutorial.
