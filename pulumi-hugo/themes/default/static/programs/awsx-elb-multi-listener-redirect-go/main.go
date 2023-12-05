package main

import (
	awslb "github.com/pulumi/pulumi-aws/sdk/v6/go/aws/lb"
	"github.com/pulumi/pulumi-awsx/sdk/v2/go/awsx/lb"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		// Create a load balancer in the default VPC.
		alb, err := lb.NewApplicationLoadBalancer(ctx, "lb", &lb.ApplicationLoadBalancerArgs{
			Listeners: []lb.ListenerArgs{

				// Redirect HTTP traffic on port 8080 to port 8081.
				{
					Port:     pulumi.Int(8080),
					Protocol: pulumi.String("HTTP"),
					DefaultActions: awslb.ListenerDefaultActionArray{
						awslb.ListenerDefaultActionArgs{
							Type: pulumi.String("redirect"),
							Redirect: awslb.ListenerDefaultActionRedirectArgs{
								Port:       pulumi.String("8081"),
								Protocol:   pulumi.String("HTTP"),
								StatusCode: pulumi.String("HTTP_301"),
							},
						},
					},
				},

				// Accept HTTP traffic on port 8081.
				{
					Port:     pulumi.Int(8081),
					Protocol: pulumi.String("HTTP"),
				},
			},
		})
		if err != nil {
			return err
		}

		// Export the resulting URL so that it's easy to access.
		ctx.Export("endpoint", alb.LoadBalancer.DnsName())
		return nil
	})
}
