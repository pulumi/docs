---
title: Module serverless
---

<a href="../index.html">@pulumi/aws</a> &gt; serverless

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Function">class Function</a>
* <a href="#Context">type Context</a>
* <a href="#FunctionOptions">type FunctionOptions</a>
* <a href="#Handler">type Handler</a>
* <a href="#HandlerFactory">type HandlerFactory</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts">serverless/function.ts</a> 


<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L94">class Function</a>
</h2>

Function is a higher-level API for creating and managing AWS Lambda Function resources
implemented by a Pulumi lambda expression and with a set of attached policies.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L97">constructor</a>
</h3>

```typescript
new Function(name: string, options: FunctionOptions, func?: Handler, opts?: pulumi.ResourceOptions, serialize?: { ... })
```

* `func` Deprecated.  Pass the function as [options.func] or [options.factoryFunc] instead.

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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L96">property lambda</a>
</h3>

```typescript
public lambda: lambda.Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L95">property options</a>
</h3>

```typescript
public options: FunctionOptions;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L97">property role</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L23">type Context</a>
</h2>

```typescript
type Context = lambda.Context;
```

<h2 class="pdoc-module-header" id="FunctionOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L51">type FunctionOptions</a>
</h2>

```typescript
type FunctionOptions = utils.Overwrite<lambda.CallbackFunctionArgs<any, any>, { ... }>;
```


FunctionOptions provides configuration options for the serverless Function.  It is effectively
equivalent to [aws.lambda.FunctionArgs] except with a few important differences documented at the
property level.  For example, [role] is an actual iam.Role instance, and not an ARN. Properties
like [runtime] are now optional.  And some properties (like [code]) are entirely disallowed.

<h2 class="pdoc-module-header" id="Handler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L31">type Handler</a>
</h2>

```typescript
type Handler = lambda.Callback<any, any>;
```


[Handler] is the signature for a serverless function that will be invoked each time the AWS
Lambda is invoked.

<h2 class="pdoc-module-header" id="HandlerFactory">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/serverless/function.ts#L41">type HandlerFactory</a>
</h2>

```typescript
type HandlerFactory = { ... };
```


HandlerFactory is the signature for a function that will be called once to produce the serverless
function that AWS Lambda will invoke.  It can be used to initialize expensive state once that can
then be used across all invocations of the Lambda (as long as the Lambda is using the same warm
node instance).

