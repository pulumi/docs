import pulumi
import pulumi_eks as eks
from pulumi_kubernetes.yaml.v2 import ConfigGroup

# Create an EKS cluster.
cluster = eks.Cluster("my-cluster")

# Create resources from standard Kubernetes guestbook YAML example.
guestbook = ConfigGroup("guestbook",
    files=["yaml/*.yaml"],
    opts=pulumi.ResourceOptions(provider=cluster.provider)
)

# Export the (cluster-private) IP address of the Guestbook frontend.
pulumi.export("frontendIp",
    guestbook.get_resource("v1/Service", "frontend", "").spec.cluster_ip)
