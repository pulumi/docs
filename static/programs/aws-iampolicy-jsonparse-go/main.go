package main

import (
	"encoding/json"
	
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
		}`)

		// Parse the string output.
		policyWithNoStatements := jsonIAMPolicy.ApplyT(
			func(jsonStr string) (map[string]interface{}, error) {
				var policy map[string]interface{}
				if err := json.Unmarshal([]byte(jsonStr), &policy); err != nil {
					return nil, err
				}

				// Empty the policy's Statements list.
				policy["Statement"] = []interface{}{}
				return policy, nil
			},
		)

		// Export the modified policy.
		ctx.Export("policy", policyWithNoStatements)
		return nil
	})
}
