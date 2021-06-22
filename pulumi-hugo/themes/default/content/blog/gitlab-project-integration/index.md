---
title: "Amp-up GitLab Merge Requests With Pulumi"
authors: ["praneet-loke"]
tags: ["continuous-delivery", "gitlab"]
date: "2020-08-26"
meta_desc: "We are excited to announce the launch of first-class support for integrating GitLab Merge Requests with Pulumi."
meta_image: pulumi_gitlab.png
---

We are excited to announce the launch of native support for integrating GitLab Merge Requests with Pulumi.
By integrating your GitLab Projects directly with Pulumi, you can now approve your merge requests
with confidence.

<!--more-->

## New To Pulumi and GitLab CI/CD?

GitLab's [merge request pipelines](https://docs.gitlab.com/ee/ci/merge_request_pipelines/) runs a CI/CD workflow for building and testing your software.
Pulumi makes a great addition to it, by allowing you to preview any infrastructure changes as part of your merge request flow.

Using the merge request pipeline feature with Pulumi can validate the changes to your infrastructure before they are applied.
Once validated and approved through a peer-review process, you can apply your changes quickly and continuously with confidence while doing so,
a process commonly referred to as GitOps for infrastructure.

To leverage GitOps for your infrastructure, the Pulumi CLI offers two commands: `preview` and `up`.

Concept | Pulumi command | Role
--- | --- | ---
Merge requests pipeline | `pulumi preview` | Preview infrastructure changes to be merged.
Master branch pipeline | `pulumi up`  | Update your infrastructure with latest changes

Learn how to use [Pulumi in GitLab CI/CD]({{< relref "docs/guides/continuous-delivery/gitlab-ci" >}}) with merge request pipelines and how to configure the [GitLab project integration with Pulumi]({{< relref "docs/guides/continuous-delivery/gitlab-app" >}}).

## Already Using Both?

If you are already a user of either Pulumi and GitLab CI/CD, you
know the importance of merge request pipelines and running Pulumi within them.
With today's announcement, you can now make any changes to your infrastructure in your merge
request front and center, so you don't miss any of those changes.

Here's a _preview_ of what that looks like 😉

![Merge Request Note](/images/docs/guides/continuous-delivery/gitlab-app/merge_request_note.png)  

Head over to our docs to learn how to [configure the GitLab integration]({{< relref "docs/guides/continuous-delivery/gitlab-app" >}}), whether for
a single project or all of the projects under a GitLab Group.

GitLab provides lots of tools for streamlining your application delivery, and the new integration with Pulumi makes things even better.
As always, we'd love to hear your feedback or suggestions for other improvements. Check out the [Pulumi Community Slack](https://slack.pulumi.com).
