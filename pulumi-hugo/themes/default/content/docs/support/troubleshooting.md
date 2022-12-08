---
title: Troubleshooting Guide
meta_desc: This guide covers common troubleshooting techniques when using Pulumi, such as tracing, manually editing deployments, and resolving common errors.
menu:
  support:
    weight: 1

aliases:
  - /docs/reference/troubleshooting/
  - /docs/troubleshooting/
---

Sometimes things go wrong. If you can't update your stack, or there's another problem that is
preventing you from being productive, you've come to the right place.

## Contact Us

[Join Community Slack](https://slack.pulumi.com), where our whole team, in addition to a passionate
community of users, are there to help. Any and all questions are welcome!

We also encourage everyone to contribute to the [Pulumi open source
projects](https://github.com/pulumi) by [opening new issues](https://github.com/pulumi/pulumi/issues/new) and upvoting existing issues.

Or email our support team: [support@pulumi.com](mailto:support@pulumi.com).

## Verbose Logging

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
$ pulumi up --logtostderr --logflow -v=9 2> out.txt
```

Diagnostic logging can also be controlled with flags and environment variables of the resource providers. For example, Pulumi providers that use a bridged Terraform provider can make use of the [`TF_LOG`](https://www.terraform.io/docs/internals/debugging.html) environment variable (set to `TRACE`, `DEBUG`, `INFO`, `WARN` or `ERROR`) in order to provide additional diagnostic information.

```bash
$ TF_LOG=TRACE pulumi up --logtostderr --logflow -v=9 2> out.txt
```

## Performance

If you are seeing unexpectedly slow performance, you can gather a trace to understand what
operations are being performed throughout the deployment and what the long poles are for your
deployment. In most cases, the most time consuming operations will be the provisioning of one or more resources in your cloud
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

## Common Problems

### 403 error fetching plugin

This error commonly occurs when using an ARM64-based processor while using an older version of a provider that does not support ARM64. It is not possible to upgrade the providers as your state file requires the version of the provider used at the time the resources were created.

The method for fixing this issue depends on whether you are using an Intel based processor:

#### Intel based processor

1. Open your Pulumi program on a non-arm64 based computer.
1. Update your packages (pip / nuget / npm / go) and run `pulumi up`.
1. Once the update is complete, open the new, updated Pulumi program on your arm64-based system.

#### Non-Intel based processor

1. Remove Pulumi - if you're using Homebrew, `brew remove pulumi` to remove Pulumi and `rm -rf ~/.pulumi` to remove plugins and templates.
1. Download [latest version of Pulumi](/docs/get-started/install/versions/).
1. Add Pulumi to path: `export PATH=$PATH:~/.pulumi/bin`
1. Update packages in your Pulumi program to latest version (for example `npm install @pulumi/aws@latest)
1. Install Pulumi provider: `arch -x86_64 pulumi plugin install resource {provider_name} v{version}` (where  {provider_name} is the name of the provider, i.e. aws and {version} is the same version number that your package has updated to). `arch` is used to run the selected architecture of a binary, in this case so that you can run the non-ARM64 version of Pulumi on your laptop.
1. [Login to Pulumi](/docs/intro/concepts/state#logging-into-and-out-of-state-backends).
1. Run a Pulumi preview: `arch -x86_64 pulumi pre`.
1. Remove Pulumi again `rm -rf ~/.pulumi`.
1. [Re-install Pulumi](/docs/get-started/install/)
1. [Login to Pulumi](/docs/intro/concepts/state#logging-into-and-out-of-state-backends).
1. Run a Pulumi preview to check everything is ok: `pulumi pre`

### 409 Conflict: Another update is currently in progress. {#conflict}

Run `pulumi cancel` to cancel the update.

{{% notes type="warning" %}}
Warning! If you cancel another person's update, their update will fail immediately.
{{% /notes %}}

One of the services that the [Pulumi Service](/docs/intro/pulumi-service/) provides is *concurrency control*.
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

### 500 Internal Server Error {#internal-server-error}

The Pulumi CLI interacts with the Pulumi web service throughout the course of an update. If the
service is unable to process an update, it is possible that users of the CLI may see this error message
throughout the course of an update.

We take great pride in service uptime and work rapidly to fix service interruption. The [Pulumi status page](https://status.pulumi.com) communicates information about service incidents.

### post-step event returned an error {#post-step-event}

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

### Error: could not load plugin for provider

You may encounter an error when you downgrade provider versions _after_ your stack is already updated with a newer version.
If you must downgrade the version of a provider your `pulumi` program depends on, you will need to [manually edit your deployment](#editing-your-deployment)
and change the version of the provider your stack depends on and then import that as the latest state of your stack.

The `pulumi` program that you author for your infrastructure may contain one or more dependencies to `providers`.
The version information for these providers is stored in the deployment for each of your stacks (since each pulumi program belongs to a stack).
This error can occur when the deployment state for a stack already contains a newer version of a specific provider, but you are trying
to run a `pulumi up` (or `preview`) command after downgrading the provider dependency in your pulumi program.

This error occurs because the `pulumi` [plugin cache](/docs/reference/cli/pulumi_plugin_ls/) does not have the required version installed.
This is more likely to occur if you are running `pulumi` in a CI/CD environment, since your plugin cache is likely not saved across builds.

It is okay to have multiple versions of a provider installed and have stacks depend on different provider version. It is only a problem when you
downgrade the version of a particular stack that was already deployed using a newer version.

Full error example:

```
error: could not load plugin for aws provider 'urn:pulumi:<stack_name>::pulumi-service::pulumi:providers:aws::default': no resource plugin 'aws-v0.16.2' found in the workspace or on your $PATH, install the plugin using \`pulumi plugin install resource aws v0.16.2\`
```

### Cannot connect to the Pulumi Service

If your network blocks external traffic and you're using the Pulumi Service to manage your state, your security team may need the following details to allow the Pulumi CLI to connect to the Service:

- The URL that the Pulumi CLI uses to connect to the Service is `https://api.pulumi.com`. (It does not use `https://app.pulumi.com`, so if you want to view the console from a web browser, you'll need enable that as well.)
- All access goes over HTTPS via port 443.

### Nothing happens due to network proxy

You run Pulumi and nothing happens, with output resembling this:

```
$ pulumi up
Previewing update (<stack name>):

Resources:

$
```

If you have a system-wide proxy server running on your machine, it may be misconfigured. The [Pulumi architecture](https://www.pulumi.com/docs/intro/concepts/how-pulumi-works/) has three different components, running as separate processes which talk to each other using a bidirectional gRPC protocol
on IP address `127.0.0.1`. Your proxy server should be configured **NOT** to proxy
these local network connections. Add both `127.0.0.1` and `localhost` to the exclusion list of your proxy server.

### Ingress .status.loadBalancer field was not updated with a hostname/IP address {#ingress-status-loadbalancer}

This error is often caused by a misconfigured ingress-controller not updating the `status.loadBalancer`
field once the Ingress resource is ready to route traffic.

In some cases this may be fixed by running `pulumi refresh`.

#### *Traefik*

For the Traefik controller, verify that the `kubernetes.ingressEndpoint` config
is [set properly](https://docs.traefik.io/providers/kubernetes-ingress/). This option was
introduced in Traefik 1.7.0.

### Synchronous call made to "X" with an unregistered provider {#synchronous-call}

Asynchronous calls are the default in `@pulumi/pulumi>=2.0.0` and the below only applies to programs using the `1.x` SDK.

The warning occurs when invoking a resource function synchronously while also using an
[explicit provider object](/docs/intro/concepts/resources#providers) that isn't yet ready to use.

For example:

```ts
const provider = new aws.Provider(...);

// A call to some provider's `getXXX` data source function.
const ids = aws.ec2.getSubnetIds(..., { provider });

// or

const parent = new SomeResource("name", { provider });
const ids = aws.ec2.getSubnetIds(..., { parent });
```

This warning may be benign. However, if you are experiencing crashes or hangs in Pulumi (especially in Node.js version 12.11.0 and above) and you see this warning, then it is likely that the older version of Pulumi is the issue.

The root cause of this problem pertains to undefined behavior in the Node.js runtime,
It is recommended that Pulumi apps be updated to prevent breakage.

To address the issue update your app to use one of the following forms:

#### Globally opt out of synchronous calls

Set the following config variable for your application:

```bash
pulumi config set pulumi:noSyncCalls true
```

```ts
const ids = pulumi.output(aws.ec2.getSubnetIds(..., { provider })); // or
const ids = pulumi.output(aws.ec2.getSubnetIds(..., { parent }));
```

This is the preferred way to solve this issue. In this form all resource function calls will always execute asynchronously,
returning their result through a `Promise<...>`. The result of the call is then wrapped into an `Output` so it can easily be
passed as a resource input and to make it [simple to access properties](/docs/intro/concepts/inputs-outputs#lifting) off of it.

#### Invoke the resource function asynchronously

Use this method to update only specific problematic calls to be asynchronous.

```ts
const ids = pulumi.output(aws.ec2.getSubnetIds(..., { provider, async: true })); // or
const ids = pulumi.output(aws.ec2.getSubnetIds(..., { parent, async: true }));
```

In this form, the `async: true` flag is passed in which forces `getSubnetIds` to always execute asynchronously.  The result
of the call is then wrapped into an `Output` so it can easily be passed as a resource input and to make it
[simple to access properties](/docs/intro/concepts/inputs-outputs#lifting) off of it.

#### Register the provider first

If the problem exists in a layer deeper (e.g, a component not under your control), use this solution.

```ts
const provider = new aws.Provider(...);
await ProviderResource.register(provider);

// later on

const ids = aws.ec2.getSubnetIds(..., { provider }); // or
const ids = aws.ec2.getSubnetIds(..., { parent });
```

In this form, the ProviderResource is explicitly registered first, allowing it to be safely used *synchronously* in the resource
function calls. This registration should generally be done immediately after creating the provider. With this form the resource function
results can be used immediately, without needing to operate on them as promises (i.e. no need for `await` or `.then(...)`).

This approach makes it possible to safely perform these resource function calls synchronously.  However, it may require refactoring
some code due to the need to potentially use `async`/`await` code in areas of a program that are currently synchronous.

### StackReference.getOutputSync/requireOutputSync called on a StackReference whose name is a Promise/Output {#stackreference-sync}

`getOutputSync` and `requireOutputSync` are not available in `@pulumi/pulumi>=2.0.0` and the below only applies to programs using the `1.x` SDK.

The warning occurs when calling `getOutputSync` or `requireOutputSync` on a `StackReference` whose name is not a simple string.
For example:

```ts
const stackReference = new StackReference("...", { name: otherResource.outputValue });
const val = stackReference.getOutputSync("outputName");
```

This warning may be benign. However, if you are experiencing crashes or hangs in Pulumi (especially in Node.js version 12.11.0 and above) and you see this warning, then it is likely that the older version of Pulumi is the issue.

A warning is issued so as to not break existing code that is functionality properly. However, the root cause of this problem
pertains to undefined behavior in the Node.js runtime, so apparently-working code today may begin crashing or hanging in the future. We recommend updating your code to ensure your Pulumi program works reliably.

There are only two ways supported to avoid this issue:

#### Use getOutput/requireOutput instead {#use-getoutput}

```ts
const stackReference = new StackReference("...", { name: otherResource.outputValue });
const val = stackReference.getOutput("outputName");
```

In this form the result of the call is an `Output` (which internally asynchronously retrieves the stack output value).  This can
easily be passed as a resource input and supports [simple to access properties](/docs/intro/concepts/inputs-outputs#lifting) off of it.

However, because the value is not known synchronously, it is not possible to have the value affect the flow of your application.
For example if the output value is an array, there is no way to know the length of the array in order to make specific resources
corresponding to it.  If the exact value is needed for this purpose the only way to get it is like so:

#### Pass the stack reference name in as a string

```ts
const stackReference = new StackReference("...", { name: "explicitly-provided-name" });
const values: string[] = stackReference.getOutput("outputName");
for (const e of values) {
   ...
```

This approach requires you to pass in the name as a string either explicitly as a literal like above, or just as some string
value defined elsewhere in your application. If the value is known, it can be copied into your application and used directly.

If the stack-reference-name truly is dynamic and cannot be known ahead of time to supply directly into the app, then this
approach will not work, and the only way to workaround the issue is to follow the steps in [Use getOutput/requireOutput](#use-getoutput).

## Recovering from an Interrupted Update {#interrupted-update-recovery}

If the Pulumi CLI is interrupted when performing a deployment, you may see a warning message
that looks something like this on your next update:

```bash
$ pulumi up
...
Diagnostics:
  pulumi:pulumi:Stack (proj):
    warning: Attempting to deploy or update resources with 1 pending operations from previous deployment.
      * urn:pulumi:dev::proj::aws:s3/bucketV2:BucketV2::bucket, interrupted while creating
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

## Manually Editing Your Deployment {#editing-your-deployment}

Sometimes the only recourse for fixing a stack that is unable to complete deployments is to edit the
deployment directly. We would love to hear about the issues you are experiencing
that you can't resolve, both so we can assist you in fixing your stack and also to fix the issues in Pulumi
that made it impossible for you to recover your stack in any other way.

The Pulumi engine uses both your program and your stack's existing state to make decisions about what
resources to create, read, update, or delete. The most common problem that makes it impossible to
make changes to your stack is that the stack's state has been corrupted in some way. There
are a variety of ways that a stack's state could be corrupted, but in almost all cases it is possible
to manually edit the stack's state to fix the issue.

This is an advanced operation and should be an absolute last resort. We recommend you check-in with the [Pulumi Community Slack](https://slack.pulumi.com) first before editing your snapshot.

If you intend to unprotect or delete a resource, consider using the [`pulumi state`](/docs/reference/cli/pulumi_state) command instead of editing your state directly. `pulumi state` makes fixes to your state without
requiring you to edit the JSON representation of your stack's current state.

To get a JSON representation of your stack's current state, export your current stack
to a file:

```bash
$ pulumi stack export --file state.json
```

This file contains a lot of information. At the top-level, this JSON object has two fields:

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
| `initErrors` | A list of errors that occured that prevented the resource from initializing. Some resource providers (most notably Kubernetes) populate this field to indicate that a resource was created but failed to initialize. |
| `provider` | Reference to the provider esponsible for the resource. |

The `resources` field is a list, not a set. The order of resources in the list is important and is enforced by
the Pulumi engine. Resources in a deployment must be in *dependency order* - if resource A depends on resource B,
resource A *must* appear after resource B in the list.

Import your changes by running:

```bash
$ pulumi stack import --file state.json
```
