---
title: "Writing CrossGuard Policies"
date: 2019-12-19
meta_desc: "A look at the different types of policies that can be written for Pulumi CrossGuard."
meta_image: crossguard.png
authors:
    - justin-vanpatten
tags:
    - crossguard
    - policy-as-code
---

We recently announced [a new policy as code solution, CrossGuard]({{< relref "/blog/announcing-crossguard-preview" >}}) that validates policies at deployment time. Policies are expressed as code and are used to prevent the creation of out-of-compliance resources. Since policies are written using full-blown programming languages, it's possible to do interesting things such as [combining IAM Access Analyzer and Pulumi CrossGuard]({{< relref "/blog/aws-iam-access-analyzer-and-crossguard" >}}). In this post, we'll take a closer look at the different types of policies that can be written.

<!--more-->

## Authoring Policies

A policy contains specific logic you want to enforce. For example, you may want to prevent the creation of public, world-readable storage objects (e.g. on AWS S3, Azure BlobStore, etc.) or prevent the creation of a virtual machine without the proper security groups in-place. Policies are run during `pulumi preview` and `pulumi update`, ensuring that cloud resource definitions are in compliance.

Policies are written as validation functions that are evaluated against all resources in your Pulumi stack. If the validation function calls `reportViolation`, the associated resource will be considered in violation of the policy.

There are two types of policies:

1. `ResourceValidationPolicy` - Validates a particular resource in a stack.
2. `StackValidationPolicy` - Validates the stack as a whole.

Let's take a closer look at these and why you'd use one over the other.

## Resource Validation Policies

Policies of `ResourceValidationPolicy` are called for each resource in a stack. These policies are run _before_ a resource is registered and thus block an out-of-compliance resource from ever being created or modified.

A resource validation function is passed `args` with more information about the resource (such as the resource's type, _input_ properties, name, and URN) and a `reportViolation` callback that can be called to report a policy violation. In most cases, you will just use the helper function `validateTypedResource` to filter the resource type you want to validate and provide stronger typing of the resource's input properties.

An example resource validation policy is shown below:

```typescript
const ec2DetailedMonitoring: ResourceValidationPolicy = {
    name: "ec2-detailed-monitoring",
    description: "Detailed monitoring should be enabled for all EC2 instances.",
    enforcementLevel: "mandatory",
    validateResource: validateTypedResource(aws.ec2.Instance, (instance, args, reportViolation) => {
        if (instance.monitoring !== true) {
            reportViolation("EC2 Instance should have monitoring enabled.");
        }
    }),
};
```

If you have multiple resources that require a similar policy, you can group them together under one policy. This is possible by setting `validateResource` to an array of callback functions. The example below shows a case where we want to run similar checks against multiple types of resources.

```typescript
const elbLoggingEnabled: ResourceValidationPolicy = {
    name: "elb-logging-enabled",
    description: "Checks whether the Application Load Balancers and the Classic Load Balancers have logging enabled.",
    enforcementLevel: "mandatory",
    validateResource: [
        validateTypedResource(aws.elasticloadbalancing.LoadBalancer, (loadBalancer, args, reportViolation) => {
            if (loadBalancer.accessLogs === undefined || !loadBalancer.accessLogs.enabled) {
                reportViolation("Elastic Load Balancer must have access logs enabled.");
            }
        }),
        validateTypedResource(aws.elasticloadbalancingv2.LoadBalancer, (loadBalancer, args, reportViolation) => {
            if (loadBalancer.accessLogs === undefined || !loadBalancer.accessLogs.enabled) {
                reportViolation("Elastic Load Balancer must have access logs enabled.");
            }
        }),
        validateTypedResource(aws.applicationloadbalancing.LoadBalancer, (loadBalancer, args, reportViolation) => {
            if (loadBalancer.accessLogs === undefined || !loadBalancer.accessLogs.enabled) {
                reportViolation("Application Load Balancer must have access logs enabled.");
            }
        }),
    ],
};
```

## Stack Validation Policies

Policies of `StackValidationPolicy` are run against the stack as a whole. These policies are run _after_ all stack resources are registered and thus do not block an out-of-compliance resource from being created or modified, but do fail the preview or update. To avoid creating out-of-compliance resources, we recommend running a preview command before an update. However, there are cases where a policy requires a resource to exist in order to perform its validation, such as inspecting the resource's output properties that are only available to already provisioned resources (e.g. checking if a resource's `id` is referenced by another resource). In such cases, the policy can skip reporting violations during previews and only report violations during updates when the information it needs is available. Thus, the preview will succeed and the resources will be created or modified during the update, but the overall update operation will fail if any resources are in violation.

