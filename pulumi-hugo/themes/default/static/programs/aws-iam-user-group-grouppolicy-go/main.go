package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Create our users.
		jane, err := iam.NewUser(ctx, "jane", &iam.UserArgs{
			Name: pulumi.String("jane"),
		})
		if err != nil {
			return err
		}
		mary, err := iam.NewUser(ctx, "mary", &iam.UserArgs{
			Name: pulumi.String("mary"),
		})
		if err != nil {
			return err
		}

		// Define a group and assign a policy for it.
		devs, err := iam.NewGroup(ctx, "devs", &iam.GroupArgs{
			Path: pulumi.String("/users/"),
		})
		if err != nil {
			return err
		}
		_, err = iam.NewGroupPolicy(
			ctx, "my_developer_policy", &iam.GroupPolicyArgs{
				Group: devs.ID().ToStringOutput(),
				Policy: pulumi.String(`{
					"Version": "2012-10-17",
					"Statement": [{
						"Action": [ "ec2:Describe*" ],
						"Effect": "Allow",
						"Resource": "*"
					}]
				}
				`),
			},
		)
		if err != nil {
			return err
		}

		// Finally add the users as members to this group.
		_, err = iam.NewGroupMembership(
			ctx, "dev-team", &iam.GroupMembershipArgs{
				Group: devs.ID().ToStringOutput(),
				Users: pulumi.StringArray{
					jane.ID().ToStringOutput(),
					mary.ID().ToStringOutput(),
				},
			},
		)
		if err != nil {
			return err
		}

		return nil
	})
}
