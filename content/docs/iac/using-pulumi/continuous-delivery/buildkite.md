---
title_tag: "Using Buildkite | CI/CD"
meta_desc: This page details how to use Buildkite pipelines to deploy infrastructure implemented using Pulumi.
title: Buildkite
h1: Pulumi CI/CD with Buildkite
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Buildkite
        parent: iac-using-pulumi-cicd
        weight: 2
---

[Buildkite](https://buildkite.com/) is a continuous intergration and delivery platform designed to scale with your projects. This guide shows you how to install, configure, and run Pulumi in a Buildkite pipeline.

## Prerequisites

- Sign up for a [Pulumi account](https://app.pulumi.com)
- Create a [Pulumi Access Token](https://app.pulumi.com/account/tokens)
  - Save this token as a [pipeline secret](https://buildkite.com/docs/pipelines/security/secrets/buildkite-secrets)
named `PULUMI_ACCESS_TOKEN`.
- Install the [latest Pulumi CLI](/docs/install/), so you can run the project locally as a test
- Create a new GitHub [repository](https://github.com/new)
- Create a [new Pulumi project](/tutorials/pulumi-fundamentals/create-a-pulumi-project/) and [initialize it as a git repository](https://git-scm.com/docs/git-init)
- Obtain credentials for the cloud provider your Pulumi project will use and store them as pipeline secrets similar to the Pulumi access token from the previous step.
  - Some cloud providers support OIDC token exchange. See [OIDC in Buildkite Pipelines](https://buildkite.com/docs/pipelines/security/oidc).
- A Buildkite cluster and agent. Follow the [Getting Started](https://buildkite.com/docs/pipelines/getting-started) guide to complete setup.

## Install and Configure Pulumi

Pipeline steps can be defined in Buildkite directly or stored in a YAML file in your
source repo. Defining steps in a YAML file will give you access to more configuration
options than the web interface.

1. In your source repository, create the `.buildkite` folder in the root. The Buildkite agent will look for a pipeline
configuration file [in a few places](https://buildkite.com/docs/agent/v3/cli-pipeline#uploading-pipelines-description). You may also choose one of the other locations to store your config.
1. Create a new file called `pipeline.yml` and paste the following pipeline configuration into the file.

**Note**: The pipeline assumes you are using the Node.js Pulumi SDK for your cloud infrastructure
but you can, of course, use any of the languages supported by Pulumi.

```yaml
env:
  PULUMI_STACK: dev

steps:
  - label: ":pulumi: Preview"
    commands:
      - npm install
      - pulumi preview -s $PULUMI_STACK | tee preview
      - printf '```\n%b\n```\n' "$(cat preview)" | buildkite-agent annotate --style "info"
    plugins:
      - secrets:
        variables:
          # Map the PULUMI_ACCESS_TOKEN secret to an env var of the same name.
          # If you are using OIDC, this won't be needed.
          PULUMI_ACCESS_TOKEN: PULUMI_ACCESS_TOKEN
          #
          # NOTE: Don't forget to map cloud provider credentials as env vars
          # also unless you are using OIDC with the cloud provider too.
          # AWS_ACCESS_KEY_ID: AWS_ACCESS_KEY_ID
          # AWS_SECRET_ACCESS_KEY: AWS_SECRET_ACCESS_KEY

      - pulumi#v1.0.0:
        # Optional: The specific version to install
        # if you don't want to use the latest
        # available version.
        #
        # version: 3.183.0
        #
        # Optional: Use self-managed backend URL instead of (default) Pulumi Cloud.
        # backend-url: s3://bucket_name/project_name/stack_name
        #
        # Optional: Use OIDC auth with Pulumi Cloud.
        # use-oidc: true
        # audience: urn:pulumi:org:{INDIVIDUAL_OR_ORG_LOGIN_NAME}
        # pulumi-token-type: urn:pulumi:token-type:access_token:personal
        # pulumi-token-scope: "user:{USER_LOGIN}"
```

Use of the `pulumi` [plugin](https://buildkite.com/resources/plugins/buildkite-plugins/pulumi-buildkite-plugin/) is optional.
However, if you are using OIDC auth with Pulumi, you might consider using the plugin since it handles the OIDC token exchange
with Pulumi Cloud.

Another option to consider is to use one of Pulumi's official container [images](https://github.com/pulumi/pulumi-docker-containers) for the language
you're using. Pulumi container images have the Pulumi CLI pre-installed along with the language runtime needed to run your programs.
The following example shows how you can use one of those images (or even a custom one.)

```yaml
env:
  PULUMI_STACK: dev

steps:
  - label: ":pulumi: Preview"
    commands:
      - npm install
      - pulumi preview -s $PULUMI_STACK | tee preview
      - printf '```\n%b\n```\n' "$(cat preview)" | buildkite-agent annotate --style "info"
    plugins:
      - secrets:
          variables:
            # Map the PULUMI_ACCESS_TOKEN secret to an env var of the same name.
            # If you are using OIDC, this won't be needed.
            PULUMI_ACCESS_TOKEN: PULUMI_ACCESS_TOKEN
            #
            # NOTE: Don't forget to map cloud provider credentials as env vars
            # also unless you are using OIDC with the cloud provider too.
            # AWS_ACCESS_KEY_ID: AWS_ACCESS_KEY_ID
            # AWS_SECRET_ACCESS_KEY: AWS_SECRET_ACCESS_KEY

      - docker#v5.9.0:
          image: "pulumi/pulumi-nodejs"
          mount-buildkite-agent: true
          environment:
            - PULUMI_ACCESS_TOKEN
            #
            # NOTE: Don't forget to map cloud provider credentials as env vars
            # also unless you are using OIDC with the cloud provider too.
            # - AWS_ACCESS_KEY_ID
            # - AWS_SECRET_ACCESS_KEY
```

Create a pull request trigger by editing the [GitHub settings](https://buildkite.com/docs/pipelines/source-control/github#running-builds-on-pull-requests) in the pipeline.
See Buildkite docs on [source control](https://buildkite.com/docs/pipelines/source-control) for other VCS.

Similarly, create a pipeline config YAML that runs `pulumi up` when a commit is pushed to your default branch.

```yaml
env:
  PULUMI_STACK: xxx

steps:
  - label: ":pulumi: Up"
    commands:
      - npm install
      - pulumi up -s $PULUMI_STACK
    plugins:
      # Use pulumi plugin or the Docker plugin to ensure Pulumi is installed.
      ...
```

## Next Steps

This guide covered a simple way of running Pulumi in a Buildkite pipeline.
As your Pulumi project grows and you add more stacks to a project, you
can make the stack name dynamic (the `PULUMI_STACK` env var in the examples
above) and run a pipeline for a specific stack based on a branch.

### Dynamic Pipelines

Buildkite allows you to create [dynamic pipelines](https://buildkite.com/docs/pipelines/configure/dynamic-pipelines).
Similar to Pulumi, Buildkite, too, allows you to use a [programming language](https://buildkite.com/docs/pipelines/configure/dynamic-pipelines/sdk)
to generate pipeline configurations dynamically at build time.

### Cache Volumes

[Cache volumes](https://buildkite.com/docs/pipelines/hosted-agents/cache-volumes) are
external volumes attached to hosted agent instances. They can be used to cache Pulumi
plugins that get installed in `$HOME/.pulumi/plugins`, as well as any language-specific
packages, i.e. `node_modules` etc. Pulumi plugin binary versions are 1:1 with the
versions of the Pulumi packages that use them.
