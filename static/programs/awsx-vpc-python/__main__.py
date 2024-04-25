import pulumi
import pulumi_awsx as awsx

# Allocate a new VPC with the default settings.
vpc = awsx.ec2.Vpc("vpc")

# Export a few properties to make them easy to use.
pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
