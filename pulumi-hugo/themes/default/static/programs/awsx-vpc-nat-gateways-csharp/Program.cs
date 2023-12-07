using Pulumi;
using System.Collections.Generic;
using Pulumi.Awsx.Ec2.Inputs;
using Ec2 = Pulumi.Awsx.Ec2;

return await Deployment.RunAsync(() =>
{
    var vpc = new Ec2.Vpc("vpc", new()
    {
        NatGateways = new NatGatewayConfigurationArgs
        {
            Strategy = Ec2.NatGatewayStrategy.Single,
        },
    });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
    };
});
