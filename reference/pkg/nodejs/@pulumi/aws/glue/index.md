---
title: Module glue
---

<a href="../index.html">@pulumi/aws</a> &gt; glue

<h2 class="pdoc-module-header">Index</h2>

* <a href="#CatalogDatabase">class CatalogDatabase</a>
* <a href="#CatalogTable">class CatalogTable</a>
* <a href="#Classifier">class Classifier</a>
* <a href="#Connection">class Connection</a>
* <a href="#Crawler">class Crawler</a>
* <a href="#Job">class Job</a>
* <a href="#Trigger">class Trigger</a>
* <a href="#getScript">function getScript</a>
* <a href="#CatalogDatabaseArgs">interface CatalogDatabaseArgs</a>
* <a href="#CatalogDatabaseState">interface CatalogDatabaseState</a>
* <a href="#CatalogTableArgs">interface CatalogTableArgs</a>
* <a href="#CatalogTableState">interface CatalogTableState</a>
* <a href="#ClassifierArgs">interface ClassifierArgs</a>
* <a href="#ClassifierState">interface ClassifierState</a>
* <a href="#ConnectionArgs">interface ConnectionArgs</a>
* <a href="#ConnectionState">interface ConnectionState</a>
* <a href="#CrawlerArgs">interface CrawlerArgs</a>
* <a href="#CrawlerState">interface CrawlerState</a>
* <a href="#GetScriptArgs">interface GetScriptArgs</a>
* <a href="#GetScriptResult">interface GetScriptResult</a>
* <a href="#JobArgs">interface JobArgs</a>
* <a href="#JobState">interface JobState</a>
* <a href="#TriggerArgs">interface TriggerArgs</a>
* <a href="#TriggerState">interface TriggerState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts">glue/catalogDatabase.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts">glue/catalogTable.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts">glue/classifier.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts">glue/connection.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts">glue/crawler.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts">glue/getScript.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts">glue/job.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts">glue/trigger.ts</a> 


<h2 class="pdoc-module-header" id="CatalogDatabase">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L9">class CatalogDatabase</a>
</h2>

Provides a Glue Catalog Database Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L41">constructor</a>
</h3>

```typescript
new CatalogDatabase(name: string, args?: CatalogDatabaseArgs, opts?: pulumi.ResourceOptions)
```


Create a CatalogDatabase resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CatalogDatabaseState): CatalogDatabase
```


Get an existing CatalogDatabase resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L25">property catalogId</a>
</h3>

```typescript
public catalogId: pulumi.Output<string>;
```


ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L33">property locationUri</a>
</h3>

```typescript
public locationUri: pulumi.Output<string | undefined>;
```


The location of the database (for example, an HDFS path).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L41">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... } | undefined>;
```


A list of key-value pairs that define parameters and properties of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CatalogTable">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L9">class CatalogTable</a>
</h2>

Provides a Glue Catalog Table Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L69">constructor</a>
</h3>

```typescript
new CatalogTable(name: string, args: CatalogTableArgs, opts?: pulumi.ResourceOptions)
```


Create a CatalogTable resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CatalogTableState): CatalogTable
```


Get an existing CatalogTable resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L25">property catalogId</a>
</h3>

```typescript
public catalogId: pulumi.Output<string>;
```


ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L29">property databaseName</a>
</h3>

```typescript
public databaseName: pulumi.Output<string>;
```


Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L33">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the SerDe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L41">property owner</a>
</h3>

```typescript
public owner: pulumi.Output<string | undefined>;
```


Owner of the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L45">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... } | undefined>;
```


Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L49">property partitionKeys</a>
</h3>

```typescript
public partitionKeys: pulumi.Output<{ ... }[] | undefined>;
```


A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L53">property retention</a>
</h3>

```typescript
public retention: pulumi.Output<number | undefined>;
```


Retention time for this table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L57">property storageDescriptor</a>
</h3>

