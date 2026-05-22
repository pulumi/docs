---
title_tag: "Using Jenkins with Pulumi | CI/CD"
meta_desc: Run Pulumi in Jenkins pipelines to preview and deploy infrastructure changes through a trunk-based continuous delivery workflow.
title: Jenkins
h1: Using Jenkins with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Jenkins
        parent: iac-using-pulumi-cicd
        weight: 120
aliases:
- /docs/iac/using-pulumi/continuous-delivery/jenkins/
- /docs/console/continuous-delivery/jenkins/
- /docs/guides/continuous-delivery/jenkins/
- /docs/using-pulumi/continuous-delivery/jenkins/
- /docs/iac/packages-and-automation/continuous-delivery/jenkins/
---

[Jenkins](https://www.jenkins.io/) is an open-source automation server that runs CI/CD pipelines defined in a `Jenkinsfile`. You run Pulumi in a pipeline stage that executes inside the official [`pulumi/pulumi`](https://hub.docker.com/r/pulumi/pulumi) container image. That image ships the Pulumi CLI and every language runtime, so the same pipeline works with a Pulumi program written in any [supported language](/docs/iac/languages-sdks/) and targeting [any cloud provider](/registry/) Pulumi supports.

{{< cicd-cloud-note >}}

## How Pulumi works with Jenkins

To apply infrastructure changes, Pulumi runs your program with the Pulumi CLI. A Jenkins pipeline stage with a [Docker agent](https://www.jenkins.io/doc/book/pipeline/docker/) provides that environment: it runs the stage's steps inside a container image you choose. Point the agent at `pulumi/pulumi` and the stage can run any `pulumi` command — `install`, `preview`, `up` — exactly as you would on your own machine.

There is no Pulumi-specific Jenkins plugin to install — the `pulumi/pulumi` container image is the integration point. Pulumi runs on both free and paid accounts. You wire up authentication through Jenkins credentials, described below.

## Prerequisites

Before you begin, make sure you have:

1. A [Pulumi Cloud](https://app.pulumi.com/signin) account and organization.
1. A working Jenkins installation with the [Docker Pipeline](https://plugins.jenkins.io/docker-workflow/) and [Git](https://plugins.jenkins.io/git/) plugins, on an agent that can run Docker containers.
1. A Pulumi program in a Git repository Jenkins can build. If you don't have one yet, follow a [Get started](/docs/iac/get-started/) guide.

## Authenticate with Pulumi Cloud

Give your pipeline a Pulumi Cloud identity in one of two ways. **Choose one — you don't need both:**

- **A stored access token.** A long-lived [Pulumi access token](/docs/administration/access-identity/access-tokens/) saved as a Jenkins credential. Simple to set up and works on any Jenkins installation.
- **An OIDC token exchange.** The pipeline exchanges a short-lived token for a temporary Pulumi access token, so no long-lived secret is stored anywhere. Recommended where available, but on Jenkins it requires a community plugin (see below).

### Use a stored access token

When your pipeline uses Pulumi Cloud as its backend, it needs only a single [Pulumi access token](/docs/administration/access-identity/access-tokens/) to operate. Pulumi reads the token from the `PULUMI_ACCESS_TOKEN` environment variable and authenticates without an interactive login.

Store the token as a Jenkins [credential](https://www.jenkins.io/doc/book/using/using-credentials/) of kind **Secret text** rather than committing it to source control, then expose it to the pipeline with the `environment` block:

```groovy
environment {
    PULUMI_ACCESS_TOKEN = credentials("pulumi-access-token")
}
```

Prefer an [organization or team token](/docs/administration/access-identity/access-tokens/#creating-an-organization-access-token) over a personal token so the pipeline's identity isn't tied to an individual.

### Exchange an OIDC token

You can remove the static token entirely with [OpenID Connect (OIDC)](/docs/administration/access-identity/oidc-issuers/). Pulumi Cloud can register any trusted service that issues OIDC tokens as an [OIDC Issuer](/docs/administration/access-identity/oidc-issuers/). The pipeline obtains a short-lived OIDC token from its host and exchanges it with Pulumi Cloud for a temporary Pulumi access token:

```bash
pulumi login --oidc-token "$OIDC_TOKEN" --oidc-org "your-org"
```

The OIDC token is issued *by Jenkins* and exchanged *inbound* for a Pulumi token — Pulumi Cloud never issues credentials out to Jenkins.

{{% notes type="info" %}}
Jenkins does not issue OIDC tokens for build pipelines on its own. To use this path, install the community [OpenID Connect Provider plugin](https://plugins.jenkins.io/oidc-provider/), which adds an OpenID Connect id token credential type that mints a fresh, short-lived token each time a pipeline reads it.
{{% /notes %}}

### Deliver configuration with Pulumi ESC

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a pipeline or a developer's machine, a single environment definition works in both places.

## Provide cloud credentials

When Pulumi runs, your program also needs credentials for the cloud provider it manages. You can supply them in one of two ways:

- **Pulumi ESC (recommended).** Configure an [ESC environment](/docs/esc/) to broker short-lived cloud credentials through OIDC. Your program receives temporary credentials scoped to exactly what it needs, and the pipeline stores nothing but its Pulumi access token.
- **Jenkins credentials.** Store the provider's credentials in the Jenkins [credentials store](https://www.jenkins.io/doc/book/using/using-credentials/) and bind them into a stage with `withCredentials`. Jenkins provides typed bindings for common cases — an `azureServicePrincipal` for Azure, a `usernamePassword` pair, or a plain **Secret text** entry for values such as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

{{% notes type="warning" %}}
Never commit cloud credentials or the Pulumi access token to your repository. Keep them in the Jenkins credentials store so the values stay protected and access is auditable.
{{% /notes %}}

## Configure a Jenkins pipeline

A Jenkins pipeline is defined in a `Jenkinsfile` at the root of your repository. The following declarative pipeline runs Pulumi against a [stack](/docs/iac/concepts/stacks/) inside the `pulumi/pulumi` container:

```groovy
pipeline {
    agent {
        docker { image "pulumi/pulumi" }
    }

    environment {
        PULUMI_ACCESS_TOKEN = credentials("pulumi-access-token")
    }

    stages {
        stage("Deploy") {
            steps {
                dir("infra") {
                    sh "pulumi install"
                    sh "pulumi stack select acme/website/staging"
                    sh "pulumi up --yes"
                }
            }
        }
    }
}
```

The example assumes a Pulumi program in an `infra/` directory. [`pulumi install`](/docs/iac/cli/commands/pulumi_install/) installs the program's language dependencies and required plugins, so the same step works for a program written in any supported language.

{{% notes type="info" %}}
Wrap arguments in double quotes throughout a `Jenkinsfile`. Single quotes suppress Groovy string interpolation and can cause commands to silently fail.
{{% /notes %}}

## Build a trunk-based CI/CD workflow

The most common way to run Pulumi in CI/CD follows a [trunk-based development model](/docs/iac/guides/continuous-delivery/#the-trunk-based-development-workflow): work merges into a single main branch, and deployments flow outward from there. A Jenkins [multibranch pipeline](https://www.jenkins.io/doc/book/pipeline/multibranch/) builds pull requests, branches, and tags from one `Jenkinsfile`, and a [`when`](https://www.jenkins.io/doc/book/pipeline/syntax/#when) directive maps each stage of the workflow to the event that should trigger it.

### Preview infrastructure changes in a pull request

When a pull request is opened, run a dry run instead of a deployment. Gate the stage on `changeRequest()` and run [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/):

```groovy
stage("Preview") {
    when { changeRequest() }
    steps {
        dir("infra") {
            sh "pulumi install"
            sh "pulumi stack select acme/website/staging"
            sh "pulumi preview"
        }
    }
}
```

`pulumi preview` reports the proposed changes without modifying any resources, giving reviewers a summary of what the merge would do. To let reviewers exercise the change in a live environment, use a [Review Stack](/docs/deployments/deployments/review-stacks/), which provisions an ephemeral stack for the pull request and destroys it when the pull request closes.

### Deploy to staging on merge to the main branch

When a pull request merges, run [`pulumi up`](/docs/iac/cli/commands/pulumi_up/) against an environment that receives continuous delivery, such as a shared development or staging environment. Gate the stage on the main branch:

```groovy
stage("Deploy to staging") {
    when { branch "main" }
    steps {
        dir("infra") {
            sh "pulumi install"
            sh "pulumi stack select acme/website/staging"
            sh "pulumi up --yes"
        }
    }
}
```

### Promote to production with a git tag

Production updates should be deliberate. Keep production on its own stack and deploy it only when you push a release tag — for example, a moving `production` tag that you advance to a commit already validated in staging:

```groovy
stage("Deploy to production") {
    when { buildingTag() }
    steps {
        dir("infra") {
            sh "pulumi install"
            sh "pulumi stack select acme/website/production"
            sh "pulumi up --yes"
        }
    }
}
```

Configure the multibranch pipeline to discover tags so tag pushes trigger a build. Promotion then becomes a single, traceable Git operation, and production never deploys from an untested commit.

## Report results on pull requests

Independently of Jenkins, Pulumi Cloud's [version control integrations](/docs/integrations/version-control/) connect Pulumi to popular version control systems. With one configured, Pulumi Cloud posts infrastructure-change summaries as comments and status checks on pull and merge requests, and links each stack update back to the commit and pull request that produced it — review context that a Jenkins pipeline alone does not provide.

## Speed up builds with caching

A clean Jenkins agent starts with an empty plugin cache, so Pulumi re-downloads its provider plugins on every run. Jenkins has no native cross-build cache, so the most reliable fix is to bake the plugins your program uses into a custom builder image derived from `pulumi/pulumi`:

```dockerfile
FROM pulumi/pulumi
RUN pulumi plugin install resource aws <version> \
    && pulumi plugin install resource random <version>
```

Build and publish that image, then reference it from the pipeline's Docker agent:

```groovy
agent {
    docker { image "your-registry/pulumi-builder" }
}
```

Because the plugins are present in the image, every build starts with a warm cache. See the [plugins documentation](/docs/iac/concepts/plugins/) for details on how Pulumi resolves and caches provider plugins.

## Additional resources

- [Continuous delivery](/docs/iac/guides/continuous-delivery/) — overview of running Pulumi in CI/CD.
- [CI/CD troubleshooting guide](/docs/support/troubleshooting/ci-cd/) — diagnose common failures when running Pulumi in a pipeline.
- [Pulumi ESC](/docs/esc/) — deliver credentials, secrets, and configuration to pipelines and developers consistently.
- [OIDC Issuers](/docs/administration/access-identity/oidc-issuers/) — eliminate static tokens with short-lived, exchanged credentials.
- [Review Stacks](/docs/deployments/deployments/review-stacks/) — ephemeral environments for pull requests.
- [Version Control](/docs/integrations/version-control/) — connect Pulumi Cloud to your version control system for pull request reporting.
