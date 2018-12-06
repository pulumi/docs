---
title: Module scheduler
---

<a href="../index.html">@pulumi/azure</a> &gt; scheduler

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Job">class Job</a>
* <a href="#JobCollection">class JobCollection</a>
* <a href="#getJobCollection">function getJobCollection</a>
* <a href="#GetJobCollectionArgs">interface GetJobCollectionArgs</a>
* <a href="#GetJobCollectionResult">interface GetJobCollectionResult</a>
* <a href="#JobArgs">interface JobArgs</a>
* <a href="#JobCollectionArgs">interface JobCollectionArgs</a>
* <a href="#JobCollectionState">interface JobCollectionState</a>
* <a href="#JobState">interface JobState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts">scheduler/getJobCollection.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts">scheduler/job.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts">scheduler/jobCollection.ts</a> 


<h2 class="pdoc-module-header" id="Job">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L12">class Job</a>
</h2>

Manages a Scheduler Job.

~> **NOTE:** Support for Scheduler Job has been deprecated by Microsoft in favour of Logic Apps ([more information can be found at this link](https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps)) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L68">constructor</a>
</h3>

```typescript
new Job(name: string, args: JobArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Job resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JobState): Job
```


Get an existing Job resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L28">property actionStorageQueue</a>
</h3>

```typescript
public actionStorageQueue: pulumi.Output<{ ... } | undefined>;
```


A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L32">property actionWeb</a>
</h3>

```typescript
public actionWeb: pulumi.Output<{ ... } | undefined>;
```


A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L36">property errorActionStorageQueue</a>
</h3>

```typescript
public errorActionStorageQueue: pulumi.Output<{ ... } | undefined>;
```


A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L40">property errorActionWeb</a>
</h3>

```typescript
public errorActionWeb: pulumi.Output<{ ... } | undefined>;
```


A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L44">property jobCollectionName</a>
</h3>

```typescript
public jobCollectionName: pulumi.Output<string>;
```


Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L48">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L52">property recurrence</a>
</h3>

```typescript
public recurrence: pulumi.Output<{ ... } | undefined>;
```


A `recurrence` block defining a job occurrence schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L56">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L60">property retry</a>
</h3>

```typescript
public retry: pulumi.Output<{ ... } | undefined>;
```


A `retry` block defining how to retry as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L64">property startTime</a>
</h3>

```typescript
public startTime: pulumi.Output<string>;
```


The time the first instance of the job is to start running at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L68">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="JobCollection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L12">class JobCollection</a>
</h2>

Manages a Scheduler Job Collection.

~> **NOTE:** Support for Scheduler Job Collections has been deprecated by Microsoft in favour of Logic Apps ([more information can be found at this link](https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps)) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L52">constructor</a>
</h3>

```typescript
new JobCollection(name: string, args: JobCollectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a JobCollection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JobCollectionState): JobCollection
```


Get an existing JobCollection resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L28">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L32">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L36">property quota</a>
</h3>

```typescript
public quota: pulumi.Output<{ ... } | undefined>;
```


Configures the Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L40">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L44">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L48">property state</a>
</h3>

```typescript
public state: pulumi.Output<string | undefined>;
```


Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L52">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getJobCollection">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L12">function getJobCollection</a>
</h2>

```typescript
getJobCollection(args: GetJobCollectionArgs, opts?: pulumi.InvokeOptions): Promise<GetJobCollectionResult>
```


Use this data source to access information about an existing Scheduler Job Collection.

~> **NOTE:** Support for Scheduler Job Collections has been deprecated by Microsoft in favour of Logic Apps ([more information can be found at this link](https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps)) - as such we plan to remove support for this data source as a part of version 2.0 of the AzureRM Provider.

<h2 class="pdoc-module-header" id="GetJobCollectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L22">interface GetJobCollectionArgs</a>
</h2>

A collection of arguments for invoking getJobCollection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L26">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Scheduler Job Collection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L30">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group in which the Scheduler Job Collection resides.

<h2 class="pdoc-module-header" id="GetJobCollectionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L36">interface GetJobCollectionResult</a>
</h2>

A collection of values returned by getJobCollection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L60">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L40">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L44">property quotas</a>
</h3>

```typescript
quotas: { ... }[];
```


The Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L48">property sku</a>
</h3>

```typescript
sku: string;
```


The Job Collection's pricing level's SKU.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L52">property state</a>
</h3>

```typescript
state: string;
```


The Job Collection's state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L56">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="JobArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L170">interface JobArgs</a>
</h2>

The set of arguments for constructing a Job resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L174">property actionStorageQueue</a>
</h3>

```typescript
actionStorageQueue?: pulumi.Input<{ ... }>;
```


A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L178">property actionWeb</a>
</h3>

```typescript
actionWeb?: pulumi.Input<{ ... }>;
```


A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L182">property errorActionStorageQueue</a>
</h3>

```typescript
errorActionStorageQueue?: pulumi.Input<{ ... }>;
```


A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L186">property errorActionWeb</a>
</h3>

```typescript
errorActionWeb?: pulumi.Input<{ ... }>;
```


A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L190">property jobCollectionName</a>
</h3>

```typescript
jobCollectionName: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L194">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L198">property recurrence</a>
</h3>

```typescript
recurrence?: pulumi.Input<{ ... }>;
```


A `recurrence` block defining a job occurrence schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L202">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L206">property retry</a>
</h3>

```typescript
retry?: pulumi.Input<{ ... }>;
```


A `retry` block defining how to retry as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L210">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The time the first instance of the job is to start running at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L214">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`

<h2 class="pdoc-module-header" id="JobCollectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L133">interface JobCollectionArgs</a>
</h2>

The set of arguments for constructing a JobCollection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L137">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L145">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<{ ... }>;
```


Configures the Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L149">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L153">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L157">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L161">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="JobCollectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L99">interface JobCollectionState</a>
</h2>

Input properties used for looking up and filtering JobCollection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L103">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L107">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L111">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<{ ... }>;
```


Configures the Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L115">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L119">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L123">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L127">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="JobState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L120">interface JobState</a>
</h2>

Input properties used for looking up and filtering Job resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L124">property actionStorageQueue</a>
</h3>

```typescript
actionStorageQueue?: pulumi.Input<{ ... }>;
```


A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L128">property actionWeb</a>
</h3>

```typescript
actionWeb?: pulumi.Input<{ ... }>;
```


A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L132">property errorActionStorageQueue</a>
</h3>

```typescript
errorActionStorageQueue?: pulumi.Input<{ ... }>;
```


A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L136">property errorActionWeb</a>
</h3>

```typescript
errorActionWeb?: pulumi.Input<{ ... }>;
```


A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L140">property jobCollectionName</a>
</h3>

```typescript
jobCollectionName?: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L144">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L148">property recurrence</a>
</h3>

```typescript
recurrence?: pulumi.Input<{ ... }>;
```


A `recurrence` block defining a job occurrence schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L152">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L156">property retry</a>
</h3>

```typescript
retry?: pulumi.Input<{ ... }>;
```


A `retry` block defining how to retry as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L160">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The time the first instance of the job is to start running at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L164">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`

