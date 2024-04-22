package main

import (
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/ec2"
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/lb"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Allocate (or get) a custom VPC.
		vpc, err := ec2.NewVpc(ctx, "vpc", nil)
		if err != nil {
			return err
		}

		// Create a load balancer in the default VPC listening on port 80.
		alb, err := lb.NewApplicationLoadBalancer(ctx, "lb", &lb.ApplicationLoadBalancerArgs{
			Listener: &lb.ListenerArgs{
				Port: pulumi.Int(80),
			},

			// Associate the load balancer with the VPC's `public` or `private` subnet.
			SubnetIds: vpc.PrivateSubnetIds,
		})
		if err != nil {
			return err
		}

		// Export the resulting URL so that it's easy to access.
		ctx.Export("endpoint", alb.LoadBalancer.DnsName())
		return nil
	})
}
