import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("vpc", awsx.ec2.VpcArgs(
    number_of_availability_zones=4,
))

pulumi.export("vpcId", vpc.vpc_id)
