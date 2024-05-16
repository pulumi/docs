"use strict";
const awsx = require("@pulumi/awsx");

// Create a load balancer in the default VPC.
const alb = new awsx.lb.ApplicationLoadBalancer("lb", {
    listeners: [
        {
            // Redirect HTTP traffic on port 8080 to port 8081.
            port: 8080,
            protocol: "HTTP",
            defaultActions: [
                {
                    type: "redirect",
                    redirect: {
                        port: "8081",
                        protocol: "HTTP",
                        statusCode: "HTTP_301",
                    },
                },
            ],
        },
        {
            // Accept HTTP traffic on port 8081.
            port: 8081,
            protocol: "HTTP",
        },
    ],
});

// Export the resulting URL so that it's easy to access.
exports.endpoint = alb.loadBalancer.dnsName;