```typescript
public storageDescriptor: pulumi.Output<{ ... } | undefined>;
```


A [storage descriptor](#storage_descriptor) object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L61">property tableType</a>
</h3>

```typescript
public tableType: pulumi.Output<string | undefined>;
```


The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L65">property viewExpandedText</a>
</h3>

```typescript
public viewExpandedText: pulumi.Output<string | undefined>;
```


If the table is a view, the expanded text of the view; otherwise null.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L69">property viewOriginalText</a>
</h3>

```typescript
public viewOriginalText: pulumi.Output<string | undefined>;
```


If the table is a view, the original text of the view; otherwise null.

<h2 class="pdoc-module-header" id="Classifier">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L11">class Classifier</a>
</h2>

Provides a Glue Classifier resource.

~> **NOTE:** It is only valid to create one type of classifier (grok, JSON, or XML). Changing classifier types will recreate the classifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L39">constructor</a>
</h3>

```typescript
new Classifier(name: string, args?: ClassifierArgs, opts?: pulumi.ResourceOptions)
```


Create a Classifier resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClassifierState): Classifier
```


Get an existing Classifier resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L27">property grokClassifier</a>
</h3>

```typescript
public grokClassifier: pulumi.Output<{ ... } | undefined>;
```


A classifier that uses grok patterns. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L31">property jsonClassifier</a>
</h3>

```typescript
public jsonClassifier: pulumi.Output<{ ... } | undefined>;
```


A classifier for JSON content. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L35">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the classifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L39">property xmlClassifier</a>
</h3>

```typescript
public xmlClassifier: pulumi.Output<{ ... } | undefined>;
```


A classifier for XML content. Defined below.

<h2 class="pdoc-module-header" id="Connection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L9">class Connection</a>
</h2>

Provides a Glue Connection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L49">constructor</a>
</h3>

```typescript
new Connection(name: string, args: ConnectionArgs, opts?: pulumi.ResourceOptions)
```


Create a Connection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConnectionState): Connection
```


Get an existing Connection resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L25">property catalogId</a>
</h3>

```typescript
public catalogId: pulumi.Output<string>;
```


The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L29">property connectionProperties</a>
</h3>

```typescript
public connectionProperties: pulumi.Output<{ ... }>;
```


A map of key-value pairs used as parameters for this connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L33">property connectionType</a>
</h3>

```typescript
public connectionType: pulumi.Output<string | undefined>;
```


The type of the connection. Defaults to `JBDC`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L41">property matchCriterias</a>
</h3>

```typescript
public matchCriterias: pulumi.Output<string[] | undefined>;
```


A list of criteria that can be used in selecting this connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L49">property physicalConnectionRequirements</a>
</h3>

```typescript
public physicalConnectionRequirements: pulumi.Output<{ ... } | undefined>;
```


A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Crawler">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L9">class Crawler</a>
</h2>

Manages a Glue Crawler. More information can be found in the [AWS Glue Develeper Guide](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L65">constructor</a>
</h3>

```typescript
new Crawler(name: string, args: CrawlerArgs, opts?: pulumi.ResourceOptions)
```


Create a Crawler resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CrawlerState): Crawler
```


Get an existing Crawler resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L25">property classifiers</a>
</h3>

```typescript
public classifiers: pulumi.Output<string[] | undefined>;
```


List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L29">property configuration</a>
</h3>

```typescript
public configuration: pulumi.Output<string | undefined>;
```


JSON string of configuration information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L33">property databaseName</a>
</h3>

```typescript
public databaseName: pulumi.Output<string>;
```


Glue database where results are written.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L37">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the crawler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L41">property jdbcTargets</a>
</h3>

```typescript
public jdbcTargets: pulumi.Output<{ ... }[] | undefined>;
```


List of nested JBDC target arguments. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Name of the crawler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L49">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The IAM role (or ARN of an IAM role) used by the crawler to access other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L53">property s3Targets</a>
</h3>

```typescript
public s3Targets: pulumi.Output<{ ... }[] | undefined>;
```


List nested Amazon S3 target arguments. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L57">property schedule</a>
</h3>

```typescript
public schedule: pulumi.Output<string | undefined>;
```


A cron expression used to specify the schedule. For more information, see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L61">property schemaChangePolicy</a>
</h3>

```typescript
public schemaChangePolicy: pulumi.Output<{ ... } | undefined>;
```


Policy for the crawler's update and deletion behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L65">property tablePrefix</a>
</h3>

```typescript
public tablePrefix: pulumi.Output<string | undefined>;
```


The table prefix used for catalog tables that are created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Job">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L9">class Job</a>
</h2>

Provides a Glue Job resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L61">constructor</a>
</h3>

```typescript
new Job(name: string, args: JobArgs, opts?: pulumi.ResourceOptions)
```


Create a Job resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JobState): Job
```


