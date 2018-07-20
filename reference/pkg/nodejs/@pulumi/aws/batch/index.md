---
title: Module batch
---

<a href="../index.html">@pulumi/aws</a> &gt; batch

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ComputeEnvironment">class ComputeEnvironment</a>
* <a href="#JobDefinition">class JobDefinition</a>
* <a href="#JobQueue">class JobQueue</a>
* <a href="#getComputeEnvironment">function getComputeEnvironment</a>
* <a href="#getJobQueue">function getJobQueue</a>
* <a href="#ComputeEnvironmentArgs">interface ComputeEnvironmentArgs</a>
* <a href="#ComputeEnvironmentState">interface ComputeEnvironmentState</a>
* <a href="#GetComputeEnvironmentArgs">interface GetComputeEnvironmentArgs</a>
* <a href="#GetComputeEnvironmentResult">interface GetComputeEnvironmentResult</a>
* <a href="#GetJobQueueArgs">interface GetJobQueueArgs</a>
* <a href="#GetJobQueueResult">interface GetJobQueueResult</a>
* <a href="#JobDefinitionArgs">interface JobDefinitionArgs</a>
* <a href="#JobDefinitionState">interface JobDefinitionState</a>
* <a href="#JobQueueArgs">interface JobQueueArgs</a>
* <a href="#JobQueueState">interface JobQueueState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts">batch/computeEnvironment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts">batch/getComputeEnvironment.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts">batch/getJobQueue.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts">batch/jobDefinition.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts">batch/jobQueue.ts</a> 


<h2 class="pdoc-module-header" id="ComputeEnvironment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L15">class ComputeEnvironment</a>
</h2>

Creates a AWS Batch compute environment. Compute environments contain the Amazon ECS container instances that are used to run containerized batch jobs.

For information about AWS Batch, see [What is AWS Batch?][1] .
For information about compute environment, see [Compute Environments][2] .

~> **Note:** To prevent a race condition during environment deletion, make sure to set `depends_on` to the related `aws_iam_role_policy_attachment`;
   otherwise, the policy may be destroyed too soon and the compute environment will then get stuck in the `DELETING` state, see [Troubleshooting AWS Batch][3] .

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L64">constructor</a>
</h3>

```typescript
new ComputeEnvironment(name: string, args: ComputeEnvironmentArgs, opts?: pulumi.ResourceOptions)
```


Create a ComputeEnvironment resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ComputeEnvironmentState): ComputeEnvironment
```


Get an existing ComputeEnvironment resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L31">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L35">property computeEnvironmentName</a>
</h3>

```typescript
public computeEnvironmentName: pulumi.Output<string>;
```


The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L39">property computeResources</a>
</h3>

```typescript
public computeResources: pulumi.Output<{ ... } | undefined>;
```


Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L40">property eccClusterArn</a>
</h3>

```typescript
public eccClusterArn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L44">property ecsClusterArn</a>
</h3>

```typescript
public ecsClusterArn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L48">property serviceRole</a>
</h3>

```typescript
public serviceRole: pulumi.Output<string>;
```


The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L52">property state</a>
</h3>

```typescript
public state: pulumi.Output<string | undefined>;
```


The state of the compute environment. If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are `ENABLED` or `DISABLED`. Defaults to `ENABLED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L56">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```


The current status of the compute environment (for example, CREATING or VALID).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L60">property statusReason</a>
</h3>

```typescript
public statusReason: pulumi.Output<string>;
```


A short, human-readable string to provide additional details about the current status of the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L64">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of compute environment. Valid items are `EC2` or `SPOT`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="JobDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L9">class JobDefinition</a>
</h2>

Provides a Batch Job Definition resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L55">constructor</a>
</h3>

```typescript
new JobDefinition(name: string, args: JobDefinitionArgs, opts?: pulumi.ResourceOptions)
```


Create a JobDefinition resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JobDefinitionState): JobDefinition
```


Get an existing JobDefinition resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name of the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L30">property containerProperties</a>
</h3>

```typescript
public containerProperties: pulumi.Output<string | undefined>;
```


A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L38">property parameters</a>
</h3>

```typescript
public parameters: pulumi.Output<{ ... } | undefined>;
```


Specifies the parameter substitution placeholders to set in the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L43">property retryStrategy</a>
</h3>

```typescript
public retryStrategy: pulumi.Output<{ ... } | undefined>;
```


Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L47">property revision</a>
</h3>

```typescript
public revision: pulumi.Output<number>;
```


The revision of the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L51">property timeout</a>
</h3>

```typescript
public timeout: pulumi.Output<{ ... } | undefined>;
```


Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L55">property type</a>
</h3>

```typescript
public type: pulumi.Output<string>;
```


The type of job definition.  Must be `container`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="JobQueue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L9">class JobQueue</a>
</h2>

Provides a Batch Job Queue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L45">constructor</a>
</h3>

```typescript
new JobQueue(name: string, args: JobQueueArgs, opts?: pulumi.ResourceOptions)
```


Create a JobQueue resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: JobQueueState): JobQueue
```


