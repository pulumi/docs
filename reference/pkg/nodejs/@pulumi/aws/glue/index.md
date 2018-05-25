---
title: Module glue
---

<a href="..">@pulumi/aws</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#CatalogDatabase">class CatalogDatabase</a>
* <a href="#CatalogDatabaseArgs">interface CatalogDatabaseArgs</a>
* <a href="#CatalogDatabaseState">interface CatalogDatabaseState</a>

<a href="/glue/catalogDatabase.ts">glue/catalogDatabase.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="CatalogDatabase">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L9">class CatalogDatabase</a>
</h2>

Provides a Glue Catalog Database Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L41">constructor</a>
</h3>

```typescript
new CatalogDatabase(name: string, args?: CatalogDatabaseArgs, opts?: pulumi.ResourceOptions)
```


Create a CatalogDatabase resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new CatalogDatabase(name: string, state?: CatalogDatabaseState, opts?: pulumi.ResourceOptions)
```


Create a CatalogDatabase resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CatalogDatabaseState): CatalogDatabase
```


Get an existing CatalogDatabase resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L25">property catalogId</a>
</h3>

```typescript
public catalogId: pulumi.Output<string>;
```


ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L33">property locationUri</a>
</h3>

```typescript
public locationUri: pulumi.Output<string | undefined>;
```


The location of the database (for example, an HDFS path).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L41">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... } | undefined>;
```


A list of key-value pairs that define parameters and properties of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CatalogDatabaseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L103">interface CatalogDatabaseArgs</a>
</h2>

The set of arguments for constructing a CatalogDatabase resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L107">property catalogId</a>
</h3>

```typescript
catalogId?: pulumi.Input<string>;
```


ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L111">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L115">property locationUri</a>
</h3>

```typescript
locationUri?: pulumi.Input<string>;
```


The location of the database (for example, an HDFS path).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L123">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A list of key-value pairs that define parameters and properties of the database.

<h2 class="pdoc-module-header" id="CatalogDatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L77">interface CatalogDatabaseState</a>
</h2>

Input properties used for looking up and filtering CatalogDatabase resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L81">property catalogId</a>
</h3>

```typescript
catalogId?: pulumi.Input<string>;
```


ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L85">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L89">property locationUri</a>
</h3>

```typescript
locationUri?: pulumi.Input<string>;
```


The location of the database (for example, an HDFS path).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/pack/nodejs/glue/catalogDatabase.ts#L97">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A list of key-value pairs that define parameters and properties of the database.

