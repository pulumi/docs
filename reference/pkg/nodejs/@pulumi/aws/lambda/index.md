---
title: Module lambda
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Alias">class Alias</a>
* <a href="#EventSourceMapping">class EventSourceMapping</a>
* <a href="#Function">class Function</a>
* <a href="#Permission">class Permission</a>
* <a href="#AliasArgs">interface AliasArgs</a>
* <a href="#AliasState">interface AliasState</a>
* <a href="#EventSourceMappingArgs">interface EventSourceMappingArgs</a>
* <a href="#EventSourceMappingState">interface EventSourceMappingState</a>
* <a href="#FunctionArgs">interface FunctionArgs</a>
* <a href="#FunctionState">interface FunctionState</a>
* <a href="#PermissionArgs">interface PermissionArgs</a>
* <a href="#PermissionState">interface PermissionState</a>
* <a href="#DotnetCore1d0Runtime">let DotnetCore1d0Runtime</a>
* <a href="#DotnetCore2d0Runtime">let DotnetCore2d0Runtime</a>
* <a href="#Go1dxRuntime">let Go1dxRuntime</a>
* <a href="#Java8Runtime">let Java8Runtime</a>
* <a href="#NodeJS4d3EdgeRuntime">let NodeJS4d3EdgeRuntime</a>
* <a href="#NodeJS4d3Runtime">let NodeJS4d3Runtime</a>
* <a href="#NodeJS6d10Runtime">let NodeJS6d10Runtime</a>
* <a href="#NodeJS8d10Runtime">let NodeJS8d10Runtime</a>
* <a href="#NodeJSRuntime">let NodeJSRuntime</a>
* <a href="#Python2d7Runtime">let Python2d7Runtime</a>
* <a href="#Python3d6Runtime">let Python3d6Runtime</a>
* <a href="#Runtime">type Runtime</a>

<a href="/lambda/alias.ts">lambda/alias.ts</a> <a href="/lambda/eventSourceMapping.ts">lambda/eventSourceMapping.ts</a> <a href="/lambda/function.ts">lambda/function.ts</a> <a href="/lambda/permission.ts">lambda/permission.ts</a> <a href="/lambda/runtimes.ts">lambda/runtimes.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Alias">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L12">class Alias</a>
</h2>

Creates a Lambda function alias. Creates an alias that points to the specified Lambda function version.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about function aliases, see [CreateAlias][2] in the API docs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L44">constructor</a>
</h3>

```typescript
new Alias(name: string, args: AliasArgs, opts?: pulumi.ResourceOptions)
```


Create a Alias resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Alias(name: string, state?: AliasState, opts?: pulumi.ResourceOptions)
```


Create a Alias resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AliasState): Alias
```


Get an existing Alias resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda function alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L32">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L36">property functionName</a>
</h3>

```typescript
public functionName: pulumi.Output<string>;
```


The function ARN of the Lambda function for which you want to create an alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L40">property functionVersion</a>
</h3>

```typescript
public functionVersion: pulumi.Output<string>;
```


Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]+)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name for the alias you are creating. Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EventSourceMapping">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L12">class EventSourceMapping</a>
</h2>

Provides a Lambda event source mapping. This allows Lambda functions to get events from Kinesis and DynamoDB.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about event source mappings, see [CreateEventSourceMapping][2] in the API docs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L68">constructor</a>
</h3>

```typescript
new EventSourceMapping(name: string, args: EventSourceMappingArgs, opts?: pulumi.ResourceOptions)
```


Create a EventSourceMapping resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new EventSourceMapping(name: string, state?: EventSourceMappingState, opts?: pulumi.ResourceOptions)
```


Create a EventSourceMapping resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventSourceMappingState): EventSourceMapping
```


Get an existing EventSourceMapping resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L28">property batchSize</a>
</h3>

```typescript
public batchSize: pulumi.Output<number | undefined>;
```


The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L32">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Determines if the mapping will be enabled on creation. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L36">property eventSourceArn</a>
</h3>

```typescript
public eventSourceArn: pulumi.Output<string>;
```


