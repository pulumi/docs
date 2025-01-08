---
title_tag: Create a Custom Policy Pack | Pulumi Crossguard
title: Create a Custom Policy Pack
layout: topic
description: Create a custom policy pack using Pulumi Crossguard.
meta_desc: Create a custom policy pack using Pulumi Crossguard.
weight: 1
estimated_time: 5
---

In this step, we'll create a policy pack to enforce the following rules for AWS resources:

1. S3 buckets must have versioning enabled.
2. EC2 instances must use the `t2.micro` instance type.
3. All resources must have at least one tag defined.

### Set up your policy pack project

First, create a new directory for your policy pack project:

```bash
mkdir custom-policy-pack
cd custom-policy-pack
```

Then, initialize your project. Choose Python or TypeScript based on your preferred language.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```bash
pulumi policy new aws-typescript
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
pulumi policy new aws-python
```

{{% /choosable %}}

This will initialize your project, creating the necessary files and module dependencies to interact with AWS resources.


### Define Policies

Policies are written in Python or TypeScript. Like Pulumi Programs, you can use the full power of your preferred language, including standard features like leveraging third-party modules, using sophisticated conditional logic and control flow, validating with unit testing frameworks, and everything else available to you as a developer.

By default the template sets up a simple policy example that prevents S3 buckets from being publically readable:

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

**File: `custom-policy-pack/index.ts`**
```typescript
import * as aws from "@pulumi/aws";
import { PolicyPack, validateResourceOfType } from "@pulumi/policy";

new PolicyPack("aws-typescript", {
    policies: [{
        name: "s3-no-public-read",
        description: "Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
        enforcementLevel: "mandatory",
        validateResource: validateResourceOfType(aws.s3.Bucket, (bucket, args, reportViolation) => {
            if (bucket.acl === "public-read" || bucket.acl === "public-read-write") {
                reportViolation(
                    "You cannot set public-read or public-read-write on an S3 bucket. " +
                    "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html");
            }
        }),
    }],
});
```

{{% /choosable %}}

{{% choosable language python %}}

**File: `custom-policy-pack/__main__.py`**
```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

def s3_no_public_read_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:s3/bucket:Bucket" and "acl" in args.props:
        acl = args.props["acl"]
        if acl == "public-read" or acl == "public-read-write":
            report_violation(
                "You cannot set public-read or public-read-write on an S3 bucket. " +
                "Read more about ACLs here: https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html")

s3_no_public_read = ResourceValidationPolicy(
    name="s3-no-public-read",
    description="Prohibits setting the publicRead or publicReadWrite permission on AWS S3 buckets.",
    validate=s3_no_public_read_validator,
)

PolicyPack(
    name="aws-python",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        s3_no_public_read,
    ],
)
```
{{% /choosable %}}

Here you can see the basic structure of a policy pack: 
- Some imports from the Pulumi Crossguard SDK
- a *function* that implements the policy
- a *policy* definition that wraps the implementation and describes the policy
- a *policy pack* definition that defines the policies to use, and at what level to enforce them

While this example is a useful policy, it's not what we need right now. Let's delete all of that code and create some new custom policies.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

Replace the contents of `index.ts` with the following:

```typescript
import { ResourceValidationPolicy, PolicyPack, ReportViolation } from "@pulumi/policy";

// Policy: Ensure S3 buckets have versioning enabled
const s3VersioningEnabled = new ResourceValidationPolicy("s3-versioning-enabled", {
    description: "Ensures S3 buckets have versioning enabled.",
    validate: (args, reportViolation: ReportViolation) => {
        if (args.type === "aws:s3/bucket:Bucket") {
            const versioning = args.props.versioning || {};
            if (!versioning.enabled) {
                reportViolation("Policy Violation: S3 buckets must have versioning enabled.");
            }
        }
    },
});

// Policy: Restrict EC2 instance types
const ec2InstanceTypeRestricted = new ResourceValidationPolicy("ec2-instance-type-restricted", {
    description: "Ensures EC2 instances use 't2.micro' instance type.",
    validate: (args, reportViolation: ReportViolation) => {
        if (args.type === "aws:ec2/instance:Instance") {
            const instanceType = args.props.instanceType || "";
            if (instanceType !== "t2.micro") {
                reportViolation("Policy Violation: EC2 instances must use the 't2.micro' instance type.");
            }
        }
    },
});

// Policy: Ensure all resources have at least one tag
const allResourcesMustHaveTags = new ResourceValidationPolicy("all-resources-must-have-tags", {
    description: "Ensures all resources have at least one tag.",
    validate: (args, reportViolation: ReportViolation) => {
        const tags = args.props.tags || {};
        if (Object.keys(tags).length === 0) {
            reportViolation("Policy Violation: All resources must have at least one tag.");
        }
    },
});

// Create and export the policy pack
new PolicyPack("custom-policy-pack", {
    enforcementLevel: "mandatory",
    policies: [
        s3VersioningEnabled,
        ec2InstanceTypeRestricted,
        allResourcesMustHaveTags,
    ],
});
```

