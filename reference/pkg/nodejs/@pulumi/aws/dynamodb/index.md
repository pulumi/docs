---
title: Module dynamodb
---

<a href="../index.html">@pulumi/aws</a> &gt; dynamodb

<h2 class="pdoc-module-header">Index</h2>

* <a href="#GlobalTable">class GlobalTable</a>
* <a href="#Table">class Table</a>
* <a href="#TableEventSubscription">class TableEventSubscription</a>
* <a href="#TableItem">class TableItem</a>
* <a href="#getTable">function getTable</a>
* <a href="#GetTableArgs">interface GetTableArgs</a>
* <a href="#GetTableResult">interface GetTableResult</a>
* <a href="#GlobalTableArgs">interface GlobalTableArgs</a>
* <a href="#GlobalTableState">interface GlobalTableState</a>
* <a href="#TableArgs">interface TableArgs</a>
* <a href="#TableEvent">interface TableEvent</a>
* <a href="#TableEventRecord">interface TableEventRecord</a>
* <a href="#TableEventSubscriptionArgs">interface TableEventSubscriptionArgs</a>
* <a href="#TableItemArgs">interface TableItemArgs</a>
* <a href="#TableItemState">interface TableItemState</a>
* <a href="#TableState">interface TableState</a>
* <a href="#TableEventHandler">type TableEventHandler</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts">dynamodb/dynamodbMixins.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts">dynamodb/getTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts">dynamodb/globalTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts">dynamodb/table.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts">dynamodb/tableItem.ts</a> 


<h2 class="pdoc-module-header" id="GlobalTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L12">class GlobalTable</a>
</h2>

Provides a resource to manage a DynamoDB Global Table. These are layered on top of existing DynamoDB Tables.

~> Note: There are many restrictions before you can properly create DynamoDB Global Tables in multiple regions. See the [AWS DynamoDB Global Table Requirements](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html) for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L36">constructor</a>
</h3>

```typescript
new GlobalTable(name: string, args: GlobalTableArgs, opts?: pulumi.CustomResourceOptions)
```


Create a GlobalTable resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: GlobalTableState): GlobalTable
```


Get an existing GlobalTable resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The ARN of the DynamoDB Global Table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L32">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the global table. Must match underlying DynamoDB Table names in all regions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L36">property replicas</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L12">class Table</a>
</h2>

Provides a DynamoDB table resource

~> **Note:** It is recommended to use `lifecycle` [`ignore_changes`](https://www.terraform.io/docs/configuration/resources.html#ignore_changes) for `read_capacity` and/or `write_capacity` if there's [autoscaling policy](https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html) attached to the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L100">constructor</a>
</h3>

```typescript
new Table(name: string, args: TableArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Table resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState): Table
```


Get an existing Table resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L28">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The arn of the table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L32">property attributes</a>
</h3>

```typescript
public attributes: pulumi.Output<{ ... }[]>;
```


List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L38">property globalSecondaryIndexes</a>
</h3>

```typescript
public globalSecondaryIndexes: pulumi.Output<{ ... }[] | undefined>;
```


Describe a GSO for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L43">property hashKey</a>
</h3>

```typescript
public hashKey: pulumi.Output<string>;
```


The name of the hash key in the index; must be
defined as an attribute in the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L49">property localSecondaryIndexes</a>
</h3>

```typescript
public localSecondaryIndexes: pulumi.Output<{ ... }[] | undefined>;
```


Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L57">property pointInTimeRecovery</a>
</h3>

```typescript
public pointInTimeRecovery: pulumi.Output<{ ... }>;
```


Point-in-time recovery options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L61">property rangeKey</a>
</h3>

```typescript
public rangeKey: pulumi.Output<string | undefined>;
```


The name of the range key; must be defined

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L65">property readCapacity</a>
</h3>

```typescript
public readCapacity: pulumi.Output<number>;
```


The number of read units for this index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L69">property serverSideEncryption</a>
</h3>

```typescript
public serverSideEncryption: pulumi.Output<{ ... }>;
```


Encrypt at rest options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L73">property streamArn</a>
</h3>

```typescript
public streamArn: pulumi.Output<string>;
```


The ARN of the Table Stream. Only available when `stream_enabled = true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L77">property streamEnabled</a>
</h3>

