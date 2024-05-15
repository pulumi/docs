using Pulumi;
using System.Collections.Generic;
using Pulumi.Awsx.Ec2;

return await Deployment.RunAsync(() =>
{
    // Fetch the default VPC for the current AWS region.
    var vpc = new DefaultVpc("default-vpc");

    // Export a few properties to make them easy to use.
    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
        ["vpcPrivateSubnetIds"] = vpc.PrivateSubnetIds,
        ["vpcPublicSubnetIds"] = vpc.PublicSubnetIds,
    };
});
