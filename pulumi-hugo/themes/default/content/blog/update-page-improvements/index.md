---
title: "Pulumi Cloud Gets Full Historical Views of Resources and Stack Outputs"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-12-12T10:34:32-08:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Pulumi Cloud now has enhanced stack update pages with information on the timeline, outputs, resources and policies for each update.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - meagan-cojocar
    - komal-ali

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - features
    - pulumi-cloud

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

As part of our ongoing commitment to providing developers and infrastructure teams with powerful tools, we're thrilled to introduce the latest enhancement to Pulumi Cloud's stack update pages. We have shipped an improvement to Pulumi Cloud stack update pages where all update pages now show the resources in the stack at that time and the stack outputs going back since your first update on the stack.

<!--more-->
![Screenshot of the new experience](update-page.png)

### Expanded Resource Information

Now, each update will provide detailed information about the resources. This includes a list of resources created, modified, or deleted in each update, offering a clearer understanding of the changes made to your infrastructure.

### Stack Outputs

The updated pages also now include information on the stack's outputs for each update instead of just the current point in time. The value of this is being able to go back and see what output values were after any update.

![Screenshot of the new outputs](stack-outputs.png)

### The Value of Enhanced Data Visibility

Having a more detailed and transparent view of your stack updates provides several key benefits:

1. **Resource Lifecycle Management**: Understanding when and why a resource was added, modified, or deleted helps in better managing your infrastructure's lifecycle and planning future changes.

2. **Enhanced Troubleshooting and Analysis**: The ability to go back to a specific point in time and analyze the state of your infrastructure at that moment can be invaluable in troubleshooting issues or understanding the impact of certain changes.

In summary, the improved Pulumi Cloud stack update pages offer a more detailed, transparent, and insightful view of your infrastructure changes. This upgrade came directly from customer asks, and underscores our commitment to empowering developers with the tools and information they need to effectively manage and understand their cloud resources and how they change over time.

Stay tuned for more updates as we continue to enhance our platform to better meet your needs. As always, submit any feedback on the feature in the [Pulumi Cloud Requests](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose) repository.
