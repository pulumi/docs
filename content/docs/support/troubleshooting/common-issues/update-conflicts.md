---
title_tag: "Resolving Pulumi Update Conflicts"
meta_desc: "Learn how to resolve 409 conflict errors when another update is currently in progress."
title: Update conflicts
h1: "409 conflict: Another update is currently in progress"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    support:
        name: Update Conflicts
        parent: support-troubleshooting-common-issues
        weight: 10
aliases:
    - /docs/troubleshooting/#conflict
---

Run `pulumi cancel` to cancel the update.

{{% notes type="warning" %}}
Warning! If you cancel another person's update, their update will fail immediately.
{{% /notes %}}

One of the services that the [Pulumi Cloud](/docs/pulumi-cloud/) provides is *concurrency control*. The service will allow at most one user to update a particular stack at a time. This is accomplished by using "leases"; whenever a user requests an update, they request a "lease" on the stack that gives them the right to update the requested stack. The service makes sure that only one person has a lease active at a time.

If you get this error message, this means that the service believes that somebody else has requested and was granted a lease to the stack that you are attempting to update. There are two reasons why this could be:

1. Somebody else is currently updating the stack. If you are working on a stack with more than one collaborator, it could be that your collaborators have initiated an update without your knowledge. You can confirm this by visiting the Pulumi web console and seeing who initiated the most recent update.
1. You were updating the stack, but the Pulumi CLI crashed in the middle of the update.

If you are working on a stack with no other collaborators, it is common to encounter situation number 2 if you run into a bug in Pulumi. If this update was not triggered by someone else, you can use the `pulumi cancel` command to cancel the current update. This operation revokes the "lease" that the service has given to the person who initiated the stack update.
