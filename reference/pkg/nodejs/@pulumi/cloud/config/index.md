---
title: Module config
---

<a href="../index.html">@pulumi/cloud-aws</a> &gt; config

<h2 class="pdoc-module-header">Index</h2>

* <a href="#config">const config</a>
* <a href="#externalPublicSubnetsString">const externalPublicSubnetsString</a>
* <a href="#externalSecurityGroupsString">const externalSecurityGroupsString</a>
* <a href="#externalSubnetsString">const externalSubnetsString</a>
* <a href="#functionIncludePackagesString">const functionIncludePackagesString</a>
* <a href="#functionIncludePathsString">const functionIncludePathsString</a>
* <a href="#setEcsCluster">function setEcsCluster</a>
* <a href="#acmCertificateARN">let acmCertificateARN</a>
* <a href="#computeIAMRolePolicyARNs">let computeIAMRolePolicyARNs</a>
* <a href="#ecsAutoCluster">let ecsAutoCluster</a>
* <a href="#ecsAutoClusterECSOptimizedAMIName">let ecsAutoClusterECSOptimizedAMIName</a>
* <a href="#ecsAutoClusterInstanceDockerImageVolumeSize">let ecsAutoClusterInstanceDockerImageVolumeSize</a>
* <a href="#ecsAutoClusterInstanceRolePolicyARNs">let ecsAutoClusterInstanceRolePolicyARNs</a>
* <a href="#ecsAutoClusterInstanceRootVolumeSize">let ecsAutoClusterInstanceRootVolumeSize</a>
* <a href="#ecsAutoClusterInstanceSwapVolumeSize">let ecsAutoClusterInstanceSwapVolumeSize</a>
* <a href="#ecsAutoClusterInstanceType">let ecsAutoClusterInstanceType</a>
* <a href="#ecsAutoClusterMaxSize">let ecsAutoClusterMaxSize</a>
* <a href="#ecsAutoClusterMinSize">let ecsAutoClusterMinSize</a>
* <a href="#ecsAutoClusterNumberOfAZs">let ecsAutoClusterNumberOfAZs</a>
* <a href="#ecsAutoClusterPublicKey">let ecsAutoClusterPublicKey</a>
* <a href="#ecsAutoClusterUseEFS">let ecsAutoClusterUseEFS</a>
* <a href="#ecsClusterARN">let ecsClusterARN</a>
* <a href="#ecsClusterEfsMountPath">let ecsClusterEfsMountPath</a>
* <a href="#ecsClusterSecurityGroup">let ecsClusterSecurityGroup</a>
* <a href="#externalPublicSubnets">let externalPublicSubnets</a>
* <a href="#externalSecurityGroups">let externalSecurityGroups</a>
* <a href="#externalSubnets">let externalSubnets</a>
* <a href="#externalVpcId">let externalVpcId</a>
* <a href="#functionIncludePackages">let functionIncludePackages</a>
* <a href="#functionIncludePaths">let functionIncludePaths</a>
* <a href="#functionMemorySize">let functionMemorySize</a>
* <a href="#useFargate">let useFargate</a>
* <a href="#usePrivateNetwork">let usePrivateNetwork</a>

<a href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts">config/index.ts</a> 


<h2 class="pdoc-module-header" id="config">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L19">const config</a>
</h2>

```typescript
const config: Config =  new pulumi.Config("cloud-aws");
```

<h2 class="pdoc-module-header" id="externalPublicSubnetsString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L99">const externalPublicSubnetsString</a>
</h2>

```typescript
const externalPublicSubnetsString: undefined | string =  config.get("externalPublicSubnets");
```

<h2 class="pdoc-module-header" id="externalSecurityGroupsString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L108">const externalSecurityGroupsString</a>
</h2>

```typescript
const externalSecurityGroupsString: undefined | string =  config.get("externalSecurityGroups");
```

<h2 class="pdoc-module-header" id="externalSubnetsString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L90">const externalSubnetsString</a>
</h2>

```typescript
const externalSubnetsString: undefined | string =  config.get("externalSubnets");
```

<h2 class="pdoc-module-header" id="functionIncludePackagesString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L42">const functionIncludePackagesString</a>
</h2>

```typescript
const functionIncludePackagesString: undefined | string =  config.get("functionIncludePackages");
```

<h2 class="pdoc-module-header" id="functionIncludePathsString">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L32">const functionIncludePathsString</a>
</h2>

```typescript
const functionIncludePathsString: undefined | string =  config.get("functionIncludePaths");
```

<h2 class="pdoc-module-header" id="setEcsCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L190">function setEcsCluster</a>
</h2>

```typescript
setEcsCluster(cluster: aws.ecs.Cluster, securityGroup?: pulumi.Output<string>, efsMountPath?: undefined | string): void
```


setEcsCluster configures the ambient ECS cluster imperatively rather than using standard configuration.