Get an existing Job resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L25">property allocatedCapacity</a>
</h3>

```typescript
public allocatedCapacity: pulumi.Output<number | undefined>;
```


The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L29">property command</a>
</h3>

```typescript
public command: pulumi.Output<{ ... }>;
```


The command of the job. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L33">property connections</a>
</h3>

```typescript
public connections: pulumi.Output<string[] | undefined>;
```


The list of connections used for this job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L37">property defaultArguments</a>
</h3>

```typescript
public defaultArguments: pulumi.Output<{ ... } | undefined>;
```


The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the [Special Parameters Used by AWS Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html) topic in the developer guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L41">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


Description of the job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L45">property executionProperty</a>
</h3>

```typescript
public executionProperty: pulumi.Output<{ ... }>;
```


Execution property of the job. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L49">property maxRetries</a>
</h3>

```typescript
public maxRetries: pulumi.Output<number | undefined>;
```


The maximum number of times to retry this job if it fails.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the job command. Defaults to `glueetl`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L57">property roleArn</a>
</h3>

```typescript
public roleArn: pulumi.Output<string>;
```


The ARN of the IAM role associated with this job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L61">property timeout</a>
</h3>

```typescript
public timeout: pulumi.Output<number | undefined>;
```


The job timeout in minutes. The default is 2880 minutes (48 hours).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Trigger">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L9">class Trigger</a>
</h2>

Manages a Glue Trigger resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L49">constructor</a>
</h3>

```typescript
new Trigger(name: string, args: TriggerArgs, opts?: pulumi.ResourceOptions)
```


