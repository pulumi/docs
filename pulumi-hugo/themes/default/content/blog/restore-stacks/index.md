---
title: "Announcing Restore Stacks: Recover Deleted Stacks in the Pulumi Cloud"
allow_long_title: true
# The date represents the post's publish date,
# and by default corresponds with the date this file was generated.
# Posts with future dates are visible in development,
# but excluded from production builds.
# Use the time and timezone-offset portions of of this value
# to schedule posts for publishing later.
date: 2023-07-19

# Use the meta_desc property to provide a brief summary
# (one or two sentences) of the content of the post,
# which is useful for targeting search results or social-media previews.
# This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: Pulumi Cloud launches new Restore Stacks feature for Enterprise and Business Critical editions.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect ratio
# has been provided for you.
meta_image: meta.png

# At least one author is required.
# The values in this list correspond with the `id` properties
# of the team member files at /data/team/team.
# Create a file for yourself if you don't already have one.
authors:
    - meagan-cojocar
    - isabel-suchanek

# At least one tag is required.
# Lowercase, hyphen-delimited is recommended.
tags:
    - features

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md.
# for additional details,
# and please remove these comments before submitting for review.
---

Starting today, you can restore previously deleted stacks in the Pulumi Cloud console. We've had a number of requests from customers to recover stacks, either because the stack was accidentally deleted or the stack was intentionally deleted but, later on, they want to restore and preserve the activity history on the stack and just remove its resources.

<!--more-->

Customers often use `pulumi destroy` to delete the resources in a stack but leave the state file. If they want to delete the state file they use `pulumi stack rm`. Customers might also use `pulumi stack rm --force`, which forces the deletion of the state file but leaves behind its resources and in doing so you lose the ability to manage those resources going forward. There are cases where a force delete is a valid choice, but at Pulumi we sometimes receive customer support tickets when someone runs `pulumi stack rm --force` accidentally. One of the benefits of using Pulumi Cloud is that it maintains state file versions enabling Pulumi to be able to restore deleted state files. Starting today we have built this recovery process into the product, allowing customers to self-serve restoration of deleted state files.

### See it in action

![Walking through the restore stacks experience](https://www.pulumi.com/uploads/restore-stacks.gif)

And tada 🎉, you how have a trash bin for your stacks! To recover a deleted stack, organization admins should navigate to the Stacks page. Next to the Create Project button there is a three dot menu to transfer stacks and restore stacks. Click on restore stacks to navigate to your recently deleted stacks. The last 10 deleted stacks in an organization can be restored, if you need a stack restored that is older, contact support.

### Keep the feedback coming

As always, submit any feedback on the feature in the [Pulumi Cloud Requests](https://github.com/pulumi/pulumi-cloud-requests/issues/new/choose) repository.
