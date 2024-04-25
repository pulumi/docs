import * as awsx from "@pulumi/awsx";

// Allocate (or get) a custom VPC.
const vpc = new awsx.ec2.Vpc("vpc");

// Create a load balancer in the default VPC listening on port 80.
const alb = new awsx.lb.ApplicationLoadBalancer("lb", {
    listener: {
        port: 80,
    },

    // Associate the load balancer with the VPC's `public` or `private` subnet.
    subnetIds: vpc.publicSubnetIds,
});

// Export the resulting URL so that it's easy to access.
export const endpoint = alb.loadBalancer.dnsName;
