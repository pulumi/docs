using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Apps.V1;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var appName = "nginx";
    var appLabels = new InputMap<string>
    {
        { "app", appName },
    };

    var deployment = new Pulumi.Kubernetes.Apps.V1.Deployment(appName, new DeploymentArgs
    {
        Spec = new DeploymentSpecArgs
        {
            Selector = new LabelSelectorArgs
            {
                MatchLabels = appLabels,
            },
            Replicas = 1,
            Template = new PodTemplateSpecArgs
            {
                Metadata = new ObjectMetaArgs
                {
                    Labels = appLabels,
                },
                Spec = new PodSpecArgs
                {
                    Containers =
                    {
                        new ContainerArgs
                        {
                            Name = appName,
                            Image = "nginx",
                            Ports =
                            {
                                new ContainerPortArgs
                                {
                                    ContainerPortValue = 80
                                },
                            },
                        },
                    },
                },
            },
        },
    });

    var frontend = new Service(appName, new ServiceArgs
    {
        Metadata = new ObjectMetaArgs
        {
            Labels = deployment.Spec.Apply(spec =>
                spec.Template.Metadata.Labels
            ),
        },
        Spec = new ServiceSpecArgs
        {
            Type = "ClusterIP",
            Selector = appLabels,
            Ports = new ServicePortArgs
            {
                Port = 80,
                TargetPort = 80,
                Protocol = "TCP",
            },
        }
    });
});