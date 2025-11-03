import pytest
from pulumi_policy import ResourceValidationArgs

# Define the validator function directly for testing
# This is the same logic as in __main__.py
REQUIRED_S3_PREFIX = "mycompany-"

def s3_bucket_prefix_validator(args: ResourceValidationArgs, report_violation):
    """Validates that S3 buckets use the required naming prefix."""
    if args.resource_type == "aws:s3/bucket:Bucket" and "bucketPrefix" in args.props:
        actual_prefix = args.props["bucketPrefix"]
        if not actual_prefix.startswith(REQUIRED_S3_PREFIX):
            report_violation(
                f"S3 bucket must use '{REQUIRED_S3_PREFIX}' prefix. Current prefix: '{actual_prefix}'")

def test_bucket_with_correct_prefix():
    """Test that policy passes when bucket has correct prefix."""
    args = ResourceValidationArgs(
        resource_type="aws:s3/bucket:Bucket",
        props={"bucketPrefix": "mycompany-data"},
        urn="urn:pulumi:dev::test::aws:s3/bucket:Bucket::my-bucket",
        name="my-bucket",
        opts={},
        provider="",
    )

    # Should not raise any violations
    violations = []
    def report_violation(message: str):
        violations.append(message)

    s3_bucket_prefix_validator(args, report_violation)
    assert len(violations) == 0

def test_bucket_with_wrong_prefix():
    """Test that policy fails when bucket has wrong prefix."""
    args = ResourceValidationArgs(
        resource_type="aws:s3/bucket:Bucket",
        props={"bucketPrefix": "wrongprefix-data"},
        urn="urn:pulumi:dev::test::aws:s3/bucket:Bucket::my-bucket",
        name="my-bucket",
        opts={},
        provider="",
    )

    violations = []
    def report_violation(message: str):
        violations.append(message)

    s3_bucket_prefix_validator(args, report_violation)
    assert len(violations) == 1
    assert "mycompany-" in violations[0]

def test_bucket_with_no_prefix():
    """Test that policy fails when bucket has no prefix."""
    args = ResourceValidationArgs(
        resource_type="aws:s3/bucket:Bucket",
        props={"bucketPrefix": ""},
        urn="urn:pulumi:dev::test::aws:s3/bucket:Bucket::my-bucket",
        name="my-bucket",
        opts={},
        provider="",
    )

    violations = []
    def report_violation(message: str):
        violations.append(message)

    s3_bucket_prefix_validator(args, report_violation)
    assert len(violations) == 1
