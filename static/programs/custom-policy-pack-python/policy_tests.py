import unittest
from unittest.mock import Mock
import policies
from policies import (
    s3_product_prefix_policy, 
    ec2_instance_type_restricted_policy,
    all_aws_resources_must_have_tags_policy,
)
from typing import Optional

def report(message: str, urn: Optional[str] = None):
    raise AssertionError(message)

class Bucket_Prefix_Policy(unittest.TestCase):
    def test__passes_when_an_S3_bucket_has_the_correct_prefix(self):
        args = Mock(
            resource_type="aws:s3/bucketV2:BucketV2", 
            props={ "bucketPrefix": policies.REQUIRED_S3_PREFIX }
        )
        s3_product_prefix_policy.validate(args, report)

    def test__fails_when_an_S3_bucket_has_no_prefix(self):
        args = Mock(
            resource_type="aws:s3/bucketV2:BucketV2", 
            props={ "bucketPrefix": "" }
        )
        with self.assertRaises(AssertionError):
            s3_product_prefix_policy.validate(args, report)

    def test__fails_when_an_S3_bucket_has_the_wrong_prefix(self):
        args = Mock(
            resource_type="aws:s3/bucketV2:BucketV2", 
            props={ "bucketPrefix": "something-unexpected" }
        )
        with self.assertRaises(AssertionError):
            s3_product_prefix_policy.validate(args, report)

class EC2_Instance_Type_Restricted_Policy(unittest.TestCase):
    def test__passes_when_an_EC2_instance_has_the_correct_instance_type(self):
        args = Mock(
            resource_type="aws:ec2/instance:Instance", 
            props={ "instanceType": policies.REQUIRED_INSTANCE_TYPE }
        )
        ec2_instance_type_restricted_policy.validate(args, report)

    def test__fails_when_an_EC2_instance_has_no_instance_type(self):
        args = Mock(
            resource_type="aws:ec2/instance:Instance", 
            props={ "instanceType": "" }
        )
        with self.assertRaises(AssertionError):
            ec2_instance_type_restricted_policy.validate(args, report)

    def test__fails_when_an_EC2_instance_has_the_wrong_instance_type(self):
        args = Mock(
            resource_type="aws:ec2/instance:Instance", 
            props={ "instanceType": "something-unexpected" }
        )
        with self.assertRaises(AssertionError):
            ec2_instance_type_restricted_policy.validate(args, report)

class All_AWS_Resources_Must_Have_Tags_Policy(unittest.TestCase):
    def test__passes_when_AWS_resources_have_tags(self):
        args = Mock(
            resource_type="aws:ec2/instance:Instance", 
            props={ 
                "tags": {
                    "Name": "Value"
                }
            }
        )
        all_aws_resources_must_have_tags_policy.validate(args, report)

    def test__fails_when_AWS_resources_have_no_tags_property(self):
        args = Mock(
            resource_type="aws:ec2/instance:Instance", 
            props={ }
        )
        with self.assertRaises(AssertionError):
            all_aws_resources_must_have_tags_policy.validate(args, report)

    def test__fails_when_AWS_resources_have_an_empty_tags_property(self):
        args = Mock(
            resource_type="aws:ec2/instance:Instance", 
            props={ "tags": {} }
        )
        with self.assertRaises(AssertionError):
            all_aws_resources_must_have_tags_policy.validate(args, report)

    def test__passes_when_non_AWS_resources_have_no_tags(self):
        args = Mock(
            resource_type="azure-native:storage:Blob", 
            props={ }
        )
        all_aws_resources_must_have_tags_policy.validate(args, report)
