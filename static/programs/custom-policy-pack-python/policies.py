from pulumi_policy import (
    EnforcementLevel,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

# S3 Bucket Policy
REQUIRED_S3_PREFIX="myproduct-"

def s3_product_prefix(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:s3/bucketV2:BucketV2" and "bucketPrefix" in args.props:
        actualPrefix = args.props["bucketPrefix"]
        if actualPrefix != REQUIRED_S3_PREFIX:
            report_violation("Invalid prefix: '{}'. S3 buckets must use '{}' prefix.".format(actualPrefix, REQUIRED_S3_PREFIX))

s3_product_prefix_policy = ResourceValidationPolicy(
    name="s3-product-prefix",
    description="Ensures S3 buckets have the correct product prefix.",
    validate=s3_product_prefix,
    enforcement_level=EnforcementLevel.MANDATORY
)

# EC2 Instance Policy
REQUIRED_INSTANCE_TYPE="t2.micro"

def ec2_instance_type_restricted(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type == "aws:ec2/instance:Instance" and "instanceType" in args.props:
        actualInstanceType = args.props["instanceType"]
        if actualInstanceType != REQUIRED_INSTANCE_TYPE:
            report_violation("Invalid instance type: '{}'. E2 instances must use '{}' instance type.".format(actualInstanceType, REQUIRED_INSTANCE_TYPE))

ec2_instance_type_restricted_policy = ResourceValidationPolicy(
    name="ec2-instance-type-restricted",
    description="Ensures EC2 instances use approved instance type.",
    validate=ec2_instance_type_restricted,
    enforcement_level=EnforcementLevel.MANDATORY
)

# AWS Resource Tags Policy
def all_aws_resources_must_have_tags(args: ResourceValidationArgs, report_violation: ReportViolation):
    if args.resource_type.startswith("aws"):
        tags = {}
        if 'tags' in args.props:
            tags = args.props['tags']
        if len(tags) == 0:
            report_violation("All AWS resources must have at least one tag.")

all_aws_resources_must_have_tags_policy = ResourceValidationPolicy(
    name="all-aws-resources-must-have-tags",
    description="Ensures all AWS resources have at least one tag.",
    validate=all_aws_resources_must_have_tags,
    enforcement_level=EnforcementLevel.MANDATORY
)

