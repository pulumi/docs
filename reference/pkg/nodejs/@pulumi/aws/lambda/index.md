---
title: Module lambda
---

<a href="../index.html">@pulumi/aws</a> &gt; lambda

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Alias">class Alias</a>
* <a href="#EventSourceMapping">class EventSourceMapping</a>
* <a href="#Function">class Function</a>
* <a href="#Permission">class Permission</a>
* <a href="#getFunction">function getFunction</a>
* <a href="#getInvocation">function getInvocation</a>
* <a href="#AliasArgs">interface AliasArgs</a>
* <a href="#AliasState">interface AliasState</a>
* <a href="#EventSourceMappingArgs">interface EventSourceMappingArgs</a>
* <a href="#EventSourceMappingState">interface EventSourceMappingState</a>
* <a href="#FunctionArgs">interface FunctionArgs</a>
* <a href="#FunctionState">interface FunctionState</a>
* <a href="#GetFunctionArgs">interface GetFunctionArgs</a>
* <a href="#GetFunctionResult">interface GetFunctionResult</a>
* <a href="#GetInvocationArgs">interface GetInvocationArgs</a>
* <a href="#GetInvocationResult">interface GetInvocationResult</a>
* <a href="#PermissionArgs">interface PermissionArgs</a>
* <a href="#PermissionState">interface PermissionState</a>
* <a href="#DotnetCore1d0Runtime">let DotnetCore1d0Runtime</a>
* <a href="#DotnetCore2d0Runtime">let DotnetCore2d0Runtime</a>
* <a href="#DotnetCore2d1Runtime">let DotnetCore2d1Runtime</a>
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

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts">lambda/alias.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts">lambda/eventSourceMapping.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts">lambda/function.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts">lambda/getFunction.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts">lambda/getInvocation.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts">lambda/permission.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts">lambda/runtimes.ts</a> 


<h2 class="pdoc-module-header" id="Alias">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L13">class Alias</a>
</h2>

Creates a Lambda function alias. Creates an alias that points to the specified Lambda function version.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about function aliases, see [CreateAlias][2] and [AliasRoutingConfiguration][3] in the API docs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L49">constructor</a>
</h3>

```typescript
new Alias(name: string, args: AliasArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Alias resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AliasState): Alias
```


Get an existing Alias resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L29">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda function alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L37">property functionName</a>
</h3>

```typescript
public functionName: pulumi.Output<string>;
```


The function ARN of the Lambda function for which you want to create an alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L41">property functionVersion</a>
</h3>

```typescript
public functionVersion: pulumi.Output<string>;
```


Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]+)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name for the alias you are creating. Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L49">property routingConfig</a>
</h3>

```typescript
public routingConfig: pulumi.Output<{ ... } | undefined>;
```


The Lambda alias' route configuration settings. Fields documented below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="EventSourceMapping">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L13">class EventSourceMapping</a>
</h2>

Provides a Lambda event source mapping. This allows Lambda functions to get events from Kinesis, DynamoDB and SQS

For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about event source mappings, see [CreateEventSourceMapping][2] in the API docs.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L69">constructor</a>
</h3>

```typescript
new EventSourceMapping(name: string, args: EventSourceMappingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a EventSourceMapping resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: EventSourceMappingState): EventSourceMapping
```


Get an existing EventSourceMapping resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L29">property batchSize</a>
</h3>

```typescript
public batchSize: pulumi.Output<number | undefined>;
```