Create a Trigger resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TriggerState): Trigger
```


Get an existing Trigger resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L25">property actions</a>
</h3>

```typescript
public actions: pulumi.Output<{ ... }[]>;
```


List of actions initiated by this trigger when it fires. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description of the new trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L33">property enabled</a>
</h3>

```typescript
public enabled: pulumi.Output<boolean | undefined>;
```


Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L41">property predicate</a>
</h3>

```typescript
public predicate: pulumi.Output<{ ... } | undefined>;
```


A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L45">property schedule</a>
</h3>

```typescript
public schedule: pulumi.Output<string | undefined>;
```


A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L49">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getScript">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts#L9">function getScript</a>
</h2>

```typescript
getScript(args: GetScriptArgs): Promise<GetScriptResult>
```


Use this data source to generate a Glue script from a Directed Acyclic Graph (DAG).

<h2 class="pdoc-module-header" id="CatalogDatabaseArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L101">interface CatalogDatabaseArgs</a>
</h2>

The set of arguments for constructing a CatalogDatabase resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L105">property catalogId</a>
</h3>

```typescript
catalogId?: pulumi.Input<string>;
```


ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L109">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L113">property locationUri</a>
</h3>

```typescript
locationUri?: pulumi.Input<string>;
```


The location of the database (for example, an HDFS path).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L117">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L121">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A list of key-value pairs that define parameters and properties of the database.

<h2 class="pdoc-module-header" id="CatalogDatabaseState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L75">interface CatalogDatabaseState</a>
</h2>

Input properties used for looking up and filtering CatalogDatabase resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L79">property catalogId</a>
</h3>

```typescript
catalogId?: pulumi.Input<string>;
```


ID of the Glue Catalog to create the database in. If omitted, this defaults to the AWS Account ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L83">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L87">property locationUri</a>
</h3>

```typescript
locationUri?: pulumi.Input<string>;
```


The location of the database (for example, an HDFS path).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L91">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the database.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogDatabase.ts#L95">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


A list of key-value pairs that define parameters and properties of the database.

<h2 class="pdoc-module-header" id="CatalogTableArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L174">interface CatalogTableArgs</a>
</h2>

The set of arguments for constructing a CatalogTable resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L178">property catalogId</a>
</h3>

```typescript
catalogId?: pulumi.Input<string>;
```


ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L182">property databaseName</a>
</h3>

```typescript
databaseName: pulumi.Input<string>;
```


Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L186">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L190">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the SerDe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L194">property owner</a>
</h3>

```typescript
owner?: pulumi.Input<string>;
```


Owner of the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L198">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L202">property partitionKeys</a>
</h3>

```typescript
partitionKeys?: pulumi.Input<{ ... }[]>;
```


A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L206">property retention</a>
</h3>

```typescript
retention?: pulumi.Input<number>;
```


Retention time for this table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L210">property storageDescriptor</a>
</h3>

```typescript
storageDescriptor?: pulumi.Input<{ ... }>;
```


A [storage descriptor](#storage_descriptor) object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L214">property tableType</a>
</h3>

```typescript
tableType?: pulumi.Input<string>;
```


The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L218">property viewExpandedText</a>
</h3>

```typescript
viewExpandedText?: pulumi.Input<string>;
```


If the table is a view, the expanded text of the view; otherwise null.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L222">property viewOriginalText</a>
</h3>

```typescript
viewOriginalText?: pulumi.Input<string>;
```


If the table is a view, the original text of the view; otherwise null.

<h2 class="pdoc-module-header" id="CatalogTableState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L120">interface CatalogTableState</a>
</h2>

Input properties used for looking up and filtering CatalogTable resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L124">property catalogId</a>
</h3>

```typescript
catalogId?: pulumi.Input<string>;
```


ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L128">property databaseName</a>
</h3>

```typescript
databaseName?: pulumi.Input<string>;
```


Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L132">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the SerDe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L140">property owner</a>
</h3>

```typescript
owner?: pulumi.Input<string>;
```


Owner of the table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L144">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L148">property partitionKeys</a>
</h3>

```typescript
partitionKeys?: pulumi.Input<{ ... }[]>;
```


A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L152">property retention</a>
</h3>

```typescript
retention?: pulumi.Input<number>;
```


Retention time for this table.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L156">property storageDescriptor</a>
</h3>

```typescript
storageDescriptor?: pulumi.Input<{ ... }>;
```


A [storage descriptor](#storage_descriptor) object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L160">property tableType</a>
</h3>

```typescript
tableType?: pulumi.Input<string>;
```


The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L164">property viewExpandedText</a>
</h3>

```typescript
viewExpandedText?: pulumi.Input<string>;
```


If the table is a view, the expanded text of the view; otherwise null.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/catalogTable.ts#L168">property viewOriginalText</a>
</h3>

```typescript
viewOriginalText?: pulumi.Input<string>;
```


If the table is a view, the original text of the view; otherwise null.

<h2 class="pdoc-module-header" id="ClassifierArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L93">interface ClassifierArgs</a>
</h2>

The set of arguments for constructing a Classifier resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L97">property grokClassifier</a>
</h3>

```typescript
grokClassifier?: pulumi.Input<{ ... }>;
```


A classifier that uses grok patterns. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L101">property jsonClassifier</a>
</h3>

```typescript
jsonClassifier?: pulumi.Input<{ ... }>;
```


A classifier for JSON content. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the classifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L109">property xmlClassifier</a>
</h3>

```typescript
xmlClassifier?: pulumi.Input<{ ... }>;
```


A classifier for XML content. Defined below.

<h2 class="pdoc-module-header" id="ClassifierState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L71">interface ClassifierState</a>
</h2>

Input properties used for looking up and filtering Classifier resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L75">property grokClassifier</a>
</h3>

```typescript
grokClassifier?: pulumi.Input<{ ... }>;
```


A classifier that uses grok patterns. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L79">property jsonClassifier</a>
</h3>

```typescript
jsonClassifier?: pulumi.Input<{ ... }>;
```


A classifier for JSON content. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L83">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the classifier.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/classifier.ts#L87">property xmlClassifier</a>
</h3>

```typescript
xmlClassifier?: pulumi.Input<{ ... }>;
```


A classifier for XML content. Defined below.

<h2 class="pdoc-module-header" id="ConnectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L124">interface ConnectionArgs</a>
</h2>

The set of arguments for constructing a Connection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L128">property catalogId</a>
</h3>

```typescript
catalogId?: pulumi.Input<string>;
```


The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L132">property connectionProperties</a>
</h3>

```typescript
connectionProperties: pulumi.Input<{ ... }>;
```


A map of key-value pairs used as parameters for this connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L136">property connectionType</a>
</h3>

```typescript
connectionType?: pulumi.Input<string>;
```


The type of the connection. Defaults to `JBDC`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L140">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L144">property matchCriterias</a>
</h3>

```typescript
matchCriterias?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of criteria that can be used in selecting this connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L148">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L152">property physicalConnectionRequirements</a>
</h3>

