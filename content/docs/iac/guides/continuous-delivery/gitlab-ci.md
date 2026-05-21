---
title_tag: "Using GitLab CI/CD with Pulumi | CI/CD"
meta_desc: Run Pulumi in GitLab CI/CD pipelines and ship infrastructure through a trunk-based workflow, with static-token or OIDC authentication.
title: GitLab CI/CD
h1: Using GitLab CI/CD with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: GitLab CI/CD
        parent: iac-using-pulumi-cicd
        weight: 90
aliases:
- /docs/iac/using-pulumi/continuous-delivery/gitlab-ci/
- /docs/reference/cd-gitlab-ci/
- /docs/console/continuous-delivery/gitlab-ci/
- /docs/guides/continuous-delivery/gitlab-ci/
- /docs/using-pulumi/continuous-delivery/cd-gitlab-ci/
- /docs/guides/continuous-delivery/cd-gitlab-ci/
- /docs/using-pulumi/continuous-delivery/gitlab-ci/
- /docs/iac/packages-and-automation/continuous-delivery/gitlab-ci/
---

[GitLab CI/CD](https://docs.gitlab.com/ci/) is the CI/CD service built into GitLab. It runs pipelines defined in a `.gitlab-ci.yml` file at the root of your repository, triggered by events such as merge requests, pushes, and tags.

You run Pulumi in a pipeline by invoking the Pulumi CLI directly. The official [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) container images ship the CLI together with a language runtime, so a job can run `pulumi preview` or `pulumi up` with no install step. Because the pipeline runs the CLI, it works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/) and targeting [any cloud provider](/registry/).

{{< cicd-cloud-note >}}

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A GitLab project.
1. A Pulumi program committed to that project. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Authenticate with Pulumi Cloud

Your pipeline authenticates to Pulumi Cloud with a single [Pulumi access token](/docs/administration/access-identity/access-tokens/), supplied through the `PULUMI_ACCESS_TOKEN` environment variable. Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the pipeline's identity isn't tied to an individual.