The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100` for DynamoDB and Kinesis, `10` for SQS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L33">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Determines if the mapping will be enabled on creation. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L37">property eventSourceArn</a>
</h3>

```typescript
public eventSourceArn: pulumi.Output<string>;
```


The event source ARN - can either be a Kinesis or DynamoDB stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L41">property functionArn</a>
</h3>

```typescript
public functionArn: pulumi.Output<string>;
```


The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from `function_name` above.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L45">property functionName</a>
</h3>

```typescript
public functionName: pulumi.Output<string>;
```


The name or the ARN of the Lambda function that will be subscribing to events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L49">property lastModified</a>
</h3>

```typescript
public lastModified: pulumi.Output<string>;
```


The date this resource was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L53">property lastProcessingResult</a>
</h3>

```typescript
public lastProcessingResult: pulumi.Output<string>;
```


The result of the last AWS Lambda invocation of your Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L57">property startingPosition</a>
</h3>

```typescript
public startingPosition: pulumi.Output<string | undefined>;
```


The position in the stream where AWS Lambda should start reading. Must be one of either `TRIM_HORIZON` or `LATEST` if getting events from Kinesis or DynamoDB.  Must not be provided if getting events from SQS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L61">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The state of the event source mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L65">property stateTransitionReason</a>
</h3>

```typescript
public stateTransitionReason: pulumi.Output<string>;
```


The reason the event source mapping is in its current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L69">property uuid</a>
</h3>

```typescript
public uuid: pulumi.Output<string>;
```


The UUID of the created event source mapping.

<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L14">class Function</a>
</h2>

Provides a Lambda Function resource. Lambda allows you to trigger execution of code in response to events in AWS. The Lambda Function itself includes source code and runtime configuration.

For information about Lambda and how to use it, see [What is AWS Lambda?][1]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L128">constructor</a>
</h3>

```typescript
new Function(name: string, args: FunctionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Function resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FunctionState): Function
```


Get an existing Function resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L30">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L46">property code</a>
</h3>

```typescript
public code: pulumi.Output<pulumi.asset.Archive | undefined>;
```


The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L34">property deadLetterConfig</a>
</h3>

```typescript
public deadLetterConfig: pulumi.Output<{ ... } | undefined>;
```


Nested block to configure the function's *dead letter queue*. See details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L38">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of what your Lambda Function does.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L42">property environment</a>
</h3>

```typescript
public environment: pulumi.Output<{ ... } | undefined>;
```


The Lambda environment's configuration settings. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L54">property handler</a>
</h3>

```typescript
public handler: pulumi.Output<string>;
```


The function [entrypoint][3] in your code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L58">property invokeArn</a>
</h3>

```typescript
public invokeArn: pulumi.Output<string>;
```


The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws_api_gateway_integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L62">property kmsKeyArn</a>
</h3>

```typescript
public kmsKeyArn: pulumi.Output<string | undefined>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L66">property lastModified</a>
</h3>

```typescript
public lastModified: pulumi.Output<string>;
```


The date this resource was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L70">property memorySize</a>
</h3>

```typescript
public memorySize: pulumi.Output<number | undefined>;
```


Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L74">property publish</a>
</h3>

```typescript
public publish: pulumi.Output<boolean | undefined>;
```


Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L79">property qualifiedArn</a>
</h3>

```typescript
public qualifiedArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L83">property reservedConcurrentExecutions</a>
</h3>

```typescript
public reservedConcurrentExecutions: pulumi.Output<number | undefined>;
```


The amount of reserved concurrent executions for this lambda function. Defaults to Unreserved Concurrency Limits. See [Managing Concurrency][9]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L87">property role</a>
</h3>

```typescript
public role: pulumi.Output<ARN>;
```


IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L91">property runtime</a>
</h3>

```typescript
public runtime: pulumi.Output<string>;
```


See [Runtimes][6] for valid values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L95">property s3Bucket</a>
</h3>

```typescript
public s3Bucket: pulumi.Output<string | undefined>;
```


The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L99">property s3Key</a>
</h3>

```typescript
public s3Key: pulumi.Output<string | undefined>;
```


The S3 key of an object containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L103">property s3ObjectVersion</a>
</h3>

```typescript
public s3ObjectVersion: pulumi.Output<string | undefined>;
```


The object version containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L107">property sourceCodeHash</a>
</h3>

```typescript
public sourceCodeHash: pulumi.Output<string>;
```


Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${base64sha256(file("file.zip"))}`, where "file.zip" is the local filename of the lambda function source archive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L111">property sourceCodeSize</a>
</h3>

