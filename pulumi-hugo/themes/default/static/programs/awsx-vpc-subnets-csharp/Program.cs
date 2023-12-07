using Pulumi;
using System.Collections.Generic;
using Pulumi.Awsx.Ec2.Inputs;
using Ec2 = Pulumi.Awsx.Ec2;

return await Deployment.RunAsync(() =>
{
    var vpc = new Ec2.Vpc("vpc", new()
    {
        SubnetSpecs =
        {
            new SubnetSpecArgs
            {
                Type = Ec2.SubnetType.Public,
                CidrMask = 22,
            },
            new SubnetSpecArgs
            {
                Type = Ec2.SubnetType.Private,
                CidrMask = 20,
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
    };
});
