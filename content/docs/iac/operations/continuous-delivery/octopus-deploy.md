---
title_tag: "Using Octopus Deploy with Pulumi | CI/CD"
meta_desc: Run Pulumi in an Octopus Deploy deployment process to deploy infrastructure changes and promote them to production through Octopus environments.
title: Octopus Deploy
h1: Using Octopus Deploy with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Octopus Deploy
        parent: iac-operations-cicd
        weight: 130
aliases:
- /docs/iac/guides/continuous-delivery/octopus-deploy/
- /docs/iac/using-pulumi/continuous-delivery/octopus-deploy/
- /docs/guides/continuous-delivery/octopus-deploy/
- /docs/using-pulumi/continuous-delivery/octopus-deploy/
- /docs/iac/packages-and-automation/continuous-delivery/octopus-deploy/
---

[Octopus Deploy](https://octopus.com) is a deployment automation server that orchestrates releases across environments. Octopus is organized around [projects](https://octopus.com/docs/projects), versioned releases, and [environments](https://octopus.com/docs/infrastructure/environments) that a release advances through. You run Pulumi as a step in an Octopus [deployment process](https://octopus.com/docs/projects/deployment-process), so an infrastructure change is deployed and promoted with the same release mechanics Octopus already uses for application code.

{{< cicd-cloud-note >}}

## How Pulumi works with Octopus Deploy

Octopus Deploy is a *continuous delivery* server, not a continuous integration server: it does not track your version control system, and it does not watch for pull requests or branch pushes. Octopus is typically paired with an upstream CI system — such as [GitHub Actions](/docs/iac/operations/continuous-delivery/github-actions/), [Jenkins](/docs/iac/operations/continuous-delivery/jenkins/), or [TeamCity](/docs/iac/operations/continuous-delivery/teamcity/) — that builds and tests your code, runs pull request previews, and produces the versioned package Octopus releases.

To apply infrastructure changes, Pulumi runs your program with the Pulumi CLI. In an Octopus deployment process, a **Run a Script** step provides that environment. Octopus [execution containers](https://octopus.com/docs/projects/steps/execution-containers-for-workers) let that step run inside a container image you choose: point it at the official [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) image and the step has the Pulumi CLI and every language runtime preinstalled. The same deployment process then works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/) and targeting [any cloud provider](/registry/) Pulumi supports.

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. An Octopus Deploy instance — [Octopus Cloud](https://octopus.com) or a self-hosted server — with a project and one or more environments configured.
1. A Pulumi program in a Git repository. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.
1. An upstream CI system that builds your program and publishes it as a [package](https://octopus.com/docs/packaging-applications) for Octopus to release.

## Authenticate with Pulumi Cloud

Give your deployment process a Pulumi Cloud identity in one of two ways. **Choose one — you don't need both:**

- **A stored access token.** Save a long-lived [Pulumi access token](/docs/administration/access-identity/access-tokens/) as a sensitive Octopus variable. Simple to set up and works on every Octopus version.
- **OpenID Connect (OIDC), recommended where supported.** Exchange a short-lived token issued by Octopus for a temporary Pulumi access token, so no long-lived credential is stored anywhere.

### Use a stored access token

Pulumi reads its access token from the `PULUMI_ACCESS_TOKEN` environment variable and authenticates without an interactive login. Store the token as a **sensitive** Octopus [project variable](https://octopus.com/docs/projects/variables) — or, to reuse it across projects, in a [library variable set](https://octopus.com/docs/projects/variables/library-variable-sets) — named `PULUMI_ACCESS_TOKEN`. Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the deployment's identity isn't tied to an individual.

Marking the variable sensitive keeps its value out of logs and the Octopus UI. Scope it to the environments that should use it.

### Use OIDC

Octopus Deploy 2025.1 and later can issue a short-lived OIDC token for a deployment run through a [Generic OpenID Connect account](https://octopus.com/docs/infrastructure/accounts/openid-connect). Pulumi Cloud can register Octopus Server as a trusted [OIDC issuer](/docs/administration/access-identity/oidc-issuers/), which removes the need to store a static `PULUMI_ACCESS_TOKEN`.

The flow is generic:

1. Register your Octopus Server as an OIDC issuer in Pulumi Cloud, and configure a Generic OIDC account in Octopus whose audience matches what Pulumi Cloud expects.
1. During the deployment, the Run a Script step reads the issued token from the account's `OpenIdConnect.Jwt` variable.
1. The step exchanges that token for a temporary Pulumi access token with `pulumi login --oidc-token <token> --oidc-org <your-org>`.

{{% notes type="info" %}}
The OIDC path requires Octopus Deploy 2025.1 or later, and Pulumi Cloud must be able to reach your Octopus Server's OIDC discovery endpoint to validate the token. This works for Octopus Cloud; a firewalled self-hosted server may not be reachable. See [OIDC Issuers](/docs/administration/access-identity/oidc-issuers/) for the full configuration reference.
{{% /notes %}}

## Provide cloud credentials

When Pulumi runs, your program also needs credentials for the cloud provider it manages. You can supply them in one of two ways:

- **Pulumi ESC (recommended).** Configure a [Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) environment to broker short-lived cloud credentials through OIDC. Your program receives temporary credentials scoped to exactly what it needs, and the deployment stores nothing but its Pulumi access token. Because ESC delivers those values the same way whether the consumer is an Octopus deployment or a developer's machine, a single environment definition works in both places.
- **Octopus accounts and variables.** Add the provider's credentials as an Octopus [account](https://octopus.com/docs/infrastructure/accounts) — for example an AWS or Azure account — or as sensitive variables for other clouds, and expose them to the Run a Script step.

{{% notes type="warning" %}}
Never commit cloud credentials or the Pulumi access token to your repository. Keep them in sensitive Octopus variables or accounts so the values stay protected and access is auditable.
{{% /notes %}}

## Run Pulumi in a deployment process

Add a **Run a Script** step to your project's deployment process and run the Pulumi CLI against a [stack](/docs/iac/concepts/stacks/). The following inline Bash script assumes the Pulumi program lives in an `infra/` directory of the deployed package:

```bash
cd infra

# Install the program's language dependencies and required plugins.
pulumi install

# Select the stack for the environment being deployed.
pulumi stack select acme/website/staging

# Apply the infrastructure changes.
pulumi up --yes
```

Bind `PULUMI_ACCESS_TOKEN` to the step from the sensitive variable you created, or run the OIDC `pulumi login` exchange before the other commands. Set the step's [execution container](https://octopus.com/docs/projects/steps/execution-containers-for-workers) image to `pulumi/pulumi` so the CLI and every language runtime are already present — no installation step required.

[`pulumi install`](/docs/iac/cli/commands/pulumi_install/) installs the program's language dependencies and required plugins, so the same step works for a program written in any supported language.

## Build a trunk-based CI/CD workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/operations/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there. Because Octopus is a delivery server, the work is split: your upstream CI system handles the pull request and packaging stages, and Octopus deploys each release and promotes it through its environments.

### Preview infrastructure changes

A [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) reports the proposed changes without modifying any resources. Run it on every pull request in your upstream CI system so reviewers see the infrastructure changes alongside the code diff.

Within Octopus, you can also preview before applying: run `pulumi preview` as an early step in the deployment process, then add a [manual intervention and approval step](https://octopus.com/docs/projects/built-in-step-templates/manual-intervention-and-approvals) that pauses the deployment until someone signs off on the preview. The `pulumi up` step runs only after approval.

To let reviewers exercise a change in a live environment before it merges, use a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions an ephemeral stack for the pull request and destroys it when the pull request closes.

### Deploy to staging on merge

When a pull request merges, your upstream CI system publishes a new package and creates an Octopus release. Octopus deploys that release to an environment that receives continuous delivery — such as a shared development or staging environment — by running `pulumi up` against the stack for that environment.

### Promote to production

Octopus [lifecycles](https://octopus.com/docs/releases/lifecycles) make the production deployment a deliberate, traceable step. Rather than rebuilding, you *promote* the same release that was validated in staging to the Production environment, where the deployment process runs `pulumi up` against the production stack. Trigger the promotion from a release marker in your upstream CI — for example, a moving `production` Git tag that you advance to a commit already verified in staging. Production never deploys an untested build.

## Speed up builds with caching

A fresh Octopus worker starts with an empty plugin cache, so Pulumi re-downloads its provider plugins on every deployment. Octopus has no native cross-deployment cache for these runs. To avoid the repeated downloads, bake the provider plugins into a custom image:

1. Derive an image from `pulumi/pulumi`.
1. Run [`pulumi plugin install`](/docs/iac/cli/commands/pulumi_plugin_install/) for each provider your program uses.
1. Use that image as the execution container for the Run a Script step.

This makes each deployment deterministic and removes plugin-download time from every run. See the [plugins documentation](/docs/iac/concepts/plugins/) for details.

## Report results on pull requests

Octopus Deploy is not aware of pull requests, but Pulumi Cloud's [version control integrations](/docs/integrations/version-control/) work independently of whichever system runs Pulumi. A version control integration lets Pulumi Cloud post infrastructure-change summaries as pull request comments and status checks, and link each stack update back to the commit and pull request that produced it. Pulumi maintains integrations for popular version control systems — see [Version Control](/docs/integrations/version-control/) for the current list.

## Additional resources

- [Continuous delivery](/docs/iac/operations/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [CI/CD troubleshooting guide](/docs/iac/operations/continuous-delivery/troubleshooting/) — diagnose common failures when running Pulumi in a pipeline.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to deployments and developers consistently.
- [OIDC Issuers](/docs/administration/access-identity/oidc-issuers/) — eliminate static tokens with short-lived, exchanged credentials.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral environments for pull requests.
- [Version Control](/docs/integrations/version-control/) — connect Pulumi Cloud to your version control system.
