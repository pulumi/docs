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

With the launch of Pulumi 2.0, we introduced the preview of Python Policy as Code. Policies written in code let you test, automate deployment, and enable version control. Typically, policies are written using the cloud providers web base interface making it difficult to recreate the policy or version it. These policies must be tested on a deployed system, meaning that the  policy must be run against a live test environment or ephemeral environment which adds to system overhead. In contrast, Pulumi runs policies during the preview phase along with the other cloud resources you have declared. Preview validates your infrastructure before any resources are deployed.

<!--more-->

Devops benefits greatly from policy as code because policies can use standard software development practices and verify resources without deployments that are costly in time and money. Organizations can also gain significant benefits through cost savings, fine-grained control over infrastructure, efficient deployments, improved compliance, and better use of cloud provider native resources.

## How it Works

Policies enforce specific criteria for a resource or a stack (a set of resources). A common policy is to ensure that storage is not publicly accessible over the Internet or to ensure that virtual machines must have a firewall. Policies are run twice. First, during pulumi preview when the resource graph is creates; and second, during pulumi update when resources are created.

Policies are validation functions that evaluate all resources in a Pulumi stack. When a resource is in violation of a policy, the validation function calls reportViolation .

Pulumi supports two types of polices:

- **ResourceValidationPolicy** validates individual resources in a stack and is run during preview.
- **StackValidationPolicy** validates the stack as a whole and runs when the stack is deployed because some resources may need to exists to validate inputs or outputs.

Now that we have the basics of policy as code, lets take a look at example policies written in Python.

## Examples

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

Kubernetes

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

loren ipsum
