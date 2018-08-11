---
title: "Cloud Framework"
---

The Cloud framework for Pulumi lets you program infrastructure and application logic, side by side, using simple, high-level cloud building blocks.  This package has three key defining attributes:

- **Easy Cloud Development**: Build robust and scalable cloud applications with just a few lines of code.
- **Cloud Agnostic**: Not specific to any one particular cloud (AWS, Azure, Google Cloud, Kubernetes, and various on-premises clouds). Applications built using the high-level Cloud components like [`Service`], [`Table`], [`Topic`] and [`API`] can be deployed to a variety of cloud platforms. Although Pulumi only support AWS today in this framework, our plan is to offer an implementation of this on all major clouds.
* **Serverless**: The Cloud framework makes it easy to build applications with minimal fixed infrastructure, event-driven application logic, and using resources that are charged based on actual consumption.

The Cloud framework must be configured with credentials to deploy and update resources in the target cloud platform.

See the [full API documentation](./pkg/nodejs/@pulumi/cloud/index.html) for complete details of the available Cloud framework APIs.

## Example

```javascript
const cloud = require("@pulumi/cloud");

const api = new cloud.API("my-api");
api.get("/hello", (req, res) => {
    res.
});

exports.url = api.publish().url;
```

You can find additional examples of using the Cloud framework in [the Pulumi examples repo](https://github.com/pulumi/examples).
* [HTTP API](https://github.com/pulumi/examples/tree/master/cloud-js-api)
* [Containers](https://github.com/pulumi/examples/tree/master/cloud-js-containers)
* [Thumbnailer (buckets, containers, functions)](https://github.com/pulumi/examples/tree/master/cloud-js-thumbnailer)
* [URL Shortner (table, API)](https://github.com/pulumi/examples/tree/master/cloud-ts-url-shortener)
* [Voting App (table, API)](https://github.com/pulumi/examples/tree/master/cloud-ts-voting-app)

## Libraries

The following packages are available in package managers:
* JavaScript/TypeScript: https://www.npmjs.com/package/@pulumi/cloud

The provider-specific implementations of this library are also available for use directly when writing code that does not need to be portable:
* JavaScript/TypeScript: https://www.npmjs.com/package/@pulumi/cloud-aws

The Cloud framework is open source and available in the [pulumi/pulumi-cloud](https://github.com/pulumi/pulumi-cloud) repo. 

## Authentication

Authentication options must be set for the target cloud provider. See the [AWS installation page](/install/aws.html) for details (more providers for the Cloud framework coming soon).

## Configuration

The Cloud framework accepts the following configuration settings.  These can be provided via `pulumi config set cloud:<option>`.

* `provider`: (Required) The provider to deploy cloud resources into. Currently only `aws` is supported.

The AWS implementation of the Cloud framework accepts the following configuration settings.

<!-- TODO: Flesh out below. -->

* `functionMemorySize`: (Optional) 
* `functionIncludePaths`: (Optional) 
* `functionIncludePackages`: (Optional) 
* `computeIAMRolePolicyARNs`: (Optional) 
* `acmCertificateARN`: (Optional) 
* `ecsClusterARN`: (Optional) 
* `ecsClusterSecurityGroup`: (Optional) 
* `ecsClusterEfsMountPath`: (Optional) 
* `usePrivateNetwork`: (Optional) 
* `externalVpcId`: (Optional) 
* `externalSubnets`: (Optional) 
* `externalPublicSubnets`: (Optional) 
* `externalSecurityGroups`: (Optional) 
* `useFargate`: (Optional) 
* `ecsAutoCluster`: (Optional) 
* `ecsAutoClusterNumberOfAZs`: (Optional) 
* `ecsAutoClusterInstanceType`: (Optional) 
* `ecsAutoClusterInstanceRolePolicyARNs`: (Optional) 
* `ecsAutoClusterInstanceRootVolumeSize`: (Optional) 
* `ecsAutoClusterInstanceDockerImageVolumeSize`: (Optional) 
* `ecsAutoClusterInstanceSwapVolumeSize`: (Optional) 
* `ecsAutoClusterMinSize`: (Optional) 
* `ecsAutoClusterMaxSize`: (Optional) 
* `ecsAutoClusterPublicKey`: (Optional) 
* `ecsAutoClusterInstanceRolePolicyARNs`: (Optional) 
* `ecsAutoClusterECSOptimizedAMIName`: (Optional) 
* `ecsAutoClusterUseEFS`: (Optional) 

