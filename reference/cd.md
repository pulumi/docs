---
title: Continuous Deployment
---

Pulumi is great for continuous deployment and supports a range of workflows.  In fact, our team uses Pulumi
itself to deploy and manage [https://pulumi.com/](https://pulumi.com) and follows many of the practices described below.

## Continuous Integration

Continuous integration (CI) encompasses the system you use for automatically testing your source code, usually upon
commits to a particular branch.  This relates to, but is independent from, continuous deployment (CD), which deploys
a subset of these code changes after specific gates have been passed (certain tests passing, approval, and so on).

Pulumi is agnostic to what system you use for CI.  For instance, we are happy to plug into a range of systems including
AWS CodePipeline/CodeDeploy, CircleCI, Travis, Jenkins, Microsoft VSTS, and Shippable.

For help with specific CI systems, please see these links:

* [Travis](./cd-travis.html)

> **Note:** More content is on it's way here.  Please let us know what specific systems and topics you'd like to know
> more about.

## Branching Strategy for Deployments

Pulumi is also agnostic to what sort of branching strategy you take.  Most of our customers use various Git-based
flows, but the most common we see is to have one branch-per-[stack](./stack.html).  This allows you to control
deployments to environments using your usual commit, code review, and approval process (e.g., GitHub Pull Requests).

## Stacks and Configuration

Pulumi is designed to be entirely code-centric, including the way in which configuration and secrets are managed.  These
configuration values and secrets are stored safely inside of `Pulumi.yaml` files, which you will commit.  As a result,
your source code is effectively everything Pulumi needs to perform a deployment, with minimal external dependencies.

## How to Achieve Pulumi-Based CD from CI

The easiest way to achieve a Pulumi-based CD flow is to simply integrate it into your existing CI process.

The basic idea here is that, after running your usual CI processes upon merging a commit into a release branch, you can
proceed to doing a Pulumi deployment.  This usually entails running `pulumi update --preview` followed by a `pulumi update`.
After the deployment completes, of course, you may want to perform additional post-deployment verification.

There are many variants of this, of course.  For instance, Pulumi makes it so easy to stand up new developer stacks, you
might even consider creating a one-off stack for a branch via `pulumi stack init testing-<branch>`, stand it up from
scratch using the above flow, test it out, and then tear it down using `pulumi destroy` and `pulumi stack rm`.

Over time, we expect to develop services and tools to help accomplish these practices across a wide variety of CI
systems and workflows.  In the meantime, we'd love to [hear more](mailto:support@pulumi.com) about your scenarios,
what worked well, and what you'd like to see improved!
