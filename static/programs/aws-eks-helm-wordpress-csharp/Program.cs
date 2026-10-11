using System.Collections.Generic;
using Pulumi;
using Eks = Pulumi.Eks;
using Kubernetes = Pulumi.Kubernetes;

return await Deployment.RunAsync(() =>
{
    var cluster = new Eks.Cluster("cluster");

    var eksProvider = new Kubernetes.Provider("eks-provider", new()
    {
        KubeConfig = cluster.KubeconfigJson,
    });

    var wordpress = new Kubernetes.Helm.V3.Release("wordpress", new()
    {
        RepositoryOpts = new Kubernetes.Types.Inputs.Helm.V3.RepositoryOptsArgs
        {
            Repo = "https://charts.bitnami.com/bitnami",
        },
        Chart = "wordpress",
        Values =
        {
            { "wordpressBlogName", "My Cool Kubernetes Blog!" },
        },
    }, new CustomResourceOptions
    {
        Provider = eksProvider,
    });

    return new Dictionary<string, object?>
    {
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
