---
title: "Announcing Public Preview of Insights Account Discovery"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
#date: 2024-12-2T11:00:00-08:00
date: 2024-12-02T9:10:00-00:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Insights Account Discovery makes it easy for you to gain visibility of your entire infrastructure regardless of how it is managed

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - craig-symonds

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - insights
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

Enterprise cloud infrastructures are complex environments that are evolved over time and made up of thousands of different kinds of resources. Enabling customers to wrap their arms around this complexity and get a complete understanding of the scope and structure is the goal of the Pulumi Insights 2.0 product.

<!--more-->

{{< youtube "fa7s5_oYnaM?rel=0" >}}

We are excited to announce the public preview of Insights Account Discovery that makes it easy for you to gain visibility of your entire infrastructure regardless of how it is managed. Insights provides the tools to find, group and drill into your resources as needed to make sense of all aspects of your cloud infrastructure. In addition Copilot AI gives you the ability to get answers about your infrastructure that can be challenging to get in other ways, dramatically simplifying the work needed to move your infrastructure forward.

### Account Management

To get started, Insights Account Discovery provides a simple UI approach to setting up all of your infrastructure accounts to be scanned and read into the Insights supergraph. Once discovered, all of your infrastructure resources can then be seen in the Resource Explorer and accessed by Pulumi Copilot and Resource Search, providing you the tools needed to deliver on your strategic infrastructure goals.

Account Discovery starts with the new Accounts page to provide a list of all accounts created along with the current status of the latest account scans. The Accounts page is the single place to go to manage all aspects of the Insights Account Discovery process.

{{< video title="Accounts" src="accounts.mp4" autoplay="true" loop="true" >}}

### Account Creation

From this page you can create new Accounts to provide the configuration and credentials needed for Insights to regularly scan and manage your infrastructure. Once you create a new top level Account, Insights will automatically create child accounts, based on the underlying platform model, for each group you enabled. These child accounts enable you to control the discovery behavior for each group separately. For example, AWS enables you to divide you infrastructure into regions and Insights will create separate child accounts for each region you specify.

{{% notes type="info" %}}
Account Discovery leverages Pulumi ESC to enter and manage the credentials needed for the Discovery process to find and read all of the infrastructure resources. By relying on ESC, Insights aligns with enterprise best practices for creating and handling application secrets.
{{% /notes %}}

{{< video title="Create Account" src="create-account.mp4" autoplay="true" loop="true" >}}

### Understanding Your Infrastructure

Once each of your Accounts have started scanning, your resources will be displayed in the Insights Resources Explorer along with all Infrastructure as Code resources that you have imported. The Resources Explorer and Resources Search enables you to ask questions and factor your resources into logical groupings that significantly improves the process for managing your infrastructure and getting answers to key questions needed for your projects. For example, you can ask the AI Resource Search to 'Find all public IP addresses' and any other question you might have about your infrastructure.

{{< video title="Discovered Resources" src="resources.mp4" autoplay="true" loop="true" >}}

### More to Come

We are excited about the potential of Pulumi Insights and are working hard to bring additional capabilities to continue to simplify the experience of managing today's complex cloud environments. Watch for additional features like Pulumi Crossguard Policy support for Discovered resources, along with additional platform support, and more, coming soon.

Insights Account Discovery is free while in public preview, with per-resource pricing for Team, Enterprise and Business Critical tiers coming in Q1 2025.

### Conclusion

The addition of Account Discovery significantly expands the scope of Pulumi Insights. You can now leverage the capabilities of Insights 2.0, not just for your Pulumi IaC managed resources, but for all resources in your infrastructure regardless of how they are managed. With Pulumi Copilot and Resource Search, you are able to gain insights and ask questions about your infrastructure that would otherwise be challenging to answer, saving time and providing the critical information needed.

For additional information about Pulumi Insights please refer to: [Pulumi Insights](https://www.pulumi.com/product/pulumi-insights/)