Here we define three different policies:
- **s3-versioning-enabled**: Ensures S3 buckets have versioning enabled by checking the `versioning` property on all `aws:s3/bucket:Bucket` resources.
- **ec2-instance-type-restricted**: Restricts EC2 instance types to only use the affordable `t2.micro` type, by checking the `instanceType` property on all `aws:ec2/instance:Instance` resources.
- **all-resources-must-have-tags**: Ensure all resources have at least one tag by checking the `tags` property on all taggable resources, of all types.

Each of the policies uses the same pattern:
1. Check the *resource type* by inspecting `args.type` to filter for only the resources we want to check. 
The way Crossguard policies work, every resource in the project will be passed to every policy, so, for performance purposes, the first step should always be to check the resource type(s) to make sure its something you want to act on. 
1. Check one or more properties on the resource using `args.props`. We always check that the property exists first, and then inspect/validate the value of the property.
1. If there is a problem with the property value or some other aspect of the resource is out of compliance, we use the `reportViolation` function from the Crossguard SDK to throw an error. The error message should be a full sentence and give useful information on how to remediate the problem.

A note on strong typing: In the above example, we are not typing the The Crossguard SDK for TypeScript allows you to use strong typing by referenci

{{% notes type="tip" %}}
**Writing Testable Code**: We've structured this code to be a little bit more readable than the template example. Instead of defining everything in one big nested object, we break each policy out into its own definition and then assemble the policy pack at the end. However, this still isn't very testable code. The implementation functions are anonymous lambda functions that are defined inline when setting the `validate` property of the `ResourceValidationPolicy` wrapper. Instead, you could pull that anonymous function out and give it a name, then write unit tests against each function. We'll leave that as an exercise for the reader.
{{% /notes %}}

Finally we assemble the policies into a policy pack object, giving a name `custom-policy-pack` and setting its `enforcementLevel` to `mandatory`. 

{{% /choosable %}}

{{% choosable language python %}}

Replace the contents of `__main__.py` with the following:

```python
from pulumi_policy import ResourceValidationPolicy, PolicyPack, ReportViolation

# Policy: Ensure S3 buckets have versioning enabled
def s3_versioning_enabled(args, report_violation: ReportViolation):
    if args.resource_type == "aws:s3/bucket:Bucket":
        versioning = args.props.get("versioning", {})
        if not versioning.get("enabled"):
            report_violation("S3 buckets must have versioning enabled.")

# Policy: Restrict EC2 instance types
def ec2_instance_type_restricted(args, report_violation: ReportViolation):
    if args.resource_type == "aws:ec2/instance:Instance":
        instance_type = args.props.get("instanceType", "")
        if instance_type != "t2.micro":
            report_violation("EC2 instances must use the 't2.micro' instance type.")

# Policy: Ensure all resources have at least one tag
def all_resources_must_have_tags(args, report_violation: ReportViolation):
    tags = args.props.get("tags", {})
    if not tags:
        report_violation("All resources must have at least one tag.")

# Create and export the Policy Pack
PolicyPack(
    name="custom-policy-pack",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        ResourceValidationPolicy(
            name="s3-versioning-enabled",
            description="Ensures S3 buckets have versioning enabled.",
            validate=s3_versioning_enabled,
        ),
        ResourceValidationPolicy(
            name="ec2-instance-type-restricted",
            description="Ensures EC2 instances use 't2.micro' instance type.",
            validate=ec2_instance_type_restricted,
        ),
        ResourceValidationPolicy(
            name="all-resources-must-have-tags",
            description="Ensures all resources have at least one tag.",
            validate=all_resources_must_have_tags,
        ),
    ],
)
```

{{% /choosable %}}

Next up, we'll validate our custom policy pack by checking some cloud resources for compliance. Let's go!

{{< tutorials/stepper >}}
