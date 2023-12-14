using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var group = new SecurityGroup("web-sg", new SecurityGroupArgs {
        Description = "Enable HTTP access",
        Ingress = {
            new SecurityGroupIngressArgs {
                Protocol = "tcp",
                FromPort = 80,
                ToPort = 80,
                CidrBlocks = { "0.0.0.0/0" }
            }
        }
    });

    var server = new Instance("web-server", new InstanceArgs {
        Ami = "ami-0319ef1a70c93d5c8",
        InstanceType = "t2.micro",
        VpcSecurityGroupIds = { group.Name }
    });

    return new Dictionary<string, object?>
    {
        ["publicIp"] = server.PublicIp,
        ["publicDns"] = server.PublicIp,
    };
});
