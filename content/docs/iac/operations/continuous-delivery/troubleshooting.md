---
title_tag: "Troubleshooting Pulumi in CI/CD"
meta_desc: Diagnose and fix the most common failures encountered when running Pulumi in a CI/CD pipeline, organized by the step of a typical pipeline run.
title: Troubleshooting
h1: Troubleshooting Pulumi in CI/CD
menu:
    iac:
        name: Troubleshooting
        parent: iac-operations-cicd
        weight: 170
aliases:
- /docs/iac/guides/continuous-delivery/troubleshooting/
- /docs/support/troubleshooting/ci-cd/
- /docs/iac/using-pulumi/continuous-delivery/troubleshooting-guide/
- /docs/guides/continuous-delivery/troubleshooting-guide/
- /docs/using-pulumi/continuous-delivery/troubleshooting-guide/
- /docs/iac/packages-and-automation/continuous-delivery/troubleshooting-guide/
---

Every CI/CD system runs Pulumi the same way under the hood, so the failures you hit in an automated pipeline tend to fall into the same handful of categories regardless of which system you use. This guide walks through the steps of a typical Pulumi pipeline run and the class of failure tied to each one, so you can narrow down where a build is going wrong and what to check.

## Overall requirements

To run a `pulumi preview` or `pulumi up` in a pipeline, the build agent needs all of the following:

- A way to authenticate with your backend — a [Pulumi access token](/docs/administration/access-identity/access-tokens/) when using Pulumi Cloud.
- A [stack](/docs/iac/concepts/stacks/) that the pipeline will update, created ahead of time.
- The Pulumi CLI available on the system `PATH`.
- The language runtime and build tools for your Pulumi program (more on this below).
- Your program's dependencies and resource provider plugins, installed before a preview or update.
- Valid cloud provider credentials with permission to manage your resources.

The type of failure you see is almost always traceable to one of these. The sections below cover each in turn.

## Pulumi access token

When Pulumi detects that it's running inside a CI/CD system, it skips the interactive `pulumi login` prompt and authenticates non-interactively instead. With Pulumi Cloud as your backend, it reads the access token from the `PULUMI_ACCESS_TOKEN` environment variable.

What to check when authentication fails:

