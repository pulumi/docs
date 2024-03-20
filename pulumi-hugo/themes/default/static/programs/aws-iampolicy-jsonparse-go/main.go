package main

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		jsonIAMPolicy := pulumi.ToOutput(`{
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
		}`).(pulumi.StringInput)

		policyWithNoStatements := pulumi.JSONUnmarshal(jsonIAMPolicy).ApplyT(
			func(v interface{}) (interface{}, error) {

				// delete the policy statements
				v.(map[string]interface{})["Statement"] = []pulumi.ArrayOutput{}
				return v, nil
			})

		ctx.Export("policy", policyWithNoStatements)
		return nil
	})
}