```typescript
public sourceCodeSize: pulumi.Output<number>;
```


The size in bytes of the function .zip file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L115">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<Tags | undefined>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L119">property timeout</a>
</h3>

```typescript
public timeout: pulumi.Output<number | undefined>;
```


The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L120">property tracingConfig</a>
</h3>

```typescript
public tracingConfig: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L124">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


Latest published version of your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L128">property vpcConfig</a>
</h3>

```typescript
public vpcConfig: pulumi.Output<{ ... } | undefined>;
```


Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]

<h2 class="pdoc-module-header" id="Permission">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L13">class Permission</a>
</h2>

Creates a Lambda permission to allow external sources invoking the Lambda function
(e.g. CloudWatch Event Rule, SNS or S3).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L70">constructor</a>
</h3>

```typescript
new Permission(name: string, args: PermissionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Permission resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PermissionState): Permission
```


Get an existing Permission resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L29">property action</a>
</h3>

```typescript
public action: pulumi.Output<string>;
```


The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L33">property eventSourceToken</a>
</h3>

```typescript
public eventSourceToken: pulumi.Output<string | undefined>;
```


The Event Source Token to validate.  Used with [Alexa Skills][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L37">property function</a>
</h3>

```typescript
public function: pulumi.Output<Function>;
```


Name of the Lambda function whose resource policy you are updating

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L43">property principal</a>
</h3>

```typescript
public principal: pulumi.Output<string>;
```


The principal who is getting this permission.
e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
such as `events.amazonaws.com` or `sns.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L49">property qualifier</a>
</h3>

```typescript
public qualifier: pulumi.Output<string | undefined>;
```


Query parameter to specify function version or alias name.
The permission will then apply to the specific qualified ARN.
e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L53">property sourceAccount</a>
</h3>

```typescript
public sourceAccount: pulumi.Output<string | undefined>;
```


This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L62">property sourceArn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L66">property statementId</a>
</h3>

```typescript
public statementId: pulumi.Output<string>;
```


A unique statement identifier. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L70">property statementIdPrefix</a>
</h3>

```typescript
public statementIdPrefix: pulumi.Output<string | undefined>;
```


A statement identifier prefix. Terraform will generate a unique suffix. Conflicts with `statement_id`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getFunction">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L10">function getFunction</a>
</h2>

```typescript
getFunction(args: GetFunctionArgs, opts?: pulumi.InvokeOptions): Promise<GetFunctionResult>
```


Provides information about a Lambda Function.

<h2 class="pdoc-module-header" id="getInvocation">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts#L12">function getInvocation</a>
</h2>

```typescript
getInvocation(args: GetInvocationArgs, opts?: pulumi.InvokeOptions): Promise<GetInvocationResult>
```


Use this data source to invoke custom lambda functions as data source.
The lambda function is invoked with [RequestResponse](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax)
invocation type.

<h2 class="pdoc-module-header" id="AliasArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L121">interface AliasArgs</a>
</h2>

The set of arguments for constructing a Alias resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L125">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L129">property functionName</a>
</h3>

```typescript
functionName: pulumi.Input<string>;
```


The function ARN of the Lambda function for which you want to create an alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L133">property functionVersion</a>
</h3>

```typescript
functionVersion: pulumi.Input<string>;
```


Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]+)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the alias you are creating. Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L141">property routingConfig</a>
</h3>

```typescript
routingConfig?: pulumi.Input<{ ... }>;
```


The Lambda alias' route configuration settings. Fields documented below

<h2 class="pdoc-module-header" id="AliasState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L91">interface AliasState</a>
</h2>

Input properties used for looking up and filtering Alias resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L95">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda function alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L103">property functionName</a>
</h3>

```typescript
functionName?: pulumi.Input<string>;
```


