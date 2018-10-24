---
title: Module codepipeline
---

<a href="../index.html">@pulumi/aws</a> &gt; codepipeline

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Pipeline">class Pipeline</a>
* <a href="#Webhook">class Webhook</a>
* <a href="#PipelineArgs">interface PipelineArgs</a>
* <a href="#PipelineState">interface PipelineState</a>
* <a href="#WebhookArgs">interface WebhookArgs</a>
* <a href="#WebhookState">interface WebhookState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts">codepipeline/pipeline.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts">codepipeline/webhook.ts</a> 


<h2 class="pdoc-module-header" id="Pipeline">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L12">class Pipeline</a>
</h2>

Provides a CodePipeline.

~> **NOTE on `aws_codepipeline`:** - the `GITHUB_TOKEN` environment variable must be set if the GitHub provider is specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L42">constructor</a>
</h3>

```typescript
new Pipeline(name: string, args: PipelineArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Pipeline resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PipelineState): Pipeline
```


Get an existing Pipeline resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The codepipeline ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L33">property artifactStore</a>
</h3>

```typescript
public artifactStore: pulumi.Output<{ ... }>;
```


An artifact_store block. Artifact stores are documented below.
* `stage` (Minimum of at least two `stage` blocks is required) A stage block. Stages are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L41">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L42">property stages</a>
</h3>

```typescript
public stages: pulumi.Output<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Webhook">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L10">class Webhook</a>
</h2>

Provides a CodePipeline Webhook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L50">constructor</a>
</h3>

```typescript
new Webhook(name: string, args: WebhookArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Webhook resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: WebhookState): Webhook
```


Get an existing Webhook resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L26">property authentication</a>
</h3>

```typescript
public authentication: pulumi.Output<string>;
```


The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L30">property authenticationConfiguration</a>
</h3>

```typescript
public authenticationConfiguration: pulumi.Output<{ ... } | undefined>;
```


An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L34">property filters</a>
</h3>

```typescript
public filters: pulumi.Output<{ ... }[]>;
```


One or more `filter` blocks. Filter blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L38">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the webhook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L42">property targetAction</a>
</h3>

```typescript
public targetAction: pulumi.Output<string>;
```


The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L46">property targetPipeline</a>
</h3>

```typescript
public targetPipeline: pulumi.Output<string>;
```


The name of the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L50">property url</a>
</h3>

```typescript
public url: pulumi.Output<string>;
```


The CodePipeline webhook's URL. POST events to this endpoint to trigger the target.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PipelineArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L109">interface PipelineArgs</a>
</h2>

The set of arguments for constructing a Pipeline resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L114">property artifactStore</a>
</h3>

```typescript
artifactStore: pulumi.Input<{ ... }>;
```


An artifact_store block. Artifact stores are documented below.
* `stage` (Minimum of at least two `stage` blocks is required) A stage block. Stages are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L122">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L123">property stages</a>
</h3>

```typescript
stages: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h2 class="pdoc-module-header" id="PipelineState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L85">interface PipelineState</a>
</h2>

Input properties used for looking up and filtering Pipeline resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L89">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The codepipeline ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L94">property artifactStore</a>
</h3>

```typescript
artifactStore?: pulumi.Input<{ ... }>;
```


An artifact_store block. Artifact stores are documented below.
* `stage` (Minimum of at least two `stage` blocks is required) A stage block. Stages are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L102">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


A service role Amazon Resource Name (ARN) that grants AWS CodePipeline permission to make calls to AWS services on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L103">property stages</a>
</h3>

```typescript
stages?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h2 class="pdoc-module-header" id="WebhookArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L134">interface WebhookArgs</a>
</h2>

The set of arguments for constructing a Webhook resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L138">property authentication</a>
</h3>

```typescript
authentication: pulumi.Input<string>;
```


The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L142">property authenticationConfiguration</a>
</h3>

```typescript
authenticationConfiguration?: pulumi.Input<{ ... }>;
```


An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L146">property filters</a>
</h3>

```typescript
filters: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `filter` blocks. Filter blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L150">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the webhook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L154">property targetAction</a>
</h3>

```typescript
targetAction: pulumi.Input<string>;
```


The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L158">property targetPipeline</a>
</h3>

```typescript
targetPipeline: pulumi.Input<string>;
```


The name of the pipeline.

<h2 class="pdoc-module-header" id="WebhookState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L100">interface WebhookState</a>
</h2>

Input properties used for looking up and filtering Webhook resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L104">property authentication</a>
</h3>

```typescript
authentication?: pulumi.Input<string>;
```


The type of authentication  to use. One of `IP`, `GITHUB_HMAC`, or `UNAUTHENTICATED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L108">property authenticationConfiguration</a>
</h3>

```typescript
authenticationConfiguration?: pulumi.Input<{ ... }>;
```


An `auth` block. Required for `IP` and `GITHUB_HMAC`. Auth blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L112">property filters</a>
</h3>

```typescript
filters?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `filter` blocks. Filter blocks are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L116">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the webhook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L120">property targetAction</a>
</h3>

```typescript
targetAction?: pulumi.Input<string>;
```


The name of the action in a pipeline you want to connect to the webhook. The action must be from the source (first) stage of the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L124">property targetPipeline</a>
</h3>

```typescript
targetPipeline?: pulumi.Input<string>;
```


The name of the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/webhook.ts#L128">property url</a>
</h3>

```typescript
url?: pulumi.Input<string>;
```


The CodePipeline webhook's URL. POST events to this endpoint to trigger the target.

