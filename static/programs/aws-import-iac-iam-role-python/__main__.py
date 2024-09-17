import pulumi
import pulumi_aws as aws

imported_role = aws.iam.Role("imported_role",
    name="imported_role",
    assume_role_policy=json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Action": "sts:AssumeRole",
            "Effect": "Allow",
            "Sid": "",
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