The function ARN of the Lambda function for which you want to create an alias.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L107">property functionVersion</a>
</h3>

```typescript
functionVersion?: pulumi.Input<string>;
```


Lambda function version for which you are creating the alias. Pattern: `(\$LATEST|[0-9]+)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name for the alias you are creating. Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_]+)`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/alias.ts#L115">property routingConfig</a>
</h3>

```typescript
routingConfig?: pulumi.Input<{ ... }>;
```


The Lambda alias' route configuration settings. Fields documented below

<h2 class="pdoc-module-header" id="EventSourceMappingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L171">interface EventSourceMappingArgs</a>
</h2>

The set of arguments for constructing a EventSourceMapping resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L175">property batchSize</a>
</h3>

```typescript
batchSize?: pulumi.Input<number>;
```


The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100` for DynamoDB and Kinesis, `10` for SQS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L179">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Determines if the mapping will be enabled on creation. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L183">property eventSourceArn</a>
</h3>

```typescript
eventSourceArn: pulumi.Input<string>;
```


The event source ARN - can either be a Kinesis or DynamoDB stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L187">property functionName</a>
</h3>

```typescript
functionName: pulumi.Input<string>;
```


The name or the ARN of the Lambda function that will be subscribing to events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L191">property startingPosition</a>
</h3>

```typescript
startingPosition?: pulumi.Input<string>;
```


The position in the stream where AWS Lambda should start reading. Must be one of either `TRIM_HORIZON` or `LATEST` if getting events from Kinesis or DynamoDB.  Must not be provided if getting events from SQS.

<h2 class="pdoc-module-header" id="EventSourceMappingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L121">interface EventSourceMappingState</a>
</h2>

Input properties used for looking up and filtering EventSourceMapping resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L125">property batchSize</a>
</h3>

```typescript
batchSize?: pulumi.Input<number>;
```


The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100` for DynamoDB and Kinesis, `10` for SQS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L129">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Determines if the mapping will be enabled on creation. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L133">property eventSourceArn</a>
</h3>

```typescript
eventSourceArn?: pulumi.Input<string>;
```


The event source ARN - can either be a Kinesis or DynamoDB stream.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L137">property functionArn</a>
</h3>

```typescript
functionArn?: pulumi.Input<string>;
```


The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from `function_name` above.)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L141">property functionName</a>
</h3>

```typescript
functionName?: pulumi.Input<string>;
```


The name or the ARN of the Lambda function that will be subscribing to events.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L145">property lastModified</a>
</h3>

```typescript
lastModified?: pulumi.Input<string>;
```


The date this resource was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L149">property lastProcessingResult</a>
</h3>

```typescript
lastProcessingResult?: pulumi.Input<string>;
```


The result of the last AWS Lambda invocation of your Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L153">property startingPosition</a>
</h3>

```typescript
startingPosition?: pulumi.Input<string>;
```


The position in the stream where AWS Lambda should start reading. Must be one of either `TRIM_HORIZON` or `LATEST` if getting events from Kinesis or DynamoDB.  Must not be provided if getting events from SQS.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L157">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The state of the event source mapping.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L161">property stateTransitionReason</a>
</h3>

```typescript
stateTransitionReason?: pulumi.Input<string>;
```


The reason the event source mapping is in its current state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/eventSourceMapping.ts#L165">property uuid</a>
</h3>

```typescript
uuid?: pulumi.Input<string>;
```


The UUID of the created event source mapping.

<h2 class="pdoc-module-header" id="FunctionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L321">interface FunctionArgs</a>
</h2>

The set of arguments for constructing a Function resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L337">property code</a>
</h3>

```typescript
code?: pulumi.Input<pulumi.asset.Archive>;
```


The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L325">property deadLetterConfig</a>
</h3>

```typescript
deadLetterConfig?: pulumi.Input<{ ... }>;
```


Nested block to configure the function's *dead letter queue*. See details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L329">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of what your Lambda Function does.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L333">property environment</a>
</h3>

