---
title: GitLab CI
meta_desc: This page details how to use GitLab CI to manage deploying staging and
           production stacks based on commits to specific Git branches.
menu:
    userguides:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-gitlab-ci/
- /docs/console/continuous-delivery/gitlab-ci/
---

[This](https://about.gitlab.com/features/gitlab-ci-cd/) page details how to use GitLab CI to manage deploying
staging and production stacks based on commits to specific Git branches. This is sometimes
referred to as Push-to-Deploy.

Pulumi doesn't require any particular arrangement of stacks or workflow to work in a
continuous integration / continuous deployment system. So the steps described here can be
altered to fit into any existing type of deployment setup.

## Prerequisites

- An account on [https://app.pulumi.com](https://app.pulumi.com) and that you have created a new project.
    - This just means you will sign-in using your GitLab credentials.
    - However, pulumi can be run from anywhere and your infrastrucutre code itself can be hosted anywhere.
- The latest CLI. Installation instructions are [here]({{< relref "/docs/get-started/install" >}}).
- A bare repo and set the remote URL to be your GitLab project.

## Stack and Branch Mappings

The scripts below act on a hypothetical stack: `acme/product-catalog-service-stack`.
You can create a stack by running `pulumi stack init`.
The source code for the stack is in a repository in GitLab and uses `TypeScript` as the language.

**Note**: The names used above are purely for demonstration purposes only.
You may choose a naming convention that best suits your organization.

Alternatively, you can also run `pulumi new [template]` to create a template project.
Learn more [here]({{< relref "/docs/reference/cli/pulumi_new.md" >}}).

## GitLab CI Runners

## Protected Branches

In order to prevent abuse of protected resources, as well as some sensitive information used
by your repository, GitLab has the concept of [Protected Branches and Tags](https://gitlab.com/help/user/project/protected_branches.md).

If you are running `pulumi` from any branch other than the `master` branch,
you are likely to hit an error that the `PULUMI_ACCESS_TOKEN`
environment variable (introduced later in this document) cannot be accessed.
You can fix this by specifying a wildcard regex to allow specific branches to
be able to access the secret environment variables. Please refer to the GitLab
documentation link above to learn how to do that.

## Merge Request Builds

GitLab has the ability to restrict jobs to _only_ run for merge requests. Learn more [here](https://docs.gitlab.com/ee/ci/merge_request_pipelines/). This is done by adding the following configuration to your GitLab pipeline config file:

```
only:
- merge_requests
```

We will use this to run the `pulumi preview` command only in merge request pipelines.

## Environment Variables

To use Pulumi within GitLab CI, there are a few environment variables you'll need to set for each
build.

The first is `PULUMI_ACCESS_TOKEN`, which is required to authenticate with pulumi.com in order to
perform the preview or update. You can create a new Pulumi access token specifically for your
CI/CD job on your [Pulumi Account page](https://app.pulumi.com/account/tokens).

Next, you will also need to set environment variables specific to your cloud resource provider.
For example, if your stack is managing resources on AWS, `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY`.

**Note**: It is a good security practice to mark any sensitive variables as protected in GitLab.
Please read the note about **Protected Branches** above.

## Scripts

Your repository must contain the `.gitlab-ci.yml` in the root. GitLab looks there by default.
If you are using an alternate location, be sure to update the settings for your GitLab project
by going to [https://gitlab.com](https://gitlab.com) > (select your project) > Settings > General.

The following are samples only. You may choose to structure your configuration any way you like.

The `pulumi-preview.sh` script (not shown here) is similar to the `run-pulumi.sh`, except that
it runs the `pulumi preview` command instead of the `pulumi up` command, which is sort of a dry-run
that only shows you changes (if any) in your infrastructure.

### Sample `.gitlab-ci.yml`

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
  # This job should only be created if the pipeline is created for the master branch.
  only:
  - master

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
apt-get install sudo -y
# nodejs
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
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
# Learn more about pulumi configuration at: {{< absurl "/reference/config/" >}}
pulumi config set mysetting:myvalue
pulumi up
```