Get an existing JobQueue resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name of the job queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L32">property computeEnvironments</a>
</h3>

```typescript
public computeEnvironments: pulumi.Output<string[]>;
```


Specifies the set of compute environments
mapped to a job queue and their order.  The position of the compute environments
in the list will dictate the order. You can associate up to 3 compute environments
with a job queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L36">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the job queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L41">property priority</a>
</h3>

```typescript
public priority: pulumi.Output<number>;
```


The priority of the job queue. Job queues with a higher priority
are evaluated first when associated with the same compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L45">property state</a>
</h3>

```typescript
public state: pulumi.Output<string>;
```


The state of the job queue. Must be one of: `ENABLED` or `DISABLED`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getComputeEnvironment">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L10">function getComputeEnvironment</a>
</h2>

```typescript
getComputeEnvironment(args: GetComputeEnvironmentArgs): Promise<GetComputeEnvironmentResult>
```


The Batch Compute Environment data source allows access to details of a specific
compute environment within AWS Batch.

<h2 class="pdoc-module-header" id="getJobQueue">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L10">function getJobQueue</a>
</h2>

```typescript
getJobQueue(args: GetJobQueueArgs): Promise<GetJobQueueResult>
```


The Batch Job Queue data source allows access to details of a specific
job queue within AWS Batch.

<h2 class="pdoc-module-header" id="ComputeEnvironmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L160">interface ComputeEnvironmentArgs</a>
</h2>

The set of arguments for constructing a ComputeEnvironment resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L164">property computeEnvironmentName</a>
</h3>

```typescript
computeEnvironmentName: pulumi.Input<string>;
```


The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L168">property computeResources</a>
</h3>

```typescript
computeResources?: pulumi.Input<{ ... }>;
```


Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L172">property serviceRole</a>
</h3>

```typescript
serviceRole: pulumi.Input<string>;
```


The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L176">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The state of the compute environment. If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are `ENABLED` or `DISABLED`. Defaults to `ENABLED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L180">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of compute environment. Valid items are `EC2` or `SPOT`.

<h2 class="pdoc-module-header" id="ComputeEnvironmentState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L117">interface ComputeEnvironmentState</a>
</h2>

Input properties used for looking up and filtering ComputeEnvironment resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L121">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L125">property computeEnvironmentName</a>
</h3>

```typescript
computeEnvironmentName?: pulumi.Input<string>;
```


The name for your compute environment. Up to 128 letters (uppercase and lowercase), numbers, and underscores are allowed.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L129">property computeResources</a>
</h3>

```typescript
computeResources?: pulumi.Input<{ ... }>;
```


Details of the compute resources managed by the compute environment. This parameter is required for managed compute environments. See details below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L130">property eccClusterArn</a>
</h3>

```typescript
eccClusterArn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L134">property ecsClusterArn</a>
</h3>

```typescript
ecsClusterArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the underlying Amazon ECS cluster used by the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L138">property serviceRole</a>
</h3>

```typescript
serviceRole?: pulumi.Input<string>;
```


The full Amazon Resource Name (ARN) of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L142">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The state of the compute environment. If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues. Valid items are `ENABLED` or `DISABLED`. Defaults to `ENABLED`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L146">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```


The current status of the compute environment (for example, CREATING or VALID).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L150">property statusReason</a>
</h3>

```typescript
statusReason?: pulumi.Input<string>;
```


A short, human-readable string to provide additional details about the current status of the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/computeEnvironment.ts#L154">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of compute environment. Valid items are `EC2` or `SPOT`.

<h2 class="pdoc-module-header" id="GetComputeEnvironmentArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L19">interface GetComputeEnvironmentArgs</a>
</h2>

A collection of arguments for invoking getComputeEnvironment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L23">property computeEnvironmentName</a>
</h3>

```typescript
computeEnvironmentName: pulumi.Input<string>;
```


The name of the Batch Compute Environment

<h2 class="pdoc-module-header" id="GetComputeEnvironmentResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L29">interface GetComputeEnvironmentResult</a>
</h2>

A collection of values returned by getComputeEnvironment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L33">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L37">property ecsClusterArn</a>
</h3>

```typescript
ecsClusterArn: string;
```


The ARN of the underlying Amazon ECS cluster used by the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L61">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L41">property serviceRole</a>
</h3>

```typescript
serviceRole: string;
```


The ARN of the IAM role that allows AWS Batch to make calls to other AWS services on your behalf.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L45">property state</a>
</h3>

```typescript
state: string;
```


The state of the compute environment (for example, `ENABLED` or `DISABLED`). If the state is `ENABLED`, then the compute environment accepts jobs from a queue and can scale out automatically based on queues.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L49">property status</a>
</h3>

```typescript
status: string;
```


The current status of the compute environment (for example, `CREATING` or `VALID`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L53">property statusReason</a>
</h3>

```typescript
statusReason: string;
```


A short, human-readable string to provide additional details about the current status of the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getComputeEnvironment.ts#L57">property type</a>
</h3>

```typescript
type: string;
```


The type of the compute environment (for example, `MANAGED` or `UNMANAGED`).

<h2 class="pdoc-module-header" id="GetJobQueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L19">interface GetJobQueueArgs</a>
</h2>

A collection of arguments for invoking getJobQueue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


The name of the job queue.

<h2 class="pdoc-module-header" id="GetJobQueueResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L29">interface GetJobQueueResult</a>
</h2>

A collection of values returned by getJobQueue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L33">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the job queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L40">property computeEnvironmentOrders</a>
</h3>

```typescript
computeEnvironmentOrders: { ... }[];
```


The compute environments that are attached to the job queue and the order in
which job placement is preferred. Compute environments are selected for job placement in ascending order.
* `compute_environment_order.#.order` - The order of the compute environment.
* `compute_environment_order.#.compute_environment` - The ARN of the compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L62">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L45">property priority</a>
</h3>

