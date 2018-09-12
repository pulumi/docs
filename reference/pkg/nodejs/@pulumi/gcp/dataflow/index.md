---
title: Module dataflow
---

<a href="../index.html">@pulumi/gcp</a> &gt; dataflow

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Job">class Job</a>
* <a href="#JobArgs">interface JobArgs</a>
* <a href="#JobState">interface JobState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts">dataflow/job.ts</a> 


<h2 class="pdoc-module-header" id="Job">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L13">class Job</a>
</h2>

Creates a job on Dataflow, which is an implementation of Apache Beam running on Google Compute Engine. For more information see
the official documentation for
[Beam](https://beam.apache.org) and [Dataflow](https://cloud.google.com/dataflow/).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L61">constructor</a>
</h3>

```typescript
new Job(name: string, args: JobArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Job resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JobState): Job
```


Get an existing Job resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L29">property maxWorkers</a>
</h3>

```typescript
public maxWorkers: pulumi.Output<number | undefined>;
```


The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by Dataflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L37">property onDelete</a>
</h3>

```typescript
public onDelete: pulumi.Output<string | undefined>;
```


One of "drain" or "cancel".  Specifies behavior of deletion during `terraform destroy`.  See above note.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L41">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... } | undefined>;
```


Key/Value pairs to be passed to the Dataflow job (as used in the template).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L45">property project</a>
</h3>

```typescript
public project: pulumi.Output<string | undefined>;
```


The project in which the resource belongs. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L49">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The current state of the resource, selected from the [JobState enum](https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.JobState)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L53">property tempGcsLocation</a>
</h3>

```typescript
public tempGcsLocation: pulumi.Output<string>;
```


A writeable location on GCS for the Dataflow job to dump its temporary data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L57">property templateGcsPath</a>
</h3>

```typescript
public templateGcsPath: pulumi.Output<string>;
```


The GCS path to the Dataflow job template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L61">property zone</a>
</h3>

```typescript
public zone: pulumi.Output<string | undefined>;
```


The zone in which the created job should run. If it is not provided, the provider zone is used.

<h2 class="pdoc-module-header" id="JobArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L151">interface JobArgs</a>
</h2>

The set of arguments for constructing a Job resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L155">property maxWorkers</a>
</h3>

```typescript
maxWorkers?: pulumi.Input<number>;
```


The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L159">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by Dataflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L163">property onDelete</a>
</h3>

```typescript
onDelete?: pulumi.Input<string>;
```


One of "drain" or "cancel".  Specifies behavior of deletion during `terraform destroy`.  See above note.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L167">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


Key/Value pairs to be passed to the Dataflow job (as used in the template).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L171">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L175">property tempGcsLocation</a>
</h3>

```typescript
tempGcsLocation: pulumi.Input<string>;
```


A writeable location on GCS for the Dataflow job to dump its temporary data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L179">property templateGcsPath</a>
</h3>

```typescript
templateGcsPath: pulumi.Input<string>;
```


The GCS path to the Dataflow job template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L183">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone in which the created job should run. If it is not provided, the provider zone is used.

<h2 class="pdoc-module-header" id="JobState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L109">interface JobState</a>
</h2>

Input properties used for looking up and filtering Job resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L113">property maxWorkers</a>
</h3>

```typescript
maxWorkers?: pulumi.Input<number>;
```


The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L117">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by Dataflow.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L121">property onDelete</a>
</h3>

```typescript
onDelete?: pulumi.Input<string>;
```


One of "drain" or "cancel".  Specifies behavior of deletion during `terraform destroy`.  See above note.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L125">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


Key/Value pairs to be passed to the Dataflow job (as used in the template).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L129">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L133">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The current state of the resource, selected from the [JobState enum](https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.JobState)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L137">property tempGcsLocation</a>
</h3>

```typescript
tempGcsLocation?: pulumi.Input<string>;
```


A writeable location on GCS for the Dataflow job to dump its temporary data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L141">property templateGcsPath</a>
</h3>

```typescript
templateGcsPath?: pulumi.Input<string>;
```


The GCS path to the Dataflow job template.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataflow/job.ts#L145">property zone</a>
</h3>

```typescript
zone?: pulumi.Input<string>;
```


The zone in which the created job should run. If it is not provided, the provider zone is used.