A stack validation function is passed `args` with information about all of the resources in the stack (such as each resource's type, _output_ properties, name, and URN) and a `reportViolation` callback that can be called to report a policy violation. `reportViolation` requires passing a `message` and also supports an optional `urn` parameter, to specify the URN of the resource in violation (otherwise violation is associated with the stack itself).

An example stack validation policy is shown below:

```typescript
import { Resource } from "@pulumi/pulumi";
import * as q from "@pulumi/pulumi/queryable";
import * as aws from "@pulumi/aws";
import { PolicyPack, ReportViolation, StackValidation, StackValidationArgs, StackValidationPolicy } from "@pulumi/policy";

const s3BucketLoggingEnabled: StackValidationPolicy = {
    name: "s3-bucket-logging-enabled",
    description: "Checks whether logging is enabled for your S3 buckets.",
    enforcementLevel: "mandatory",
    validateStack: validateTypedResources(aws.s3.Bucket, (buckets, args, reportViolation) => {
        // First, save any bucket IDs that are being used as logging targets.
        const logBucketIDs: Set<string> = new Set();
        for (const bucket of buckets) {
            if (bucket.loggings) {
                for (const logging of bucket.loggings) {
                    if (logging.targetBucket) {
                        logBucketIDs.add(logging.targetBucket);
                    }
                }
            }
        }

        // Then, check the buckets for violations.
        for (const bucket of buckets) {
            // Skip any buckets that haven't yet been provisioned (i.e. during previews).
            if (!bucket.id) {
                continue;
            }
            // If the bucket doesn't have any loggings and the bucket itself isn't being used as
            // a log target, it's in violation of the policy.
            if (!bucket.loggings || bucket.loggings.length === 0) {
                if (!logBucketIDs.has(bucket.id)) {
                    reportViolation("Bucket logging must be defined.", bucket.urn);
                }
            }
        }
    }),
};

// Utility method for defining a new StackValidation that will return the resources matching the provided type.
function validateTypedResources<TResource extends Resource>(
    resourceClass: { new(...rest: any[]): TResource },
    validate: (
        resources: q.Resolved<TResource>[],
        args: StackValidationArgs,
        reportViolation: ReportViolation) => Promise<void> | void,
): StackValidation {
    return (args: StackValidationArgs, reportViolation: ReportViolation) => {
        const isInstance = (<any>resourceClass).isInstance;
        if (!isInstance || typeof isInstance !== "function") {
            return;
        }
        const resources = args.resources
            .filter(r => isInstance({ __pulumiType: r.type }) === true)
            .map(r => ({ ...r.props, urn: r.urn } as q.Resolved<TResource>));
        validate(resources, args, reportViolation);
    };
}
```

The above example checks whether logging is enabled on S3 buckets. If a bucket does not have a `loggings` property defined, it will be in violation of the policy unless the bucket is being used as a logging `targetBucket` of another bucket. The policy check is skipped if the bucket's `id` isn't available, meaning this policy will only run during updates when the resource `id`s are available.

At the time of writing, there is no built-in helper for stack validation policies similar to `validateTypedResource` for resource validation policies, so we've included our own helper that can be used until a [built-in helper](https://github.com/pulumi/pulumi-policy/issues/158) is available.

## Resource Validation vs. Stack Validation

|                                | Resource Validation                   | Stack Validation                                     |
|--------------------------------|---------------------------------------|------------------------------------------------------|
| What does it check?            | Individual resources                  | All resources in the stack                           |
| When is the check performed?   | Before resources are created/modified | After all stack resources have been created/modified |
| What information is available? | Resource _input_ properties           | Resource _output_ properties                         |

In summary:

- Use resource validation policies when you want to check individual types of resources and block them from being created or modified, checking resource _input_ properties.

- Use stack validation policies when you want to check the stack as a whole (all resources) after they've been created or modified, checking resource _output_ properties.

## Trying It Out

In this post, we've seen the different types of CrossGuard policies that can be written. To give it a try, [download and install Pulumi]({{< relref "/docs/get-started" >}}) and [get started with policy as code]({{< relref "/docs/get-started/crossguard" >}}). For examples of policies, check out [Pulumi CrossGuard policies for AWS (AWSGuard)](https://github.com/pulumi/pulumi-policy-aws) or our [policy examples](https://github.com/pulumi/examples/tree/master/policy-packs).
