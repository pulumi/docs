using Pulumi;
using Awsx = Pulumi.Awsx;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
   // Allocate (or get) a custom VPC.
   var vpc = new Awsx.Ec2.Vpc("vpc");

   // Create a load balancer in the default VPC listening on port 80.
   var alb = new Awsx.Lb.ApplicationLoadBalancer("lb", new()
   {
        Listener = new()
        {
            Port = 80,
        },

         // Associate the load balancer with the VPC's `public` or `private` subnet.
        SubnetIds = vpc.PublicSubnetIds,
   });

    // Export the resulting URL so that it's easy to access.
    return new Dictionary<string, object?>
    {
        ["endpoint"] = alb.LoadBalancer.Apply(lb => lb.DnsName),
    };
});
