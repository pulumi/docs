import pulumi

json_iam_policy = pulumi.Output.from_input(
    """
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::my-bucket"
        }
    ]
}
"""
)


def update_policy(policy):
    # Empty the policy's Statements list.
    policy.update({"Statement": []})
    return policy


# Parse the string output.
policy_with_no_statements = pulumi.Output.json_loads(json_iam_policy).apply(
    lambda policy: update_policy
)

# Export the modified policy.
pulumi.export("policy", policy_with_no_statements)
