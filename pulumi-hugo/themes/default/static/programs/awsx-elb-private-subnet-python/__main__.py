import pulumi
import pulumi_awsx as awsx

# Create a load balancer in the default VPC listening on port 80.
alb = awsx.lb.ApplicationLoadBalancer(
    "lb",
    awsx.lb.ApplicationLoadBalancerArgs(
        listener=awsx.lb.ListenerArgs(
            port=80,
        ),

        # Configure the load balancer as internal rather than internet-facing.
        internal=True,
    ),
)

# Export the resulting URL so that it's easy to access.
pulumi.export("endpoint", alb.load_balancer.dns_name)
