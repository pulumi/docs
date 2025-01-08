---
title_tag: Validate a Custom Policy Pack | Pulumi Crossguard
title: Validate a Custom Policy Pack
layout: topic
description: Validate a custom policy pack using Pulumi Crossguard.
meta_desc: Validate a custom policy pack using Pulumi Crossguard.
weight: 2
estimated_time: 5
---

---

## Test the Policy Pack

Now that you’ve created your Policy Pack, let’s see it in action. We’ll create some AWS resources that violate the policies, run the Policy Pack to check compliance, and then fix the resources to adhere to the policies.

### Step 1: Create Non-Compliant Resources

Below are examples of non-compliant resources defined in Pulumi. Save these in a file, e.g., `non_compliant_resources.py` or `non_compliant_resources.ts`, based on your language preference.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
import * as aws from "@pulumi/aws";

// S3 bucket without versioning enabled
const s3Bucket = new aws.s3.Bucket("nonCompliantBucket", {
    versioning: {
        enabled: false, // Policy violation
    },
});

// EC2 instance with a non-compliant instance type
const ec2Instance = new aws.ec2.Instance("nonCompliantInstance", {
    instanceType: "m5.large", // Policy violation
    ami: "ami-0c55b159cbfafe1f0", // Replace with a valid AMI ID
});

// Resource with no tags
const untaggedResource = new aws.s3.Bucket("untaggedBucket", {
    tags: {}, // Policy violation
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
import pulumi_aws as aws

# S3 bucket without versioning enabled
s3_bucket = aws.s3.Bucket("nonCompliantBucket",
    versioning={
        "enabled": False,  # Policy violation
    }
)

# EC2 instance with a non-compliant instance type
ec2_instance = aws.ec2.Instance("nonCompliantInstance",
    instance_type="m5.large",  # Policy violation
    ami="ami-0c55b159cbfafe1f0",  # Replace with a valid AMI ID
)

# Resource with no tags
untagged_resource = aws.s3.Bucket("untaggedBucket",
    tags={}  # Policy violation
)
```

{{% /choosable %}}

### Step 2: Run the Policy Pack

Run `pulumi up` in the directory where you defined the non-compliant resources. Pulumi will evaluate the Policy Pack against these resources and report any violations.

```bash
pulumi up
```

Example output for violations:

```plaintext
Policy violations:
- s3-versioning-enabled: S3 buckets must have versioning enabled.
- ec2-instance-type-restricted: EC2 instances must use the 't2.micro' instance type.
- all-resources-must-have-tags: All resources must have at least one tag.
```

### Step 3: Fix the Resources

Update the resources to comply with the policies.

{{< chooser language "typescript,python" />}}

{{% choosable language typescript %}}

```typescript
// S3 bucket with versioning enabled
const compliantS3Bucket = new aws.s3.Bucket("compliantBucket", {
    versioning: {
        enabled: true, // Compliant
    },
});

// EC2 instance with a compliant instance type
const compliantEc2Instance = new aws.ec2.Instance("compliantInstance", {
    instanceType: "t2.micro", // Compliant
    ami: "ami-0c55b159cbfafe1f0", // Replace with a valid AMI ID
});

// Resource with tags
const taggedResource = new aws.s3.Bucket("taggedBucket", {
    tags: {
        Environment: "Production", // Compliant
    },
});
```

{{% /choosable %}}

{{% choosable language python %}}

```python
# S3 bucket with versioning enabled
compliant_s3_bucket = aws.s3.Bucket("compliantBucket",
    versioning={
        "enabled": True,  # Compliant
    }
)

# EC2 instance with a compliant instance type
compliant_ec2_instance = aws.ec2.Instance("compliantInstance",
    instance_type="t2.micro",  # Compliant
    ami="ami-0c55b159cbfafe1f0",  # Replace with a valid AMI ID
)

# Resource with tags
tagged_resource = aws.s3.Bucket("taggedBucket",
    tags={
        "Environment": "Production",  # Compliant
    }
)
```

{{% /choosable %}}

### Step 4: Verify Compliance

Run `pulumi up` again. This time, no policy violations should be reported.

```bash
pulumi up
```

Expected output:

```plaintext
Resources:
    3 created

No policy violations found. The deployment is compliant with all policies.
```

Congratulations! You’ve successfully created and tested a Policy Pack with Pulumi CrossGuard.

## Next Steps

You have successfully created, deployed, and tested a custom policy pack. To learn more about using Pulumi CrossGuard and policies, explore the following:

- [Pulumi Crossguard: Policy as Code Documentation](https://www.pulumi.com/docs/guides/crossguard/)
- [Advanced Policy Examples](https://github.com/pulumi/examples/tree/master/policy)

If you are using *Pulumi Business Critical* edition, you can also publish this policy to your Pulumi Cloud organization, which enables server-side policy enforcement on all Pulumi projects in your organization. See [pricing](/pricing/) for more details.

{{< tutorials/stepper >}}
