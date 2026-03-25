using System.Collections.Immutable;
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

        var namespaceName = "guestbook";

        var guestbook = new K8sYaml.ConfigGroup("guestbook",
            new K8sYaml.ConfigGroupArgs {
                Files = new[] { "yaml/*.yaml" },
            },
            new ComponentResourceOptions {
                Provider = eksProvider,
                ResourceTransformations = {
                    (args) => {
                        var props = args.Args as ImmutableDictionary<string, object>
                            ?? ImmutableDictionary<string, object>.Empty;
                        // Make every service private to the cluster.
                        if (args.Resource.GetResourceType() == "kubernetes:core/v1:Service") {
                            var spec = props.GetValueOrDefault("spec")
                                as ImmutableDictionary<string, object>
                                ?? ImmutableDictionary<string, object>.Empty;
                            if (spec.TryGetValue("type", out var t) && (string)t == "LoadBalancer") {
                                props = props.SetItem("spec", spec.SetItem("type", "ClusterIP"));
                            }
                        }
                        // Put every resource in the created namespace.
                        var meta = props.GetValueOrDefault("metadata")
                            as ImmutableDictionary<string, object>
                            ?? ImmutableDictionary<string, object>.Empty;
                        props = props.SetItem("metadata", meta.SetItem("namespace", namespaceName));
                        return new ResourceTransformationResult(props, args.Options);
                    },
                }
            }
        );
    }
}
