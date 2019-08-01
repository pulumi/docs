---
title: Continuous Delivery
menu:
  reference:
    identifier: cd
    weight: 8
---

Continuous delivery is an approach to managing cloud applications and infrastructure where all changes are
represented in code, reviewed like ordinary software changes, and applied using automated workflows. This approach
builds upon continuous integration, a commonly used practice for performing testing and validation before committing
changes. Continuous deployment ensures that releasing software into cloud environments is done with all of the
rigor we usually apply to software changes, while ensuring repeatability, auditing, and removing manual steps.

Infrastructure as code is great for continuous delivery, because it uses source code to model cloud resources.
This means checking it into your source control system (such as Git) and uses existing review processes (such as
Pull Requests), validation procedures including linting and testing, and promotion processes (such as Git branches),
all "just works" for your infrastructure code like it does your application code.

## Continuous Delivery with Pulumi

Pulumi integrates with existing CI/CD systems that drive overall execution and pipelines. Pulumi is just one
step in that pipeline, but helps to connect your source code changes to your live cloud environments. Instead of
aiming to replace these existing systems, Pulumi prefers to let you leverage existing setups.

Here are examples for many CI/CD systems that Pulumi integrates with:

* [AWS Code Services]({{< relref "cd-aws-code-services.md" >}})
* [Azure DevOps]({{< relref "cd-azure-devops" >}})
* [CircleCI]({{< relref "cd-circleci.md" >}})
* [Codefresh]({{< relref "cd-codefresh.md" >}})
* [GitHub Actions]({{< relref "cd-github-actions.md" >}})
* [GitLab CI]({{< relref "cd-gitlab-ci.md" >}})
* [Google Cloud Build]({{< relref "cd-google-cloud-build.md" >}})
* [Travis]({{< relref "cd-travis.md" >}})

Continuous integration encompasses the system you use for automatically testing your source code, usually upon
commits to a particular branch. This relates to, but is independent from, continuous deployment (CD), which deploys
a subset of these code changes after specific gates have been passed (certain tests passing, approval, and so on).

Pulumi can also bridge results from your CI/CD system with GitHub, for example surfacing the results of stack
updates on GitHub pull requests. See [Pulumi GitHub App]({{< relref "cd-github.md" >}}) for more information.

## Managing Environments

Pulumi is designed to be entirely code-centric, including the way in which configuration and secrets are managed.
Configuration values and secrets are stored safely inside of `Pulumi.<stack-name>.yaml` files, which you will commit.
So, the source is effectively everything that Pulumi needs to for deployment, with minimal external dependencies.

Secret configuration values are encrypted on pulumi.com, and are safe to check into your source code repository.
The encrypted value can only be decrypted by someone with access to that stack.

### Managing Complex Environments

Most real-world environments are complex. Perhaps you have a networking stack that's independent from your data
and application stacks. Pulumi [supports "stack references"]({{< relref "organizing-stacks-projects.md" >}}), which
permit one stack to depend upon another. This facilitates continuous delivery at scale.

### Using Branches for Environments

Pulumi is agnostic to what sort of branching strategy you take. Most customers use Git-based flows; the most common is
to use one branch-per-[stack]({{< relref "stack.md" >}}). This allows you to control deployments to environments
using your usual commit, code review, and approval process, such as GitHub pull requests.

If you are using GitHub pull requests to trigger updates, you will likely want to use the
[Pulumi GitHub App]({{< relref "cd-github.md" >}}). This gives you interactive infrastructure change previews
inside of your Pull Request, making it easier to see, review, and comment on any changes before a deployment occurs.

### How to Achieve Continuous Delivery for an Environment

The easiest way to achieve a Pulumi-based CD flow is to simply integrate it into your existing CI process.

After running your usual CI processes upon merging a commit into a release branch, you can proceed to a Pulumi
deployment.  This usually entails running `pulumi up --yes`. After the deployment completes, you may want to perform
additional post-deployment verification.

There are many variants of this. For instance, Pulumi makes easy to stand up new developer stacks, so you can create a
one-off stack for a branch via `pulumi stack init testing-<branch>`, stand it up from scratch (using the flow above),
test it out, and finally tear it down using `pulumi destroy` and `pulumi stack rm`.

Over time, we expect to develop services and tools to help accomplish these practices across a wide variety of CI
systems and workflows.  In the meantime, we'd love to [hear more](mailto:support@pulumi.com) about your scenarios,
what worked well, and what you'd like to see improved!

## Continuous Delivery vs. Continuous Deployment

Often you will see the two terms _continuous delivery_ and _continuous deployment_ used interchangeably. Both share
the same approach of delivering changes to an environment using an automated process that is based on source code
changes. The difference, however, is that with continuous delivery, there is an automated process.

The major difference between the two, however, is that continuous delivery includes an approval process before
updating your production environments. The benefit is that continuous delivery tooling and automation intrinsically
supports better visibility into changes before they happen, compared to continuous deployment, something that Pulumi
fully embraces with its preview model and services like [GitHub Pull Request integration]({{< relref "cd-github.md" >}}).
