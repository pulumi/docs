---
title_tag: "Pulumi Troubleshooting Guide"
meta_desc: This guide covers common troubleshooting techniques when using Pulumi, such as tracing, manually editing deployments, and resolving common errors.
title: Troubleshooting
h1: Pulumi troubleshooting
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Troubleshooting
        parent: iac-support
        weight: 2
        identifier: iac-support-troubleshooting
    support:
        weight: 1
search:
    keywords:
        - debugging pulumi programs

aliases:
    - /docs/reference/troubleshooting/
    - /docs/troubleshooting/
    - /docs/support/troubleshooting/
---

Sometimes things go wrong. If you can't update your stack, or there's another problem that is
preventing you from being productive, you've come to the right place.

## Talk to a human

[Join Community Slack](https://slack.pulumi.com), where our whole team, in addition to a passionate
community of users, are there to help. Any and all questions are welcome!

We also encourage everyone to contribute to the [Pulumi open source
projects](https://github.com/pulumi) by [opening new issues](https://github.com/pulumi/pulumi/issues/new) and upvoting existing issues.

Or email our support team: [support@pulumi.com](mailto:support@pulumi.com).

## Verbose logging

Verbose logging of the internals of the Pulumi engine and resource providers can be enabled by
passing the `-v` flag to any `pulumi` CLI command. Pulumi emits logs at log levels between `1` and
`11`, with `11` being the most verbose. At log level 10 or below, Pulumi will avoid intentionally exposing any *known* credentials. At log level 11, Pulumi will intentionally expose some known credentials to aid with debugging, so these log levels should be used only when absolutely needed.

By default, logs are written to the top-level temp directory (usually `/tmp` or the value of
`$TMPDIR`). The `--logtostderr` flag can be used to write logs to stderr instead.
Use the flag `--logflow` to apply the same log level to resource providers.

{{% notes type="warning" %}}
Enabling verbose logging may reveal sensitive information (tokens, credentials...) that is provided from
your execution environment directly to your cloud provider, and which Pulumi may not be aware of. Before sharing the logs, be careful to audit and redact any sensitive information.
{{% /notes %}}

```bash
$ pulumi up --logtostderr --logflow -v=10 2> out.txt
```

Diagnostic logging can also be controlled with flags and environment variables of the resource providers. For example, Pulumi providers that use a bridged Terraform provider can make use of the [`TF_LOG`](https://www.terraform.io/docs/internals/debugging.html) environment variable (set to `TRACE`, `DEBUG`, `INFO`, `WARN` or `ERROR`) in order to provide additional diagnostic information.

```bash
$ TF_LOG=TRACE pulumi up --logtostderr --logflow -v=10 2> out.txt
```

## Attaching a debugger to a Pulumi program

When developing or troubleshooting Pulumi programs, you may need to debug your code. This example walks you through starting a Node.js debugging session in VS Code and setting breakpoints.

### Create VS Code launch configuration

In your project directory, create or update `.vscode/launch.json` with the following configuration to enable debugging:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Pulumi Program (debug)",
            "type": "node",
            "request": "attach",
            "continueOnAttach": true,
            "skipFiles": [
                "${workspaceFolder}/node_modules/**/*.js",
                "${workspaceFolder}/lib/**/*.js",
                "<node_internals>/**/*.js"
            ]
        }
    ]
}
```

### Set breakpoints and start Pulumi in debug mode

Open your program and set breakpoints by clicking in the gutter next to the line numbers.

In a terminal run `NODE_OPTIONS=”--inspect-brk” pulumi up` to start the deployment process in debug mode. This will cause Pulumi to pause execution and wait for a debugger to attach.

Press `F5` in VS Code to start debugging. VS Code will attach to the waiting Node.js process, and execution will continue until reaching the first breakpoint you have set.

For a step-by-step guide for attaching a debugger to a Pulumi TypeScript program, check out this [blog on breakpoint debugging.](/blog/next-level-iac-breakpoint-debugging/)

Guides for all languages supported by Pulumi are available in [the Debugging guide](/docs/using-pulumi/debugging/).

## Performance

If you are seeing unexpectedly slow performance, you can gather a trace to understand what
operations are being performed throughout the deployment and what the long poles are for your
deployment. In most cases, the most time-consuming operations will be the provisioning of one or more resources in your cloud
provider, however, there may be cases where Pulumi itself is doing work that is limiting the performance
of your deployments, and this may indicate an opportunity to further improve the Pulumi deployment
orchestration engine to get the maximal parallelism and performance possible for your cloud
deployment.

### Tracing

To collect a trace:

```
$ pulumi up --tracing=file:./up.trace
```

To view a trace locally using [AppDash](https://github.com/sourcegraph/appdash):

```
$ PULUMI_DEBUG_COMMANDS=1 pulumi view-trace ./up.trace
Displaying trace at http://localhost:8008
```

Pulumi also supports [Zipkin](https://zipkin.io) compatible tracing.
To collect a trace to a local
[Jaeger](https://www.jaegertracing.io/docs/1.22/getting-started/)
server:

```
$ docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -p 16686:16686 \
  -p 9411:9411 \
  jaegertracing/all-in-one:1.22

