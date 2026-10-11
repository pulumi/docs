import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

# Create a load balancer in the default VPC.
alb = awsx.lb.ApplicationLoadBalancer(
    "lb",
    awsx.lb.ApplicationLoadBalancerArgs(
        listeners=[

            # Redirect HTTP traffic on port 8080 to port 8081.
            awsx.lb.ListenerArgs(
                port=8080,
                protocol="HTTP",
                default_actions=[
                    aws.lb.ListenerDefaultActionArgs(
                        type="redirect",
                        redirect=aws.lb.ListenerDefaultActionRedirectArgs(
                            port="8081",
                            protocol="HTTP",
                            status_code="HTTP_301",
                        ),
                    ),
                ],
            ),

            # Accept HTTP traffic on port 8081.
            awsx.lb.ListenerArgs(
                port=8081,
                protocol="HTTP",
            ),
        ],
    ),
)

# Export the resulting URL so that it's easy to access.
pulumi.export("endpoint", alb.load_balancer.dns_name)
