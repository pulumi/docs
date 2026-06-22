---
title_tag: "Using CircleCI with Pulumi | CI/CD"
meta_desc: Run Pulumi in CircleCI with the Pulumi Orbs, authenticate with Pulumi Cloud, and ship infrastructure through a trunk-based CI/CD workflow.
title: CircleCI
h1: Using CircleCI with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: CircleCI
        parent: iac-operations-cicd
        weight: 60
aliases:
- /docs/iac/guides/continuous-delivery/circleci/
- /docs/iac/using-pulumi/continuous-delivery/circleci/
- /docs/reference/cd-circleci/
- /docs/console/continuous-delivery/circleci/
- /docs/guides/continuous-delivery/circleci/
- /docs/using-pulumi/continuous-delivery/cd-circleci/
- /docs/guides/continuous-delivery/cd-circleci/
- /docs/using-pulumi/continuous-delivery/circleci/
- /docs/iac/packages-and-automation/continuous-delivery/circleci/
---

[CircleCI](https://circleci.com/) is a CI/CD platform that runs build, test, and deployment jobs defined in a `.circleci/config.yml` file in your repository. You run Pulumi in CircleCI with the [Pulumi Orbs for CircleCI](https://circleci.com/developer/orbs/orb/pulumi/pulumi), a Pulumi-maintained [orb](https://circleci.com/docs/orb-intro/) that provides reusable commands to install the Pulumi CLI and run Pulumi operations without custom scripts.

The orb runs CLI commands, so it works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/). It also works with [any cloud provider](/registry/) Pulumi supports.