- The token is exposed to the pipeline as an environment variable named exactly `PULUMI_ACCESS_TOKEN`. Store it as a secret — most CI/CD systems can mark an environment variable as sensitive, and your access token is a sensitive value.
- The environment variable is actually in scope for the job or step that runs the `pulumi` command. Many CI/CD systems reset the environment between jobs or stages, so a variable set in one job may not be visible in another.
- The pipeline can reach the secret. Several systems restrict secrets to specific branches or environments — confirm the branch and job running Pulumi are allowed to read it.
- Prefer an [organization or team access token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal one, so the pipeline's identity isn't tied to an individual.

To avoid storing a long-lived secret at all, use [OpenID Connect (OIDC)](/docs/administration/access-identity/oidc-issuers/): the pipeline exchanges a short-lived token issued by your CI/CD system for a temporary Pulumi access token. [Pulumi ESC](/docs/esc/) can then supply cloud credentials and configuration the same way to both pipelines and developer machines.

## Stack name

A [stack](/docs/iac/concepts/stacks/) is a specific, [configurable](/docs/iac/concepts/config/) instance of your infrastructure. A pipeline updates an existing stack — it does not create one — so the stack must already exist in the correct organization, created beforehand with `pulumi stack init`.

What to check when a `pulumi` command can't find or access your stack:

- The account behind your access token has access to the stack. A token without access produces 404s from Pulumi Cloud. Confirm by signing in to [Pulumi Cloud](https://app.pulumi.com/signin) with the same account and navigating to the stack.
- Pass a fully qualified stack name to `pulumi` commands. A fully qualified stack name has the form `<organization>/<project>/<stack>` — for example, a stack named `production` in the `pulumi` organization and `slack-bot` project is `pulumi/slack-bot/production`. Pulumi can infer the project from your `Pulumi.yaml`, so the fully qualified form is optional, but using it removes any ambiguity about which stack a pipeline targets.
- The `pulumi` command runs from the directory containing your project's `Pulumi.yaml`. If your program lives elsewhere, pass `--cwd` — see the [global flags](/docs/iac/cli/commands/pulumi/#options) supported by every `pulumi` command.
- The stack's configuration file sits alongside `Pulumi.yaml`. For a stack named `production`, `Pulumi.production.yaml` must be in the same directory as `Pulumi.yaml`.

## Installing the Pulumi CLI

The build agent needs the Pulumi CLI on its `PATH`. Several CI/CD systems have a native extension that installs and runs the CLI for you:

- [Azure Pipelines task extension](https://marketplace.visualstudio.com/items?itemName=pulumi.build-and-release-task) — see the [Azure DevOps guide](/docs/iac/operations/continuous-delivery/azure-devops/).
- GitHub Actions — [`pulumi/actions`](https://github.com/pulumi/actions) and [`pulumi/action-install-pulumi-cli`](https://github.com/pulumi/action-install-pulumi-cli); see the [GitHub Actions guide](/docs/iac/operations/continuous-delivery/github-actions/). GitHub-hosted runners ship the Pulumi CLI pre-installed, so an explicit install step is only needed to pin a specific version.
- [CircleCI orb](https://circleci.com/developer/orbs/orb/compute/pulumi) — see the [CircleCI guide](/docs/iac/operations/continuous-delivery/circleci/).

If your system has no native extension, add an inline script step to [install the CLI manually](/docs/install/).

What to check when `pulumi` isn't found:

- The CLI is available in the same step that runs `pulumi` commands. The official install script adds `pulumi` to the `PATH` of the current environment, but that change does not always carry across steps.
- This is especially common with container-based pipelines: a container's filesystem and environment often don't persist between steps, so installing the CLI in one step and calling it in another won't work. Some systems let you define a reusable setup step or template to avoid repeating the install. Running Pulumi inside the [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) container image — which already includes the CLI and every language runtime — sidesteps the problem entirely.

## Build tools

Pulumi invokes the build tool for your project's runtime. If the pipeline is missing that toolchain, Pulumi can't run your program. For example, a `nodejs` project needs a supported version of Node.js along with the package manager you use (`npm`, `yarn`, or `pnpm`). The requirements differ by language — see the page for your [language](/docs/iac/languages-sdks/) for the specific runtime and tooling it needs.

What to check when a build fails before Pulumi reaches your resources:

- Your project's runtime and build tools are installed on the build agent. Most CI/CD systems offer a built-in way to install a specific language version — GitHub Actions, for instance, provides `actions/setup-node`, `actions/setup-python`, `actions/setup-go`, and `actions/setup-dotnet`.
- For container-based pipelines, consider the [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) image, which bundles the CLI and every supported language runtime.

## Restoring dependencies

Every Pulumi program depends on at least the Pulumi SDK, and those dependencies — along with the resource provider plugins your program uses — must be present before Pulumi runs a preview or update.

What to check when a run fails on missing packages or plugins:

- The simplest way to restore everything is [`pulumi install`](/docs/iac/cli/commands/pulumi_install/), which installs both your program's dependencies and the required plugins in a single step, for any runtime. Run it before `pulumi preview` or `pulumi up`.
- If you restore dependencies with your language's own package manager instead, note that the behavior varies by runtime: for `dotnet` and `go` projects, dependencies are restored automatically when you run `pulumi preview` or `pulumi up`, while `nodejs` and `python` projects need an explicit restore step.
- A `.NET` project that pulls packages from a private feed is an exception to automatic restore. Make sure the private feed is reachable from the pipeline, or use a [pre-built binary](/docs/iac/concepts/projects/) so the solution doesn't need to be rebuilt. If you use a pre-built binary, install the necessary plugins manually with [`pulumi plugin install`](/docs/iac/cli/commands/pulumi_plugin_install/).
- If you cache dependencies, cache the Pulumi plugins too. Installing the Pulumi SDK triggers a post-install step that downloads [resource provider](/docs/iac/guides/basics/how-pulumi-works/#resource-providers) plugins from Pulumi's CDN. Caching only your language packages leaves those plugins to be re-downloaded — or missing — on each run. Note that plugin caches can grow large depending on how many providers you use, and some CI/CD systems cap cache size.
- When a run fails for reasons you can't pin down, clear all caches and restore dependencies from scratch to rule out a stale cache.

## Cloud provider credentials

Cloud provider credentials are another common point of failure. Credential errors usually fall into two buckets: the wrong credentials (wrong account, mismatched keys) or credentials whose access scope is too narrow to create the resources your program declares.

What to check when resource operations fail with authentication or authorization errors:

- The credentials are supplied to Pulumi through a mechanism the provider supports. Environment variables work in nearly all cases. Some providers also support authentication through their own CLI — the Azure provider, for example, can use the Azure CLI's session, but only if that CLI is itself authenticated with an account that has the right role and subscription.
- The step running the `pulumi` command can actually read the credential variables. As with the Pulumi access token, secrets are often scoped to specific jobs, stages, or branches, and environments can reset between jobs.
- There are no typos in the credential environment variable names.

Refer to each provider's page in the [Pulumi Registry](/registry/) for the exact environment variables it expects.

If you use Pulumi Cloud, [Pulumi ESC](/docs/esc/) is an alternative to storing static cloud keys in your CI/CD system: it can supply cloud provider credentials to your pipeline dynamically, including short-lived credentials issued through OIDC.

## Still need help?

If none of the above resolves your issue, the [Pulumi Community Slack](https://slack.pulumi.com) is a great place to ask — signup is free, and Pulumi team members are active there alongside other community members. To report a bug, see the [guide for filing issues](/docs/support/filing-issues/) so it lands in the right repository.
