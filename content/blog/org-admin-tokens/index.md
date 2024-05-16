---
title: "Admin Organization Access Tokens in Pulumi Cloud"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-08-28

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Pulumi Cloud now has Admin Organization Access Tokens, Organization Access Tokens with increased privileges.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - meagan-cojocar
    - devon-grove

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - features

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Last year [we launched Organization Access Tokens for Pulumi Cloud](/blog/organization-access-tokens), service tokens not tied to individual users, ideal for garnering programmatic access for continuous integration and continuous delivery (CI/CD) tools and other automated processes. After launching this feature we saw record level adoption, with a majority of customers who could use it creating Organization Access Tokens within a matter of weeks.

<!--more-->

Organization Access Tokens have member level permissions, meaning they can be used to perform actions that a member has permissions to perform. We heard from multiple customers that being able to provision access tokens with admin level permissions would light up several programmatic use cases. Today we are launching an Admin permission scope for Organization Access Tokens: increased privileges for when you need them.

### See it in action!

![Gif of creating an Admin token](https://www.pulumi.com/uploads/admintoken.gif)

### Increased Privileges

{{% notes type="warning" %}}
Admin Organization Access Tokens have elevated permissions, please use them with caution.
{{% /notes %}}

Admin Organization Access Tokens can perform many actions that a regular Organization Access Token can not. Here are some of the actions you can now perform with a token that were previously not possible:

- Transferring stacks
- Adding and removing users in your organization
- Update team membership roles
- Add and remove stacks from Teams
- Add and remove Team Access Tokens
- Get audit log events

For a full list of all actions that can be performed by each access token type please refer to the [Access Token documentation](/docs/pulumi-cloud/access-management/access-tokens/).

### Wrapping up

Organization Access Tokens are available to Enterprise and Business Critical customers, as well as on our 14-day trial. You can [start a trial](https://app.pulumi.com/site/trial) or [Contact Us](/contact?form=sales) about the Pulumi Service Enterprise Edition and Business Critical Edition to take it for a spin!

As always, submit any feedback on the feature in the [Pulumi Cloud Requests](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose) repository.
