package main

import (
	"encoding/json"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		user, err := iam.NewUser(ctx, "webmaster", &iam.UserArgs{
			Path: pulumi.String("/system/"),
			Tags: pulumi.StringMap{
				"Name": pulumi.String("webmaster"),
			},
		})
		if err != nil {
			return err
		}

		_, err = iam.NewAccessKey(ctx, "webmasterKey", &iam.AccessKeyArgs{
			User: user.Name,
		})
		if err != nil {
			return err
		}

		policy, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				map[string]interface{}{
					"Action": []string{
						"ec2:Describe*",
					},
					"Effect":   "Allow",
					"Resource": "*",
				},
			},
		})
		if err != nil {
			return err
		}

		_, err = iam.NewUserPolicy(ctx, "webmasterPolicy", &iam.UserPolicyArgs{
			User:   user.Name,
			Policy: pulumi.String(string(policy)),
		})
		if err != nil {
			return err
		}

		return nil
	})
}
