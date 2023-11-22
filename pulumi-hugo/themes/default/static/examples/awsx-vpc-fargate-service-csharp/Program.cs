using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Aws = Pulumi.Aws;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() =>
{
    var vpc = new Awsx.Ec2.Vpc("vpc");

    var securityGroup = new Aws.Ec2.SecurityGroup("securityGroup", new()
    {
        VpcId = vpc.VpcId,
        Egress = new[]
        {
            new Aws.Ec2.Inputs.SecurityGroupEgressArgs
            {
                FromPort = 0,
                ToPort = 0,
                Protocol = "-1",
                CidrBlocks = new[]
                {
                    "0.0.0.0/0",
                },
                Ipv6CidrBlocks = new[]
                {
                    "::/0",
                },
            },
        },
    });

    var cluster = new Aws.Ecs.Cluster("cluster");

    var service = new Awsx.Ecs.FargateService("service", new()
    {
        Cluster = cluster.Arn,
        NetworkConfiguration = new Aws.Ecs.Inputs.ServiceNetworkConfigurationArgs
        {
            Subnets = vpc.PrivateSubnetIds,
            SecurityGroups = new[]
            {
                securityGroup.Id,
            },
        },
        DesiredCount = 2,
        TaskDefinitionArgs = new Awsx.Ecs.Inputs.FargateServiceTaskDefinitionArgs
        {
            Container = new Awsx.Ecs.Inputs.TaskDefinitionContainerDefinitionArgs
            {
                Name = "my-service",
                Image = "nginx:latest",
                Cpu = 128,
                Memory = 512,
                Essential = true,
            },
        },
    });
});
