---
title: Module swf
---

<a href="../index.html">@pulumi/aws</a> &gt; swf

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Domain">class Domain</a>
* <a href="#DomainArgs">interface DomainArgs</a>
* <a href="#DomainState">interface DomainState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts">swf/domain.ts</a> 


<h2 class="pdoc-module-header" id="Domain">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L10">class Domain</a>
</h2>

Provides an SWF Domain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L38">constructor</a>
</h3>

```typescript
new Domain(name: string, args: DomainArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Domain resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DomainState): Domain
```


Get an existing Domain resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The domain description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the domain. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L34">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L38">property workflowExecutionRetentionPeriodInDays</a>
</h3>

```typescript
public workflowExecutionRetentionPeriodInDays: pulumi.Output<string>;
```


Length of time that SWF will continue to retain information about the workflow execution after the workflow execution is complete, must be between 0 and 90 days.

<h2 class="pdoc-module-header" id="DomainArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L95">interface DomainArgs</a>
</h2>

The set of arguments for constructing a Domain resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L99">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The domain description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the domain. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L107">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L111">property workflowExecutionRetentionPeriodInDays</a>
</h3>

```typescript
workflowExecutionRetentionPeriodInDays: pulumi.Input<string>;
```


Length of time that SWF will continue to retain information about the workflow execution after the workflow execution is complete, must be between 0 and 90 days.

<h2 class="pdoc-module-header" id="DomainState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L73">interface DomainState</a>
</h2>

Input properties used for looking up and filtering Domain resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L77">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The domain description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L81">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the domain. If omitted, Terraform will assign a random, unique name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L85">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/swf/domain.ts#L89">property workflowExecutionRetentionPeriodInDays</a>
</h3>

```typescript
workflowExecutionRetentionPeriodInDays?: pulumi.Input<string>;
```


Length of time that SWF will continue to retain information about the workflow execution after the workflow execution is complete, must be between 0 and 90 days.

