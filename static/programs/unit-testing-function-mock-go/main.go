package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type infrastructure struct {
	server *ec2.Instance
}

func createInfrastructure(ctx *pulumi.Context) (*infrastructure, error) {
	// Look up the most recent Amazon Linux 2 AMI.
	ami, err := ec2.LookupAmi(ctx, &ec2.LookupAmiArgs{
		Owners:     []string{"amazon"},
		MostRecent: pulumi.BoolRef(true),
		Filters: []ec2.GetAmiFilter{
			{
				Name:   "name",
				Values: []string{"amzn2-ami-hvm-*-x86_64-gp2"},
			},
		},
	})
	if err != nil {
		return nil, err
	}

	server, err := ec2.NewInstance(ctx, "web-server", &ec2.InstanceArgs{
		Ami:          pulumi.String(ami.Id),
		InstanceType: pulumi.String("t3.micro"),
		Tags: pulumi.StringMap{
			"Name": pulumi.String("web-server"),
		},
	})
	if err != nil {
		return nil, err
	}

	return &infrastructure{server: server}, nil
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := createInfrastructure(ctx)
		return err
	})
}
