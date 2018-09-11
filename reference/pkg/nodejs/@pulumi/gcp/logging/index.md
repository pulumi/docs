---
title: Module logging
---

<a href="../index.html">@pulumi/gcp</a> &gt; logging

<h2 class="pdoc-module-header">Index</h2>

* <a href="#BillingAccountExclusion">class BillingAccountExclusion</a>
* <a href="#BillingAccountSink">class BillingAccountSink</a>
* <a href="#FolderExclusion">class FolderExclusion</a>
* <a href="#FolderSink">class FolderSink</a>
* <a href="#OrganizationExclusion">class OrganizationExclusion</a>
* <a href="#OrganizationSink">class OrganizationSink</a>
* <a href="#ProjectExclusion">class ProjectExclusion</a>
* <a href="#ProjectSink">class ProjectSink</a>
* <a href="#BillingAccountExclusionArgs">interface BillingAccountExclusionArgs</a>
* <a href="#BillingAccountExclusionState">interface BillingAccountExclusionState</a>
* <a href="#BillingAccountSinkArgs">interface BillingAccountSinkArgs</a>
* <a href="#BillingAccountSinkState">interface BillingAccountSinkState</a>
* <a href="#FolderExclusionArgs">interface FolderExclusionArgs</a>
* <a href="#FolderExclusionState">interface FolderExclusionState</a>
* <a href="#FolderSinkArgs">interface FolderSinkArgs</a>
* <a href="#FolderSinkState">interface FolderSinkState</a>
* <a href="#OrganizationExclusionArgs">interface OrganizationExclusionArgs</a>
* <a href="#OrganizationExclusionState">interface OrganizationExclusionState</a>
* <a href="#OrganizationSinkArgs">interface OrganizationSinkArgs</a>
* <a href="#OrganizationSinkState">interface OrganizationSinkState</a>
* <a href="#ProjectExclusionArgs">interface ProjectExclusionArgs</a>
* <a href="#ProjectExclusionState">interface ProjectExclusionState</a>
* <a href="#ProjectSinkArgs">interface ProjectSinkArgs</a>
* <a href="#ProjectSinkState">interface ProjectSinkState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts">logging/billingAccountExclusion.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts">logging/billingAccountSink.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts">logging/folderExclusion.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts">logging/folderSink.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts">logging/organizationExclusion.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts">logging/organizationSink.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts">logging/projectExclusion.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts">logging/projectSink.ts</a> 


<h2 class="pdoc-module-header" id="BillingAccountExclusion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L15">class BillingAccountExclusion</a>
</h2>

