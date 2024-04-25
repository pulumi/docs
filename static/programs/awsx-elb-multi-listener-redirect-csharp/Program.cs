using Pulumi;
using Aws = Pulumi.Aws;
using Awsx = Pulumi.Awsx;
using System.Collections.Generic;
using System;

return await Deployment.RunAsync(() =>
{
   // Create a load balancer in the default VPC.
   var alb = new Awsx.Lb.ApplicationLoadBalancer("lb", new()
   {
        Listeners = {

            // Redirect HTTP traffic on port 8080 to port 8081.
            new Awsx.Lb.Inputs.ListenerArgs
            {
                Port = 8080,
                Protocol = "HTTP",
                DefaultActions = {
                    new Aws.LB.Inputs.ListenerDefaultActionArgs
                    {
                        Type = "redirect",
                        Redirect = new Aws.LB.Inputs.ListenerDefaultActionRedirectArgs
                        {
                            Port = "8081",
                            Protocol = "HTTP",
                            StatusCode = "HTTP_301",
                        },
                    }
                }
            },

            // Accept HTTP traffic on port 8081.
            new Awsx.Lb.Inputs.ListenerArgs
            {
                Port = 8081,
                Protocol = "HTTP",
            },
        },
   });

    // Export the resulting URL so that it's easy to access.
    return new Dictionary<string, object?>
    {
        ["endpoint"] = alb.LoadBalancer.Apply(lb => lb.DnsName),
    };
});