The event source ARN - can either be a Kinesis or DynamoDB stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L40">property functionArn</a>
</h3>

```typescript
public functionArn: pulumi.Output<string>;
```


The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from `function_name` above.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L44">property functionName</a>
</h3>

```typescript
public functionName: pulumi.Output<string>;
```


The name or the ARN of the Lambda function that will be subscribing to events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L48">property lastModified</a>
</h3>

```typescript
public lastModified: pulumi.Output<string>;
```


The date this resource was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L52">property lastProcessingResult</a>
</h3>

```typescript
public lastProcessingResult: pulumi.Output<string>;
```


The result of the last AWS Lambda invocation of your Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L56">property startingPosition</a>
</h3>

```typescript
public startingPosition: pulumi.Output<string>;
```


The position in the stream where AWS Lambda should start reading. Can be one of either `TRIM_HORIZON` or `LATEST`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L60">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The state of the event source mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L64">property stateTransitionReason</a>
</h3>

```typescript
public stateTransitionReason: pulumi.Output<string>;
```


The reason the event source mapping is in its current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L68">property uuid</a>
</h3>

```typescript
public uuid: pulumi.Output<string>;
```


The UUID of the created event source mapping.

<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L13">class Function</a>
</h2>

Provides a Lambda Function resource. Lambda allows you to trigger execution of code in response to events in AWS. The Lambda Function itself includes source code and runtime configuration.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L123">constructor</a>
</h3>

```typescript
new Function(name: string, args: FunctionArgs, opts?: pulumi.ResourceOptions)
```


Create a Function resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Function(name: string, state?: FunctionState, opts?: pulumi.ResourceOptions)
```


Create a Function resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FunctionState): Function
```


Get an existing Function resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L45">property code</a>
</h3>

```typescript
public code: pulumi.Output<pulumi.asset.Archive | undefined>;
```


The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L33">property deadLetterConfig</a>
</h3>

```typescript
public deadLetterConfig: pulumi.Output<{ ... } | undefined>;
```


Nested block to configure the function's *dead letter queue*. See details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of what your Lambda Function does.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L41">property environment</a>
</h3>

```typescript
public environment: pulumi.Output<{ ... } | undefined>;
```


The Lambda environment's configuration settings. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L53">property handler</a>
</h3>

```typescript
public handler: pulumi.Output<string>;
```


The function [entrypoint][3] in your code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L57">property invokeArn</a>
</h3>

```typescript
public invokeArn: pulumi.Output<string>;
```


The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws_api_gateway_integration`](/docs/providers/aws/r/api_gateway_integration.html)'s `uri`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L61">property kmsKeyArn</a>
</h3>

```typescript
public kmsKeyArn: pulumi.Output<string | undefined>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L65">property lastModified</a>
</h3>

```typescript
public lastModified: pulumi.Output<string>;
```


The date this resource was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L69">property memorySize</a>
</h3>

```typescript
public memorySize: pulumi.Output<number | undefined>;
```


Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L73">property publish</a>
</h3>

```typescript
public publish: pulumi.Output<boolean | undefined>;
```


Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L78">property qualifiedArn</a>
</h3>

```typescript
public qualifiedArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L82">property reservedConcurrentExecutions</a>
</h3>

```typescript
public reservedConcurrentExecutions: pulumi.Output<number | undefined>;
```


The amount of reserved concurrent executions for this lambda function. Defaults to Unreserved Concurrency Limits. See [Managing Concurrency][9]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L86">property role</a>
</h3>

```typescript
public role: pulumi.Output<ARN>;
```


IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L90">property runtime</a>
</h3>

```typescript
public runtime: pulumi.Output<string>;
```


See [Runtimes][6] for valid values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L94">property s3Bucket</a>
</h3>

```typescript
public s3Bucket: pulumi.Output<string | undefined>;
```


The S3 bucket location containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L98">property s3Key</a>
</h3>

```typescript
public s3Key: pulumi.Output<string | undefined>;
```


The S3 key of an object containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L102">property s3ObjectVersion</a>
</h3>

```typescript
public s3ObjectVersion: pulumi.Output<string | undefined>;
```


The object version containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L106">property sourceCodeHash</a>
</h3>

```typescript
public sourceCodeHash: pulumi.Output<string>;
```


Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${base64sha256(file("file.zip"))}`, where "file.zip" is the local filename of the lambda function source archive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L110">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L114">property timeout</a>
</h3>

