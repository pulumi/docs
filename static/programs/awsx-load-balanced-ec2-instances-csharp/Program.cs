using Pulumi;
using Aws = Pulumi.Aws;
using Awsx = Pulumi.Awsx;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    // Get the default VPC for the current region.
    var vpc = new Awsx.Ec2.DefaultVpc("default-vpc");

    // Create a security group to allow traffic to and from the virtual machine.
    var securityGroup = new Aws.Ec2.SecurityGroup("web-sg", new()
    {
        VpcId = vpc.VpcId,
        Ingress = new[]
        {
            new Aws.Ec2.Inputs.SecurityGroupIngressArgs
            {
                Protocol = "tcp",
                FromPort = 80,
                ToPort = 80,
                CidrBlocks = new[]
                {
                    "0.0.0.0/0",
                },
            },
        },
        Egress = new[]
        {
            new Aws.Ec2.Inputs.SecurityGroupEgressArgs
            {
                Protocol = "-1",
                FromPort = 0,
                ToPort = 0,
                CidrBlocks = new[]
                {
                    "0.0.0.0/0"
                },
            },
        },
    });

    // Create an ALB in the default VPC listening on port 80.
    var alb = new Awsx.Lb.ApplicationLoadBalancer("lb", new()
    {
        Listener = new()
        {
            Port = 80,
        },

        SecurityGroups = new[] { securityGroup.Id },
    });

    vpc.PublicSubnetIds.Apply(subnetIds => {

        // Get the latest Amazon Linux 2 AMI.
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

        // In each VPC subnet, create an EC2 instance and attach it to the ALB.
        for (var i = 0; i < subnetIds.Length; i++)
        {
            var vm = new Aws.Ec2.Instance($"web-{i}", new()
            {
                Ami = ami.Apply(result => result.Id),
                InstanceType = "t2.micro",
                SubnetId = subnetIds[i],
                VpcSecurityGroupIds = alb.LoadBalancer.Apply(lb => lb.SecurityGroups),
                UserData = $@"
                    #!/bin/bash
                    echo ""Hello World, from Server {i + 1}!"" > index.html
                    nohup python -m SimpleHTTPServer 80 &
                ",
            });

            var attachment = new Awsx.Lb.TargetGroupAttachment($"attachment-{i}", new()
            {
                TargetGroup = alb.DefaultTargetGroup,
                Instance = vm,
            });
        }

        return subnetIds;
    });

    // Export the resulting URL so that it's easy to access.
    return new Dictionary<string, object?>
    {
        ["endpoint"] = alb.LoadBalancer.Apply(lb => lb.DnsName),
    };
});
