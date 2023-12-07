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
        Ingress =
        {
            new Aws.Ec2.Inputs.SecurityGroupIngressArgs
            {
                FromPort = 22,
                ToPort = 22,
                Protocol = "tcp",
                CidrBlocks =
                {
                    "203.0.113.25/32"
                },
            },
            new Aws.Ec2.Inputs.SecurityGroupIngressArgs
            {
                FromPort = 443,
                ToPort = 443,
                Protocol = "tcp",
                CidrBlocks =
                {
                    "0.0.0.0/0"
                },
            },
        },
        Egress =
        {
            new Aws.Ec2.Inputs.SecurityGroupEgressArgs
            {
                FromPort = 0,
                ToPort = 0,
                Protocol = "-1",
                CidrBlocks =
                {
                    "0.0.0.0/0",
                },
            },
        },
    });


    return new Dictionary<string, object?>
    {
        ["vpcId"] = vpc.VpcId,
    };
});
