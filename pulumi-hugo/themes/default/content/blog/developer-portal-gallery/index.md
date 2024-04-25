---
title: "Developer Portal Gallery: Org Templates, Pulumi Templates and AI Generated Templates"
allow_long_title: True
# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-01-25

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Pulumi Cloud adds a template gallery to make creating cloud infrastructure easier than ever.

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
    - developer-portals
    - platform-engineering

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

Late last year [we announced Pulumi for Developer Portals](/blog/building-developer-portals): a suite of features designed to empower organizations to construct robust internal developer portals. Since launching the level of adoption and customer interest has led us to make further improvements to enhance developer productivity and collaboration in the authoring experience. We are excited to announce the latest enhancement in Pulumi Cloud: the introduction of a template gallery in New Project Wizard, making creating cloud infrastructure easier than ever.

<!--more-->
## See it in action

{{< video title="Walking through the gallery experience" src="https://www.pulumi.com/uploads/gallery.mp4" width=600 height=420 autoplay="true" loop="true" >}}

## What the Pulumi Cloud New Project Wizard?

The Pulumi Cloud [New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard) is the fastest way to get a Pulumi program up and running. The New Project Wizard provides a more turnkey, out-of-the-box alternative to the [Pulumi Backstage Plugin](/docs/pulumi-cloud/developer-portals/backstage) or custom-built integrations.

By using the wizard, developers can generate Pulumi programs from your Organization Templates, commit and push code to GitHub, and trigger an initial deployment – all in a few clicks and without leaving the browser.

Try it out by selecting the 'New Project' option on the left-nav bar inside your Pulumi organization.

## What is a template gallery?

The Pulumi Cloud template gallery is a curated collection of templates designed to help Platform Teams provision and distribute templates that get their developers up and running. Whether they're setting up a simple server or orchestrating a complex microservices architecture, the template gallery can support a wide array of starting points that are both time-efficient and best practice-oriented. The idea is simple yet powerful – provide developers with the resources they need to get up and running swiftly, without having to reinvent the wheel each time.

The new template gallery in Pulumi Cloud contains three types of templates:

1. **Organization Templates**: Pulumi Cloud Enterprise and Business Critical editions support registering [your own custom templates for your organization](/docs/pulumi-cloud/developer-portals/templates) which will be made available in the New Project Wizard. This enables platform teams to standardize infrastructure creation and distribute those best practices where developers are already spending their time.
2. **Pulumi Templates**: All Pulumi Cloud organizations get a handful of Pulumi templates included in the gallery, [templates Pulumi has authored](/templates) to cover common architecture patterns.
3. **AI Generated Templates**: Starting today, you can leverage [Pulumi AI](/ai) to genera†e the templates you need from the template gallery. Pulumi AI is a purpose-built AI assistant that can create cloud infrastructure using Pulumi. If your developers are looking for a template that is not yet created, Pulumi AI can dramatically reduce the time it takes to build their Pulumi program.

## Wrapping up

We look forward to hearing about your experience trying out the new project wizard template gallery! As always, please raise any feedback- big or small- in the [Pulumi Cloud Requests repository](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose).

Happy building!