```typescript
physicalConnectionRequirements?: pulumi.Input<{ ... }>;
```


A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.

<h2 class="pdoc-module-header" id="ConnectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L90">interface ConnectionState</a>
</h2>

Input properties used for looking up and filtering Connection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L94">property catalogId</a>
</h3>

```typescript
catalogId?: pulumi.Input<string>;
```


The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L98">property connectionProperties</a>
</h3>

```typescript
connectionProperties?: pulumi.Input<{ ... }>;
```


A map of key-value pairs used as parameters for this connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L102">property connectionType</a>
</h3>

```typescript
connectionType?: pulumi.Input<string>;
```


The type of the connection. Defaults to `JBDC`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L106">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L110">property matchCriterias</a>
</h3>

```typescript
matchCriterias?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of criteria that can be used in selecting this connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L114">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/connection.ts#L118">property physicalConnectionRequirements</a>
</h3>

```typescript
physicalConnectionRequirements?: pulumi.Input<{ ... }>;
```


A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.

<h2 class="pdoc-module-header" id="CrawlerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L167">interface CrawlerArgs</a>
</h2>

The set of arguments for constructing a Crawler resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L171">property classifiers</a>
</h3>

```typescript
classifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L175">property configuration</a>
</h3>

```typescript
configuration?: pulumi.Input<string>;
```


JSON string of configuration information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L179">property databaseName</a>
</h3>

```typescript
databaseName: pulumi.Input<string>;
```


Glue database where results are written.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L183">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the crawler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L187">property jdbcTargets</a>
</h3>

```typescript
jdbcTargets?: pulumi.Input<{ ... }[]>;
```


List of nested JBDC target arguments. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L191">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the crawler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L195">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The IAM role (or ARN of an IAM role) used by the crawler to access other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L199">property s3Targets</a>
</h3>

```typescript
s3Targets?: pulumi.Input<{ ... }[]>;
```


