---
title: Module dynamodb
---

<a href="../index.html">@pulumi/aws</a> &gt; dynamodb

<h2 class="pdoc-module-header">Index</h2>

* <a href="#GlobalTable">class GlobalTable</a>
* <a href="#Table">class Table</a>
* <a href="#TableItem">class TableItem</a>
* <a href="#getTable">function getTable</a>
* <a href="#GetTableArgs">interface GetTableArgs</a>
* <a href="#GetTableResult">interface GetTableResult</a>
* <a href="#GlobalTableArgs">interface GlobalTableArgs</a>
* <a href="#GlobalTableState">interface GlobalTableState</a>
* <a href="#TableArgs">interface TableArgs</a>
* <a href="#TableItemArgs">interface TableItemArgs</a>
* <a href="#TableItemState">interface TableItemState</a>
* <a href="#TableState">interface TableState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts">dynamodb/getTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts">dynamodb/globalTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts">dynamodb/table.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts">dynamodb/tableItem.ts</a> 


<h2 class="pdoc-module-header" id="GlobalTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L11">class GlobalTable</a>
</h2>

Provides a resource to manage a DynamoDB Global Table. These are layered on top of existing DynamoDB Tables.

~> Note: There are many restrictions before you can properly create DynamoDB Global Tables in multiple regions. See the [AWS DynamoDB Global Table Requirements](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L35">constructor</a>
</h3>

```typescript
new GlobalTable(name: string, args: GlobalTableArgs, opts?: pulumi.ResourceOptions)
```


Create a GlobalTable resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GlobalTableState): GlobalTable
```


Get an existing GlobalTable resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the DynamoDB Global Table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the global table. Must match underlying DynamoDB Table names in all regions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L35">property replicas</a>
</h3>

```typescript
public replicas: pulumi.Output<{ ... }[]>;
```


Underlying DynamoDB Table. At least 1 replica must be defined. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Table">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L11">class Table</a>
</h2>

Provides a DynamoDB table resource

~> **Note:** It is recommended to use `lifecycle` [`ignore_changes`](/docs/configuration/resources.html#ignore_changes) for `read_capacity` and/or `write_capacity` if there's [autoscaling policy](/docs/providers/aws/r/appautoscaling_policy.html) attached to the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L99">constructor</a>
</h3>

```typescript
new Table(name: string, args: TableArgs, opts?: pulumi.ResourceOptions)
```


Create a Table resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState): Table
```


Get an existing Table resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L27">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The arn of the table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L31">property attributes</a>
</h3>

```typescript
public attributes: pulumi.Output<{ ... }[]>;
```


List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L37">property globalSecondaryIndexes</a>
</h3>

```typescript
public globalSecondaryIndexes: pulumi.Output<{ ... }[] | undefined>;
```


Describe a GSO for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L42">property hashKey</a>
</h3>

```typescript
public hashKey: pulumi.Output<string>;
```


The name of the hash key in the index; must be
defined as an attribute in the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L48">property localSecondaryIndexes</a>
</h3>

```typescript
public localSecondaryIndexes: pulumi.Output<{ ... }[] | undefined>;
```


Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L52">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L56">property pointInTimeRecovery</a>
</h3>

```typescript
public pointInTimeRecovery: pulumi.Output<{ ... }>;
```


Point-in-time recovery options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L60">property rangeKey</a>
</h3>

```typescript
public rangeKey: pulumi.Output<string | undefined>;
```


The name of the range key; must be defined

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L64">property readCapacity</a>
</h3>

```typescript
public readCapacity: pulumi.Output<number>;
```


The number of read units for this index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L68">property serverSideEncryption</a>
</h3>

```typescript
public serverSideEncryption: pulumi.Output<{ ... }>;
```


Encrypt at rest options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L72">property streamArn</a>
</h3>

```typescript
public streamArn: pulumi.Output<string>;
```


The ARN of the Table Stream. Only available when `stream_enabled = true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L76">property streamEnabled</a>
</h3>

```typescript
public streamEnabled: pulumi.Output<boolean | undefined>;
```


Indicates whether Streams are to be enabled (true) or disabled (false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L83">property streamLabel</a>
</h3>

```typescript
public streamLabel: pulumi.Output<string>;
```


A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L87">property streamViewType</a>
</h3>

```typescript
public streamViewType: pulumi.Output<string>;
```


When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L91">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A map of tags to populate on the created table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L95">property ttl</a>
</h3>

```typescript
public ttl: pulumi.Output<{ ... } | undefined>;
```


Defines ttl, has two properties, and can only be specified once:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L99">property writeCapacity</a>
</h3>

```typescript
public writeCapacity: pulumi.Output<number>;
```


The number of write units for this index

<h2 class="pdoc-module-header" id="TableItem">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L12">class TableItem</a>
</h2>

Provides a DynamoDB table item resource

-> **Note:** This resource is not meant to be used for managing large amounts of data in your table, it is not designed to scale.
  You should perform **regular backups** of all data in the table, see [AWS docs for more](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L41">constructor</a>
</h3>

```typescript
new TableItem(name: string, args: TableItemArgs, opts?: pulumi.ResourceOptions)
```


Create a TableItem resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableItemState): TableItem
```


