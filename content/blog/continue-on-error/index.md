---
title: "Continue on Error in the Pulumi CLI"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2024-05-09

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Introducing continue on error functionality for pulumi up and destroy.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - thomas-gummerer

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - error-handling
    - announcement

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

When managing many resources with Pulumi, a `pulumi up` or `pulumi destroy` can lead to a complex graph of resource operations being performed as concurrently as possible relative to the dependencies in your program. If one of those operations fails, you may have noticed that Pulumi takes the most conservative approach, letting already in-flight operations complete, but not starting any new operations. Most often, that's what you want -- there might be no point in bringing up more infrastructure if a resource fails.

However, in some cases it can be useful to keep going to try to bring resources that are independent from the failed one into the requested state, be that resources being created or destroyed. For example, when doing a `pulumi destroy`, you may want to have Pulumi destroy as many resources as it can, without stopping when the first error occurs.

You can now do exactly that with the new `--continue-on-error` flag for `pulumi up` and `pulumi destroy`.

<!--more-->

{{< video title="Using pulumi new with the new AI option" src="coe.mp4" controls="false" autoplay="true" loop="true" >}}

Using `--continue-on-error` means that resources that are not in the same dependency tree as the failed resource will still continue to be updated or destroyed, as they would normally.  To make sure dependencies are still correctly respected, resources that depend on a successful update or destroy of the failed resource will not continue to be updated.  This means that this flag is always safe to use, as Pulumi will continue to manage the failed resources, and they can be updated or destroyed in subsequent runs of Pulumi.

When the execution finishes, Pulumi will report the resource failures as you would currently expect from a failure, and exit with a non-zero exit code.  This indicates that even though we continued to update resources independent from the failed one, there was an error during the deployment.

## What do I need to do?

`pulumi destroy --continue-on-error` was introduced in Pulumi v3.112.0.  After upgrading to this version or later of the Pulumi CLI you can go ahead and use this feature.

`pulumi up --continue-on-error` was introduced in Pulumi v3.114.0. However, it also requires updated language SDKs to work best. Since we now have resources that fail to create, but the Pulumi program continues to execute, the SDK has to deal with the outputs of these resources.  Currently during `pulumi up` there are no "unknown" values expected by the SDK.  Since we may now have a failed resource, the outputs for that resource might still be unknown, and the SDK will have to deal with that.  This means that to fully support this feature some SDK changes were necessary.  So in addition to upgrading the Pulumi CLI to v3.114.0, you will also have to upgrade the Pulumi SDK to v3.114.0 or later for Go, Python and Node.js, and 3.63.0 or later for .NET. For Pulumi YAML programs, you'll need to use v3.115.0 or later of the Pulumi CLI.

When `--continue-on-error` is used with older SDK versions, the Pulumi engine will return an error to your program, which then will need to be handled, or the rest of the program might not be executed, and thus some resources may not be updated.

This feature was a [highly requested feature](https://github.com/pulumi/pulumi/issues/3304) in the Pulumi open source project, and we're constantly working to address these highly requested features across the open source projects, so jump in and give features you'd like to see us add a 👍.

Give `--continue-on-error` a try and [let us know](https://slack.pulumi.com) what you think!
