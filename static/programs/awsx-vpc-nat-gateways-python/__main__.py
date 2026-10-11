import pulumi
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("vpc", awsx.ec2.VpcArgs(
    nat_gateways=awsx.ec2.NatGatewayConfigurationArgs(
        strategy=awsx.ec2.NatGatewayStrategy.SINGLE,
    ),
))

pulumi.export("vpcId", vpc.vpc_id)