Manages a billing account logging exclusion. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Excluding Logs](https://cloud.google.com/logging/docs/exclusions).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L50">constructor</a>
</h3>

```typescript
new BillingAccountExclusion(name: string, args: BillingAccountExclusionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a BillingAccountExclusion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BillingAccountExclusionState): BillingAccountExclusion
```


Get an existing BillingAccountExclusion resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L31">property billingAccount</a>
</h3>

```typescript
public billingAccount: pulumi.Output<string>;
```


The billing account to create the exclusion for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L35">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L40">property disabled</a>
</h3>

```typescript
public disabled: pulumi.Output<boolean | undefined>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L46">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging exclusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BillingAccountSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L15">class BillingAccountSink</a>
</h2>

Manages a billing account logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L57">constructor</a>
</h3>

```typescript
new BillingAccountSink(name: string, args: BillingAccountSinkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a BillingAccountSink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BillingAccountSinkState): BillingAccountSink
```


Get an existing BillingAccountSink resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L31">property billingAccount</a>
</h3>

```typescript
public billingAccount: pulumi.Output<string>;
```


The billing account exported to the sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L42">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L48">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string | undefined>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L52">property name</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L57">property writerIdentity</a>
</h3>

```typescript
public writerIdentity: pulumi.Output<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="FolderExclusion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L15">class FolderExclusion</a>
</h2>

Manages a folder-level logging exclusion. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Excluding Logs](https://cloud.google.com/logging/docs/exclusions).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L51">constructor</a>
</h3>

```typescript
new FolderExclusion(name: string, args: FolderExclusionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FolderExclusion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FolderExclusionState): FolderExclusion
```


Get an existing FolderExclusion resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L36">property disabled</a>
</h3>

```typescript
public disabled: pulumi.Output<boolean | undefined>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L42">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L47">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string>;
```


The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L51">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging exclusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="FolderSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L15">class FolderSink</a>
</h2>

Manages a folder-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L63">constructor</a>
</h3>

```typescript
new FolderSink(name: string, args: FolderSinkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a FolderSink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FolderSinkState): FolderSink
```


Get an existing FolderSink resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L38">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L44">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string | undefined>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L49">property folder</a>
</h3>

```typescript
public folder: pulumi.Output<string>;
```


The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L54">property includeChildren</a>
</h3>

```typescript
public includeChildren: pulumi.Output<boolean | undefined>;
```


Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L58">property name</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L63">property writerIdentity</a>
</h3>

```typescript
public writerIdentity: pulumi.Output<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="OrganizationExclusion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L15">class OrganizationExclusion</a>
</h2>

Manages an organization-level logging exclusion. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Excluding Logs](https://cloud.google.com/logging/docs/exclusions).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L50">constructor</a>
</h3>

```typescript
new OrganizationExclusion(name: string, args: OrganizationExclusionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a OrganizationExclusion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationExclusionState): OrganizationExclusion
```


Get an existing OrganizationExclusion resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L36">property disabled</a>
</h3>

```typescript
public disabled: pulumi.Output<boolean | undefined>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L42">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging exclusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L50">property orgId</a>
</h3>

```typescript
public orgId: pulumi.Output<string>;
```


The organization to create the exclusion in.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="OrganizationSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L15">class OrganizationSink</a>
</h2>

Manages a organization-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L62">constructor</a>
</h3>

```typescript
new OrganizationSink(name: string, args: OrganizationSinkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a OrganizationSink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationSinkState): OrganizationSink
```


Get an existing OrganizationSink resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L38">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L44">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string | undefined>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L49">property includeChildren</a>
</h3>

```typescript
public includeChildren: pulumi.Output<boolean | undefined>;
```


Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L53">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L57">property orgId</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L62">property writerIdentity</a>
</h3>

```typescript
public writerIdentity: pulumi.Output<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="ProjectExclusion">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L15">class ProjectExclusion</a>
</h2>

Manages a project-level logging exclusion. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Excluding Logs](https://cloud.google.com/logging/docs/exclusions).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L51">constructor</a>
</h3>

```typescript
new ProjectExclusion(name: string, args: ProjectExclusionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ProjectExclusion resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectExclusionState): ProjectExclusion
```


Get an existing ProjectExclusion resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L36">property disabled</a>
</h3>

```typescript
public disabled: pulumi.Output<boolean | undefined>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L42">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging exclusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L51">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project to create the exclusion in. If omitted, the project associated with the provider is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ProjectSink">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L17">class ProjectSink</a>
</h2>

Manages a project-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/),
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs)
and
[API](https://cloud.google.com/logging/docs/reference/v2/rest/).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L67">constructor</a>
</h3>

```typescript
new ProjectSink(name: string, args: ProjectSinkArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ProjectSink resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProjectSinkState): ProjectSink
```


Get an existing ProjectSink resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L40">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L46">property filter</a>
</h3>

```typescript
public filter: pulumi.Output<string | undefined>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L55">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L62">property uniqueWriterIdentity</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L67">property writerIdentity</a>
</h3>

```typescript
public writerIdentity: pulumi.Output<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="BillingAccountExclusionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L119">interface BillingAccountExclusionArgs</a>
</h2>

The set of arguments for constructing a BillingAccountExclusion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L123">property billingAccount</a>
</h3>

```typescript
billingAccount: pulumi.Input<string>;
```


The billing account to create the exclusion for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L127">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L132">property disabled</a>
</h3>

```typescript
disabled?: pulumi.Input<boolean>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L138">property filter</a>
</h3>

```typescript
filter: pulumi.Input<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L142">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging exclusion.

<h2 class="pdoc-module-header" id="BillingAccountExclusionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L90">interface BillingAccountExclusionState</a>
</h2>

Input properties used for looking up and filtering BillingAccountExclusion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L94">property billingAccount</a>
</h3>

```typescript
billingAccount?: pulumi.Input<string>;
```


The billing account to create the exclusion for.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L98">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L103">property disabled</a>
</h3>

```typescript
disabled?: pulumi.Input<boolean>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L109">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountExclusion.ts#L113">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging exclusion.

<h2 class="pdoc-module-header" id="BillingAccountSinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L133">interface BillingAccountSinkArgs</a>
</h2>

The set of arguments for constructing a BillingAccountSink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L137">property billingAccount</a>
</h3>

```typescript
billingAccount: pulumi.Input<string>;
```


The billing account exported to the sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L148">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L154">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L158">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h2 class="pdoc-module-header" id="BillingAccountSinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L97">interface BillingAccountSinkState</a>
</h2>

Input properties used for looking up and filtering BillingAccountSink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L101">property billingAccount</a>
</h3>

```typescript
billingAccount?: pulumi.Input<string>;
```


The billing account exported to the sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L112">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L118">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/billingAccountSink.ts#L127">property writerIdentity</a>
</h3>

```typescript
writerIdentity?: pulumi.Input<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="FolderExclusionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L121">interface FolderExclusionArgs</a>
</h2>

The set of arguments for constructing a FolderExclusion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L125">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L130">property disabled</a>
</h3>

```typescript
disabled?: pulumi.Input<boolean>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L136">property filter</a>
</h3>

```typescript
filter: pulumi.Input<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L141">property folder</a>
</h3>

```typescript
folder: pulumi.Input<string>;
```


The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L145">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging exclusion.

<h2 class="pdoc-module-header" id="FolderExclusionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L91">interface FolderExclusionState</a>
</h2>

Input properties used for looking up and filtering FolderExclusion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L95">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L100">property disabled</a>
</h3>

```typescript
disabled?: pulumi.Input<boolean>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L106">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L111">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderExclusion.ts#L115">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging exclusion.

<h2 class="pdoc-module-header" id="FolderSinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L147">interface FolderSinkArgs</a>
</h2>

The set of arguments for constructing a FolderSink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L158">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L164">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L169">property folder</a>
</h3>

```typescript
folder: pulumi.Input<string>;
```


The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L174">property includeChildren</a>
</h3>

```typescript
includeChildren?: pulumi.Input<boolean>;
```


Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L178">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h2 class="pdoc-module-header" id="FolderSinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L105">interface FolderSinkState</a>
</h2>

Input properties used for looking up and filtering FolderSink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L116">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L122">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L127">property folder</a>
</h3>

```typescript
folder?: pulumi.Input<string>;
```


The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L132">property includeChildren</a>
</h3>

```typescript
includeChildren?: pulumi.Input<boolean>;
```


Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/folderSink.ts#L141">property writerIdentity</a>
</h3>

```typescript
writerIdentity?: pulumi.Input<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="OrganizationExclusionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L119">interface OrganizationExclusionArgs</a>
</h2>

The set of arguments for constructing a OrganizationExclusion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L123">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L128">property disabled</a>
</h3>

```typescript
disabled?: pulumi.Input<boolean>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L134">property filter</a>
</h3>

```typescript
filter: pulumi.Input<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L138">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging exclusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L142">property orgId</a>
</h3>

```typescript
orgId: pulumi.Input<string>;
```


The organization to create the exclusion in.

<h2 class="pdoc-module-header" id="OrganizationExclusionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L90">interface OrganizationExclusionState</a>
</h2>

Input properties used for looking up and filtering OrganizationExclusion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L94">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L99">property disabled</a>
</h3>

```typescript
disabled?: pulumi.Input<boolean>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L105">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging exclusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationExclusion.ts#L113">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The organization to create the exclusion in.

<h2 class="pdoc-module-header" id="OrganizationSinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L145">interface OrganizationSinkArgs</a>
</h2>

The set of arguments for constructing a OrganizationSink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L156">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L162">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L167">property includeChildren</a>
</h3>

```typescript
includeChildren?: pulumi.Input<boolean>;
```


Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L175">property orgId</a>
</h3>

```typescript
orgId: pulumi.Input<string>;
```


The numeric ID of the organization to be exported to the sink.

<h2 class="pdoc-module-header" id="OrganizationSinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L104">interface OrganizationSinkState</a>
</h2>

Input properties used for looking up and filtering OrganizationSink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L115">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L121">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L126">property includeChildren</a>
</h3>

```typescript
includeChildren?: pulumi.Input<boolean>;
```


Whether or not to include children organizations in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided organization are included.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L130">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L134">property orgId</a>
</h3>

```typescript
orgId?: pulumi.Input<string>;
```


The numeric ID of the organization to be exported to the sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/organizationSink.ts#L139">property writerIdentity</a>
</h3>

```typescript
writerIdentity?: pulumi.Input<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

<h2 class="pdoc-module-header" id="ProjectExclusionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L118">interface ProjectExclusionArgs</a>
</h2>

The set of arguments for constructing a ProjectExclusion resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L122">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L127">property disabled</a>
</h3>

```typescript
disabled?: pulumi.Input<boolean>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L133">property filter</a>
</h3>

```typescript
filter: pulumi.Input<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging exclusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L142">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project to create the exclusion in. If omitted, the project associated with the provider is
used.

<h2 class="pdoc-module-header" id="ProjectExclusionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L88">interface ProjectExclusionState</a>
</h2>

Input properties used for looking up and filtering ProjectExclusion resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L92">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A human-readable description.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L97">property disabled</a>
</h3>

```typescript
disabled?: pulumi.Input<boolean>;
```


Whether this exclusion rule should be disabled or not. This defaults to
false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L103">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when excluding logs. Only log entries that match the filter are excluded.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced-filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L107">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging exclusion.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectExclusion.ts#L112">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project to create the exclusion in. If omitted, the project associated with the provider is
used.

<h2 class="pdoc-module-header" id="ProjectSinkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L150">interface ProjectSinkArgs</a>
</h2>

The set of arguments for constructing a ProjectSink resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L161">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L167">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L176">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L183">property uniqueWriterIdentity</a>
</h3>

```typescript
uniqueWriterIdentity?: pulumi.Input<boolean>;
```


Whether or not to create a unique identity associated with this sink. If `false`
(the default), then the `writer_identity` used is `serviceAccount:cloud-logs@system.gserviceaccount.com`. If `true`,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set `unique_writer_identity` to true.

<h2 class="pdoc-module-header" id="ProjectSinkState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L106">interface ProjectSinkState</a>
</h2>

Input properties used for looking up and filtering ProjectSink resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L117">property destination</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L123">property filter</a>
</h3>

```typescript
filter?: pulumi.Input<string>;
```


The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L127">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the logging sink.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L132">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project to create the sink in. If omitted, the project associated with the provider is
used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L139">property uniqueWriterIdentity</a>
</h3>

```typescript
uniqueWriterIdentity?: pulumi.Input<boolean>;
```


Whether or not to create a unique identity associated with this sink. If `false`
(the default), then the `writer_identity` used is `serviceAccount:cloud-logs@system.gserviceaccount.com`. If `true`,
then a unique service account is created and used for this sink. If you wish to publish logs across projects, you
must set `unique_writer_identity` to true.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/logging/projectSink.ts#L144">property writerIdentity</a>
</h3>

```typescript
writerIdentity?: pulumi.Input<string>;
```


The identity associated with this sink. This identity must be granted write access to the
configured `destination`.

