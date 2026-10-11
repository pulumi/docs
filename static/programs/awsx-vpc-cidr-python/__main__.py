import pulumi
import pulumi_awsx as awsx

# Allocate a new VPC with a custom CIDR block.
vpc = awsx.ec2.Vpc("vpc", awsx.ec2.VpcArgs(
    cidr_block="172.16.8.0/24",
))

pulumi.export("vpcId", vpc.vpc_id)
