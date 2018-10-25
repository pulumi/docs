---
title: Module workspaces
---

<a href="../index.html">@pulumi/aws</a> &gt; workspaces

<h2 class="pdoc-module-header">Index</h2>

* <a href="#getBundle">function getBundle</a>
* <a href="#GetBundleArgs">interface GetBundleArgs</a>
* <a href="#GetBundleResult">interface GetBundleResult</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts">workspaces/getBundle.ts</a> 


<h2 class="pdoc-module-header" id="getBundle">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L10">function getBundle</a>
</h2>

```typescript
getBundle(args: GetBundleArgs, opts?: pulumi.InvokeOptions): Promise<GetBundleResult>
```


Use this data source to get information about a Workspaces Bundle.

<h2 class="pdoc-module-header" id="GetBundleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L19">interface GetBundleArgs</a>
</h2>

A collection of arguments for invoking getBundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L23">property bundleId</a>
</h3>

```typescript
bundleId: string;
```


The ID of the bundle.

<h2 class="pdoc-module-header" id="GetBundleResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L29">interface GetBundleResult</a>
</h2>

A collection of values returned by getBundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L33">property computeTypes</a>
</h3>

```typescript
computeTypes: { ... }[];
```


The compute type. See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L37">property description</a>
</h3>

```typescript
description: string;
```


The description of the bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L57">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L41">property name</a>
</h3>

```typescript
name: string;
```


The name of the compute type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L45">property owner</a>
</h3>

```typescript
owner: string;
```


The owner of the bundle.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L49">property rootStorages</a>
</h3>

```typescript
rootStorages: { ... }[];
```


The root volume. See supported fields below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/workspaces/getBundle.ts#L53">property userStorages</a>
</h3>

```typescript
userStorages: { ... }[];
```


The user storage. See supported fields below.

