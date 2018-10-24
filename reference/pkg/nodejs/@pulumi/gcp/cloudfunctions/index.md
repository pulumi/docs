---
title: Module cloudfunctions
---

<a href="../index.html">@pulumi/gcp</a> &gt; cloudfunctions

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Function">class Function</a>
* <a href="#getFunction">function getFunction</a>
* <a href="#FunctionArgs">interface FunctionArgs</a>
* <a href="#FunctionState">interface FunctionState</a>
* <a href="#GetFunctionArgs">interface GetFunctionArgs</a>
* <a href="#GetFunctionResult">interface GetFunctionResult</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts">cloudfunctions/function.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts">cloudfunctions/getFunction.ts</a> 


<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L13">class Function</a>
</h2>

Creates a new Cloud Function. For more information see
[the official documentation](https://cloud.google.com/functions/docs/)
and
[API](https://cloud.google.com/functions/docs/apis).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L96">constructor</a>
</h3>

```typescript
new Function(name: string, args: FunctionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Function resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FunctionState): Function
```


Get an existing Function resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L29">property availableMemoryMb</a>
</h3>

```typescript
public availableMemoryMb: pulumi.Output<number | undefined>;
```


Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L37">property entryPoint</a>
</h3>

```typescript
public entryPoint: pulumi.Output<string | undefined>;
```


Name of a JavaScript function that will be executed when the Google Cloud Function is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L41">property environmentVariables</a>
</h3>

```typescript
public environmentVariables: pulumi.Output<{ ... } | undefined>;
```


A set of key/value environment variable pairs to assign to the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L45">property eventTrigger</a>
</h3>

```typescript
public eventTrigger: pulumi.Output<{ ... }>;
```


A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L49">property httpsTriggerUrl</a>
</h3>

```typescript
public httpsTriggerUrl: pulumi.Output<string>;
```


URL which triggers function execution. Returned only if `trigger_http` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L53">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A set of key/value label pairs to assign to the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L57">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A user-defined name of the function. Function names must be unique globally.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L61">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


Project of the function. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L65">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L70">property retryOnFailure</a>
</h3>

```typescript
public retryOnFailure: pulumi.Output<boolean>;
```


Whether the function should be retried on failure. This only applies to bucket and topic triggers, not HTTPS triggers.
Deprecated. Use `event_trigger.failure_policy.retry` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L74">property sourceArchiveBucket</a>
</h3>

```typescript
public sourceArchiveBucket: pulumi.Output<string>;
```


The GCS bucket containing the zip archive which contains the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L78">property sourceArchiveObject</a>
</h3>

```typescript
public sourceArchiveObject: pulumi.Output<string>;
```


The source archive object (file) in archive bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L82">property timeout</a>
</h3>

```typescript
public timeout: pulumi.Output<number | undefined>;
```


Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L87">property triggerBucket</a>
</h3>

```typescript
public triggerBucket: pulumi.Output<string>;
```


Google Cloud Storage bucket name. Every change in files in this bucket will trigger function execution. Cannot be used with `trigger_http` and `trigger_topic`.
Deprecated. Use `event_trigger` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L91">property triggerHttp</a>
</h3>

```typescript
public triggerHttp: pulumi.Output<boolean | undefined>;
```


Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L96">property triggerTopic</a>
</h3>

```typescript
public triggerTopic: pulumi.Output<string>;
```


Name of Pub/Sub topic. Every message published in this topic will trigger function execution with message contents passed as input data. Cannot be used with `trigger_http` and `trigger_bucket`.
Deprecated. Use `event_trigger` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L12">function getFunction</a>
</h2>

```typescript
getFunction(args: GetFunctionArgs, opts?: pulumi.InvokeOptions): Promise<GetFunctionResult>
```


Get information about a Google Cloud Function. For more information see
the [official documentation](https://cloud.google.com/functions/docs/)
and [API](https://cloud.google.com/functions/docs/apis).

<h2 class="pdoc-module-header" id="FunctionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L237">interface FunctionArgs</a>
</h2>

The set of arguments for constructing a Function resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L241">property availableMemoryMb</a>
</h3>

```typescript
availableMemoryMb?: pulumi.Input<number>;
```


Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L245">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L249">property entryPoint</a>
</h3>

```typescript
entryPoint?: pulumi.Input<string>;
```


Name of a JavaScript function that will be executed when the Google Cloud Function is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L253">property environmentVariables</a>
</h3>

```typescript
environmentVariables?: pulumi.Input<{ ... }>;
```


A set of key/value environment variable pairs to assign to the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L257">property eventTrigger</a>
</h3>

```typescript
eventTrigger?: pulumi.Input<{ ... }>;
```


A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L261">property httpsTriggerUrl</a>
</h3>

```typescript
httpsTriggerUrl?: pulumi.Input<string>;
```


URL which triggers function execution. Returned only if `trigger_http` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L265">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L269">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-defined name of the function. Function names must be unique globally.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L273">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


Project of the function. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L277">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L282">property retryOnFailure</a>
</h3>

```typescript
retryOnFailure?: pulumi.Input<boolean>;
```


Whether the function should be retried on failure. This only applies to bucket and topic triggers, not HTTPS triggers.
Deprecated. Use `event_trigger.failure_policy.retry` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L286">property sourceArchiveBucket</a>
</h3>

```typescript
sourceArchiveBucket: pulumi.Input<string>;
```


The GCS bucket containing the zip archive which contains the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L290">property sourceArchiveObject</a>
</h3>

```typescript
sourceArchiveObject: pulumi.Input<string>;
```


The source archive object (file) in archive bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L294">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L299">property triggerBucket</a>
</h3>

```typescript
triggerBucket?: pulumi.Input<string>;
```


Google Cloud Storage bucket name. Every change in files in this bucket will trigger function execution. Cannot be used with `trigger_http` and `trigger_topic`.
Deprecated. Use `event_trigger` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L303">property triggerHttp</a>
</h3>

```typescript
triggerHttp?: pulumi.Input<boolean>;
```


Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L308">property triggerTopic</a>
</h3>

```typescript
triggerTopic?: pulumi.Input<string>;
```


Name of Pub/Sub topic. Every message published in this topic will trigger function execution with message contents passed as input data. Cannot be used with `trigger_http` and `trigger_bucket`.
Deprecated. Use `event_trigger` instead.

<h2 class="pdoc-module-header" id="FunctionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L160">interface FunctionState</a>
</h2>

Input properties used for looking up and filtering Function resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L164">property availableMemoryMb</a>
</h3>

```typescript
availableMemoryMb?: pulumi.Input<number>;
```


Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L168">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L172">property entryPoint</a>
</h3>

```typescript
entryPoint?: pulumi.Input<string>;
```


Name of a JavaScript function that will be executed when the Google Cloud Function is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L176">property environmentVariables</a>
</h3>

```typescript
environmentVariables?: pulumi.Input<{ ... }>;
```


A set of key/value environment variable pairs to assign to the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L180">property eventTrigger</a>
</h3>

```typescript
eventTrigger?: pulumi.Input<{ ... }>;
```


A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L184">property httpsTriggerUrl</a>
</h3>

```typescript
httpsTriggerUrl?: pulumi.Input<string>;
```


URL which triggers function execution. Returned only if `trigger_http` is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L188">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L192">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A user-defined name of the function. Function names must be unique globally.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L196">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


Project of the function. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L200">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L205">property retryOnFailure</a>
</h3>

```typescript
retryOnFailure?: pulumi.Input<boolean>;
```


Whether the function should be retried on failure. This only applies to bucket and topic triggers, not HTTPS triggers.
Deprecated. Use `event_trigger.failure_policy.retry` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L209">property sourceArchiveBucket</a>
</h3>

```typescript
sourceArchiveBucket?: pulumi.Input<string>;
```


The GCS bucket containing the zip archive which contains the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L213">property sourceArchiveObject</a>
</h3>

```typescript
sourceArchiveObject?: pulumi.Input<string>;
```


The source archive object (file) in archive bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L217">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L222">property triggerBucket</a>
</h3>

```typescript
triggerBucket?: pulumi.Input<string>;
```


Google Cloud Storage bucket name. Every change in files in this bucket will trigger function execution. Cannot be used with `trigger_http` and `trigger_topic`.
Deprecated. Use `event_trigger` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L226">property triggerHttp</a>
</h3>

```typescript
triggerHttp?: pulumi.Input<boolean>;
```


Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/function.ts#L231">property triggerTopic</a>
</h3>

```typescript
triggerTopic?: pulumi.Input<string>;
```


Name of Pub/Sub topic. Every message published in this topic will trigger function execution with message contents passed as input data. Cannot be used with `trigger_http` and `trigger_bucket`.
Deprecated. Use `event_trigger` instead.

<h2 class="pdoc-module-header" id="GetFunctionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L23">interface GetFunctionArgs</a>
</h2>

A collection of arguments for invoking getFunction.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L27">property name</a>
</h3>

```typescript
name: string;
```


The name of a Cloud Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L32">property project</a>
</h3>

```typescript
project?: string;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L37">property region</a>
</h3>

```typescript
region?: string;
```


The region in which the resource belongs. If it
is not provided, the provider region is used.

<h2 class="pdoc-module-header" id="GetFunctionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L43">interface GetFunctionResult</a>
</h2>

A collection of values returned by getFunction.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L47">property availableMemoryMb</a>
</h3>

```typescript
availableMemoryMb: number;
```


Available memory (in MB) to the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L51">property description</a>
</h3>

```typescript
description: string;
```


Description of the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L55">property entryPoint</a>
</h3>

```typescript
entryPoint: string;
```


Name of a JavaScript function that will be executed when the Google Cloud Function is triggered.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L56">property environmentVariables</a>
</h3>

```typescript
environmentVariables: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L60">property eventTriggers</a>
</h3>

```typescript
eventTriggers: { ... }[];
```


A source that fires events in response to a condition in another service. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L64">property httpsTriggerUrl</a>
</h3>

```typescript
httpsTriggerUrl: string;
```


If function is triggered by HTTP, trigger URL is set here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L97">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L68">property labels</a>
</h3>

```typescript
labels: { ... };
```


A map of labels applied to this function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L69">property retryOnFailure</a>
</h3>

```typescript
retryOnFailure: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L73">property sourceArchiveBucket</a>
</h3>

```typescript
sourceArchiveBucket: string;
```


The GCS bucket containing the zip archive which contains the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L77">property sourceArchiveObject</a>
</h3>

```typescript
sourceArchiveObject: string;
```


The source archive object (file) in archive bucket.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L81">property timeout</a>
</h3>

```typescript
timeout: number;
```


Function execution timeout (in seconds).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L85">property triggerBucket</a>
</h3>

```typescript
triggerBucket: string;
```


If function is triggered by bucket, bucket name is set here. Deprecated. Use `event_trigger` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L89">property triggerHttp</a>
</h3>

```typescript
triggerHttp: boolean;
```


If function is triggered by HTTP, this boolean is set.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/cloudfunctions/getFunction.ts#L93">property triggerTopic</a>
</h3>

```typescript
triggerTopic: string;
```


If function is triggered by Pub/Sub topic, name of topic is set here. Deprecated. Use `event_trigger` instead.