```typescript
public streamEnabled: pulumi.Output<boolean | undefined>;
```


Indicates whether Streams are to be enabled (true) or disabled (false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L84">property streamLabel</a>
</h3>

```typescript
public streamLabel: pulumi.Output<string>;
```


A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L88">property streamViewType</a>
</h3>

```typescript
public streamViewType: pulumi.Output<string>;
```


When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L92">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


A map of tags to populate on the created table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L96">property ttl</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L100">property writeCapacity</a>
</h3>

```typescript
public writeCapacity: pulumi.Output<number>;
```


The number of write units for this index

<h2 class="pdoc-module-header" id="TableEventSubscription">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L62">class TableEventSubscription</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L64">constructor</a>
</h3>

```typescript
new TableEventSubscription(name: string, table: table.Table, handler: TableEventHandler, args: TableEventSubscriptionArgs, opts?: pulumi.ComponentResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L12">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L135">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | Promise<Inputs> | Output<Inputs> | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L64">property eventSourceMapping</a>
</h3>

```typescript
public eventSourceMapping: lambda.EventSourceMapping;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L227">property func</a>
</h3>

```typescript
public func: LambdaFunction;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/lambda/lambdaMixins.ts#L226">property permission</a>
</h3>

```typescript
public permission: permission.Permission;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L63">property table</a>
</h3>

```typescript
public table: pulumi.Output<table.Table>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="TableItem">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L13">class TableItem</a>
</h2>

Provides a DynamoDB table item resource

-> **Note:** This resource is not meant to be used for managing large amounts of data in your table, it is not designed to scale.
  You should perform **regular backups** of all data in the table, see [AWS docs for more](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BackupRestore.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L42">constructor</a>
</h3>

```typescript
new TableItem(name: string, args: TableItemArgs, opts?: pulumi.CustomResourceOptions)
```


Create a TableItem resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableItemState): TableItem
```


Get an existing TableItem resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L29">property hashKey</a>
</h3>

```typescript
public hashKey: pulumi.Output<string>;
```


Hash key to use for lookups and identification of the item

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L34">property item</a>
</h3>

```typescript
public item: pulumi.Output<string>;
```


JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L38">property rangeKey</a>
</h3>

```typescript
public rangeKey: pulumi.Output<string | undefined>;
```


Range key to use for lookups and identification of the item. Required if there is range key defined in the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L42">property tableName</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L10">function getTable</a>
</h2>

```typescript
getTable(args: GetTableArgs, opts?: pulumi.InvokeOptions): Promise<GetTableResult>
```


Provides information about a DynamoDB table.

<h2 class="pdoc-module-header" id="GetTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L21">interface GetTableArgs</a>
</h2>

A collection of arguments for invoking getTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L25">property name</a>
</h3>

```typescript
name: string;
```


The name of the DynamoDB table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L26">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L27">property tags</a>
</h3>

```typescript
tags?: { ... };
```

<h2 class="pdoc-module-header" id="GetTableResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L33">interface GetTableResult</a>
</h2>

A collection of values returned by getTable.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L34">property arn</a>
</h3>

```typescript
arn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L35">property attributes</a>
</h3>

```typescript
attributes: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L36">property globalSecondaryIndexes</a>
</h3>

```typescript
globalSecondaryIndexes: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L37">property hashKey</a>
</h3>

```typescript
hashKey: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L52">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L38">property localSecondaryIndexes</a>
</h3>

```typescript
localSecondaryIndexes: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L39">property rangeKey</a>
</h3>

```typescript
rangeKey: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L40">property readCapacity</a>
</h3>

```typescript
readCapacity: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L41">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L42">property streamArn</a>
</h3>

```typescript
streamArn: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L43">property streamEnabled</a>
</h3>

```typescript
streamEnabled: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L44">property streamLabel</a>
</h3>

```typescript
streamLabel: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L45">property streamViewType</a>
</h3>

```typescript
streamViewType: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L46">property tags</a>
</h3>

```typescript
tags: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L47">property ttl</a>
</h3>

```typescript
ttl: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/getTable.ts#L48">property writeCapacity</a>
</h3>

```typescript
writeCapacity: number;
```

<h2 class="pdoc-module-header" id="GlobalTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L87">interface GlobalTableArgs</a>
</h2>

The set of arguments for constructing a GlobalTable resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L91">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the global table. Must match underlying DynamoDB Table names in all regions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L95">property replicas</a>
</h3>

```typescript
replicas: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Underlying DynamoDB Table. At least 1 replica must be defined. See below.

<h2 class="pdoc-module-header" id="GlobalTableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L69">interface GlobalTableState</a>
</h2>

Input properties used for looking up and filtering GlobalTable resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L73">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The ARN of the DynamoDB Global Table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L77">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the global table. Must match underlying DynamoDB Table names in all regions.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/globalTable.ts#L81">property replicas</a>
</h3>

```typescript
replicas?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Underlying DynamoDB Table. At least 1 replica must be defined. See below.

<h2 class="pdoc-module-header" id="TableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L252">interface TableArgs</a>
</h2>

The set of arguments for constructing a Table resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L256">property attributes</a>
</h3>

```typescript
attributes: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L262">property globalSecondaryIndexes</a>
</h3>

```typescript
globalSecondaryIndexes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Describe a GSO for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L267">property hashKey</a>
</h3>

```typescript
hashKey: pulumi.Input<string>;
```


The name of the hash key in the index; must be
defined as an attribute in the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L273">property localSecondaryIndexes</a>
</h3>

```typescript
localSecondaryIndexes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L277">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L281">property pointInTimeRecovery</a>
</h3>

```typescript
pointInTimeRecovery?: pulumi.Input<{ ... }>;
```


Point-in-time recovery options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L285">property rangeKey</a>
</h3>

```typescript
rangeKey?: pulumi.Input<string>;
```


The name of the range key; must be defined

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L289">property readCapacity</a>
</h3>

```typescript
readCapacity: pulumi.Input<number>;
```


The number of read units for this index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L293">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: pulumi.Input<{ ... }>;
```


Encrypt at rest options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L297">property streamEnabled</a>
</h3>

```typescript
streamEnabled?: pulumi.Input<boolean>;
```


Indicates whether Streams are to be enabled (true) or disabled (false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L301">property streamViewType</a>
</h3>

```typescript
streamViewType?: pulumi.Input<string>;
```


When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L305">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A map of tags to populate on the created table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L309">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<{ ... }>;
```


Defines ttl, has two properties, and can only be specified once:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L313">property writeCapacity</a>
</h3>

```typescript
writeCapacity: pulumi.Input<number>;
```


The number of write units for this index

<h2 class="pdoc-module-header" id="TableEvent">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L35">interface TableEvent</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L36">property Records</a>
</h3>

```typescript
Records: TableEventRecord[];
```

<h2 class="pdoc-module-header" id="TableEventRecord">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L39">interface TableEventRecord</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L40">property awsRegion</a>
</h3>

```typescript
awsRegion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L41">property dynamodb</a>
</h3>

```typescript
dynamodb: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L50">property eventID</a>
</h3>

```typescript
eventID: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L51">property eventName</a>
</h3>

```typescript
eventName: INSERT | MODIFY | REMOVE;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L52">property eventSource</a>
</h3>

```typescript
eventSource: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L53">property eventVersion</a>
</h3>

```typescript
eventVersion: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L54">property userIdentity</a>
</h3>

```typescript
userIdentity: { ... };
```

<h2 class="pdoc-module-header" id="TableEventSubscriptionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L23">interface TableEventSubscriptionArgs</a>
</h2>

Arguments to control the event rule subscription.  Currently empty, but still defined in case of
future need.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L27">property batchSize</a>
</h3>

```typescript
batchSize?: number;
```


The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to `100` for DynamoDB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L32">property startingPosition</a>
</h3>

```typescript
startingPosition: TRIM_HORIZON | LATEST;
```


The position in the stream where AWS Lambda should start reading. Must be one of either `TRIM_HORIZON` or `LATEST`.

<h2 class="pdoc-module-header" id="TableItemArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L106">interface TableItemArgs</a>
</h2>

The set of arguments for constructing a TableItem resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L110">property hashKey</a>
</h3>

```typescript
hashKey: pulumi.Input<string>;
```


Hash key to use for lookups and identification of the item

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L115">property item</a>
</h3>

```typescript
item: pulumi.Input<string>;
```


JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L119">property rangeKey</a>
</h3>

```typescript
rangeKey?: pulumi.Input<string>;
```


Range key to use for lookups and identification of the item. Required if there is range key defined in the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L123">property tableName</a>
</h3>

```typescript
tableName: pulumi.Input<string>;
```


The name of the table to contain the item.

<h2 class="pdoc-module-header" id="TableItemState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L83">interface TableItemState</a>
</h2>

Input properties used for looking up and filtering TableItem resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L87">property hashKey</a>
</h3>

```typescript
hashKey?: pulumi.Input<string>;
```


Hash key to use for lookups and identification of the item

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L92">property item</a>
</h3>

```typescript
item?: pulumi.Input<string>;
```


JSON representation of a map of attribute name/value pairs, one for each attribute.
Only the primary key attributes are required; you can optionally provide other attribute name-value pairs for the item.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L96">property rangeKey</a>
</h3>

```typescript
rangeKey?: pulumi.Input<string>;
```


Range key to use for lookups and identification of the item. Required if there is range key defined in the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/tableItem.ts#L100">property tableName</a>
</h3>

```typescript
tableName?: pulumi.Input<string>;
```


The name of the table to contain the item.

<h2 class="pdoc-module-header" id="TableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L170">interface TableState</a>
</h2>

Input properties used for looking up and filtering Table resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L174">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The arn of the table

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L178">property attributes</a>
</h3>

```typescript
attributes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L184">property globalSecondaryIndexes</a>
</h3>

```typescript
globalSecondaryIndexes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Describe a GSO for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L189">property hashKey</a>
</h3>

```typescript
hashKey?: pulumi.Input<string>;
```


The name of the hash key in the index; must be
defined as an attribute in the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L195">property localSecondaryIndexes</a>
</h3>

```typescript
localSecondaryIndexes?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L199">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L203">property pointInTimeRecovery</a>
</h3>

```typescript
pointInTimeRecovery?: pulumi.Input<{ ... }>;
```


Point-in-time recovery options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L207">property rangeKey</a>
</h3>

```typescript
rangeKey?: pulumi.Input<string>;
```


The name of the range key; must be defined

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L211">property readCapacity</a>
</h3>

```typescript
readCapacity?: pulumi.Input<number>;
```


The number of read units for this index

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L215">property serverSideEncryption</a>
</h3>

```typescript
serverSideEncryption?: pulumi.Input<{ ... }>;
```


Encrypt at rest options.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L219">property streamArn</a>
</h3>

```typescript
streamArn?: pulumi.Input<string>;
```


The ARN of the Table Stream. Only available when `stream_enabled = true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L223">property streamEnabled</a>
</h3>

```typescript
streamEnabled?: pulumi.Input<boolean>;
```


Indicates whether Streams are to be enabled (true) or disabled (false).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L230">property streamLabel</a>
</h3>

```typescript
streamLabel?: pulumi.Input<string>;
```


A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L234">property streamViewType</a>
</h3>

```typescript
streamViewType?: pulumi.Input<string>;
```


When an item in the table is modified, StreamViewType determines what information is written to the table's stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L238">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A map of tags to populate on the created table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L242">property ttl</a>
</h3>

```typescript
ttl?: pulumi.Input<{ ... }>;
```


Defines ttl, has two properties, and can only be specified once:

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/table.ts#L246">property writeCapacity</a>
</h3>

```typescript
writeCapacity?: pulumi.Input<number>;
```


The number of write units for this index

<h2 class="pdoc-module-header" id="TableEventHandler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/dynamodb/dynamodbMixins.ts#L60">type TableEventHandler</a>
</h2>

```typescript
type TableEventHandler = lambda.EventHandler<TableEvent, void>;
```

