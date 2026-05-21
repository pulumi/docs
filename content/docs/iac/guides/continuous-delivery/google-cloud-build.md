---
title_tag: "Using Google Cloud Build with Pulumi | CI/CD"
meta_desc: Run Pulumi in Google Cloud Build using the official Pulumi container images, and ship infrastructure through a trunk-based CI/CD workflow.
title: Google Cloud Build
h1: Using Google Cloud Build with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Google Cloud Build
        parent: iac-using-pulumi-cicd
        weight: 100
aliases:
- /docs/iac/using-pulumi/continuous-delivery/google-cloud-build/
- /docs/reference/cd-google-cloud-build/
- /docs/console/continuous-delivery/google-cloud-build/
- /docs/guides/continuous-delivery/google-cloud-build/
- /docs/using-pulumi/continuous-delivery/cd-google-cloud-build/
- /docs/guides/continuous-delivery/cd-google-cloud-build/
- /docs/using-pulumi/continuous-delivery/google-cloud-build/
- /docs/iac/packages-and-automation/continuous-delivery/google-cloud-build/
---

[Google Cloud Build](https://cloud.google.com/build/docs) is Google Cloud's serverless CI/CD platform. It runs builds as a series of container-image steps defined in a `cloudbuild.yaml` file, started by triggers that respond to repository events such as pull requests, branch pushes, and tags.

You run Pulumi in a build step by using one of Pulumi's official Docker images as the step's container image. Each image bundles the Pulumi CLI with a language runtime — `pulumi/pulumi-nodejs`, `pulumi/pulumi-python`, `pulumi/pulumi-go`, `pulumi/pulumi-dotnet`, and `pulumi/pulumi-java` — so a step can install dependencies and run Pulumi commands against a program written in any [supported language](/docs/iac/languages-sdks/) and targeting [any cloud provider](/registry/).

{{< cicd-cloud-note >}}

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A Google Cloud project with the [Cloud Build API](https://cloud.google.com/build/docs/set-up) enabled.
1. A source repository that Cloud Build can build from. Cloud Build connects to repositories hosted on GitHub, GitLab, or Bitbucket through a [repository connection](https://cloud.google.com/build/docs/repositories). (Cloud Source Repositories, Google's own hosted Git service, has been closed to new customers since June 2024.)
1. A Pulumi program committed to that repository. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Authenticate with Pulumi Cloud

Give your pipeline a Pulumi Cloud identity in one of two ways. **Choose one — you don't need both:**

- **A stored access token** — create a [Pulumi access token](/docs/administration/access-identity/access-tokens/) and keep it in [Secret Manager](https://cloud.google.com/secret-manager/docs), where a build step reads it at runtime.
- **OIDC** — exchange a short-lived OpenID Connect token for a Pulumi access token at build time, so no long-lived credential is stored anywhere. Prefer this where your CI/CD system supports it well.

This guide's examples use the stored-token path, because Cloud Build has no Pulumi-maintained OIDC integration yet — see [Authenticate without a stored token using OIDC](#authenticate-without-a-stored-token-using-oidc) below.

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a build step or a developer's machine, a single environment definition works in both places — you don't store separate cloud provider keys in Secret Manager.

### Store the access token in Secret Manager

Create a Pulumi access token, preferring an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the pipeline's identity isn't tied to an individual.

Store the token in Secret Manager and grant the Cloud Build service account permission to read it:

```bash
# Store the token as a secret.
printf '%s' "$PULUMI_ACCESS_TOKEN" | gcloud secrets create pulumi-access-token --data-file=-

# Grant the Cloud Build service account read access to the secret.
gcloud secrets add-iam-policy-binding pulumi-access-token \
  --member="serviceAccount:CLOUD_BUILD_SERVICE_ACCOUNT" \
  --role="roles/secretmanager.secretAccessor"
```

A build configuration then exposes the secret to a step as the `PULUMI_ACCESS_TOKEN` environment variable through its `availableSecrets` block, as shown in the examples below.

### Authenticate without a stored token using OIDC

You can avoid storing a static token by having Cloud Build obtain a short-lived [OpenID Connect (OIDC)](https://openid.net/developers/how-connect-works/) token at build time. A build step can request an OIDC id_token for the build's Google Cloud service account, and Pulumi Cloud can register that as a trusted [OIDC issuer](/docs/administration/access-identity/oidc-issuers/) and exchange it for a short-lived Pulumi access token.

Unlike GitHub Actions and GitLab CI, Cloud Build has no Pulumi-maintained action or component that performs this exchange for you — you would script the token request and the `pulumi login` exchange yourself. Until a dedicated integration exists, the stored-token path above is the simpler and recommended choice, and it's what the rest of this guide uses.

## The trunk-based development workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/guides/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there. This guide splits that across two build configurations:

- `cloudbuild-preview.yaml` runs `pulumi preview` on every pull request, surfacing the proposed changes for review.
- `cloudbuild-deploy.yaml` runs `pulumi up` when changes land — to staging on a push to `main`, and to production on a `release-*` tag.

Both configurations install your program's dependencies and run Pulumi from one of the official `pulumi/pulumi-*` images. The examples assume a Pulumi program in an `infra/` directory and stacks named `acme/website/staging` and `acme/website/production`. Only the step image and the dependency-install command differ between languages.

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```yaml
# cloudbuild-preview.yaml
steps:
  - name: 'pulumi/pulumi-nodejs'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        npm install
        pulumi preview --stack acme/website/staging
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

```yaml
# cloudbuild-deploy.yaml
steps:
  - name: 'pulumi/pulumi-nodejs'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        npm install
        if [ -n "$TAG_NAME" ]; then
          pulumi up --yes --stack acme/website/production
        else
          pulumi up --yes --stack acme/website/staging
        fi
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

{{% /choosable %}}
{{% choosable language python %}}

```yaml
# cloudbuild-preview.yaml
steps:
  - name: 'pulumi/pulumi-python'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        pip install -r requirements.txt
        pulumi preview --stack acme/website/staging
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

```yaml
# cloudbuild-deploy.yaml
steps:
  - name: 'pulumi/pulumi-python'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        pip install -r requirements.txt
        if [ -n "$TAG_NAME" ]; then
          pulumi up --yes --stack acme/website/production
        else
          pulumi up --yes --stack acme/website/staging
        fi
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

{{% /choosable %}}
{{% choosable language go %}}

```yaml
# cloudbuild-preview.yaml
steps:
  - name: 'pulumi/pulumi-go'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        go mod download
        pulumi preview --stack acme/website/staging
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

```yaml
# cloudbuild-deploy.yaml
steps:
  - name: 'pulumi/pulumi-go'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        go mod download
        if [ -n "$TAG_NAME" ]; then
          pulumi up --yes --stack acme/website/production
        else
          pulumi up --yes --stack acme/website/staging
        fi
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

{{% /choosable %}}
{{% choosable language csharp %}}

```yaml
# cloudbuild-preview.yaml
steps:
  - name: 'pulumi/pulumi-dotnet'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - 'pulumi preview --stack acme/website/staging'
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

```yaml
# cloudbuild-deploy.yaml
steps:
  - name: 'pulumi/pulumi-dotnet'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        if [ -n "$TAG_NAME" ]; then
          pulumi up --yes --stack acme/website/production
        else
          pulumi up --yes --stack acme/website/staging
        fi
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

{{% /choosable %}}
{{% choosable language java %}}

```yaml
# cloudbuild-preview.yaml
steps:
  - name: 'pulumi/pulumi-java'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - 'pulumi preview --stack acme/website/staging'
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

```yaml
# cloudbuild-deploy.yaml
steps:
  - name: 'pulumi/pulumi-java'
    dir: 'infra'
    entrypoint: 'bash'
    args:
      - '-c'
      - |
        if [ -n "$TAG_NAME" ]; then
          pulumi up --yes --stack acme/website/production
        else
          pulumi up --yes --stack acme/website/staging
        fi
    secretEnv: ['PULUMI_ACCESS_TOKEN']
availableSecrets:
  secretManager:
    - versionName: projects/$PROJECT_ID/secrets/pulumi-access-token/versions/latest
      env: 'PULUMI_ACCESS_TOKEN'
options:
  logging: CLOUD_LOGGING_ONLY
```

{{% /choosable %}}

{{< /chooser >}}

Pulumi runs non-interactively inside Cloud Build, so `pulumi up --yes` applies changes without a confirmation prompt. For C# and Java, the language runtime resolves and builds dependencies as part of the Pulumi run, so no separate install step is needed.

The deploy configuration reads the built-in `$TAG_NAME` substitution — which Cloud Build sets only for tag-triggered builds — to decide whether to update the staging or the production stack. The `availableSecrets` block reads the access token from Secret Manager and exposes it to the step as `PULUMI_ACCESS_TOKEN`, and `logging: CLOUD_LOGGING_ONLY` lets the build run without a Cloud Storage logs bucket.

To promote a release, push a tag that matches the `release-*` pattern:

```bash
git tag release-2026-05-21
git push origin release-2026-05-21
```

Keeping production on its own stack and deploying it only from a tag makes each production update a single, traceable Git operation, and ensures production never deploys from an untested commit.

To let reviewers exercise a change in a live environment, pair the preview build with a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions an ephemeral stack for the pull request and destroys it when the pull request closes.

{{% notes type="info" %}}
The Pulumi CLI doesn't automatically detect Cloud Build as a CI/CD system, so updates won't link back to the triggering build or commit on their own. To record that metadata in Pulumi Cloud, set the `PULUMI_CI_SYSTEM` environment variable, along with the `PULUMI_CI_*` fallback variables, in your build steps. See [adding support for CI/CD systems](/docs/iac/guides/continuous-delivery/#adding-support-for-cicd-systems).
{{% /notes %}}

## Report results on pull requests

By default, the output of a `pulumi preview` build lands in the Cloud Build logs. To surface the proposed infrastructure changes on the pull request itself, connect your repository to Pulumi Cloud with a [version control integration](/docs/integrations/version-control/).

These integrations work independently of Cloud Build: Pulumi Cloud posts a summary of resource changes as a pull request comment and status check, and links each stack update back to the commit and pull request that produced it. Pulumi maintains integrations for popular version control systems — see the [version control integrations](/docs/integrations/version-control/) documentation for the current list and setup instructions.

## Connect a repository and create a trigger

A trigger ties a repository event to a build configuration. To run the two build configurations above, create three triggers on the same repository:

1. Connect your GitHub, GitLab, or Bitbucket repository to Cloud Build by creating a [repository connection](https://cloud.google.com/build/docs/repositories) in the region where you intend to run builds.
1. Create a **pull request** trigger that runs `cloudbuild-preview.yaml` when a pull request targets `main`.
1. Create a **push** trigger that runs `cloudbuild-deploy.yaml` on pushes to the `main` branch.
1. Create a second **push** trigger that runs `cloudbuild-deploy.yaml` on tags matching `release-*`.

Because the deploy configuration inspects `$TAG_NAME` to choose the target stack, both push triggers can share the one file.

### Manage triggers as code

You can define those triggers — and the repository connection itself — as part of a Pulumi program with the [Google Cloud provider](/registry/packages/gcp/), rather than creating them by hand. Use the [`gcp.cloudbuild.Trigger`](/registry/packages/gcp/api-docs/cloudbuild/trigger/) resource for the triggers and [`gcp.cloudbuildv2.Repository`](/registry/packages/gcp/api-docs/cloudbuildv2/repository/) for the repository connection; each resource's Registry page has usage examples in every supported language. Managing triggers this way keeps your CI/CD configuration versioned and reviewed alongside the rest of your infrastructure.

## Additional resources

- [Continuous delivery](/docs/iac/guides/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) — exchange a CI/CD system's OIDC token for a short-lived Pulumi access token.
- [Version control integrations](/docs/integrations/version-control/) — pull request comments, status checks, and commit linking from Pulumi Cloud.
- [Google Cloud provider](/registry/packages/gcp/) — manage Cloud Build triggers, repository connections, and the rest of Google Cloud as code.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral environments created automatically for each pull request.
- [CI/CD troubleshooting](/docs/support/troubleshooting/ci-cd/) — diagnose common failures when running Pulumi in a pipeline.
