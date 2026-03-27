using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using Aws = Pulumi.Aws;
using Eks = Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    var managedPolicyArns = new[]
    {
        "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
        "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
        "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
    };

    var assumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
    {
        ["Version"] = "2012-10-17",
        ["Statement"] = new[]
        {
            new Dictionary<string, object?>
            {
                ["Action"] = "sts:AssumeRole",
                ["Effect"] = "Allow",
                ["Sid"] = null,
                ["Principal"] = new Dictionary<string, object?>
                {
                    ["Service"] = "ec2.amazonaws.com",
                },
            },
        },
    });

    var role1 = new Aws.Iam.Role("role1", new()
    {
        AssumeRolePolicy = assumeRolePolicy,
        ManagedPolicyArns = managedPolicyArns,
    });

    var role2 = new Aws.Iam.Role("role2", new()
    {
        AssumeRolePolicy = assumeRolePolicy,
        ManagedPolicyArns = managedPolicyArns,
    });

    var instanceProfile1 = new Aws.Iam.InstanceProfile("instanceProfile1", new()
    {
        Role = role1.Name,
    });

    var instanceProfile2 = new Aws.Iam.InstanceProfile("instanceProfile2", new()
    {
        Role = role2.Name,
    });

    var cluster = new Eks.Cluster("cluster", new()
    {
        SkipDefaultNodeGroup = true,
        InstanceRoles = new[]
        {
            role1,
            role2,
        },
    });

    var fixedNodeGroup = new Eks.NodeGroupV2("fixedNodeGroup", new()
    {
        Cluster = cluster,
        InstanceType = "t2.medium",
        DesiredCapacity = 2,
        MinSize = 1,
        MaxSize = 3,
        SpotPrice = "1",
        Labels =
        {
            { "ondemand", "true" },
        },
        InstanceProfile = instanceProfile1,
    });

    var spotNodeGroup = new Eks.NodeGroupV2("spotNodeGroup", new()
    {
        Cluster = cluster,
        InstanceType = "t2.medium",
        DesiredCapacity = 1,
        MinSize = 1,
        MaxSize = 2,
        Labels =
        {
            { "preemptible", "true" },
        },
        InstanceProfile = instanceProfile2,
    });

    return new Dictionary<string, object?>
    {
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
