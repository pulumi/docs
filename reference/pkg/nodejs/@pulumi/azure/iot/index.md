---
title: Module iot
---

<a href="..">@pulumi/azure</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#IoTHub">class IoTHub</a>
* <a href="#IoTHubArgs">interface IoTHubArgs</a>
* <a href="#IoTHubState">interface IoTHubState</a>

<a href="/iot/ioTHub.ts">iot/ioTHub.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="IoTHub">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L9">class IoTHub</a>
</h2>

Creates a new IotHub

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L50">constructor</a>
</h3>

```typescript
new IoTHub(name: string, args: IoTHubArgs, opts?: pulumi.ResourceOptions)
```


Create a IoTHub resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new IoTHub(name: string, state?: IoTHubState, opts?: pulumi.ResourceOptions)
```


Create a IoTHub resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IoTHubState): IoTHub
```


Get an existing IoTHub resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L25">property hostname</a>
</h3>

```typescript
public hostname: pulumi.Output<string>;
```


The hostname of the IotHub Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L29">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the sku. Possible values are `F1`, `S1`, `S2`, and `S3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L37">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L41">property sharedAccessPolicies</a>
</h3>

```typescript
public sharedAccessPolicies: pulumi.Output<{ ... }[]>;
```


A list of `shared_access_policy` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L45">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L49">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L50">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IoTHubArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L136">interface IoTHubArgs</a>
</h2>

The set of arguments for constructing a IoTHub resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L140">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L144">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the sku. Possible values are `F1`, `S1`, `S2`, and `S3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L148">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L152">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L156">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="IoTHubState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L101">interface IoTHubState</a>
</h2>

Input properties used for looking up and filtering IoTHub resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L105">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


The hostname of the IotHub Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L109">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the sku. Possible values are `F1`, `S1`, `S2`, and `S3`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L117">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L121">property sharedAccessPolicies</a>
</h3>

```typescript
sharedAccessPolicies?: pulumi.Input<{ ... }[]>;
```


A list of `shared_access_policy` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L125">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L129">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/iot/ioTHub.ts#L130">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```