```typescript
public timeout: pulumi.Output<number | undefined>;
```


The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L115">property tracingConfig</a>
</h3>

```typescript
public tracingConfig: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L119">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


Latest published version of your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L123">property vpcConfig</a>
</h3>

```typescript
public vpcConfig: pulumi.Output<{ ... } | undefined>;
```


Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]

<h2 class="pdoc-module-header" id="Permission">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L12">class Permission</a>
</h2>

Creates a Lambda permission to allow external sources invoking the Lambda function
(e.g. CloudWatch Event Rule, SNS or S3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L61">constructor</a>
</h3>

```typescript
new Permission(name: string, args: PermissionArgs, opts?: pulumi.ResourceOptions)
```


Create a Permission resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Permission(name: string, state?: PermissionState, opts?: pulumi.ResourceOptions)
```


Create a Permission resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PermissionState): Permission
```


Get an existing Permission resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L28">property action</a>
</h3>

```typescript
public action: pulumi.Output<string>;
```


The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L32">property function</a>
</h3>

```typescript
public function: pulumi.Output<Function>;
```


Name of the Lambda function whose resource policy you are updating

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L38">property principal</a>
</h3>

```typescript
public principal: pulumi.Output<string>;
```


The principal who is getting this permission.
e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
such as `events.amazonaws.com` or `sns.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L44">property qualifier</a>
</h3>

```typescript
public qualifier: pulumi.Output<string | undefined>;
```


Query parameter to specify function version or alias name.
The permission will then apply to the specific qualified ARN.
e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L48">property sourceAccount</a>
</h3>

```typescript
public sourceAccount: pulumi.Output<string | undefined>;
```


This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L57">property sourceArn</a>
</h3>

```typescript
public sourceArn: pulumi.Output<string | undefined>;
```


When granting Amazon S3 or CloudWatch Events permission to
invoke your function, you should specify this field with the Amazon Resource Name (ARN)
for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
generated from the specified bucket or rule can invoke the function.
API Gateway ARNs have a unique structure described
[here](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L61">property statementId</a>
</h3>

```typescript
public statementId: pulumi.Output<string>;
```


A unique statement identifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AliasArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L112">interface AliasArgs</a>
</h2>

The set of arguments for constructing a Alias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L116">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L120">property functionName</a>
</h3>

```typescript
functionName: pulumi.Input<string>;
```


The function ARN of the Lambda function for which you want to create an alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L124">property functionVersion</a>
</h3>

```typescript
functionVersion: pulumi.Input<string>;
```


Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]+)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the alias you are creating. Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`

<h2 class="pdoc-module-header" id="AliasState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L86">interface AliasState</a>
</h2>

Input properties used for looking up and filtering Alias resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L90">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda function alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L94">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L98">property functionName</a>
</h3>

```typescript
functionName?: pulumi.Input<string>;
```


The function ARN of the Lambda function for which you want to create an alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L102">property functionVersion</a>
</h3>

```typescript
functionVersion?: pulumi.Input<string>;
```


Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]+)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/alias.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the alias you are creating. Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`

<h2 class="pdoc-module-header" id="EventSourceMappingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L175">interface EventSourceMappingArgs</a>
</h2>

The set of arguments for constructing a EventSourceMapping resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L179">property batchSize</a>
</h3>

```typescript
batchSize?: pulumi.Input<number>;
```


The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L183">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Determines if the mapping will be enabled on creation. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L187">property eventSourceArn</a>
</h3>

```typescript
eventSourceArn: pulumi.Input<string>;
```


The event source ARN - can either be a Kinesis or DynamoDB stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L191">property functionName</a>
</h3>

```typescript
functionName: pulumi.Input<string>;
```


The name or the ARN of the Lambda function that will be subscribing to events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L195">property startingPosition</a>
</h3>

```typescript
startingPosition: pulumi.Input<string>;
```


