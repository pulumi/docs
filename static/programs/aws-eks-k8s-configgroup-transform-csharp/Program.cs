using Pulumi;
using Pulumi.Eks;
using Newtonsoft.Json;
using K8s = Pulumi.Kubernetes;
using K8sYaml = Pulumi.Kubernetes.Yaml.V2;

return await Deployment.RunAsync(() =>
{
    // Create an EKS cluster.
    var cluster = new Cluster("my-cluster");

    // Create a Kubernetes provider using the new cluster's Kubeconfig.
    var eksProvider = new K8s.Provider("eksProvider", new K8s.ProviderArgs
    {
        KubeConfig = cluster.Kubeconfig.Apply(JsonConvert.SerializeObject),
    });

    var guestbook = new K8sYaml.ConfigGroup("guestbook", new()
    {
        Files = new[] { "yaml/*.yaml" },
    }, new ComponentResourceOptions
    {
        Provider = eksProvider,
        ResourceTransformations =
        {
            (args) =>
            {
                // Make every service private to the cluster.
                if (args.Resource.GetResourceType() == "kubernetes:core/v1:Service")
                {
                    dynamic dynArgs = args.Args;
                    dynArgs.Spec = new K8s.Types.Inputs.Core.V1.ServiceSpecArgs
                    {
                        Type = "ClusterIP",
                    };
                }
                return new ResourceTransformationResult(args.Args, args.Options);
            },
        },
    });
});
