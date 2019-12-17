---
title: CrossGuard Core Concepts
meta_desc: This page contains an overview of core concepts when interacting with Pulumi CrossGuard and
           Policy Pack.
linktitle: Core Concepts
weight: 1

menu:
  userguides:
    parent: crossguard
---
{{% crossguard-preview %}}

## Policy

A Policy contains specific logic you would like to enforce. For example, you may want to prevent the creation of public, world-readable storage objects. (e.g. on AWS S3, Azure BlobStore, etc.) or prevent the creation of a virtual machine without the proper security groups in-place.

Policies are written as validation functions that are evaluated against all resources in your Pulumi stack. If the validation function calls `reportViolation`, the associated resource will be considered in violation of the policy. `reportViolation` can be called multiple times to report multiple violations.

Policies validation functions are executed during `pulumi preview` and `pulumi update`, asserting that cloud resource definitions comply with the policy immediately before they are created or updated.

During `preview`, every resource is checked for policy violations, which are batched up into a final report. During the `update`, the first policy violation will halt the deployment.

When authoring a policy, you must specify an Enforcement Level: `advisory` or `mandatory`. An enforcement level of `advisory` simply prints a warning message to users. A `mandatory` enforcement level means that an update will halt before creating a resource that violates that policy.

There are two types of policies: `ResourceValidationPolicy` validate a particular resource in a stack and `StackValidationPolicy` validates against the entire stack allowing you to write assertions that require multiple resources.

### Resource Validation

Policies of `ResourceValidationPolicy` validate against a particular resource in a stack. These policies are run before a resource is registered and thus block an out-of-compliance resource from ever being created.

A resource validation is passed `args` with more information about the resource and a `reportViolation` callback that can be used to report a policy violation. In most cases, you will just use the helper function `validateTypedResource` to filter the resource type you want to validate.

An example resource validation policy is shown below:

```typescript
const s3AclPolicy: ResourceValidationPolicy = {
    name: "s3-no-public-read",
    description: "Prohibits setting the public-read or public-read-write permission on AWS S3 buckets.",
    enforcementLevel: "mandatory",
    validateResource: validateTypedResource(aws.s3.Bucket, (bucket, args, reportViolation) => {
        if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
            reportViolation("S3 buckets cannot have an ACL set as public-read or public-read-write.");
        }
    }),
};
```

If you have multiple resources that require a similar policy, you can group them together under one policy. This is possible by setting `validateResource` to an array of `ResourceValidationPolicy`. The example below shows a case where we want to run similar checks against multiple types of resources.

```typescript
const elbLoggingPolicy: ResourceValidationPolicy = {
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

### Stack Validation Policy

Policies of `StackValidationPolicy` are run against all the resources in a stack. These policies are run are all stack resources are registered and thus *do not* block an out-of-compliance resource from being created, but do fail the `preview` or `update`. To avoid creating out-of-compliance resources, we recommend always running a `preview` command before an `update`. This allows you to write policies where one resource depends on the state or existence of another resource.

The below example requires that all dynamoDB tables have an App Autoscaling Policy associated with it.

```typescript
const dynamodbTableAutoscalingRequired: StackValidationPolicy = {
    name: "dynamodb-autoscaling-required",
    description: "Requires a dynamoDB table to have an associated App Autoscaling policy.",
    enforcementLevel: enforcementLevel,
    validateStack: (args: StackValidationArgs, reportViolation: ReportViolation) => {
        const dynamodbTables = getResolvedResources(aws.dynamodb.Table.isInstance, args);
        const appScalingPolicies = getResolvedResources(aws.appautoscaling.Policy.isInstance, args);

        const policyResourceIDMap: Record<string, q.ResolvedResource<aws.appautoscaling.Policy>> = {};
        for (const policy of appScalingPolicies) {
            policyResourceIDMap[policy.resourceId] = policy;
        }

        for (const table of dynamodbTables) {
            if (policyResourceIDMap[table.id] === undefined) {
                reportViolation(`DynamoDB table ${table.id} missing app autoscaling policy.`);
            }
        }
    },
}

// Utility method for returning all resources matching the provided type.
// Pulumi-policy will soon provide similar utility methods. For the meantime, you can
// use this utility method as an example for creating your own.
function getResolvedResources<TResource extends Resource>(
    typeFilter: (o: any) => o is TResource,
    args: StackValidationArgs,
): q.ResolvedResource<TResource>[] {
    return args.resources
        .map(r => (<unknown>{ ...r.props, __pulumiType: r.type } as q.ResolvedResource<TResource>))
        .filter(typeFilter);
}
```

A `StackValidationPolicy` can also be used to make validations against a resource that must already be created to validate. For example, a policy that
checks whether an Amazon Certificate Manager (ACM) certificate has expired would require the certificate already be created as it relies on its outputs.

 The [Pulumi Policy Packs examples repository](https://github.com/pulumi/examples/tree/master/policy-packs) provides example `ResourceValidationPolicy` and `StackValidationPolicy` rules for common cloud providers.

## Policy Pack

A Policy Pack can contain one or more policies to enforce. Packs provide a way to group together similar policies. For example, you may decide to have one pack with AWS policies and another with Kubernetes-specific policies. That being said, there are no restrictions on which policies you combine within a pack, and you should pack them however makes sense for your organization. Currently, there is a limitation of 25 policies per pack.

As part of CrossGuard, organization administrators can author and publish Policy Packs to the Pulumi Console.

## Policy Group

A Policy Group is a group of stacks with the same set of Policy Packs enforced. Policy Groups are only available from within the Pulumi Console when CrossGuard is enabled. A stack may belong to multiple Policy Groups. An example use of Policy Groups is to have a different group per environment. For example, you can have one for your stacks in production and a more permissive Policy Group for your other environments such as `staging` and `dev`.

Organization admins can create new Policy Groups, add stacks to a Policy Group, or remove stacks from a group.

Each Policy Group has its own set of enforced Policy Packs. An organization administrator can add, remove, or update the version of the Policy Pack enforced on the Policy Group.

In cases where a stack belongs to multiple Policy Groups and is therefore required to run multiple versions of the same Policy Pack, only the latest version of the Policy Pack gets enforced. For example, if `my-stack` belongs to two Policy Groups and you want to enforce `my-aws-policy-pack` versions 2 and 3, only version 3 will be enforced. You may view the Policy Groups a stack belongs to as well as the currently enforced Policy Packs for the stack by navigating to a stack’s `Settings` tab and then `Policies`.

### Default Policy Group

Every organization has a default Policy Group. When the default Policy Group is created, all stacks in your organization are automatically added to that Policy Group. Additionally, all stacks that are created after adding the default Policy Group are automatically added to it. Organization admins can remove stacks from the default Policy Group as desired.