The position in the stream where AWS Lambda should start reading. Can be one of either `TRIM_HORIZON` or `LATEST`.

<h2 class="pdoc-module-header" id="EventSourceMappingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L125">interface EventSourceMappingState</a>
</h2>

Input properties used for looking up and filtering EventSourceMapping resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L129">property batchSize</a>
</h3>

```typescript
batchSize?: pulumi.Input<number>;
```


The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L133">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Determines if the mapping will be enabled on creation. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L137">property eventSourceArn</a>
</h3>

```typescript
eventSourceArn?: pulumi.Input<string>;
```


The event source ARN - can either be a Kinesis or DynamoDB stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L141">property functionArn</a>
</h3>

```typescript
functionArn?: pulumi.Input<string>;
```


The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from `function_name` above.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L145">property functionName</a>
</h3>

```typescript
functionName?: pulumi.Input<string>;
```


The name or the ARN of the Lambda function that will be subscribing to events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L149">property lastModified</a>
</h3>

```typescript
lastModified?: pulumi.Input<string>;
```


The date this resource was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L153">property lastProcessingResult</a>
</h3>

```typescript
lastProcessingResult?: pulumi.Input<string>;
```


The result of the last AWS Lambda invocation of your Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L157">property startingPosition</a>
</h3>

```typescript
startingPosition?: pulumi.Input<string>;
```


The position in the stream where AWS Lambda should start reading. Can be one of either `TRIM_HORIZON` or `LATEST`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L161">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The state of the event source mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L165">property stateTransitionReason</a>
</h3>

```typescript
stateTransitionReason?: pulumi.Input<string>;
```


The reason the event source mapping is in its current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/eventSourceMapping.ts#L169">property uuid</a>
</h3>

```typescript
uuid?: pulumi.Input<string>;
```


The UUID of the created event source mapping.

<h2 class="pdoc-module-header" id="FunctionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L312">interface FunctionArgs</a>
</h2>

The set of arguments for constructing a Function resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L328">property code</a>
</h3>

```typescript
code?: pulumi.asset.Archive;
```


The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L316">property deadLetterConfig</a>
</h3>

```typescript
deadLetterConfig?: pulumi.Input<{ ... }>;
```


Nested block to configure the function's *dead letter queue*. See details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L320">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of what your Lambda Function does.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L324">property environment</a>
</h3>

```typescript
environment?: pulumi.Input<{ ... }>;
```


The Lambda environment's configuration settings. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L336">property handler</a>
</h3>

```typescript
handler: pulumi.Input<string>;
```


The function [entrypoint][3] in your code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L340">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L344">property memorySize</a>
</h3>

```typescript
memorySize?: pulumi.Input<number>;
```


Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L332">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L348">property publish</a>
</h3>

```typescript
publish?: pulumi.Input<boolean>;
```


Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L352">property reservedConcurrentExecutions</a>
</h3>

```typescript
reservedConcurrentExecutions?: pulumi.Input<number>;
```


The amount of reserved concurrent executions for this lambda function. Defaults to Unreserved Concurrency Limits. See [Managing Concurrency][9]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L356">property role</a>
</h3>

```typescript
role: pulumi.Input<ARN>;
```


IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L360">property runtime</a>
</h3>

```typescript
runtime: pulumi.Input<string>;
```


See [Runtimes][6] for valid values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L364">property s3Bucket</a>
</h3>

```typescript
s3Bucket?: pulumi.Input<string>;
```


The S3 bucket location containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L368">property s3Key</a>
</h3>

```typescript
s3Key?: pulumi.Input<string>;
```


The S3 key of an object containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L372">property s3ObjectVersion</a>
</h3>

```typescript
s3ObjectVersion?: pulumi.Input<string>;
```


The object version containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L376">property sourceCodeHash</a>
</h3>

