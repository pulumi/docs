"use strict";
const awsx = require("@pulumi/awsx");

const vpc = new awsx.ec2.Vpc("vpc", {
    subnetSpecs: [
        {
            type: awsx.ec2.SubnetType.Public,
            cidrMask: 22,
        },
        {
            type: awsx.ec2.SubnetType.Private,
            cidrMask: 20,
        },
    ],
});

exports.vpcId = vpc.vpcId;
