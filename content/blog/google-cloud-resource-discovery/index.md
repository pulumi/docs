---
title: "Introducing Google Cloud to Insights Account Discovery"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2025-07-11T12:38:18-05:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Pulumi Insights now supports Google Cloud resource discovery, uncovering all resources—including those unmanaged by infrastructure as code—for full visibility.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - insights-team

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - insights
    - google cloud
    - resources


# The social copy used to promote this post on Twitter and Linkedin. These
# properties do not actually create the post and have no effect on the
# generated blog page. They are here strictly for reference.

# Here are some examples of posts we have made in the past for inspiration:
# https://www.linkedin.com/feed/update/urn:li:activity:7171191945841561601
# https://www.linkedin.com/feed/update/urn:li:activity:7169021002394296320
# https://www.linkedin.com/feed/update/urn:li:activity:7155606616455737345
# https://twitter.com/PulumiCorp/status/1763265391042654623
# https://twitter.com/PulumiCorp/status/1762900472489185492
# https://twitter.com/PulumiCorp/status/1755637618631405655

social:
    twitter:
    linkedin:

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

We're excited to introduce Google Cloud support to [Insights Account Discovery](/docs/insights/get-started/). This new capability expands Pulumi’s resource discovery to help you uncover infrastructure in Google Cloud, regardless of how those resources are managed. With full visibility into all of your cloud resources, you can monitor, search, and manage your environments more effectively.

<!--more-->

![Provider Selection](./provider-selection.png)

## Scan an Entire Google Cloud Project in Minutes

With [Pulumi Insights](/blog/insights-cloud-account-discovery/), gaining visibility into your Google Cloud environment is fast and frictionless. Once configured, Pulumi  scans your selected project and uncovers resource data across services like Compute Engine, Cloud Storage, IAM, networking, and more.  There’s no need to install agents or write custom scripts—just link your account and let Pulumi do the rest.

Within minutes, you’ll have a comprehensive view of your cloud infrastructure, including resources not managed by infrastructure-as-code. From there, you can explore your project, search for specific configurations, and start identifying security gaps, cost inefficiencies, and compliance risks.

## Visibility Beyond Infrastructure as Code

While infrastructure as code provides control and repeatability, the reality of most cloud environments includes resources created manually or by third-party automation. [Pulumi Insights](/docs/insights/get-started/) bridges that gap by discovering all of your resources—regardless of how they were created.

With this unified view, you can:

* Identify drift from your intended infrastructure state
* Spot resources that may introduce security or cost risks
* Enforce compliance across all resources using [Pulumi Crossguard](/blog/enforcing-policy-as-code-on-discovered-resources-with-pulumi/)
* Bring unmanaged resources under Pulumi IaC using [Pulumi Interactive Import](/blog/visual-import/)

This makes [Pulumi Insights](/docs/insights/get-started/) an essential tool not just for monitoring, but also for cloud governance, compliance, and modernization.

## Getting Started

Get started today by [creating a Google Cloud Insights Account](/docs/insights/accounts/#google-cloud) and start uncovering your hidden resources.
