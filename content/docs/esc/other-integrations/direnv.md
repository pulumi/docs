---
title_tag: Integrate with Direnv | Pulumi ESC
title: Direnv
h1: "Pulumi ESC: Integrate with Direnv"
meta_desc: This page provides an overview on how to use Pulumi ESC with Direnv.
weight: 2
menu:
  pulumiesc:
    parent: esc-other-integrations
    identifier: esc-other-integrations-direnv
---

## Overview

Pulumi ESC integrates with [Direnv](https://direnv.net) to help developers automatically load configuration and secrets into their shell.

## Prerequisites

To complete the steps in this tutorial, you will need to install the following prerequisites:

- the [Pulumi ESC CLI](/docs/esc-cli/)
- the [Direnv CLI](https://direnv.net) and shell integration

## Create an ESC environment with environment variables

ESC integrates with `direnv` by exporting environment variables from an opened environment. Before you can configure `direnv`, you'll need to create an environment that exports environment variables. For example, the environment below fetches AWS credentials via OIDC and exports these credentials in environment variables:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: <your-oidc-iam-role-arn>
          sessionName: pulumi-environments-session
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

For the purposes of this guide, we'll create an environment that exports a single variable:

```yaml
values:
  environmentVariables:
    ESC_HELLO: Hello, ${context.pulumi.organization.login}!
```

## Create a .envrc file

Before each prompt, `direnv` checks for the existence of a `.envrc` file in the current directory and its ancestors. If a `.envrc` file is found, `direnv` executes it using `bash` and makes its exported variables available to the current shell. When you exit the directory that contains the loaded `.envrc` file, `direnv` unloads its variables.

To open an ESC environment and export its environment variables, create a `.envrc` file with the following contents:

```bash
eval $(esc open <your-environment-name> --format shell)
```

Once you've created this file, `direnv` may warn you that it cannot load the `.direnv` file for security reasons:

```bash
direnv: error /path/to/.envrc is blocked. Run `direnv allow` to approve its content
```

In order to allow `direnv` to load the file, run `direnv allow`:

```bash
$ direnv allow /path/to/.envrc
```

This should allow `direnv` to load the file and export its environment variables. For the example environment above, you should see the following:

```bash
direnv: loading /path/to/.envrc
direnv: export +ESC_HELLO
```

You can then retrieve the value of the environment variable:

```bash
$ echo $ESC_HELLO
Hello, <your-pulumi-login>!
```

{{< get-started-stepper >}}
