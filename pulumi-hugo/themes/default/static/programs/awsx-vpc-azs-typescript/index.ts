import * as awsx from "@pulumi/awsx";

const vpc = new awsx.ec2.Vpc("vpc", {
    numberOfAvailabilityZones: 4,
});

export const vpcId = vpc.vpcId;
