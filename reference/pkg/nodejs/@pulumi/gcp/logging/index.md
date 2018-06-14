---
title: Module logging
---

<a href="../index.html">@pulumi/gcp</a> &gt; logging

<h2 class="pdoc-module-header">Index</h2>

* <a href="#BillingAccountSink">class BillingAccountSink</a>
* <a href="#FolderSink">class FolderSink</a>
* <a href="#OrganizationSink">class OrganizationSink</a>
* <a href="#ProjectSink">class ProjectSink</a>
* <a href="#BillingAccountSinkArgs">interface BillingAccountSinkArgs</a>
* <a href="#BillingAccountSinkState">interface BillingAccountSinkState</a>
* <a href="#FolderSinkArgs">interface FolderSinkArgs</a>
* <a href="#FolderSinkState">interface FolderSinkState</a>
* <a href="#OrganizationSinkArgs">interface OrganizationSinkArgs</a>
* <a href="#OrganizationSinkState">interface OrganizationSinkState</a>
* <a href="#ProjectSinkArgs">interface ProjectSinkArgs</a>
* <a href="#ProjectSinkState">interface ProjectSinkState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts">logging/billingAccountSink.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts">logging/folderSink.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts">logging/organizationSink.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts">logging/projectSink.ts</a> 


<h2 class="pdoc-module-header" id="BillingAccountSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L14">class BillingAccountSink</a>
</h2>

Manages a billing account logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L56">constructor</a>
</h3>

```typescript
new BillingAccountSink(name: string, args: BillingAccountSinkArgs, opts?: pulumi.ResourceOptions)
```


Create a BillingAccountSink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BillingAccountSinkState): BillingAccountSink
```


Get an existing BillingAccountSink resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L30">property billingAccount</a>
</h3>

```typescript
public billingAccount: pulumi.Output<string>;
```


The billing account exported to the sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L41">property destination</a>
</h3>

```typescript
public destination: pulumi.Output<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L47">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string | undefined>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L56">property writerIdentity</a>
</h3>

```typescript
public writerIdentity: pulumi.Output<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="FolderSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L14">class FolderSink</a>
</h2>

Manages a folder-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L62">constructor</a>
</h3>

```typescript
new FolderSink(name: string, args: FolderSinkArgs, opts?: pulumi.ResourceOptions)
```


Create a FolderSink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FolderSinkState): FolderSink
```


Get an existing FolderSink resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L37">property destination</a>
</h3>

```typescript
public destination: pulumi.Output<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L43">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string | undefined>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L48">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string>;
```


The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L53">property includeChildren</a>
</h3>

```typescript
public includeChildren: pulumi.Output<boolean | undefined>;
```


Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L57">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L62">property writerIdentity</a>
</h3>

```typescript
public writerIdentity: pulumi.Output<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="OrganizationSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L14">class OrganizationSink</a>
</h2>

Manages a organization-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L61">constructor</a>
</h3>

```typescript
new OrganizationSink(name: string, args: OrganizationSinkArgs, opts?: pulumi.ResourceOptions)
```


Create a OrganizationSink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationSinkState): OrganizationSink
```


Get an existing OrganizationSink resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L37">property destination</a>
</h3>

```typescript
public destination: pulumi.Output<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L43">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string | undefined>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L48">property includeChildren</a>
</h3>

```typescript
public includeChildren: pulumi.Output<boolean | undefined>;
```


Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L52">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L56">property orgId</a>
</h3>

```typescript
public orgId: pulumi.Output<string>;
```


The numeric ID of the organization to be exported to the sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L61">property writerIdentity</a>
</h3>

```typescript
public writerIdentity: pulumi.Output<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="ProjectSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L16">class ProjectSink</a>
</h2>

Manages a project-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/),
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs)
and
[API](https://cloud.google.com/logging/docs/reference/v2/rest/).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L66">constructor</a>
</h3>

```typescript
new ProjectSink(name: string, args: ProjectSinkArgs, opts?: pulumi.ResourceOptions)
```


Create a ProjectSink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectSinkState): ProjectSink
```


Get an existing ProjectSink resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L39">property destination</a>
</h3>

```typescript
public destination: pulumi.Output<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L45">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string | undefined>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L49">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L54">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L61">property uniqueWriterIdentity</a>
</h3>

```typescript
public uniqueWriterIdentity: pulumi.Output<boolean | undefined>;
```


Whether or not to create a unique identity associated with this sink. If `false`
(the default), then the `writer_identity` used is `serviceAccount:cloud-logs@system.gserviceaccount.com`. If `true`,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set `unique_writer_identity` to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L66">property writerIdentity</a>
</h3>

