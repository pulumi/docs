using System.Collections.Generic;
using Pulumi;
using Eks = Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    // Create an EKS cluster with a modified configuration.
    var cluster = new Eks.Cluster("cluster", new()
    {
        DesiredCapacity = 5,
        MinSize = 3,
        MaxSize = 5,
        EnabledClusterLogTypes = new[]
        {
            "api",
            "audit",
            "authenticator",
        },
    });

    return new Dictionary<string, object?>
    {
        // Export the cluster's kubeconfig.
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
