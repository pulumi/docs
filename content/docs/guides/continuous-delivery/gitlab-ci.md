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

GitLab offers [rich capabitilies for CI/CD](https://about.gitlab.com/features/gitlab-ci-cd), enabling you
to easily manage Pulumi stacks using GitOps.

This guide for configuring GitLab Pipelines, will walk you through the steps necessary to manage Pulumi stacks
in response to commits to Git branches. (Commonly referred to as push-to-deploy.)

If you are interested in a deeper integration between GitLab and Pulumi, check out the
[Pulumi GitLab Integration]({{< relref "gitlab-app" >}}), which will surface more detailed information on
your merge requests.

We also detail a more advanced workflow, where you create ephemeral environments (AKA dynamic environments)
for new merge requests. These environments will create and update Pulumi stacks, allowing you to perform ad-hoc
testing or run integration tests. GitLab will automatically tear down these environments when the code is merged,
or after some time.

- [GitLab Pipeline Configuration](#gitlab-pipeline-configuration)
- [Enhanced Merge Requests](#enhanced-merge-requests)
- [Ephemeral Environments](#ephemeral-environments)

> Pulumi doesn't require any particular arrangement of stacks or workflow to be used in GitLab.
> So the steps described should be tailored to your specific application or approach to CI/CD.

## GitLab Pipeline Configuration  {#gitlab-pipeline-configuration}

### Prerequisites

- An account on [https://app.pulumi.com](https://app.pulumi.com) and that you have created a new project.
    - This just means you will sign-in using your GitLab credentials.
    - However, Pulumi can be run from anywhere and your infrastructure code itself can be hosted anywhere.
- The latest CLI. Installation instructions are [here]({{< relref "/docs/get-started/install" >}}).
- A bare repo and set the remote URL to be your GitLab project.

### Stack and Branch Mappings

The scripts below act on a hypothetical stack: `acme/product-catalog-service-stack`.
You can create a stack by running `pulumi stack init`.
The source code for the stack is in a repository in GitLab and uses `TypeScript` as the language.

**Note**: The names used above are purely for demonstration purposes only.
You may choose a naming convention that best suits your organization.

Alternatively, you can also run `pulumi new [template]` to create a template project.
Learn more [here]({{< relref "/docs/reference/cli/pulumi_new" >}}).

### Protected Branches

In order to prevent abuse of protected resources, as well as some sensitive information used
by your repository, GitLab has the concept of [Protected Branches and Tags](https://gitlab.com/help/user/project/protected_branches.md).

If you are running `pulumi` from any branch other than the `master` branch,
you are likely to hit an error that the `PULUMI_ACCESS_TOKEN`
environment variable (introduced later in this document) cannot be accessed.
You can fix this by specifying a wildcard regex to allow specific branches to
be able to access the secret environment variables. Please refer to the GitLab
documentation link above to learn how to do that.

### Merge Request Builds

GitLab has the ability to restrict jobs to _only_ run for merge requests. Learn more [here](https://docs.gitlab.com/ee/ci/merge_request_pipelines/). This is done by adding the following configuration to your GitLab pipeline config file:

```
only:
- merge_requests
```

We will use this to run the `pulumi preview` command only in merge request pipelines.

### Environment Variables

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

### Scripts

Your repository must contain the `.gitlab-ci.yml` in the root. GitLab looks there by default.
If you are using an alternate location, be sure to update the settings for your GitLab project
by going to [https://gitlab.com](https://gitlab.com) > (select your project) > Settings > General.

The following are samples only. You may choose to structure your configuration any way you like.

The `pulumi-preview.sh` script (not shown here) is similar to the `run-pulumi.sh`, except that
it runs the `pulumi preview` command instead of the `pulumi up` command, which is sort of a dry-run
that only shows you changes (if any) in your infrastructure.

#### Sample `.gitlab-ci.yml`

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

#### `setup.sh`

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
# Learn more about pulumi configuration at: {{< absurl "/docs/intro/concepts/config/" >}}
pulumi config set mysetting myvalue
pulumi up --yes
```

## Enhance Merge Requests With Pulumi {#enhanced-merge-requests}

Pulumi now supports enhancing your merge requests with insights into changes to your infrastructure.
Never miss another unintended change with the infrastructure change summary shown inline with the rest of your
merge request notes. Learn how to [configure]({{< relref "gitlab-app" >}}) the integration with Pulumi.

![Merge Request Note](/images/docs/guides/continuous-delivery/gitlab-app/merge_request_note.png)

## Ephemeral Environments  {#ephemeral-environments}

An ephemeral environment referrs to a Pulumi stack that is short-lived, such as only being used for
the duration of a single merge merge request. Automating the creation of ephemeral environments in your
CI/CD can be an extremely useful way to try out new changes, run integration tests, or just get more
confidence that you can still deploy your cloud application.

### Starting `.gitlab-ci.yml`

The following is a simple GitLab Pipelines configuration file, providing the same push-to-deploy behavior
as described earlier. The `production` stack is updated on new pushes to the `master` branch, otherwise
`pulumi preview` is ran to preview the resource changes that would take place if the code were merged.

We will start with this configuration, and then add on the creation of ephemeral environments next. For now
just notice that like before, all interactions with the Pulumi CLI is done through a `scripts/run-pulumi.sh`
file.

```yaml
image: node:14.9-buster

# Folders cached between builds. We want to preserve
# NPM dependencies as well as build outputs.
# http://docs.gitlab.com/ce/ci/yaml/README.html#cache
cache:
  paths:
    - infrastructure/bin/
    - infrastructure/node_modules/

# Build pipeline stages. Use standard build, test, deploy.
# We will update different Pulumi stacks based on the
# current branch/environment.
stages:
    - build
    - test
    - deploy

# =====================================
# Build Stage
# =====================================

build:
    stage: build
    needs: []
    script:
        - echo "=== Build App ==="
        # Build the Pulumi program for deploying the infrastructure.
        - npm install --global typescript
        - cd infrastructure
        - yarn
        - tsc
    when: always

# =====================================
# Test Stage
# =====================================

test:
    stage: test
    needs: ["build"]
    script:
        - echo "=== Test App ==="
    when: always

# =====================================
# Deploy Stage
# =====================================

# Update the production stack on commits to the 'master' branch.
production:update:
    stage: deploy
    script:
        - sh ./scripts/run-pulumi.sh update production
    rules:
        - if: '$CI_COMMIT_BRANCH == "master"'

# Preview changes to the production stack on commits to any other
# branch. (i.e. a feature branch to be merged into master.)
production:preview-changes:
    stage: deploy
    script:
        - sh ./scripts/run-pulumi.sh preview production
    rules:
        - if: '$CI_COMMIT_BRANCH != "master"'
```

### Adding Ephemeral Environments

With the basic workflow enabled, we now can add on the creation of ephemeral environments.

It's actually shockingly simple to configure, thanks to GitLab's built-in support for
[dynamic environments](https://docs.gitlab.com/ee/ci/environments/index.html#configuring-dynamic-environments).

We will introduce two new jobs:

- `ephem-env:update` is what creates or updates the ephemeral environment. It runs on merge requests, and
  is responcible for creating or updating the Pulumi stack powering the environment.
- `ephem-env:tear-down` is executed when the environment is to be shut down. It simply executes `pulumi destroy`
  and `pulumi stack rm` in succession.

Note that we are using the `${CI_COMMIT_REF_SLUG}` environment variable for the Pulumi stack name of
the ephemeral environment. This provides a stable stable identifier, while still being understandable.

```yaml
# =====================================
# Ephemeral Environments Steps
# =====================================

# Create/update an ephemeral environment on merge requests.
ephem-env:update:
    stage: deploy
    script:
        - echo "=== Deploy Ephemeral Environment"
        - sh ./scripts/run-pulumi.sh update ${CI_COMMIT_REF_SLUG}
    environment:
        name: Pulumi stack ${CI_COMMIT_REF_SLUG}
        url: https://app.pulumi.com/acme/product-catalog/${CI_COMMIT_REF_SLUG}
        auto_stop_in: 2 days
        on_stop: ephem-env:tear-down
    only:
        - merge_requests

# Specialized tear down script, so you can manually cleanup any environment.
# Will also be triggered if the ephemeral environment expires.
ephem-env:tear-down:
    stage: deploy
    # Necessary, since the branch may have been deleted.
    variables:
        GIT_STRATEGY: none
    script:
        - echo "=== Tearing Down Ephemeral Environment ==="
        - sh ./scripts/run-pulumi.sh destroy  ${CI_COMMIT_REF_SLUG}
        - sh ./scripts/run-pulumi.sh stack-rm ${CI_COMMIT_REF_SLUG}
    environment:
        name: Pulumi stack ${CI_COMMIT_REF_SLUG}
        action: stop
    when: manual
```

And that's it! There are a few more important details to be aware of, but by
simply adding these two pipeline jobs in enough to start taking advantage of
ephemeral environments!

### Detailing `run-pulumi.sh`

Like before, we need to manage the interactions with the Pulumi CLI. And to do that we rely on a
script called `run-pulumi.sh`. However, a couple of changes are made to support ephemeral environments.

```bash
#!/bin/bash
#
# Invokes Pulumi to create or update a stack.

# Installs the Pulumi CLI. Essentially
# $ curl -fsSL https://get.pulumi.com/ | bash -s
. ./scripts/install-pulumi.sh

# Confirm pulumi is setup correctly.
pulumi login
pulumi whoami --verbose

readonly PULUMI_OPERATION=${1}
readonly STACK_NAME=${2}

# CD to Pulumi project folder.
cd infrastructure

pulumi stack select ${STACK_NAME}
if [ $? -ne 0 ]; then
    echo "Stack '${STACK_NAME}' does not exist. Creating..."
    pulumi stack init ${STACK_NAME}

    # When creating ephemeral environments, we need to use some default
    # configuration values.
    pulumi config set machineSize t2.small
    pulumi config set rootDomain testing.acme-corp.net
fi

# For ephemeral environments, we need to pull down config since it isn't checked
# into the repository.
if [ "${STACK_NAME}" != "production" ]; then
    echo "Downloading configuration data for ephemeral environment..."
    pulumi config refresh
    if [ $? -ne 0 ]; then
        echo "Error pulling previous config. Ignoring, since probably just first-run."
    fi
fi

case "${PULUMI_OPERATION}" in
    "update")
        pulumi up --yes
        ;;
    "preview")
        pulumi preview
        ;;
    "destroy")
        pulumi destroy --yes
        ;;
    "stack-rm")
        pulumi stack rm --yes
        ;;
    *)
        echo "Error: Unrecognized operation '${PULUMI_OPERATION}'"
        exit 1
        ;;
esac

echo "Done"
```

#### Stack Initializatiom

There isn't an easy way to determine if we are updating the ephemeral environment for the first or
the 100th time. So in the script, we attempt to run `pulumi stack select`, and check `pulumi`'s exit code
to determine if the stack exists or not.

The `--create` flag, e.g. `pulumi stack init --create` will create a new stack if it doesn't exist.
However, that doesn't allow you to specify the new stack's configuration data. That's also why in
the example `run-pulumi.sh` script `pulumi config` is called, allowing you to provide any necessary
defaults to configure your Pulumi stack.

#### Configuration Data

And, on the topic of Pulumi stack configuration, this is actually the second obsticale when dealing
with ephemeral environments.

Pulumi configuration data is stored _alongside the code_, in a `Pulumi.<stack-name>.yaml` file rather than online
in the Pulumi Console. This is an important design point, because the configuration for a stack should always follow
its code. (Otherwise there is potential to deploy stack version _X_, but use configuration data for version _Y_.)

However, the configuration data for the ephemeral environment isn't checked-into the repo like it is for other
environments. (Since a CI/CD job making a commit would trigger another CI/CD job, and "bad things would ensue".)

So we take advantage of an obscure Pulumi CLI command here
[`pulumi config reresh`](https://www.pulumi.com/docs/reference/cli/pulumi_config_refresh/).
It simply fetches the last deployed configuration data for a stack. So we use that before running an update.

Once we have selected the right Pulumi stack and fetched its configuration, then it's simply running the right
command be it `pulumi preview`, `pulumi up`, or when we are finished, `pulumi destroy`.