Get an existing TableItem resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L28">property hashKey</a>
</h3>

```typescript
public hashKey: pulumi.Output<string>;
```


Hash key to use for lookups and identification of the item

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L33">property item</a>
</h3>

```typescript
public item: pulumi.Output<string>;
```


JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L37">property rangeKey</a>
</h3>

```typescript
public rangeKey: pulumi.Output<string | undefined>;
```


Range key to use for lookups and identification of the item. Required if there is range key defined in the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L41">property tableName</a>
</h3>

```typescript
public tableName: pulumi.Output<string>;
```


The name of the table to contain the item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L9">function getTable</a>
</h2>

```typescript
getTable(args: GetTableArgs): Promise<GetTableResult>
```


Provides information about a DynamoDB table.

<h2 class="pdoc-module-header" id="GetTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L20">interface GetTableArgs</a>
</h2>

A collection of arguments for invoking getTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L24">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the DynamoDB table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L25">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L26">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="GetTableResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L32">interface GetTableResult</a>
</h2>

A collection of values returned by getTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L33">property arn</a>
</h3>

```typescript
arn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L34">property attributes</a>
</h3>

```typescript
attributes: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L35">property globalSecondaryIndexes</a>
</h3>

```typescript
globalSecondaryIndexes: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L36">property hashKey</a>
</h3>

```typescript
hashKey: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L51">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L37">property localSecondaryIndexes</a>
</h3>

```typescript
localSecondaryIndexes: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L38">property rangeKey</a>
</h3>

```typescript
rangeKey: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L39">property readCapacity</a>
</h3>

```typescript
readCapacity: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L40">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L41">property streamArn</a>
</h3>

```typescript
streamArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L42">property streamEnabled</a>
</h3>

```typescript
streamEnabled: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L43">property streamLabel</a>
</h3>

```typescript
streamLabel: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L44">property streamViewType</a>
</h3>

```typescript
streamViewType: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L45">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L46">property ttl</a>
</h3>

```typescript
ttl: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L47">property writeCapacity</a>
</h3>

```typescript
writeCapacity: number;
```

<h2 class="pdoc-module-header" id="GlobalTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L86">interface GlobalTableArgs</a>
</h2>

The set of arguments for constructing a GlobalTable resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L90">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the global table. Must match underlying DynamoDB Table names in all regions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L94">property replicas</a>
</h3>

```typescript
replicas: pulumi.Input<{ ... }[]>;
```


Underlying DynamoDB Table. At least 1 replica must be defined. See below.

<h2 class="pdoc-module-header" id="GlobalTableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L68">interface GlobalTableState</a>
</h2>

Input properties used for looking up and filtering GlobalTable resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L72">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the DynamoDB Global Table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L76">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the global table. Must match underlying DynamoDB Table names in all regions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L80">property replicas</a>
</h3>

```typescript
replicas?: pulumi.Input<{ ... }[]>;
```


Underlying DynamoDB Table. At least 1 replica must be defined. See below.

<h2 class="pdoc-module-header" id="TableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L251">interface TableArgs</a>
</h2>

The set of arguments for constructing a Table resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L255">property attributes</a>
</h3>

```typescript
attributes: pulumi.Input<{ ... }[]>;
```


List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L261">property globalSecondaryIndexes</a>
</h3>

```typescript
globalSecondaryIndexes?: pulumi.Input<{ ... }[]>;
```


Describe a GSO for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L266">property hashKey</a>
</h3>

```typescript
hashKey: pulumi.Input<string>;
```


The name of the hash key in the index; must be
defined as an attribute in the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L272">property localSecondaryIndexes</a>
</h3>

```typescript
localSecondaryIndexes?: pulumi.Input<{ ... }[]>;
```


Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L276">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L280">property pointInTimeRecovery</a>
</h3>

```typescript
pointInTimeRecovery?: pulumi.Input<{ ... }>;
```


