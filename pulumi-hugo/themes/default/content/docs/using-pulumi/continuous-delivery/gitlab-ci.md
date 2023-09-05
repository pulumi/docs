---
title_tag: "Using GitLab CI | CI/CD"
meta_desc: This page details how to use GitLab CI to manage deploying staging and
           production stacks based on commits to specific Git branches.
title: GitLab CI
h1: Pulumi CI/CD & GitLab
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    usingpulumi:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-gitlab-ci/
- /docs/console/continuous-delivery/gitlab-ci/
- /docs/guides/continuous-delivery/gitlab-ci/
- /docs/using-pulumi/continuous-delivery/cd-gitlab-ci/
- /docs/guides/continuous-delivery/cd-gitlab-ci/
---

[GitLab CI/CD](https://docs.gitlab.com/ee/topics/build_your_application.html) enables the management of deploying
staging and production stacks based on commits to specific Git branches. This is sometimes
referred to as Push-to-Deploy.

Using GitLab with Pulumi is a great way to combine software development and infrastructure
as code (IaC) best practices. Pulumi is built with CI/CD integration in mind because:

- It doesn't require any particular arrangement of stacks or workflow to work in CI/CD processes.
- It can be run from anywhere and your infrastructure code can be hosted anywhere.

The examples provided in this guide were created under the context of a Pulumi TypeScript project with the project code hosted in a GitLab repository,
but the steps described below can be altered to fit into any existing type of deployment setup.

## Prerequisites

- Sign up for a [Pulumi account](https://app.pulumi.com) using your GitLab credentials.
- Create a [Pulumi Access Token](https://app.pulumi.com/account/tokens).
- Install the [latest Pulumi CLI](/docs/install/).
- Create a [blank GitLab project](https://docs.gitlab.com/ee/user/project/) without a README.
- Create a [new Pulumi project](https://www.pulumi.com/learn/pulumi-fundamentals/create-a-pulumi-project/) and [initialize it as a git repository](https://git-scm.com/docs/git-init)
- Set the remote URL of the Pulumi project to be your GitLab project.
  - Ex: `git remote add origin <your-gitlab-repo-url>`

## Environment Variables

To use Pulumi within GitLab CI, there are a few environment variables you'll need to set for each
build.

The first is `PULUMI_ACCESS_TOKEN`, which is required to authenticate with `pulumi.com` in order to
perform the preview or update.

Next, you will also need to set environment variables specific to your cloud resource provider.
For example, if your stack is managing resources on AWS, you will need to set `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY`.

{{% notes type="info" %}}

It is a security best practice to mark any sensitive variables as protected in GitLab. You can learn how
to set and protect environment variables in GitLab by referencing their [variables](https://docs.gitlab.com/ee/ci/variables/) documentation.

{{% /notes %}}

## Protected Branches

In order to prevent abuse of protected resources as well as other sensitive information used
by your repository, GitLab has the concept of [Protected Branches and Tags](https://gitlab.com/help/user/project/protected_branches.md).

Your GitLab repository's `main` or `master` branch is is the only branch that is created as a protected branch by default. If you are running Pulumi CLI commands from any branch other than the `main | master` branch,
you are likely to run into a login error. This is due to the `PULUMI_ACCESS_TOKEN` environment variable only being accessible by protected branches and tags.

You can fix this by configuring branch protection using [wildcard rules](https://docs.gitlab.com/ee/user/project/protected_branches.html#protect-multiple-branches-with-wildcard-rules). Doing this will
allow any branches with names that match this rule the ability to access the secret environment variables.

## Merge Request Builds

GitLab has the ability to restrict jobs to run only on [merge requests](https://docs.gitlab.com/ee/ci/merge_request_pipelines/). This is done by adding the following configuration to your GitLab pipeline config file:

```
only:
- merge_requests
```

The example script provided below will demonstrate how to use this configuration to run the `pulumi preview` command only in merge request pipelines.

## Sample Scripts

In GitLab, a CI/CD pipeline is defined in a yaml file labeled `.gitlab-ci.yml`. This file must exist
in the root of your repository as GitLab looks there by default.

If you are storing this file in an alternate location, be sure to reflect this location in the CI/CD settings of your GitLab project
by going to [https://gitlab.com](https://gitlab.com) > (select your project) > Settings > CI/CD and updating the value of
"CI/CD configuration file" under the "General pipelines" section.

The following are samples only. You may choose to structure your configuration any way you like.

The `pulumi-preview.sh` script (not shown here) is similar to the `run-pulumi.sh` script, except that
it runs the `pulumi preview` command instead of the `pulumi up --yes` command. The preview command performs a dry-run
of your project deployment and only shows you changes (if any) in your infrastructure.

### `.gitlab-ci.yml`

```yaml
#
# This sample yaml configuration file contains two stages and three jobs.
# This configuration uses GitLab's `only`, `when`, and `except` configuration
# options to create a pipeline that will create the `pulumi-preview` job in the pipeline,
# for all branches except the master.
# Only for master branch merges, the main `pulumi` job is executed automatically.
stages:
  - build
  - infrastructure-update

# Each stage may require multiple jobs to complete that stage.
# Consider a build stage, which may require building the UI, service, and a CLI.
# All 3 individual build jobs can be attributed to the build _stage_.
complex_build_job:
  stage: build
  script:
    - echo "pulumi rocks!"

pulumi:
  stage: infrastructure-update
  before_script:
    - chmod +x ./scripts/*.sh
    - ./scripts/setup.sh
  script:
    - ./scripts/run-pulumi.sh
  # Create an artifact archive with just the pulumi log file,
  # which is created using console-redirection in run-pulumi.sh.
  artifacts:
    paths:
    - pulumi-log.txt
    # This is just a sample of how artifacts can be expired (removed) automatically in GitLab.
    # You may choose to not set this at all based on your organization's or team's preference.
    expire_in: 1 week
  # This job should only be created if the pipeline is created for the master (or main) branch.
  only:
  - master # or main

pulumi-preview:
  stage: infrastructure-update
  before_script:
    - chmod +x ./scripts/*.sh
    - ./scripts/setup.sh
  script:
    - ./scripts/pulumi-preview.sh
  only:
  - merge_requests
```

### `setup.sh`

The `setup.sh` installs the `pulumi` CLI on the GitLab CI Runner, and other tools.
It also installs `yarn` and `nodejs` since that's the runtime for this sample project.

```bash
#!/bin/bash

# exit if a command returns a non-zero exit code and also print the commands and their args as they are executed
set -e -x
# Download and install required tools.
# pulumi
curl -fsSL https://get.pulumi.com/ | bash
export PATH=$PATH:$HOME/.pulumi/bin
# Login into pulumi. This will require the PULUMI_ACCESS_TOKEN environment variable
pulumi login
# update the GitLab Runner's packages
apt-get update -y
apt-get install sudo ca-certificates curl gnupg -y
# nodejs
mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
NODE_MAJOR=20
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
apt-get update -y
apt-get install -y nodejs
# yarn
npm i -g yarn
```

### `run-pulumi.sh`

The `run-pulumi.sh` script runs the `pulumi up` command to apply any stack changes and to start
updating your infrastructure.

```bash
#!/bin/bash

# exit if a command returns a non-zero exit code and also print the commands and their args as they are executed
set -e -x

# Add the pulumi CLI to the PATH
export PATH=$PATH:$HOME/.pulumi/bin

yarn install
pulumi stack select product-catalog-service
# The following is just a sample config setting that the hypothetical pulumi
# program needs.
# Learn more about pulumi configuration at: {{< absurl "/docs/concepts/config/" >}}
pulumi config set mysetting myvalue
pulumi up --yes # this line will be the pulumi preview command in pulumi-preview.sh
```

## Enhance Merge Requests With Pulumi

Pulumi now supports enhancing your merge requests with insights into changes to your infrastructure.
Never miss another unintended change with the infrastructure change summary shown inline with the rest of your
merge request notes. Learn how to [configure](/docs/using-pulumi/continuous-delivery/gitlab-app/) the integration with Pulumi.

![Merge Request Note](/images/docs/guides/continuous-delivery/gitlab-app/merge_request_note.png)
