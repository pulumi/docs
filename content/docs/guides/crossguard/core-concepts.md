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

{{< chooser language "typescript,python" />}}

{{% notes %}}
Python support is currently in preview.
{{% /notes %}}

## Policy

A Policy contains specific logic you would like to enforce. For example, you may want to prevent the creation of public, world-readable storage objects. (e.g. on AWS S3, Azure BlobStore, etc.) or prevent the creation of a virtual machine without the proper security groups in-place.

Policies are written as validation functions that are evaluated against all resources in your Pulumi stack. If the validation function calls {{< policy-reportviolation >}}, the associated resource will be considered in violation of the policy. {{< policy-reportviolation >}} can be called multiple times to report multiple violations.

Policies validation functions are executed during `pulumi preview` and `pulumi up`, asserting that cloud resource definitions comply with the policy immediately before they are created or updated.

During preview, every resource is checked for policy violations, which are batched up into a final report. During the update, the first policy violation will halt the deployment.

A policy can have an optional enforcement level of {{< policy-enforcementlevel-advisory >}}, {{< policy-enforcementlevel-mandatory >}}, or {{< policy-enforcementlevel-disabled >}}.

- {{< policy-enforcementlevel-advisory >}} simply prints a warning message when there is a violation.
- {{< policy-enforcementlevel-mandatory >}} means that an update will halt before creating a resource that violates that policy.
- {{< policy-enforcementlevel-disabled >}} prevents the policy from running.

The enforcement level can be set on the [Policy Pack](#policy-pack), which will apply to all policies in the Policy Pack, unless specified on a policy directly, which will override the value for that policy. If no enforcement level is specifed on either the policy pack or policy, the default of {{< policy-enforcementlevel-advisory >}} is used.

There are two types of policies:

1. `ResourceValidationPolicy` validates a particular resource in a stack before the resource is created or updated, looking at the resource's _input_ properties.
2. `StackValidationPolicy` validates all resources in the stack after they've been created/updated, but before the Pulumi preview/update has completed, looking at each resource's _output_ properties.

### Resource Validation

Policies of `ResourceValidationPolicy` validate against a particular resource in a stack. These policies are run before a resource is registered and thus block an out-of-compliance resource from ever being created.

A resource validation is passed `args` with more information about the resource and a {{< policy-reportviolation >}} callback that can be used to report a policy violation. In most cases in TypeScript/JavaScript, you will just use the helper function `validateResourceOfType` to filter the resource type you want to validate.

An example resource validation policy is shown below:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
const s3NoPublicRead: ResourceValidationPolicy = {
    name: "s3-no-public-read",
    description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
    enforcementLevel: "mandatory",
    validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
        if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
            reportViolation("You cannot set public-read or public-read-write on an S3 bucket.");
        }
    }),
};
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def s3_no_public_read_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:s3/bucket:Bucket" and "acl" in args.props:
        acl = args.props["acl"]
        if acl == "public-read" or acl == "public-read-write":
            report_violation(
                "You cannot set public-read or public-read-write on an S3 bucket.")

s3_no_public_read = ResourceValidationPolicy(
    name="s3-no-public-read",
    description="Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
    enforcement_level=EnforcementLevel.MANDATORY,
    validate=s3_no_public_read_validator,
)
```

{{% /choosable %}}

{{< /chooser >}}

If you have multiple resources that require a similar policy, you can group them together under one policy. This is possible by setting {{< policy-validateresource >}} to an array of `ResourceValidationPolicy`. The example below shows a case where we want to run similar checks against multiple types of resources.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
const elbLoggingEnabled: ResourceValidationPolicy = {
    name: "elb-logging-enabled",
    description: "Checks whether the Application Load Balancers and the Classic Load Balancers have logging enabled.",
    enforcementLevel: "mandatory",
    validateResource: [
        validateResourceOfType(aws.elasticloadbalancing.LoadBalancer, (loadBalancer, args, reportViolation) => {
            if (!loadBalancer.accessLogs || !loadBalancer.accessLogs.enabled) {
                reportViolation("Elastic Load Balancer must have access logs enabled.");
            }
        }),
        validateResourceOfType(aws.elasticloadbalancingv2.LoadBalancer, (loadBalancer, args, reportViolation) => {
            if (!loadBalancer.accessLogs || !loadBalancer.accessLogs.enabled) {
                reportViolation("Elastic Load Balancer must have access logs enabled.");
            }
        }),
        validateResourceOfType(aws.applicationloadbalancing.LoadBalancer, (loadBalancer, args, reportViolation) => {
            if (!loadBalancer.accessLogs || !loadBalancer.accessLogs.enabled) {
                reportViolation("Application Load Balancer must have access logs enabled.");
            }
        }),
    ],
};
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def elb_logging_enabled_elb_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:elasticloadbalancing/loadBalancer:LoadBalancer":
        if "accessLogs" not in args.props or not args.props["accessLogs"]["enabled"]:
            report_violation("Elastic Load Balancer must have access logs enabled.")

def elb_logging_enabled_elb2_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:elasticloadbalancingv2/loadBalancer:LoadBalancer":
        if "accessLogs" not in args.props or not args.props["accessLogs"]["enabled"]:
            report_violation("Elastic Load Balancer must have access logs enabled.")

def elb_logging_enabled_alb_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:applicationloadbalancing/loadBalancer:LoadBalancer":
        if "accessLogs" not in args.props or not args.props["accessLogs"]["enabled"]:
            report_violation("Application Load Balancer must have access logs enabled.")

elb_logging_enabled = ResourceValidationPolicy(
    name="elb-logging-enabled",
    description="Checks whether the Application Load Balancers and the Classic Load Balancers have logging enabled.",
    enforcement_level=EnforcementLevel.MANDATORY,
    validate=[
        elb_logging_enabled_elb_validator,
        elb_logging_enabled_elb2_validator,
        elb_logging_enabled_alb_validator,
    ],
)
```