```typescript
environment?: pulumi.Input<{ ... }>;
```


The Lambda environment's configuration settings. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L345">property handler</a>
</h3>

```typescript
handler: pulumi.Input<string>;
```


The function [entrypoint][3] in your code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L349">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L353">property memorySize</a>
</h3>

```typescript
memorySize?: pulumi.Input<number>;
```


Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L341">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L357">property publish</a>
</h3>

```typescript
publish?: pulumi.Input<boolean>;
```


Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L361">property reservedConcurrentExecutions</a>
</h3>

```typescript
reservedConcurrentExecutions?: pulumi.Input<number>;
```


The amount of reserved concurrent executions for this lambda function. Defaults to Unreserved Concurrency Limits. See [Managing Concurrency][9]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L365">property role</a>
</h3>

```typescript
role: pulumi.Input<ARN>;
```


IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L369">property runtime</a>
</h3>

```typescript
runtime: pulumi.Input<string>;
```


See [Runtimes][6] for valid values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L373">property s3Bucket</a>
</h3>

```typescript
s3Bucket?: pulumi.Input<string>;
```


The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L377">property s3Key</a>
</h3>

```typescript
s3Key?: pulumi.Input<string>;
```


The S3 key of an object containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L381">property s3ObjectVersion</a>
</h3>

```typescript
s3ObjectVersion?: pulumi.Input<string>;
```


The object version containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L385">property sourceCodeHash</a>
</h3>

```typescript
sourceCodeHash?: pulumi.Input<string>;
```


Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${base64sha256(file("file.zip"))}`, where "file.zip" is the local filename of the lambda function source archive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L389">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L393">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L394">property tracingConfig</a>
</h3>

```typescript
tracingConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L398">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: pulumi.Input<{ ... }>;
```


Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]

<h2 class="pdoc-module-header" id="FunctionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L213">interface FunctionState</a>
</h2>

Input properties used for looking up and filtering Function resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L217">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L233">property code</a>
</h3>

```typescript
code?: pulumi.Input<pulumi.asset.Archive>;
```


The path to the function's deployment package within the local filesystem. If defined, The `s3_`-prefixed options cannot be used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L221">property deadLetterConfig</a>
</h3>

```typescript
deadLetterConfig?: pulumi.Input<{ ... }>;
```


Nested block to configure the function's *dead letter queue*. See details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L225">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of what your Lambda Function does.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L229">property environment</a>
</h3>

```typescript
environment?: pulumi.Input<{ ... }>;
```


The Lambda environment's configuration settings. Fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L241">property handler</a>
</h3>

```typescript
handler?: pulumi.Input<string>;
```


The function [entrypoint][3] in your code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L245">property invokeArn</a>
</h3>

```typescript
invokeArn?: pulumi.Input<string>;
```


The ARN to be used for invoking Lambda Function from API Gateway - to be used in [`aws_api_gateway_integration`](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s `uri`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L249">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn?: pulumi.Input<string>;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L253">property lastModified</a>
</h3>

```typescript
lastModified?: pulumi.Input<string>;
```


The date this resource was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L257">property memorySize</a>
</h3>

```typescript
memorySize?: pulumi.Input<number>;
```


Amount of memory in MB your Lambda Function can use at runtime. Defaults to `128`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L237">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L261">property publish</a>
</h3>

```typescript
publish?: pulumi.Input<boolean>;
```


Whether to publish creation/change as new Lambda Function Version. Defaults to `false`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L266">property qualifiedArn</a>
</h3>

```typescript
qualifiedArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via `publish = true`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L270">property reservedConcurrentExecutions</a>
</h3>

```typescript
reservedConcurrentExecutions?: pulumi.Input<number>;
```


The amount of reserved concurrent executions for this lambda function. Defaults to Unreserved Concurrency Limits. See [Managing Concurrency][9]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L274">property role</a>
</h3>

```typescript
role?: pulumi.Input<ARN>;
```


IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L278">property runtime</a>
</h3>

```typescript
runtime?: pulumi.Input<string>;
```


See [Runtimes][6] for valid values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L282">property s3Bucket</a>
</h3>

```typescript
s3Bucket?: pulumi.Input<string>;
```


The S3 bucket location containing the function's deployment package. Conflicts with `filename`. This bucket must reside in the same AWS region where you are creating the Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L286">property s3Key</a>
</h3>

```typescript
s3Key?: pulumi.Input<string>;
```


The S3 key of an object containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L290">property s3ObjectVersion</a>
</h3>

```typescript
s3ObjectVersion?: pulumi.Input<string>;
```


The object version containing the function's deployment package. Conflicts with `filename`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L294">property sourceCodeHash</a>
</h3>

```typescript
sourceCodeHash?: pulumi.Input<string>;
```


Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either `filename` or `s3_key`. The usual way to set this is `${base64sha256(file("file.zip"))}`, where "file.zip" is the local filename of the lambda function source archive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L298">property sourceCodeSize</a>
</h3>

```typescript
sourceCodeSize?: pulumi.Input<number>;
```


The size in bytes of the function .zip file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L302">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<Tags>;
```


A mapping of tags to assign to the object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L306">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


The amount of time your Lambda Function has to run in seconds. Defaults to `3`. See [Limits][5]

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L307">property tracingConfig</a>
</h3>

```typescript
tracingConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L311">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


Latest published version of your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/function.ts#L315">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: pulumi.Input<{ ... }>;
```


Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]

<h2 class="pdoc-module-header" id="GetFunctionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L20">interface GetFunctionArgs</a>
</h2>

A collection of arguments for invoking getFunction.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L24">property functionName</a>
</h3>

```typescript
functionName: string;
```


Name of the lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L28">property qualifier</a>
</h3>

```typescript
qualifier?: string;
```


Qualifier of the lambda function. Defaults to `$LATEST`.

<h2 class="pdoc-module-header" id="GetFunctionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L34">interface GetFunctionResult</a>
</h2>

A collection of values returned by getFunction.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L38">property arn</a>
</h3>

```typescript
arn: string;
```


The Amazon Resource Name (ARN) identifying your Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L42">property deadLetterConfig</a>
</h3>

```typescript
deadLetterConfig: { ... };
```


Configure the function's *dead letter queue*.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L46">property description</a>
</h3>

```typescript
description: string;
```


Description of what your Lambda Function does.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L50">property environment</a>
</h3>

```typescript
environment: { ... };
```


The Lambda environment's configuration settings.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L54">property handler</a>
</h3>

```typescript
handler: string;
```


The function entrypoint in your code.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L114">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L58">property invokeArn</a>
</h3>

```typescript
invokeArn: string;
```


The ARN to be used for invoking Lambda Function from API Gateway.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L62">property kmsKeyArn</a>
</h3>

```typescript
kmsKeyArn: string;
```


The ARN for the KMS encryption key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L66">property lastModified</a>
</h3>

```typescript
lastModified: string;
```


The date this resource was last modified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L70">property memorySize</a>
</h3>

```typescript
memorySize: number;
```


Amount of memory in MB your Lambda Function can use at runtime.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L74">property qualifiedArn</a>
</h3>

```typescript
qualifiedArn: string;
```


The Amazon Resource Name (ARN) identifying your Lambda Function Version

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L78">property reservedConcurrentExecutions</a>
</h3>

```typescript
reservedConcurrentExecutions: number;
```


The amount of reserved concurrent executions for this lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L82">property role</a>
</h3>

```typescript
role: string;
```


IAM role attached to the Lambda Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L86">property runtime</a>
</h3>

```typescript
runtime: string;
```


The runtime environment for the Lambda function..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L90">property sourceCodeHash</a>
</h3>

```typescript
sourceCodeHash: string;
```


Base64-encoded representation of raw SHA-256 sum of the zip file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L94">property sourceCodeSize</a>
</h3>

```typescript
sourceCodeSize: number;
```


The size in bytes of the function .zip file.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L98">property timeout</a>
</h3>

```typescript
timeout: number;
```


The function execution time at which Lambda should terminate the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L102">property tracingConfig</a>
</h3>

```typescript
tracingConfig: { ... };
```


Tracing settings of the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L106">property version</a>
</h3>

```typescript
version: string;
```


The version of the Lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getFunction.ts#L110">property vpcConfig</a>
</h3>

```typescript
vpcConfig: { ... };
```


VPC configuration associated with your Lambda function.

<h2 class="pdoc-module-header" id="GetInvocationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts#L23">interface GetInvocationArgs</a>
</h2>

A collection of arguments for invoking getInvocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts#L27">property functionName</a>
</h3>

```typescript
functionName: string;
```


The name of the lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts#L31">property input</a>
</h3>

```typescript
input: string;
```


A string in JSON format that is passed as payload to the lambda function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts#L36">property qualifier</a>
</h3>

```typescript
qualifier?: string;
```


The qualifier (a.k.a version) of the lambda function. Defaults
to `$LATEST`.

<h2 class="pdoc-module-header" id="GetInvocationResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts#L42">interface GetInvocationResult</a>
</h2>

A collection of values returned by getInvocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts#L54">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts#L46">property result</a>
</h3>

```typescript
result: string;
```


A result of the lambda function invocation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/getInvocation.ts#L50">property resultMap</a>
</h3>

```typescript
resultMap: { ... };
```


This field is set only if result is a map of primitive types.

<h2 class="pdoc-module-header" id="PermissionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L172">interface PermissionArgs</a>
</h2>

The set of arguments for constructing a Permission resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L176">property action</a>
</h3>

```typescript
action: pulumi.Input<string>;
```


The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L180">property eventSourceToken</a>
</h3>

```typescript
eventSourceToken?: pulumi.Input<string>;
```


The Event Source Token to validate.  Used with [Alexa Skills][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L184">property function</a>
</h3>

```typescript
function: pulumi.Input<Function>;
```


Name of the Lambda function whose resource policy you are updating

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L190">property principal</a>
</h3>

```typescript
principal: pulumi.Input<string>;
```


The principal who is getting this permission.
e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
such as `events.amazonaws.com` or `sns.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L196">property qualifier</a>
</h3>

