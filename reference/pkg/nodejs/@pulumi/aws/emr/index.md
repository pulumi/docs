---
title: Module emr
---

<a href="../index.html">@pulumi/aws</a> &gt; emr

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#InstanceGroup">class InstanceGroup</a>
* <a href="#SecurityConfiguration">class SecurityConfiguration</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterState">interface ClusterState</a>
* <a href="#InstanceGroupArgs">interface InstanceGroupArgs</a>
* <a href="#InstanceGroupState">interface InstanceGroupState</a>
* <a href="#SecurityConfigurationArgs">interface SecurityConfigurationArgs</a>
* <a href="#SecurityConfigurationState">interface SecurityConfigurationState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts">emr/cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts">emr/instanceGroup.ts</a> <a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts">emr/securityConfiguration.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L11">class Cluster</a>
</h2>

Provides an Elastic MapReduce Cluster, a web service that makes it easy to
process large amounts of data efficiently. See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/elastic-mapreduce/)
for more information.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L127">constructor</a>
</h3>

```typescript
new Cluster(name: string, args: ClusterArgs, opts?: pulumi.ResourceOptions)
```


Create a Cluster resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L20">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L27">property additionalInfo</a>
</h3>

```typescript
public additionalInfo: pulumi.Output<string | undefined>;
```


A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L31">property applications</a>
</h3>

```typescript
public applications: pulumi.Output<string[] | undefined>;
```


A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, and `Spark`. Case insensitive

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L35">property autoscalingRole</a>
</h3>

```typescript
public autoscalingRole: pulumi.Output<string | undefined>;
```


An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L40">property bootstrapActions</a>
</h3>

```typescript
public bootstrapActions: pulumi.Output<{ ... }[] | undefined>;
```


List of bootstrap actions that will be run before Hadoop is started on
the cluster nodes. Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L41">property clusterState</a>
</h3>

```typescript
public clusterState: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L45">property configurations</a>
</h3>

```typescript
public configurations: pulumi.Output<string | undefined>;
```


List of configurations supplied for the EMR cluster you are creating

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L49">property coreInstanceCount</a>
</h3>

```typescript
public coreInstanceCount: pulumi.Output<number | undefined>;
```


Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`core_instance_count`-1) as core nodes. Cannot be specified if `instance_groups` is set. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L53">property coreInstanceType</a>
</h3>

```typescript
public coreInstanceType: pulumi.Output<string>;
```


The EC2 instance type of the slave nodes. Cannot be specified if `instance_groups` is set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L57">property customAmiId</a>
</h3>

```typescript
public customAmiId: pulumi.Output<string | undefined>;
```


A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L61">property ebsRootVolumeSize</a>
</h3>

```typescript
public ebsRootVolumeSize: pulumi.Output<number | undefined>;
```


Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L66">property ec2Attributes</a>
</h3>

```typescript
public ec2Attributes: pulumi.Output<{ ... } | undefined>;
```


Attributes for the EC2 instances running the job
flow. Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L70">property instanceGroups</a>
</h3>

```typescript
public instanceGroups: pulumi.Output<{ ... }[] | undefined>;
```


A list of `instance_group` objects for each instance group in the cluster. Exactly one of `master_instance_type` and `instance_group` must be specified. If `instance_group` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L74">property keepJobFlowAliveWhenNoSteps</a>
</h3>

```typescript
public keepJobFlowAliveWhenNoSteps: pulumi.Output<boolean>;
```


Switch on/off run cluster with no steps or when all steps are complete (default is on)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L78">property kerberosAttributes</a>
</h3>

```typescript
public kerberosAttributes: pulumi.Output<{ ... } | undefined>;
```


Kerberos configuration for the cluster. Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L83">property logUri</a>
</h3>

```typescript
public logUri: pulumi.Output<string | undefined>;
```


S3 bucket to write the log files of the job flow. If a value
is not provided, logs are not created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L87">property masterInstanceType</a>
</h3>

```typescript
public masterInstanceType: pulumi.Output<string | undefined>;
```


The EC2 instance type of the master node. Exactly one of `master_instance_type` and `instance_group` must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L91">property masterPublicDns</a>
</h3>

```typescript
public masterPublicDns: pulumi.Output<string>;
```


The public DNS name of the master EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L95">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the job flow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L99">property releaseLabel</a>
</h3>

```typescript
public releaseLabel: pulumi.Output<string>;
```


The release label for the Amazon EMR release

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L103">property scaleDownBehavior</a>
</h3>

```typescript
public scaleDownBehavior: pulumi.Output<string>;
```


The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L107">property securityConfiguration</a>
</h3>

```typescript
public securityConfiguration: pulumi.Output<string | undefined>;
```


The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `release_label` 4.8.0 or greater

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L111">property serviceRole</a>
</h3>

```typescript
public serviceRole: pulumi.Output<string>;
```


IAM role that will be assumed by the Amazon EMR service to access AWS resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L115">property steps</a>
</h3>

```typescript
public steps: pulumi.Output<{ ... }[]>;
```


List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](/docs/configuration/resources.html) with `ignore_changes` if other steps are being managed outside of Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L119">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


list of tags to apply to the EMR Cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L123">property terminationProtection</a>
</h3>

```typescript
public terminationProtection: pulumi.Output<boolean>;
```


Switch on/off termination protection (default is off)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L127">property visibleToAllUsers</a>
</h3>

```typescript
public visibleToAllUsers: pulumi.Output<boolean | undefined>;
```


Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`

