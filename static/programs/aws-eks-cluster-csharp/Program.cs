using System.Collections.Generic;
using Pulumi;
using Awsx = Pulumi.Awsx;
using Eks = Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    // Create a VPC for our cluster.
    var vpc = new Awsx.Ec2.Vpc("vpc");

    // Create an EKS cluster inside of the VPC.
    var cluster = new Eks.Cluster("cluster", new()
    {
        VpcId = vpc.VpcId,
        PublicSubnetIds = vpc.PublicSubnetIds,
        PrivateSubnetIds = vpc.PrivateSubnetIds,
        NodeAssociatePublicIpAddress = false,
    });

    // Export the cluster's kubeconfig.
    return new Dictionary<string, object?>
    {
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