<h2 class="pdoc-module-header" id="acmCertificateARN">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L61">let acmCertificateARN</a>
</h2>

```typescript
let acmCertificateARN: undefined | string =  config.get("acmCertificateARN");
```


Optional ACM certificate ARN to support services HTTPS traffic.

<h2 class="pdoc-module-header" id="computeIAMRolePolicyARNs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L56">let computeIAMRolePolicyARNs</a>
</h2>

```typescript
let computeIAMRolePolicyARNs: undefined | string =  config.get("computeIAMRolePolicyARNs");
```


Set the IAM role policies to apply to compute (both Lambda and ECS) within this Pulumi program. The default is:
"arn:aws:iam::aws:policy/AWSLambdaFullAccess,arn:aws:iam::aws:policy/AmazonEC2ContainerServiceFullAccess".

<h2 class="pdoc-module-header" id="ecsAutoCluster">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L133">let ecsAutoCluster</a>
</h2>

```typescript
let ecsAutoCluster: boolean =  config.getBoolean("ecsAutoCluster") || false;
```


Optionally auto-provision an ECS Cluster.  If set to true, parameters for the cluster can be provided via
the other "ecsAutoCluster*" configuration variables.

<h2 class="pdoc-module-header" id="ecsAutoClusterECSOptimizedAMIName">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L181">let ecsAutoClusterECSOptimizedAMIName</a>
</h2>

```typescript
let ecsAutoClusterECSOptimizedAMIName: undefined | string =  config.get("ecsAutoClusterECSOptimizedAMIName");
```


The name of the ECS-optimzed AMI to use for the Container Instances in this cluster, e.g.
"amzn-ami-2017.09.l-amazon-ecs-optimized".

See http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html for valid values.

<h2 class="pdoc-module-header" id="ecsAutoClusterInstanceDockerImageVolumeSize">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L155">let ecsAutoClusterInstanceDockerImageVolumeSize</a>
</h2>

```typescript
let ecsAutoClusterInstanceDockerImageVolumeSize: undefined | number = 
    config.getNumber("ecsAutoClusterInstanceDockerImageVolumeSize");
```


The size (in GiB) of the EBS volume to attach to each instance as Docker Image volume.  Defaults to 50 GiB.

<h2 class="pdoc-module-header" id="ecsAutoClusterInstanceRolePolicyARNs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L147">let ecsAutoClusterInstanceRolePolicyARNs</a>
</h2>

```typescript
let ecsAutoClusterInstanceRolePolicyARNs: undefined | string =  config.get("ecsAutoClusterInstanceRolePolicyARNs");
```


The EC2 instance role policy ARN to use for the cluster.  Defaults to
`arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role,
 arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess`.

<h2 class="pdoc-module-header" id="ecsAutoClusterInstanceRootVolumeSize">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L151">let ecsAutoClusterInstanceRootVolumeSize</a>
</h2>

```typescript
let ecsAutoClusterInstanceRootVolumeSize: undefined | number =  config.getNumber("ecsAutoClusterInstanceRootVolumeSize");
```


The size (in GiB) of the EBS volume to attach to each instance as the root volume.  Defaults to 8 GiB.

<h2 class="pdoc-module-header" id="ecsAutoClusterInstanceSwapVolumeSize">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L160">let ecsAutoClusterInstanceSwapVolumeSize</a>
</h2>

```typescript
let ecsAutoClusterInstanceSwapVolumeSize: undefined | number =  config.getNumber("ecsAutoClusterInstanceSwapVolumeSize");
```


The size (in GiB) of the EBS volume to attach to each instance as the swap volume.  Defaults to 5 GiB.

<h2 class="pdoc-module-header" id="ecsAutoClusterInstanceType">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L141">let ecsAutoClusterInstanceType</a>
</h2>

```typescript
let ecsAutoClusterInstanceType: undefined | string =  config.get("ecsAutoClusterInstanceType");
```


The EC2 instance type to use for the cluster.  Defaults to `t2.micro`.

<h2 class="pdoc-module-header" id="ecsAutoClusterMaxSize">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L168">let ecsAutoClusterMaxSize</a>
</h2>

```typescript
let ecsAutoClusterMaxSize: undefined | number =  config.getNumber("ecsAutoClusterMaxSize");
```


The maximum size of the cluster. Defaults to 100.

<h2 class="pdoc-module-header" id="ecsAutoClusterMinSize">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L164">let ecsAutoClusterMinSize</a>
</h2>

```typescript
let ecsAutoClusterMinSize: undefined | number =  config.getNumber("ecsAutoClusterMinSize");
```


The minimum size of the cluster. Defaults to 2.

<h2 class="pdoc-module-header" id="ecsAutoClusterNumberOfAZs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L137">let ecsAutoClusterNumberOfAZs</a>
</h2>

