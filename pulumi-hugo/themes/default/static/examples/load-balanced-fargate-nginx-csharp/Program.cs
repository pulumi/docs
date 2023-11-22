using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() =>
{
    var repo = new Awsx.Ecr.Repository("repo", new()
    {
        ForceDelete = true,
    });

    var lb = new Awsx.Lb.ApplicationLoadBalancer("lb");
    var cluster = new Aws.Ecs.Cluster("cluster");

    var service = new Awsx.Ecs.FargateService("service", new()
    {
        Cluster = cluster.Arn,
        AssignPublicIp = true,
        TaskDefinitionArgs = new Awsx.Ecs.Inputs.FargateServiceTaskDefinitionArgs
        {
            Container = new Awsx.Ecs.Inputs.TaskDefinitionContainerDefinitionArgs
            {
                Name = "my-service",
                Image = "nginx:latest",
                Cpu = 128,
                Memory = 512,
                Essential = true,
                PortMappings = new()
                {
                    new Awsx.Ecs.Inputs.TaskDefinitionPortMappingArgs
                    {
                        ContainerPort = 80,
                        TargetGroup = lb.DefaultTargetGroup,
                    },
                },
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["url"] = lb.LoadBalancer.Apply(loadBalancer => Output.Format($"http://{loadBalancer.DnsName}")),
    };
});
