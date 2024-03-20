import * as pulumi from "@pulumi/pulumi";

const jsonIAMPolicy = pulumi.output(`{
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
}`);

const policyWithNoStatements: pulumi.Output<object> = pulumi.jsonParse(jsonIAMPolicy).apply(policy => {
    // delete the policy statements
    policy.Statement = [];
    return policy;
});

export const policy = policyWithNoStatements;