```typescript
sourceCodeHash?: pulumi.Input<string>;
```


Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${base64sha256(file("file.zip"))}`, where "file.zip" is the local filename of the lambda function source archive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L380">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L384">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L385">property tracingConfig</a>
</h3>

```typescript
tracingConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L389">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: pulumi.Input<{ ... }>;
```


Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]

<h2 class="pdoc-module-header" id="FunctionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L208">interface FunctionState</a>
</h2>

Input properties used for looking up and filtering Function resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L212">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L228">property code</a>
</h3>

```typescript
code?: pulumi.asset.Archive;
```


The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L216">property deadLetterConfig</a>
</h3>

```typescript
deadLetterConfig?: pulumi.Input<{ ... }>;
```


Nested block to configure the function's *dead letter queue*. See details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L220">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of what your Lambda Function does.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L224">property environment</a>
</h3>

```typescript
environment?: pulumi.Input<{ ... }>;
```


The Lambda environment's configuration settings. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L236">property handler</a>
</h3>

```typescript
handler?: pulumi.Input<string>;
```


The function [entrypoint][3] in your code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L240">property invokeArn</a>
</h3>

```typescript
invokeArn?: pulumi.Input<string>;
```


The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws_api_gateway_integration`](/docs/providers/aws/r/api_gateway_integration.html)'s `uri`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L244">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L248">property lastModified</a>
</h3>

```typescript
lastModified?: pulumi.Input<string>;
```


The date this resource was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L252">property memorySize</a>
</h3>

```typescript
memorySize?: pulumi.Input<number>;
```


Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L232">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L256">property publish</a>
</h3>

```typescript
publish?: pulumi.Input<boolean>;
```


Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L261">property qualifiedArn</a>
</h3>

```typescript
qualifiedArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L265">property reservedConcurrentExecutions</a>
</h3>

```typescript
reservedConcurrentExecutions?: pulumi.Input<number>;
```


The amount of reserved concurrent executions for this lambda function. Defaults to Unreserved Concurrency Limits. See [Managing Concurrency][9]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L269">property role</a>
</h3>

```typescript
role?: pulumi.Input<ARN>;
```


IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L273">property runtime</a>
</h3>

```typescript
runtime?: pulumi.Input<string>;
```


See [Runtimes][6] for valid values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L277">property s3Bucket</a>
</h3>

```typescript
s3Bucket?: pulumi.Input<string>;
```


The S3 bucket location containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L281">property s3Key</a>
</h3>

```typescript
s3Key?: pulumi.Input<string>;
```


The S3 key of an object containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L285">property s3ObjectVersion</a>
</h3>

```typescript
s3ObjectVersion?: pulumi.Input<string>;
```


The object version containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L289">property sourceCodeHash</a>
</h3>

```typescript
sourceCodeHash?: pulumi.Input<string>;
```


Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${base64sha256(file("file.zip"))}`, where "file.zip" is the local filename of the lambda function source archive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L293">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L297">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L298">property tracingConfig</a>
</h3>

```typescript
tracingConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L302">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Latest published version of your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/function.ts#L306">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: pulumi.Input<{ ... }>;
```


Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]

<h2 class="pdoc-module-header" id="PermissionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L153">interface PermissionArgs</a>
</h2>

The set of arguments for constructing a Permission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L157">property action</a>
</h3>

```typescript
action: pulumi.Input<string>;
```


The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L161">property function</a>
</h3>

```typescript
function: pulumi.Input<Function>;
```


Name of the Lambda function whose resource policy you are updating

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L167">property principal</a>
</h3>

```typescript
principal: pulumi.Input<string>;
```


The principal who is getting this permission.
e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
such as `events.amazonaws.com` or `sns.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L173">property qualifier</a>
</h3>

```typescript
qualifier?: pulumi.Input<string>;
```


Query parameter to specify function version or alias name.
The permission will then apply to the specific qualified ARN.
e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L177">property sourceAccount</a>
</h3>

```typescript
sourceAccount?: pulumi.Input<string>;
```


This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L186">property sourceArn</a>
</h3>

```typescript
sourceArn?: pulumi.Input<string>;
```


When granting Amazon S3 or CloudWatch Events permission to
invoke your function, you should specify this field with the Amazon Resource Name (ARN)
for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
generated from the specified bucket or rule can invoke the function.
API Gateway ARNs have a unique structure described
[here](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L190">property statementId</a>
</h3>

```typescript
statementId?: pulumi.Input<string>;
```


A unique statement identifier.

<h2 class="pdoc-module-header" id="PermissionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L110">interface PermissionState</a>
</h2>

Input properties used for looking up and filtering Permission resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L114">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L118">property function</a>
</h3>

```typescript
function?: pulumi.Input<Function>;
```


Name of the Lambda function whose resource policy you are updating

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L124">property principal</a>
</h3>

```typescript
principal?: pulumi.Input<string>;
```


The principal who is getting this permission.
e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
such as `events.amazonaws.com` or `sns.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L130">property qualifier</a>
</h3>

