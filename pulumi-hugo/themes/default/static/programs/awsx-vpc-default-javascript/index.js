"use strict";
const awsx = require("@pulumi/awsx");

// Fetch the default VPC for the current AWS region.
const vpc = new awsx.ec2.DefaultVpc("default-vpc");

// Export a few properties to make them easy to use.
exports.vpcId = vpc.vpcId;
exports.vpcPrivateSubnetIds = vpc.privateSubnetIds;
exports.vpcPublicSubnetIds = vpc.publicSubnetIds;
