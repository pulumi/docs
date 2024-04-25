using Pulumi;
using System.Collections.Generic;
using Aws = Pulumi.Aws;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() =>
{
    var vpc = new Awsx.Ec2.Vpc("vpc");

    var securityGroup = new Aws.Ec2.SecurityGroup("group", new Aws.Ec2.SecurityGroupArgs
    {
        VpcId = vpc.VpcId,
    });

    var ami = Aws.Ec2.GetAmi.Invoke(new()
    {
        Filters = new[]
        {
            new Aws.Ec2.Inputs.GetAmiFilterInputArgs
            {
                Name = "name",
                Values = new[] { "amzn2-ami-hvm-*" },
            },
        },
        Owners = new[] { "amazon" },
        MostRecent = true,
    });

    var instance = new Aws.Ec2.Instance("instance", new Aws.Ec2.InstanceArgs
    {
        Ami = ami.Apply(ami => ami.Id),
        InstanceType = "t2.micro",
        VpcSecurityGroupIds =
        {
            securityGroup.Id,
        },
        SubnetId = vpc.PublicSubnetIds.Apply(ids => ids[0]),
    });

    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
    };
});
