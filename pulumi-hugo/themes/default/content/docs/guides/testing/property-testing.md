---
title: Property Testing
meta_desc: "Guide to property testing of Pulumi programs with Policy as Code (CrossGuard)."
weight: 2

menu:
  userguides:
    parent: testing
---

[Policy as Code]({{< relref "../crossguard" >}}) (also known as "CrossGuard") is Pulumi's offering to set guardrails and enforce compliance for cloud resources. Typically, policy packs would run across multiple projects and stacks to apply organization-wide rules.

**Property Testing** repurposes the power of policy definitions for developers to define invariants, or properties, that must hold for a specific stack they are working on. While Policy as Code and Property Testing both use the same technology, the goals and workflows are different.

This guide walks you through an example of a property test written in TypeScript. A sample Pulumi program provisions an Amazon EKS cluster. The test ensures two properties of the EKS cluster:

- Running Kubernetes version `1.13`.
- Provisioned inside a private VPC, rather than the default one.

## Blank Project

Our setup consists of two directories. The parent folder contains a typical Pulumi program written in TypeScript and bootstrapped with `pulumi new aws-typescript` command.

The sub-directory `tests` contains a policy pack with our future property tests and is created with `pulumi policy new aws-typescript` (notice the `policy` argument).

You can see the full layout in [the examples repository](https://github.com/pulumi/examples/tree/31056c3480cc445e5d4d3a8a0a86977adce2bc5e/testing-pac-ts).

Now it's time to write the code!

## Test-Driven Infrastructure

In true spirit of **test-driven development** (TDD), let's start with the tests themselves.

Here is the content of our `tests/index.ts` test file:

```typescript
import * as aws from "@pulumi/aws";
import * as policy from "@pulumi/policy";
import * as pulumi from "@pulumi/pulumi";

const stackPolicy: policy.StackValidationPolicy = {
    name: "eks-test",
    description: "EKS integration tests.",
    enforcementLevel: "mandatory",
    validateStack: async (args, reportViolation) => {
        const clusterResource = args.resources.find(r => r.isType(aws.eks.Cluster));
        const cluster = clusterResource && clusterResource.asType(aws.eks.Cluster);
        if (!cluster) {
            reportViolation("EKS Cluster not found");
            return;
        }

        // TODO 1: validate the cluster version

        // TODO 2: validate the cluster VPC
    },
}

const tests = new policy.PolicyPack("tests-pack", {
    policies: [stackPolicy],
});
```

This code does a few things worth describing. First, it imports all the packages that we're going to use. Notably, this includes the Policy SDK package for testing, and the AWS and Pulumi SDK packages. Note that it does **not** import the Pulumi program with the EKS cluster definition. The tests are going to run against any program that satisfies its invariants.

Then, the code creates a single [stack policy](https://pulumi.com/docs/guides/crossguard/core-concepts/#stack-validation-policy) to describe the properties of the EKS cluster. The first implicit property is the fact that there is an EKS cluster in the stack at all. If the cluster is not found, the test reports a violation (failure).

Now, we can add the tests for our two properties. Add the following code in place of the first TODO item:

```typescript
if (cluster.version !== "1.13") {
    reportViolation(
        `Expected EKS Cluster '${cluster.name}' version to be '1.13' but found '${cluster.version}'`);
}
```

The version test checks a property from our EKS cluster, `cluster.version`, and fails if the version is anything but 1.13 (including if it is unknown).

The VPC test is slightly more involved:

```typescript
const vpcId = cluster.vpcConfig.vpcId;
if (!vpcId) {
    if (!pulumi.runtime.isDryRun()) {
        reportViolation(`EKS Cluster '${cluster.name}' has unknown VPC`);
    }
    return;
}

const ec2 = new aws.sdk.EC2({region: aws.config.region});
const response = await ec2.describeVpcs().promise();
const defaultVpc = response.Vpcs?.find(vpc => vpc.IsDefault);
if (!defaultVpc) {
    reportViolation("Default VPC not found");
    return;
}

if (defaultVpc.VpcId === vpcId) {
    reportViolation(`EKS Cluster '${cluster.name}' should not use the default VPC`);
}
```

The first part asserts that there is a non-empty VPC identifier assigned to the cluster. Then, the test uses the AWS SDK to retrieve the default VPC. Finally, it compares the two IDs to make sure they are equal.

## Our Base (Failing) Program

Here is the program we'll be testing. Keeping with our TDD theme, let's start with the tests failing to begin with (we are using the default VPC and not specifying a version):

```typescript
import * as eks from "@pulumi/eks";

// Create a basic EKS cluster.
const cluster = new eks.Cluster("my-cluster", {
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 2,
    storageClasses: "gp2",
    deployDashboard: false,
});
```

To run our tests, we need to run the deployment with `pulumi up` but also pass an extra parameter to point to the `tests` policies. As expected, the result shows a test failure at the bottom:

```
$ pulumi up --policy-pack tests

Previewing update (dev):
...

Policy Violations:
    [mandatory]  tests-pack v1  eks-test (pac-ts-eks-dev: pulumi:pulumi:Stack)
    EKS integration tests.
    Expected EKS Cluster 'my-cluster-eksCluster-3187fd6' version to be '1.13' but found 'undefined'
```

Note that only one test failed: the VPC test requires the actual deployment to run to retrieve a VPC ID because ID is unknown during the preview (the VPC does not exist yet).

## Fixing Our Program

Now let's refactor our infrastructure so that the failing test starts passing. In the TDD spirit, we only fix the version test now, because it was the one with a violation.

To fix the first problem, we need to pass the Kubernetes version explicitly when creating our cluster. That's as simple as passing a new argument:

```typescript
const cluster = new eks.Cluster("my-cluster", {
    ...
    version: "1.13",
});
```

If we rerun `pulumi up --policy-pack tests`, we'll see that the preview now passes:

```
$ pulumi up --policy-pack tests

Previewing update (dev):
...

Policy Packs run:
    Name                Version
    tests-pack (tests)  (local)

Do you want to perform this update?
  yes
> no
  details
```

Choose 'yes' to deploy the infrastructure and rerun the tests. After the update complete, the tests run again to inspect the actual resources. Predictably, the VPC test fails now:

```
...
Policy Violations:
    [mandatory]  tests-pack v1  eks-test (pac-ts-eks-dev: pulumi:pulumi:Stack)
    EKS integration tests.
    EKS Cluster 'my-cluster-eksCluster-55b01ab' should not use the default VPC
```

Let's fix the second test by creating a custom VPC&mdash;the
`awsx.ec2.Vpc` component makes this easy&mdash;and then passing its resulting ID and subnet IDs as arguments.

```typescript
const vpc = new awsx.ec2.Vpc("my-vpc");
const cluster = new eks.Cluster("my-cluster", {
    vpcId: vpc.id,
    subnetIds: vpc.publicSubnetIds,
    ...
});
```

For reference, here is the complete, corrected `index.ts` file we have now:

```typescript
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a custom VPC.
const vpc = new awsx.ec2.Vpc("my-vpc");

// Create a basic EKS cluster.
const cluster = new eks.Cluster("my-cluster", {
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 2,
    storageClasses: "gp2",
    deployDashboard: false,
    version: "1.13",
    vpcId: vpc.id,
    subnetIds: vpc.publicSubnetIds,
});
```

If we run `pulumi up --policy-pack tests -y`, we'll see that all the tests now pass after the VPC is created and the cluster is replaced:

```typescript\
$ pulumi up --policy-pack tests -y
...
Resources:
    + 30 created
    ~ 2 updated
    +-14 replaced
    46 changes. 13 unchanged

Policy Packs run:
    Name                Version
    tests-pack (tests)  (local)
```

Voila! A successfully stood up EKS cluster, with built-in TDD security safeguards.

## Full Example

A complete runnable example of property tests is available in the examples repository: [Property Testing with TypeScript](https://github.com/pulumi/examples/tree/31056c3480cc445e5d4d3a8a0a86977adce2bc5e/testing-pac-ts).
