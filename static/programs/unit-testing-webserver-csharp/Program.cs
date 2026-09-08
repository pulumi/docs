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

        // Look up the latest Amazon Linux 2 AMI.
        var ami = GetAmi.Invoke(new GetAmiInvokeArgs
        {
            Owners = { "amazon" },
            MostRecent = true,
            Filters =
            {
                new GetAmiFilterInputArgs { Name = "name", Values = { "amzn2-ami-hvm-*-x86_64-gp2" } }
            }
        });

        var server = new Instance("web-server-www", new InstanceArgs
        {
            InstanceType = "t2.micro",
            SecurityGroups = { group.Name }, // reference the group object above
            Ami = ami.Apply(ami => ami.Id),
            UserData = userData              // start a simple web server
        });
    }
}
