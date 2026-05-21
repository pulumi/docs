---
title_tag: "Using GitHub Actions with Pulumi | CI/CD"
meta_desc: Run Pulumi in GitHub Actions with the official Pulumi GitHub Action, and ship infrastructure through a trunk-based CI/CD workflow.
title: GitHub Actions
h1: Using GitHub Actions with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: GitHub Actions
        parent: iac-using-pulumi-cicd
        weight: 80
aliases:
- /docs/iac/using-pulumi/continuous-delivery/github-actions/
- /docs/reference/cd-github-actions/
- /docs/console/continuous-delivery/github-actions/
- /docs/guides/continuous-delivery/github-actions/
- /docs/using-pulumi/continuous-delivery/cd-github-actions/
- /docs/guides/continuous-delivery/cd-github-actions/
- /docs/using-pulumi/continuous-delivery/github-actions/
- /docs/iac/packages-and-automation/continuous-delivery/github-actions/
---

[GitHub Actions](https://docs.github.com/actions) is the CI/CD service built into GitHub. It runs workflows defined in YAML files under `.github/workflows/` in your repository, triggered by events such as pull requests, pushes, and tags.

You run Pulumi in a workflow with the [Pulumi GitHub Action](https://github.com/pulumi/actions) (`pulumi/actions`), an official, Pulumi-maintained action that installs the Pulumi CLI and runs Pulumi commands as a workflow step. Because it wraps the CLI, it works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/) and targeting [any cloud provider](/registry/).

{{< cicd-cloud-note >}}

## Pulumi's GitHub Actions

Pulumi publishes and maintains several actions on the GitHub Marketplace. This guide centers on `pulumi/actions`, the action that runs Pulumi commands; the others handle authentication and configuration and are covered in the sections below.

| Action | Purpose |
|--------|---------|
| [`pulumi/actions`](https://github.com/pulumi/actions) | Installs the Pulumi CLI and runs a Pulumi command (`preview`, `up`, `destroy`, and so on) as a workflow step. |
| [`pulumi/setup-pulumi`](https://github.com/pulumi/setup-pulumi) | Installs the Pulumi CLI only, for workflows that invoke `pulumi` commands directly rather than through `pulumi/actions`. |
| [`pulumi/auth-actions`](https://github.com/pulumi/auth-actions) | Exchanges a GitHub OIDC token for a short-lived Pulumi Cloud access token, removing the need to store a token as a secret. |
| [`pulumi/esc-action`](https://github.com/pulumi/esc-action) | Opens a [Pulumi ESC](/docs/esc/) environment and injects its environment variables — cloud credentials, secrets, and configuration — into the workflow. |
| [`pulumi/esc-export-secrets-action`](https://github.com/pulumi/esc-export-secrets-action) | Exports GitHub Actions secrets into a Pulumi ESC environment, useful when migrating existing secrets to ESC. |

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A GitHub repository.
1. A Pulumi program committed to that repository. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Authenticate with Pulumi Cloud

Your workflow authenticates to Pulumi Cloud with a single [Pulumi access token](/docs/administration/access-identity/access-tokens/), supplied through the `PULUMI_ACCESS_TOKEN` environment variable. Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the workflow's identity isn't tied to an individual.

Add the token as an [encrypted secret](https://docs.github.com/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions) named `PULUMI_ACCESS_TOKEN` under your repository's **Settings > Secrets and variables > Actions**. The workflow then reads it through the `secrets` context, as shown in the examples below.

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a workflow or a developer's machine, a single environment definition works in both places — you don't store separate cloud provider keys as repository secrets.

## Authenticate without a stored token using OIDC

You can remove the static token entirely. GitHub Actions can issue a short-lived [OpenID Connect (OIDC)](https://docs.github.com/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect) token for a workflow job. Register GitHub Actions as a trusted [OIDC issuer](/docs/administration/access-identity/oidc-issuers/github/) in Pulumi Cloud, and the [`pulumi/auth-actions`](https://github.com/pulumi/auth-actions) action exchanges that OIDC token for a short-lived Pulumi access token at runtime — no long-lived credential is stored as a repository secret.

Pair it with [`pulumi/esc-action`](https://github.com/pulumi/esc-action) to pull cloud credentials, secrets, and configuration from a [Pulumi ESC](/docs/esc/) environment. This is the recommended way to provide cloud credentials in GitHub Actions because it's:

- **Provider-agnostic** — works with [AWS](/docs/esc/guides/configuring-oidc/aws/), [Azure](/docs/esc/guides/configuring-oidc/azure/), [Google Cloud](/docs/esc/guides/configuring-oidc/gcp/), and others through the same pattern.
- **Portable** — the same ESC environment works locally and in any CI/CD system, not only GitHub Actions.
- **Centralized** — credential configuration lives in ESC, not scattered across individual workflows.

A job that uses OIDC needs the `id-token: write` permission. Add `pull-requests: write` as well if the workflow comments on pull requests:

```yaml
permissions:
  id-token: write
  contents: read
  pull-requests: write # Only needed when commenting on pull requests
```

The job below authenticates with `pulumi/auth-actions`, loads an ESC environment with `pulumi/esc-action`, and then runs Pulumi — with no `PULUMI_ACCESS_TOKEN` secret and no stored cloud provider keys:

```yaml
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: infra/package.json
      - name: Authenticate with Pulumi Cloud
        uses: pulumi/auth-actions@v1
        with:
          organization: acme
          requested-token-type: urn:pulumi:token-type:access_token:organization
      - name: Load the ESC environment
        uses: pulumi/esc-action@v1
        with:
          environment: acme/website/ci
      - run: npm install
        working-directory: infra
      - uses: pulumi/actions@v7
        with:
          command: preview
          stack-name: acme/website/staging
          work-dir: infra
```

For more detail, see the [Pulumi ESC GitHub Action documentation](/docs/esc/integrations/dev-tools/github/).

To configure OIDC directly between GitHub Actions and a cloud provider without ESC — for example, with `aws-actions/configure-aws-credentials` and a `role-to-assume` input — follow that provider's GitHub Actions OIDC guide. This approach is provider-specific: each cloud requires its own trust relationship, whereas ESC configures that trust once and reuses it everywhere.

## The trunk-based development workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/guides/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there. This guide splits that across two workflow files:

- `.github/workflows/pr.yml` runs `pulumi preview` on every pull request, surfacing the proposed changes for review.
- `.github/workflows/main.yml` runs `pulumi up` when changes land — to staging on a push to `main`, and to production on a `release-*` tag.

Both files check out the repository, set up your program's language, install dependencies, and then invoke `pulumi/actions`. The examples assume a Pulumi program in an `infra/` directory and stacks named `acme/website/staging` and `acme/website/production`. Only the language setup and dependency-install steps differ between languages:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```yaml
# .github/workflows/pr.yml
name: Pulumi preview
on:
  pull_request:
jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: infra/package.json
      - run: npm install
        working-directory: infra
      - uses: pulumi/actions@v7
        with:
          command: preview
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

```yaml
# .github/workflows/main.yml
name: Pulumi deploy
on:
  push:
    branches:
      - main
    tags:
      - 'release-*'
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version-file: infra/package.json
      - run: npm install
        working-directory: infra

      # Push to main: deploy to the staging environment.
      - name: Deploy to staging
        if: github.ref == 'refs/heads/main'
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      # Release tag: promote to production.
      - name: Deploy to production
        if: startsWith(github.ref, 'refs/tags/release-')
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/production
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

{{% /choosable %}}
{{% choosable language python %}}

```yaml
# .github/workflows/pr.yml
name: Pulumi preview
on:
  pull_request:
jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
        working-directory: infra
      - uses: pulumi/actions@v7
        with:
          command: preview
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

```yaml
# .github/workflows/main.yml
name: Pulumi deploy
on:
  push:
    branches:
      - main
    tags:
      - 'release-*'
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
        working-directory: infra

      # Push to main: deploy to the staging environment.
      - name: Deploy to staging
        if: github.ref == 'refs/heads/main'
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      # Release tag: promote to production.
      - name: Deploy to production
        if: startsWith(github.ref, 'refs/tags/release-')
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/production
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

{{% /choosable %}}
{{% choosable language go %}}

```yaml
# .github/workflows/pr.yml
name: Pulumi preview
on:
  pull_request:
jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v6
        with:
          go-version: 'stable'
      - run: go mod download
        working-directory: infra
      - uses: pulumi/actions@v7
        with:
          command: preview
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

```yaml
# .github/workflows/main.yml
name: Pulumi deploy
on:
  push:
    branches:
      - main
    tags:
      - 'release-*'
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-go@v6
        with:
          go-version: 'stable'
      - run: go mod download
        working-directory: infra

      # Push to main: deploy to the staging environment.
      - name: Deploy to staging
        if: github.ref == 'refs/heads/main'
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      # Release tag: promote to production.
      - name: Deploy to production
        if: startsWith(github.ref, 'refs/tags/release-')
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/production
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

{{% /choosable %}}
{{% choosable language csharp %}}

```yaml
# .github/workflows/pr.yml
name: Pulumi preview
on:
  pull_request:
jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v5
        with:
          dotnet-version: '10.0.x'
      - uses: pulumi/actions@v7
        with:
          command: preview
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

```yaml
# .github/workflows/main.yml
name: Pulumi deploy
on:
  push:
    branches:
      - main
    tags:
      - 'release-*'
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-dotnet@v5
        with:
          dotnet-version: '10.0.x'

      # Push to main: deploy to the staging environment.
      - name: Deploy to staging
        if: github.ref == 'refs/heads/main'
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      # Release tag: promote to production.
      - name: Deploy to production
        if: startsWith(github.ref, 'refs/tags/release-')
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/production
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

{{% /choosable %}}
{{% choosable language java %}}

```yaml
# .github/workflows/pr.yml
name: Pulumi preview
on:
  pull_request:
jobs:
  preview:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v5
        with:
          distribution: temurin
          java-version: '21'
      - uses: pulumi/actions@v7
        with:
          command: preview
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

```yaml
# .github/workflows/main.yml
name: Pulumi deploy
on:
  push:
    branches:
      - main
    tags:
      - 'release-*'
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v5
        with:
          distribution: temurin
          java-version: '21'

      # Push to main: deploy to the staging environment.
      - name: Deploy to staging
        if: github.ref == 'refs/heads/main'
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

      # Release tag: promote to production.
      - name: Deploy to production
        if: startsWith(github.ref, 'refs/tags/release-')
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/production
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

{{% /choosable %}}

{{< /chooser >}}

The `pulumi/actions` step runs Pulumi non-interactively, so `pulumi up` applies changes without a confirmation prompt. For Java and C#, the language runtime resolves and builds dependencies as part of the Pulumi run, so no separate install step is needed.

To promote a release, push a tag that matches the `release-*` pattern:

```bash
git tag release-2026-05-20
git push origin release-2026-05-20
```

Keeping production on its own stack and deploying it only from a tag makes each production update a single, traceable Git operation, and ensures production never deploys from an untested commit.

To let reviewers exercise a change in a live environment, pair the preview step with a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions an ephemeral stack for the pull request and destroys it when the pull request closes.

{{% notes type="info" %}}
The Pulumi CLI automatically detects when it runs inside GitHub Actions and records the build and commit metadata. Each update in Pulumi Cloud then links back to the workflow run and pull request that triggered it — no extra configuration required.
{{% /notes %}}

## Report results on pull requests

When a workflow runs `pulumi preview` on a pull request, you'll usually want the proposed changes summarized on the pull request itself rather than buried in the workflow logs. There are two ways to do this.

### Pulumi GitHub App (recommended)

The [Pulumi GitHub App](/docs/integrations/version-control/github-app/) lets Pulumi Cloud post a rich summary of resource changes — with links to the Pulumi Cloud console — directly on the pull request. Install it once on your GitHub organization and it works for every repository, regardless of which CI/CD system runs Pulumi.

### Comments from the action

Without the GitHub App, the `pulumi/actions` action can post the raw CLI output itself. Set `comment-on-pr: true` and pass a `github-token`:

```yaml
- uses: pulumi/actions@v7
  with:
    command: preview
    stack-name: acme/website/staging
    work-dir: infra
    comment-on-pr: true
    github-token: ${{ secrets.GITHUB_TOKEN }}
  env:
    PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
```

For push-triggered deployments that have no pull request to comment on, set `comment-on-summary: true` to publish the result to the [workflow run summary](https://docs.github.com/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary) instead. The two inputs can be combined.

For the action's full set of inputs, see the [`pulumi/actions` documentation](https://github.com/pulumi/actions).

## Stack outputs

When Pulumi updates a stack, the values your program exports as [stack outputs](/docs/iac/concepts/stacks/#outputs) — a service endpoint, a bucket name, a connection string — become available to later steps in the workflow.

Give the `pulumi/actions` step an `id`, and each stack output becomes a step output at `steps.<id>.outputs.<name>`:

```yaml
- name: Deploy
  id: pulumi
  uses: pulumi/actions@v7
  with:
    command: up
    stack-name: acme/website/staging
    work-dir: infra
  env:
    PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}
- name: Use a stack output
  run: echo "Deployed to ${{ steps.pulumi.outputs.url }}"
```

To pass an output to a downstream job, promote it to a job output and depend on the producing job with `needs`:

```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    outputs:
      url: ${{ steps.pulumi.outputs.url }}
    steps:
      - uses: actions/checkout@v4
      - id: pulumi
        uses: pulumi/actions@v7
        with:
          command: up
          stack-name: acme/website/staging
          work-dir: infra
        env:
          PULUMI_ACCESS_TOKEN: ${{ secrets.PULUMI_ACCESS_TOKEN }}

  integration-test:
    runs-on: ubuntu-latest
    needs: deploy
    steps:
      - run: ./run-tests.sh
        env:
          SERVICE_URL: ${{ needs.deploy.outputs.url }}
```

{{% notes type="warning" %}}
Stack outputs can contain sensitive values such as passwords or private keys. Set `suppress-outputs: true` on the `pulumi/actions` step to keep output values out of the workflow logs, and store secrets as [encrypted secrets](https://docs.github.com/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions) rather than passing them through stack outputs when possible.
{{% /notes %}}

## Speed up runs with caching

GitHub Actions starts each run on a clean runner, so Pulumi re-downloads its plugins and policy packs every time. Caching `~/.pulumi/plugins` and `~/.pulumi/policies` with [`actions/cache`](https://github.com/actions/cache) avoids that. Add this step before the `pulumi/actions` step:

```yaml
- name: Cache Pulumi plugins and policy packs
  uses: actions/cache@v4
  with:
    path: |
      ~/.pulumi/plugins
      ~/.pulumi/policies
    key: ${{ runner.os }}-pulumi-${{ hashFiles('infra/package.json') }}
    restore-keys: |
      ${{ runner.os }}-pulumi-
```

The cache key includes a hash of your dependency manifest so the cache is rebuilt when dependencies change; use the file appropriate to your language — `package.json`, `requirements.txt`, `go.sum`, the `.csproj`, or `pom.xml`. The `restore-keys` fallback lets a run reuse a recent cache even when there's no exact match.

## Control concurrent runs

When pull requests stack up or commits land faster than a workflow finishes, runs accumulate. [Concurrency groups](https://docs.github.com/actions/using-jobs/using-concurrency) bound how many run at once.

For **pull request previews**, key the group to the pull request and cancel superseded runs so reviewers always see the result of the latest commit:

```yaml
concurrency:
  group: pulumi-pr-${{ github.event.pull_request.number }}
  cancel-in-progress: true
```

For **deployments**, use a shared group *without* `cancel-in-progress` so updates queue instead of being dropped — canceling a deployment mid-run can leave infrastructure half-applied:

```yaml
concurrency:
  group: pulumi-deploy
```

`concurrency` is a top-level workflow key, placed alongside `on` and `jobs`. You can also scope it to a single job when a workflow contains jobs with different concurrency needs.

## Managing GitHub with Pulumi

You can manage GitHub itself — repositories, teams, branch protection rules, and Actions secrets — as code with the [GitHub provider](/registry/packages/github/) in the Pulumi Registry. This lets you define the workflow secrets and repository settings this guide describes as part of a Pulumi program.

## Additional resources

- [Continuous delivery](/docs/iac/guides/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [`pulumi/actions`](https://github.com/pulumi/actions) — the Pulumi GitHub Action's full input reference.
- [Pulumi GitHub App](/docs/integrations/version-control/github-app/) — rich pull request comments and commit checks from Pulumi Cloud.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to workflows and developers consistently.
- [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) — exchange a CI/CD system's OIDC token for a short-lived Pulumi access token.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral environments created automatically for each pull request.
- [CI/CD troubleshooting](/docs/support/troubleshooting/ci-cd/) — diagnose common failures when running Pulumi in a pipeline.
