"use strict";
const awsx = require("@pulumi/awsx");

const vpc = new awsx.ec2.Vpc("vpc", {
    natGateways: {
        strategy: awsx.ec2.NatGatewayStrategy.Single,
    },
});

exports.vpcId = vpc.vpcId;