```typescript
public writerIdentity: pulumi.Output<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="BillingAccountSinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L132">interface BillingAccountSinkArgs</a>
</h2>

The set of arguments for constructing a BillingAccountSink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L136">property billingAccount</a>
</h3>

```typescript
billingAccount: pulumi.Input<string>;
```


The billing account exported to the sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L147">property destination</a>
</h3>

```typescript
destination: pulumi.Input<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L153">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L157">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h2 class="pdoc-module-header" id="BillingAccountSinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L96">interface BillingAccountSinkState</a>
</h2>

Input properties used for looking up and filtering BillingAccountSink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L100">property billingAccount</a>
</h3>

```typescript
billingAccount?: pulumi.Input<string>;
```


The billing account exported to the sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L111">property destination</a>
</h3>

```typescript
destination?: pulumi.Input<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L117">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L121">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L126">property writerIdentity</a>
</h3>

```typescript
writerIdentity?: pulumi.Input<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="FolderSinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L146">interface FolderSinkArgs</a>
</h2>

The set of arguments for constructing a FolderSink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L157">property destination</a>
</h3>

```typescript
destination: pulumi.Input<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L163">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L168">property folder</a>
</h3>

```typescript
folder: pulumi.Input<string>;
```


The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L173">property includeChildren</a>
</h3>

```typescript
includeChildren?: pulumi.Input<boolean>;
```


Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L177">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h2 class="pdoc-module-header" id="FolderSinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L104">interface FolderSinkState</a>
</h2>

Input properties used for looking up and filtering FolderSink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L115">property destination</a>
</h3>

```typescript
destination?: pulumi.Input<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L121">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L126">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L131">property includeChildren</a>
</h3>

```typescript
includeChildren?: pulumi.Input<boolean>;
```


Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L140">property writerIdentity</a>
</h3>

```typescript
writerIdentity?: pulumi.Input<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="OrganizationSinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L144">interface OrganizationSinkArgs</a>
</h2>

The set of arguments for constructing a OrganizationSink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L155">property destination</a>
</h3>

```typescript
destination: pulumi.Input<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L161">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L166">property includeChildren</a>
</h3>

```typescript
includeChildren?: pulumi.Input<boolean>;
```


Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L170">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L174">property orgId</a>
</h3>

```typescript
orgId: pulumi.Input<string>;
```


The numeric ID of the organization to be exported to the sink.

<h2 class="pdoc-module-header" id="OrganizationSinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L103">interface OrganizationSinkState</a>
</h2>

Input properties used for looking up and filtering OrganizationSink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L114">property destination</a>
</h3>

```typescript
destination?: pulumi.Input<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L120">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L125">property includeChildren</a>
</h3>

```typescript
includeChildren?: pulumi.Input<boolean>;
```


Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L133">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The numeric ID of the organization to be exported to the sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L138">property writerIdentity</a>
</h3>

```typescript
writerIdentity?: pulumi.Input<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="ProjectSinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L149">interface ProjectSinkArgs</a>
</h2>

The set of arguments for constructing a ProjectSink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L160">property destination</a>
</h3>

```typescript
destination: pulumi.Input<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L166">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L170">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L175">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L182">property uniqueWriterIdentity</a>
</h3>

```typescript
uniqueWriterIdentity?: pulumi.Input<boolean>;
```


Whether or not to create a unique identity associated with this sink. If `false`
(the default), then the `writer_identity` used is `serviceAccount:cloud-logs@system.gserviceaccount.com`. If `true`,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set `unique_writer_identity` to true.

<h2 class="pdoc-module-header" id="ProjectSinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L105">interface ProjectSinkState</a>
</h2>

Input properties used for looking up and filtering ProjectSink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L116">property destination</a>
</h3>

```typescript
destination?: pulumi.Input<string>;
```


The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```
"storage.googleapis.com/[GCS_BUCKET]"
"bigquery.googleapis.com/projects/[PROJECT_ID]/datasets/[DATASET]"
"pubsub.googleapis.com/projects/[PROJECT_ID]/topics/[TOPIC_ID]"
```
The writer associated with the sink must have access to write to the above resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L122">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L131">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L138">property uniqueWriterIdentity</a>
</h3>

```typescript
uniqueWriterIdentity?: pulumi.Input<boolean>;
```


Whether or not to create a unique identity associated with this sink. If `false`
(the default), then the `writer_identity` used is `serviceAccount:cloud-logs@system.gserviceaccount.com`. If `true`,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set `unique_writer_identity` to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L143">property writerIdentity</a>
</h3>

```typescript
writerIdentity?: pulumi.Input<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