```typescript
qualifier?: pulumi.Input<string>;
```


Query parameter to specify function version or alias name.
The permission will then apply to the specific qualified ARN.
e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L134">property sourceAccount</a>
</h3>

```typescript
sourceAccount?: pulumi.Input<string>;
```


This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L143">property sourceArn</a>
</h3>

```typescript
sourceArn?: pulumi.Input<string>;
```


When granting Amazon S3 or CloudWatch Events permission to
invoke your function, you should specify this field with the Amazon Resource Name (ARN)
for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
generated from the specified bucket or rule can invoke the function.
API Gateway ARNs have a unique structure described
[here](http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/permission.ts#L147">property statementId</a>
</h3>

```typescript
statementId?: pulumi.Input<string>;
```


A unique statement identifier.

<h2 class="pdoc-module-header" id="DotnetCore1d0Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L31">let DotnetCore1d0Runtime</a>
</h2>

```typescript
let DotnetCore1d0Runtime: Runtime = "dotnetcore1.0";
```

<h2 class="pdoc-module-header" id="DotnetCore2d0Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L32">let DotnetCore2d0Runtime</a>
</h2>

```typescript
let DotnetCore2d0Runtime: Runtime = "dotnetcore2.0";
```

<h2 class="pdoc-module-header" id="Go1dxRuntime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L33">let Go1dxRuntime</a>
</h2>

```typescript
let Go1dxRuntime: Runtime = "go1.x";
```

<h2 class="pdoc-module-header" id="Java8Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L34">let Java8Runtime</a>
</h2>

```typescript
let Java8Runtime: Runtime = "java8";
```

<h2 class="pdoc-module-header" id="NodeJS4d3EdgeRuntime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L35">let NodeJS4d3EdgeRuntime</a>
</h2>

```typescript
let NodeJS4d3EdgeRuntime: Runtime = "nodejs4.3-edge";
```

<h2 class="pdoc-module-header" id="NodeJS4d3Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L36">let NodeJS4d3Runtime</a>
</h2>

```typescript
let NodeJS4d3Runtime: Runtime = "nodejs4.3";
```

<h2 class="pdoc-module-header" id="NodeJS6d10Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L37">let NodeJS6d10Runtime</a>
</h2>

```typescript
let NodeJS6d10Runtime: Runtime = "nodejs6.10";
```

<h2 class="pdoc-module-header" id="NodeJS8d10Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L38">let NodeJS8d10Runtime</a>
</h2>

```typescript
let NodeJS8d10Runtime: Runtime = "nodejs8.10";
```

<h2 class="pdoc-module-header" id="NodeJSRuntime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L39">let NodeJSRuntime</a>
</h2>

```typescript
let NodeJSRuntime: Runtime = "nodejs";
```

<h2 class="pdoc-module-header" id="Python2d7Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L40">let Python2d7Runtime</a>
</h2>

```typescript
let Python2d7Runtime: Runtime = "python2.7";
```

<h2 class="pdoc-module-header" id="Python3d6Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L41">let Python3d6Runtime</a>
</h2>

```typescript
let Python3d6Runtime: Runtime = "python3.6";
```

<h2 class="pdoc-module-header" id="Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/lambda/runtimes.ts#L18">type Runtime</a>
</h2>

```typescript
type Runtime = dotnetcore1.0 | dotnetcore2.0 | go1.x | java8 | nodejs4.3-edge | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs | python2.7 | python3.6;
```


Runtime is a union type containing all available AWS Lambda runtimes.

