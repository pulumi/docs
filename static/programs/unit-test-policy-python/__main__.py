from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

REQUIRED_S3_PREFIX = "mycompany-"

def s3_bucket_prefix_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    """Validates that S3 buckets use the required naming prefix."""
    if args.resource_type == "aws:s3/bucket:Bucket" and "bucketPrefix" in args.props:
        actual_prefix = args.props["bucketPrefix"]
        if not actual_prefix.startswith(REQUIRED_S3_PREFIX):
            report_violation(
                f"S3 bucket must use '{REQUIRED_S3_PREFIX}' prefix. Current prefix: '{actual_prefix}'")

s3_bucket_prefix_policy = ResourceValidationPolicy(
    name="s3-bucket-prefix",
    description="Ensures S3 buckets use the required naming prefix.",
    enforcement_level=EnforcementLevel.MANDATORY,
    validate=s3_bucket_prefix_validator,
)

PolicyPack(
    name="policy-pack-python",
    policies=[
        s3_bucket_prefix_policy,
    ],
)
