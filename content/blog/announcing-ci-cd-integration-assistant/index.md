---
title: "Announcing CI/CD Integration Assistant for teams"
authors: ["praneet-loke"]
tags: ["CI/CD"]
date: "2020-11-18"
meta_desc: "We are excited to announce the launch of the integration assistant to make integration with CI/CD easy."
meta_image: integration-assistant.png
---

We are excited to announce the launch of the integration assistant to make integration with CI/CD easy.
Now you can easily get started with popular CI/CD services without the hassle of the initial setup.

<!--more-->

We often hear developers wanting to setup CI/CD automation for their stacks but don't have the time or simply don't like
the experience of figuring out how to configure a working pipeline. The integration assistant not only guides you with
instructions based on the CI/CD service, but also provides the customized pipeline configuration
for CI/CD services that you can add to your VCS repo.

The following CI/CD services are supported at launch:

* [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/)
* [Bitbucket Pipelines](https://support.atlassian.com/bitbucket-cloud/docs/get-started-with-bitbucket-pipelines/)
* [GitHub Actions](https://github.com/features/actions)
* [GitLab CI/CD](https://docs.gitlab.com/ce/ci/)

> You can always [request](https://github.com/pulumi/ci-workflow-templates/issues/new/choose) support for a new CI/CD service.

### What is a VCS?

A VCS is a version control system. You may already be familiar with Git-based services such as
[Atlassian Bitbucket](https://bitbucket.org), [GitHub](https://github.com), [GitLab](https://gitlab.com).
Adding your code to a central VCS allows you to secure your codebase against failures, as well as team collaboration.
When you add an automated CI/CD pipeline your team will be able to deliver software safely and efficiently.

The assistant also goes beyond helping you get started with an automated pipeline. It works throughout the Pulumi Console
providing hints for configuring a VCS for projects that don't have one, as well as identifying updates in the activity
tab of you stack that were not run in an automated pipeline. These additions will help you quickly identify the stacks
where the best practices are not being followed and take corrective actions.

Access the wizard in the Integrations option of your stack's settings page to help you through the whole process of
configuring a VCS to setting up a working automated pipeline.

Learn more about the [CI/CD integration assistant]({{< relref "/docs/intro/console/extensions/ci-cd-integration-assistant" >}}).

We are eager to hear your feedback on how we can improve your experience with this feature. If you
haven't already signed up for our [Community Slack](https://slack.pulumi.com), it's quick and easy! You can join in on
conversations you like and get help from other community members, as well as the Pulumi Team. That's it for now! 👋
