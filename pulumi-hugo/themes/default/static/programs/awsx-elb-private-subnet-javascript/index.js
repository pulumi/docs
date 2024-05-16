"use strict";
const awsx = require("@pulumi/awsx");

// Create a load balancer in the default VPC listening on port 80.
const alb = new awsx.lb.ApplicationLoadBalancer("lb", {
    listener: {
        port: 80,
    },

    // Configure the load balancer as internal rather than internet-facing.
    internal: true,
});

// Export the resulting URL so that it's easy to access.
exports.endpoint = alb.loadBalancer.dnsName;
