import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes
from pulumi_kubernetes.yaml.v2 import ConfigGroup

# Create an EKS cluster.
cluster = eks.Cluster("my-cluster")

# Create a Kubernetes provider using the new cluster's kubeconfig.
eks_provider = kubernetes.Provider("eks-provider", kubeconfig=cluster.kubeconfig_json)

# Create resources from standard Kubernetes guestbook YAML example.
guestbook = ConfigGroup("guestbook",
    files=["yaml/*.yaml"],
    opts=pulumi.ResourceOptions(provider=eks_provider)
)

# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", cluster.kubeconfig)
