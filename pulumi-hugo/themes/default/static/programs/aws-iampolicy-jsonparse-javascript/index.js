"use strict";
const pulumi = require("@pulumi/pulumi");

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

// Parse the string output.
const policyWithNoStatements = pulumi.jsonParse(jsonIAMPolicy).apply(policy => {
    // Empty the policy's Statements list.
    policy.Statement = [];
    return policy;
});

// Export the modified policy.
exports.policy = policyWithNoStatements;
