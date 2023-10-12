---
title_tag: "Core Concepts | CrossGuard"
meta_desc: This page contains an overview of core concepts when interacting with Pulumi CrossGuard and
           Policy Pack.
title: Concepts
h1: Pulumi policy as code concepts
weight: 2
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    parent: crossguard
    identifier: crossguard-core-concepts
aliases:
- /docs/guides/crossguard/core-concepts/
---

Policies can be written in TypeScript/JavaScript (Node.js) or Python and can be applied to Pulumi stacks written in any language. More information on [language support for policies](/docs/using-pulumi/crossguard#languages).

{{< chooser language "typescript,python" />}}

## Policies

A *Policy* contains specific logic you would like to enforce. For example, you may want to prevent the creation of public, world-readable storage objects. (e.g. on AWS S3, Azure BlobStore, etc.) or prevent the creation of a virtual machine without the proper security groups in-place.

Policies are written as validation functions that are evaluated against resources in your Pulumi stack. If the validation function calls {{< policy-reportviolation >}}, the associated resource will be considered in violation of the policy. {{< policy-reportviolation >}} can be called multiple times to report multiple violations.

Policies may also define *remediations* to automatically fix violations rather than report them. A remediation is written as a function that transforms a resource's state so that it complies with the policy. The resource will be configured using the transformed state.

Policies are executed during `pulumi preview` and `pulumi up`, ensuring that cloud resource definitions comply with the policy immediately before they are created or updated. During preview, every resource is checked for policy violations, which are batched up into a final report. Policy violations may show up as warnings, or errors which halt the deployment.

### Policy Packs

A Policy Pack contains a collection of policies to enforce. Packs provide a way to group together similar policies. For example, you may decide to have one pack with AWS policies and another with Kubernetes policies. Alternatively, you may have one pack that specifies security policies and another that defines cost management policies.

A policy pack has a name, a list of policies, and an optional default [enforcement level](#enforcement-levels):

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
import { PolicyPack } from "@pulumi/policy";

new PolicyPack("aws-best-practices", {
    enforcementLevel: "remediate",
    policies: [
        // ...
    ],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_policy import EnforcementLevel, PolicyPack

PolicyPack(
    name="aws-best-practices",
    enforcement_level=EnforcementLevel.REMEDIATE,
    policies=[
        # ...
    ],
)
```

{{% /choosable %}}

{{< /chooser >}}

There are no restrictions on which policies you combine within a pack, and you should pack them however makes sense for your organization. As part of CrossGuard, organization administrators can author, publish to, and enforce Policy Packs using the Pulumi Cloud.

### Types of Policies

There are two broad types of policies:

1. *Resource Policies*: These validate a particular resource in a stack before the resource is created or updated, looking at the resource's _input_ properties.
2. *Stack Policies*: These validate validates all resources in the stack after they've been created/updated, but before the Pulumi preview/update has completed, looking at each resource's _output_ properties.

This table summarizes the primary differences between the two types:

|                                | Resource Policies                     | Stack Policies                                                                       |
|--------------------------------|---------------------------------------|--------------------------------------------------------------------------------------|
| What does it check?            | Individual resources                  | All resources in the stack                                                           |
| When is the check performed?   | Before resources are created/modified | After all stack resources have been created/modified                                 |
| Can it remediate?              | Yes                                   | No                                                                                   |
| What information is available? | Resource _input_ properties           | Resource _output_ properties (Note: inputs are propagated to outputs during preview) |
| What is the type name?         | `ResourceValidationPolicy`            | `StackValidationPolicy`                                                              |

### Enforcement Levels

A policy has one of the following *enforcement levels*:

- {{< policy-enforcementlevel-advisory >}} prints a warning message when there is a violation.
- {{< policy-enforcementlevel-mandatory >}} halts an update before creating a resource that violates that policy.
- {{< policy-enforcementlevel-remediate >}} is stricter than mandatory and enables policy remediations where available.
- {{< policy-enforcementlevel-disabled >}} prevents the policy from running.

The enforcement level can be specified in multiple ways: on the definition of a policy, on the Policy Pack as a whole, or through [*Policy Configuration*](/docs/using-pulumi/crossguard/configuration/) for either. If the enforcement is set in multiple places, the most granular setting for any given policy is used (so, policy-specific configuration overrides the Policy Pack-wide configuration). The default enforcement level is {{< policy-enforcementlevel-advisory >}} if no enforcement level is specified on either the policy pack or policy.

### Resource Policies

Policies of `ResourceValidationPolicy` validate against a particular resource in a stack. These policies are run before a resource is registered and thus block an out-of-compliance resource from ever being created. Resource policies can validate compliance and report violations, remediate violations automatically, or do both.

#### Resource Validation

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

#### Resource Remediation

A policy may define a remediation which is similarly given `args` with information about the resource. Instead of reporting violations, however, the remediation may alter and return resource properties. The Pulumi engine will use these new properties in place of the original ones passed to the remediation function.

Here is an example resource policy remediation. Similar to resource validation, in TypeScript/JavaScript this example uses the `remediateResourceOfType` helper to filter and add strong typing:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
const s3NoPublicRead: ResourceValidationPolicy = {
    name: "s3-no-public-read",
    description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
    enforcementLevel: "remediate",
    remediateResource: remediateResourceOfType(aws.s3.Bucket, (bucket, args) => {
        if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
            // Modify the ACL and return the new bucket state to use instead.
            bucket.acl = "private";
            return bucket;
        }
    }),
};
```

{{% /choosable %}}
{{% choosable language python %}}

```python
def s3_no_public_read_remediator(args: ResourceValidationArgs):
    if args.resource_type == "aws:s3/bucket:Bucket" and "acl" in args.props:
        acl = args.props["acl"]
        if acl == "public-read" or acl == "public-read-write":
            # Modify the ACL and return the new bucket state to use instead.
            args.props["acl"] = "private
            return args.props

s3_no_public_read = ResourceValidationPolicy(
    name="s3-no-public-read",
    description="Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
    enforcement_level=EnforcementLevel.REMEDIATE,
    remediate=s3_no_public_read_remediator,
)
```

{{% /choosable %}}

{{< /chooser >}}

All remediations are run before validation takes place. This ensures that no policy violations occur if a resource *would* have flagged a policy violation, were it not for a remediation.

Remediations are order dependent because multiple remediations may mutate the same resource state. For organizations with many Policy Packs, they are sorted in lexicographic order; and within a Policy Pack, remediations are evaluated in the order specified. This ensures there is always a deterministic, predictable order in which they run.

#### Defining Resource Validations and Remediations Together

It is possible to define a resource validation and remediation together. This allows a policy to function as both when the enforcement level is set to {{< policy-enforcementlevel-remediate >}} in addition to when it is not. It also serves as a sort of belts-and-suspenders "test" since, if the validation fails, it means the remediation failed to do its job.

This can be done simply by specifying both a `validate` and a `remediate` on the policy definition. However, this can lead to code duplication. That is sometimes unavoidably, but it is also possible to remediate and validate with a single function:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
const s3NoPublicReadPolicy: ResourceValidationPolicy = {
    name: "s3-no-public-read",
    description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
    enforcementLevel: "remediate",
    ...validateRemediateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
        if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
            // First, issue a violation (this only happens if remediation is disabled):
            reportViolation("You cannot set public-read or public-read-write on an S3 bucket.");
            // Next, modify the ACL and return the new bucket state to use instead (for when it is enabled):
            bucket.acl = "private";
            return bucket;
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
            # First, issue a violation (this only happens if remediation is disabled):
            report_violation(
                "You cannot set public-read or public-read-write on an S3 bucket.")
            # Next, modify the ACL and return the new bucket state to use instead (for when it is enabled):
            args.props["acl"] = "private"
            return args.props

s3_no_public_read = ResourceValidationPolicy(
    name="s3-no-public-read",
    description="Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
    enforcement_level=EnforcementLevel.MANDATORY,
    validate_remediate=s3_no_public_read_validator,
)
```

{{% /choosable %}}

{{< /chooser >}}

#### Dealing with Unknowns

Because resource policies run during previews before resources are actually physically created, there may be [unknown values](/docs/concepts/inputs-outputs) in the resource state. In this case, the validation and/or remediation for a policy will be skipped during preview, and a warning is emitted. The validation and/or remediation will be reapplied during the subsequent update. This is suboptimal because during an update, it will potentially fail part-way through the update, unlike the preview which stops any action from taking place. That said, at least the policy will be run before the final state for a resource in violation of policy is used.

#### Dealing with Secrets

In the context of a policy's execution, all [secrets](/docs/concepts/secrets) will be seen as plaintext. As such, you should only ever run policy packs that you trust!

Policy remediations go to great lengths to preserve input secretness. Any resource property that was secret when passed to a remediation will remain secret after the remediation runs, even if its value has been replaced.

It is also possible to explicitly mark new things as secret using the `Secret` class in the Policy SDK. For example:

{{< chooser language "typescript,python" >}}

{{% choosable language typescript %}}

```typescript
import {
    remediateResourceOfType,
    ResourceValidationPolicy,
    Secret,
} from "@pulumi/policy";

const rdsDefaultPassword: ResourceValidationPolicy = {
    name: "rds-has-default-password",
    description: "Ensures RDS instances have a default, secure password.",
    enforcementLevel: "remediate",
    remediateResource: remediateResourceOfType(aws.rds.Instance, (db, args) => {
        if (!db.password) {
            db.password = new Secret("<lookup from secure source>");
            return db;
        }
    }),
};
```

{{% /choosable %}}
{{% choosable language python %}}

```python
from pulumi_policy import ResourceValidationPolicy, Secret

def rds_default_password_remediator(args: ResourceValidationArgs):
    if args.resource_type == "aws:rds/instance:Instance" and
            "password" not in args.props:
        args.props["password"] = Secret("<lookup from secure source>")
        return args.props

rds_default_password = ResourceValidationPolicy(
    name="rds-has-default-password",
    description="Ensures RDS instances have a default, secure password.",
    enforcement_level=EnforcementLevel.REMEDIATE,
    remediate=rds_default_password_remediator,
)
```

{{% /choosable %}}

{{< /chooser >}}

In this example, the `password` property will be encrypted using the stack's secrets manager.

### Stack Policies

Policies of `StackValidationPolicy` are run against all the resources in a stack. These policies are run after all stack resources are registered and thus *do not* block an out-of-compliance resource from being created, but do fail the preview or update. To avoid creating out-of-compliance resources, we recommend always running a preview command before an update. This allows you to write policies where one resource depends on the state or existence of another resource.

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

## Policy Groups

A *Policy Group* is a group of stacks with the same set of Policy Packs enforced. Policy Groups are only available from within the Pulumi Cloud when CrossGuard is enabled. A stack may belong to multiple Policy Groups. An example use of Policy Groups is to have a different group per environment. For example, you can have one for your stacks in production and a more permissive Policy Group for your other environments such as `staging` and `dev`.

Organization admins can create new Policy Groups, add stacks to a Policy Group, or remove stacks from a group.

Each Policy Group has its own set of enforced Policy Packs. An organization administrator can add, remove, or update the version of the Policy Pack enforced on the Policy Group.

In cases where a stack belongs to multiple Policy Groups and is therefore required to run multiple versions of the same Policy Pack, only the latest version of the Policy Pack gets enforced. For example, if `my-stack` belongs to two Policy Groups and you want to enforce `my-aws-policy-pack` versions 2 and 3, only version 3 will be enforced. You may view the Policy Groups a stack belongs to as well as the currently enforced Policy Packs for the stack by navigating to a stack’s `Settings` tab and then `Policies`.

### Default Policy Group

Every organization has a default Policy Group. When the default Policy Group is created, all stacks in your organization are automatically added to that Policy Group. Additionally, all stacks that are created after adding the default Policy Group are automatically added to it. Organization admins can remove stacks from the default Policy Group as desired.
