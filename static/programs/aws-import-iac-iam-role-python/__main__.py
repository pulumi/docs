###############################################
# Note that in the Python SDK, the import option
# is named import_ to avoid conflicting with the 
# reserved import keyword.
###############################################
import pulumi
import pulumi_aws as aws
import json

# Resource defintion for IAM role using import resource option
imported_role = aws.iam.Role("imported_role",
    name="pulumi-tutorial-iam-role",
    description="Allows Lambda functions to call AWS services on your behalf.",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Principal": {
                "Service": "lambda.amazonaws.com",
            },
        }],
    }),
    managed_policy_arns=[
        "arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole"
    ],
    opts = pulumi.ResourceOptions(import_="pulumi-tutorial-iam-role")
)