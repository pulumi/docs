from pulumi_policy import (
    EnforcementLevel,
    PolicyPack,
    ReportViolation,
    ResourceValidationArgs,
    ResourceValidationPolicy,
)

def rds_storage_encryption_validator(args: ResourceValidationArgs, report_violation: ReportViolation):
    """Requires RDS instances to have storage encryption enabled, unless tagged as non-production data."""
    if args.resource_type == "aws:rds/instance:Instance":
        # Exempt instances explicitly tagged as non-production data.
        tags = args.props.get("tags", {}) or {}
        if tags.get("data-classification") == "non-production":
            return
        if not args.props.get("storageEncrypted"):
            report_violation(
                "RDS instance must have storage encryption enabled "
                "(or be tagged 'data-classification=non-production').")

rds_storage_encryption_policy = ResourceValidationPolicy(
    name="rds-storage-encryption",
    description="Requires RDS instances to have storage encryption enabled, unless tagged as non-production data.",
    enforcement_level=EnforcementLevel.MANDATORY,
    validate=rds_storage_encryption_validator,
)

PolicyPack(
    name="policy-pack-python",
    policies=[
        rds_storage_encryption_policy,
    ],
)
