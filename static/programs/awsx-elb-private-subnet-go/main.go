package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/lb"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Create a load balancer in the default VPC listening on port 80.
		alb, err := lb.NewApplicationLoadBalancer(ctx, "lb", &lb.ApplicationLoadBalancerArgs{
			Listener: &lb.ListenerArgs{
				Port: pulumi.Int(80),
			},

			// Configure the load balancer as internal rather than internet-facing.
			Internal: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		// Export the resulting URL so that it's easy to access.
		ctx.Export("endpoint", alb.LoadBalancer.DnsName())
		return nil
	})
}
