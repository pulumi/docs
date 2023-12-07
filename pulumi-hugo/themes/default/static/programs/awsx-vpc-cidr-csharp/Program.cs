using Pulumi;
using System.Collections.Generic;
using Pulumi.Awsx.Ec2;

return await Deployment.RunAsync(() =>
{
    // Allocate a new VPC with a custom CIDR block.
    var vpc = new Vpc("vpc", new()
    {
        CidrBlock = "172.16.8.0/24",
    });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
    };
});
