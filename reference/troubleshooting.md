---
title: Troubleshooting
---

Pulumi tries very hard to ensure that your infrastructure is always in a known and predictable state.
However, the reality is that sometimes things go wrong. If you can't update your stack, or there's
some other problem that is preventing you from being productive with a Pulumi stack, you've come to the
right place.

## Common Problems

This section covers a few problems that can arise when working with Pulumi.

### [409] Conflict: Another update is currently in progress.

One of the services that `pulumi.com` provides is *concurrency control*. The service will allow
at most one user to update a particular stack at a time. This is accomplished by using "leases"; whenever a user
requests an update, they request a "lease" on the stack that gives them the right to update the requested stack.
The service makes sure that only one person has a lease active at a time.

If you get this error message, this means that the service believes that somebody else has requested and was granted
a lease to the stack that you are attempting to update. There are two reasons why this could be:

1. Somebody else is currently updating the stack. If you are working on a stack with more than one collaborator, it could
be that your collaborators have initiated an update without your knowledge. You can confirm this by visiting the Pulumi
web console and seeing who initiated the most recent update.
2. You were just updating the stack, but the Pulumi command-line tool crashed in the middle of the update.

If you are working on a stack with no other collaborators, it is common to encounter situation number 2 if you
run into a bug in Pulumi. If you are *absolutely sure* that this update was not triggered by someone else, you can use the
`pulumi cancel` command to cancel the current update. This operation revokes the "lease" that the service has given
to the person who initiated the stack update.

#### Quick Summary

Run `pulumi cancel` to cancel the update.

> Warning! If you cancel another person's update, their update will fail immediately.

### [500] Internal Server Error

The Pulumi command-line tool interacts with the Pulumi web service throughout the course of an update. If the
service is unable to process an update, it is possible that users of the command-line tool may see this error message
throughout the course of an update.

We take great pride in service uptime and work rapidly to fix service interruption. You can follow our
[official Twitter account](https://twitter.com/PulumiCorp) to keep up-to-date on service interruptions.

### post-step event returned an error

The Pulumi engine runs a small amount of code after every "step" that it performs. If this code fails for any reason,
it will fail the entire update.

There are a few specific errors that commonly cause a post-step failure:

#### after mutation of snapshot

Before and after every operation, the Pulumi engine performs a self-check on its internal data structures to ensure
that they are in a consistent state. If they are not, Pulumi will issue an error and fail the deployment.

This error message is **always a bug in Pulumi**. If you see this error message, we would greatly appreciate a bug report
on our [official bug tracker](https://github.com/pulumi/pulumi/issues).
