using Pulumi;
using Awsx = Pulumi.Awsx;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
   // Create a load balancer in the default VPC listening on port 80.
   var alb = new Awsx.Lb.ApplicationLoadBalancer("lb", new()
   {
        Listener = new()
        {
            Port = 80,
        },

        // Configure the load balancer as internal rather than internet-facing.
        Internal =   true,
   });

    // Export the resulting URL so that it's easy to access.
    return new Dictionary<string, object?>
    {
        ["endpoint"] = alb.LoadBalancer.Apply(lb => lb.DnsName),
    };
});
