---
title_tag: "Using Travis CI with Pulumi | CI/CD"
meta_desc: Run Pulumi in a Travis CI build to preview and deploy infrastructure through a trunk-based CI/CD workflow.
title: Travis CI
h1: Using Travis CI with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Travis CI
        parent: iac-operations-cicd
        weight: 160
aliases:
- /docs/iac/guides/continuous-delivery/travis/
- /docs/iac/using-pulumi/continuous-delivery/travis/
- /docs/reference/cd-travis/
- /docs/console/continuous-delivery/travis/
- /docs/guides/continuous-delivery/travis/
- /docs/using-pulumi/continuous-delivery/cd-travis/
- /docs/guides/continuous-delivery/cd-travis/
- /docs/using-pulumi/continuous-delivery/travis/
- /docs/iac/packages-and-automation/continuous-delivery/travis/
---

[Travis CI](https://www.travis-ci.com/) is a CI/CD service that builds and tests projects hosted in source control. You run Pulumi in a Travis build by installing the Pulumi CLI and invoking it from a `.travis.yml` file in your repository.

Because Travis runs the CLI directly, this works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/) and with [any cloud provider](/registry/) Pulumi supports.

{{< cicd-cloud-note >}}

{{< pulumi-docker-images-note >}}

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A Travis CI account with your repository activated.
1. A Git repository connected to Travis CI.
1. A Pulumi program. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Install and configure Pulumi

Travis runs the build steps defined in a `.travis.yml` file in the root of your repository. Install the Pulumi CLI in the `before_install` phase so later phases can call it:

```yaml
# .travis.yml
language: node_js
node_js:
  - lts/*

before_install:
  - curl -fsSL https://get.pulumi.com | sh
  - export PATH="$PATH:$HOME/.pulumi/bin"

script:
  - pulumi version
```

As an alternative to installing the CLI on each build, you can run your build steps inside one of Pulumi's official [container images](https://github.com/pulumi/pulumi-docker-containers), which ship the Pulumi CLI and a language runtime preinstalled. Enable Travis's Docker service and select the image for your language:

```yaml
language: minimal
services:
  - docker

script:
  - docker run --rm -e PULUMI_ACCESS_TOKEN -v "$PWD:/work" -w /work/infra
      pulumi/pulumi-nodejs bash -c "npm ci && pulumi preview --stack acme/website/staging"
```

## Authenticate with Pulumi Cloud

When your pipeline uses Pulumi Cloud as its backend, it needs a single [Pulumi access token](/docs/administration/access-identity/access-tokens/) to operate. Prefer an organization or team token over a personal one.

Provide the token to the build as the `PULUMI_ACCESS_TOKEN` environment variable. Set it as an encrypted variable so it isn't exposed in build logs or committed to source control. The recommended way is the Travis repository settings — under **Settings → Environment Variables** add `PULUMI_ACCESS_TOKEN` and leave **Display value in build log** off. You can also encrypt it into `.travis.yml` with the Travis CLI:

```bash
travis encrypt PULUMI_ACCESS_TOKEN=pul-xxxxxxxx --add env.global
```

The Pulumi CLI reads `PULUMI_ACCESS_TOKEN` automatically and logs in non-interactively — no `pulumi login` step is required.

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a pipeline or a developer's machine, a single environment definition works in both places — you don't store separate cloud provider keys in Travis.

## The trunk-based development workflow

The most common way to run Pulumi in Travis CI follows a trunk-based development model, where work merges into a single main branch and deployments flow outward from there:

1. **Open a pull request.** The build runs `pulumi preview` and surfaces the proposed changes for review.
1. **Merge to the main branch.** The build runs `pulumi up` to deploy the change to an environment that receives continuous delivery, such as a shared development or staging environment.
1. **Promote to production.** Pushing a git tag triggers a deployment to production, keeping production updates deliberate and traceable.

The `.travis.yml` below implements all three stages with conditional jobs. It assumes a Pulumi program in an `infra/` directory and stacks named `acme/website/staging` and `acme/website/production`:

```yaml
# .travis.yml
language: node_js
node_js:
  - lts/*

before_install:
  - curl -fsSL https://get.pulumi.com | sh
  - export PATH="$PATH:$HOME/.pulumi/bin"

# Skip the default root-level `npm install`; the Pulumi program lives in infra/.
install: true

jobs:
  include:
    # Pull request: preview the changes the merge would make.
    - stage: preview
      if: type = pull_request
      script:
        - cd infra && npm ci
        - pulumi preview --stack acme/website/staging

    # Push to the main branch: deploy to the staging environment.
    - stage: deploy to staging
      if: branch = main AND type = push AND tag IS blank
      script:
        - cd infra && npm ci
        - pulumi up --yes --stack acme/website/staging

    # Tag push: promote to production.
    - stage: deploy to production
      if: tag IS present
      script:
        - cd infra && npm ci
        - pulumi up --yes --stack acme/website/production
```

To promote a release, push a tag:

```bash
git tag release-2026-05-20
git push origin release-2026-05-20
```

Travis decides *when* to start a build — on pull requests, branch pushes, and tags — primarily through your repository's Travis settings (for example, **Build pushed branches** and **Build pushed pull requests**). The `.travis.yml` file can further restrict which branches or tags trigger a build via the top-level `branches:` key, and the `if:` conditions above then select which job runs for each build.

For an optional ephemeral environment on each pull request, pair the preview job with a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions and tears down a per-PR environment automatically.

{{% notes type="info" %}}
The Pulumi CLI automatically detects when it runs inside Travis CI and records the build and commit metadata. Each update in Pulumi Cloud then links back to the build and pull request that triggered it — no extra configuration required.
{{% /notes %}}

## Report results on pull requests

Independently of the build you run in Travis, Pulumi offers native [version control integrations](/docs/integrations/version-control/) for popular version control systems. A version control integration lets Pulumi Cloud post infrastructure-change summaries directly on pull requests as comments and status checks, and link each stack update back to the commit and pull request that produced it. See the [Version Control](/docs/integrations/version-control/) page for the systems currently supported.

## Speed up builds with caching

Travis workers don't persist state across runs, so without caching Pulumi must fetch its provider [plugins](/docs/iac/concepts/plugins/) on every build. Use Travis's [caching](https://docs.travis-ci.com/user/caching/) to persist the Pulumi plugin directory — and your language dependencies — across builds:

```yaml
cache:
  directories:
    - $HOME/.pulumi/plugins
    - infra/node_modules
```

Pulumi plugin versions are tied to the provider package versions your program uses, so the cache stays correct as long as those packages are unchanged. For the most deterministic builds, bake the provider plugins into a custom builder image derived from an official `pulumi/pulumi-*` image and reference that image from your build. See the [plugins documentation](/docs/iac/concepts/plugins/) for details.

## Concurrency

If commits merge to the main branch in quick succession, Travis can start overlapping builds that each run `pulumi up` on the same stack. Pulumi locks stack state during an update, so a concurrent update can't corrupt your state — the second update fails fast rather than clashing with the first. To avoid those failed builds, set **Limit concurrent jobs** to `1` in your repository's settings so deployment builds run one at a time. You can also enable auto-cancellation, which discards builds that are still *waiting to run* when a newer build arrives — note this won't cancel a build that has already started.

## Additional resources

- [Continuous delivery](/docs/iac/operations/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral environments created automatically for each pull request.
- [CI/CD troubleshooting guide](/docs/support/troubleshooting/ci-cd/) — fixes for common failures when running Pulumi in CI/CD.
