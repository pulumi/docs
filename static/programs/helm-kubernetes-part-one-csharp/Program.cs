using System.Collections.Generic;
using Pulumi;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var config = new Config();
    var k8sNamespace = config.Get("k8sNamespace") ?? "nginx-ingress";
    var appLabels = new InputMap<string>
    {
        { "app", "nginx-ingress" },
    };

    var ingressns = new Kubernetes.Core.V1.Namespace("ingressns", new()
    {
        Metadata = new Kubernetes.Types.Inputs.Meta.V1.ObjectMetaArgs
        {
            Labels = appLabels,
            Name = k8sNamespace,
        },
    });

    var ingresscontroller = new Kubernetes.Helm.V3.Release("ingresscontroller", new()
    {
        Chart = "nginx-ingress",
        Namespace = ingressns.Metadata.Apply(m => m.Name),
        RepositoryOpts = new Kubernetes.Types.Inputs.Helm.V3.RepositoryOptsArgs
        {
            Repo = "https://helm.nginx.com/stable",
        },
        SkipCrds = true,
        Values = new Dictionary<string, object>
        {
            ["controller"] = new Dictionary<string, object>
            {
                ["enableCustomResources"] = "false",
                ["appprotect"] = new Dictionary<string, object>
                {
                    ["enable"] = "false"
                },
                ["appprotectdos"] = new Dictionary<string, object>
                {
                    ["enable"] = "false"
                },
                ["service"] = new Dictionary<string, object>
                {
                    ["extraLabels"] = appLabels
                },
            },
        },
        Version = "0.14.1",
    });

    return new Dictionary<string, object?>
    {
        ["name"] = ingresscontroller.Name,
    };
});
