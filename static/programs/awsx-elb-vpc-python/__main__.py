import pulumi
import pulumi_awsx as awsx

# Allocate (or get) a custom VPC.
vpc = awsx.ec2.Vpc("vpc");

# Create a load balancer in the default VPC listening on port 80.
alb = awsx.lb.ApplicationLoadBalancer(
    "lb",
    awsx.lb.ApplicationLoadBalancerArgs(
        listener=awsx.lb.ListenerArgs(
            port=80,
        ),

        # Associate the load balancer with the VPC's `public` or `private` subnet.
        subnet_ids=vpc.public_subnet_ids,
    ),
)

# Export the resulting URL so that it's easy to access.
pulumi.export("endpoint", alb.load_balancer.dns_name)
