---
title_tag: Integrate with Docker | Pulumi ESC
title: Docker
h1: "Pulumi ESC: Integrate with Docker"
meta_desc: This page provides an overview on how to use Pulumi ESC with Docker.
weight: 2
menu:
  pulumiesc:
    parent: esc-other-integrations
    identifier: esc-other-integrations-docker
---

## Overview

Pulumi ESC integrates with [Docker](https://www.docker.com/) to help developers automatically manage configuration and secrets while running `docker` commands.

## Prerequisites

To complete the steps in this tutorial, you will need to install the following prerequisites:

- the [Pulumi ESC CLI](/docs/esc-cli/)
- the [Docker CLI](https://www.docker.com/)

## Manage environment variables for Docker containers

### Set individual environment variables in a Docker container

ESC integrates with `docker` by setting command-line arguments with values from an opened environment. The first step is to create an environment with your desired configuration.

The following environment sets two values that are exported as environment variables:

```yaml
values:
  environmentVariables:
    ESC_ORG: You are in the ${context.pulumi.organization.login} organization!
    ESC_HELLO_USER: Hello, ${context.pulumi.user.login}!
```

You can [set environment variables for a Docker container](https://docs.docker.com/reference/cli/docker/container/run/#env) as part of a `docker run` command:

```bash
$ esc run <your-environment-name> -- docker run --rm -t -e ESC_ORG -e ESC_HELLO_USER alpine env
```

This command opens the environment you just created, sets the specified environment variables, and then uses those environment variables in the context of the `docker run`. In this case, the command
runs an alpine container, prints the container environment, and then exits. The output should look something like this, but with your own username and organization name set in the environment variables.

```bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=e2d74889ef6d
TERM=xterm
ESC_HELLO_USER=Hello, example-user!
ESC_ORG=You are in the example organization!
HOME=/root
```

### Set multiple environment variables in a Docker container from an env-file

Instead of setting each environment variable explicitly, you also have the option of using an env-file to set variables in your container environment. Here, we extend the environment definition from the
previous example to include a value in the `files` section. When the environment is opened, the value is copied to a temporary file on your system, with the path set as an environment variable with
the key name.

```yaml
values:
    environmentVariables:
        ESC_ORG: You are in the ${context.pulumi.organization.login} organization!
        ESC_HELLO_USER: Hello, ${context.pulumi.user.login}!
    files:
        DOCKER_ENVFILE: |
            ESC_ORG=${environmentVariables.ESC_ORG}
            ESC_HELLO_USER=${environmentVariables.ESC_HELLO_USER}
```

If you open this environment in a terminal, you will see something like this:

```bash
$ esc open pulumi/docker-env-test --format shell

export ESC_HELLO_USER="Hello, example-user!"
export ESC_ORG="You are in the example organization!"
export DOCKER_ENVFILE="/var/folders/ny/f_y5fsqd235fpx5bs6ghyk4w0000gn/T/esc-1312668514"
```

The temporary file contains the value specified in your environment:

```bash
$ cat /var/folders/ny/f_y5fsqd235fpx5bs6ghyk4w0000gn/T/esc-1312668514

ESC_ORG=You are in the example organization!
ESC_HELLO_USER=Hello, example-user!
```

Now you can reference this env-file to set environment variables dynamically in a `docker run` command:

```bash
$ esc run -i <your-environment-name> -- sh -c 'docker run --rm -t --env-file=$DOCKER_ENVFILE alpine env'
```

This command opens the environment you just created and references the path of the temporary env-file to set environment variables in the context of the `docker run`. In this case, the command
runs an alpine container, prints the container environment, and then exits. The output should look something like this, but with your own username and organization name set in the environment variables.

```bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOSTNAME=e2d74889ef6d
TERM=xterm
ESC_HELLO_USER=Hello, example-user!
ESC_ORG=You are in the example organization!
HOME=/root
```

## Manage Docker registry credentials

### Create an ESC environment with your Docker registry credentials

ESC integrates with `docker` by setting command-line arguments with values from an opened environment. You can store login configuration securely with an ESC environment.
This example stores the username and encrypted password directly in the environment, but you can also reference external secrets with [ESC providers](/docs/esc/providers/).

```yaml
values:
  docker:
    username: <your-registry-username>
    password:
      fn::secret: <your-registry-password>
    registry: null # Provide a registry URL if you are not using Docker Hub
```

### Log in to a Docker registry

Now, you can [log into a Docker registry](https://docs.docker.com/reference/cli/docker/login/) without needing to manage the credentials directly in your shell:

```bash
$ esc run <your-environment-name> -- sh -c 'echo ${docker.password} | docker login --username ${docker.username} --password-stdin ${docker.registry}'

Login Succeeded
```