$ pulumi up --tracing http://localhost:9411/api/v1/spans
```

To view a trace locally navigate to the [Jaeger UI](http://localhost:16686/search).

## Common problems

### 409 conflict: Another update is currently in progress. {#conflict}

Run `pulumi cancel` to cancel the update.

{{% notes type="warning" %}}
Warning! If you cancel another person's update, their update will fail immediately.
{{% /notes %}}

One of the services that the [Pulumi Cloud](/docs/pulumi-cloud/) provides is *concurrency control*.
The service will allow at most one user to update a particular stack at a time. This is accomplished by using "leases"; whenever a user
requests an update, they request a "lease" on the stack that gives them the right to update the requested stack.
The service makes sure that only one person has a lease active at a time.

If you get this error message, this means that the service believes that somebody else has requested and was granted
a lease to the stack that you are attempting to update. There are two reasons why this could be:

1. Somebody else is currently updating the stack. If you are working on a stack with more than one collaborator, it could
be that your collaborators have initiated an update without your knowledge. You can confirm this by visiting the Pulumi
web console and seeing who initiated the most recent update.
1. You were updating the stack, but the Pulumi CLI crashed in the middle of the update.

If you are working on a stack with no other collaborators, it is common to encounter situation number 2 if you
run into a bug in Pulumi. If this update was not triggered by someone else, you can use the
`pulumi cancel` command to cancel the current update. This operation revokes the "lease" that the service has given
to the person who initiated the stack update.

### 500 Internal server error {#internal-server-error}

The Pulumi CLI interacts with the Pulumi web service throughout the course of an update. If the
service is unable to process an update, it is possible that users of the CLI may see this error message
throughout the course of an update.

We take great pride in service uptime and work rapidly to fix service interruption. The [Pulumi status page](https://status.pulumi.com) communicates information about service incidents.

### Post-step event returned an error {#post-step-event}

If an I/O error occurs after "post-step event returned an error", you can safely re-start your
update. If you see "after mutation of snapshot", you have hit a bug in Pulumi. You will possibly
need to do some [manual intervention to repair your stack](#editing-your-deployment).

The Pulumi engine runs a small amount of code after every "step" that it performs. If this code fails for any reason,
it will fail the entire update. One of the things that the Pulumi engine does before and after every step is
a self-check on its internal data structures to ensure that they are in a consistent state. If they are not,
Pulumi will issue an error and fail the deployment.

There are two reasons why this error could occur:

1. You experienced a network partition while performing an update.
2. The Pulumi engine failed its data structure self-check.

In each case, some more specific information is printed in addition to "post-step returned an error". In the first
case, it is common for you to see an additional error indicating that some I/O operation has failed. This can be disregarded and it is safe to re-start the update. You may need to
[recover from the interrupted update](#interrupted-update-recovery).

In the second case, you may see an additional error message "after mutation of snapshot". This error
message is **always a bug in Pulumi**. If you see this error message, please open a [GitHub issue](https://github.com/pulumi/pulumi/issues). We also
recommend joining our [Pulumi Community Slack](https://slack.pulumi.com/) and sharing your problem
if you experience this error message.

### Cannot connect to Pulumi Cloud

If your network blocks external traffic and you're using Pulumi Cloud to manage your state, your security team may need the following details to allow the Pulumi CLI to connect to Pulumi Cloud:

- The URL that the Pulumi CLI uses to connect to Pulumi Cloud is `https://api.pulumi.com`. (It does not use `https://app.pulumi.com`, so if you want to view the console from a web browser, you will need to enable that as well.)
- All access goes over HTTPS via port 443.