```typescript
qualifier?: pulumi.Input<string>;
```


Query parameter to specify function version or alias name.
The permission will then apply to the specific qualified ARN.
e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L200">property sourceAccount</a>
</h3>

```typescript
sourceAccount?: pulumi.Input<string>;
```


This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L209">property sourceArn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L213">property statementId</a>
</h3>

```typescript
statementId?: pulumi.Input<string>;
```


A unique statement identifier. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L217">property statementIdPrefix</a>
</h3>

```typescript
statementIdPrefix?: pulumi.Input<string>;
```


A statement identifier prefix. Terraform will generate a unique suffix. Conflicts with `statement_id`.

<h2 class="pdoc-module-header" id="PermissionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L121">interface PermissionState</a>
</h2>

Input properties used for looking up and filtering Permission resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L125">property action</a>
</h3>

```typescript
action?: pulumi.Input<string>;
```


The AWS Lambda action you want to allow in this statement. (e.g. `lambda:InvokeFunction`)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L129">property eventSourceToken</a>
</h3>

```typescript
eventSourceToken?: pulumi.Input<string>;
```


The Event Source Token to validate.  Used with [Alexa Skills][1].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L133">property function</a>
</h3>

```typescript
function?: pulumi.Input<Function>;
```


Name of the Lambda function whose resource policy you are updating

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L139">property principal</a>
</h3>

```typescript
principal?: pulumi.Input<string>;
```


