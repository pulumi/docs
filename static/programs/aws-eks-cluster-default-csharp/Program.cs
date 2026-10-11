using System.Collections.Generic;
using Pulumi;
using Eks = Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    // Create an EKS cluster with the default configuration.
    var cluster = new Eks.Cluster("cluster");

    return new Dictionary<string, object?>
    {
        // Export the cluster's kubeconfig.
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
