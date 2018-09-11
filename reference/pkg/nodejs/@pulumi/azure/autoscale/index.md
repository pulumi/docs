---
title: Module autoscale
---

<a href="../index.html">@pulumi/azure</a> &gt; autoscale

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Setting">class Setting</a>
* <a href="#SettingArgs">interface SettingArgs</a>
* <a href="#SettingState">interface SettingState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts">autoscale/setting.ts</a> 


<h2 class="pdoc-module-header" id="Setting">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L10">class Setting</a>
</h2>

Manages an AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L54">constructor</a>
</h3>

```typescript
new Setting(name: string, args: SettingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Setting resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SettingState): Setting
```


Get an existing Setting resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L26">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the AutoScale Setting. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L38">property notification</a>
</h3>

```typescript
public notification: pulumi.Output<{ ... } | undefined>;
```


Specifies a `notification` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L42">property profiles</a>
</h3>

```typescript
public profiles: pulumi.Output<{ ... }[]>;
```


Specifies one or more (up to 20) `profile` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L46">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L50">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L54">property targetResourceId</a>
</h3>

```typescript
public targetResourceId: pulumi.Output<string>;
```


Specifies the resource ID of the resource that the autoscale setting should be added to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SettingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L144">interface SettingArgs</a>
</h2>

The set of arguments for constructing a Setting resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L148">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L152">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the AutoScale Setting. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L160">property notification</a>
</h3>

```typescript
notification?: pulumi.Input<{ ... }>;
```


Specifies a `notification` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L164">property profiles</a>
</h3>

```typescript
profiles: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies one or more (up to 20) `profile` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L168">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L172">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L176">property targetResourceId</a>
</h3>

```typescript
targetResourceId: pulumi.Input<string>;
```


Specifies the resource ID of the resource that the autoscale setting should be added to.

<h2 class="pdoc-module-header" id="SettingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L106">interface SettingState</a>
</h2>

Input properties used for looking up and filtering Setting resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L110">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Specifies whether automatic scaling is enabled for the target resource. Defaults to `true`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L114">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the AutoScale Setting. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L122">property notification</a>
</h3>

```typescript
notification?: pulumi.Input<{ ... }>;
```


Specifies a `notification` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L126">property profiles</a>
</h3>

```typescript
profiles?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies one or more (up to 20) `profile` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L134">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/autoscale/setting.ts#L138">property targetResourceId</a>
</h3>

```typescript
targetResourceId?: pulumi.Input<string>;
```


Specifies the resource ID of the resource that the autoscale setting should be added to.

