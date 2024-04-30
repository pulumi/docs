using Pulumi;
using System.Collections.Generic;
using Pulumi.Awsx.Ec2;

return await Deployment.RunAsync(() =>
{
    var vpc = new Vpc("vpc", new()
    {
        NumberOfAvailabilityZones = 4,
    });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
    };
});
