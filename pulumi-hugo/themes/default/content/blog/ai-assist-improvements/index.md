---
title: "Resource Search - AI Assist is Generally Available"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-08-07T08:42:44-07:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Pulumi Cloud Resource Search adds new I'm Feeling Lucky functionality, new and easier to use toggle and expands access outside of waitlist.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - meagan-cojocar

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - features
    - ai
    - data-and-analytics

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Pulumi Cloud [Resource Search](/docs/pulumi-cloud/insights/search) AI assist functionality is now generally available to all organizations! In addition we have shipped some improvements to the feature to make it easier to use and more discoverable: a toggle on the search bar, suggested queries and an "I'm Feeling Lucky" button to generate a random query for you.

<!--more-->
See it in action below!

![Walking through the new AI assist experience](https://www.pulumi.com/uploads/feeling-lucky.gif)

### AI Assist is Generally Available

Resource Search AI assist is a way to search your Pulumi organization using natural language. We launched it in a [private beta in April](/blog/pulumi-insights) this year. Previously only customers who requested private beta access have been able to leverage natural language resource search, starting today customers on any edition of Pulumi Cloud, AI assist is generally available. You can provide a plain English (or Spanish, or French, or Japanese!) request, to express queries where you might not know the exact syntax, type tokens, or package names. AI Assist makes it easier to gain insight over infrastructure, using queries like:

1. `show me all s3 buckets not tagged in production`
2. `show azure and azure native security groups`
3. `show all AWS VPCs`

### Suggested Queries and I'm Feeling Lucky

A blank search bar can be intimidating. We now have suggested natural language searches to get you up and running faster. We also added "I'm Feeling Lucky" functionality that generates random queries for you. This can be a good way to quickly understand the types of insights Resource Search can deliver for your organization.

### Wrapping Up

As always, submit any feedback on the feature in the [Pulumi Cloud Requests](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose) repository.
