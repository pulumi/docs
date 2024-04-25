"use strict";
const awsx = require("@pulumi/awsx");

const vpc = new awsx.ec2.Vpc("vpc", {
    numberOfAvailabilityZones: 4,
});

exports.vpcId = vpc.vpcId;
