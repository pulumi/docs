---
title: Codefresh
meta_desc: This page will walk you through setting up Codefresh CI/CD with a Pulumi program.
menu:
    userguides:
        parent: cont_delivery
        weight: 1

aliases:
- /docs/reference/cd-codefresh/
- /docs/console/continuous-delivery/codefresh/
---

[Codefresh](https://codefresh.io) is a CI/CD platform designed for containers and microservices. It has built-in support for Docker, Kubernetes and Helm.

Codefresh pipelines are composed by different [steps](https://codefresh.io/docs/docs/codefresh-yaml/steps/) where each step runs inside a Docker container.
Since Pulumi is also released as [Docker container](https://hub.docker.com/r/pulumi/pulumi), it is very easy to use Pulumi in Codefresh pipelines.

## Project setup

First of all follow the instructions for creating a Pulumi stack. There are three ways to do this:

1. [Clone an Existing Example](https://github.com/pulumi/examples)
2. [Use the New Project Wizard](https://app.pulumi.com/site/new-project)
3. [Download the CLI]({{< relref "/docs/get-started/install" >}}) and run `pulumi new` to select a template.

Then [signup for a Codefresh account](https://codefresh.io/docs/docs/getting-started/create-a-codefresh-account/) and [create a pipeline](https://codefresh.io/docs/docs/configure-ci-cd-pipeline/pipelines/). There is no special setup needed on the Codefresh side (i.e. you can use Pulumi on both free and paid Codefresh accounts).

### Environment Variables

To use Pulumi within Codefresh, there are a few environment variables you'll need to set for each
build.

The first is `PULUMI_ACCESS_TOKEN`, which is required to authenticate with pulumi.com in order to
perform the preview or update. You can create a new Pulumi access token specifically for your
CI/CD job on your [Pulumi Account page](https://app.pulumi.com/account/tokens).

You can either add the token on the pipeline itself as a variable, or store it globally using [Codefresh shared configuration](https://codefresh.io/docs/docs/configure-ci-cd-pipeline/shared-configuration/).

![Pulumi token in Codefresh](/images/docs/reference/codefresh/codefresh-pulumi-token.png)

Next, you will also need to set environment variables specific to your cloud resource provider.
For example, if your stack is managing resources on AWS, `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY`.

## Codefresh CI/CD pipeline with Pulumi

In your pipeline you need at least two steps.

1. A step that downloads all Pulumi dependencies according to your programming language
1. A step that performs the actual deployment

In all cases you use a [Codefresh freestyle step](https://codefresh.io/docs/docs/codefresh-yaml/steps/freestyle/) with the Pulumi Docker image.

```yaml
  RunMyPulumiStep:
    title: Running Pulumi inside Codefresh
    image: pulumi/pulumi
    commands:
      # run any pulumi command that you would run locally such as:
      - pulumi login
      - pulumi stack
```

Pulumi will search for a login token named `PULUMI_ACCESS_TOKEN` so assuming that you have setup this variable in the pipeline, Pulumi will not ask for interactive login.

For Kubernetes based deployments, there is no other setup needed. Codefresh is setting up automatically a `kubeconfig` in all freestyle steps which is the same mechanism used by `kubectl` and Pulumi to access Kubernetes clusters. You only need to select your cluster if you have more than one, using a `kubectl config use-context` command prior to running `pulumi`.

For other non-Kubernetes deployments, you need to add additional environment variables in your pipeline that will be used by Pulumi for accessing your cloud provider.

Here is a full example:

 `codefresh.yml`

```yaml
version: '1.0'
stages:
  - prepare
  - build
  - deploy
steps:
  main_clone:
    title: Cloning main repository...
    type: git-clone
    repo: '${{CF_REPO_OWNER}}/${{CF_REPO_NAME}}'
    revision: '${{CF_REVISION}}'
    stage: prepare
    git: github-1
  BuildProject:
    title: Build project
    stage: build
    image: pulumi/pulumi
    commands:
      - yarn install
  SelectMyCluster:
    title: Select K8s cluster
    stage: deploy
    image: codefresh/kubectl:1.13.3
    commands:
      - kubectl config get-contexts
      - kubectl config use-context "kostis-demo@FirstKubernetes"
  RunPulumi:
    title: Deploying
    stage: deploy
    image: pulumi/pulumi
    commands:
      - pulumi login
      - pulumi stack select dev
      # (Optional) Use pulumi stack to get more information in CI/CD logs about the current stack
      - pulumi stack
      - pulumi up --non-interactive
```

This pipeline uses a Kubernetes/Typescript Pulumi stack. Once you run it you should see a new entry in your Pulumi history as well as the deployment in the Codefresh Kubernetes Dashboard.

![Pulumi in Codefresh pipeline](/images/docs/reference/codefresh/pulumi-pipeline.png)

You can find the full more details at the [full documentation page](https://codefresh.io/docs/docs/yaml-examples/examples/pulumi/).

## Previewing pull requests

Codefresh has full support for [branch triggers](https://codefresh.io/docs/docs/configure-ci-cd-pipeline/triggers/git-triggers/) with specific expressions as well as [conditionals](https://codefresh.io/docs/docs/codefresh-yaml/conditional-execution-of-steps/).
You can modify your existing pipeline or add another pipeline with a different trigger that runs `pulumi preview` or any other Pulumi command
in a different scenario.
