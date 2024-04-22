package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		assumeRole, err := iam.GetPolicyDocument(ctx, &iam.GetPolicyDocumentArgs{
			Statements: []iam.GetPolicyDocumentStatement{
				{
					Effect: pulumi.StringRef("Allow"),
					Principals: []iam.GetPolicyDocumentStatementPrincipal{
						{
							Type: "Service",
							Identifiers: []string{
								"ec2.amazonaws.com",
							},
						},
					},
					Actions: []string{
						"sts:AssumeRole",
					},
				},
			},
		}, nil)
		if err != nil {
			return err
		}

		role, err := iam.NewRole(ctx, "my-role", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.String(assumeRole.Json),
		})
		if err != nil {
			return err
		}

		_, err = iam.NewRolePolicyAttachment(ctx, "my-rpa", &iam.RolePolicyAttachmentArgs{
			Role:      role.Name,
			PolicyArn: iam.ManagedPolicyReadOnlyAccess,
		})
		if err != nil {
			return err
		}
		return nil
	})
}