```typescript
priority: number;
```


The priority of the job queue. Job queues with a higher priority are evaluated first when
associated with the same compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L49">property state</a>
</h3>

```typescript
state: string;
```


Describes the ability of the queue to accept new jobs (for example, `ENABLED` or `DISABLED`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L53">property status</a>
</h3>

```typescript
status: string;
```


The current status of the job queue (for example, `CREATING` or `VALID`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/getJobQueue.ts#L58">property statusReason</a>
</h3>

```typescript
statusReason: string;
```


A short, human-readable string to provide additional details about the current status
of the job queue.

<h2 class="pdoc-module-header" id="JobDefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L138">interface JobDefinitionArgs</a>
</h2>

The set of arguments for constructing a JobDefinition resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L143">property containerProperties</a>
</h3>

```typescript
containerProperties?: pulumi.Input<string>;
```


A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L147">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L151">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


Specifies the parameter substitution placeholders to set in the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L156">property retryStrategy</a>
</h3>

```typescript
retryStrategy?: pulumi.Input<{ ... }>;
```


Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L160">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<{ ... }>;
```


Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L164">property type</a>
</h3>

```typescript
type: pulumi.Input<string>;
```


The type of job definition.  Must be `container`

<h2 class="pdoc-module-header" id="JobDefinitionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L98">interface JobDefinitionState</a>
</h2>

Input properties used for looking up and filtering JobDefinition resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L102">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name of the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L107">property containerProperties</a>
</h3>

```typescript
containerProperties?: pulumi.Input<string>;
```


A valid [container properties](http://docs.aws.amazon.com/batch/latest/APIReference/API_RegisterJobDefinition.html)
provided as a single valid JSON document. This parameter is required if the `type` parameter is `container`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L111">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L115">property parameters</a>
</h3>

```typescript
parameters?: pulumi.Input<{ ... }>;
```


Specifies the parameter substitution placeholders to set in the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L120">property retryStrategy</a>
</h3>

```typescript
retryStrategy?: pulumi.Input<{ ... }>;
```


Specifies the retry strategy to use for failed jobs that are submitted with this job definition.
Maximum number of `retry_strategy` is `1`.  Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L124">property revision</a>
</h3>

```typescript
revision?: pulumi.Input<number>;
```


The revision of the job definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L128">property timeout</a>
</h3>

```typescript
timeout?: pulumi.Input<{ ... }>;
```


Specifies the timeout for jobs so that if a job runs longer, AWS Batch terminates the job. Maximum number of `timeout` is `1`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobDefinition.ts#L132">property type</a>
</h3>

```typescript
type?: pulumi.Input<string>;
```


The type of job definition.  Must be `container`

<h2 class="pdoc-module-header" id="JobQueueArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L118">interface JobQueueArgs</a>
</h2>

The set of arguments for constructing a JobQueue resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L125">property computeEnvironments</a>
</h3>

```typescript
computeEnvironments: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies the set of compute environments
mapped to a job queue and their order.  The position of the compute environments
in the list will dictate the order. You can associate up to 3 compute environments
with a job queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L129">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the job queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L134">property priority</a>
</h3>

```typescript
priority: pulumi.Input<number>;
```


The priority of the job queue. Job queues with a higher priority
are evaluated first when associated with the same compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L138">property state</a>
</h3>

```typescript
state: pulumi.Input<string>;
```


The state of the job queue. Must be one of: `ENABLED` or `DISABLED`

<h2 class="pdoc-module-header" id="JobQueueState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L88">interface JobQueueState</a>
</h2>

Input properties used for looking up and filtering JobQueue resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L92">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name of the job queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L99">property computeEnvironments</a>
</h3>

```typescript
computeEnvironments?: pulumi.Input<pulumi.Input<string>[]>;
```


Specifies the set of compute environments
mapped to a job queue and their order.  The position of the compute environments
in the list will dictate the order. You can associate up to 3 compute environments
with a job queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the job queue.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L108">property priority</a>
</h3>

```typescript
priority?: pulumi.Input<number>;
```


The priority of the job queue. Job queues with a higher priority
are evaluated first when associated with the same compute environment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/batch/jobQueue.ts#L112">property state</a>
</h3>

```typescript
state?: pulumi.Input<string>;
```


The state of the job queue. Must be one of: `ENABLED` or `DISABLED`

