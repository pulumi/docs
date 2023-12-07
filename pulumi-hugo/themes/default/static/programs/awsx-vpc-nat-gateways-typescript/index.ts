import * as awsx from "@pulumi/awsx";

const vpc = new awsx.ec2.Vpc("vpc", {
    natGateways: {
        strategy: awsx.ec2.NatGatewayStrategy.Single,
    },
});

export const vpcId = vpc.vpcId;
