package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v7/go/aws/ec2"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type infrastructure struct {
	group  *ec2.SecurityGroup
	server *ec2.Instance
}

func createInfrastructure(ctx *pulumi.Context) (*infrastructure, error) {
	group, err := ec2.NewSecurityGroup(ctx, "web-secgrp", &ec2.SecurityGroupArgs{
		Ingress: ec2.SecurityGroupIngressArray{
			ec2.SecurityGroupIngressArgs{
				Protocol:   pulumi.String("tcp"),
				FromPort:   pulumi.Int(22),
				ToPort:     pulumi.Int(22),
				CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
			},
			ec2.SecurityGroupIngressArgs{
				Protocol:   pulumi.String("tcp"),
				FromPort:   pulumi.Int(80),
				ToPort:     pulumi.Int(80),
				CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
			},
		},
	})
	if err != nil {
		return nil, err
	}

	const userData = `#!/bin/bash echo "Hello, World!" > index.html nohup python3 -m http.server 80 &`

	server, err := ec2.NewInstance(ctx, "web-server-www", &ec2.InstanceArgs{
		InstanceType:   pulumi.String("t2.micro"),
		SecurityGroups: pulumi.StringArray{group.Name}, // reference the group object above
		Ami:            pulumi.String("ami-c55673a0"),  // AMI for us-east-2 (Ohio)
		UserData:       pulumi.String(userData),        // start a simple web server
	})
	if err != nil {
		return nil, err
	}

	return &infrastructure{
		group:  group,
		server: server,
	}, nil
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		_, err := createInfrastructure(ctx)
		return err
	})
}
