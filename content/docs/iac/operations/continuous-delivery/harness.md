---
title_tag: "Using Harness with Pulumi | CI/CD"
meta_desc: Run Pulumi in Harness CI with standard pipeline steps, authenticate with Pulumi Cloud, and ship infrastructure through a trunk-based CI/CD workflow.
title: Harness
h1: Using Harness with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/iac/guides/continuous-delivery/harness/
- /docs/iac/using-pulumi/continuous-delivery/harness/
menu:
    iac:
        name: Harness
        parent: iac-operations-cicd
        weight: 110
---

[Harness](https://www.harness.io/) is a software delivery platform whose CI module runs pipelines defined as stages of steps. A pipeline can live in Harness itself or in your Git repository through [Git Experience](https://developer.harness.io/docs/platform/git-experience/git-experience-overview/).

You run Pulumi in Harness with standard [`Run` steps](https://developer.harness.io/docs/continuous-integration/use-ci/run-step-settings/) that invoke the Pulumi CLI. Because the CLI drives every operation, this works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/) and targeting [any cloud provider](/registry/) Pulumi supports.

{{< cicd-cloud-note >}}

{{< pulumi-docker-images-note >}}

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A Harness account with the CI module enabled and a project connected to your Git repository.
1. A Pulumi program committed to that repository. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Authenticate with Pulumi Cloud

When your pipeline uses Pulumi Cloud as its backend, it needs only a single [Pulumi access token](/docs/administration/access-identity/access-tokens/) to operate. Add the token as a Harness [secret](https://developer.harness.io/docs/platform/secrets/add-use-text-secrets/) and reference it from a step's environment variables — the examples below read it from a secret named `pulumi_access_token` into `PULUMI_ACCESS_TOKEN`. Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the pipeline's identity isn't tied to an individual.

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a Harness pipeline or a developer's machine, a single environment definition works in both places — you don't store separate cloud provider keys as Harness secrets.

To remove the static token entirely, Harness can act as an OIDC issuer, and Pulumi Cloud can register any third-party issuer as a trusted [OIDC Issuer](/docs/administration/access-identity/oidc-issuers/). A pipeline then exchanges a short-lived OIDC token for a Pulumi access token at runtime instead of storing one. See [OIDC Issuers](/docs/administration/access-identity/oidc-issuers/) for the Pulumi Cloud side of the setup, and the Harness documentation for issuing OIDC tokens from a pipeline.

## Build a trunk-based CI/CD workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/operations/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there.

The pipeline below maps each stage of that model to its own CI stage, gated by a `when` condition on the [build type](https://developer.harness.io/docs/continuous-integration/use-ci/codebase-configuration/built-in-cie-codebase-variables-reference/):

1. **Open a pull request.** The `preview` stage runs on pull requests and reports the proposed changes with `pulumi preview`.
1. **Merge to the main branch.** The `deploy-staging` stage runs on pushes to `main` and deploys the change to a staging environment with `pulumi up`.
1. **Promote to production.** Pushing a `release-*` tag runs the `deploy-production` stage, which deploys to production.

Each `Run` step uses the official [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) container image, which bundles the Pulumi CLI and every language runtime, so the same step works regardless of your program's language. Pin the image to a specific version, as the examples do, so builds stay reproducible. The examples assume a Pulumi program in an `infra/` directory and stacks named `acme/website/staging` and `acme/website/production`:

```yaml
pipeline:
  name: Pulumi
  identifier: pulumi
  projectIdentifier: my_project
  orgIdentifier: default
  properties:
    ci:
      codebase:
        connectorRef: my_git_connector
        repoName: website
        build: <+input>
  stages:
    # Pull request: preview the proposed changes.
    - stage:
        name: Preview
        identifier: preview
        type: CI
        spec:
          cloneCodebase: true
          platform:
            os: Linux
            arch: Amd64
          runtime:
            type: Cloud
            spec: {}
          execution:
            steps:
              - step:
                  type: Run
                  name: Pulumi preview
                  identifier: pulumi_preview
                  spec:
                    shell: Bash
                    image: pulumi/pulumi:3.242.0
                    envVariables:
                      PULUMI_ACCESS_TOKEN: <+secrets.getValue("pulumi_access_token")>
                    command: |-
                      pulumi login
                      pulumi install --cwd infra/
                      pulumi preview --cwd infra/ --stack acme/website/staging
        when:
          pipelineStatus: Success
          condition: <+codebase.build.type> == "PR"

    # Merge to main: deploy to the staging environment.
    - stage:
        name: Deploy staging
        identifier: deploy_staging
        type: CI
        spec:
          cloneCodebase: true
          platform:
            os: Linux
            arch: Amd64
          runtime:
            type: Cloud
            spec: {}
          execution:
            steps:
              - step:
                  type: Run
                  name: Pulumi up
                  identifier: pulumi_up_staging
                  spec:
                    shell: Bash
                    image: pulumi/pulumi:3.242.0
                    envVariables:
                      PULUMI_ACCESS_TOKEN: <+secrets.getValue("pulumi_access_token")>
                    command: |-
                      pulumi login
                      pulumi install --cwd infra/
                      pulumi up --yes --cwd infra/ --stack acme/website/staging
        when:
          pipelineStatus: Success
          condition: <+codebase.build.type> == "branch" && <+codebase.branch> == "main"

    # Release tag: promote to production.
    - stage:
        name: Deploy production
        identifier: deploy_production
        type: CI
        spec:
          cloneCodebase: true
          platform:
            os: Linux
            arch: Amd64
          runtime:
            type: Cloud
            spec: {}
          execution:
            steps:
              - step:
                  type: Run
                  name: Pulumi up
                  identifier: pulumi_up_production
                  spec:
                    shell: Bash
                    image: pulumi/pulumi:3.242.0
                    envVariables:
                      PULUMI_ACCESS_TOKEN: <+secrets.getValue("pulumi_access_token")>
                    command: |-
                      pulumi login
                      pulumi install --cwd infra/
                      pulumi up --yes --cwd infra/ --stack acme/website/production
        when:
          pipelineStatus: Success
          condition: <+codebase.build.type> == "tag" && <+codebase.tag>.startsWith("release-")
```

`pulumi install` installs the program's language dependencies and required plugins, and `pulumi up --yes` applies changes non-interactively, with no confirmation prompt.

To run this pipeline automatically, add two Harness [triggers](https://developer.harness.io/docs/platform/triggers/triggering-pipelines/) on your repository: a **pull request** trigger and a **push** trigger. The push trigger fires for both branch pushes and tag pushes; the per-stage `when` conditions then route each event to the correct stage. To promote a release, push a tag that matches the `release-*` pattern:

```bash
git tag release-2026-05-20
git push origin release-2026-05-20
```

Keeping production on its own stack and deploying it only from a tag makes each production update a single, traceable Git operation, and ensures production never deploys from an untested commit. To require human sign-off before a production deployment, add a [`HarnessApproval` step](https://developer.harness.io/docs/platform/approvals/adding-harness-approval-stages/) ahead of the `pulumi up` step in the `Deploy production` stage.

For an optional ephemeral environment on each pull request, pair the `preview` stage with a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions and tears down a per-pull-request environment automatically.

{{% notes type="info" %}}
If you already maintain Pulumi workflows for GitHub Actions, Harness CI can run them directly: its [GitHub Action step](https://developer.harness.io/docs/continuous-integration/use-ci/use-drone-plugins/ci-github-action-step/) executes a published action such as [`pulumi/actions`](https://github.com/pulumi/actions) as a pipeline step.
{{% /notes %}}

## Speed up builds with caching

A clean CI worker starts with an empty plugin cache, so Pulumi re-downloads its provider plugins on every run. Cache the Pulumi plugin directory (`~/.pulumi/plugins`) to avoid that.

On Harness Cloud, enable [Cache Intelligence](https://developer.harness.io/docs/continuous-integration/use-ci/caching-ci-data/cache-intelligence/) on the stage and add the plugin directory to its cached paths:

```yaml
spec:
  cloneCodebase: true
  caching:
    enabled: true
    paths:
      - "~/.pulumi/plugins"
```

On self-managed build infrastructure, use the [`Save Cache`/`Restore Cache` steps](https://developer.harness.io/docs/category/share-and-cache-ci-data) to store the same directory in an [S3](https://developer.harness.io/docs/continuous-integration/use-ci/caching-ci-data/saving-cache/) or [GCS](https://developer.harness.io/docs/continuous-integration/use-ci/caching-ci-data/save-cache-in-gcs/) bucket.

The most deterministic option is to bake the plugins into a custom builder image: derive it from `pulumi/pulumi`, `pulumi plugin install` the providers your program uses, and reference that image from the `Run` step instead of `pulumi/pulumi`. See the [plugins documentation](/docs/iac/concepts/plugins/) for details.

## Report results on pull requests

When the `preview` stage runs `pulumi preview` on a pull request, you'll want the proposed changes summarized on the pull request itself rather than buried in the pipeline logs.

Pulumi offers native [version control integrations](/docs/integrations/version-control/) for popular version control systems. Independently of which CI/CD system runs Pulumi, a version control integration lets Pulumi Cloud post infrastructure-change summaries as pull request comments and status checks, and link each stack update back to the commit and pull request that produced it. See the [Version Control](/docs/integrations/version-control/) page for the current list of supported systems.

## Managing Harness with Pulumi

You can manage Harness itself — projects, environments, services, connectors, and pipelines — as code with the [Pulumi Harness provider](/registry/packages/harness/) in the Pulumi Registry. This lets you define the Harness resources this guide describes as part of a Pulumi program, in any supported language.

## Additional resources

- [Continuous delivery](/docs/iac/operations/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [OIDC Issuers](/docs/administration/access-identity/oidc-issuers/) — exchange a CI/CD system's OIDC token for a short-lived Pulumi access token.
- [Version Control](/docs/integrations/version-control/) — post infrastructure-change summaries on pull requests.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral per-pull-request environments.
- [CI/CD troubleshooting](/docs/iac/operations/continuous-delivery/troubleshooting/) — fixes for common failures when running Pulumi in CI/CD.
