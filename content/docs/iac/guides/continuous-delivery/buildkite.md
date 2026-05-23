---
title_tag: "Using Buildkite with Pulumi | CI/CD"
meta_desc: Run Pulumi in a Buildkite pipeline with the official Pulumi plugin, and ship infrastructure through a trunk-based CI/CD workflow.
title: Buildkite
h1: Using Buildkite with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
aliases:
- /docs/iac/using-pulumi/continuous-delivery/buildkite/
menu:
    iac:
        name: Buildkite
        parent: iac-using-pulumi-cicd
        weight: 50
---

[Buildkite](https://buildkite.com/) is a CI/CD platform that runs pipelines on agents you host or on Buildkite-hosted agents. You run Pulumi in a Buildkite pipeline with the [`pulumi` plugin](https://buildkite.com/resources/plugins/buildkite-plugins/pulumi-buildkite-plugin/), an official Buildkite plugin that installs and configures the Pulumi CLI for a step.

Because the plugin runs CLI commands, it works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/), and with [any cloud provider](/registry/) Pulumi supports.

{{% notes type="info" %}}
This guide assumes [Pulumi Cloud](/docs/pulumi-cloud/) as your backend. Pulumi Cloud isn't required to run Pulumi in CI/CD — Pulumi also supports [self-managed backends](/docs/iac/concepts/state-and-backends/) — but the access token, OIDC, and ESC features described here are specific to Pulumi Cloud.
{{% /notes %}}

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A Buildkite account with a [cluster and agent](https://buildkite.com/docs/pipelines/getting-started).
1. A Git repository connected to a Buildkite pipeline.
1. A Pulumi program. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Install and configure Pulumi

A Buildkite pipeline's steps can be defined in the web interface or, more commonly, in a `pipeline.yml` file committed to your repository. The Buildkite agent looks for this file in [a few locations](https://buildkite.com/docs/agent/v3/cli-pipeline#uploading-pipelines-description); `.buildkite/pipeline.yml` in the repository root is the conventional choice.

Add the `pulumi` plugin to any step that runs a Pulumi command. The plugin installs the CLI before the step's commands run:

```yaml
# .buildkite/pipeline.yml
steps:
  - label: ":pulumi: Preview"
    commands:
      - cd infra && npm install
      - pulumi preview --stack acme/website/dev
    plugins:
      - pulumi#v1.0.0:
          # Pin a specific CLI version. Optional; defaults to the latest release.
          version: 3.143.0
```

As an alternative to the plugin, you can run your step inside one of Pulumi's official [container images](https://github.com/pulumi/pulumi-docker-containers), which ship the Pulumi CLI and a language runtime preinstalled. Use the [`docker` plugin](https://buildkite.com/resources/plugins/buildkite-plugins/docker-buildkite-plugin/) to select the image for your language:

```yaml
    plugins:
      - docker#v5.9.0:
          image: pulumi/pulumi-nodejs
          mount-buildkite-agent: true
          environment:
            - PULUMI_ACCESS_TOKEN
```

## Authenticate with Pulumi Cloud

When your pipeline uses Pulumi Cloud as its backend, it needs only a single [Pulumi access token](/docs/administration/access-identity/access-tokens/) to operate.

Store the token as a [Buildkite secret](https://buildkite.com/docs/pipelines/security/secrets/buildkite-secrets) so it isn't committed to source control, and use the [`secrets` plugin](https://buildkite.com/resources/plugins/buildkite-plugins/secrets-buildkite-plugin/) to map it to the `PULUMI_ACCESS_TOKEN` environment variable:

```yaml
    plugins:
      - secrets#v1.0.0:
          variables:
            PULUMI_ACCESS_TOKEN: PULUMI_ACCESS_TOKEN
      - pulumi#v1.0.0: ~
```

Prefer an organization or team token over a personal token.

You can remove even that static secret with [OpenID Connect (OIDC)](/docs/administration/access-identity/oidc-issuers/). Register Buildkite as an OIDC issuer in Pulumi Cloud, then enable OIDC on the plugin — it exchanges the [OIDC token Buildkite issues for the job](https://buildkite.com/docs/pipelines/security/oidc) for a short-lived Pulumi access token, so no long-lived credential is stored:

```yaml
    plugins:
      - pulumi#v1.0.0:
          use-oidc: true
          audience: "urn:pulumi:org:ACME_ORG"
```

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a pipeline or a developer's machine, a single environment definition works in both places — you don't store separate cloud provider keys in the pipeline.

## The trunk-based development workflow

The most common way to run Pulumi in Buildkite follows a trunk-based development model, where work merges into a single main branch and deployments flow outward from there:

1. **Open a pull request.** The pipeline runs `pulumi preview` and surfaces the proposed changes for review.
1. **Merge to the main branch.** The pipeline runs `pulumi up` to deploy the change to an environment that receives continuous delivery, such as a shared development or staging environment.
1. **Promote to production.** Pushing a git tag triggers a deployment to production, keeping production updates deliberate and traceable.

The pipeline below implements all three stages with conditional steps. It assumes a Pulumi program in an `infra/` directory and stacks named `acme/website/staging` and `acme/website/production`.

```yaml
# .buildkite/pipeline.yml
steps:
  # Pull request: preview the proposed changes and post them as a build annotation.
  - label: ":pulumi: Preview"
    if: build.pull_request.id != null
    commands:
      - cd infra && npm install
      - pulumi preview --stack acme/website/staging 2>&1 | tee preview.txt
      - printf '```\n%s\n```\n' "$(cat preview.txt)" | buildkite-agent annotate --style info
    plugins:
      - secrets#v1.0.0:
          variables:
            PULUMI_ACCESS_TOKEN: PULUMI_ACCESS_TOKEN
      - pulumi#v1.0.0: ~

  # Merge to the main branch: deploy to the staging environment.
  - label: ":pulumi: Deploy to staging"
    if: build.branch == "main" && build.pull_request.id == null
    commands:
      - cd infra && npm install
      - pulumi up --yes --stack acme/website/staging
    plugins:
      - secrets#v1.0.0:
          variables:
            PULUMI_ACCESS_TOKEN: PULUMI_ACCESS_TOKEN
      - pulumi#v1.0.0: ~

  # Tag push: promote to production.
  - label: ":pulumi: Deploy to production"
    if: build.tag != null
    commands:
      - cd infra && npm install
      - pulumi up --yes --stack acme/website/production
    plugins:
      - secrets#v1.0.0:
          variables:
            PULUMI_ACCESS_TOKEN: PULUMI_ACCESS_TOKEN
      - pulumi#v1.0.0: ~
```

To promote a release, push a tag:

```bash
git tag release-2026-05-20
git push origin release-2026-05-20
```

Buildkite decides *when* to start a build — on pull requests, branch pushes, and tags — through your pipeline's [source control settings](https://buildkite.com/docs/pipelines/source-control), not the pipeline file. Enable pull request and tag builds there; the `if` expressions above then select which steps run for each build.

For an optional ephemeral environment on each pull request, pair the preview step with a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions and tears down a per-PR environment automatically.

{{% notes type="info" %}}
The Pulumi CLI automatically detects when it runs inside Buildkite and records the build and commit metadata. Each update in Pulumi Cloud then links back to the build and pull request that triggered it — no extra configuration required.
{{% /notes %}}

## Buildkite features worth knowing

- **Dynamic pipelines.** Buildkite can generate pipeline steps at build time with [dynamic pipelines](https://buildkite.com/docs/pipelines/configure/dynamic-pipelines). This is useful when you want to fan out a step per Pulumi stack or project rather than hard-coding each one.
- **Cache volumes.** On hosted agents, [cache volumes](https://buildkite.com/docs/pipelines/hosted-agents/cache-volumes) persist directories across builds. Caching `~/.pulumi/plugins` and your language packages (`node_modules`, and so on) speeds up runs. Pulumi plugin versions are tied 1:1 to the Pulumi package versions that use them, so the cache stays correct as long as those packages are unchanged.

## Managing Buildkite with Pulumi

You can also manage Buildkite itself — pipelines, teams, and agent tokens — as code with the community-maintained [Pulumiverse Buildkite provider](/registry/packages/buildkite/) in the Pulumi Registry.

## Additional resources

- [Continuous delivery](/docs/iac/guides/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) — exchange a CI/CD system's OIDC token for a short-lived Pulumi access token.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral environments created automatically for each pull request.
