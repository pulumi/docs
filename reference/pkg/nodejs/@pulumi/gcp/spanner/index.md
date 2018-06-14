---
title: Module spanner
---

<a href="../index.html">@pulumi/gcp</a> &gt; spanner

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Database">class Database</a>
* <a href="#Instance">class Instance</a>
* <a href="#DatabaseArgs">interface DatabaseArgs</a>
* <a href="#DatabaseState">interface DatabaseState</a>
* <a href="#InstanceArgs">interface InstanceArgs</a>
* <a href="#InstanceState">interface InstanceState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts">spanner/database.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts">spanner/instance.ts</a> 


<h2 class="pdoc-module-header" id="Database">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L9">class Database</a>
</h2>

Creates a Google Spanner Database within a Spanner Instance. For more information, see the [official documentation](https://cloud.google.com/spanner/), or the [JSON API](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L45">constructor</a>
</h3>

```typescript
new Database(name: string, args: DatabaseArgs, opts?: pulumi.ResourceOptions)
```


Create a Database resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatabaseState): Database
```


Get an existing Database resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L28">property ddls</a>
</h3>

```typescript
public ddls: pulumi.Output<string[] | undefined>;
```


An optional list of DDL statements to run inside the newly created
database. Statements can create tables, indexes, etc. These statements execute atomically
with the creation of the database: if there is an error in any statement, the database
is not created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L32">property instance</a>
</h3>

```typescript
public instance: pulumi.Output<string>;
```


The name of the instance that will serve the new database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L41">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which to look for the `instance` specified. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L45">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The current state of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Instance">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L9">class Instance</a>
</h2>

Creates and manages a Google Spanner Instance. For more information, see the [official documentation](https://cloud.google.com/spanner/), or the [JSON API](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L59">constructor</a>
</h3>

```typescript
new Instance(name: string, args: InstanceArgs, opts?: pulumi.ResourceOptions)
```


Create a Instance resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceState): Instance
```


Get an existing Instance resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L30">property config</a>
</h3>

```typescript
public config: pulumi.Output<string>;
```


The name of the instance's configuration (similar but not
quite the same as a region) which defines defines the geographic placement and
replication of your databases in this instance. It determines where your data
is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
In order to obtain a valid list please consult the
[Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L35">property displayName</a>
</h3>

```typescript
public displayName: pulumi.Output<string>;
```


The descriptive name for this instance as it appears
in UIs. Can be updated, however should be kept globally unique to avoid confusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L39">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A mapping (key/value pairs) of labels to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The unique name (ID) of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L50">property numNodes</a>
</h3>

```typescript
public numNodes: pulumi.Output<number | undefined>;
```


The number of nodes allocated to this instance.
Defaults to `1`. This can be updated after creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L55">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L59">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The current state of the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="DatabaseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L112">interface DatabaseArgs</a>
</h2>

The set of arguments for constructing a Database resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L119">property ddls</a>
</h3>

```typescript
ddls?: pulumi.Input<pulumi.Input<string>[]>;
```


An optional list of DDL statements to run inside the newly created
database. Statements can create tables, indexes, etc. These statements execute atomically
with the creation of the database: if there is an error in any statement, the database
is not created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L123">property instance</a>
</h3>

```typescript
instance: pulumi.Input<string>;
```


The name of the instance that will serve the new database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L127">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L132">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which to look for the `instance` specified. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="DatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L82">interface DatabaseState</a>
</h2>

Input properties used for looking up and filtering Database resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L89">property ddls</a>
</h3>

```typescript
ddls?: pulumi.Input<pulumi.Input<string>[]>;
```


An optional list of DDL statements to run inside the newly created
database. Statements can create tables, indexes, etc. These statements execute atomically
with the creation of the database: if there is an error in any statement, the database
is not created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L93">property instance</a>
</h3>

```typescript
instance?: pulumi.Input<string>;
```


The name of the instance that will serve the new database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L102">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which to look for the `instance` specified. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/database.ts#L106">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The current state of the database.

<h2 class="pdoc-module-header" id="InstanceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L147">interface InstanceArgs</a>
</h2>

The set of arguments for constructing a Instance resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L156">property config</a>
</h3>

```typescript
config: pulumi.Input<string>;
```


The name of the instance's configuration (similar but not
quite the same as a region) which defines defines the geographic placement and
replication of your databases in this instance. It determines where your data
is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
In order to obtain a valid list please consult the
[Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L161">property displayName</a>
</h3>

```typescript
displayName: pulumi.Input<string>;
```


The descriptive name for this instance as it appears
in UIs. Can be updated, however should be kept globally unique to avoid confusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L165">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A mapping (key/value pairs) of labels to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The unique name (ID) of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L176">property numNodes</a>
</h3>

```typescript
numNodes?: pulumi.Input<number>;
```


The number of nodes allocated to this instance.
Defaults to `1`. This can be updated after creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L181">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="InstanceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L103">interface InstanceState</a>
</h2>

Input properties used for looking up and filtering Instance resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L112">property config</a>
</h3>

```typescript
config?: pulumi.Input<string>;
```


The name of the instance's configuration (similar but not
quite the same as a region) which defines defines the geographic placement and
replication of your databases in this instance. It determines where your data
is stored. Values are typically of the form `regional-europe-west1` , `us-central` etc.
In order to obtain a valid list please consult the
[Configuration section of the docs](https://cloud.google.com/spanner/docs/instances).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L117">property displayName</a>
</h3>

```typescript
displayName?: pulumi.Input<string>;
```


The descriptive name for this instance as it appears
in UIs. Can be updated, however should be kept globally unique to avoid confusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L121">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A mapping (key/value pairs) of labels to assign to the instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L127">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The unique name (ID) of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L132">property numNodes</a>
</h3>

```typescript
numNodes?: pulumi.Input<number>;
```


The number of nodes allocated to this instance.
Defaults to `1`. This can be updated after creation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L137">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/spanner/instance.ts#L141">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The current state of the instance.