List nested Amazon S3 target arguments. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L203">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<string>;
```


A cron expression used to specify the schedule. For more information, see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L207">property schemaChangePolicy</a>
</h3>

```typescript
schemaChangePolicy?: pulumi.Input<{ ... }>;
```


Policy for the crawler's update and deletion behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L211">property tablePrefix</a>
</h3>

```typescript
tablePrefix?: pulumi.Input<string>;
```


The table prefix used for catalog tables that are created.

<h2 class="pdoc-module-header" id="CrawlerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L117">interface CrawlerState</a>
</h2>

Input properties used for looking up and filtering Crawler resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L121">property classifiers</a>
</h3>

```typescript
classifiers?: pulumi.Input<pulumi.Input<string>[]>;
```


List of custom classifiers. By default, all AWS classifiers are included in a crawl, but these custom classifiers always override the default classifiers for a given classification.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L125">property configuration</a>
</h3>

```typescript
configuration?: pulumi.Input<string>;
```


JSON string of configuration information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L129">property databaseName</a>
</h3>

```typescript
databaseName?: pulumi.Input<string>;
```


Glue database where results are written.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L133">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the crawler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L137">property jdbcTargets</a>
</h3>

```typescript
jdbcTargets?: pulumi.Input<{ ... }[]>;
```


List of nested JBDC target arguments. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Name of the crawler.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L145">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The IAM role (or ARN of an IAM role) used by the crawler to access other resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L149">property s3Targets</a>
</h3>

```typescript
s3Targets?: pulumi.Input<{ ... }[]>;
```


List nested Amazon S3 target arguments. See below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L153">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<string>;
```


A cron expression used to specify the schedule. For more information, see [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html). For example, to run something every day at 12:15 UTC, you would specify: `cron(15 12 * * ? *)`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L157">property schemaChangePolicy</a>
</h3>

```typescript
schemaChangePolicy?: pulumi.Input<{ ... }>;
```


Policy for the crawler's update and deletion behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/crawler.ts#L161">property tablePrefix</a>
</h3>

```typescript
tablePrefix?: pulumi.Input<string>;
```


The table prefix used for catalog tables that are created.

<h2 class="pdoc-module-header" id="GetScriptArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts#L20">interface GetScriptArgs</a>
</h2>

A collection of arguments for invoking getScript.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts#L24">property dagEdges</a>
</h3>

```typescript
dagEdges: pulumi.Input<{ ... }[]>;
```


A list of the edges in the DAG. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts#L28">property dagNodes</a>
</h3>

```typescript
dagNodes: pulumi.Input<{ ... }[]>;
```


A list of the nodes in the DAG. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts#L32">property language</a>
</h3>

```typescript
language?: pulumi.Input<string>;
```


The programming language of the resulting code from the DAG. Defaults to `PYTHON`. Valid values are `PYTHON` and `SCALA`.

<h2 class="pdoc-module-header" id="GetScriptResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts#L38">interface GetScriptResult</a>
</h2>

A collection of values returned by getScript.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts#L50">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts#L42">property pythonScript</a>
</h3>

```typescript
pythonScript: string;
```


The Python script generated from the DAG when the `language` argument is set to `PYTHON`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/getScript.ts#L46">property scalaCode</a>
</h3>

```typescript
scalaCode: string;
```


The Scala code generated from the DAG when the `language` argument is set to `SCALA`.

<h2 class="pdoc-module-header" id="JobArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L157">interface JobArgs</a>
</h2>

The set of arguments for constructing a Job resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L161">property allocatedCapacity</a>
</h3>

```typescript
allocatedCapacity?: pulumi.Input<number>;
```


The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L165">property command</a>
</h3>

```typescript
command: pulumi.Input<{ ... }>;
```


The command of the job. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L169">property connections</a>
</h3>

