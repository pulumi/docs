---
title_tag: "Using TeamCity with Pulumi | CI/CD"
meta_desc: Run Pulumi in TeamCity build configurations to preview and deploy infrastructure changes through a trunk-based continuous delivery workflow.
title: TeamCity
h1: Using TeamCity with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: TeamCity
        parent: iac-operations-cicd
        weight: 150
aliases:
- /docs/iac/guides/continuous-delivery/teamcity/
- /docs/iac/using-pulumi/continuous-delivery/teamcity/
- /docs/guides/continuous-delivery/teamcity/
- /docs/using-pulumi/continuous-delivery/teamcity/
- /docs/iac/packages-and-automation/continuous-delivery/teamcity/
---

[TeamCity](https://www.jetbrains.com/teamcity/) is a CI/CD server from JetBrains, available both as self-hosted TeamCity On-Premises and as the hosted TeamCity Cloud. You run Pulumi in TeamCity by adding a build step that invokes the Pulumi CLI, so the same build configuration works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/) and targeting [any cloud provider](/registry/) Pulumi supports.

{{< cicd-cloud-note >}}

## How Pulumi works with TeamCity

A TeamCity [build configuration](https://www.jetbrains.com/help/teamcity/creating-and-editing-build-configurations.html) is an ordered sequence of [build steps](https://www.jetbrains.com/help/teamcity/configuring-build-steps.html). To apply infrastructure changes, Pulumi runs your program with the Pulumi CLI, so you add a **Command Line** build step that runs `pulumi` commands — `install`, `preview`, `up` — exactly as you would on your own machine.

The Command Line runner can execute its script inside a Docker container. Point it at the official [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) image, which ships the Pulumi CLI and every language runtime, and the step works for a program in any supported language with no extra setup. If you prefer to run directly on the build agent, install the Pulumi CLI on the agent instead.

You can define build configurations through the TeamCity UI or version-control them alongside your code with the [Kotlin DSL](https://www.jetbrains.com/help/teamcity/kotlin-dsl.html).

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A TeamCity project with a build configuration attached to a [VCS root](https://www.jetbrains.com/help/teamcity/configuring-vcs-roots.html) for your Git repository.
1. A Pulumi program in that repository. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Authenticate with Pulumi Cloud

When your pipeline uses Pulumi Cloud as its backend, it needs only a single [Pulumi access token](/docs/administration/access-identity/access-tokens/) to operate. Pulumi reads the token from the `PULUMI_ACCESS_TOKEN` environment variable and authenticates without an interactive login.

Store the token outside of source control. Add it as a [build parameter](https://www.jetbrains.com/help/teamcity/configuring-build-parameters.html) of type **Password** named `env.PULUMI_ACCESS_TOKEN` so TeamCity keeps the value encrypted and masks it in build logs. Define it on a parent project to reuse it across every build configuration underneath. Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the pipeline's identity isn't tied to an individual.

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a pipeline or a developer's machine, a single environment definition works in both places.

## Provide cloud credentials

When Pulumi runs, your program also needs credentials for the cloud provider it manages. You can supply them in one of two ways:

- **Pulumi ESC (recommended).** Configure an [ESC environment](/docs/esc/) to broker short-lived cloud credentials through OIDC. Your program receives temporary credentials scoped to exactly what it needs, and the build stores nothing but its Pulumi access token.
- **Build parameters.** Set the provider's credentials as `Password`-type build parameters — for example, `env.AWS_ACCESS_KEY_ID` and `env.AWS_SECRET_ACCESS_KEY` for AWS — so they're exposed as environment variables to the build step.

{{% notes type="warning" %}}
Never commit cloud credentials or the Pulumi access token to your repository. Keep them in `Password`-type build parameters or an ESC environment so the values stay encrypted and access is auditable.
{{% /notes %}}

## Configure a TeamCity build

Add a **Command Line** build step that runs Pulumi against a [stack](/docs/iac/concepts/stacks/). Set the step's runner to run inside the `pulumi/pulumi` Docker container, and use the following custom script:

```bash
pulumi install
pulumi stack select acme/website/staging
pulumi up --yes
```

[`pulumi install`](/docs/iac/cli/commands/pulumi_install/) installs the program's language dependencies and required plugins, so the same step works for a program written in any supported language. The step picks up the `env.PULUMI_ACCESS_TOKEN` build parameter automatically, so no `pulumi login` call is needed.

If your Pulumi program lives in a subdirectory of the repository, set the build step's **Working directory** to that path.

## Build a trunk-based CI/CD workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/operations/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there. In TeamCity, a VCS root's [branch specification](https://www.jetbrains.com/help/teamcity/working-with-feature-branches.html) controls which branches a build configuration watches, and a [VCS trigger](https://www.jetbrains.com/help/teamcity/configuring-vcs-triggers.html) starts a build when those branches change — so you can map each stage of the workflow to its own build configuration.

### Preview infrastructure changes in a pull request

When a pull request is opened, run a dry run instead of a deployment. Add the [Pull Requests build feature](https://www.jetbrains.com/help/teamcity/pull-requests.html) so TeamCity discovers pull request branches, and have the Command Line step run [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/):

```bash
pulumi install
pulumi stack select acme/website/staging
pulumi preview
```

`pulumi preview` reports the proposed changes without modifying any resources, giving reviewers a summary of what the merge would do. To let reviewers exercise the change in a live environment, use a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions an ephemeral stack for the pull request and destroys it when the pull request closes.

### Deploy to staging on merge to the main branch

When a pull request merges, run [`pulumi up`](/docs/iac/cli/commands/pulumi_up/) against an environment that receives continuous delivery, such as a shared development or staging environment. Use a build configuration whose VCS trigger fires on changes to the main branch:

```bash
pulumi install
pulumi stack select acme/website/staging
pulumi up --yes
```

### Promote to production with a git tag

Production updates should be deliberate. Keep production on its own stack and deploy it only when you push a release tag — for example, a moving `production` tag that you advance to a commit already validated in staging.

Give the production build configuration a VCS root with a branch specification that watches tags, such as `+:refs/tags/*`, and target the production stack:

```bash
pulumi install
pulumi stack select acme/website/production
pulumi up --yes
```

Promotion then becomes a single, traceable Git operation, and production never deploys from an untested commit.

## Report results on pull requests

Independently of TeamCity, Pulumi offers native [version control integrations](/docs/integrations/version-control/) for popular Git hosts. With one configured, Pulumi Cloud posts infrastructure-change summaries as pull request comments and status checks, and links each stack update back to the commit and pull request that produced it. See the [Version Control](/docs/integrations/version-control/) page for the integrations currently available.

## Speed up builds with caching

A clean build agent starts with an empty plugin cache, so Pulumi re-downloads its provider plugins on every run. How you avoid that depends on your agents:

- **Persistent agents** retain Pulumi's plugin directory (`~/.pulumi/plugins`) between builds when the CLI runs directly on the agent, so the cache warms itself after the first run. If the step runs inside the `pulumi/pulumi` container, the plugin directory is discarded with the container — mount a persistent volume for it, or use the custom builder image described below.
- **Ephemeral or cloud agents** start fresh each time. Bake the provider plugins into a custom builder image: derive it from the official `pulumi/pulumi` image, `pulumi plugin install` the providers your program uses, and run the Command Line step in that image. This is the most deterministic option even where a cache exists — see the [plugins documentation](/docs/iac/concepts/plugins/).

## Additional resources

- [Continuous delivery](/docs/iac/operations/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [CI/CD troubleshooting guide](/docs/iac/operations/continuous-delivery/troubleshooting/) — diagnose common failures when running Pulumi in a pipeline.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [OIDC Issuers](/docs/administration/access-identity/oidc-issuers/) — eliminate static tokens on CI/CD systems that can issue OIDC tokens.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral environments for pull requests.
- [Version Control](/docs/integrations/version-control/) — connect Pulumi Cloud to your Git host for pull request reporting.
