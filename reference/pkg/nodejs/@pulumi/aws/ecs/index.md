---
title: Module ecs
---

<a href="../index.html">@pulumi/aws</a> &gt; ecs

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#Service">class Service</a>
* <a href="#TaskDefinition">class TaskDefinition</a>
* <a href="#getCluster">function getCluster</a>
* <a href="#getContainerDefinition">function getContainerDefinition</a>
* <a href="#getService">function getService</a>
* <a href="#getTaskDefinition">function getTaskDefinition</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#ContainerDefinition">interface ContainerDefinition</a>
* <a href="#Device">interface Device</a>
* <a href="#GetClusterArgs">interface GetClusterArgs</a>
* <a href="#GetClusterResult">interface GetClusterResult</a>
* <a href="#GetContainerDefinitionArgs">interface GetContainerDefinitionArgs</a>
* <a href="#GetContainerDefinitionResult">interface GetContainerDefinitionResult</a>
* <a href="#GetServiceArgs">interface GetServiceArgs</a>
* <a href="#GetServiceResult">interface GetServiceResult</a>
* <a href="#GetTaskDefinitionArgs">interface GetTaskDefinitionArgs</a>
* <a href="#GetTaskDefinitionResult">interface GetTaskDefinitionResult</a>
* <a href="#HostEntry">interface HostEntry</a>
* <a href="#KernelCapabilities">interface KernelCapabilities</a>
* <a href="#KeyValuePair">interface KeyValuePair</a>
* <a href="#LinuxParameters">interface LinuxParameters</a>
* <a href="#LogConfiguration">interface LogConfiguration</a>
* <a href="#MountPoint">interface MountPoint</a>
* <a href="#PortMapping">interface PortMapping</a>
* <a href="#ServiceArgs">interface ServiceArgs</a>
* <a href="#ServiceState">interface ServiceState</a>
* <a href="#TaskDefinitionArgs">interface TaskDefinitionArgs</a>
* <a href="#TaskDefinitionState">interface TaskDefinitionState</a>
* <a href="#Ulimit">interface Ulimit</a>
* <a href="#VolumeFrom">interface VolumeFrom</a>
* <a href="#KernelCapability">type KernelCapability</a>
* <a href="#LogDriver">type LogDriver</a>
* <a href="#Protocol">type Protocol</a>
* <a href="#UlimitName">type UlimitName</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts">ecs/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts">ecs/container.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts">ecs/getCluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts">ecs/getContainerDefinition.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts">ecs/getService.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts">ecs/getTaskDefinition.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts">ecs/service.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts">ecs/taskDefinition.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L9">class Cluster</a>
</h2>

Provides an ECS cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L29">constructor</a>
</h3>

```typescript
new Cluster(name: string, args?: ClusterArgs, opts?: pulumi.ResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ClusterState): Cluster
```


Get an existing Cluster resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


The Amazon Resource Name (ARN) that identifies the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Service">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L13">class Service</a>
</h2>

-> **Note:** To prevent a race condition during service deletion, make sure to set `depends_on` to the related `aws_iam_role_policy`; otherwise, the policy may be destroyed too soon and the ECS service will then get stuck in the `DRAINING` state.

Provides an ECS service - effectively a task that is expected to run until an error occurs or a user terminates it (typically a webserver or a database).

