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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L9">class Job</a>
</h2>

Manages a Scheduler Job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L65">constructor</a>
</h3>

```typescript
new Job(name: string, args: JobArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Job resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L25">property actionStorageQueue</a>
</h3>

```typescript
public actionStorageQueue: pulumi.Output<{ ... } | undefined>;
```


A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L29">property actionWeb</a>
</h3>

```typescript
public actionWeb: pulumi.Output<{ ... } | undefined>;
```


A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L33">property errorActionStorageQueue</a>
</h3>

```typescript
public errorActionStorageQueue: pulumi.Output<{ ... } | undefined>;
```


A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L37">property errorActionWeb</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L41">property jobCollectionName</a>
</h3>

```typescript
public jobCollectionName: pulumi.Output<string>;
```


Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L49">property recurrence</a>
</h3>

```typescript
public recurrence: pulumi.Output<{ ... } | undefined>;
```


A `recurrence` block defining a job occurrence schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L53">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L57">property retry</a>
</h3>

```typescript
public retry: pulumi.Output<{ ... } | undefined>;
```


A `retry` block defining how to retry as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L61">property startTime</a>
</h3>

```typescript
public startTime: pulumi.Output<string>;
```


The time the first instance of the job is to start running at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L65">property state</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L9">class JobCollection</a>
</h2>

Manages a Scheduler Job Collection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L49">constructor</a>
</h3>

```typescript
new JobCollection(name: string, args: JobCollectionArgs, opts?: pulumi.CustomResourceOptions)
```


Create a JobCollection resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L33">property quota</a>
</h3>

```typescript
public quota: pulumi.Output<{ ... } | undefined>;
```


Configures the Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L37">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L41">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L45">property state</a>
</h3>

```typescript
public state: pulumi.Output<string | undefined>;
```


Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L49">property tags</a>
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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L9">function getJobCollection</a>
</h2>

```typescript
getJobCollection(args: GetJobCollectionArgs, opts?: pulumi.InvokeOptions): Promise<GetJobCollectionResult>
```


Use this data source to access the properties of an Azure scheduler job collection.

<h2 class="pdoc-module-header" id="GetJobCollectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L19">interface GetJobCollectionArgs</a>
</h2>

A collection of arguments for invoking getJobCollection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Scheduler Job Collection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group in which the Scheduler Job Collection resides.

<h2 class="pdoc-module-header" id="GetJobCollectionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L33">interface GetJobCollectionResult</a>
</h2>

A collection of values returned by getJobCollection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L57">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L37">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the resource exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L41">property quotas</a>
</h3>

```typescript
quotas: { ... }[];
```


The Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L45">property sku</a>
</h3>

```typescript
sku: string;
```


The Job Collection's pricing level's SKU.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L49">property state</a>
</h3>

```typescript
state: string;
```


The Job Collection's state.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/getJobCollection.ts#L53">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="JobArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L167">interface JobArgs</a>
</h2>

The set of arguments for constructing a Job resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L171">property actionStorageQueue</a>
</h3>

```typescript
actionStorageQueue?: pulumi.Input<{ ... }>;
```


A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L175">property actionWeb</a>
</h3>

```typescript
actionWeb?: pulumi.Input<{ ... }>;
```


A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L179">property errorActionStorageQueue</a>
</h3>

```typescript
errorActionStorageQueue?: pulumi.Input<{ ... }>;
```


A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L183">property errorActionWeb</a>
</h3>

```typescript
errorActionWeb?: pulumi.Input<{ ... }>;
```


A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L187">property jobCollectionName</a>
</h3>

```typescript
jobCollectionName: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L191">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L195">property recurrence</a>
</h3>

```typescript
recurrence?: pulumi.Input<{ ... }>;
```


A `recurrence` block defining a job occurrence schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L199">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L203">property retry</a>
</h3>

```typescript
retry?: pulumi.Input<{ ... }>;
```


A `retry` block defining how to retry as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L207">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The time the first instance of the job is to start running at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L211">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`

<h2 class="pdoc-module-header" id="JobCollectionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L130">interface JobCollectionArgs</a>
</h2>

The set of arguments for constructing a JobCollection resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L134">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L138">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L142">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<{ ... }>;
```


Configures the Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L146">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L150">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L154">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L158">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="JobCollectionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L96">interface JobCollectionState</a>
</h2>

Input properties used for looking up and filtering JobCollection resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L100">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L108">property quota</a>
</h3>

```typescript
quota?: pulumi.Input<{ ... }>;
```


Configures the Job collection quotas as documented in the `quota` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L112">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L116">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Sets the Job Collection's pricing level's SKU. Possible values include: `Standard`, `Free`, `P10Premium`, `P20Premium`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L120">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


Sets Job Collection's state. Possible values include: `Enabled`, `Disabled`, `Suspended`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/jobCollection.ts#L124">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="JobState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L117">interface JobState</a>
</h2>

Input properties used for looking up and filtering Job resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L121">property actionStorageQueue</a>
</h3>

```typescript
actionStorageQueue?: pulumi.Input<{ ... }>;
```


A `action_storage_queue` block defining a storage queue job action as described below. Note this is identical to an `error_action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L125">property actionWeb</a>
</h3>

```typescript
actionWeb?: pulumi.Input<{ ... }>;
```


A `action_web` block defining the job action as described below. Note this is identical to an `error_action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L129">property errorActionStorageQueue</a>
</h3>

```typescript
errorActionStorageQueue?: pulumi.Input<{ ... }>;
```


A `error_action_storage_queue` block defining the a web action to take on an error as described below. Note this is identical to an `action_storage_queue` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L133">property errorActionWeb</a>
</h3>

```typescript
errorActionWeb?: pulumi.Input<{ ... }>;
```


A `error_action_web` block defining the action to take on an error as described below. Note this is identical to an `action_web` block.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L137">property jobCollectionName</a>
</h3>

```typescript
jobCollectionName?: pulumi.Input<string>;
```


Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L141">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L145">property recurrence</a>
</h3>

```typescript
recurrence?: pulumi.Input<{ ... }>;
```


A `recurrence` block defining a job occurrence schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L149">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L153">property retry</a>
</h3>

```typescript
retry?: pulumi.Input<{ ... }>;
```


A `retry` block defining how to retry as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L157">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


The time the first instance of the job is to start running at.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/scheduler/job.ts#L161">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The sets or gets the current state of the job. Can be set to either `Enabled` or `Completed`

