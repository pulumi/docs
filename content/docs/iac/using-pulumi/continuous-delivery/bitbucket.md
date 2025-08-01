---
title_tag: "Using Bitbucket Pipelines | CI/CD"
meta_desc: This page details how to use Bitbucket Pipelines to manage deploying staging and production stacks based on commits to specific Git branches.
title: Bitbucket Pipelines
h1: Pulumi CI/CD with Bitbucket Pipelines
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Bitbucket Pipelines
        parent: iac-using-pulumi-cicd
        weight: 3
---

[Bitbucket Pipelines](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/) is a CI/CD service built into Bitbucket Cloud. It allows you to build, test, and deploy your code automatically to your Pulumi staging and production stacks based on commits to specific Git branches.

This guide provides examples for integrating Bitbucket Pipelines with a [Pulumi AWS TypeScript project](/docs/iac/get-started/), but the outlined steps can be adapted for other projects in your favorite language.

## Prerequisites

- Sign up for a [Pulumi account](https://app.pulumi.com)
- Create a [Pulumi Access Token](https://app.pulumi.com/account/tokens)
- Install the [latest Pulumi CLI](/docs/install/)
- Create a [Bitbucket account](https://bitbucket.org) with Pipelines enabled
- Create a [new Bitbucket repository](https://support.atlassian.com/bitbucket-cloud/docs/create-a-git-repository/), and ensure you do not initialize it with a README

- Create a [new Pulumi project](/tutorials/pulumi-fundamentals/create-a-pulumi-project/) and [initialize it as a git repository](https://git-scm.com/docs/git-init)

## Setting up environment variables

To use Pulumi within Bitbucket Pipelines, there are a few environment variables you'll need to set.

The first is `PULUMI_ACCESS_TOKEN`, which is required to authenticate with Pulumi in order to
perform the `preview` or `update`.

Next, you will need to set environment variables specific to your cloud resource provider.
For example, if your stack is managing resources on AWS, you will need to set `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY`.

{{% notes type="info" %}}

Add these variables in Bitbucket to your **Repository settings > Repository variables**, ensuring you click on the **Secured** checkbox, as is a security best practice to mark any sensitive variables as protected in Bitbucket. You can learn more about how to protect environment variables by referencing their [variables and secrets](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/) documentation.

{{% /notes %}}

## Bitbucket pipeline configuration

In Bitbucket, a CI/CD pipeline is defined in a yaml file labeled `.bitbucket-pipelines.yml`. This file must exist in the root of your repository and defines how Bitbucket Pipelines will build and deploy your Pulumi stack.

Here's an example configuration:

```yaml
# This is an example Bitbucket starter pipeline configuration
# Use a skeleton to build, test and deploy using manual and parallel steps
# -----
# You can specify a custom docker image from Docker Hub as your build environment.

image: atlassian/default-image:4

pipelines:
  pull-requests:
    '**':
      - step:
          script:
            - if [ "${BITBUCKET_PR_DESTINATION_BRANCH}" != "main" ]; then printf 'target branch not main, skipping preview'; exit; fi
      - step:
          name: 'Run Pulumi Preview'
          image: pulumi/pulumi-nodejs:latest
          script:
            - npm ci
            - pulumi login
            - pulumi stack select $STACK
            - pulumi preview

  branches:
    main:
      - step:
          name: 'Run Pulumi Up'
          image: pulumi/pulumi-nodejs:latest
          script:
            - npm ci
            - pulumi login
            - pulumi stack select $STACK
            - pulumi up --yes

```

When working with Pulumi in Bitbucket Pipelines with Pulumi, you will need to specify when certain actions, like previews, are run.

```yaml
'**':
  - step:
      script:
        - if [ "${BITBUCKET_PR_DESTINATION_BRANCH}" != "main" ]; then printf 'target branch not main, skipping preview'; exit; fi
```

This step and script ensures that the following Pulumi preview step only runs if the pull request is targeting the main branch. This avoids unnecessary previews for pull requests to other branches.

## Running the pipeline

Once the `.bitbucket-pipelines.yml` is committed, each push or pull request to the main branch of the repository will trigger the pipeline, automating the deployment of your infrastructure. You can monitor the pipeline status in the **Pipelines** tab in Bitbucket.
