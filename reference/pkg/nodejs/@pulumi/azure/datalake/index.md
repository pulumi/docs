---
title: Module datalake
---

<a href="../index.html">@pulumi/azure</a> &gt; datalake

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Store">class Store</a>
* <a href="#getStore">function getStore</a>
* <a href="#GetStoreArgs">interface GetStoreArgs</a>
* <a href="#GetStoreResult">interface GetStoreResult</a>
* <a href="#StoreArgs">interface StoreArgs</a>
* <a href="#StoreState">interface StoreState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts">datalake/getStore.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts">datalake/store.ts</a> 


<h2 class="pdoc-module-header" id="Store">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L9">class Store</a>
</h2>

Manage an Azure Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L41">constructor</a>
</h3>

```typescript
new Store(name: string, args: StoreArgs, opts?: pulumi.ResourceOptions)
```


Create a Store resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StoreState): Store
```


Get an existing Store resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L37">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L41">property tier</a>
</h3>

```typescript
public tier: pulumi.Output<string | undefined>;
```


The monnthly commitment tier for Data Lake Store. Accepted values are `Consumption`, `Commitment_1TB`, `Commitment_10TB`, `Commitment_100TB`, `Commitment_500TB`, `Commitment_1PB` or `Commitment_5PB`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getStore">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L9">function getStore</a>
</h2>

```typescript
getStore(args: GetStoreArgs): Promise<GetStoreResult>
```


Use this data source to obtain information about a Data Lake Store.

<h2 class="pdoc-module-header" id="GetStoreArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L19">interface GetStoreArgs</a>
</h2>

A collection of arguments for invoking getStore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The Name of the Resource Group where the Data Lake Store exists.

<h2 class="pdoc-module-header" id="GetStoreResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L33">interface GetStoreResult</a>
</h2>

A collection of values returned by getStore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L34">property location</a>
</h3>

```typescript
location: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L38">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assign to the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L42">property tier</a>
</h3>

```typescript
tier: string;
```


Current monthly commitment tier for the account.

<h2 class="pdoc-module-header" id="StoreArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L107">interface StoreArgs</a>
</h2>

The set of arguments for constructing a Store resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L111">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L115">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L119">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L123">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L127">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


The monnthly commitment tier for Data Lake Store. Accepted values are `Consumption`, `Commitment_1TB`, `Commitment_10TB`, `Commitment_100TB`, `Commitment_500TB`, `Commitment_1PB` or `Commitment_5PB`.

<h2 class="pdoc-module-header" id="StoreState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L81">interface StoreState</a>
</h2>

Input properties used for looking up and filtering Store resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L85">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L89">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L93">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L97">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L101">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


The monnthly commitment tier for Data Lake Store. Accepted values are `Consumption`, `Commitment_1TB`, `Commitment_10TB`, `Commitment_100TB`, `Commitment_500TB`, `Commitment_1PB` or `Commitment_5PB`.

