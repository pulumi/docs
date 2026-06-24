---
title_tag: "Using Bitbucket Pipelines with Pulumi | CI/CD"
meta_desc: Run Pulumi in Bitbucket Pipelines, authenticate with Pulumi Cloud, and ship infrastructure changes through a trunk-based CI/CD workflow.
title: Bitbucket Pipelines
h1: Using Bitbucket Pipelines with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Bitbucket Pipelines
        parent: iac-operations-cicd
        weight: 40
aliases:
- /docs/iac/guides/continuous-delivery/bitbucket/
- /docs/reference/cd-bitbucket/
- /docs/console/continuous-delivery/bitbucket/
- /docs/guides/continuous-delivery/bitbucket/
- /docs/guides/continuous-delivery/cd-bitbucket/
- /docs/using-pulumi/continuous-delivery/cd-bitbucket/
- /docs/using-pulumi/continuous-delivery/bitbucket/
- /docs/iac/using-pulumi/continuous-delivery/bitbucket/
- /docs/iac/packages-and-automation/continuous-delivery/bitbucket/
---

[Bitbucket Pipelines](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/) is the CI/CD service built into Bitbucket Cloud. It runs the pipeline defined in a `bitbucket-pipelines.yml` file at the root of your repository, building and deploying your code on each push, pull request, or tag.

Pulumi runs in a pipeline as plain CLI commands, so this guide works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/) and targeting [any cloud provider](/registry/).

{{< pulumi-docker-images-note >}}

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A Bitbucket Cloud repository with [Pipelines enabled](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/).
1. A Pulumi program committed to that repository. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Authenticate with Pulumi Cloud

Give your pipeline a Pulumi Cloud identity in one of two ways. **Choose one — you don't need both:**

- **A stored access token** — a long-lived Pulumi access token kept as a secured repository variable. Simplest to set up.
- **OIDC token exchange** — no stored secret; the pipeline exchanges a short-lived OIDC token for a Pulumi access token at runtime. Recommended.

Whichever you choose, [Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a pipeline or a developer's machine, a single environment definition works in both places — you don't store separate cloud provider keys as repository variables.

### Authenticate with a stored access token

Your pipeline authenticates to Pulumi Cloud with a single [Pulumi access token](/docs/administration/access-identity/access-tokens/), supplied through the `PULUMI_ACCESS_TOKEN` environment variable. Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the pipeline's identity is not tied to an individual.

Add the token as a [repository variable](https://support.atlassian.com/bitbucket-cloud/docs/variables-and-secrets/) under **Repository settings > Repository variables**. Name it `PULUMI_ACCESS_TOKEN` and select the **Secured** checkbox so the value is encrypted and masked in build logs. Secured variables are exposed to every step of the pipeline as environment variables.

{{% notes type="info" %}}
Always mark sensitive values — access tokens, cloud provider keys — as **Secured**. An unsecured variable is stored and printed in plaintext.
{{% /notes %}}

### Authenticate without a stored token using OIDC

You can remove the static token entirely. Bitbucket Pipelines can issue a short-lived [OpenID Connect (OIDC)](https://support.atlassian.com/bitbucket-cloud/docs/integrate-pipelines-with-resource-servers-using-oidc/) token for any step that sets `oidc: true`, exposing it as the `BITBUCKET_STEP_OIDC_TOKEN` environment variable.

Register Bitbucket Pipelines as a trusted [OIDC issuer](/docs/administration/access-identity/oidc-issuers/) in Pulumi Cloud, and your pipeline can exchange that OIDC token for a short-lived Pulumi access token at runtime — no long-lived credential is stored as a repository variable.

## The trunk-based development workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/operations/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there.

Bitbucket Pipelines has three pipeline triggers that map directly onto the three stages of this workflow:

- `pull-requests` runs when a pull request is opened or updated — use it to **preview** changes.
- `branches` runs when commits land on a branch — use it to **deploy to staging** on merge to `main`.
- `tags` runs when a tag is pushed — use it to **promote to production**.

The `bitbucket-pipelines.yml` below implements all three stages. It assumes a Pulumi program in an `infra/` directory and stacks named `acme/website/staging` and `acme/website/production`:

```yaml
# bitbucket-pipelines.yml
image: pulumi/pulumi:latest

pipelines:
  # Pull request: preview the proposed changes.
  pull-requests:
    '**':
      - step:
          name: Preview infrastructure changes
          script:
            - cd infra
            - pulumi install
            - pulumi stack select acme/website/staging
            - pulumi preview

  # Merge to main: deploy to the staging environment.
  branches:
    main:
      - step:
          name: Deploy to staging
          script:
            - cd infra
            - pulumi install
            - pulumi stack select acme/website/staging
            - pulumi up --yes

  # Tag push: promote to production.
  tags:
    'release-*':
      - step:
          name: Deploy to production
          script:
            - cd infra
            - pulumi install
            - pulumi stack select acme/website/production
            - pulumi up --yes
```

The `pulumi/pulumi` Docker image includes the Pulumi CLI and every language runtime, so the same pipeline works regardless of the language your program is written in. [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) installs the program's language dependencies and required plugins.

`pulumi preview` reports the proposed changes without modifying any resources, giving reviewers a summary of what the merge would do. To let reviewers exercise the change in a live environment, pair the preview step with a [Review Stack](/docs/deployments/concepts/review-stacks/), which provisions an ephemeral stack for the pull request and destroys it when the pull request closes.

To promote a release, push a tag that matches the `release-*` pattern:

```bash
git tag release-2026-05-20
git push origin release-2026-05-20
```

Keeping production on its own stack and deploying it only from a tag makes each production update a single, traceable Git operation, and ensures production never deploys from an untested commit.

## Cloud provider credentials

Your Pulumi program needs credentials for whichever cloud it manages. Supply them as **Secured** repository variables, or — better — use [Pulumi ESC](/docs/esc/) to broker short-lived cloud credentials so no provider keys are stored as repository variables at all.

## Report results back to Bitbucket

The Pulumi Cloud [Bitbucket version control integration](/docs/integrations/version-control/bitbucket/) posts pull request comments and commit status checks for every deployment, regardless of which CI/CD system triggers the run. Connecting it gives reviewers a summary of resource changes directly on the pull request.

The integration can also replace a hand-written pipeline entirely: with [push-to-deploy](/docs/deployments/concepts/triggers/#push-to-deploy) and [review stacks](/docs/deployments/concepts/review-stacks/), Pulumi Cloud runs your updates on Pulumi-hosted infrastructure in response to Bitbucket events, with no `bitbucket-pipelines.yml` to maintain.

## Additional resources

- [Continuous delivery](/docs/iac/operations/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) — exchange a CI/CD system's OIDC token for a short-lived Pulumi access token.
- [Bitbucket version control integration](/docs/integrations/version-control/bitbucket/) — pull request comments and commit statuses from Pulumi Cloud.
- [Review Stacks](/docs/deployments/concepts/review-stacks/) — ephemeral environments created automatically for each pull request.
- [CI/CD troubleshooting](/docs/iac/operations/continuous-delivery/troubleshooting/) — diagnose common failures when running Pulumi in a pipeline.
