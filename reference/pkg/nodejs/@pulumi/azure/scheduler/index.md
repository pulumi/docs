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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L10">class Job</a>
</h2>

Manages a Scheduler Job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L66">constructor</a>
</h3>

```typescript
new Job(name: string, args: JobArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Job resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L26">property actionStorageQueue</a>
</h3>

```typescript
public actionStorageQueue: pulumi.Output<{ ... } | undefined>;
```


A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L30">property actionWeb</a>
</h3>

```typescript
public actionWeb: pulumi.Output<{ ... } | undefined>;
```


A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L34">property errorActionStorageQueue</a>
</h3>

```typescript
public errorActionStorageQueue: pulumi.Output<{ ... } | undefined>;
```


A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L38">property errorActionWeb</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L42">property jobCollectionName</a>
</h3>

```typescript
public jobCollectionName: pulumi.Output<string>;
```


Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L46">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L50">property recurrence</a>
</h3>

```typescript
public recurrence: pulumi.Output<{ ... } | undefined>;
```


A `recurrence` block defining a job occurrence schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L54">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L58">property retry</a>
</h3>

```typescript
public retry: pulumi.Output<{ ... } | undefined>;
```


A `retry` block defining how to retry as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L62">property startTime</a>
</h3>

```typescript
public startTime: pulumi.Output<string>;
```


The time the first instance of the job is to start running at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L66">property state</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L10">class JobCollection</a>
</h2>

Manages a Scheduler Job Collection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L50">constructor</a>
</h3>

```typescript
new JobCollection(name: string, args: JobCollectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a JobCollection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L34">property quota</a>
</h3>

```typescript
public quota: pulumi.Output<{ ... } | undefined>;
```


Configures the Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L42">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L46">property state</a>
</h3>

```typescript
public state: pulumi.Output<string | undefined>;
```


Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L50">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L10">function getJobCollection</a>
</h2>

```typescript
getJobCollection(args: GetJobCollectionArgs, opts?: pulumi.InvokeOptions): Promise<GetJobCollectionResult>
```


Use this data source to access the properties of an Azure scheduler job collection.

<h2 class="pdoc-module-header" id="GetJobCollectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L20">interface GetJobCollectionArgs</a>
</h2>

A collection of arguments for invoking getJobCollection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Scheduler Job Collection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group in which the Scheduler Job Collection resides.

<h2 class="pdoc-module-header" id="GetJobCollectionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L34">interface GetJobCollectionResult</a>
</h2>

A collection of values returned by getJobCollection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L58">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L38">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L42">property quotas</a>
</h3>

```typescript
quotas: { ... }[];
```


The Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L46">property sku</a>
</h3>

```typescript
sku: string;
```


The Job Collection's pricing level's SKU.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L50">property state</a>
</h3>

```typescript
state: string;
```


The Job Collection's state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L54">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="JobArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L168">interface JobArgs</a>
</h2>

The set of arguments for constructing a Job resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L172">property actionStorageQueue</a>
</h3>

```typescript
actionStorageQueue?: pulumi.Input<{ ... }>;
```


A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L176">property actionWeb</a>
</h3>

```typescript
actionWeb?: pulumi.Input<{ ... }>;
```


A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L180">property errorActionStorageQueue</a>
</h3>

```typescript
errorActionStorageQueue?: pulumi.Input<{ ... }>;
```


A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L184">property errorActionWeb</a>
</h3>

```typescript
errorActionWeb?: pulumi.Input<{ ... }>;
```


A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L188">property jobCollectionName</a>
</h3>

```typescript
jobCollectionName: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L192">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L196">property recurrence</a>
</h3>

```typescript
recurrence?: pulumi.Input<{ ... }>;
```


A `recurrence` block defining a job occurrence schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L200">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L204">property retry</a>
</h3>

```typescript
retry?: pulumi.Input<{ ... }>;
```


A `retry` block defining how to retry as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L208">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The time the first instance of the job is to start running at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L212">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`

<h2 class="pdoc-module-header" id="JobCollectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L131">interface JobCollectionArgs</a>
</h2>

The set of arguments for constructing a JobCollection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L135">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L139">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L143">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<{ ... }>;
```


Configures the Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L147">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L151">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L155">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L159">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="JobCollectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L97">interface JobCollectionState</a>
</h2>

Input properties used for looking up and filtering JobCollection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L101">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L105">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L109">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<{ ... }>;
```


Configures the Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L113">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L117">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L121">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L125">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="JobState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L118">interface JobState</a>
</h2>

Input properties used for looking up and filtering Job resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L122">property actionStorageQueue</a>
</h3>

```typescript
actionStorageQueue?: pulumi.Input<{ ... }>;
```


A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L126">property actionWeb</a>
</h3>

```typescript
actionWeb?: pulumi.Input<{ ... }>;
```


A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L130">property errorActionStorageQueue</a>
</h3>

```typescript
errorActionStorageQueue?: pulumi.Input<{ ... }>;
```


A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L134">property errorActionWeb</a>
</h3>

```typescript
errorActionWeb?: pulumi.Input<{ ... }>;
```


A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L138">property jobCollectionName</a>
</h3>

```typescript
jobCollectionName?: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L142">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L146">property recurrence</a>
</h3>

```typescript
recurrence?: pulumi.Input<{ ... }>;
```


A `recurrence` block defining a job occurrence schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L150">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L154">property retry</a>
</h3>

```typescript
retry?: pulumi.Input<{ ... }>;
```


A `retry` block defining how to retry as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L158">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The time the first instance of the job is to start running at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L162">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`

