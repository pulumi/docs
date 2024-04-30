import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";

// Allocate a new VPC with the default settings.
const vpc = new awsx.ec2.Vpc("vpc");

// Export a few properties to make them easy to use.
export const vpcId = vpc.vpcId;
export const privateSubnetIds = vpc.privateSubnetIds;
export const publicSubnetIds = vpc.publicSubnetIds;
