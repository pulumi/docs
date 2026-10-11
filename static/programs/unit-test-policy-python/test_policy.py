import pytest
from pulumi_policy import ResourceValidationArgs

# Define the validator function directly for testing.
# This is the same logic as in __main__.py.
def rds_storage_encryption_validator(args: ResourceValidationArgs, report_violation):
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

def test_encrypted_instance_passes():
    """Test that the policy passes when storage encryption is enabled."""
    args = ResourceValidationArgs(
        resource_type="aws:rds/instance:Instance",
        props={"storageEncrypted": True},
        urn="urn:pulumi:dev::test::aws:rds/instance:Instance::my-db",
        name="my-db",
        opts={},
        provider="",
    )

    violations = []
    def report_violation(message: str):
        violations.append(message)

    rds_storage_encryption_validator(args, report_violation)
    assert len(violations) == 0

def test_unencrypted_instance_fails():
    """Test that the policy fails when storage encryption is not enabled."""
    args = ResourceValidationArgs(
        resource_type="aws:rds/instance:Instance",
        props={"storageEncrypted": False},
        urn="urn:pulumi:dev::test::aws:rds/instance:Instance::my-db",
        name="my-db",
        opts={},
        provider="",
    )

    violations = []
    def report_violation(message: str):
        violations.append(message)

    rds_storage_encryption_validator(args, report_violation)
    assert len(violations) == 1
    assert "storage encryption" in violations[0]

def test_non_production_instance_is_exempt():
    """Test that an unencrypted instance tagged as non-production data is exempt."""
    args = ResourceValidationArgs(
        resource_type="aws:rds/instance:Instance",
        props={
            "storageEncrypted": False,
            "tags": {"data-classification": "non-production"},
        },
        urn="urn:pulumi:dev::test::aws:rds/instance:Instance::my-db",
        name="my-db",
        opts={},
        provider="",
    )

    violations = []
    def report_violation(message: str):
        violations.append(message)

    rds_storage_encryption_validator(args, report_violation)
    assert len(violations) == 0
