import * as awsx from "@pulumi/awsx";

// Create a load balancer in the default VPC listening on port 80.
const alb = new awsx.lb.ApplicationLoadBalancer("lb", {
    listener: {
        port: 80,
    },
});

// Export the resulting URL so that it's easy to access.
export const endpoint = alb.loadBalancer.dnsName;
