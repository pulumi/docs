using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;
using System.Collections.Generic;

return await Deployment.RunAsync(() => 
{
    // Create a VPC.
    var vpc = new Vpc("vpc", new VpcArgs
    {
        CidrBlock = "10.0.0.0/16",
    });

    // Create an internet gateway.
    var gateway = new InternetGateway("gateway", new InternetGatewayArgs
    {
        VpcId = vpc.Id,
    });

    // Create a subnet that automatically assigns new instances a public IP address.
    var subnet = new Subnet("subnet", new SubnetArgs
    {
        VpcId = vpc.Id,
        CidrBlock = "10.0.1.0/24",
        MapPublicIpOnLaunch = true,
    });

    // Create a route table.
    var routes = new RouteTable("routes", new RouteTableArgs
    {
        VpcId = vpc.Id,
        Routes = new List<RouteTableRouteArgs>
        {
            new RouteTableRouteArgs
            {
                CidrBlock = "0.0.0.0/0",
                GatewayId = gateway.Id,
            },
        },
    });

    // Associate the route table with the public subnet.
    var routeTableAssociation = new RouteTableAssociation("route-table-association", new RouteTableAssociationArgs
    {
        SubnetId = subnet.Id,
        RouteTableId = routes.Id,
    });

    // Create a security group allowing inbound access over port 80 and outbound access to anywhere.
    var securityGroup = new SecurityGroup("security-group", new SecurityGroupArgs
    {
        VpcId = vpc.Id,
        Ingress = new List<SecurityGroupIngressArgs>
        {
            new SecurityGroupIngressArgs
            {
                CidrBlocks = new List<string> { "0.0.0.0/0" },
                Protocol = "tcp",
                FromPort = 80,
                ToPort = 80,
            },
        },
        Egress = new List<SecurityGroupEgressArgs>
        {
            new SecurityGroupEgressArgs
            {
                CidrBlocks = new List<string> { "0.0.0.0/0" },
                FromPort = 0,
                ToPort = 0,
                Protocol = "-1",
            },
        },
    });

    // Find the latest Amazon Linux 2 AMI.
    var ami = Output.Create(GetAmi.InvokeAsync(new GetAmiArgs
    {
        Owners = new List<string> { "amazon" },
        MostRecent = true,
        Filters = new List<GetAmiFilterArgs>
        {
            new GetAmiFilterArgs
            {
                Name = "description",
                Values = new List<string> { "Amazon Linux 2 *" },
            },
        },
    })).Apply(ami => ami.Id);

    // Create and launch an Amazon Linux EC2 instance into the public subnet.
    var instance = new Instance("instance", new InstanceArgs
    {
        Ami = ami,
        InstanceType = "t3.nano",
        SubnetId = subnet.Id,
        VpcSecurityGroupIds = new InputList<string> { securityGroup.Id },
        UserData = @"
            #!/bin/bash
            sudo yum update -y
            sudo yum upgrade -y
            sudo amazon-linux-extras install nginx1 -y
            sudo systemctl enable nginx
            sudo systemctl start nginx;
        ",
    });

    // Export the instance's publicly accessible URL.
    return new Dictionary<string, object?>
    {
        ["instanceURL"] = Output.Format($"http://{instance.PublicIp}")
    };
});
