using System.Threading.Tasks;
using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Ec2.Inputs;

class Program
{
    static Task<int> Main() => Deployment.RunAsync<WebserverStack>();
}

public class WebserverStack : Stack
{
    public WebserverStack()
    {
        // Look up the most recent Amazon Linux 2 AMI.
        var ami = GetAmi.Invoke(new GetAmiInvokeArgs
        {
            Owners = { "amazon" },
            MostRecent = true,
            Filters =
            {
                new GetAmiFilterInputArgs { Name = "name", Values = { "amzn2-ami-hvm-*-x86_64-gp2" } },
            },
        });

        this.Server = new Instance("web-server", new InstanceArgs
        {
            Ami = ami.Apply(ami => ami.Id),
            InstanceType = "t3.micro",
            Tags = { { "Name", "web-server" } },
        });
    }

    public Instance Server { get; private set; }
}