{{% /choosable %}}

{{< /chooser >}}

### Stack Validation Policy

Policies of `StackValidationPolicy` are run against all the resources in a stack. These policies are run are all stack resources are registered and thus *do not* block an out-of-compliance resource from being created, but do fail the preview or update. To avoid creating out-of-compliance resources, we recommend always running a preview command before an update. This allows you to write policies where one resource depends on the state or existence of another resource.

The below example requires that all dynamoDB tables have an App Autoscaling Policy associated with it.

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
const dynamodbTableAutoscalingRequired: StackValidationPolicy = {
    name: "dynamodb-autoscaling-required",
    description: "Requires a dynamoDB table to have an associated App Autoscaling policy.",
    enforcementLevel: "mandatory",
    validateStack: (args: StackValidationArgs, reportViolation: ReportViolation) => {
        const dynamodbTables = args.resources.map(r => r.asType(aws.dynamodb.Table)).filter(r => r);
        const appScalingPolicies = args.resources.map(r => r.asType(aws.appautoscaling.Policy)).filter(r => r);

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
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def dynamodb_autoscaling_required_validator(args: StackValidationArgs, report_violation: ReportViolation):
    tables = filter(lambda r: r.resource_type == "aws:dynamodb/table:Table", args.resources)
    policies = filter(lambda r: r.resource_type == "aws:autoscaling/policy:Policy", args.resources)

    policy_resource_ids = set()
    for policy in policies:
        policy_resource_ids.add(policy["resourceId"])

    for table in tables:
        if table["id"] not in policy_resource_ids:
            report_violation(f"DynamoDB table {table['id']} missing app autoscaling policy.")

dynamodb_autoscaling_required = StackValidationPolicy(
    name="dynamodb-autoscaling-required",
    description="Requires a dynamoDB table to have an associated App Autoscaling policy.",
    enforcement_level=EnforcementLevel.MANDATORY,
    validate=dynamodb_autoscaling_required_validator,
)
```

{{% /choosable %}}

{{< /chooser >}}

A `StackValidationPolicy` can also be used to make validations against a resource that must already be created to validate. For example, a policy that
checks whether an Amazon Certificate Manager (ACM) certificate has expired would require the certificate already be created as it relies on its outputs.

The [Pulumi Policy Packs examples repository](https://github.com/pulumi/examples/tree/master/policy-packs) provides example `ResourceValidationPolicy` and `StackValidationPolicy` rules for common cloud providers.

### Resource Validation vs. Stack Validation

|                                | Resource Validation                   | Stack Validation                                                                     |
|--------------------------------|---------------------------------------|--------------------------------------------------------------------------------------|
| What does it check?            | Individual resources                  | All resources in the stack                                                           |
| When is the check performed?   | Before resources are created/modified | After all stack resources have been created/modified                                 |
| What information is available? | Resource _input_ properties           | Resource _output_ properties (Note: inputs are propagated to outputs during preview) |

## Policy Pack

A Policy Pack can contain one or more policies to enforce. Packs provide a way to group together similar policies. For example, you may decide to have one pack with AWS policies and another with Kubernetes-specific policies. That being said, there are no restrictions on which policies you combine within a pack, and you should pack them however makes sense for your organization.

As part of CrossGuard, organization administrators can author and publish Policy Packs to the Pulumi Console. Publishing Policy Packs to the Pulumi Console is currently supported for the Node.js Policy SDK (TypeScript/JavaScript). Python support is [coming soon](https://github.com/pulumi/pulumi-policy/issues/211).

## Policy Group

A Policy Group is a group of stacks with the same set of Policy Packs enforced. Policy Groups are only available from within the Pulumi Console when CrossGuard is enabled. A stack may belong to multiple Policy Groups. An example use of Policy Groups is to have a different group per environment. For example, you can have one for your stacks in production and a more permissive Policy Group for your other environments such as `staging` and `dev`.

Organization admins can create new Policy Groups, add stacks to a Policy Group, or remove stacks from a group.

Each Policy Group has its own set of enforced Policy Packs. An organization administrator can add, remove, or update the version of the Policy Pack enforced on the Policy Group.

In cases where a stack belongs to multiple Policy Groups and is therefore required to run multiple versions of the same Policy Pack, only the latest version of the Policy Pack gets enforced. For example, if `my-stack` belongs to two Policy Groups and you want to enforce `my-aws-policy-pack` versions 2 and 3, only version 3 will be enforced. You may view the Policy Groups a stack belongs to as well as the currently enforced Policy Packs for the stack by navigating to a stack’s `Settings` tab and then `Policies`.

### Default Policy Group

Every organization has a default Policy Group. When the default Policy Group is created, all stacks in your organization are automatically added to that Policy Group. Additionally, all stacks that are created after adding the default Policy Group are automatically added to it. Organization admins can remove stacks from the default Policy Group as desired.
