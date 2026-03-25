using System.Collections.Generic;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    // Create an NGINX Deployment and load balanced Service.
    var myDeployment = new Kubernetes.Apps.V1.Deployment("my-deployment", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", "my-deployment" },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Apps.V1.DeploymentSpecArgs
        {
            Replicas = 2,
            Selector = new Kubernetes.Types.Inputs.Meta.V1.LabelSelectorArgs
            {
                MatchLabels =
                {
                    { "appClass", "my-deployment" },
                },
            },
            Template = new Kubernetes.Types.Inputs.Core.V1.PodTemplateSpecArgs
            {
                Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                {
                    Labels =
                    {
                        { "appClass", "my-deployment" },
                    },
                },
                Spec = new Kubernetes.Types.Inputs.Core.V1.PodSpecArgs
                {
                    Containers = new[]
                    {
                        new Kubernetes.Types.Inputs.Core.V1.ContainerArgs
                        {
                            Name = "my-deployment",
                            Image = "nginx",
                            Ports = new[]
                            {
                                new Kubernetes.Types.Inputs.Core.V1.ContainerPortArgs
                                {
                                    Name = "http",
                                    ContainerPortValue = 80,
                                },
                            },
                        },
                    },
                },
            },
        },
    });

    var myService = new Kubernetes.Core.V1.Service("my-service", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", "my-deployment" },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Core.V1.ServiceSpecArgs
        {
            Type = "LoadBalancer",
            Ports = new[]
            {
                new Kubernetes.Types.Inputs.Core.V1.ServicePortArgs
                {
                    Port = 80,
                    TargetPort = "http",
                },
            },
            Selector =
            {
                { "appClass", "my-deployment" },
            },
        },
    });

    // Export the URL for the load balanced service.
    return new Dictionary<string, object?>
    {
        ["url"] = myService.Status.Apply(status => status?.LoadBalancer?.Ingress[0]?.Hostname),
    };
});
