using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;
using System.Threading.Tasks;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<WebserverStack>();
}

public class WebserverStack : Stack
{
    public WebserverStack()
    {
        var group = new SecurityGroup("web-secgrp", new SecurityGroupArgs
        {
            Ingress =
            {
                new SecurityGroupIngressArgs { Protocol = "tcp", FromPort = 22, ToPort = 22, CidrBlocks = { "0.0.0.0/0" } },
                new SecurityGroupIngressArgs { Protocol = "tcp", FromPort = 80, ToPort = 80, CidrBlocks = { "0.0.0.0/0" } }
            }
        });

        var userData = "#!/bin/bash echo \"Hello, World!\" > index.html nohup python3 -m http.server 80 &";

        var server = new Instance("web-server-www", new InstanceArgs
        {
            InstanceType = "t2.micro",
            SecurityGroups = { group.Name }, // reference the group object above
            Ami = "ami-c55673a0",            // AMI for us-east-2 (Ohio)
            UserData = userData              // start a simple webserver
        });
    }
}
