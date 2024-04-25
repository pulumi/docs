import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("vpc", awsx.ec2.VpcArgs(
    subnet_specs=[
        awsx.ec2.SubnetSpecArgs(
            type=awsx.ec2.SubnetType.PUBLIC,
            cidr_mask=22,
        ),
        awsx.ec2.SubnetSpecArgs(
            type=awsx.ec2.SubnetType.PRIVATE,
            cidr_mask=20,
        ),
    ],
))

pulumi.export("vpcId", vpc.vpc_id)
