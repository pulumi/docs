---
title: Cloud Framework Preview
meta_desc: The Cloud framework for Pulumi lets you program infrastructure and application logic using high-level
           cloud-agnostic building blocks.
aliases: ["/docs/quickstart/cloudfx/"]
---

<img src="/images/docs/quickstart/cloudfx-purple.png" align="right">

The Cloud Framework for Pulumi lets you program infrastructure and application logic, side by side, using simple, high-level, cloud-agnostic building blocks.

The Cloud Framework must be configured with credentials to deploy and update resources in the target cloud adoption platform.

See the [full API documentation]({{< relref "/docs/reference/pkg/nodejs/pulumi/cloud" >}}) for complete details of the available Cloud Framework [APIs](https://www.pulumi.com/docs/reference/pkg/).

For AWS-specific use cases, see also the [awsx]({{< relref "/docs/reference/pkg/nodejs/pulumi/awsx" >}}) library which provides higher-level libraries for working with many AWS services.

## Getting Started

The easiest way to start with the Cloud Framework is to follow one of the tutorials for adoption:

* [A simple serverless REST API]({{< relref "rest-api" >}}): Deploy cloud-agnostic managed REST API
* [A simple containerized app]({{< relref "service" >}}): Deploy cloud-agnostic containerized services
* [Serverless + Containers + Infrastructure]({{< relref "thumbnailer" >}}): Deploy a complete cloud-agnostic application using a combination of buckets, serverless functions and containers.

In addition to the tutorials, several interesting examples are available complete with instructions for adoption:

* [HTTP API](https://github.com/pulumi/examples/tree/master/cloud-js-api)
* [Containers](https://github.com/pulumi/examples/tree/master/cloud-js-containers)
* [Thumbnailer (buckets, containers, functions)](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer)
* [URL Shortener (table, API)](https://github.com/pulumi/examples/tree/master/cloud-ts-url-shortener)
* [Voting App (table, API)](https://github.com/pulumi/examples/tree/master/cloud-ts-voting-app)

## Example

```javascript
const cloud = require("@pulumi/cloud");
const api = new cloud.API("my-api");

api.get("/hello", (req, res) => {
    res.json({ message: "Hi, world!" });
});

exports.url = api.publish().url;
```

## Libraries

The following packages are available in package managers:

* JavaScript/TypeScript: [https://www.npmjs.com/package/@pulumi/cloud](https://www.npmjs.com/package/@pulumi/cloud)

The provider-specific implementations of this library are also available for use directly when writing code that does not need to be portable:

* JavaScript/TypeScript: [https://www.npmjs.com/package/@pulumi/cloud-aws](https://www.npmjs.com/package/@pulumi/cloud-aws)

The Cloud Framework is open source and available in the [pulumi/pulumi-cloud](https://github.com/pulumi/pulumi-cloud) repo.

## Authentication

Authentication options must be set for the target cloud provider. See the [AWS setup page]({{< relref "/docs/intro/cloud-providers/aws/setup" >}}) for details (more providers for the Cloud Framework coming soon).

## Configuration

The Cloud Framework accepts the following configuration settings.  These can be provided via `pulumi config set cloud:<option>`.

* `provider`: (Required) The provider to deploy cloud resources into. Currently only `aws` is supported.

The AWS implementation of the Cloud Framework accepts the following configuration settings.  These can be provided via `pulumi config set cloud-aws:<option>`.

* `functionMemorySize`: (Optional) Override the Lambda function memory size for all functions.
* `functionIncludePaths`: (Optional) Comma-separated list of additional paths (relative to the project root) to include in Lambda zip uploads for JavaScript callbacks.  E.g `./img.png,app/`.
* `functionIncludePackages`: (Optional) Comma-separated list of additional packages (relative to the project root) to include in Lambda zip uploads for JavaScript callbacks.  E.g `body-parser,typescript`.
* `computeIAMRolePolicyARNs`: (Optional) Set the IAM role policies to apply to compute (both Lambda and ECS) within this Pulumi program. The default is: `arn:aws:iam::aws:policy/AWSLambdaFullAccess,arn:aws:iam::aws:policy/AmazonEC2ContainerServiceFullAccess`.
* `acmCertificateARN`: (Optional) ACM certificate ARN to support services HTTPS traffic.
* `ecsClusterARN`: (Optional) ECS cluster ARN. One of `useFargate`, `ecsClusterARN`, or `ecsAutoCluster` must be provided to use container-based resources like `cloud.Service` and `cloud.Task`.
* `ecsClusterSecurityGroup`: (Optional) ECS cluster security group that all ALBs for services within the cluster will use.
* `ecsClusterEfsMountPath`: (Optional) EFS mount path on the cluster hosts.  If not provided, `Volumes` cannot be used in `cloud.Service` and `cloud.Task`.
* `usePrivateNetwork`: (Optional) Put all compute in a private network.
* `externalVpcId`: (Optional) Use an existing VPC.  If both `usePrivateNetwork` and `externalVpcId` are provided, the VPC must be configured to run all compute in private subnets with Internet egress enabled via NAT Gateways.
* `externalSubnets`: (Optional) Provide subnets ids for the VPC as a comma-separated string.  Required if using an existing VPC.
* `externalPublicSubnets`: (Optional) Provide public subnets ids for the VPC as a comma-separated string.  Required if using an existing VPC.
* `externalSecurityGroups`: (Optional) Provide securityGroup ids for the VPC as a comma-separated string.  Required if using an existing VPC.
* `useFargate`: (Optional) Wse Fargate-based container compute. All tasks must be Fargate-compatible. One of `useFargate`, `ecsClusterARN`, or `ecsAutoCluster` must be provided to use container-based resources like `cloud.Service` and `cloud.Task.
* `ecsAutoCluster`: (Optional) Auto-provision an ECS Cluster.  If set to true, parameters for the cluster can be provided via the other "ecsAutoCluster*" configuration variables. One of `useFargate`, `ecsClusterARN`, or `ecsAutoCluster` must be provided to use container-based resources like `cloud.Service` and `cloud.Task.
* `ecsAutoClusterNumberOfAZs`: (Optional) The number of AZs to create subnets in as part of the cluster.  Defaults to `2`.
* `ecsAutoClusterInstanceType`: (Optional) The EC2 instance type to use for the cluster.  Defaults to `t2.micro`.
* `ecsAutoClusterInstanceRolePolicyARNs`: (Optional) The EC2 instance role policy ARN to use for the cluster.  Defaults to `arn:aws:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role,arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess`.
* `ecsAutoClusterInstanceRootVolumeSize`: (Optional) The size (in GiB) of the EBS volume to attach to each instance as the root volume.  Defaults to `8` GiB.
* `ecsAutoClusterInstanceDockerImageVolumeSize`: (Optional) The size (in GiB) of the EBS volume to attach to each instance as Docker Image volume.  Defaults to `50` GiB.
* `ecsAutoClusterInstanceSwapVolumeSize`: (Optional) The size (in GiB) of the EBS volume to attach to each instance as the swap volume.  Defaults to `5` GiB.
* `ecsAutoClusterMinSize`: (Optional) The minimum size of the cluster. Defaults to `2`.
* `ecsAutoClusterMaxSize`: (Optional) The maximum size of the cluster. Defaults to `100`.
* `ecsAutoClusterPublicKey`: (Optional) Public key material for SSH access to the cluster. See [allowed formats](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html). If not provided, no SSH access is enabled on VMs.
* `ecsAutoClusterECSOptimizedAMIName`: (Optional) The name of the ECS-optimzed AMI to use for the Container Instances in this cluster, e.g. `amzn-ami-2017.09.l-amazon-ecs-optimized`. See [valid values](http://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-optimized_AMI.html).
* `ecsAutoClusterUseEFS`: (Optional) Optionally auto-provision an Elastic File System for the Cluster.  Defaults to `false`.
