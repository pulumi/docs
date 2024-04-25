import * as awsx from "@pulumi/awsx";

// Fetch the default VPC for the current AWS region.
const vpc = new awsx.ec2.DefaultVpc("default-vpc");

// Export a few properties to make them easy to use.
export const vpcId = vpc.vpcId;
export const vpcPrivateSubnetIds = vpc.privateSubnetIds;
export const vpcPublicSubnetIds = vpc.publicSubnetIds;
