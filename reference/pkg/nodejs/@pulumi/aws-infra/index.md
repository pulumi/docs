---
title: Package @pulumi/aws-infra
---


Node.js:

```javascript
var awsInfra = require("@pulumi/aws-infra");
```

ES6 modules:

```typescript
import * as awsInfra from "@pulumi/aws-infra";
```

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Cluster">class Cluster</a>
* <a href="#Network">class Network</a>
* <a href="#defaultEfsMountPath">const defaultEfsMountPath</a>
* <a href="#createAutoScalingGroup">function createAutoScalingGroup</a>
* <a href="#getAwsAz">function getAwsAz</a>
* <a href="#getCloudFormationAsgTemplate">function getCloudFormationAsgTemplate</a>
* <a href="#getEcsAmiId">function getEcsAmiId</a>
* <a href="#getInstanceUserData">function getInstanceUserData</a>
* <a href="#sha1hash">function sha1hash</a>
* <a href="#ClusterArgs">interface ClusterArgs</a>
* <a href="#ClusterNetworkArgs">interface ClusterNetworkArgs</a>
* <a href="#NetworkArgs">interface NetworkArgs</a>
* <a href="#NetworkVpcArgs">interface NetworkVpcArgs</a>
* <a href="#azs">let azs</a>

<a href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/aws.ts">aws.ts</a> <a href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts">cluster.ts</a> <a href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts">network.ts</a> <a href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/utils.ts">utils.ts</a> 


<h2 class="pdoc-module-header" id="Cluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L107">class Cluster</a>
</h2>

A Cluster is a general purpose ECS cluster configured to run in a provided
Network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L124">constructor</a>
</h3>

```typescript
new Cluster(name: string, args: ClusterArgs, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L120">property autoScalingGroupStack</a>
</h3>

```typescript
public autoScalingGroupStack?: pulumi.Resource;
```


The auto-scaling group that ECS Service's should add to their
`dependsOn`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L111">property ecsClusterARN</a>
</h3>

```typescript
public ecsClusterARN: pulumi.Output<string>;
```


The ECS Cluster ARN.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L124">property efsMountPath</a>
</h3>

```typescript
public efsMountPath?: undefined | string;
```


The EFS host mount path if EFS is enabled on this Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L115">property securityGroupId</a>
</h3>

```typescript
public securityGroupId?: pulumi.Output<string>;
```


The ECS Cluster's Security Group ID.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Network">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L61">class Network</a>
</h2>

Network encapsulates the configuration of an Amazon VPC.  Both [VPC with Public
Subnet](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario1.html) and [VPC with Public and Private
Subnets (NAT)](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Scenario2.html) configurations are
supported.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L131">constructor</a>
</h3>

```typescript
new Network(name: string, args?: NetworkArgs, opts?: pulumi.ResourceOptions)
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L116">method fromVpc</a>
</h3>

```typescript
public static fromVpc(name: string, vpcArgs: NetworkVpcArgs, opts?: pulumi.ResourceOptions): Network
```


Creates a new network using the configuration values of an existing VPC.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L92">method getDefault</a>
</h3>

```typescript
public static getDefault(opts?: pulumi.ResourceOptions): Network
```


Gets the default VPC for the AWS account as a Network.  This first time this is called,
the default network will be lazily created, using whatever options are provided in opts.
All subsequent calls will return that same network even if different opts are provided.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L16">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L108">method registerOutputs</a>
</h3>

```typescript
protected registerOutputs(outputs: Inputs | undefined): void
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L85">property defaultNetwork</a>
</h3>

```typescript
private static defaultNetwork: Network;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L82">property publicSubnetIds</a>
</h3>

```typescript
public publicSubnetIds: pulumi.Output<string>[];
```


The public subnets for the VPC.  In case [usePrivateSubnets] == false, these are the same as [subnets].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L73">property securityGroupIds</a>
</h3>

```typescript
public securityGroupIds: pulumi.Output<string>[];
```


The security group IDs for the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L78">property subnetIds</a>
</h3>

```typescript
public subnetIds: pulumi.Output<string>[];
```


The subnets in which compute should run.  These are the private subnets if [usePrivateSubnets] == true, else
these are the public subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L69">property usePrivateSubnets</a>
</h3>

```typescript
public usePrivateSubnets: boolean;
```


Whether the network includes private subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L65">property vpcId</a>
</h3>

```typescript
public vpcId: pulumi.Output<string>;
```


The VPC id of the network.

<h2 class="pdoc-module-header" id="defaultEfsMountPath">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L23">const defaultEfsMountPath</a>
</h2>

```typescript
const defaultEfsMountPath: /mnt/efs = "/mnt/efs";
```

<h2 class="pdoc-module-header" id="createAutoScalingGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L226">function createAutoScalingGroup</a>
</h2>

```typescript
createAutoScalingGroup(parent: Cluster, name: string, args: ClusterArgs, securityGroup: aws.ec2.SecurityGroup, cluster: aws.ecs.Cluster, filesystem: aws.efs.FileSystem | undefined): aws.cloudformation.Stack
```

<h2 class="pdoc-module-header" id="getAwsAz">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/aws.ts#L23">function getAwsAz</a>
</h2>

```typescript
getAwsAz(index: number): Promise<string>
```

<h2 class="pdoc-module-header" id="getCloudFormationAsgTemplate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L433">function getCloudFormationAsgTemplate</a>
</h2>

