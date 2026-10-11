using Pulumi;
using System.Collections.Generic;
using Pulumi.Awsx.Ec2;

return await Deployment.RunAsync(() =>
{
    // Allocate a new VPC with the default settings.
    var vpc = new Vpc("vpc");

    // Export a few properties to make them easy to use.
    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
        ["vpcPrivateSubnetIds"] = vpc.PrivateSubnetIds,
        ["vpcPublicSubnetIds"] = vpc.PublicSubnetIds,
    };
});
