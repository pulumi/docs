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
        // Look up the most recent Amazon Linux 2023 AMI.
        var ami = GetAmi.Invoke(new GetAmiInvokeArgs
        {
            Owners = { "amazon" },
            MostRecent = true,
            Filters =
            {
                new GetAmiFilterInputArgs { Name = "name", Values = { "al2023-ami-2023.*-x86_64" } },
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