The principal who is getting this permission.
e.g. `s3.amazonaws.com`, an AWS account ID, or any valid AWS service principal
such as `events.amazonaws.com` or `sns.amazonaws.com`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L145">property qualifier</a>
</h3>

```typescript
qualifier?: pulumi.Input<string>;
```


Query parameter to specify function version or alias name.
The permission will then apply to the specific qualified ARN.
e.g. `arn:aws:lambda:aws-region:acct-id:function:function-name:2`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L149">property sourceAccount</a>
</h3>

```typescript
sourceAccount?: pulumi.Input<string>;
```


This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L158">property sourceArn</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L162">property statementId</a>
</h3>

```typescript
statementId?: pulumi.Input<string>;
```


A unique statement identifier. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/permission.ts#L166">property statementIdPrefix</a>
</h3>

```typescript
statementIdPrefix?: pulumi.Input<string>;
```


A statement identifier prefix. Terraform will generate a unique suffix. Conflicts with `statement_id`.

<h2 class="pdoc-module-header" id="DotnetCore1d0Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L32">let DotnetCore1d0Runtime</a>
</h2>

```typescript
let DotnetCore1d0Runtime: Runtime = "dotnetcore1.0";
```

<h2 class="pdoc-module-header" id="DotnetCore2d0Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L33">let DotnetCore2d0Runtime</a>
</h2>

```typescript
let DotnetCore2d0Runtime: Runtime = "dotnetcore2.0";
```

<h2 class="pdoc-module-header" id="DotnetCore2d1Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L34">let DotnetCore2d1Runtime</a>
</h2>

```typescript
let DotnetCore2d1Runtime: Runtime = "dotnetcore2.1";
```

<h2 class="pdoc-module-header" id="Go1dxRuntime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L35">let Go1dxRuntime</a>
</h2>

```typescript
let Go1dxRuntime: Runtime = "go1.x";
```

<h2 class="pdoc-module-header" id="Java8Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L36">let Java8Runtime</a>
</h2>

```typescript
let Java8Runtime: Runtime = "java8";
```

<h2 class="pdoc-module-header" id="NodeJS4d3EdgeRuntime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L37">let NodeJS4d3EdgeRuntime</a>
</h2>

```typescript
let NodeJS4d3EdgeRuntime: Runtime = "nodejs4.3-edge";
```

<h2 class="pdoc-module-header" id="NodeJS4d3Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L38">let NodeJS4d3Runtime</a>
</h2>

```typescript
let NodeJS4d3Runtime: Runtime = "nodejs4.3";
```

<h2 class="pdoc-module-header" id="NodeJS6d10Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L39">let NodeJS6d10Runtime</a>
</h2>

```typescript
let NodeJS6d10Runtime: Runtime = "nodejs6.10";
```

<h2 class="pdoc-module-header" id="NodeJS8d10Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L40">let NodeJS8d10Runtime</a>
</h2>

```typescript
let NodeJS8d10Runtime: Runtime = "nodejs8.10";
```

<h2 class="pdoc-module-header" id="NodeJSRuntime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L41">let NodeJSRuntime</a>
</h2>

```typescript
let NodeJSRuntime: Runtime = "nodejs";
```

<h2 class="pdoc-module-header" id="Python2d7Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L42">let Python2d7Runtime</a>
</h2>

```typescript
let Python2d7Runtime: Runtime = "python2.7";
```

<h2 class="pdoc-module-header" id="Python3d6Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L43">let Python3d6Runtime</a>
</h2>

```typescript
let Python3d6Runtime: Runtime = "python3.6";
```

<h2 class="pdoc-module-header" id="Runtime">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/runtimes.ts#L18">type Runtime</a>
</h2>

```typescript
type Runtime = dotnetcore1.0 | dotnetcore2.0 | dotnetcore2.1 | go1.x | java8 | nodejs4.3-edge | nodejs4.3 | nodejs6.10 | nodejs8.10 | nodejs | python2.7 | python3.6;
```


Runtime is a union type containing all available AWS Lambda runtimes.

