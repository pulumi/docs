---
title: Module serverless
---

<a href="../index.html">@pulumi/gcp</a> &gt; serverless

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Function">class Function</a>
* <a href="#FunctionOptions">interface FunctionOptions</a>
* <a href="#Handler">type Handler</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts">serverless/function.ts</a> 


<h2 class="pdoc-module-header" id="Function">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L71">class Function</a>
</h2>

Function is a higher-level API for creating and managing GCP Cloud Function resources implemented
by a given handler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L75">constructor</a>
</h3>

```typescript
new Function(name: string, options: FunctionOptions, func: Handler, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L74">property bucket</a>
</h3>

```typescript
public bucket: storage.Bucket;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L75">property bucketObject</a>
</h3>

```typescript
public bucketObject: storage.BucketObject;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L73">property function</a>
</h3>

```typescript
public function: cloudfunctions.Function;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L72">property options</a>
</h3>

```typescript
public options: FunctionOptions;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="FunctionOptions">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L32">interface FunctionOptions</a>
</h2>

FunctionOptions provides configuration options for the serverless Function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L36">property availableMemoryMb</a>
</h3>

```typescript
availableMemoryMb?: pulumi.Input<number>;
```


Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L40">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L64">property excludePackages</a>
</h3>

```typescript
excludePackages?: string[];
```


The packages relative to the program folder to not include the Function upload. This can be
used to override the default serialization logic that includes all packages referenced by
project.json (except @pulumi packages).  Default is `[]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L44">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A set of key/value label pairs to assign to the function.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L50">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


Project of the function. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L54">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L58">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.

<h2 class="pdoc-module-header" id="Handler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/serverless/function.ts#L27">type Handler</a>
</h2>

```typescript
type Handler = { ... };
```


Handler is the signature for a serverless function.
For HTTP Function it accepts Request and Response from Express.
See https://cloud.google.com/functions/docs/writing/http.

