from pulumi_policy import (
    PolicyPack,
)
import policies

# Create PolicyPack
PolicyPack(
    name="custom-policy-pack",
    policies=[
        policies.s3_product_prefix_policy, 
        policies.ec2_instance_type_restricted_policy,
        policies.all_aws_resources_must_have_tags_policy
    ]
)