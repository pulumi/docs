package main

import (
	"encoding/json"

	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		tmpJSON0, err := json.Marshal(map[string]interface{}{
			"Version": "2012-10-17",
			"Statement": []map[string]interface{}{
				map[string]interface{}{
					"Action": "sts:AssumeRole",
					"Effect": "Allow",
					"Sid":    "",
					"Principal": map[string]interface{}{
						"Service": "lambda.amazonaws.com",
					},
				},
			},
		})
		if err != nil {
			return err
		}

		json0 := string(tmpJSON0)

		_, err = iam.NewRole(ctx, "imported_role", &iam.RoleArgs{
			Name:             pulumi.String("pulumi-tutorial-iam-role"),
			AssumeRolePolicy: pulumi.String(json0),
			Description: pulumi.String("Allows Lambda functions to call AWS services on your behalf."),
		}, pulumi.Import(pulumi.ID("pulumi-tutorial-iam-role")))
		if err != nil {
			return err
		}
		return nil
	})
}
