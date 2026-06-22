---
title_tag: "Continuous Delivery for the Cloud"
meta_desc: Pulumi models cloud infrastructure as source code, so infrastructure changes flow through the same CI/CD pipeline as your application code.
title: Continuous Delivery
h1: Pulumi and Continuous Delivery
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Continuous Delivery
        parent: iac-operations
        weight: 20
        identifier: iac-operations-cicd
aliases:
- /docs/iac/guides/continuous-delivery/
- /docs/iac/using-pulumi/continuous-delivery/
- /docs/reference/cd/
- /docs/console/continuous-delivery/
- /docs/guides/continuous-delivery/
- /docs/using-pulumi/continuous-delivery/
- /docs/iac/packages-and-automation/continuous-delivery/
- /docs/iac/operations/continuous-delivery/add-support-for-cicd-systems/
- /docs/iac/using-pulumi/continuous-delivery/add-support-for-cicd-systems/
- /docs/reference/cd-supporting-new-ci/
- /docs/console/continuous-delivery/other/
- /docs/guides/continuous-delivery/other/
- /docs/guides/continuous-delivery/add-support-for-cicd-systems/
- /docs/using-pulumi/continuous-delivery/add-support-for-cicd-systems/
- /docs/iac/packages-and-automation/continuous-delivery/add-support-for-cicd-systems/
---

Pulumi models cloud resources as source code, so changes to your infrastructure can be reviewed, tested, and deployed through the same pipeline you already use for application code: pull requests, code review, and automated tests. Pulumi integrates with any continuous integration and continuous delivery (CI/CD) system.

{{% notes %}}
Running into failures with Pulumi in CI/CD? See the [CI/CD troubleshooting guide](/docs/iac/operations/continuous-delivery/troubleshooting/).
{{% /notes %}}

## The trunk-based development workflow

The most common way to run Pulumi in CI/CD follows a trunk-based development model, where work merges into a single main branch and deployments flow outward from there:

1. **Open a pull request.** The pipeline runs [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) and posts the summary of proposed changes for review. Optionally, a [Review Stack](/docs/deployments/concepts/review-stacks/) provisions an ephemeral environment for the pull request so reviewers can exercise the change before it merges.
1. **Merge to the main branch.** The pipeline runs [`pulumi up`](/docs/iac/cli/commands/pulumi_up/) to deploy the change to an environment that receives continuous delivery, such as a shared development or staging environment.
1. **Promote to production.** Pushing a git tag — or otherwise marking a release — triggers a deployment to production, keeping production updates deliberate and traceable.

## Review infrastructure changes before merging

A preview compares your code against the *current* state of your infrastructure, so a change merged to the main branch can alter what an open pull request would actually do. Require that a branch be up to date with the main branch before it merges, and re-run `pulumi preview` after each update to the branch. Review the refreshed preview carefully: an intervening change to the main branch can invalidate an earlier preview in consequential ways — for example, by adding or removing resources that the original review never showed.

{{% notes type="warning" %}}
A CI/CD pipeline for infrastructure **must** run a preview on every pull request. Declarative infrastructure as code — whether Pulumi or any other IaC tool — cannot be reviewed from the code change alone: the same code edit can produce very different infrastructure changes depending on the current state of your resources. Reviewers need to see *both* the code diff *and* the proposed infrastructure changes that the preview reports.
{{% /notes %}}

## Authentication and configuration with Pulumi Cloud

Your pipeline needs a single [Pulumi access token](/docs/administration/access-identity/access-tokens/) to authenticate with Pulumi Cloud.

You can remove even that static secret with [OpenID Connect (OIDC)](/docs/administration/access-identity/oidc-issuers/): the pipeline exchanges the OIDC token issued by your CI/CD system for a short-lived Pulumi access token, so no long-lived credential is stored anywhere.

[Pulumi ESC](/docs/esc/) then supplies cloud credentials, secrets, and configuration to your Pulumi program. Because ESC delivers those values the same way whether the consumer is a CI/CD pipeline or a developer's machine, a single environment definition works in both places.

## Pulumi-native continuous delivery

Pulumi also provides its own continuous delivery mechanisms:

- [Pulumi Deployments](/docs/deployments/) — runs Pulumi operations on Pulumi-hosted infrastructure, triggered by git pushes, the CLI, or the API.
- [Review Stacks](/docs/deployments/concepts/review-stacks/) — ephemeral environments created automatically for each pull request and destroyed when it closes.
- [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) — manages Pulumi stacks from within a Kubernetes cluster using a custom resource.

## Third-party CI/CD systems