```typescript
let ecsAutoClusterNumberOfAZs: undefined | number =  config.getNumber("ecsAutoClusterNumberOfAZs");
```


The number of AZs to create subnets in as part of the cluster.  Defaults to 2.

<h2 class="pdoc-module-header" id="ecsAutoClusterPublicKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L174">let ecsAutoClusterPublicKey</a>
</h2>

```typescript
let ecsAutoClusterPublicKey: undefined | string =  config.get("ecsAutoClusterPublicKey");
```


Public key material for SSH access to the cluster. See allowed formats at:
https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html
If not provided, no SSH access is enabled on VMs.

<h2 class="pdoc-module-header" id="ecsAutoClusterUseEFS">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L185">let ecsAutoClusterUseEFS</a>
</h2>

```typescript
let ecsAutoClusterUseEFS: boolean =  config.getBoolean("ecsAutoClusterUseEFS") || false;
```


Optionally auto-provision an Elastic File System for the Cluster.  Defaults to false.

<h2 class="pdoc-module-header" id="ecsClusterARN">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L67">let ecsClusterARN</a>
</h2>

```typescript
let ecsClusterARN: pulumi.Input<string> | undefined =  config.get("ecsClusterARN");
```


Optional ECS cluster ARN.  If not provided, `Service`s and `Task`s are not available for the target
environment.

<h2 class="pdoc-module-header" id="ecsClusterEfsMountPath">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L77">let ecsClusterEfsMountPath</a>
</h2>

```typescript
let ecsClusterEfsMountPath: undefined | string =  config.get("ecsClusterEfsMountPath");
```


Optional EFS mount path on the cluster hosts.  If not provided, `Volumes` cannot be used in `Service`s and `Task`s.

<h2 class="pdoc-module-header" id="ecsClusterSecurityGroup">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L72">let ecsClusterSecurityGroup</a>
</h2>

```typescript
let ecsClusterSecurityGroup: pulumi.Input<string> | undefined =  config.get("ecsClusterSecurityGroup");
```


Optional ECS cluster security group that all ALBs for services within the cluster will use.

<h2 class="pdoc-module-header" id="externalPublicSubnets">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L103">let externalPublicSubnets</a>
</h2>

```typescript
let externalPublicSubnets: string[] | undefined =  undefined;
```


Provide public subnets ids for the VPC as a comma-seperated string.  Required if using an existing VPC.

<h2 class="pdoc-module-header" id="externalSecurityGroups">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L112">let externalSecurityGroups</a>
</h2>

```typescript
let externalSecurityGroups: string[] | undefined =  undefined;
```


Provide securityGroup ids for the VPC as a comma-seperated string.  Required if using an existing VPC.

<h2 class="pdoc-module-header" id="externalSubnets">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L94">let externalSubnets</a>
</h2>

```typescript
let externalSubnets: string[] | undefined =  undefined;
```


Provide subnets ids for the VPC as a comma-seperated string.  Required if using an existing VPC.

<h2 class="pdoc-module-header" id="externalVpcId">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L88">let externalVpcId</a>
</h2>

```typescript
let externalVpcId: undefined | string =  config.get("externalVpcId");
```


Use an existing VPC.  If both `usePrivateNetwork` and `externalVpcId` are provided, the VPC must be configured to run
all compute in private subnets with Internet egress enabled via NAT Gateways.

<h2 class="pdoc-module-header" id="functionIncludePackages">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L47">let functionIncludePackages</a>
</h2>

```typescript
let functionIncludePackages: string[] | undefined =  undefined;
```


Comma-seperated list of additional packages (relative to the project root) to include in Lambda zip uploads for
JavaScript callbacks.  E.g "body-parser,typescript".

<h2 class="pdoc-module-header" id="functionIncludePaths">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L37">let functionIncludePaths</a>
</h2>

```typescript
let functionIncludePaths: string[] | undefined =  undefined;
```


Comma-seperated list of additional paths (relative to the project root) to include in Lambda zip uploads for
JavaScript callbacks.  E.g "./img.png,app/".

<h2 class="pdoc-module-header" id="functionMemorySize">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L27">let functionMemorySize</a>
</h2>

```typescript
let functionMemorySize: number =  config.getNumber("functionMemorySize") || 128;
```


Optionally override the Lambda function memory size for all functions.

<h2 class="pdoc-module-header" id="useFargate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L127">let useFargate</a>
</h2>

```typescript
let useFargate: boolean =  config.getBoolean("useFargate") || false;
```


Optionally use Fargate-based container compute. All tasks must be Fargate-compatible.

<h2 class="pdoc-module-header" id="usePrivateNetwork">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-cloud/blob/master/aws/config/index.ts#L82">let usePrivateNetwork</a>
</h2>

```typescript
let usePrivateNetwork: boolean =  config.getBoolean("usePrivateNetwork") || false;
```


Optionally put all compute in a private network with no Internet ingress except via explicit API.

