---
title: Module serverless
---

<a href="../index.html">@pulumi/aws</a> &gt; serverless

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Function">class Function</a>
* <a href="#Context">interface Context</a>
* <a href="#FunctionOptions">type FunctionOptions</a>
* <a href="#Handler">type Handler</a>
* <a href="#HandlerFactory">type HandlerFactory</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts">serverless/function.ts</a> 


<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L128">class Function</a>
</h2>

Function is a higher-level API for creating and managing AWS Lambda Function resources implemented
by a Lumi lambda expression and with a set of attached policies.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L131">constructor</a>
</h3>

```typescript
new Function(name: string, options: FunctionOptions, func?: Handler, opts?: pulumi.ResourceOptions, serialize?: { ... })
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L130">property lambda</a>
</h3>

```typescript
public lambda: lambda.Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L129">property options</a>
</h3>

```typescript
public options: FunctionOptions;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L131">property role</a>
</h3>

```typescript
public role: Role;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Context">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L25">interface Context</a>
</h2>

Context is the shape of the context object passed to a Function callback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L36">method getRemainingTimeInMillis</a>
</h3>

```typescript
getRemainingTimeInMillis(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L31">property awsRequestId</a>
</h3>

```typescript
awsRequestId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L26">property callbackWaitsForEmptyEventLoop</a>
</h3>

```typescript
callbackWaitsForEmptyEventLoop: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L35">property clientContext</a>
</h3>

```typescript
clientContext: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L27">property functionName</a>
</h3>

```typescript
functionName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L28">property functionVersion</a>
</h3>

```typescript
functionVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L34">property identity</a>
</h3>

```typescript
identity: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L29">property invokedFunctionArn</a>
</h3>

```typescript
invokedFunctionArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L32">property logGroupName</a>
</h3>

```typescript
logGroupName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L33">property logStreamName</a>
</h3>

```typescript
logStreamName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L30">property memoryLimitInMB</a>
</h3>

```typescript
memoryLimitInMB: string;
```

<h2 class="pdoc-module-header" id="FunctionOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L59">type FunctionOptions</a>
</h2>

```typescript
type FunctionOptions = Overwrite<lambda.FunctionArgs, { ... }>;
```


FunctionOptions provides configuration options for the serverless Function.  It is effectively
equivalent to [aws.lambda.FunctionArgs] except with a few important differences documented at the
property level.  For example, [role] is an actual iam.Role instance, and not an ARN. Properties
like [runtime] are now optional.  And some properties (like [code]) are entirely disallowed.

<h2 class="pdoc-module-header" id="Handler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L43">type Handler</a>
</h2>

```typescript
type Handler = { ... };
```


HandlerSignature is the signature for a serverless function that will be invoked each time
the AWS Lambda is invoked.

<h2 class="pdoc-module-header" id="HandlerFactory">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L51">type HandlerFactory</a>
</h2>

```typescript
type HandlerFactory = { ... };
```


HandlerFactory is the signature for a function that will be called once to produce the serverless
function that AWS Lambda will invoke.  It can be used to initialize expensive state once that can
then be used across all invocations of the Lambda (as long as the Lambda is using the same warm
node instance).