Add the token as a [CI/CD variable](https://docs.gitlab.com/ci/variables/) named `PULUMI_ACCESS_TOKEN` under your project's **Settings > CI/CD > Variables**. Mark it **Masked** so it doesn't appear in job logs, and **Protected** so it's exposed only to pipelines running on [protected branches and tags](https://docs.gitlab.com/user/project/protected_branches/). The Pulumi CLI reads the variable from the environment automatically — no explicit `pulumi login` is required.

{{% notes type="info" %}}
A protected CI/CD variable is available only to jobs that run on a protected branch or tag. If a job that runs on an unprotected branch needs the token, either remove the **Protected** flag or extend branch protection to those branches with a [wildcard rule](https://docs.gitlab.com/user/project/protected_branches/#protect-multiple-branches-with-wildcard-rules).
{{% /notes %}}

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a pipeline or a developer's machine, a single environment definition works in both places — you don't store separate cloud provider keys as CI/CD variables.

## Authenticate without a stored token using OIDC

You can remove the static token entirely. GitLab CI/CD can issue a short-lived [OpenID Connect (OIDC)](https://docs.gitlab.com/ci/secrets/id_token_authentication/) `id_token` for a job. Register GitLab as a trusted [OIDC issuer](/docs/administration/access-identity/oidc-issuers/gitlab/) in Pulumi Cloud, and the job exchanges that `id_token` for a short-lived Pulumi access token at runtime — no long-lived credential is stored as a CI/CD variable.

The trust flows inbound: GitLab issues the `id_token`, and `pulumi login --oidc-token` exchanges it with Pulumi Cloud for an access token. A job requests the token with the `id_tokens` keyword and then logs in before running Pulumi:

```yaml
variables:
  PULUMI_ORG: acme

.pulumi:
  id_tokens:
    PULUMI_OIDC_TOKEN:
      aud: urn:pulumi:org:$PULUMI_ORG
  before_script:
    - pulumi login --oidc-token "$PULUMI_OIDC_TOKEN" --oidc-org "$PULUMI_ORG"
```

For the full setup — registering the issuer and writing the authorization policy that controls which projects and branches may exchange a token — see [Configuring OpenID Connect for GitLab](/docs/administration/access-identity/oidc-issuers/gitlab/) and the central [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) reference.

## The trunk-based development workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/guides/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there. A single `.gitlab-ci.yml` covers the whole flow with three jobs:

- `preview` runs `pulumi preview` on every merge request, surfacing the proposed changes for review.
- `deploy-staging` runs `pulumi up` against the staging stack when changes land on `main`.
- `deploy-production` runs `pulumi up` against the production stack when a `release-*` tag is pushed.

GitLab [`rules`](https://docs.gitlab.com/ci/yaml/#rules) decide which jobs run for a given pipeline. The examples assume a Pulumi program in an `infra/` directory and stacks named `acme/website/staging` and `acme/website/production`. A hidden `.pulumi` job, reused through [`extends`](https://docs.gitlab.com/ci/yaml/#extends), holds the steps the three jobs share; only the image and the dependency-install command differ between languages:

{{< chooser language "typescript,python,go,csharp,java" >}}

{{% choosable language typescript %}}

```yaml
# .gitlab-ci.yml
stages:
  - preview
  - deploy

default:
  image:
    name: pulumi/pulumi-nodejs:latest
    entrypoint: [""]

variables:
  PULUMI_STACK_STAGING: acme/website/staging
  PULUMI_STACK_PRODUCTION: acme/website/production

# Shared setup: enter the program directory and install dependencies.
.pulumi:
  before_script:
    - cd infra
    - npm ci

# Merge request: preview the proposed changes.
preview:
  extends: .pulumi
  stage: preview
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
  script:
    - pulumi preview --stack "$PULUMI_STACK_STAGING"

# Push to main: deploy to the staging environment.
deploy-staging:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  environment:
    name: staging
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_STAGING"

# Release tag: promote to production.
deploy-production:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_TAG =~ /^release-/
  environment:
    name: production
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_PRODUCTION"
```

{{% /choosable %}}
{{% choosable language python %}}

```yaml
# .gitlab-ci.yml
stages:
  - preview
  - deploy

default:
  image:
    name: pulumi/pulumi-python:latest
    entrypoint: [""]

variables:
  PULUMI_STACK_STAGING: acme/website/staging
  PULUMI_STACK_PRODUCTION: acme/website/production

# Shared setup: enter the program directory and install dependencies.
.pulumi:
  before_script:
    - cd infra
    - pip install -r requirements.txt

# Merge request: preview the proposed changes.
preview:
  extends: .pulumi
  stage: preview
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
  script:
    - pulumi preview --stack "$PULUMI_STACK_STAGING"

# Push to main: deploy to the staging environment.
deploy-staging:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  environment:
    name: staging
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_STAGING"

# Release tag: promote to production.
deploy-production:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_TAG =~ /^release-/
  environment:
    name: production
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_PRODUCTION"
```

{{% /choosable %}}
{{% choosable language go %}}

```yaml
# .gitlab-ci.yml
stages:
  - preview
  - deploy

default:
  image:
    name: pulumi/pulumi-go:latest
    entrypoint: [""]

variables:
  PULUMI_STACK_STAGING: acme/website/staging
  PULUMI_STACK_PRODUCTION: acme/website/production

# Shared setup: enter the program directory and install dependencies.
.pulumi:
  before_script:
    - cd infra
    - go mod download

# Merge request: preview the proposed changes.
preview:
  extends: .pulumi
  stage: preview
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
  script:
    - pulumi preview --stack "$PULUMI_STACK_STAGING"

# Push to main: deploy to the staging environment.
deploy-staging:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  environment:
    name: staging
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_STAGING"

# Release tag: promote to production.
deploy-production:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_TAG =~ /^release-/
  environment:
    name: production
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_PRODUCTION"
```

{{% /choosable %}}
{{% choosable language csharp %}}

```yaml
# .gitlab-ci.yml
stages:
  - preview
  - deploy

default:
  image:
    name: pulumi/pulumi-dotnet:latest
    entrypoint: [""]

variables:
  PULUMI_STACK_STAGING: acme/website/staging
  PULUMI_STACK_PRODUCTION: acme/website/production

# Shared setup: enter the program directory.
# The .NET runtime restores and builds the project during the Pulumi run.
.pulumi:
  before_script:
    - cd infra

# Merge request: preview the proposed changes.
preview:
  extends: .pulumi
  stage: preview
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
  script:
    - pulumi preview --stack "$PULUMI_STACK_STAGING"

# Push to main: deploy to the staging environment.
deploy-staging:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  environment:
    name: staging
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_STAGING"

# Release tag: promote to production.
deploy-production:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_TAG =~ /^release-/
  environment:
    name: production
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_PRODUCTION"
```

{{% /choosable %}}
{{% choosable language java %}}

```yaml
# .gitlab-ci.yml
stages:
  - preview
  - deploy

default:
  image:
    name: pulumi/pulumi-java:latest
    entrypoint: [""]

variables:
  PULUMI_STACK_STAGING: acme/website/staging
  PULUMI_STACK_PRODUCTION: acme/website/production

# Shared setup: enter the program directory.
# The Java runtime resolves and builds the project during the Pulumi run.
.pulumi:
  before_script:
    - cd infra

# Merge request: preview the proposed changes.
preview:
  extends: .pulumi
  stage: preview
  rules:
    - if: $CI_PIPELINE_SOURCE == "merge_request_event"
  script:
    - pulumi preview --stack "$PULUMI_STACK_STAGING"

# Push to main: deploy to the staging environment.
deploy-staging:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_BRANCH == "main"
  environment:
    name: staging
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_STAGING"

# Release tag: promote to production.
deploy-production:
  extends: .pulumi
  stage: deploy
  rules:
    - if: $CI_COMMIT_TAG =~ /^release-/
  environment:
    name: production
  script:
    - pulumi up --yes --stack "$PULUMI_STACK_PRODUCTION"
```

{{% /choosable %}}

{{< /chooser >}}

The `pulumi up --yes` flag applies changes without an interactive confirmation prompt, which is required in a non-interactive pipeline. The `environment` keyword records each deployment against a [GitLab environment](https://docs.gitlab.com/ci/environments/), giving you a deployment history and a one-click rollback in the GitLab UI.

To promote a release, push a tag that matches the `release-*` pattern:

```bash
git tag release-2026-05-21
git push origin release-2026-05-21
```

Keeping production on its own stack and deploying it only from a tag makes each production update a single, traceable Git operation, and ensures production never deploys from an untested commit.

To let reviewers exercise a change in a live environment, pair the `preview` job with a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions an ephemeral stack for the merge request and destroys it when the merge request closes.

{{% notes type="info" %}}
The Pulumi CLI automatically detects when it runs inside GitLab CI/CD and records the build and commit metadata. Each update in Pulumi Cloud then links back to the pipeline and merge request that triggered it — no extra configuration required.
{{% /notes %}}

## Report results to GitLab

When a pipeline runs `pulumi preview` on a merge request, you'll usually want the proposed changes summarized on the merge request itself rather than buried in the job logs. The [Pulumi GitLab integration](/docs/integrations/version-control/gitlab/) does this: connect your GitLab group to Pulumi Cloud once, and Pulumi posts a summary of resource changes — with links to the Pulumi Cloud console — as a merge request comment, along with commit status checks. It works for every project in the group regardless of which CI/CD system runs Pulumi.

## Speed up runs with caching

GitLab CI/CD starts each job in a fresh container, so Pulumi re-downloads its plugins and policy packs every time. GitLab's [`cache`](https://docs.gitlab.com/ci/caching/) can only store paths inside the project directory, so point [`PULUMI_HOME`](/docs/iac/cli/environment-variables/) at a directory in the workspace and cache that:

```yaml
variables:
  PULUMI_HOME: $CI_PROJECT_DIR/.pulumi

cache:
  key:
    files:
      - infra/package-lock.json
  paths:
    - .pulumi/plugins
    - .pulumi/policies
```

Keying the cache on your dependency manifest rebuilds it when dependencies change; use the file appropriate to your language — `package-lock.json`, `requirements.txt`, `go.sum`, the `.csproj`, or `pom.xml`.

## Serialize deployments

When commits land faster than a pipeline finishes, deployment jobs can overlap. Running two `pulumi up` jobs against the same stack at once causes one to fail on an [update conflict](/docs/support/troubleshooting/common-issues/update-conflicts/). Assign deployment jobs a [`resource_group`](https://docs.gitlab.com/ci/resource_groups/) so GitLab runs them one at a time:

```yaml
deploy-staging:
  # ...
  resource_group: staging

deploy-production:
  # ...
  resource_group: production
```

Jobs in the same resource group queue instead of running concurrently, while jobs in different groups — staging and production here — still run in parallel.

## Managing GitLab with Pulumi

You can manage GitLab itself — projects, groups, branch protection rules, and CI/CD variables — as code with the [GitLab provider](/registry/packages/gitlab/) in the Pulumi Registry. This lets you define the CI/CD variables and project settings this guide describes as part of a Pulumi program.

## Additional resources

- [Continuous delivery](/docs/iac/guides/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Pulumi GitLab integration](/docs/integrations/version-control/gitlab/) — merge request comments, commit statuses, and review stacks from Pulumi Cloud.
- [Configuring OpenID Connect for GitLab](/docs/administration/access-identity/oidc-issuers/gitlab/) — register GitLab as a trusted OIDC issuer.
- [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) — exchange a CI/CD system's OIDC token for a short-lived Pulumi access token.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral environments created automatically for each merge request.
- [CI/CD troubleshooting](/docs/support/troubleshooting/ci-cd/) — diagnose common failures when running Pulumi in a pipeline.
