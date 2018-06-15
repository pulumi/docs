---
title: Module bigquery
---

<a href="../index.html">@pulumi/gcp</a> &gt; bigquery

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Dataset">class Dataset</a>
* <a href="#Table">class Table</a>
* <a href="#DatasetArgs">interface DatasetArgs</a>
* <a href="#DatasetState">interface DatasetState</a>
* <a href="#TableArgs">interface TableArgs</a>
* <a href="#TableState">interface TableState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts">bigquery/dataset.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts">bigquery/table.ts</a> 


<h2 class="pdoc-module-header" id="Dataset">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L12">class Dataset</a>
</h2>

Creates a dataset resource for Google BigQuery. For more information see
[the official documentation](https://cloud.google.com/bigquery/docs/) and
[API](https://cloud.google.com/bigquery/docs/reference/rest/v2/datasets).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L74">constructor</a>
</h3>

```typescript
new Dataset(name: string, args: DatasetArgs, opts?: pulumi.ResourceOptions)
```


Create a Dataset resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DatasetState): Dataset
```


Get an existing Dataset resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L28">property creationTime</a>
</h3>

```typescript
public creationTime: pulumi.Output<number>;
```


The time when this dataset was created, in milliseconds since the epoch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L33">property datasetId</a>
</h3>

```typescript
public datasetId: pulumi.Output<string>;
```


A unique ID for the resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L39">property defaultTableExpirationMs</a>
</h3>

```typescript
public defaultTableExpirationMs: pulumi.Output<number | undefined>;
```


The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L43">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A user-friendly description of the dataset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L47">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


A hash of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L51">property friendlyName</a>
</h3>

```typescript
public friendlyName: pulumi.Output<string | undefined>;
```


A descriptive name for the dataset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L55">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A mapping of labels to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L60">property lastModifiedTime</a>
</h3>

```typescript
public lastModifiedTime: pulumi.Output<number>;
```


The date when this dataset or any of its tables was last modified,
in milliseconds since the epoch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L65">property location</a>
</h3>

```typescript
public location: pulumi.Output<string | undefined>;
```


The geographic location where the dataset should reside.
See [official docs](https://cloud.google.com/bigquery/docs/dataset-locations).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L70">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L74">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Table">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L12">class Table</a>
</h2>

Creates a table resource in a dataset for Google BigQuery. For more information see
[the official documentation](https://cloud.google.com/bigquery/docs/) and
[API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L109">constructor</a>
</h3>

```typescript
new Table(name: string, args: TableArgs, opts?: pulumi.ResourceOptions)
```


Create a Table resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState): Table
```


Get an existing Table resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L28">property creationTime</a>
</h3>

```typescript
public creationTime: pulumi.Output<number>;
```


The time when this table was created, in milliseconds since the epoch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L33">property datasetId</a>
</h3>

```typescript
public datasetId: pulumi.Output<string>;
```


The dataset ID to create the table in.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The field description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L41">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


A hash of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L48">property expirationTime</a>
</h3>

```typescript
public expirationTime: pulumi.Output<number>;
```


The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L52">property friendlyName</a>
</h3>

```typescript
public friendlyName: pulumi.Output<string | undefined>;
```


A descriptive name for the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L56">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


A mapping of labels to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L60">property lastModifiedTime</a>
</h3>

```typescript
public lastModifiedTime: pulumi.Output<number>;
```


The time when this table was last modified, in milliseconds since the epoch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L64">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The geographic location where the table resides. This value is inherited from the dataset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L68">property numBytes</a>
</h3>

```typescript
public numBytes: pulumi.Output<number>;
```


The size of this table in bytes, excluding any data in the streaming buffer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L72">property numLongTermBytes</a>
</h3>

```typescript
public numLongTermBytes: pulumi.Output<number>;
```


The number of bytes in the table that are considered "long-term storage".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L76">property numRows</a>
</h3>

```typescript
public numRows: pulumi.Output<number>;
```


The number of rows of data in this table, excluding any data in the streaming buffer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L81">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L85">property schema</a>
</h3>

```typescript
public schema: pulumi.Output<string>;
```


A JSON schema for the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L89">property selfLink</a>
</h3>

```typescript
public selfLink: pulumi.Output<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L94">property tableId</a>
</h3>

```typescript
public tableId: pulumi.Output<string>;
```


A unique ID for the resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L99">property timePartitioning</a>
</h3>

```typescript
public timePartitioning: pulumi.Output<{ ... } | undefined>;
```


If specified, configures time-based
partitioning for this table. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L104">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The only type supported is DAY, which will generate
one partition per day based on data loading time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L109">property view</a>
</h3>

```typescript
public view: pulumi.Output<{ ... } | undefined>;
```


If specified, configures this table as a view.
Structure is documented below.

<h2 class="pdoc-module-header" id="DatasetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L179">interface DatasetArgs</a>
</h2>

The set of arguments for constructing a Dataset resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L184">property datasetId</a>
</h3>

```typescript
datasetId: pulumi.Input<string>;
```


A unique ID for the resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L190">property defaultTableExpirationMs</a>
</h3>

```typescript
defaultTableExpirationMs?: pulumi.Input<number>;
```


The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L194">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A user-friendly description of the dataset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L198">property friendlyName</a>
</h3>

```typescript
friendlyName?: pulumi.Input<string>;
```


A descriptive name for the dataset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L202">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A mapping of labels to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L207">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The geographic location where the dataset should reside.
See [official docs](https://cloud.google.com/bigquery/docs/dataset-locations).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L212">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="DatasetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L123">interface DatasetState</a>
</h2>

Input properties used for looking up and filtering Dataset resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L127">property creationTime</a>
</h3>

```typescript
creationTime?: pulumi.Input<number>;
```


The time when this dataset was created, in milliseconds since the epoch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L132">property datasetId</a>
</h3>

```typescript
datasetId?: pulumi.Input<string>;
```


A unique ID for the resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L138">property defaultTableExpirationMs</a>
</h3>

```typescript
defaultTableExpirationMs?: pulumi.Input<number>;
```


The default lifetime of all
tables in the dataset, in milliseconds. The minimum value is 3600000
milliseconds (one hour).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L142">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A user-friendly description of the dataset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L146">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


A hash of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L150">property friendlyName</a>
</h3>

```typescript
friendlyName?: pulumi.Input<string>;
```


A descriptive name for the dataset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L154">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A mapping of labels to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L159">property lastModifiedTime</a>
</h3>

```typescript
lastModifiedTime?: pulumi.Input<number>;
```


The date when this dataset or any of its tables was last modified,
in milliseconds since the epoch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L164">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The geographic location where the dataset should reside.
See [official docs](https://cloud.google.com/bigquery/docs/dataset-locations).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L169">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/dataset.ts#L173">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h2 class="pdoc-module-header" id="TableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L268">interface TableArgs</a>
</h2>

The set of arguments for constructing a Table resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L273">property datasetId</a>
</h3>

```typescript
datasetId: pulumi.Input<string>;
```


The dataset ID to create the table in.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L277">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The field description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L284">property expirationTime</a>
</h3>

```typescript
expirationTime?: pulumi.Input<number>;
```


The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L288">property friendlyName</a>
</h3>

```typescript
friendlyName?: pulumi.Input<string>;
```


A descriptive name for the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L292">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A mapping of labels to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L297">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L301">property schema</a>
</h3>

```typescript
schema?: pulumi.Input<string>;
```


A JSON schema for the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L306">property tableId</a>
</h3>

```typescript
tableId: pulumi.Input<string>;
```


A unique ID for the resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L311">property timePartitioning</a>
</h3>

```typescript
timePartitioning?: pulumi.Input<{ ... }>;
```


If specified, configures time-based
partitioning for this table. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L316">property view</a>
</h3>

```typescript
view?: pulumi.Input<{ ... }>;
```


If specified, configures this table as a view.
Structure is documented below.

<h2 class="pdoc-module-header" id="TableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L177">interface TableState</a>
</h2>

Input properties used for looking up and filtering Table resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L181">property creationTime</a>
</h3>

```typescript
creationTime?: pulumi.Input<number>;
```


The time when this table was created, in milliseconds since the epoch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L186">property datasetId</a>
</h3>

```typescript
datasetId?: pulumi.Input<string>;
```


The dataset ID to create the table in.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L190">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The field description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L194">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


A hash of the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L201">property expirationTime</a>
</h3>

```typescript
expirationTime?: pulumi.Input<number>;
```


The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L205">property friendlyName</a>
</h3>

```typescript
friendlyName?: pulumi.Input<string>;
```


A descriptive name for the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L209">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


A mapping of labels to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L213">property lastModifiedTime</a>
</h3>

```typescript
lastModifiedTime?: pulumi.Input<number>;
```


The time when this table was last modified, in milliseconds since the epoch.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L217">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The geographic location where the table resides. This value is inherited from the dataset.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L221">property numBytes</a>
</h3>

```typescript
numBytes?: pulumi.Input<number>;
```


The size of this table in bytes, excluding any data in the streaming buffer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L225">property numLongTermBytes</a>
</h3>

```typescript
numLongTermBytes?: pulumi.Input<number>;
```


The number of bytes in the table that are considered "long-term storage".

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L229">property numRows</a>
</h3>

```typescript
numRows?: pulumi.Input<number>;
```


The number of rows of data in this table, excluding any data in the streaming buffer.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L234">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L238">property schema</a>
</h3>

```typescript
schema?: pulumi.Input<string>;
```


A JSON schema for the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L242">property selfLink</a>
</h3>

```typescript
selfLink?: pulumi.Input<string>;
```


The URI of the created resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L247">property tableId</a>
</h3>

```typescript
tableId?: pulumi.Input<string>;
```


A unique ID for the resource.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L252">property timePartitioning</a>
</h3>

```typescript
timePartitioning?: pulumi.Input<{ ... }>;
```


If specified, configures time-based
partitioning for this table. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L257">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The only type supported is DAY, which will generate
one partition per day based on data loading time.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/bigquery/table.ts#L262">property view</a>
</h3>

```typescript
view?: pulumi.Input<{ ... }>;
```


If specified, configures this table as a view.
Structure is documented below.

