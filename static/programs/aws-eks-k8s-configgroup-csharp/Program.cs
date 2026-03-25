using K8s = Pulumi.Kubernetes;
using K8sCore = Pulumi.Kubernetes.Core.V1;
using K8sYaml = Pulumi.Kubernetes.Yaml.V2;
using Newtonsoft.Json;
using Pulumi;
using Pulumi.Eks;

class MyStack : Stack
{
    public MyStack()
    {
        // Create an EKS cluster.
        var cluster = new Cluster("my-cluster");

        // Create a Kubernetes provider using the new cluster's Kubeconfig.
        var eksProvider = new K8s.Provider("eksProvider", new K8s.ProviderArgs {
            KubeConfig = cluster.Kubeconfig.Apply(JsonConvert.SerializeObject)
        });

        // Create resources from standard Kubernetes guestbook YAML.
        var guestbook = new K8sYaml.ConfigGroup("guestbook",
            new K8sYaml.ConfigGroupArgs {
                Files = new[] { "yaml/*.yaml" },
            },
            new ComponentResourceOptions { Provider = eksProvider }
        );

        // Export the (cluster-private) IP address of the Guestbook frontend.
        this.FrontendIp = guestbook.GetResource<K8sCore.Service>(
            "frontend").Apply((svc) => svc.Spec.Apply((spec) => spec.ClusterIP));
    }

    [Output]
    public Output<string> FrontendIp { get; set; }
}