Point-in-time recovery options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L284">property rangeKey</a>
</h3>

```typescript
rangeKey?: pulumi.Input<string>;
```


The name of the range key; must be defined

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L288">property readCapacity</a>
</h3>

```typescript
readCapacity: pulumi.Input<number>;
```


The number of read units for this index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L292">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: pulumi.Input<{ ... }>;
```


Encrypt at rest options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L296">property streamEnabled</a>
</h3>

```typescript
streamEnabled?: pulumi.Input<boolean>;
```


Indicates whether Streams are to be enabled (true) or disabled (false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L300">property streamViewType</a>
</h3>

```typescript
streamViewType?: pulumi.Input<string>;
```


When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L304">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A map of tags to populate on the created table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L308">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<{ ... }>;
```


Defines ttl, has two properties, and can only be specified once:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L312">property writeCapacity</a>
</h3>

```typescript
writeCapacity: pulumi.Input<number>;
```


The number of write units for this index

<h2 class="pdoc-module-header" id="TableItemArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L105">interface TableItemArgs</a>
</h2>

The set of arguments for constructing a TableItem resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L109">property hashKey</a>
</h3>

```typescript
hashKey: pulumi.Input<string>;
```


Hash key to use for lookups and identification of the item

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L114">property item</a>
</h3>

```typescript
item: pulumi.Input<string>;
```


JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L118">property rangeKey</a>
</h3>

```typescript
rangeKey?: pulumi.Input<string>;
```


Range key to use for lookups and identification of the item. Required if there is range key defined in the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L122">property tableName</a>
</h3>

```typescript
tableName: pulumi.Input<string>;
```


The name of the table to contain the item.

<h2 class="pdoc-module-header" id="TableItemState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L82">interface TableItemState</a>
</h2>

Input properties used for looking up and filtering TableItem resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L86">property hashKey</a>
</h3>

```typescript
hashKey?: pulumi.Input<string>;
```


Hash key to use for lookups and identification of the item

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L91">property item</a>
</h3>

```typescript
item?: pulumi.Input<string>;
```


JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L95">property rangeKey</a>
</h3>

```typescript
rangeKey?: pulumi.Input<string>;
```


Range key to use for lookups and identification of the item. Required if there is range key defined in the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L99">property tableName</a>
</h3>

```typescript
tableName?: pulumi.Input<string>;
```


The name of the table to contain the item.

<h2 class="pdoc-module-header" id="TableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L169">interface TableState</a>
</h2>

Input properties used for looking up and filtering Table resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L173">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The arn of the table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L177">property attributes</a>
</h3>

```typescript
attributes?: pulumi.Input<{ ... }[]>;
```


List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L183">property globalSecondaryIndexes</a>
</h3>

```typescript
globalSecondaryIndexes?: pulumi.Input<{ ... }[]>;
```


Describe a GSO for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L188">property hashKey</a>
</h3>

```typescript
hashKey?: pulumi.Input<string>;
```


The name of the hash key in the index; must be
defined as an attribute in the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L194">property localSecondaryIndexes</a>
</h3>

```typescript
localSecondaryIndexes?: pulumi.Input<{ ... }[]>;
```


Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L198">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L202">property pointInTimeRecovery</a>
</h3>

```typescript
pointInTimeRecovery?: pulumi.Input<{ ... }>;
```


Point-in-time recovery options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L206">property rangeKey</a>
</h3>

```typescript
rangeKey?: pulumi.Input<string>;
```


The name of the range key; must be defined

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L210">property readCapacity</a>
</h3>

```typescript
readCapacity?: pulumi.Input<number>;
```


The number of read units for this index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L214">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: pulumi.Input<{ ... }>;
```


Encrypt at rest options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L218">property streamArn</a>
</h3>

```typescript
streamArn?: pulumi.Input<string>;
```


The ARN of the Table Stream. Only available when `stream_enabled = true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L222">property streamEnabled</a>
</h3>

```typescript
streamEnabled?: pulumi.Input<boolean>;
```


Indicates whether Streams are to be enabled (true) or disabled (false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L229">property streamLabel</a>
</h3>

```typescript
streamLabel?: pulumi.Input<string>;
```


A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L233">property streamViewType</a>
</h3>

```typescript
streamViewType?: pulumi.Input<string>;
```


When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L237">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A map of tags to populate on the created table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L241">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<{ ... }>;
```


Defines ttl, has two properties, and can only be specified once:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L245">property writeCapacity</a>
</h3>

```typescript
writeCapacity?: pulumi.Input<number>;
```


The number of write units for this index

