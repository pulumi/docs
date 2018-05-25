---
title: Module serverless
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Function">class Function</a>
* <a href="#Context">interface Context</a>
* <a href="#FunctionOptions">interface FunctionOptions</a>
* <a href="#Handler">type Handler</a>

<a href="/serverless/function.ts">serverless/function.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L89">class Function</a>
</h2>

Function is a higher-level API for creating and managing AWS Lambda Function resources implemented
by a Lumi lambda expression and with a set of attached policies.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L92">constructor</a>
</h3>

```typescript
new Function(name: string, options: FunctionOptions, func: Handler, opts?: pulumi.ResourceOptions, serialize?: { ... })
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L91">property lambda</a>
</h3>

```typescript
public lambda: lambda.Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L90">property options</a>
</h3>

```typescript
public options: FunctionOptions;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L92">property role</a>
</h3>

```typescript
public role: Role;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Context">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L25">interface Context</a>
</h2>

Context is the shape of the context object passed to a Function callback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L36">method getRemainingTimeInMillis</a>
</h3>

```typescript
getRemainingTimeInMillis(): string
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L31">property awsRequestId</a>
</h3>

```typescript
awsRequestId: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L26">property callbackWaitsForEmptyEventLoop</a>
</h3>

```typescript
callbackWaitsForEmptyEventLoop: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L35">property clientContext</a>
</h3>

```typescript
clientContext: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L27">property functionName</a>
</h3>

```typescript
functionName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L28">property functionVersion</a>
</h3>

```typescript
functionVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L34">property identity</a>
</h3>

```typescript
identity: any;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L29">property invokedFunctionArn</a>
</h3>

```typescript
invokedFunctionArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L32">property logGroupName</a>
</h3>

```typescript
logGroupName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L33">property logStreamName</a>
</h3>

```typescript
logStreamName: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L30">property memoryLimitInMB</a>
</h3>

```typescript
memoryLimitInMB: string;
```

<h2 class="pdoc-module-header" id="FunctionOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L47">interface FunctionOptions</a>
</h2>

FunctionOptions provides configuration options for the serverless Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L71">property deadLetterConfig</a>
</h3>

```typescript
deadLetterConfig?: { ... };
```


A dead letter target ARN to send function invocation failures to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L82">property includePaths</a>
</h3>

```typescript
includePaths?: string[];
```


The paths relative to the program folder to include in the Lambda upload.  Default is `["node_modules"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L63">property memorySize</a>
</h3>

```typescript
memorySize?: number;
```


The memory size limit to use for execution of the Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L51">property policies</a>
</h3>

```typescript
policies?: ARN[];
```


A list of IAM policy ARNs to attach to the Function.  Must provide either [policies] or [role].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L55">property role</a>
</h3>

```typescript
role?: Role;
```


A pre-created role to use for the Function.  Must provide either [policies] or [role].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L67">property runtime</a>
</h3>

```typescript
runtime?: lambda.Runtime;
```


The Lambda runtime to use.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L59">property timeout</a>
</h3>

```typescript
timeout?: number;
```


A timout, in seconds, to apply to the Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L75">property vpcConfig</a>
</h3>

```typescript
vpcConfig?: { ... };
```


Configuration for a VPC to run the Function within.

<h2 class="pdoc-module-header" id="Handler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/serverless/function.ts#L42">type Handler</a>
</h2>

```typescript
type Handler = { ... };
```


Handler is the signature for a serverless function.