```typescript
getCloudFormationAsgTemplate(instanceName: string, minSize: number, maxSize: number, instanceLaunchConfigurationId: pulumi.Output<string>, subnetIds: pulumi.Input<string>[]): pulumi.Output<string>
```

<h2 class="pdoc-module-header" id="getEcsAmiId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L330">function getEcsAmiId</a>
</h2>

```typescript
getEcsAmiId(name?: undefined | string): Promise<any>
```

<h2 class="pdoc-module-header" id="getInstanceUserData">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L360">function getInstanceUserData</a>
</h2>

```typescript
getInstanceUserData(cluster: aws.ecs.Cluster, fileSystem: aws.efs.FileSystem | undefined, mountPath: string | undefined, cloudFormationStackName: pulumi.Output<string>): Output<string>
```

<h2 class="pdoc-module-header" id="sha1hash">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/utils.ts#L18">function sha1hash</a>
</h2>

```typescript
sha1hash(s: string): string
```

<h2 class="pdoc-module-header" id="ClusterArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L39">interface ClusterArgs</a>
</h2>

Arguments bag for creating infrastrcture for a new Cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L47">property addEFS</a>
</h3>

```typescript
addEFS: boolean;
```


Whether to create an EFS File System to manage volumes across the cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L100">property ecsOptimizedAMIName</a>
</h3>

```typescript
ecsOptimizedAMIName?: undefined | string;
```


The name of the ECS-optimzed AMI to use for the Container Instances in this cluster, e.g.
"amzn-ami-2017.09.l-amazon-ecs-optimized". Defaults to using the latest recommended ECS Optimized AMI, which may
change over time and cause recreation of EC2 instances when new versions are release. To control when these
changes are adopted, set this parameter explicitly to the version you would like to use.

See http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html for valid values.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L70">property instanceDockerImageVolumeSize</a>
</h3>

```typescript
instanceDockerImageVolumeSize?: undefined | number;
```


The size (in GiB) of the EBS volume to attach to each instance to use for Docker image and metadata storage.

The default is 50 GiB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L58">property instanceRolePolicyARNs</a>
</h3>

```typescript
instanceRolePolicyARNs?: string[];
```


The policy to apply to the cluster instance role.

The default is `["arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role",
"arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess"]`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L64">property instanceRootVolumeSize</a>
</h3>

```typescript
instanceRootVolumeSize?: undefined | number;
```


The size (in GiB) of the EBS volume to attach to each instance as the root volume.

The default is 8 GiB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L76">property instanceSwapVolumeSize</a>
</h3>

```typescript
instanceSwapVolumeSize?: undefined | number;
```


The size (in GiB) of the EBS volume to attach to each instance for swap space.

The default is 5 GiB.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L51">property instanceType</a>
</h3>

```typescript
instanceType?: undefined | string;
```


The EC2 instance type to use for the Cluster.  Defaults to `t2.micro`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L85">property maxSize</a>
</h3>

```typescript
maxSize?: undefined | number;
```


The maximum size of the cluster. Setting to 0 will prevent an EC2 AutoScalingGroup from being created. Defaults
to 100.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L80">property minSize</a>
</h3>

```typescript
minSize?: undefined | number;
```


The minimum size of the cluster. Defaults to 2.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L43">property network</a>
</h3>

```typescript
network: ClusterNetworkArgs;
```


The network in which to create this cluster.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L91">property publicKey</a>
</h3>

```typescript
publicKey?: undefined | string;
```


Public key material for SSH access. See allowed formats at:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
If not provided, no SSH access is enabled on VMs.

<h2 class="pdoc-module-header" id="ClusterNetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L25">interface ClusterNetworkArgs</a>
</h2>
<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L33">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<string>[];
```


The network subnets for the clusters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/cluster.ts#L29">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The VPC id of the network for the cluster

<h2 class="pdoc-module-header" id="NetworkArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L24">interface NetworkArgs</a>
</h2>

Optional arguments that can be provided when creating a network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L25">property numberOfAvailabilityZones</a>
</h3>

```typescript
numberOfAvailabilityZones?: undefined | number;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L26">property usePrivateSubnets</a>
</h3>

```typescript
usePrivateSubnets?: undefined | true | false;
```

<h2 class="pdoc-module-header" id="NetworkVpcArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L32">interface NetworkVpcArgs</a>
</h2>

Arguments necessary when creating a network using Network.fromVpc.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L52">property publicSubnetIds</a>
</h3>

```typescript
publicSubnetIds: pulumi.Input<string>[];
```


The public subnets for the VPC.  In case [usePrivateSubnets] == false, these are the same as [subnets].

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L48">property securityGroupIds</a>
</h3>

```typescript
securityGroupIds: pulumi.Input<string>[];
```


The security group IDs for the network.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L40">property subnetIds</a>
</h3>

```typescript
subnetIds: pulumi.Input<string>[];
```


The network subnets for the clusters

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L44">property usePrivateSubnets</a>
</h3>

```typescript
usePrivateSubnets: boolean;
```


Whether the network includes private subnets.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/network.ts#L36">property vpcId</a>
</h3>

```typescript
vpcId: pulumi.Input<string>;
```


The VPC id of the network for the cluster

<h2 class="pdoc-module-header" id="azs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws-infra/blob/master/nodejs/aws.ts#L20">let azs</a>
</h2>

```typescript
let azs: Promise<aws.GetAvailabilityZonesResult> | undefined;
```

