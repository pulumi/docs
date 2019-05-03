---
title: Troubleshooting & Support
---

{% include mini-toc.html %}

Pulumi tries very hard to ensure that your infrastructure is always in a known and predictable state.
However, sometimes things go wrong. If you can't update your stack, or there's some other problem that is
preventing you from being productive with a Pulumi stack, you've come to the right place.

## Contact Us

First thing's first, we are always happy to hear from you and will try to help. Please
[join our Community Slack](https://slack.pulumi.io), where our whole team, in addition to a passionate
community of users, are there to help out. Any and all questions are welcome!

## Common Problems

This section covers a few problems that can arise when working with Pulumi.

### [409] Conflict: Another update is currently in progress. {#conflict}

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

### [500] Internal Server Error {#internal-server-error}

The Pulumi command-line tool interacts with the Pulumi web service throughout the course of an update. If the
service is unable to process an update, it is possible that users of the command-line tool may see this error message
throughout the course of an update.

We take great pride in service uptime and work rapidly to fix service interruption and use our [status page](https://status.pulumi.com) to
communicate information about service incidents.


### post-step event returned an error {#post-step-event}

The Pulumi engine runs a small amount of code after every "step" that it performs. If this code fails for any reason,
it will fail the entire update. One of the things that the Pulumi engine does before and after every step is
a self-check on its internal data structures to ensure that they are in a consistent state. If they are not,
Pulumi will issue an error and fail the deployment.

There are two reasons why this error could occur:

1. You experienced a network partition while performing an update.
2. The Pulumi engine failed its data structure self-check.

In each case, some more specific information is printed in addition to "post-step returned an error". In the first
case, it is common for you to see an additional error indicating that some I/O operation has failed. This can be
safely disregarded and it is safe to re-start the update. You may need to
[recover from the interrupted update](#interrupted-update-recovery).

In the second case, you may see an additional error message "after mutation of snapshot". This error
message is **always a bug in Pulumi**. If you see this error message, we would greatly appreciate a
bug report on our [official bug tracker](https://github.com/pulumi/pulumi/issues). We also
recommend joining our [Pulumi Community Slack](https://slack.pulumi.io/) and sharing your problem
if you experience this error message.

#### Quick Summary

If you see an I/O error after "post-step event returned an error", you can safely re-start your
update. If you see "after mutation of snapshot", you have hit a bug in Pulumi. You will possibly
need to do some [manual intervention to repair your stack](#editing-your-deployment).

### Error during pulumi preview/up - error: could not load plugin for `aws|azure` (etc.) provider

The `pulumi` program that you author for your infrastructure may contain one or more dependencies to `providers`.
The version information for these providers is stored in the deployment for each of your stacks (since each pulumi program belongs to a stack).
This error can occur when the deployment state for a stack already contains a newer version of a specific provider, but you are trying
to run a `pulumi up` (or `preview`) command after downgrading the provider dependency in your pulumi program.

To be more specific, the error occurs because the `pulumi` [plugin cache](https://pulumi.io/reference/cli/pulumi_plugin_ls.html) does not have the required version installed.
This is especially more likely to occur if you are running `pulumi` in a CI/CD environment, since your plugin cache is likely not saved across builds.

Please note that, it is fine to have multiple versions of a provider installed and have stacks depend on different provider version. It is only a problem when you
downgrade the version of a particular stack that already has been deployed using a newer version.

Here's an example of the full error:
```
error: could not load plugin for aws provider 'urn:pulumi:<stack_name>::pulumi-service::pulumi:providers:aws::default': no resource plugin 'aws-v0.16.2' found in the workspace or on your $PATH, install the plugin using \`pulumi plugin install resource aws v0.16.2\`
```

#### Quick Summary

You may encounter an error when you downgrade provider versions _after_ your stack is already updated with a newer version.
If you must downgrade the version of a provider your `pulumi` program depends on, you will need to [manually edit your deployment](#editing-your-deployment)
and change the version of the provider your stack depends on and then import that as the latest state of your stack.

## Recovering from an Interrupted Update {#interrupted-update-recovery}

If the Pulumi CLI is interrupted when performing a deployment, you may see an error message
that looks something like this on your next update:

```
$ pulumi up
Previewing update of stack 'interruptedstack'
error: the current deployment has 1 resource(s) with pending operations:
  * ...

...
error: refusing to proceed
```

This occurs when the Pulumi CLI fails to complete cleanly. There are a number of ways this
can happen, such as:

1. The CLI experiences a network partition when attempting to save your stack's state
1. The CLI process is killed by your operating system while performing an update
1. The CLI crashes when performing an update

In any case, this error means that the Pulumi engine initiated an operation but was not able to
see if this operation was successful. Because of this, the Pulumi engine has no way of knowing
whether or not the operations it initated completed successfully or failed. This means that resources
may have been created that Pulumi does not know about.

To fix this situation, you should first cancel the last update. If the CLI was not able to save your
stack's state, it was also likely unable to tell the Service that an update has completed.

```bash
$ pulumi cancel
...
The currently running update for 'interruptedstack' has been canceled!
```

> If `pulumi cancel` fails with `error: [400] Bad Request: the update has already completed`, you can safely ignore
> that error and continue with the next step.

You should then export and import your stack. This will clear your state's stack of all pending operations.

```bash
$ pulumi stack export | pulumi stack import
warning: removing pending operation 'creating' on '...' from snapshot
Import successful.
```

For every warning that this command prints out, you should verify with your cloud provider whether or not this
operation was successful. If the operation was successful, and a resource was created, you should delete that
resource using your cloud provider's console, CLI, or SDK.

Finally, you should run `pulumi refresh` to synchronize your stack's state with the true state of your cloud
resources:

```bash
$ pulumi refresh
Refreshing stack 'interruptedstack'
Performing changes:

   Type  Name  Status     Info

   info: no changes required:
         12 resources unchanged
```

At this point your stack should be valid, up-to-date, and ready to accept future updates.

## Manually Editing Your Deployment {#editing-your-deployment}

Sometimes the only recourse for fixing a stack that is unable to do deployments is to edit the
deployment directly. It is possible to do this, though it is a tactic of last resort. It is a goal of Pulumi
to never require users to edit their state directly. We would love to hear about the issues you are experiencing
that you can't resolve, both so we can assist you in fixing your stack and also to fix the issues in Pulumi
that made it impossible for you to recover your stack in any other way.

The Pulumi engine uses both your program and your stack's existing state to make decisions about what
resources to create, read, update, or delete. The most common problem that makes it impossible to
make changes to your stack is that the stack's existing state has gotten corrupted in some way. There
are a variety of ways that a stack's state could be corrupted, but in almost all cases it is possible
to manually edit the stack's existing state to fix the corruption.

Note that this is an advanced operation and should be an absolute last resort.

If you intend to unprotect or delete a resource, consider using the [`pulumi state`](./cli/pulumi_state.html) command to
do so instead of editing your state directly. `pulumi state` also makes surgical fixes to your state but without
requiring you to edit the JSON representation of your stack's current state.

To get a JSON representation of your stack's current state, you can export your current stack
to a file:

```bash
$ pulumi stack export --file state.json
```

This file contains a lot of information. At the top-level, this JSON object has two fields:

1. A `version`, indicating the version of the file format you're currently looking at. Don't
change this.
1. A `deployment`, which represents the state of the last deployment that this stack completed.

The `deployment` object itself has three fields:

1. A `manifest`, which contains some metadata about the previous deployment. You should not ever
need to edit this.
1. A list of `pending_operations`, which is a record of the operations that the Pulumi engine
started but hasn't seen finish yet.
1. A list of `resources`, which is a record of all resource that Pulumi knows about. When you create
a resource, that resource's information is stored here.

The possible fields of a resource are:

1. `urn` - This resource's URN, or "universal resource name", which is a Pulumi-specific universal
resource identifier.
1. `custom` - A boolean indicating whether or not this resource is a "custom" resource, which means that
it uses a resource provider to operate. Component resources are not `custom`.
1. `delete` - A boolean indicating whether or not this resource is pending deletion.
1. `id` - This resource's ID, which is a provider-specific resource identifier. This often corresponds to
a cloud provider's identifier for a resource.
1. `type` - The Pulumi type of this resource.
1. `inputs` - A map of "inputs" for this resource. Inputs are the set of key-value pairs used as an input
to a resource provider that created or updated the given resource.
1. `outputs` - A map of "outputs" for this resource. Outputs are the set of key-value pairs that were given
to Pulumi by a resource provider after a resource has been provisioned.
1. `parent` - A URN for this resource's parent resource.
1. `protect` - A boolean indicating whether or not this resource is protected. If a resource is protected,
it can't be deleted.
1. `external` - A boolean indicating whether or not this resource is "external" to Pulumi. If a resource is
External, Pulumi does not own its life cycle and it will not ever delete or update the resource. Resources
that are "read" using the `get` function are External.
1. `dependencies` - A list of URNs indicating the resources that this resource depends on. Pulumi tracks dependencies
between resources and so it is important that this list be the full list of resources upon which this resource
depends.
1. `initErrors` - A list of errors that occured that prevented this particular resource from initializing. Some resource
providers (most notably Kubernetes) populate this field to indicate that a resource was created but failed to initialize.
1. `provider` - A provider reference to the provider that is responsible for this particular resource.

The `resources` field is a list, not a set; the order of resources in the list is important and is enforced by
the Pulumi engine. Resources in a deployment must be in *dependency order* - if a resource A depends on a resource B,
resource A *must* appear after resource B in the list.

Once you have completed any edits to your stack's state, you can import your changes by running:

```bash
$ pulumi stack import --file state.json
```

Depending on the class of error that you are experiencing, you may need to edit one or more of these resource fields,
as well as potentially change the location of particular resources in the list. Since this is an advanced operation,
we recommend you check-in with the [Pulumi Community Slack](https://slack.pulumi.io) first before editing your snapshot.

## Provider-specific problems {#provider-problems}

This section includes troubleshooting information specific to Pulumi providers.

### Kubernetes {#provider-kubernetes}

This section includes detailed troubleshooting information for the [Kubernetes provider](https://github.com/pulumi/pulumi-kubernetes)

#### Ingress Errors {#provider-kubernetes-ingress}

##### Ingress .status.loadBalancer field was not updated with a hostname/IP address {#ingress-status-loadbalancer}

This error is often caused by a misconfigured ingress-controller not updating the `status.loadBalancer`
field once the Ingress resource is ready to route traffic.

*Traefik*

For the Traefik controller, verify that the `kubernetes.ingressEndpoint` config
is [set properly](https://docs.traefik.io/configuration/backends/kubernetes/). This option was
introduced in Traefik 1.7.0.
