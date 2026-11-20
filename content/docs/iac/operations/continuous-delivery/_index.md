---
title_tag: "Continuous Delivery for the Cloud"
meta_desc: Run Pulumi in the CI/CD system you already use, or in Pulumi Cloud with Pulumi Delivery, Pulumi Deployments, and review stacks.
title: Continuous delivery
h1: Pulumi and continuous delivery
menu:
    iac:
        name: Continuous delivery
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
- /docs/iac/guides/continuous-delivery/add-support-for-cicd-systems/
- /docs/iac/operations/continuous-delivery/add-support-for-cicd-systems/
- /docs/iac/using-pulumi/continuous-delivery/add-support-for-cicd-systems/
- /docs/reference/cd-supporting-new-ci/
- /docs/console/continuous-delivery/other/
- /docs/guides/continuous-delivery/other/
- /docs/guides/continuous-delivery/add-support-for-cicd-systems/
- /docs/using-pulumi/continuous-delivery/add-support-for-cicd-systems/
- /docs/iac/packages-and-automation/continuous-delivery/add-support-for-cicd-systems/
---

Pulumi models cloud resources as source code, so changes to your infrastructure can be reviewed, tested, and deployed through the same pipeline you already use for application code: pull requests, code review, and automated tests.

Pulumi integrates with any continuous integration and continuous delivery (CI/CD) system, and Pulumi Cloud can also run your release pipelines for you [with Pulumi Delivery](#pulumi-delivery).

{{% notes %}}
[Pulumi Delivery](/docs/delivery/) is currently available in public preview. With Delivery, you can write your release pipelines as Pulumi programs that orchestrate multiple stacks and gate each release on an approval, an AI decision, or your own code. [Learn more about how Delivery works](/docs/delivery/concepts/).
{{% /notes %}}

## Trunk-based development workflows {#the-trunk-based-development-workflow}

The most common way to run Pulumi in CI/CD workflows follows a trunk-based development model, where work merges into a single main branch and deployments flow outward from there:

1. **Open a pull request.** The pipeline runs [`pulumi preview`](/docs/iac/cli/commands/pulumi_preview/) and posts the summary of proposed changes for review. Optionally, a [review stack](/docs/deployments/concepts/review-stacks/) provisions an ephemeral environment for the pull request so reviewers can exercise the change before it merges.
1. **Merge to the main branch.** The pipeline runs [`pulumi up`](/docs/iac/cli/commands/pulumi_up/) to deploy the change to an environment that receives continuous delivery, such as a shared development or staging environment.
1. **Promote to production.** Pushing a git tag — or otherwise marking a release — triggers a deployment to production, keeping production updates deliberate and traceable.

## Previewing infrastructure changes

A Pulumi preview compares your code against the *current* state of your infrastructure, so a change merged to the main branch can alter what an open pull request would actually do. Require that a branch be up to date with the main branch before it merges, and re-run `pulumi preview` after each update to the branch. Review the refreshed preview carefully: an intervening change to the main branch can invalidate an earlier preview in consequential ways — for example, by adding or removing resources that the original review never showed.

{{% notes type="warning" %}}
A CI/CD pipeline for infrastructure **must** run a preview on every pull request. Declarative infrastructure as code — whether Pulumi or any other IaC tool — cannot be reviewed from the code change alone: the same code edit can produce very different infrastructure changes depending on the current state of your resources. Reviewers need to see *both* the code diff *and* the proposed infrastructure changes that the preview reports.
{{% /notes %}}

## Authenticating with Pulumi Cloud

If you use Pulumi Cloud and your pipeline runs outside of it, the Pulumi CLI needs a [Pulumi access token](/docs/administration/concepts/access-tokens/) to authenticate.

To avoid having to obtain and manage long-lived access tokens, Pulumi Cloud supports [authenticating with OpenID Connect (OIDC)](/docs/administration/guides/oidc-issuers/). This allows your pipeline to exchange an OIDC token issued by your CI/CD system for a short-lived Pulumi access token.

Pipelines that run within Pulumi Cloud get credentials automatically. [Pulumi Delivery](/docs/delivery/concepts/identity/#credentials-in-stack-updates-and-jobs) and [Pulumi Deployments](/docs/deployments/concepts/settings/environment-variables/) (including [review stacks](/docs/deployments/concepts/review-stacks/)) grant each Pulumi operation a temporary access token that acts as the identity used by the run — for example, as a [service principal or team](/docs/deployments/concepts/settings/pulumi-cloud-role/).

If you use a [DIY backend](/docs/iac/operations/stack-management/using-a-diy-backend/), you don't need a Pulumi access token. In this case, Pulumi authenticates with whatever storage provider holds your stack state (e.g., an S3 bucket).

## Authenticating with cloud providers

Your Pulumi program also needs credentials for the clouds it deploys to. Often, these are static secrets stored in your CI/CD system, which you then have to manage and rotate.

Alternatively, if you use Pulumi Cloud, [Pulumi ESC](/docs/esc/) can supply them, along with other secrets and configuration, wherever the program runs. With ESC, [OIDC](/docs/esc/guides/configuring-oidc/) removes the need to store long-lived cloud credentials: ESC issues a short-lived OIDC token, and your cloud provider, such as AWS, Azure, or Google Cloud, exchanges it for temporary credentials. For Delivery pipelines specifically, see [cloud credentials for Pulumi Delivery](/docs/delivery/guides/cloud-credentials/).

## Continuous delivery with Pulumi Cloud {#pulumi-native-continuous-delivery}

{{< pulumi-cloud />}}

Pulumi Cloud has several options for CI/CD workflows that can work alongside, and in some cases replace, the CI/CD system you already use. Which option fits best depends on how much you need to coordinate, from releases across many stacks to a single stack or pull request.

### Pulumi Delivery

[Pulumi Delivery](/docs/delivery/) allows you to manage and promote changes through multiple stacks and environments. Delivery pipelines are written as Pulumi programs that define stages that run in a particular order. Stages update Pulumi stacks and can also run jobs, such as shell scripts or smoke tests, and gates can be used between stages to hold releases until a human or agent approves them.

![Pulumi Delivery inside Pulumi Cloud, promoting a release from your repository through dev, staging, and prod stages to your clouds](/images/docs/delivery-platform-diagram.svg)

Delivery covers the merge and promote steps of the trunk-based workflow described earlier on this page. In the example above, a push to a `main` branch starts a run that deploys and tests a change to a `dev` stack before deploying it automatically to `staging`, then waits for human approval before deploying the same change to `prod`. Because the pipeline itself is a Pulumi program, you can build it with loops, functions, and conditionals, and it's versioned and reviewed along with the infrastructure and application code it delivers.

To learn more about Pulumi Delivery, see [How Pulumi Delivery works](/docs/delivery/concepts/).

### Pulumi Deployments

[Pulumi Deployments](/docs/deployments/) runs Pulumi operations for individual stacks, either on your own or on Pulumi-managed runners. Deployments can be triggered by Git push events, [CLI commands](/docs/iac/cli/commands/pulumi_deployment/), the [REST API](/docs/reference/cloud-rest-api/deployments/), or on a schedule. With a connected repository, Deployments can run all three steps of the trunk-based workflow described earlier: `pulumi preview` when a pull request is opened, and `pulumi up` when commits merge to a specified branch or a matching tag is pushed.

### Review stacks

[Review stacks](/docs/deployments/concepts/review-stacks/) create ephemeral Pulumi stacks for every pull request of an associated source repository. Built on top of Pulumi Deployments, review stacks allow reviewers to exercise a change before it's merged, and they're destroyed automatically when pull requests close.

## Pulumi Kubernetes Operator

The [Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/) manages Pulumi stacks from inside a Kubernetes cluster using a custom resource. It runs a stack's program from a Git repository, a Flux source, or a Program resource, and keeps the stack up to date with GitOps. It's suited to managing infrastructure alongside your Kubernetes workloads or from a dedicated control-plane cluster, and you can combine it with [Argo CD](/docs/iac/operations/continuous-delivery/argocd/). To learn more and get started, see [installing the Pulumi Kubernetes Operator](/docs/integrations/clouds/kubernetes/pulumi-kubernetes-operator/installation/).

## Third-party CI/CD systems

If you already run a CI/CD system, Pulumi has guides for running in the following systems:

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

## Troubleshooting

If you're having trouble with Pulumi in CI/CD, see the [CI/CD troubleshooting guide](/docs/iac/operations/continuous-delivery/troubleshooting/).
