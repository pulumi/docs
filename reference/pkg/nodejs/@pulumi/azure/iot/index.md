---
title: Module iot
---

<a href="../index.html">@pulumi/azure</a> &gt; iot

<h2 class="pdoc-module-header">Index</h2>

* <a href="#IoTHub">class IoTHub</a>
* <a href="#IoTHubArgs">interface IoTHubArgs</a>
* <a href="#IoTHubState">interface IoTHubState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts">iot/ioTHub.ts</a> 


<h2 class="pdoc-module-header" id="IoTHub">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L10">class IoTHub</a>
</h2>

Manages a IotHub

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L51">constructor</a>
</h3>

```typescript
new IoTHub(name: string, args: IoTHubArgs, opts?: pulumi.CustomResourceOptions)
```


Create a IoTHub resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IoTHubState): IoTHub
```


Get an existing IoTHub resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L26">property hostname</a>
</h3>

```typescript
public hostname: pulumi.Output<string>;
```


The hostname of the IotHub Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the IotHub resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L42">property sharedAccessPolicies</a>
</h3>

```typescript
public sharedAccessPolicies: pulumi.Output<{ ... }[]>;
```


One or more `shared_access_policy` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L46">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L50">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L51">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="IoTHubArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L135">interface IoTHubArgs</a>
</h2>

The set of arguments for constructing a IoTHub resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L139">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L143">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the IotHub resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L147">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L151">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L155">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="IoTHubState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L100">interface IoTHubState</a>
</h2>

Input properties used for looking up and filtering IoTHub resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L104">property hostname</a>
</h3>

```typescript
hostname?: pulumi.Input<string>;
```


The hostname of the IotHub Resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L108">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource has to be createc. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L112">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the IotHub resource. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L116">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group under which the IotHub resource has to be created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L120">property sharedAccessPolicies</a>
</h3>

```typescript
sharedAccessPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


One or more `shared_access_policy` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L124">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L128">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/iot/ioTHub.ts#L129">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```