<h2 class="pdoc-module-header" id="InstanceGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L14">class InstanceGroup</a>
</h2>

Provides an Elastic MapReduce Cluster Instance Group configuration.
See [Amazon Elastic MapReduce Documentation](https://aws.amazon.com/documentation/emr/) for more information.

~> **NOTE:** At this time, Instance Groups cannot be destroyed through the API nor
web interface. Instance Groups are destroyed when the EMR Cluster is destroyed.
Terraform will resize any Instance Group to zero when destroying the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L52">constructor</a>
</h3>

```typescript
new InstanceGroup(name: string, args: InstanceGroupArgs, opts?: pulumi.ResourceOptions)
```


Create a InstanceGroup resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L23">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceGroupState): InstanceGroup
```


Get an existing InstanceGroup resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L30">property clusterId</a>
</h3>

```typescript
public clusterId: pulumi.Output<string>;
```


ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L34">property ebsConfigs</a>
</h3>

```typescript
public ebsConfigs: pulumi.Output<{ ... }[] | undefined>;
```


One or more `ebs_config` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L38">property ebsOptimized</a>
</h3>

```typescript
public ebsOptimized: pulumi.Output<boolean | undefined>;
```


Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L42">property instanceCount</a>
</h3>

```typescript
public instanceCount: pulumi.Output<number | undefined>;
```


Target number of instances for the instance group. Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L46">property instanceType</a>
</h3>

```typescript
public instanceType: pulumi.Output<string>;
```


The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Human friendly name given to the instance group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L51">property runningInstanceCount</a>
</h3>

```typescript
public runningInstanceCount: pulumi.Output<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L52">property status</a>
</h3>

```typescript
public status: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="SecurityConfiguration">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L9">class SecurityConfiguration</a>
</h2>

Provides a resource to manage AWS EMR Security Configurations

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L38">constructor</a>
</h3>

```typescript
new SecurityConfiguration(name: string, args: SecurityConfigurationArgs, opts?: pulumi.ResourceOptions)
```


Create a SecurityConfiguration resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecurityConfigurationState): SecurityConfiguration
```


Get an existing SecurityConfiguration resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L25">property configuration</a>
</h3>

```typescript
public configuration: pulumi.Output<string>;
```


A JSON formatted Security Configuration

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L29">property creationDate</a>
</h3>

```typescript
public creationDate: pulumi.Output<string>;
```


Date the Security Configuration was created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the EMR Security Configuration. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L38">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string | undefined>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L319">interface ClusterArgs</a>
</h2>

The set of arguments for constructing a Cluster resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L323">property additionalInfo</a>
</h3>

```typescript
additionalInfo?: pulumi.Input<string>;
```


A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L327">property applications</a>
</h3>

```typescript
applications?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, and `Spark`. Case insensitive

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L331">property autoscalingRole</a>
</h3>

```typescript
autoscalingRole?: pulumi.Input<string>;
```


An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L336">property bootstrapActions</a>
</h3>

```typescript
bootstrapActions?: pulumi.Input<{ ... }[]>;
```


List of bootstrap actions that will be run before Hadoop is started on
the cluster nodes. Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L340">property configurations</a>
</h3>

```typescript
configurations?: pulumi.Input<string>;
```


List of configurations supplied for the EMR cluster you are creating

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L344">property coreInstanceCount</a>
</h3>

```typescript
coreInstanceCount?: pulumi.Input<number>;
```


Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`core_instance_count`-1) as core nodes. Cannot be specified if `instance_groups` is set. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L348">property coreInstanceType</a>
</h3>

```typescript
coreInstanceType?: pulumi.Input<string>;
```


The EC2 instance type of the slave nodes. Cannot be specified if `instance_groups` is set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L352">property customAmiId</a>
</h3>

```typescript
customAmiId?: pulumi.Input<string>;
```


A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L356">property ebsRootVolumeSize</a>
</h3>

```typescript
ebsRootVolumeSize?: pulumi.Input<number>;
```


Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L361">property ec2Attributes</a>
</h3>

```typescript
ec2Attributes?: pulumi.Input<{ ... }>;
```


Attributes for the EC2 instances running the job
flow. Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L365">property instanceGroups</a>
</h3>

```typescript
instanceGroups?: pulumi.Input<{ ... }[]>;
```


A list of `instance_group` objects for each instance group in the cluster. Exactly one of `master_instance_type` and `instance_group` must be specified. If `instance_group` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L369">property keepJobFlowAliveWhenNoSteps</a>
</h3>

```typescript
keepJobFlowAliveWhenNoSteps?: pulumi.Input<boolean>;
```


Switch on/off run cluster with no steps or when all steps are complete (default is on)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L373">property kerberosAttributes</a>
</h3>

```typescript
kerberosAttributes?: pulumi.Input<{ ... }>;
```


Kerberos configuration for the cluster. Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L378">property logUri</a>
</h3>

```typescript
logUri?: pulumi.Input<string>;
```


S3 bucket to write the log files of the job flow. If a value
is not provided, logs are not created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L382">property masterInstanceType</a>
</h3>

```typescript
masterInstanceType?: pulumi.Input<string>;
```


The EC2 instance type of the master node. Exactly one of `master_instance_type` and `instance_group` must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L386">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the job flow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L390">property releaseLabel</a>
</h3>

```typescript
releaseLabel: pulumi.Input<string>;
```


The release label for the Amazon EMR release

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L394">property scaleDownBehavior</a>
</h3>

```typescript
scaleDownBehavior?: pulumi.Input<string>;
```


The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L398">property securityConfiguration</a>
</h3>

```typescript
securityConfiguration?: pulumi.Input<string>;
```


The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `release_label` 4.8.0 or greater

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L402">property serviceRole</a>
</h3>

```typescript
serviceRole: pulumi.Input<string>;
```


IAM role that will be assumed by the Amazon EMR service to access AWS resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L406">property steps</a>
</h3>

```typescript
steps?: pulumi.Input<{ ... }[]>;
```


List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](/docs/configuration/resources.html) with `ignore_changes` if other steps are being managed outside of Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L410">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


list of tags to apply to the EMR Cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L414">property terminationProtection</a>
</h3>

```typescript
terminationProtection?: pulumi.Input<boolean>;
```


Switch on/off termination protection (default is off)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L418">property visibleToAllUsers</a>
</h3>

```typescript
visibleToAllUsers?: pulumi.Input<boolean>;
```


Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`

<h2 class="pdoc-module-header" id="ClusterState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L209">interface ClusterState</a>
</h2>

Input properties used for looking up and filtering Cluster resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L213">property additionalInfo</a>
</h3>

```typescript
additionalInfo?: pulumi.Input<string>;
```


A JSON string for selecting additional features such as adding proxy information. Note: Currently there is no API to retrieve the value of this argument after EMR cluster creation from provider, therefore Terraform cannot detect drift from the actual EMR cluster if its value is changed outside Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L217">property applications</a>
</h3>

```typescript
applications?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of applications for the cluster. Valid values are: `Flink`, `Hadoop`, `Hive`, `Mahout`, `Pig`, and `Spark`. Case insensitive

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L221">property autoscalingRole</a>
</h3>

```typescript
autoscalingRole?: pulumi.Input<string>;
```


An IAM role for automatic scaling policies. The IAM role provides permissions that the automatic scaling feature requires to launch and terminate EC2 instances in an instance group.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L226">property bootstrapActions</a>
</h3>

```typescript
bootstrapActions?: pulumi.Input<{ ... }[]>;
```


List of bootstrap actions that will be run before Hadoop is started on
the cluster nodes. Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L227">property clusterState</a>
</h3>

```typescript
clusterState?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L231">property configurations</a>
</h3>

```typescript
configurations?: pulumi.Input<string>;
```


List of configurations supplied for the EMR cluster you are creating

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L235">property coreInstanceCount</a>
</h3>

```typescript
coreInstanceCount?: pulumi.Input<number>;
```


Number of Amazon EC2 instances used to execute the job flow. EMR will use one node as the cluster's master node and use the remainder of the nodes (`core_instance_count`-1) as core nodes. Cannot be specified if `instance_groups` is set. Default `1`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L239">property coreInstanceType</a>
</h3>

```typescript
coreInstanceType?: pulumi.Input<string>;
```


The EC2 instance type of the slave nodes. Cannot be specified if `instance_groups` is set

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L243">property customAmiId</a>
</h3>

```typescript
customAmiId?: pulumi.Input<string>;
```


A custom Amazon Linux AMI for the cluster (instead of an EMR-owned AMI). Available in Amazon EMR version 5.7.0 and later.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L247">property ebsRootVolumeSize</a>
</h3>

```typescript
ebsRootVolumeSize?: pulumi.Input<number>;
```


Size in GiB of the EBS root device volume of the Linux AMI that is used for each EC2 instance. Available in Amazon EMR version 4.x and later.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L252">property ec2Attributes</a>
</h3>

```typescript
ec2Attributes?: pulumi.Input<{ ... }>;
```


Attributes for the EC2 instances running the job
flow. Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L256">property instanceGroups</a>
</h3>

```typescript
instanceGroups?: pulumi.Input<{ ... }[]>;
```


A list of `instance_group` objects for each instance group in the cluster. Exactly one of `master_instance_type` and `instance_group` must be specified. If `instance_group` is set, then it must contain a configuration block for at least the `MASTER` instance group type (as well as any additional instance groups). Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L260">property keepJobFlowAliveWhenNoSteps</a>
</h3>

```typescript
keepJobFlowAliveWhenNoSteps?: pulumi.Input<boolean>;
```


Switch on/off run cluster with no steps or when all steps are complete (default is on)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L264">property kerberosAttributes</a>
</h3>

```typescript
kerberosAttributes?: pulumi.Input<{ ... }>;
```


Kerberos configuration for the cluster. Defined below

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L269">property logUri</a>
</h3>

```typescript
logUri?: pulumi.Input<string>;
```


S3 bucket to write the log files of the job flow. If a value
is not provided, logs are not created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L273">property masterInstanceType</a>
</h3>

```typescript
masterInstanceType?: pulumi.Input<string>;
```


The EC2 instance type of the master node. Exactly one of `master_instance_type` and `instance_group` must be specified.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L277">property masterPublicDns</a>
</h3>

```typescript
masterPublicDns?: pulumi.Input<string>;
```


The public DNS name of the master EC2 instance.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L281">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the job flow

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L285">property releaseLabel</a>
</h3>

```typescript
releaseLabel?: pulumi.Input<string>;
```


The release label for the Amazon EMR release

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L289">property scaleDownBehavior</a>
</h3>

```typescript
scaleDownBehavior?: pulumi.Input<string>;
```


The way that individual Amazon EC2 instances terminate when an automatic scale-in activity occurs or an `instance group` is resized.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L293">property securityConfiguration</a>
</h3>

```typescript
securityConfiguration?: pulumi.Input<string>;
```


The security configuration name to attach to the EMR cluster. Only valid for EMR clusters with `release_label` 4.8.0 or greater

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L297">property serviceRole</a>
</h3>

```typescript
serviceRole?: pulumi.Input<string>;
```


IAM role that will be assumed by the Amazon EMR service to access AWS resources

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L301">property steps</a>
</h3>

```typescript
steps?: pulumi.Input<{ ... }[]>;
```


List of steps to run when creating the cluster. Defined below. It is highly recommended to utilize the [lifecycle configuration block](/docs/configuration/resources.html) with `ignore_changes` if other steps are being managed outside of Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L305">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


list of tags to apply to the EMR Cluster

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L309">property terminationProtection</a>
</h3>

```typescript
terminationProtection?: pulumi.Input<boolean>;
```


Switch on/off termination protection (default is off)

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/cluster.ts#L313">property visibleToAllUsers</a>
</h3>

```typescript
visibleToAllUsers?: pulumi.Input<boolean>;
```


Whether the job flow is visible to all IAM users of the AWS account associated with the job flow. Default `true`

<h2 class="pdoc-module-header" id="InstanceGroupArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L130">interface InstanceGroupArgs</a>
</h2>

The set of arguments for constructing a InstanceGroup resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L134">property clusterId</a>
</h3>

```typescript
clusterId: pulumi.Input<string>;
```


ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L138">property ebsConfigs</a>
</h3>

```typescript
ebsConfigs?: pulumi.Input<{ ... }[]>;
```


One or more `ebs_config` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L142">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L146">property instanceCount</a>
</h3>

```typescript
instanceCount?: pulumi.Input<number>;
```


Target number of instances for the instance group. Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L150">property instanceType</a>
</h3>

```typescript
instanceType: pulumi.Input<string>;
```


The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L154">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human friendly name given to the instance group. Changing this forces a new resource to be created.

<h2 class="pdoc-module-header" id="InstanceGroupState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L98">interface InstanceGroupState</a>
</h2>

Input properties used for looking up and filtering InstanceGroup resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L102">property clusterId</a>
</h3>

```typescript
clusterId?: pulumi.Input<string>;
```


ID of the EMR Cluster to attach to. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L106">property ebsConfigs</a>
</h3>

```typescript
ebsConfigs?: pulumi.Input<{ ... }[]>;
```


One or more `ebs_config` blocks as defined below. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L110">property ebsOptimized</a>
</h3>

```typescript
ebsOptimized?: pulumi.Input<boolean>;
```


Indicates whether an Amazon EBS volume is EBS-optimized. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L114">property instanceCount</a>
</h3>

```typescript
instanceCount?: pulumi.Input<number>;
```


Target number of instances for the instance group. Defaults to 0.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L118">property instanceType</a>
</h3>

```typescript
instanceType?: pulumi.Input<string>;
```


The EC2 instance type for all instances in the instance group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L122">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Human friendly name given to the instance group. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L123">property runningInstanceCount</a>
</h3>

```typescript
runningInstanceCount?: pulumi.Input<number>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/instanceGroup.ts#L124">property status</a>
</h3>

```typescript
status?: pulumi.Input<string>;
```

<h2 class="pdoc-module-header" id="SecurityConfigurationArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L96">interface SecurityConfigurationArgs</a>
</h2>

The set of arguments for constructing a SecurityConfiguration resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L100">property configuration</a>
</h3>

```typescript
configuration: pulumi.Input<string>;
```


A JSON formatted Security Configuration

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L104">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the EMR Security Configuration. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L109">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

<h2 class="pdoc-module-header" id="SecurityConfigurationState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L73">interface SecurityConfigurationState</a>
</h2>

Input properties used for looking up and filtering SecurityConfiguration resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L77">property configuration</a>
</h3>

```typescript
configuration?: pulumi.Input<string>;
```


A JSON formatted Security Configuration

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L81">property creationDate</a>
</h3>

```typescript
creationDate?: pulumi.Input<string>;
```


Date the Security Configuration was created

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the EMR Security Configuration. By default generated by Terraform.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/emr/securityConfiguration.ts#L90">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


Creates a unique name beginning with the specified
prefix. Conflicts with `name`.

