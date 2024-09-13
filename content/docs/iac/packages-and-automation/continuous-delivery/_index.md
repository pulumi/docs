---
title_tag: "Continuous Delivery for the Cloud"
meta_desc: Pulumi's approach to infrastructure as code is great for CI/CD because it uses source code to model cloud resources and integrates into any CI/CD system.
title: Continuous Delivery
h1: Pulumi & Continuous delivery
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Continuous delivery
        parent: iac-packages-automation
        weight: 4
        identifier: iac-packages-automation-cicd
    usingpulumi:
        name: Continuous Delivery
        identifier: cont_delivery
        weight: 5
aliases:
- /docs/reference/cd/
- /docs/console/continuous-delivery/
- /docs/guides/continuous-delivery/
- /docs/using-pulumi/continuous-delivery/
---

Pulumi's approach to infrastructure as code is great for continuous delivery, because it uses source code to model
cloud resources. This means updates to your cloud infrastructure can be reviewed, validated, and tested using the same
process that you have today. For example, doing code reviews via Pull Requests, running code through linters or static
analysis tools, and running unit and integration tests as appropriate. It all "just works" for your cloud
infrastructure the same way it would for your application code.

Pulumi can easily integrate into any continuous integration/continuous delivery (CI/CD) system. If your CI/CD system isn't listed below or you are testing something new, see [adding support for CI/CD systems](/docs/using-pulumi/continuous-delivery/add-support-for-cicd-systems).

> Looking to troubleshoot failures related to running Pulumi in CI/CD? Check out our [CI/CD troubleshooting guide](/docs/using-pulumi/continuous-delivery/troubleshooting-guide).

<div class="supported-cicd-platforms">
    <a href="/docs/using-pulumi/continuous-delivery/aws-code-services">
        <img src="/logos/tech/ci-cd/aws-codedeploy.svg" alt="AWS Code Services">
        <h4 class="no-anchor">AWS Code Services</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/azure-devops">
        <img src="/logos/tech/ci-cd/azure-devops.svg" alt="Azure DevOps">
        <h4 class="no-anchor">Azure DevOps</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/circleci">
        <img src="/logos/tech/ci-cd/circleci.svg" alt="CircleCI">
        <h4 class="no-anchor">CircleCI</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/codefresh">
        <img src="/logos/tech/ci-cd/codefresh.svg" alt="Codefresh">
        <h4 class="no-anchor">Codefresh</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/github-actions">
        <img src="/logos/tech/ci-cd/github-actions.svg" alt="GitHub Actions">
        <h4 class="no-anchor">GitHub Actions</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/gitlab-ci">
        <img src="/logos/tech/ci-cd/gitlab-ci.svg" alt="GitLab CI">
        <h4 class="no-anchor">GitLab CI</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/google-cloud-build">
        <img src="/logos/tech/ci-cd/google-cloud-build.png" alt="Google Cloud Build">
        <h4 class="no-anchor">Google Cloud Build</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/jenkins">
        <img src="/logos/tech/ci-cd/jenkins.svg" alt="Jenkins">
        <h4 class="no-anchor">Jenkins</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/octopus-deploy">
        <img src="/logos/tech/ci-cd/octopus-deploy.svg" alt="Octopus Deploy">
        <h4 class="no-anchor">Octopus Deploy</h4>
    </a>
    <a href="/docs/pulumi-cloud/deployments/">
        <img src="/logos/brand/avatar-on-white.png" alt="Pulumi Deployments">
        <h4 class="no-anchor">Pulumi Deployments</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator">
        <img src="/logos/tech/ci-cd/kubernetes.png" alt="Pulumi Kubernetes Operator">
        <h4 class="no-anchor">Pulumi Kubernetes Operator</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/teamcity">
        <img src="/logos/tech/ci-cd/teamcity.svg" alt="JetBrains TeamCity">
        <h4 class="no-anchor">JetBrains TeamCity</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/spinnaker">}}">
        <img src="/logos/tech/ci-cd/spinnaker.svg" alt="Spinnaker">
        <h4 class="no-anchor">Spinnaker</h4>
    </a>
    <a href="/docs/using-pulumi/continuous-delivery/travis">
        <img src="/logos/tech/ci-cd/travis-ci.svg" alt="TravisCI">
        <h4 class="no-anchor">TravisCI</h4>
    </a>
</div>

> Pulumi can also bridge results from your CI/CD system with GitHub, surfacing the results of stack updates
> on GitHub pull requests. See the [Pulumi GitHub App](/docs/using-pulumi/continuous-delivery/github-app/) for more information.

### Configuration and Secrets

Pulumi is designed to be entirely code-centric, including the way in which configuration and secrets are managed.
Configuration values and secrets are stored safely inside of `Pulumi.yaml` files, which you will commit.
The source is effectively everything that Pulumi needs to for deployment, with minimal external dependencies.

Secret configuration values are encrypted on [app.pulumi.com](https://app.pulumi.com) and are safe to check into your
source code repository. But you can use your own secrets provider, ensuring that only you have access to your
sensitive information. See [Managing Secrets with Pulumi](/blog/managing-secrets-with-pulumi/) for more information.

### Managing Complex Environments

Most real-world environments are complex. Perhaps you have a networking stack that's independent from your data
and application stacks. Pulumi [supports "stack references"](/docs/guides/organizing-projects-stacks), which
permit one stack to depend upon another. This facilitates continuous delivery and integration at scale.

### Using Branches for Environments

Pulumi is agnostic to what sort of branching strategy you take. Most customers use Git-based flows; the most common is
to use one branch-per-[stack](/docs/concepts/stack/). This allows you to control deployments to environments
using your usual commit, code review, and approval process, such as GitHub pull requests.

If you are using GitHub pull requests to trigger updates, you will likely want to use the
[Pulumi GitHub App](/docs/using-pulumi/continuous-delivery/github-app/). This gives you interactive infrastructure change previews
inside of your Pull Request, making it easier to see, review, and comment on any changes before a deployment occurs.