### Nothing happens due to a network proxy

You run Pulumi and nothing happens, with output resembling this:

```
$ pulumi up
Previewing update (<stack name>):

Resources:

$
```

If you have a system-wide proxy server running on your machine, it may be misconfigured. The [Pulumi architecture](/docs/concepts/how-pulumi-works/) has three different components, running as separate processes that talk to each other using a bidirectional gRPC protocol
on IP address `127.0.0.1`. Your proxy server should be configured **NOT** to proxy
these local network connections. Add both `127.0.0.1` and `localhost` to the exclusion list of your proxy server.

### Ingress .status.loadBalancer field was not updated with a hostname/IP address {#ingress-status-loadbalancer}

This error is often caused by a misconfigured ingress-controller not updating the `status.loadBalancer`
field once the Ingress resource is ready to route traffic.

In some cases, this may be fixed by running `pulumi refresh`.

#### Traefik

For the Traefik controller, verify that the `kubernetes.ingressEndpoint` config
is [set properly](https://docs.traefik.io/providers/kubernetes-ingress/). This option was
introduced in Traefik 1.7.0.

### Pulumi destroy fails {#pulumi-destroy-fails}

There are scenarios when `pulumi destroy` will fail to delete resources as expected. This is anticipated due to the nature of cloud provider dependencies, permissions, resources being in a state that prevents their deletion, or when a timeout is not long enough for the cloud provider to complete its operation. Review the output to identify which resources were not deleted and consider the following steps depending on the nature of the failure.

#### Check to see if a resource was deleted after all

Some resources take time to be removed. Common examples include CloudFront Lambda@Edge functions, which will fail to `destroy` but will eventually disappear without requiring further action. In these cases, you can wait and run `pulumi refresh` to see if the cloud provider was able to remove the resource.

#### Check dependencies

If the issue is due to dependencies, identify and delete the dependent external resources manually. This may involve navigating the cloud provider's console or using its CLI to pinpoint and resolve these dependencies.

#### Empty or adjust resources

Occasionally a resource cannot be deleted because it contains data or uses network interfaces or other dependencies managed outside the stack. Common examples include deleting VPCs with EINs attached elsewhere or deleting a security group when it is in use. You will need to evaluate the dependencies given the failure and take the necessary actions to resolve this on each provider resource.

#### Delete resources manually

For each resource that couldn't be deleted, use the cloud provider's console or CLI to manually delete it. This may be necessary for resources in a locked state or those with specific permissions preventing automated deletion.

Once you have resolved the source of the deletion failure, you can run `pulumi refresh` to validate that all of your resources are destroyed. This command will update your Pulumi state to reflect the current state in the cloud, effectively recognizing any manual deletions or changes that occurred outside of Pulumi's management.

## Recovering from an interrupted update {#interrupted-update-recovery}

If the Pulumi CLI is interrupted when performing a deployment, you may see a warning message
that looks something like this on your next update:

```bash
$ pulumi up
...
Diagnostics:
  pulumi:pulumi:Stack (proj):
    warning: Attempting to deploy or update resources with 1 pending operations from previous deployment.
      * urn:pulumi:dev::proj::aws:s3/bucket:Bucket::bucket, interrupted while creating
    These resources are in an unknown state because the Pulumi CLI was interrupted while waiting for changes to these resources
    to complete. You should confirm whether or not the operations listed completed successfully by checking the state of the
    appropriate provider. For example, if you are using AWS, you can confirm using the AWS Console.

    Once you have confirmed the status of the interrupted operations, you can repair your stack using `pulumi refresh` which will refresh the state from the provider you are using and clear the pending operations if there are any.

    Note that `pulumi refresh` will need to be run interactively to clear pending CREATE operations.
...
```

This occurs when the Pulumi CLI fails to complete cleanly. There are a number of ways this
can happen:

- The CLI experiences a network partition when attempting to save your stack's state.
- The CLI process is killed by your operating system while performing an update.
- The CLI crashes when performing an update.

This error means that the Pulumi engine initiated an operation but was not able to determine if the operation completed successfully. As a result, resources may have been created that Pulumi does not know about.

To fix this condition, you should first cancel the update:

```bash
$ pulumi cancel
...
The currently running update for 'interruptedstack' has been canceled!
```

If `pulumi cancel` fails with `error: [400] Bad Request: the update has already completed`, you can safely ignore
that error and continue with the next step.

Then run `pulumi refresh` to remove any pending operations cleanly, allowing you to
resolve any pending operations that Pulumi could not fix unaided.

At this point your stack should be valid, up-to-date, and ready to accept future updates.

## Manually editing your deployment {#editing-your-deployment}

Sometimes the only recourse for fixing a stack that is unable to complete deployments is to edit the
deployment directly. We would love to hear about the issues you are experiencing
that you can't resolve, both so we can assist you in fixing your stack and also to fix the issues in Pulumi
that made it impossible for you to recover your stack in any other way.

The Pulumi engine uses both your program and your stack's existing state to make decisions about what
resources to create, read, update, or delete. The most common problem that makes it impossible to
make changes to your stack is that the stack's state has been corrupted in some way. There
are a variety of ways that a stack's state could be corrupted, but in almost all cases it is possible
to manually edit the stack's state to fix the issue.

This is an advanced operation and should be an absolute last resort. We recommend you check in with the [Pulumi Community Slack](https://slack.pulumi.com) first before editing your snapshot.

If you intend to unprotect or delete a resource, consider using the [`pulumi state`](/docs/cli/commands/pulumi_state) command instead of editing your state directly. `pulumi state` makes fixes to your state without
requiring you to edit the JSON representation of your stack's current state.

To get a JSON representation of your stack's current state, export your current stack
to a file:

```bash
$ pulumi stack export --file state.json
```

This file contains a lot of information. At the top level, this JSON object has two fields:

| Field | Description |
| - | - |
| `version` | The version of the file format. This should not be changed. |
| `deployment` | The last deployment state of the stack. |

The `deployment` object itself has three fields:

| Field | Description |
| - | - |
| `manifest` | Metadata about the previous deployment. This should not be changed. |
| `pending_operations` | List of the operations that the Pulumi engine started but has not finished. |
| `resources` | List of resources that Pulumi knows about. |

The possible fields of a resource are:

| Field |  Description |
| - | - |
| `urn` | The resource URN, which is a Pulumi-specific universal resource identifier. |
| `custom` | A boolean indicating whether or not this resource is a `custom` resource, which means that it uses a resource provider to operate. Component resources are not `custom`. |
| `delete` | A boolean indicating whether or not this resource is pending deletion. |
| `id` | This resource's ID, which is a provider-specific resource identifier. This often corresponds to a cloud provider's identifier for a resource. |
| `type` | The Pulumi type of this resource. |
| `inputs` | A map of inputs for this resource. Inputs are the set of key-value pairs used as an input to a resource provider. |
| `outputs` | A map of outputs for this resource. Outputs are the set of key-value pairs that were given to Pulumi by a resource provider after a resource has been provisioned. |
| `parent` | A URN for this resource's parent resource. |
| `protect` |  A boolean indicating whether or not this resource is protected. Protected resources can not be deleted. |
| `external` | A boolean indicating whether or not this resource is external to Pulumi. If a resource is external, Pulumi does not own its life cycle and it will not ever delete or update the resource. Resources that are read using the `get` function are external. |
| `dependencies` | A list of URNs indicating the resources that this resource depends on. Pulumi tracks dependencies between resources. It is important that this list be the full list of resources upon which this resource depends. |
| `initErrors` | A list of errors that occurred that prevented the resource from initializing. Some resource providers (most notably Kubernetes) populate this field to indicate that a resource was created but failed to initialize. |
| `provider` | Reference to the provider responsible for the resource. |

The `resources` field is a list, not a set. The order of resources in the list is important and is enforced by
the Pulumi engine. Resources in a deployment must be in *dependency order* - if resource A depends on resource B,
resource A *must* appear after resource B in the list.

Import your changes by running:

```bash
$ pulumi stack import --file state.json
```