{{% notes type="info" %}}
This guide assumes you use [Pulumi Cloud](https://app.pulumi.com/signin) as your [state backend](/docs/iac/concepts/state-and-backends/). Pulumi also supports [self-managed backends](/docs/iac/concepts/state-and-backends/#using-a-diy-backend) in CI/CD, but the authentication steps in this guide are written for Pulumi Cloud.
{{% /notes %}}

{{< pulumi-docker-images-note >}}

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A CircleCI account with a project connected to your Git repository.
1. A Pulumi program. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Add the Pulumi orb

Reference the orb at the top of your `.circleci/config.yml`. Pin a specific version so builds stay reproducible:

```yaml
version: 2.1

orbs:
  pulumi: pulumi/pulumi@2.2.0
```

Once the orb is referenced, its commands — such as `pulumi/login`, `pulumi/preview`, and `pulumi/update` — are available in any job's `steps`.

## Authenticate with Pulumi Cloud

When your pipeline uses Pulumi Cloud as its backend, it needs only a single [Pulumi access token](/docs/administration/access-identity/access-tokens/) to operate. The `pulumi/login` command reads the token from the `PULUMI_ACCESS_TOKEN` environment variable.

Store the token in a CircleCI [context](https://circleci.com/docs/contexts/) rather than committing it to your repository. A context holds environment variables at the organization level, so the same token is available to every project that needs it. You can also set it as a [project environment variable](https://circleci.com/docs/set-environment-variable/#set-an-environment-variable-in-a-project) if it's used by only one project. Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the pipeline's identity isn't tied to an individual.

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a CircleCI job or a developer's machine, a single environment definition works in both places — you don't store separate cloud provider keys in CircleCI.

## Install program dependencies

The `pulumi/login` command installs the Pulumi CLI, but it does not install your program's language dependencies. Add a step that runs [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) before any `preview` or `update` step:

```yaml
- run:
    name: Install dependencies
    command: pulumi install --cwd infra/
```

`pulumi install` installs the program's language dependencies and required plugins, so the same step works for a Pulumi program written in any supported language.

{{% notes type="info" %}}
The CircleCI executor image must include the runtime for your program's language — for example, a `cimg/node` image for TypeScript or JavaScript, or a `cimg/python` image for Python. See the [CircleCI convenience images](https://circleci.com/developer/images) for the available options.
{{% /notes %}}

## Build a trunk-based CI/CD workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/operations/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there.

CircleCI does not have a dedicated pull request trigger; instead, you control when a job runs with [workflow filters](https://circleci.com/docs/configuration-reference/#filters) on branches and tags. The workflow below maps each stage of the trunk-based model to its own job:

1. **Open a pull request.** The `preview` job runs on every non-main branch and reports the proposed changes with `pulumi preview`.
1. **Merge to the main branch.** The `deploy-staging` job runs on `main` and deploys the change to a staging environment with `pulumi up`.
1. **Promote to production.** Pushing a `release-*` tag runs the `deploy-production` job, which deploys to production.

The following `.circleci/config.yml` implements all three stages. It assumes a Pulumi program in an `infra/` directory, stacks named `acme/website/staging` and `acme/website/production`, and a context named `pulumi` that holds `PULUMI_ACCESS_TOKEN`:

```yaml
version: 2.1

orbs:
  pulumi: pulumi/pulumi@2.2.0

jobs:
  preview:
    docker:
      - image: cimg/node:lts
    steps:
      - checkout
      - pulumi/login
      - run:
          name: Install dependencies
          command: pulumi install --cwd infra/
      - pulumi/preview:
          stack: acme/website/staging
          working_directory: infra/

  deploy-staging:
    docker:
      - image: cimg/node:lts
    steps:
      - checkout
      - pulumi/login
      - run:
          name: Install dependencies
          command: pulumi install --cwd infra/
      - pulumi/update:
          stack: acme/website/staging
          working_directory: infra/

  deploy-production:
    docker:
      - image: cimg/node:lts
    steps:
      - checkout
      - pulumi/login
      - run:
          name: Install dependencies
          command: pulumi install --cwd infra/
      - pulumi/update:
          stack: acme/website/production
          working_directory: infra/

workflows:
  pulumi:
    jobs:
      # Pull request: preview the proposed changes on any non-main branch.
      - preview:
          context: pulumi
          filters:
            branches:
              ignore: main
      # Merge to main: deploy to the staging environment.
      - deploy-staging:
          context: pulumi
          filters:
            branches:
              only: main
      # Tag push: promote to production.
      - deploy-production:
          context: pulumi
          filters:
            tags:
              only: /^release-.*/
            branches:
              ignore: /.*/
```

By default, CircleCI ignores tag pushes, so the `deploy-production` job sets an explicit `filters.tags` entry and ignores all branches. To promote a release, push a tag that matches the `release-*` pattern:

```bash
git tag release-2026-05-20
git push origin release-2026-05-20
```

For an optional ephemeral environment on each pull request, pair the `preview` job with a [Review Stack](/docs/deployments/concepts/review-stacks/), which provisions and tears down a per-PR environment automatically.

## Orb command reference

The Pulumi orb provides the following commands. Every command except `login` accepts a `working_directory` parameter (default `.`) for a Pulumi program in a subdirectory.

| Command | Description | Key parameters |
|---------|-------------|----------------|
| `pulumi/login` | Installs the Pulumi CLI and runs `pulumi login`. | `version` (default `latest`), `cloud-url`, `access-token` (default `${PULUMI_ACCESS_TOKEN}`) |
| `pulumi/preview` | Runs `pulumi preview` for a stack. | `stack` |
| `pulumi/update` | Runs `pulumi up` for a stack. | `stack`, `skip-preview` |
| `pulumi/refresh` | Runs `pulumi refresh` for a stack. | `stack`, `expect_no_changes`, `skip-preview` |
| `pulumi/destroy` | Runs `pulumi destroy` for a stack. | `stack`, `skip-preview` |
| `pulumi/stack_init` | Creates a new stack. | `stack`, `secrets_provider`, `copy` |
| `pulumi/stack_rm` | Removes a stack and its configuration. | `stack`, `force` |
| `pulumi/stack_output` | Reads a stack output into an environment variable. | `stack`, `property_name`, `env_var`, `show_secrets` |

For the full parameter documentation, see the [orb registry page](https://circleci.com/developer/orbs/orb/pulumi/pulumi) and the [orb source](https://github.com/pulumi/circleci).

## Using with other cloud providers

To use the orb with AWS, Google Cloud, or another provider, supply the required credentials as environment variables in a CircleCI context or project. Your Pulumi program reads them when it runs in the `preview` and `update` jobs.

Using [Pulumi ESC](/docs/esc/) to broker short-lived cloud credentials through [OpenID Connect (OIDC)](/docs/esc/guides/configuring-oidc/) avoids storing long-lived provider keys in CircleCI at all — the job needs only its Pulumi access token, and everything else flows from ESC.

## Managing CircleCI with Pulumi

You can manage CircleCI itself — projects, contexts, and environment variables — as code with the [CircleCI provider](/registry/packages/circleci/) in the Pulumi Registry. The provider is bridged from a Terraform provider; add it to your project with:

```bash
pulumi package add terraform-provider mrolla/circleci
```

## Additional resources

- [Continuous delivery](/docs/iac/operations/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) — exchange a CI/CD system's OIDC token for a short-lived Pulumi access token.
- [Review Stacks](/docs/deployments/concepts/review-stacks/) — ephemeral per-pull-request environments.
- [CI/CD troubleshooting](/docs/iac/operations/continuous-delivery/troubleshooting/) — fixes for common failures when running Pulumi in CI/CD.
