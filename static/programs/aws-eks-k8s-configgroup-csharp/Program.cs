using System.Collections.Generic;
using K8s = Pulumi.Kubernetes;
using K8sYaml = Pulumi.Kubernetes.Yaml.V2;
using Newtonsoft.Json;
using Pulumi;
using Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    // Create an EKS cluster.
    var cluster = new Cluster("my-cluster");

    // Create a Kubernetes provider using the new cluster's Kubeconfig.
    var eksProvider = new K8s.Provider("eksProvider", new K8s.ProviderArgs
    {
        KubeConfig = cluster.Kubeconfig.Apply(JsonConvert.SerializeObject),
    });

    // Create resources from standard Kubernetes guestbook YAML.
    var guestbook = new K8sYaml.ConfigGroup("guestbook", new()
    {
        Files = new[] { "yaml/*.yaml" },
    }, new ComponentResourceOptions { Provider = eksProvider });

    return new Dictionary<string, object?>
    {
        ["kubeconfig"] = cluster.Kubeconfig,
    };
});
