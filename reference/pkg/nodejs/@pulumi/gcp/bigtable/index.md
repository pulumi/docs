---
title: Module bigtable
---

<a href="../index.html">@pulumi/gcp</a> &gt; bigtable

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Instance">class Instance</a>
* <a href="#Table">class Table</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceState">interface InstanceState</a>
* <a href="#TableArgs">interface TableArgs</a>
* <a href="#TableState">interface TableState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts">bigtable/instance.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts">bigtable/table.ts</a> 


<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L13">class Instance</a>
</h2>

Creates a Google Bigtable instance. For more information see
[the official documentation](https://cloud.google.com/bigtable/) and
[API](https://cloud.google.com/bigtable/docs/go/reference).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L58">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L29">property clusterId</a>
</h3>

```typescript
public clusterId: pulumi.Output<string>;
```


The ID of the Cloud Bigtable cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L33">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string>;
```


The human-readable display name of the Bigtable instance. Defaults to the instance `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L37">property instanceType</a>
</h3>

```typescript
public instanceType: pulumi.Output<string | undefined>;
```


The instance type to create. One of `"DEVELOPMENT"` or `"PRODUCTION"`. Defaults to `"PRODUCTION"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Cloud Bigtable instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L45">property numNodes</a>
</h3>

```typescript
public numNodes: pulumi.Output<number | undefined>;
```


The number of nodes in your Cloud Bigtable cluster. Minimum of `3` for a `PRODUCTION` instance. Cannot be set for a `DEVELOPMENT` instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L50">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L54">property storageType</a>
</h3>

```typescript
public storageType: pulumi.Output<string | undefined>;
```


The storage type to use. One of `"SSD"` or `"HDD"`. Defaults to `"SSD"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L58">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string>;
```


The zone to create the Cloud Bigtable cluster in. Zones that support Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).

<h2 class="pdoc-module-header" id="Table">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L13">class Table</a>
</h2>

Creates a Google Bigtable table inside an instance. For more information see
[the official documentation](https://cloud.google.com/bigtable/) and
[API](https://cloud.google.com/bigtable/docs/go/reference).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L42">constructor</a>
</h3>

```typescript
new Table(name: string, args: TableArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Table resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState): Table
```


Get an existing Table resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L29">property instanceName</a>
</h3>

```typescript
public instanceName: pulumi.Output<string>;
```


The name of the Bigtable instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L38">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L42">property splitKeys</a>
</h3>

```typescript
public splitKeys: pulumi.Output<string[] | undefined>;
```


A list of predefined keys to split the table on.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L140">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L144">property clusterId</a>
</h3>

```typescript
clusterId: pulumi.Input<string>;
```


The ID of the Cloud Bigtable cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L148">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The human-readable display name of the Bigtable instance. Defaults to the instance `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L152">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The instance type to create. One of `"DEVELOPMENT"` or `"PRODUCTION"`. Defaults to `"PRODUCTION"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L156">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Cloud Bigtable instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L160">property numNodes</a>
</h3>

```typescript
numNodes?: pulumi.Input<number>;
```


The number of nodes in your Cloud Bigtable cluster. Minimum of `3` for a `PRODUCTION` instance. Cannot be set for a `DEVELOPMENT` instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L165">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L169">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


The storage type to use. One of `"SSD"` or `"HDD"`. Defaults to `"SSD"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L173">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone to create the Cloud Bigtable cluster in. Zones that support Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L101">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L105">property clusterId</a>
</h3>

```typescript
clusterId?: pulumi.Input<string>;
```


The ID of the Cloud Bigtable cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L109">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The human-readable display name of the Bigtable instance. Defaults to the instance `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L113">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The instance type to create. One of `"DEVELOPMENT"` or `"PRODUCTION"`. Defaults to `"PRODUCTION"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L117">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Cloud Bigtable instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L121">property numNodes</a>
</h3>

```typescript
numNodes?: pulumi.Input<number>;
```


The number of nodes in your Cloud Bigtable cluster. Minimum of `3` for a `PRODUCTION` instance. Cannot be set for a `DEVELOPMENT` instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L126">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L130">property storageType</a>
</h3>

```typescript
storageType?: pulumi.Input<string>;
```


The storage type to use. One of `"SSD"` or `"HDD"`. Defaults to `"SSD"`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/instance.ts#L134">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone to create the Cloud Bigtable cluster in. Zones that support Bigtable instances are noted on the [Cloud Bigtable locations page](https://cloud.google.com/bigtable/docs/locations).

<h2 class="pdoc-module-header" id="TableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L100">interface TableArgs</a>
</h2>

The set of arguments for constructing a Table resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L104">property instanceName</a>
</h3>

```typescript
instanceName: pulumi.Input<string>;
```


The name of the Bigtable instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L108">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L113">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L117">property splitKeys</a>
</h3>

```typescript
splitKeys?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of predefined keys to split the table on.

<h2 class="pdoc-module-header" id="TableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L77">interface TableState</a>
</h2>

Input properties used for looking up and filtering Table resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L81">property instanceName</a>
</h3>

```typescript
instanceName?: pulumi.Input<string>;
```


The name of the Bigtable instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L90">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigtable/table.ts#L94">property splitKeys</a>
</h3>

```typescript
splitKeys?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of predefined keys to split the table on.

