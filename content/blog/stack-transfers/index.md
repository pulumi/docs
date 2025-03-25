---
title: "Transferring Stacks in the Pulumi Service Just Got Easier"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-12-07T11:11:45-08:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
# Max length is 160 characters.
meta_desc: We are excited to announce bulk stack transfer to address this feedback
  and a new organization set up wizard to improve discovery of the feature.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
  - meagan-cojocar

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
  - features
  - pulumi-service

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
search:
  keywords:
    - easier
    - transferring
    - transfer
    - got
    - stacks
    - bulk
    - organization
---

Exactly 3 years ago we added support in the [Pulumi Service](/product/pulumi-service) to transfer stacks from an Individual account to a Pulumi organization and between Pulumi organizations. We heard from customers that they love this feature but found it both hard to discover and tedious when moving a large workload from one organization to another and from Individual accounts to organizations. We are excited to announce bulk stack transfer to address this feedback and a new organization set up wizard to improve discovery of the feature.

<!--more-->

Let’s review how bulk stack transfers can be used and when you would use them. Stack transfers relocate a stack between organizations and Individual accounts. Let’s highlight some use cases:

- **Use case #1: Individual account to a collaborative organization:** We know that users are building projects in Individual accounts and want to easily move their stacks to an organization so they can collaboratively build infrastructure with others.
- **Use case #2: Organization to Individual account:** There may be instances where users want to take a stack from an organization into their Individual org. This could be due to mistakenly creating a stack in the wrong location.
- **Use case #3: Organization to organization:** As customers scale there may be use cases where they want to add additional organizations and being able to transfer stacks in bulk will help with this.

### Transferring one stack

To transfer a specific stack, you can navigate to that stack and then go to Settings > Transfer Stack. To transfer a stack, you need to be either the Stack Admin or an Organization Admin. For organizations on the Pulumi Enterprise or Business Critical Editions, an audit log will be produced each time a stack is transferred and it records which organization the stack was transferred to.

![Transfer stack](transfer_stack.png)

### Transferring multiple stacks

To transfer multiple stacks, you can navigate to the Stacks page and then click the `...` icon beside the ‘Create a Project’ button in a collaborative organization and the `Transfer stacks` button in an Individual account. In order to transfer multiple stacks you need to be an Organization Admin. For organizations on the Pulumi Enterprise or Business Critical Editions, an audit log will be produced each time a stack is transferred and it records which organization the stack was transferred to.

![Bulk stack transfer](bulk_transfer.png)

### Bringing stacks into new organizations

We recently added a new organization setup wizard that will walk you through inviting members, importing stacks and setting your preferred cloud and language when you create a new organization. This compacts common usage patterns into one place to make it easier for you.

See it in action!

![New org flow](new-org-flow.png)

Learn more in the [Stack Transfer documentation](/docs/pulumi-cloud/projects-and-stacks/#transferring-stacks). Please submit an issue in the [Pulumi Service Requests repo](https://github.com/pulumi/pulumi-cloud-requests/issues/new?assignees=&labels=kind%2Fenhancement&template=feature-request.md) if you have feature requests for the Pulumi Service or [join our Slack channel](https://slack.pulumi.com) if you have questions.

Until next time!
