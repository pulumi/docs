"use strict";
const awsx = require("@pulumi/awsx");

// Allocate a new VPC with a custom CIDR block.
const vpc = new awsx.ec2.Vpc("vpc", {
    cidrBlock: "172.16.8.0/24",
});

exports.vpcId = vpc.vpcId;
