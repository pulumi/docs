using Pulumi;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Threading.Tasks;
using Deployment = Pulumi.Deployment;

class MyStack : Stack
{
    public MyStack()
    {
        var nginxDeployment = new Pulumi.Kubernetes.Apps.V1.Deployment("nginxDeployment", new DeploymentArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Name = "nginx-deployment",
            },
            Spec = new DeploymentSpecArgs
            {
                Replicas = 1,
                Selector = new LabelSelectorArgs
                {
                    MatchLabels =
                    {
                        { "app", "nginx" }
                    }
                },
                Template = new PodTemplateSpecArgs
                {
                    Metadata = new ObjectMetaArgs
                    {
                        Labels =
                        {
                            { "app", "nginx" }
                        }
                    },
                    Spec = new PodSpecArgs
                    {
                        Containers =
                        {
                            new ContainerArgs
                            {
                                Name = "nginx",
                                Image = "nginx:latest",
                            }
                        }
                    }
                }
            }
        });
    }
}

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
