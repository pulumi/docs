---
title: Continuous Deployment
---

Pulumi is great for continuous deployment and supports a range of workflows.  In fact, our team uses Pulumi
itself to deploy and manage [https://pulumi.com/](https://pulumi.com) and follows many of the practices described below.

## CI / CD

Continuous integration (CI) encompasses the system you use for automatically testing your source code, usually upon
commits to a particular branch.  This relates to, but is independent from, continuous deployment (CD), which deploys
a subset of these code changes after specific gates have been passed (certain tests passing, approval, and so on).

### Provider-specific examples

* [AWS Code Services](./cd-aws-code-services.html)
* [Azure DevOps](./cd-azure-devops.html)
* [CircleCI](./cd-circleci.html)
* [GitHub Actions](./cd-github-actions.html)
* [GitLab CI](./cd-gitlab-ci.html)
* [Travis](./cd-travis.html)


Pulumi can also bridge results from your CI/CD system with GitHub, for example surfacing the results of stack
updates on GitHub pull requests. See [Pulumi GitHub App](./cd-github.html) for more information.

## Branching strategy for deployments

Pulumi is also agnostic to what sort of branching strategy you take.  Most customers use Git-based flows; the most common is to use one branch-per-[stack](./stack.html).  This allows you to control deployments to environments using your usual commit, code review, and approval process, such as GitHub pull requests.

## Stacks and configuration

Pulumi is designed to be entirely code-centric, including the way in which configuration and secrets are managed. Configuration values and secrets are stored safely inside of `Pulumi.<stack-name>.yaml` files, which you will commit. So, the source is effectively everything that Pulumi needs to for deployment, with minimal external dependencies.

Secret configuration values are encrypted on pulumi.com, and are safe to check into your source code repository. The encrypted value can only be decrypted by someone with access to that stack.

## How to achieve Pulumi-based CD from CI

The easiest way to achieve a Pulumi-based CD flow is to simply integrate it into your existing CI process.

After running your usual CI processes upon merging a commit into a release branch, you can proceed to a Pulumi deployment.  This usually entails running `pulumi update --yes`. After the deployment completes, you may want to perform additional post-deployment verification.

There are many variants of this. For instance, Pulumi makes easy to stand up new developer stacks, so you can create a one-off stack for a branch via `pulumi stack init testing-<branch>`, stand it up from scratch (using the flow above), test it out, and finally tear it down using `pulumi destroy` and `pulumi stack rm`.

Over time, we expect to develop services and tools to help accomplish these practices across a wide variety of CI
systems and workflows.  In the meantime, we'd love to [hear more](mailto:support@pulumi.com) about your scenarios,
what worked well, and what you'd like to see improved!