```typescript
connections?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of connections used for this job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L173">property defaultArguments</a>
</h3>

```typescript
defaultArguments?: pulumi.Input<{ ... }>;
```


The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the [Special Parameters Used by AWS Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html) topic in the developer guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L177">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L181">property executionProperty</a>
</h3>

```typescript
executionProperty?: pulumi.Input<{ ... }>;
```


Execution property of the job. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L185">property maxRetries</a>
</h3>

```typescript
maxRetries?: pulumi.Input<number>;
```


The maximum number of times to retry this job if it fails.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L189">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the job command. Defaults to `glueetl`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L193">property roleArn</a>
</h3>

```typescript
roleArn: pulumi.Input<string>;
```


The ARN of the IAM role associated with this job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L197">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


The job timeout in minutes. The default is 2880 minutes (48 hours).

<h2 class="pdoc-module-header" id="JobState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L111">interface JobState</a>
</h2>

Input properties used for looking up and filtering Job resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L115">property allocatedCapacity</a>
</h3>

```typescript
allocatedCapacity?: pulumi.Input<number>;
```


The number of AWS Glue data processing units (DPUs) to allocate to this Job. At least 2 DPUs need to be allocated; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L119">property command</a>
</h3>

```typescript
command?: pulumi.Input<{ ... }>;
```


The command of the job. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L123">property connections</a>
</h3>

```typescript
connections?: pulumi.Input<pulumi.Input<string>[]>;
```


The list of connections used for this job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L127">property defaultArguments</a>
</h3>

```typescript
defaultArguments?: pulumi.Input<{ ... }>;
```


The map of default arguments for this job. You can specify arguments here that your own job-execution script consumes, as well as arguments that AWS Glue itself consumes. For information about how to specify and consume your own Job arguments, see the [Calling AWS Glue APIs in Python](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide. For information about the key-value pairs that AWS Glue consumes to set up your job, see the [Special Parameters Used by AWS Glue](http://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-glue-arguments.html) topic in the developer guide.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L131">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L135">property executionProperty</a>
</h3>

```typescript
executionProperty?: pulumi.Input<{ ... }>;
```


Execution property of the job. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L139">property maxRetries</a>
</h3>

```typescript
maxRetries?: pulumi.Input<number>;
```


The maximum number of times to retry this job if it fails.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L143">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the job command. Defaults to `glueetl`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L147">property roleArn</a>
</h3>

```typescript
roleArn?: pulumi.Input<string>;
```


The ARN of the IAM role associated with this job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/job.ts#L151">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<number>;
```


The job timeout in minutes. The default is 2880 minutes (48 hours).

<h2 class="pdoc-module-header" id="TriggerArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L127">interface TriggerArgs</a>
</h2>

The set of arguments for constructing a Trigger resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L131">property actions</a>
</h3>

```typescript
actions: pulumi.Input<{ ... }[]>;
```


List of actions initiated by this trigger when it fires. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L135">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the new trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L139">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L143">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L147">property predicate</a>
</h3>

```typescript
predicate?: pulumi.Input<{ ... }>;
```


A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L151">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<string>;
```


A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L155">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.

<h2 class="pdoc-module-header" id="TriggerState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L93">interface TriggerState</a>
</h2>

Input properties used for looking up and filtering Trigger resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L97">property actions</a>
</h3>

```typescript
actions?: pulumi.Input<{ ... }[]>;
```


List of actions initiated by this trigger when it fires. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L101">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description of the new trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L105">property enabled</a>
</h3>

```typescript
enabled?: pulumi.Input<boolean>;
```


Start the trigger. Defaults to `true`. Not valid to disable for `ON_DEMAND` type.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the trigger.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L113">property predicate</a>
</h3>

```typescript
predicate?: pulumi.Input<{ ... }>;
```


A predicate to specify when the new trigger should fire. Required when trigger type is `CONDITIONAL`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L117">property schedule</a>
</h3>

```typescript
schedule?: pulumi.Input<string>;
```


A cron expression used to specify the schedule. [Time-Based Schedules for Jobs and Crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/glue/trigger.ts#L121">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of trigger. Valid values are `CONDITIONAL`, `ON_DEMAND`, and `SCHEDULED`.

