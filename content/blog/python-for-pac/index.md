---
title: "Policy as Code with Python"
date: 2020-06-16
meta_desc: "Policy as Code for Python available as a preview in the 2.0 release."
meta_image: meta.png
authors:
    - sophia-parafina
tags:
    - "Python"
    - "Policy as Code"
---

With the launch of Pulumi 2.0, we introduced the preview of Python Policy as Code. Policies written in code let you test, automate deployment, and enable version control. Python is a popular scripting language used for machine learning and artificial intelligence, data science, web development and devops. It's an ideal language for developers and operators to use in common.

<!--more-->

Devops benefits greatly from policy as code because policies can use software development practices and verify resources without deployments that are costly in time and money. Organizations can also gain significant benefits through cost savings, fine-grained control over infrastructure, efficient deployments, improved compliance, and better use of cloud provider native resources.

## How Policy as Code Works

Policies enforce specific criteria for a resource or for a set of resources (stacks). For example, a common policy is to ensure that storage is not publicly accessible over the Internet or to ensure that virtual machines must have a firewall.

Pulumi supports two types of polices:

- **ResourceValidationPolicy** validates individual resources in a stack and is run during preview.
- **StackValidationPolicy** validates the stack as a whole and runs when the stack is deployed because some resources may need to exists to validate inputs or outputs.

Policies are enforced as either

- *advisory*, which prints a warning message the resource violates the policy, or
- *mandatory*, which prevents a resource deployment if it violates the policy.

Now that we have the basics of policy as code, lets take a look at example policies written in Python.

## Examples

Policies are validation functions that validate resources in a Pulumi stack. In the examples below, we define a function that takes `ResourceValidationArgs` and `ReportViolation` as arguments. The function checks to see what type of resource and its arguments, these are used to determine of the resource violates the policy. If the resource is not compliant, the function returns the violation and because the enforcement level is *mandatory*, the resource will not be deployed.

{{< chooser cloud "aws,azure,gcp" >}}
{{% choosable cloud aws %}}

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
{{% choosable cloud azure %}}

```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

def storage_container_no_public_read_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "azure:storage/container:Container" and "containerAccessType" in args.props:
        access_type = args.props["containerAccessType"]
        if access_type == "blob" or access_type == "container":
            report_violation(
                "Azure Storage Container must not have blob or container access set. " +
                "Read more about read access here: " +
                "https://docs.microsoft.com/en-us/azure/storage/blobs/storage-manage-access-to-resources")

storage_container_no_public_read = ResourceValidationPolicy(
    name="storage-container-no-public-read",
    description="Prohibits setting the public permission on Azure Storage Blob Containers.",
    validate=storage_container_no_public_read_validator,
)

PolicyPack(
    name="azure-python",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        storage_container_no_public_read,
    ],
)
```

{{% /choosable %}}
{{% choosable cloud gcp %}}

```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

def storage_bucket_no_public_read_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "gcp:storage/bucketACL:BucketACL" and "predefinedAcl" in args.props:
        acl = args.props["predefinedAcl"]
        if acl == "public-read" or acl == "public-read-write":
            report_violation("Storage buckets acl cannot be set to public-read or public-read-write.")

storage_bucket_no_public_read = ResourceValidationPolicy(
    name="storage-bucket-no-public-read",
    description="Prohibits setting the publicRead or publicReadWrite permission on GCP Storage buckets.",
    validate=storage_bucket_no_public_read_validator,
)

PolicyPack(
    name="gcp-python",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        storage_bucket_no_public_read,
    ],
)
```

{{% /choosable %}}
{{< /chooser >}}

In the case of this Kubernetes policy example, the policy does not allow deploying a loadbalancer which would open the kubernetes cluster to the public Internet.

```python
from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

def no_public_services_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "kubernetes:core/v1:Service" and "spec" in args.props:
        spec = args.props["spec"]
        if "type" in spec and spec["type"] == "LoadBalancer":
            report_violation(
                "Kubernetes Services cannot be of type LoadBalancer, which are exposed to " +
                "anything that can reach the Kubernetes cluster. This likely including the " +
                "public Internet.")

no_public_services = ResourceValidationPolicy(
    name="no-public-services",
    description="Kubernetes Services should be cluster-private.",
    validate=no_public_services_validator,
)

PolicyPack(
    name="kubernetes-python",
    enforcement_level=EnforcementLevel.MANDATORY,
    policies=[
        no_public_services,
    ],
)
```

## Summary

Policy as Code is an important tool for building secure and efficient cloud infrastructure. Pulumi lets you efficiently test resources before deployment and entire stacks when deployed. Learn more about what you can do with Policy as Code:

- [Get Started with Policy as Code]({{< relref "/docs/get-started/crossguard">}})
- [New Policy as Code Capabilities with CrossGuard]({{< relref "/blog/crossguard-2-0" >}})
- [Automatically Enforcing AWS Resource Tagging Policies]({{< relref "/blog/automatically-enforcing-aws-resource-tagging-policies" >}})
- [Manage Any Infrastructure with Policy as Code]({{< relref "/blog/manage-infrastructure-with-pac" >}})
- [Enforcing Different Kinds of Policies for Cloud Resources]({{< relref "/blog/enforcing-different-kinds-of-policies-for-cloud-resources" >}})
- [Running AWS IAM Access Analyzer at Deployment Time]({{< relref "/blog/aws-iam-access-analyzer-and-crossguard" >}})
