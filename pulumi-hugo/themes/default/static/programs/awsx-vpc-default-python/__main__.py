import pulumi
import pulumi_awsx as awsx

# Fetch the default VPC for the current AWS region.
vpc = awsx.ec2.DefaultVpc("default-vpc")

# Export a few properties to make them easy to use.
pulumi.export("vpcId", vpc.vpc_id)
pulumi.export("publicSubnetIds", vpc.public_subnet_ids)
pulumi.export("privateSubnetIds", vpc.private_subnet_ids)
