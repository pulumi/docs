---
title: "Pulumi now supports Atlassian Identity"
authors: ["praneet-loke"]
tags: ["Features","CI/CD"]
date: "2019-01-30"

meta_image: "atlassian-1.png"
---

Today we added support for yet another developer favorite product,
Atlassian Bitbucket. You can now sign-up for a Pulumi account with an
Atlassian identity. This also means you can connect your Atlassian
identity with an existing Pulumi account.

This work follows on from the support for
[GitLab identity]({{< relref "welcoming-gitlab-users-to-pulumi" >}})
and also the ability to
[connect identities]({{< relref "connecting-multiple-identities-to-pulumi" >}}),
eliminating the need for users to create multiple accounts on Pulumi.

This helps users with repos across the major version control systems to
seamlessly import their GitHub Organizations and GitLab Groups - and now
Atlassian Bitbucket Teams - into a single Pulumi account. Of course, you
don't *need* to connect identities. You can always create separate
account for each of your identities, if that's what you want to do.
<!--more-->

## Creating a new Pulumi account using your Atlassian identity

To get started using your Atlassian identity, you can navigate to
<https://app.pulumi.com> and click the Atlassian button to authenticate.
If you are already logged-in to Pulumi, you should first logout and then
head back to the Pulumi Console.

![atlassian-1](./atlassian-1.png)

## Connecting an existing Pulumi account to your Atlassian identity

If you want to connect your Atlassian identity to an existing Pulumi
account, then navigate to <https://app.pulumi.com> and once logged in,
head to Account Settings to choose the option to connect your Atlassian
identity.

![atlassian-2](./atlassian-2.png)

## Bitbucket Team-backed Organizations

A [Bitbucket Team](https://confluence.atlassian.com/bitbucket/teams-321853005.html)
helps you organize users into user groups and therefore, assign each of
them a permission to your repositories. By adding a Bitbucket
Team-backed organization, you can invite the same members to collaborate
on Pulumi. 

This allows you to set permissions on
[Stacks]({{< ref "/docs/reference/stack" >}}) owned by your
organization. You can learn more about
[Teams & Collaboration]({{< ref "/docs/reference/service" >}})
in the Pulumi and how those permissions get applied too.

## CI Integration

Did you also know that the Pulumi CLI can be used in most, if not all,
CI/CD workflows? Check out our
[documentation]({{< ref "/docs/reference/cd" >}}) for integrating
with several popular CI/CD systems. Get up and running with Pulumi in CI
on [GitLab]({{< ref "/docs/reference/cd-gitlab-ci" >}}),
[Travis]({{< ref "/docs/reference/cd-travis" >}}),
[Azure DevOps]({{< ref "/docs/reference/cd-azure-devops" >}}) and more.
Don't see docs for a particular CI system? Let us know or better yet
file an issue [here](https://github.com/pulumi/docs/issues).

Having trouble? Questions? Join our
[community Slack](https://slack.pulumi.io/) or send us an email.