See [ECS Services section in AWS developer guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs_services.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L90">constructor</a>
</h3>

```typescript
new Service(name: string, args: ServiceArgs, opts?: pulumi.ResourceOptions)
```


Create a Service resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceState): Service
```


Get an existing Service resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L29">property cluster</a>
</h3>

```typescript
public cluster: pulumi.Output<string>;
```


ARN of an ECS cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L33">property deploymentMaximumPercent</a>
</h3>

```typescript
public deploymentMaximumPercent: pulumi.Output<number | undefined>;
```


The upper limit (as a percentage of the service's desiredCount) of the number of running tasks that can be running in a service during a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L37">property deploymentMinimumHealthyPercent</a>
</h3>

```typescript
public deploymentMinimumHealthyPercent: pulumi.Output<number | undefined>;
```


The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L41">property desiredCount</a>
</h3>

```typescript
public desiredCount: pulumi.Output<number | undefined>;
```


The number of instances of the task definition to place and keep running

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L45">property healthCheckGracePeriodSeconds</a>
</h3>

```typescript
public healthCheckGracePeriodSeconds: pulumi.Output<number | undefined>;
```


Seconds to ignore failing load balancer health checks on newly instantiated tasks to prevent premature shutdown, up to 7200. Only valid for services configured to use load balancers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L49">property iamRole</a>
</h3>

```typescript
public iamRole: pulumi.Output<string>;
```


ARN of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is required if you are using a load balancer with your service, but only if your task definition does not use the `awsvpc` network mode. If using `awsvpc` network mode, do not specify this role. If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L53">property launchType</a>
</h3>

```typescript
public launchType: pulumi.Output<string | undefined>;
```


The launch type on which to run your service. The valid values are `EC2` and `FARGATE`. Defaults to `EC2`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L57">property loadBalancers</a>
</h3>

```typescript
public loadBalancers: pulumi.Output<{ ... }[] | undefined>;
```


A load balancer block. Load balancers documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L61">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the service (up to 255 letters, numbers, hyphens, and underscores)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L65">property networkConfiguration</a>
</h3>

```typescript
public networkConfiguration: pulumi.Output<{ ... } | undefined>;
```


The network configuration for the service. This parameter is required for task definitions that use the `awsvpc` network mode to receive their own Elastic Network Interface, and it is not supported for other network modes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L69">property orderedPlacementStrategies</a>
</h3>

```typescript
public orderedPlacementStrategies: pulumi.Output<{ ... }[] | undefined>;
```


Service level strategy rules that are taken into consideration during task placement. List from top to bottom in order of precedence. The maximum number of `ordered_placement_strategy` blocks is `5`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L74">property placementConstraints</a>
</h3>

```typescript
public placementConstraints: pulumi.Output<{ ... }[] | undefined>;
```


rules that are taken into consideration during task placement. Maximum number of
`placement_constraints` is `10`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L78">property placementStrategies</a>
</h3>

```typescript
public placementStrategies: pulumi.Output<{ ... }[] | undefined>;
```


**Deprecated**, use `ordered_placement_strategy` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L82">property serviceRegistries</a>
</h3>

```typescript
public serviceRegistries: pulumi.Output<{ ... } | undefined>;
```


The service discovery registries for the service. The maximum number of `service_registries` blocks is `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L86">property taskDefinition</a>
</h3>

```typescript
public taskDefinition: pulumi.Output<string>;
```


The family and revision (`family:revision`) or full ARN of the task definition that you want to run in your service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L90">property waitForSteadyState</a>
</h3>

```typescript
public waitForSteadyState: pulumi.Output<boolean | undefined>;
```


If `true`, Terraform will wait for the service to reach a steady state (like [`aws ecs wait services-stable`](https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html)) before continuing. Default `false`.

<h2 class="pdoc-module-header" id="TaskDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L9">class TaskDefinition</a>
</h2>

Provides an ECS task definition to be used in `aws_ecs_service`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L74">constructor</a>
</h3>

```typescript
new TaskDefinition(name: string, args: TaskDefinitionArgs, opts?: pulumi.ResourceOptions)
```


Create a TaskDefinition resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TaskDefinitionState): TaskDefinition
```


Get an existing TaskDefinition resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L25">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```


