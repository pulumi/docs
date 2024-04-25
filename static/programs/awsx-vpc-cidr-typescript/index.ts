import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with a custom CIDR block.
const vpc = new awsx.ec2.Vpc("vpc", {
    cidrBlock: "172.16.8.0/24",
});

export const vpcId = vpc.vpcId;
