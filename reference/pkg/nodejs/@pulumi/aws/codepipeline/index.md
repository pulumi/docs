---
title: Module codepipeline
---

<a href="../index.html">@pulumi/aws</a> &gt; codepipeline

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Pipeline">class Pipeline</a>
* <a href="#PipelineArgs">interface PipelineArgs</a>
* <a href="#PipelineState">interface PipelineState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts">codepipeline/pipeline.ts</a> 


<h2 class="pdoc-module-header" id="Pipeline">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L11">class Pipeline</a>
</h2>

Provides a CodePipeline.

~> **NOTE on `aws_codepipeline`:** - the `GITHUB_TOKEN` environment variable must be set if the GitHub provider is specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L43">constructor</a>
</h3>

```typescript
new Pipeline(name: string, args: PipelineArgs, opts?: pulumi.ResourceOptions)
```


Create a Pipeline resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PipelineState): Pipeline
```


Get an existing Pipeline resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The codepipeline ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L31">property artifactStore</a>
</h3>

```typescript
public artifactStore: pulumi.Output<{ ... }>;
```


An artifact_store block. Artifact stores are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The action declaration's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L39">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L43">property stages</a>
</h3>

```typescript
public stages: pulumi.Output<{ ... }[]>;
```


A stage block. Stages are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PipelineArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L112">interface PipelineArgs</a>
</h2>

The set of arguments for constructing a Pipeline resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L116">property artifactStore</a>
</h3>

```typescript
artifactStore: pulumi.Input<{ ... }>;
```


An artifact_store block. Artifact stores are documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The action declaration's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L124">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L128">property stages</a>
</h3>

```typescript
stages: pulumi.Input<{ ... }[]>;
```


A stage block. Stages are documented below.

<h2 class="pdoc-module-header" id="PipelineState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L86">interface PipelineState</a>
</h2>

Input properties used for looking up and filtering Pipeline resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L90">property arn</a>
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

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The action declaration's name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L102">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM service role that will perform the declared action. This is assumed through the roleArn for the pipeline.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/codepipeline/pipeline.ts#L106">property stages</a>
</h3>

```typescript
stages?: pulumi.Input<{ ... }[]>;
```


A stage block. Stages are documented below.

