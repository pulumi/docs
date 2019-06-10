---
title: "TODO Port frontmatter"
authors: ["chris-smith"]
tags: ["todo"]
date: "2017-01-01"
draft: true
description: "TODO: Put in a reasonable summary"
---

[Today we added support for yet another developer favorite product,
Atlassian Bitbucket. You can now sign-up for a Pulumi account with an
Atlassian identity. This also means you can connect your Atlassian
identity with an existing Pulumi account.

This work follows on from the support for [GitLab
identity](../../../com/pulumi/blog/welcoming-gitlab-users-to-pulumi.html)
and also the ability to [connect
identities](../../../com/pulumi/blog/connecting-multiple-identities-to-pulumi.html),
eliminating the need for users to create multiple accounts on Pulumi.

This helps users with repos across the major version control systems to
seamlessly import their GitHub Organizations and GitLab Groups - and now
Atlassian Bitbucket Teams - into a single Pulumi account. Of course, you
don't *need* to connect identities. You can always create separate
account for each of your identities, if that's what you want to do.
]{#hs_cos_wrapper_post_body .hs_cos_wrapper .hs_cos_wrapper_meta_field

Creating a new Pulumi account using your Atlassian identity
-----------------------------------------------------------

To get started using your Atlassian identity, you can navigate to
<https://app.pulumi.com> and click the Atlassian button to authenticate.
If you are already logged-in to Pulumi, you should first logout and then
head back to the Pulumi Console.

[![atlassian-1](https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-1.png?width=600&name=atlassian-1.png){width="600"
sizes="(max-width: 600px) 100vw, 600px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-1.png?width=300&name=atlassian-1.png 300w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-1.png?width=600&name=atlassian-1.png 600w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-1.png?width=900&name=atlassian-1.png 900w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-1.png?width=1200&name=atlassian-1.png 1200w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-1.png?width=1500&name=atlassian-1.png 1500w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-1.png?width=1800&name=atlassian-1.png 1800w"}](https://app.pulumi.com)

Connecting an existing Pulumi account to your Atlassian identity
----------------------------------------------------------------

If you want to connect your Atlassian identity to an existing Pulumi
account, then navigate to <https://app.pulumi.com> and once logged in,
head to Account Settings to choose the option to connect your Atlassian
identity.

![atlassian-2](https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-2.png?width=600&name=atlassian-2.png){width="600"
sizes="(max-width: 600px) 100vw, 600px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-2.png?width=300&name=atlassian-2.png 300w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-2.png?width=600&name=atlassian-2.png 600w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-2.png?width=900&name=atlassian-2.png 900w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-2.png?width=1200&name=atlassian-2.png 1200w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-2.png?width=1500&name=atlassian-2.png 1500w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-2.png?width=1800&name=atlassian-2.png 1800w"}

Bitbucket Team-backed Organizations
-----------------------------------

A [Bitbucket
Team](https://confluence.atlassian.com/bitbucket/teams-321853005.html)
helps you organize users into user groups and therefore, assign each of
them a permission to your repositories. By adding a Bitbucket
Team-backed organization, you can invite the same members to collaborate
on Pulumi. 

This allows you to set permissions on
[Stacks](https://pulumi.io/reference/stack.html) owned by your
organization. You can learn more about [Teams &
Collaboration](https://pulumi.io/reference/service/index.html) in Pulumi
in the docs.

![atlassian-3](https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-3.png?width=310&name=atlassian-3.png){width="310"
sizes="(max-width: 310px) 100vw, 310px"
srcset="https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-3.png?width=155&name=atlassian-3.png 155w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-3.png?width=310&name=atlassian-3.png 310w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-3.png?width=465&name=atlassian-3.png 465w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-3.png?width=620&name=atlassian-3.png 620w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-3.png?width=775&name=atlassian-3.png 775w, https://blog.pulumi.com/hs-fs/hubfs/Blog/atlassian-3.png?width=930&name=atlassian-3.png 930w"}

CI Integration
--------------

Did you also know that the Pulumi CLI can be used in most, if not all,
CI/CD workflows? Check out our
[documentation](https://pulumi.io/reference/cd.html) for integrating
with several popular CI/CD systems. Get up and running with Pulumi in CI
on [GitLab](https://pulumi.io/reference/cd-gitlab-ci.html),
[Travis](https://pulumi.io/reference/cd-travis.html), [Azure
DevOps](https://pulumi.io/reference/cd-azure-devops.html) and more.
Don't see docs for a particular CI system? Let us know or better yet
file an issue [here](https://github.com/pulumi/docs/issues).

Having trouble? Questions? Join our [community
Slack](https://slack.pulumi.io/) or send us an email.

