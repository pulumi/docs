---
title: Module dataproc
---

<a href="../index.html">@pulumi/gcp</a> &gt; dataproc

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#Job">class Job</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#JobArgs">interface JobArgs</a>
* <a href="#JobState">interface JobState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts">dataproc/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts">dataproc/job.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L16">class Cluster</a>
</h2>

Manages a Cloud Dataproc cluster resource within GCP. For more information see
[the official dataproc documentation](https://cloud.google.com/dataproc/).

!> **Warning:** Due to limitations of the API, all arguments except
`labels`,`cluster_config.worker_config.num_instances` and `cluster_config.preemptible_worker_config.num_instances` are non-updateable. Changing others will cause recreation of the
whole cluster!

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L54">constructor</a>
</h3>

```typescript
new Cluster(name: string, args?: ClusterArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L25">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState): Cluster
```


Get an existing Cluster resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L33">property clusterConfig</a>
</h3>

```typescript
public clusterConfig: pulumi.Output<{ ... }>;
```


Allows you to configure various aspects of the cluster.
Structure defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L39">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... }>;
```


The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L44">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the cluster, unique within the project and
zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L49">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L54">property region</a>
</h3>

```typescript
public region: pulumi.Output<string | undefined>;
```


The region in which the cluster and associated nodes will be created in.
Defaults to `global`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Job">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L13">class Job</a>
</h2>

Manages a job resource within a Dataproc cluster within GCE. For more information see
[the official dataproc documentation](https://cloud.google.com/dataproc/).

!> **Note:** This resource does not support 'update' and changing any attributes will cause the resource to be recreated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L66">constructor</a>
</h3>

```typescript
new Job(name: string, args: JobArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Job resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L22">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L29">property driverControlsFilesUri</a>
</h3>

```typescript
public driverControlsFilesUri: pulumi.Output<string>;
```


If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L33">property driverOutputResourceUri</a>
</h3>

```typescript
public driverOutputResourceUri: pulumi.Output<string>;
```


A URI pointing to the location of the stdout of the job's driver program.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L39">property forceDelete</a>
</h3>

```typescript
public forceDelete: pulumi.Output<boolean | undefined>;
```


By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L40">property hadoopConfig</a>
</h3>

```typescript
public hadoopConfig: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L41">property hiveConfig</a>
</h3>

```typescript
public hiveConfig: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L45">property labels</a>
</h3>

```typescript
public labels: pulumi.Output<{ ... } | undefined>;
```


The list of labels (key/value pairs) to add to the job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L46">property pigConfig</a>
</h3>

```typescript
public pigConfig: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L47">property placement</a>
</h3>

```typescript
public placement: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L52">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L53">property pysparkConfig</a>
</h3>

```typescript
public pysparkConfig: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L54">property reference</a>
</h3>

```typescript
public reference: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L59">property region</a>
</h3>

```typescript
public region: pulumi.Output<string | undefined>;
```


The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L63">property scheduling</a>
</h3>

```typescript
public scheduling: pulumi.Output<{ ... } | undefined>;
```


Optional. Job scheduling configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L64">property sparkConfig</a>
</h3>

```typescript
public sparkConfig: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L65">property sparksqlConfig</a>
</h3>

```typescript
public sparksqlConfig: pulumi.Output<{ ... } | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L66">property status</a>
</h3>

```typescript
public status: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L120">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L125">property clusterConfig</a>
</h3>

```typescript
clusterConfig?: pulumi.Input<{ ... }>;
```


Allows you to configure various aspects of the cluster.
Structure defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L131">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster, unique within the project and
zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L141">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L146">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which the cluster and associated nodes will be created in.
Defaults to `global`.

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L88">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L93">property clusterConfig</a>
</h3>

```typescript
clusterConfig?: pulumi.Input<{ ... }>;
```


Allows you to configure various aspects of the cluster.
Structure defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L99">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including `goog-dataproc-cluster-name`
which is the name of the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster, unique within the project and
zone.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L109">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The ID of the project in which the `cluster` will exist. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/cluster.ts#L114">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The region in which the cluster and associated nodes will be created in.
Defaults to `global`.

<h2 class="pdoc-module-header" id="JobArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L172">interface JobArgs</a>
</h2>

The set of arguments for constructing a Job resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L178">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L179">property hadoopConfig</a>
</h3>

```typescript
hadoopConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L180">property hiveConfig</a>
</h3>

```typescript
hiveConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L184">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


The list of labels (key/value pairs) to add to the job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L185">property pigConfig</a>
</h3>

```typescript
pigConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L186">property placement</a>
</h3>

```typescript
placement: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L191">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L192">property pysparkConfig</a>
</h3>

```typescript
pysparkConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L193">property reference</a>
</h3>

```typescript
reference?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L198">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L202">property scheduling</a>
</h3>

```typescript
scheduling?: pulumi.Input<{ ... }>;
```


Optional. Job scheduling configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L203">property sparkConfig</a>
</h3>

```typescript
sparkConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L204">property sparksqlConfig</a>
</h3>

```typescript
sparksqlConfig?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="JobState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L125">interface JobState</a>
</h2>

Input properties used for looking up and filtering Job resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L129">property driverControlsFilesUri</a>
</h3>

```typescript
driverControlsFilesUri?: pulumi.Input<string>;
```


If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L133">property driverOutputResourceUri</a>
</h3>

```typescript
driverOutputResourceUri?: pulumi.Input<string>;
```


A URI pointing to the location of the stdout of the job's driver program.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L139">property forceDelete</a>
</h3>

```typescript
forceDelete?: pulumi.Input<boolean>;
```


By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L140">property hadoopConfig</a>
</h3>

```typescript
hadoopConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L141">property hiveConfig</a>
</h3>

```typescript
hiveConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L145">property labels</a>
</h3>

```typescript
labels?: pulumi.Input<{ ... }>;
```


The list of labels (key/value pairs) to add to the job.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L146">property pigConfig</a>
</h3>

```typescript
pigConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L147">property placement</a>
</h3>

```typescript
placement?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L152">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the `cluster` can be found and jobs
subsequently run against. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L153">property pysparkConfig</a>
</h3>

```typescript
pysparkConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L154">property reference</a>
</h3>

```typescript
reference?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L159">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to `global`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L163">property scheduling</a>
</h3>

```typescript
scheduling?: pulumi.Input<{ ... }>;
```


Optional. Job scheduling configuration.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L164">property sparkConfig</a>
</h3>

```typescript
sparkConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L165">property sparksqlConfig</a>
</h3>

```typescript
sparksqlConfig?: pulumi.Input<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/dataproc/job.ts#L166">property status</a>
</h3>

```typescript
status?: pulumi.Input<{ ... }>;
```