Pulumi has guides for running in the following CI/CD systems:

- [ArgoCD](/docs/iac/operations/continuous-delivery/argocd/)
- [AWS Code Services](/docs/iac/operations/continuous-delivery/aws-code-services/)
- [Azure DevOps](/docs/iac/operations/continuous-delivery/azure-devops/)
- [Bitbucket Pipelines](/docs/iac/operations/continuous-delivery/bitbucket/)
- [Buildkite](/docs/iac/operations/continuous-delivery/buildkite/)
- [CircleCI](/docs/iac/operations/continuous-delivery/circleci/)
- [Codefresh](/docs/iac/operations/continuous-delivery/codefresh/)
- [GitHub Actions](/docs/iac/operations/continuous-delivery/github-actions/)
- [GitLab CI/CD](/docs/iac/operations/continuous-delivery/gitlab-ci/)
- [Google Cloud Build](/docs/iac/operations/continuous-delivery/google-cloud-build/)
- [Harness](/docs/iac/operations/continuous-delivery/harness/)
- [Jenkins](/docs/iac/operations/continuous-delivery/jenkins/)
- [Octopus Deploy](/docs/iac/operations/continuous-delivery/octopus-deploy/)
- [TeamCity](/docs/iac/operations/continuous-delivery/teamcity/)
- [Travis CI](/docs/iac/operations/continuous-delivery/travis/)

If the system you use isn't listed, see [adding support for CI/CD systems](#adding-support-for-cicd-systems).

{{% notes %}}
For Pulumi-maintained version control integrations — including the GitHub App, GitLab, Bitbucket, and Azure DevOps — see [Version Control](/docs/integrations/version-control/).
{{% /notes %}}

## Adding support for CI/CD systems

When the Pulumi CLI runs a `preview` or `update`, it checks whether it runs
inside a CI/CD system. If it recognizes the system, it reads the environment
variables that system injects into its build agents and captures metadata about
the build.

That metadata appears alongside each update in the [Pulumi Cloud](https://app.pulumi.com/signin)
stack activity log. Combined with the information Pulumi has about your Git
repository, it lets Pulumi link an update back to the commit and pull request that
triggered it—so you can jump from a stack update straight to the corresponding PR
or commit in your source control system.

The Pulumi CLI detects the following metadata:

- CI system name
- Build ID
- Build number
- Build type
- Build URL
- Commit SHA
- Branch name
- Commit message
- PR number

The Pulumi CLI already detects the following CI/CD systems:

AppVeyor, AWS CodeBuild, Atlassian Bamboo, Atlassian Bitbucket Pipelines, Azure
Pipelines, Buildkite, CircleCI, Codefresh, Codeship, Drone, GitHub Actions, GitLab
CI/CD, GoCD, Hudson, Jenkins, Magnum CI, Semaphore, Spacelift, TaskCluster,
TeamCity, and Travis CI.

If your CI/CD system is in this list, no action is needed—the CLI captures build
metadata automatically.

If your system is not in the list, you can still surface build metadata by
setting fallback environment variables in your pipeline. This works with any
CI/CD system. Set the `PULUMI_CI_SYSTEM` environment variable, and the CLI reads
the following environment variables to surface CI/CD metadata for an update:

- `PULUMI_CI_SYSTEM`
- `PULUMI_CI_BRANCH_NAME`
- `PULUMI_CI_BUILD_ID`
- `PULUMI_CI_BUILD_NUMBER`
- `PULUMI_CI_BUILD_TYPE`
- `PULUMI_CI_BUILD_URL`
- `PULUMI_CI_PULL_REQUEST_SHA`
- `PULUMI_COMMIT_MESSAGE`
- `PULUMI_PR_NUMBER`

{{% notes type="info" %}}
`PULUMI_CI_BRANCH_NAME` and `PULUMI_COMMIT_MESSAGE` are treated as fallbacks rather than overrides. When the Pulumi CLI runs inside a Git repository with a normal (non-detached) HEAD and a non-empty commit message, the values read from Git win and these two environment variables are ignored. They take effect when:

- The Git working tree is in a detached-HEAD state (common on CI runners that check out a commit SHA), or
- The build runs against a Mercurial repository (in which case the CI branch name overrides the hg branch), or
- No repository is detected at all and the corresponding `PULUMI_GIT_HEAD_NAME` / `PULUMI_GIT_COMMIT_MESSAGE` variables are not set.

The other `PULUMI_CI_*` variables (build ID, build number, build type, build URL, PR SHA, PR number) are applied whenever they are set.
{{% /notes %}}
