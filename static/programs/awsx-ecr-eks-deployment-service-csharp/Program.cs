using System.Collections.Generic;
using Pulumi;
using Awsx = Pulumi.Awsx;
using Eks = Pulumi.Eks;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var appName = "my-app";

    var repository = new Awsx.Ecr.Repository("repository", new()
    {
        ForceDelete = true,
    });

    var image = new Awsx.Ecr.Image("image", new()
    {
        RepositoryUrl = repository.Url,
        Context = "./app",
        Platform = "linux/amd64",
    });

    var cluster = new Eks.Cluster("cluster");

    var clusterProvider = new Kubernetes.Provider("clusterProvider", new()
    {
        KubeConfig = cluster.KubeconfigJson,
        EnableServerSideApply = true,
    });

    var deployment = new Kubernetes.Apps.V1.Deployment("deployment", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", appName },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Apps.V1.DeploymentSpecArgs
        {
            Replicas = 2,
            Selector = new Kubernetes.Types.Inputs.Meta.V1.LabelSelectorArgs
            {
                MatchLabels =
                {
                    { "appClass", appName },
                },
            },
            Template = new Kubernetes.Types.Inputs.Core.V1.PodTemplateSpecArgs
            {
                Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
                {
                    Labels =
                    {
                        { "appClass", appName },
                    },
                },
                Spec = new Kubernetes.Types.Inputs.Core.V1.PodSpecArgs
                {
                    Containers = new[]
                    {
                        new Kubernetes.Types.Inputs.Core.V1.ContainerArgs
                        {
                            Name = appName,
                            Image = image.ImageUri,
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
    }, new CustomResourceOptions
    {
        Provider = clusterProvider,
    });

    var service = new Kubernetes.Core.V1.Service("service", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels =
            {
                { "appClass", appName },
            },
        },
        Spec = new Kubernetes.Types.Inputs.Core.V1.ServiceSpecArgs
        {
            Type = "LoadBalancer",
            Selector =
            {
                { "appClass", appName },
            },
            Ports = new[]
            {
                new Kubernetes.Types.Inputs.Core.V1.ServicePortArgs
                {
                    Port = 80,
                    TargetPort = "http",
                },
            },
        },
    }, new CustomResourceOptions
    {
        Provider = clusterProvider,
    });

    var hostname = service.Status.Apply(status => status.LoadBalancer.Ingress[0].Hostname);

    return new Dictionary<string, object?>
    {
        ["url"] = Output.Format($"http://{hostname}"),
    };
});
