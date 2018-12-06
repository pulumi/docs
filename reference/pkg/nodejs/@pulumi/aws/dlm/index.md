---
title: Module dlm
---

<a href="../index.html">@pulumi/aws</a> &gt; dlm

<h2 class="pdoc-module-header">Index</h2>

* <a href="#LifecyclePolicy">class LifecyclePolicy</a>
* <a href="#LifecyclePolicyArgs">interface LifecyclePolicyArgs</a>
* <a href="#LifecyclePolicyState">interface LifecyclePolicyState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts">dlm/lifecyclePolicy.ts</a> 


<h2 class="pdoc-module-header" id="LifecyclePolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L10">class LifecyclePolicy</a>
</h2>

Provides a [Data Lifecycle Manager (DLM) lifecycle policy](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshot-lifecycle.html) for managing snapshots.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L38">constructor</a>
</h3>

```typescript
new LifecyclePolicy(name: string, args: LifecyclePolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a LifecyclePolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LifecyclePolicyState): LifecyclePolicy
```


Get an existing LifecyclePolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L26">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


A description for the DLM lifecycle policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L30">property executionRoleArn</a>
</h3>

```typescript
public executionRoleArn: pulumi.Output<string>;
```


The ARN of an IAM role that is able to be assumed by the DLM service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L34">property policyDetails</a>
</h3>

```typescript
public policyDetails: pulumi.Output<{ ... }>;
```


See the `policy_details` configuration block. Max of 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L38">property state</a>
</h3>

```typescript
public state: pulumi.Output<string | undefined>;
```


Whether the lifecycle policy should be enabled or disabled. `ENABLED` or `DISABLED` are valid values. Defaults to `ENABLED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="LifecyclePolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L101">interface LifecyclePolicyArgs</a>
</h2>

The set of arguments for constructing a LifecyclePolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L105">property description</a>
</h3>

```typescript
description: pulumi.Input<string>;
```


A description for the DLM lifecycle policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L109">property executionRoleArn</a>
</h3>

```typescript
executionRoleArn: pulumi.Input<string>;
```


The ARN of an IAM role that is able to be assumed by the DLM service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L113">property policyDetails</a>
</h3>

```typescript
policyDetails: pulumi.Input<{ ... }>;
```


See the `policy_details` configuration block. Max of 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L117">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


Whether the lifecycle policy should be enabled or disabled. `ENABLED` or `DISABLED` are valid values. Defaults to `ENABLED`.

<h2 class="pdoc-module-header" id="LifecyclePolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L79">interface LifecyclePolicyState</a>
</h2>

Input properties used for looking up and filtering LifecyclePolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L83">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for the DLM lifecycle policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L87">property executionRoleArn</a>
</h3>

```typescript
executionRoleArn?: pulumi.Input<string>;
```


The ARN of an IAM role that is able to be assumed by the DLM service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L91">property policyDetails</a>
</h3>

```typescript
policyDetails?: pulumi.Input<{ ... }>;
```


See the `policy_details` configuration block. Max of 1.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dlm/lifecyclePolicy.ts#L95">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


Whether the lifecycle policy should be enabled or disabled. `ENABLED` or `DISABLED` are valid values. Defaults to `ENABLED`.

