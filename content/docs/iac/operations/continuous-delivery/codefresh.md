---
title_tag: "Using Codefresh with Pulumi | CI/CD"
meta_desc: Run Pulumi in Codefresh pipelines to preview and deploy infrastructure changes through a trunk-based continuous delivery workflow.
title: Codefresh
h1: Using Codefresh with Pulumi
menu:
    iac:
        name: Codefresh
        parent: iac-operations-cicd
        weight: 70
aliases:
- /docs/iac/guides/continuous-delivery/codefresh/
- /docs/iac/using-pulumi/continuous-delivery/codefresh/
- /docs/reference/cd-codefresh/
- /docs/console/continuous-delivery/codefresh/
- /docs/guides/continuous-delivery/codefresh/
- /docs/using-pulumi/continuous-delivery/codefresh/
- /docs/iac/packages-and-automation/continuous-delivery/codefresh/
---

[Codefresh](https://codefresh.io) is a CI/CD platform for Kubernetes and Argo CD, now part of Octopus Deploy. Its CI pipelines run each step as a container, so you run Pulumi in a pipeline step that uses the official [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) container image. That image ships the Pulumi CLI and every language runtime, so the same pipeline works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/) and targeting [any cloud provider](/registry/) Pulumi supports.

{{% notes type="info" %}}
This guide assumes Pulumi Cloud as the [state backend](/docs/iac/concepts/state-and-backends/). Pulumi can also run in CI/CD with a self-managed backend, but Pulumi Cloud is assumed throughout because it simplifies pipeline authentication and is the most common choice.
{{% /notes %}}

{{< pulumi-docker-images-note >}}

## How Pulumi works with Codefresh

To apply infrastructure changes, Pulumi runs your program with the Pulumi CLI. A Codefresh [freestyle step](https://codefresh.io/docs/docs/pipelines/steps/freestyle/) provides that environment: it runs a set of commands inside a container image you choose. Point the step at `pulumi/pulumi` and it can run any `pulumi` command — `install`, `preview`, `up` — exactly as you would on your own machine.

No special setup is required on the Codefresh side, and Pulumi runs on both free and paid accounts. You wire up authentication through pipeline variables, described below.

{{% notes type="info" %}}
Codefresh's GitOps offering is built on Argo CD. If you deploy with Argo CD rather than Codefresh CI pipelines, see the [Argo CD guide](/docs/iac/operations/continuous-delivery/argocd/) and the [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/).
{{% /notes %}}

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A [Codefresh account](https://codefresh.io/docs/docs/getting-started/create-a-codefresh-account/) with a [pipeline](https://codefresh.io/docs/docs/pipelines/pipelines/) connected to your Git repository.
1. A Pulumi program in that repository. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Authenticate with Pulumi Cloud

When your pipeline uses Pulumi Cloud as its backend, it needs only a single [Pulumi access token](/docs/administration/access-identity/access-tokens/) to operate. Pulumi reads the token from the `PULUMI_ACCESS_TOKEN` environment variable and authenticates without an interactive login.

Store the token outside of source control. Add it as an encrypted variable on the pipeline itself, or — to reuse it across pipelines — create a [shared configuration](https://codefresh.io/docs/docs/pipelines/configuration/shared-configuration/) context and import it. Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the pipeline's identity isn't tied to an individual.

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a pipeline or a developer's machine, a single environment definition works in both places.

You can remove the static token entirely with [OpenID Connect (OIDC)](/docs/administration/access-identity/oidc-issuers/): the pipeline exchanges a short-lived OIDC token issued by Codefresh for a temporary Pulumi access token, so no long-lived credential is stored anywhere.

## Provide cloud credentials

When Pulumi runs, your program also needs credentials for the cloud provider it manages. You can supply them in one of two ways:

- **Pulumi ESC (recommended).** Configure an [ESC environment](/docs/esc/) to broker short-lived cloud credentials through OIDC. Your program receives temporary credentials scoped to exactly what it needs, and the pipeline stores nothing but its Pulumi access token.
- **Pipeline variables.** Set the provider's credentials as encrypted pipeline variables — for example, `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for AWS — and expose them to the freestyle step.

{{% notes type="warning" %}}
Never commit cloud credentials or the Pulumi access token to your repository. Keep them in encrypted pipeline variables or a shared secret context so the values stay protected and access is auditable.
{{% /notes %}}

## Configure a Codefresh pipeline

A Codefresh pipeline is defined in a `codefresh.yml` file. The following pipeline clones your repository and runs Pulumi against a [stack](/docs/iac/concepts/stacks/):

```yaml
version: '1.0'
stages:
  - clone
  - deploy
steps:
  clone:
    title: Clone repository
    type: git-clone
    stage: clone
    repo: '${{CF_REPO_OWNER}}/${{CF_REPO_NAME}}'
    revision: '${{CF_REVISION}}'
  deploy:
    title: Deploy with Pulumi
    type: freestyle
    stage: deploy
    image: pulumi/pulumi
    working_directory: '${{clone}}/infra'
    environment:
      - PULUMI_ACCESS_TOKEN=${{PULUMI_ACCESS_TOKEN}}
    commands:
      - pulumi install
      - pulumi stack select acme/website/staging
      - pulumi up --yes
```

The example assumes a Pulumi program in an `infra/` directory. [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) installs the program's language dependencies and required plugins, so the same step works for a program written in any supported language.

## Build a trunk-based CI/CD workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/operations/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there. Codefresh [Git triggers](https://codefresh.io/docs/docs/pipelines/triggers/git-triggers/) distinguish pull request, branch, and tag events, so you can map each stage of the workflow to its own trigger.

### Preview infrastructure changes in a pull request

When a pull request is opened, run a dry run instead of a deployment. Attach a Git trigger that fires on pull request events and have the freestyle step run [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/):

```yaml
    commands:
      - pulumi install
      - pulumi stack select acme/website/staging
      - pulumi preview
```

`pulumi preview` reports the proposed changes without modifying any resources, giving reviewers a summary of what the merge would do. To let reviewers exercise the change in a live environment, use a [Review Stack](/docs/deployments/concepts/review-stacks/), which provisions an ephemeral stack for the pull request and destroys it when the pull request closes.

### Deploy to staging on merge to the main branch

When a pull request merges, run [`pulumi up`](/docs/iac/cli/commands/pulumi_up/) against an environment that receives continuous delivery, such as a shared development or staging environment. Attach a Git trigger that fires on pushes to the main branch:

```yaml
    commands:
      - pulumi install
      - pulumi stack select acme/website/staging
      - pulumi up --yes
```

### Promote to production with a git tag

Production updates should be deliberate. Keep production on its own stack and deploy it only when you push a release tag — for example, a moving `production` tag that you advance to a commit already validated in staging:

```yaml
    commands:
      - pulumi install
      - pulumi stack select acme/website/production
      - pulumi up --yes
```

Configure this pipeline's Git trigger to fire on tag push events rather than branch pushes. Promotion then becomes a single, traceable Git operation, and production never deploys from an untested commit.

## Additional resources

- [Continuous delivery](/docs/iac/operations/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [CI/CD troubleshooting guide](/docs/iac/operations/continuous-delivery/troubleshooting/) — diagnose common failures when running Pulumi in a pipeline.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [OIDC Issuers](/docs/administration/access-identity/oidc-issuers/) — eliminate static tokens with short-lived, exchanged credentials.
- [Review Stacks](/docs/deployments/concepts/review-stacks/) — ephemeral environments for pull requests.
- [Argo CD](/docs/iac/operations/continuous-delivery/argocd/) — deploy Pulumi stacks with Argo CD, which underpins Codefresh GitOps.