Full ARN of the Task Definition (including both `family` and `revision`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L34">property containerDefinitions</a>
</h3>

```typescript
public containerDefinitions: pulumi.Output<string>;
```


A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L38">property cpu</a>
</h3>

```typescript
public cpu: pulumi.Output<string | undefined>;
```


The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L42">property executionRoleArn</a>
</h3>

```typescript
public executionRoleArn: pulumi.Output<string | undefined>;
```


The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L46">property family</a>
</h3>

```typescript
public family: pulumi.Output<string>;
```


A unique name for your task definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L50">property memory</a>
</h3>

```typescript
public memory: pulumi.Output<string | undefined>;
```


The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L54">property networkMode</a>
</h3>

```typescript
public networkMode: pulumi.Output<string>;
```


The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L58">property placementConstraints</a>
</h3>

```typescript
public placementConstraints: pulumi.Output<{ ... }[] | undefined>;
```


A set of [placement constraints](#placement-constraints-arguments) rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L62">property requiresCompatibilities</a>
</h3>

```typescript
public requiresCompatibilities: pulumi.Output<string[] | undefined>;
```


A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L66">property revision</a>
</h3>

```typescript
public revision: pulumi.Output<number>;
```


The revision of the task in a particular family.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L70">property taskRoleArn</a>
</h3>

```typescript
public taskRoleArn: pulumi.Output<string | undefined>;
```


The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L74">property volumes</a>
</h3>

```typescript
public volumes: pulumi.Output<{ ... }[] | undefined>;
```


A set of [volume blocks](#volume-block-arguments) that containers in your task may use.

<h2 class="pdoc-module-header" id="getCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts#L10">function getCluster</a>
</h2>

```typescript
getCluster(args: GetClusterArgs): Promise<GetClusterResult>
```


The ECS Cluster data source allows access to details of a specific
cluster within an AWS ECS service.

<h2 class="pdoc-module-header" id="getContainerDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L10">function getContainerDefinition</a>
</h2>

```typescript
getContainerDefinition(args: GetContainerDefinitionArgs): Promise<GetContainerDefinitionResult>
```


The ECS container definition data source allows access to details of
a specific container within an AWS ECS service.

<h2 class="pdoc-module-header" id="getService">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts#L10">function getService</a>
</h2>

```typescript
getService(args: GetServiceArgs): Promise<GetServiceResult>
```


The ECS Service data source allows access to details of a specific
Service within a AWS ECS Cluster.

<h2 class="pdoc-module-header" id="getTaskDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts#L11">function getTaskDefinition</a>
</h2>

```typescript
getTaskDefinition(args: GetTaskDefinitionArgs): Promise<GetTaskDefinitionResult>
```


The ECS task definition data source allows access to details of
a specific AWS ECS task definition.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L71">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L75">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L57">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L61">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) that identifies the cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/cluster.ts#L65">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the cluster (up to 255 letters, numbers, hyphens, and underscores)

<h2 class="pdoc-module-header" id="ContainerDefinition">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L19">interface ContainerDefinition</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L20">property command</a>
</h3>

```typescript
command?: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L21">property cpu</a>
</h3>

```typescript
cpu?: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L22">property disableNetworking</a>
</h3>

```typescript
disableNetworking?: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L23">property dnsSearchDomains</a>
</h3>

```typescript
dnsSearchDomains?: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L24">property dnsServers</a>
</h3>

```typescript
dnsServers?: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L25">property dockerLabels</a>
</h3>

```typescript
dockerLabels?: { ... };
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L26">property dockerSecurityOptions</a>
</h3>

```typescript
dockerSecurityOptions?: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L27">property entryPoint</a>
</h3>

```typescript
entryPoint?: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L28">property environment</a>
</h3>

```typescript
environment?: KeyValuePair[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L29">property essential</a>
</h3>

```typescript
essential?: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L30">property extraHosts</a>
</h3>

```typescript
extraHosts?: HostEntry[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L31">property hostname</a>
</h3>

```typescript
hostname?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L32">property image</a>
</h3>

```typescript
image?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L33">property links</a>
</h3>

```typescript
links?: string[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L34">property linuxParameters</a>
</h3>

```typescript
linuxParameters?: LinuxParameters;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L35">property logConfiguration</a>
</h3>

```typescript
logConfiguration?: LogConfiguration;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L36">property memory</a>
</h3>

```typescript
memory?: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L37">property memoryReservation</a>
</h3>

```typescript
memoryReservation?: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L38">property mountPoints</a>
</h3>

```typescript
mountPoints?: MountPoint[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L39">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L40">property portMappings</a>
</h3>

```typescript
portMappings?: PortMapping[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L41">property privileged</a>
</h3>

```typescript
privileged?: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L42">property readonlyRootFilesystem</a>
</h3>

```typescript
readonlyRootFilesystem?: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L43">property ulimits</a>
</h3>

```typescript
ulimits?: Ulimit[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L44">property user</a>
</h3>

```typescript
user?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L45">property volumesFrom</a>
</h3>

```typescript
volumesFrom?: VolumeFrom[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L46">property workingDirectory</a>
</h3>

```typescript
workingDirectory?: string;
```

<h2 class="pdoc-module-header" id="Device">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L83">interface Device</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L84">property containerPath</a>
</h3>

```typescript
containerPath?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L85">property hostPath</a>
</h3>

```typescript
hostPath: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L86">property permissions</a>
</h3>

```typescript
permissions?: string[];
```

<h2 class="pdoc-module-header" id="GetClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts#L19">interface GetClusterArgs</a>
</h2>

A collection of arguments for invoking getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts#L23">property clusterName</a>
</h3>

```typescript
clusterName: pulumi.Input<string>;
```


The name of the ECS Cluster

<h2 class="pdoc-module-header" id="GetClusterResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts#L29">interface GetClusterResult</a>
</h2>

A collection of values returned by getCluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts#L33">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the ECS Cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts#L37">property pendingTasksCount</a>
</h3>

```typescript
pendingTasksCount: number;
```


The number of pending tasks for the ECS Cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts#L41">property registeredContainerInstancesCount</a>
</h3>

```typescript
registeredContainerInstancesCount: number;
```


The number of registered container instances for the ECS Cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts#L45">property runningTasksCount</a>
</h3>

```typescript
runningTasksCount: number;
```


The number of running tasks for the ECS Cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getCluster.ts#L49">property status</a>
</h3>

```typescript
status: string;
```


The status of the ECS Cluster

<h2 class="pdoc-module-header" id="GetContainerDefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L20">interface GetContainerDefinitionArgs</a>
</h2>

A collection of arguments for invoking getContainerDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L24">property containerName</a>
</h3>

```typescript
containerName: pulumi.Input<string>;
```


The name of the container definition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L28">property taskDefinition</a>
</h3>

```typescript
taskDefinition: pulumi.Input<string>;
```


The ARN of the task definition which contains the container

<h2 class="pdoc-module-header" id="GetContainerDefinitionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L34">interface GetContainerDefinitionResult</a>
</h2>

A collection of values returned by getContainerDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L38">property cpu</a>
</h3>

```typescript
cpu: number;
```


The CPU limit for this container definition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L42">property disableNetworking</a>
</h3>

```typescript
disableNetworking: boolean;
```


Indicator if networking is disabled

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L46">property dockerLabels</a>
</h3>

```typescript
dockerLabels: { ... };
```


Set docker labels

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L50">property environment</a>
</h3>

```typescript
environment: { ... };
```


The environment in use

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L54">property image</a>
</h3>

```typescript
image: string;
```


The docker image in use, including the digest

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L58">property imageDigest</a>
</h3>

```typescript
imageDigest: string;
```


The digest of the docker image in use

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L62">property memory</a>
</h3>

```typescript
memory: number;
```


The memory limit for this container definition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getContainerDefinition.ts#L66">property memoryReservation</a>
</h3>

```typescript
memoryReservation: number;
```


The soft limit (in MiB) of memory to reserve for the container. When system memory is under contention, Docker attempts to keep the container memory to this soft limit

<h2 class="pdoc-module-header" id="GetServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts#L20">interface GetServiceArgs</a>
</h2>

A collection of arguments for invoking getService.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts#L24">property clusterArn</a>
</h3>

```typescript
clusterArn: pulumi.Input<string>;
```


The arn of the ECS Cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts#L28">property serviceName</a>
</h3>

```typescript
serviceName: pulumi.Input<string>;
```


The name of the ECS Service

<h2 class="pdoc-module-header" id="GetServiceResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts#L34">interface GetServiceResult</a>
</h2>

A collection of values returned by getService.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts#L38">property arn</a>
</h3>

```typescript
arn: string;
```


The ARN of the ECS Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts#L42">property desiredCount</a>
</h3>

```typescript
desiredCount: number;
```


The number of tasks for the ECS Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts#L46">property launchType</a>
</h3>

```typescript
launchType: string;
```


The launch type for the ECS Service

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getService.ts#L50">property taskDefinition</a>
</h3>

```typescript
taskDefinition: string;
```


The family for the latest ACTIVE revision

<h2 class="pdoc-module-header" id="GetTaskDefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts#L20">interface GetTaskDefinitionArgs</a>
</h2>

A collection of arguments for invoking getTaskDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts#L24">property taskDefinition</a>
</h3>

```typescript
taskDefinition: pulumi.Input<string>;
```


The family for the latest ACTIVE revision, family and revision (family:revision) for a specific revision in the family, the ARN of the task definition to access to.

<h2 class="pdoc-module-header" id="GetTaskDefinitionResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts#L30">interface GetTaskDefinitionResult</a>
</h2>

A collection of values returned by getTaskDefinition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts#L34">property family</a>
</h3>

```typescript
family: string;
```


The family of this task definition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts#L38">property networkMode</a>
</h3>

```typescript
networkMode: string;
```


The Docker networking mode to use for the containers in this task.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts#L42">property revision</a>
</h3>

```typescript
revision: number;
```


The revision of this task definition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts#L46">property status</a>
</h3>

```typescript
status: string;
```


The status of this task definition

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/getTaskDefinition.ts#L50">property taskRoleArn</a>
</h3>

```typescript
taskRoleArn: string;
```


The ARN of the IAM role that containers in this task can assume

<h2 class="pdoc-module-header" id="HostEntry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L56">interface HostEntry</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L57">property hostname</a>
</h3>

```typescript
hostname: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L58">property ipAddress</a>
</h3>

```typescript
ipAddress: string;
```

<h2 class="pdoc-module-header" id="KernelCapabilities">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L69">interface KernelCapabilities</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L70">property add</a>
</h3>

```typescript
add?: KernelCapability[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L71">property drop</a>
</h3>

```typescript
drop?: KernelCapability[];
```

<h2 class="pdoc-module-header" id="KeyValuePair">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L50">interface KeyValuePair</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L51">property name</a>
</h3>

```typescript
name: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L52">property value</a>
</h3>

```typescript
value: string;
```

<h2 class="pdoc-module-header" id="LinuxParameters">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L62">interface LinuxParameters</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L63">property capabilities</a>
</h3>

```typescript
capabilities?: KernelCapabilities;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L64">property devices</a>
</h3>

```typescript
devices?: Device[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L65">property initProcessEnabled</a>
</h3>

```typescript
initProcessEnabled?: boolean;
```

<h2 class="pdoc-module-header" id="LogConfiguration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L90">interface LogConfiguration</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L91">property logDriver</a>
</h3>

```typescript
logDriver: LogDriver;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L92">property options</a>
</h3>

```typescript
options?: { ... };
```

<h2 class="pdoc-module-header" id="MountPoint">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L99">interface MountPoint</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L100">property containerPath</a>
</h3>

```typescript
containerPath?: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L101">property readOnly</a>
</h3>

```typescript
readOnly?: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L102">property sourceVolume</a>
</h3>

```typescript
sourceVolume?: string;
```

<h2 class="pdoc-module-header" id="PortMapping">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L106">interface PortMapping</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L107">property containerPort</a>
</h3>

```typescript
containerPort?: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L108">property hostPort</a>
</h3>

```typescript
hostPort?: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L109">property protocol</a>
</h3>

```typescript
protocol?: Protocol;
```

<h2 class="pdoc-module-header" id="ServiceArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L220">interface ServiceArgs</a>
</h2>

The set of arguments for constructing a Service resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L224">property cluster</a>
</h3>

```typescript
cluster?: pulumi.Input<string>;
```


ARN of an ECS cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L228">property deploymentMaximumPercent</a>
</h3>

```typescript
deploymentMaximumPercent?: pulumi.Input<number>;
```


The upper limit (as a percentage of the service's desiredCount) of the number of running tasks that can be running in a service during a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L232">property deploymentMinimumHealthyPercent</a>
</h3>

```typescript
deploymentMinimumHealthyPercent?: pulumi.Input<number>;
```


The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L236">property desiredCount</a>
</h3>

```typescript
desiredCount?: pulumi.Input<number>;
```


The number of instances of the task definition to place and keep running

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L240">property healthCheckGracePeriodSeconds</a>
</h3>

```typescript
healthCheckGracePeriodSeconds?: pulumi.Input<number>;
```


Seconds to ignore failing load balancer health checks on newly instantiated tasks to prevent premature shutdown, up to 7200. Only valid for services configured to use load balancers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L244">property iamRole</a>
</h3>

```typescript
iamRole?: pulumi.Input<string>;
```


ARN of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is required if you are using a load balancer with your service, but only if your task definition does not use the `awsvpc` network mode. If using `awsvpc` network mode, do not specify this role. If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L248">property launchType</a>
</h3>

```typescript
launchType?: pulumi.Input<string>;
```


The launch type on which to run your service. The valid values are `EC2` and `FARGATE`. Defaults to `EC2`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L252">property loadBalancers</a>
</h3>

```typescript
loadBalancers?: pulumi.Input<{ ... }[]>;
```


A load balancer block. Load balancers documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L256">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the service (up to 255 letters, numbers, hyphens, and underscores)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L260">property networkConfiguration</a>
</h3>

```typescript
networkConfiguration?: pulumi.Input<{ ... }>;
```


The network configuration for the service. This parameter is required for task definitions that use the `awsvpc` network mode to receive their own Elastic Network Interface, and it is not supported for other network modes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L264">property orderedPlacementStrategies</a>
</h3>

```typescript
orderedPlacementStrategies?: pulumi.Input<{ ... }[]>;
```


Service level strategy rules that are taken into consideration during task placement. List from top to bottom in order of precedence. The maximum number of `ordered_placement_strategy` blocks is `5`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L269">property placementConstraints</a>
</h3>

```typescript
placementConstraints?: pulumi.Input<{ ... }[]>;
```


rules that are taken into consideration during task placement. Maximum number of
`placement_constraints` is `10`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L273">property placementStrategies</a>
</h3>

```typescript
placementStrategies?: pulumi.Input<{ ... }[]>;
```


**Deprecated**, use `ordered_placement_strategy` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L277">property serviceRegistries</a>
</h3>

```typescript
serviceRegistries?: pulumi.Input<{ ... }>;
```


The service discovery registries for the service. The maximum number of `service_registries` blocks is `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L281">property taskDefinition</a>
</h3>

```typescript
taskDefinition: pulumi.Input<string>;
```


The family and revision (`family:revision`) or full ARN of the task definition that you want to run in your service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L285">property waitForSteadyState</a>
</h3>

```typescript
waitForSteadyState?: pulumi.Input<boolean>;
```


If `true`, Terraform will wait for the service to reach a steady state (like [`aws ecs wait services-stable`](https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html)) before continuing. Default `false`.

<h2 class="pdoc-module-header" id="ServiceState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L149">interface ServiceState</a>
</h2>

Input properties used for looking up and filtering Service resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L153">property cluster</a>
</h3>

```typescript
cluster?: pulumi.Input<string>;
```


ARN of an ECS cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L157">property deploymentMaximumPercent</a>
</h3>

```typescript
deploymentMaximumPercent?: pulumi.Input<number>;
```


The upper limit (as a percentage of the service's desiredCount) of the number of running tasks that can be running in a service during a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L161">property deploymentMinimumHealthyPercent</a>
</h3>

```typescript
deploymentMinimumHealthyPercent?: pulumi.Input<number>;
```


The lower limit (as a percentage of the service's desiredCount) of the number of running tasks that must remain running and healthy in a service during a deployment.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L165">property desiredCount</a>
</h3>

```typescript
desiredCount?: pulumi.Input<number>;
```


The number of instances of the task definition to place and keep running

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L169">property healthCheckGracePeriodSeconds</a>
</h3>

```typescript
healthCheckGracePeriodSeconds?: pulumi.Input<number>;
```


Seconds to ignore failing load balancer health checks on newly instantiated tasks to prevent premature shutdown, up to 7200. Only valid for services configured to use load balancers.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L173">property iamRole</a>
</h3>

```typescript
iamRole?: pulumi.Input<string>;
```


ARN of the IAM role that allows Amazon ECS to make calls to your load balancer on your behalf. This parameter is required if you are using a load balancer with your service, but only if your task definition does not use the `awsvpc` network mode. If using `awsvpc` network mode, do not specify this role. If your account has already created the Amazon ECS service-linked role, that role is used by default for your service unless you specify a role here.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L177">property launchType</a>
</h3>

```typescript
launchType?: pulumi.Input<string>;
```


The launch type on which to run your service. The valid values are `EC2` and `FARGATE`. Defaults to `EC2`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L181">property loadBalancers</a>
</h3>

```typescript
loadBalancers?: pulumi.Input<{ ... }[]>;
```


A load balancer block. Load balancers documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L185">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the service (up to 255 letters, numbers, hyphens, and underscores)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L189">property networkConfiguration</a>
</h3>

```typescript
networkConfiguration?: pulumi.Input<{ ... }>;
```


The network configuration for the service. This parameter is required for task definitions that use the `awsvpc` network mode to receive their own Elastic Network Interface, and it is not supported for other network modes.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L193">property orderedPlacementStrategies</a>
</h3>

```typescript
orderedPlacementStrategies?: pulumi.Input<{ ... }[]>;
```


Service level strategy rules that are taken into consideration during task placement. List from top to bottom in order of precedence. The maximum number of `ordered_placement_strategy` blocks is `5`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L198">property placementConstraints</a>
</h3>

```typescript
placementConstraints?: pulumi.Input<{ ... }[]>;
```


rules that are taken into consideration during task placement. Maximum number of
`placement_constraints` is `10`. Defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L202">property placementStrategies</a>
</h3>

```typescript
placementStrategies?: pulumi.Input<{ ... }[]>;
```


**Deprecated**, use `ordered_placement_strategy` instead.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L206">property serviceRegistries</a>
</h3>

```typescript
serviceRegistries?: pulumi.Input<{ ... }>;
```


The service discovery registries for the service. The maximum number of `service_registries` blocks is `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L210">property taskDefinition</a>
</h3>

```typescript
taskDefinition?: pulumi.Input<string>;
```


The family and revision (`family:revision`) or full ARN of the task definition that you want to run in your service.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/service.ts#L214">property waitForSteadyState</a>
</h3>

```typescript
waitForSteadyState?: pulumi.Input<boolean>;
```


If `true`, Terraform will wait for the service to reach a steady state (like [`aws ecs wait services-stable`](https://docs.aws.amazon.com/cli/latest/reference/ecs/wait/services-stable.html)) before continuing. Default `false`.

<h2 class="pdoc-module-header" id="TaskDefinitionArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L187">interface TaskDefinitionArgs</a>
</h2>

The set of arguments for constructing a TaskDefinition resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L196">property containerDefinitions</a>
</h3>

```typescript
containerDefinitions: pulumi.Input<string>;
```


A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L200">property cpu</a>
</h3>

```typescript
cpu?: pulumi.Input<string>;
```


The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L204">property executionRoleArn</a>
</h3>

```typescript
executionRoleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L208">property family</a>
</h3>

```typescript
family: pulumi.Input<string>;
```


A unique name for your task definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L212">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<string>;
```


The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L216">property networkMode</a>
</h3>

```typescript
networkMode?: pulumi.Input<string>;
```


The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L220">property placementConstraints</a>
</h3>

```typescript
placementConstraints?: pulumi.Input<{ ... }[]>;
```


A set of [placement constraints](#placement-constraints-arguments) rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L224">property requiresCompatibilities</a>
</h3>

```typescript
requiresCompatibilities?: pulumi.Input<pulumi.Input<string>[]>;
```


A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L228">property taskRoleArn</a>
</h3>

```typescript
taskRoleArn?: pulumi.Input<string>;
```


The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L232">property volumes</a>
</h3>

```typescript
volumes?: pulumi.Input<{ ... }[]>;
```


A set of [volume blocks](#volume-block-arguments) that containers in your task may use.

<h2 class="pdoc-module-header" id="TaskDefinitionState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L128">interface TaskDefinitionState</a>
</h2>

Input properties used for looking up and filtering TaskDefinition resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L132">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```


Full ARN of the Task Definition (including both `family` and `revision`).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L141">property containerDefinitions</a>
</h3>

```typescript
containerDefinitions?: pulumi.Input<string>;
```


A list of valid [container definitions]
(http://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html) provided as a
single valid JSON document. Please note that you should only provide values that are part of the container
definition document. For a detailed description of what parameters are available, see the [Task Definition Parameters]
(https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) section from the
official [Developer Guide](https://docs.aws.amazon.com/AmazonECS/latest/developerguide).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L145">property cpu</a>
</h3>

```typescript
cpu?: pulumi.Input<string>;
```


The number of cpu units used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L149">property executionRoleArn</a>
</h3>

```typescript
executionRoleArn?: pulumi.Input<string>;
```


The Amazon Resource Name (ARN) of the task execution role that the Amazon ECS container agent and the Docker daemon can assume.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L153">property family</a>
</h3>

```typescript
family?: pulumi.Input<string>;
```


A unique name for your task definition.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L157">property memory</a>
</h3>

```typescript
memory?: pulumi.Input<string>;
```


The amount (in MiB) of memory used by the task. If the `requires_compatibilities` is `FARGATE` this field is required.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L161">property networkMode</a>
</h3>

```typescript
networkMode?: pulumi.Input<string>;
```


The Docker networking mode to use for the containers in the task. The valid values are `none`, `bridge`, `awsvpc`, and `host`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L165">property placementConstraints</a>
</h3>

```typescript
placementConstraints?: pulumi.Input<{ ... }[]>;
```


A set of [placement constraints](#placement-constraints-arguments) rules that are taken into consideration during task placement. Maximum number of `placement_constraints` is `10`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L169">property requiresCompatibilities</a>
</h3>

```typescript
requiresCompatibilities?: pulumi.Input<pulumi.Input<string>[]>;
```


A set of launch types required by the task. The valid values are `EC2` and `FARGATE`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L173">property revision</a>
</h3>

```typescript
revision?: pulumi.Input<number>;
```


The revision of the task in a particular family.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L177">property taskRoleArn</a>
</h3>

```typescript
taskRoleArn?: pulumi.Input<string>;
```


The ARN of IAM role that allows your Amazon ECS container task to make calls to other AWS services.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/taskDefinition.ts#L181">property volumes</a>
</h3>

```typescript
volumes?: pulumi.Input<{ ... }[]>;
```


A set of [volume blocks](#volume-block-arguments) that containers in your task may use.

<h2 class="pdoc-module-header" id="Ulimit">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L116">interface Ulimit</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L118">property hardLimit</a>
</h3>

```typescript
hardLimit: number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L117">property name</a>
</h3>

```typescript
name: UlimitName;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L119">property softLimit</a>
</h3>

```typescript
softLimit: number;
```

<h2 class="pdoc-module-header" id="VolumeFrom">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L127">interface VolumeFrom</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L129">property readOnly</a>
</h3>

```typescript
readOnly?: boolean;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L128">property sourceContainer</a>
</h3>

```typescript
sourceContainer?: string;
```

<h2 class="pdoc-module-header" id="KernelCapability">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L75">type KernelCapability</a>
</h2>

```typescript
type KernelCapability = ALL | AUDIT_CONTROL | AUDIT_WRITE | BLOCK_SUSPEND | CHOWN | DAC_OVERRIDE | DAC_READ_SEARCH | FOWNER | FSETID | IPC_LOCK | IPC_OWNER | KILL | LEASE | LINUX_IMMUTABLE | MAC_ADMIN | MAC_OVERRIDE | MKNOD | NET_ADMIN | NET_BIND_SERVICE | NET_BROADCAST | NET_RAW | SETFCAP | SETGID | SETPCAP | SETUID | SYS_ADMIN | SYS_BOOT | SYS_CHROOT | SYS_MODULE | SYS_NICE | SYS_PACCT | SYS_PTRACE | SYS_RAWIO | SYS_RESOURCE | SYS_TIME | SYS_TTY_CONFIG | SYSLOG | WAKE_ALARM;
```

<h2 class="pdoc-module-header" id="LogDriver">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L96">type LogDriver</a>
</h2>

```typescript
type LogDriver = json-file | syslog | journald | gelf | fluentd | awslogs | splunk;
```

<h2 class="pdoc-module-header" id="Protocol">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L113">type Protocol</a>
</h2>

```typescript
type Protocol = tcp | udp;
```

<h2 class="pdoc-module-header" id="UlimitName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/ecs/container.ts#L123">type UlimitName</a>
</h2>

```typescript
type UlimitName = core | cpu | data | fsize | locks | memlock | msgqueue | nice | nofile | nproc | rss | rtprio | rttime | sigpending | stack;
```

