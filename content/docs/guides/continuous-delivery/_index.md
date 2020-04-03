---
title: Continuous Delivery for Cloud Resources
meta_desc: Pulumi's approach to infrastructure as code is great for continuous delivery, because it uses source code to model cloud resources. Pulumi can easily integrate into any CI/CD system.
menu:
    userguides:
        identifier: cont_delivery
        weight: 3

aliases:
- /docs/reference/cd/
- /docs/console/continuous-delivery/
---

Pulumi's approach to infrastructure as code is great for continuous delivery, because it uses source code to model
cloud resources. This means updates to your cloud infrastructure can be reviewed, validated, and tested using the same
process that you have today. For example, doing code reviews via Pull Requests, running code through linters or static
analysis tools, and running unit and integration tests as appropriate. It all "just works" for your cloud
infrastructure the same way it would for your application code.

Pulumi can easily integrate into any continuous integration/continuous deliver (CI/CD) system. If your CI/CD system isn't listed below or you are testing something new, see our guide for using Pulumi
within a [generic CI/CD system]({{< relref "other" >}}).

<div class="supported-cicd-platforms">
    <a href="{{< relref aws-code-services >}}">
        <img src="/logos/tech/ci-cd/aws-codedeploy.svg" alt="AWS Code Services">
        <h4 class="no-anchor">AWS Code Services</h4>
    </a>
    <a href="{{< relref azure-devops >}}">
        <img src="/logos/tech/ci-cd/azure-devops.svg" alt="Azure DevOps">
        <h4 class="no-anchor">Azure DevOps</h4>
    </a>
    <a href="{{< relref circleci >}}">
        <img src="/logos/tech/ci-cd/circleci.svg" alt="CircleCI">
        <h4 class="no-anchor">CircleCI</h4>
    </a>
    <a href="{{< relref codefresh >}}">
        <img style="width: 120px;" src="/logos/tech/ci-cd/codefresh.svg" alt="Codefresh">
        <h4 class="no-anchor">Codefresh</h4>
    </a>
    <a href="{{< relref github-actions >}}">
        <img style="width: 120px;" src="/logos/tech/ci-cd/github-actions.svg" alt="GitHub Actions">
        <h4 class="no-anchor">GitHub Actions</h4>
    </a>
    <a href="{{< relref gitlab-ci >}}">
        <img src="/logos/tech/ci-cd/gitlab-ci.svg" alt="GitLab CI">
        <h4 class="no-anchor">GitLab CI</h4>
    </a>
    <a href="{{< relref google-cloud-build >}}">
        <img src="/logos/tech/ci-cd/google-cloud-build.png" alt="Google Cloud Build">
        <h4 class="no-anchor">Google Cloud Build</h4>
    </a>
    <a href="{{< relref jenkins >}}">
        <img src="/logos/tech/ci-cd/jenkins.svg" alt="Jenkins">
        <h4 class="no-anchor">Jenkins</h4>
    </a>
    <a href="{{< relref octopus-deploy >}}">
        <img src="/logos/tech/ci-cd/octopus-deploy.svg" alt="Octopus Deploy">
        <h4 class="no-anchor">Octopus Deploy</h4>
    </a>
    <a href="{{< relref teamcity >}}">
            <img src="/logos/tech/ci-cd/teamcity.svg" alt="JetBrains TeamCity">
            <h4 class="no-anchor">JetBrains TeamCity</h4>
        </a>
    <a href="{{< relref travis >}}">
        <img src="/logos/tech/ci-cd/travis-ci.svg" alt="TravisCI">
        <h4 class="no-anchor">TravisCI</h4>
    </a>
</div>

> Pulumi can also bridge results from your CI/CD system with GitHub, surfacing the results of stack updates
> on GitHub pull requests. See the [Pulumi GitHub App]({{< relref "github-app" >}}) for more information.

### Configuration and Secrets

Pulumi is designed to be entirely code-centric, including the way in which configuration and secrets are managed.
Configuration values and secrets are stored safely inside of `Pulumi.yaml` files, which you will commit.
The source is effectively everything that Pulumi needs to for deployment, with minimal external dependencies.

Secret configuration values are encrypted on [app.pulumi.com](https://app.pulumi.com) and are safe to check into your
source code repository. But you can use your own secrets provider, ensuring that only you have access to your
sensitive information. See [Managing Secrets with Pulumi]({{< relref "managing-secrets-with-pulumi" >}}) for more information.

### Managing Complex Environments

Most real-world environments are complex. Perhaps you have a networking stack that's independent from your data
and application stacks. Pulumi [supports "stack references"]({{< relref "/docs/intro/concepts/organizing-stacks-projects" >}}), which
permit one stack to depend upon another. This facilitates continuous delivery and integration at scale.

### Using Branches for Environments

Pulumi is agnostic to what sort of branching strategy you take. Most customers use Git-based flows; the most common is
to use one branch-per-[stack]({{< relref "/docs/intro/concepts/stack" >}}). This allows you to control deployments to environments
using your usual commit, code review, and approval process, such as GitHub pull requests.

If you are using GitHub pull requests to trigger updates, you will likely want to use the
[Pulumi GitHub App]({{< relref "github-app" >}}). This gives you interactive infrastructure change previews
inside of your Pull Request, making it easier to see, review, and comment on any changes before a deployment occurs.
