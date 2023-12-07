"use strict";
const awsx = require("@pulumi/awsx");

// Allocate a new VPC with the default settings.
const vpc = new awsx.ec2.Vpc("vpc");

// Export a few properties to make them easy to use.
exports.vpcId = vpc.vpcId;
exports.privateSubnetIds = vpc.privateSubnetIds;
exports.publicSubnetIds = vpc.publicSubnetIds;
