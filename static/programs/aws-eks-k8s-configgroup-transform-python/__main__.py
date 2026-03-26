import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes
from pulumi_kubernetes.yaml.v2 import ConfigGroup

# Create an EKS cluster.
cluster = eks.Cluster("my-cluster")

# Create a Kubernetes provider using the new cluster's kubeconfig.
eks_provider = kubernetes.Provider("eks-provider", kubeconfig=cluster.kubeconfig_json)

namespace_name = "guestbook"

def xform(args):
    props = dict(args.props)
    # Make every service private to the cluster.
    if args.type_ == "kubernetes:core/v1:Service":
        spec = dict(props.get("spec", {}))
        if spec.get("type") == "LoadBalancer":
            spec["type"] = "ClusterIP"
            props["spec"] = spec
    # Put every resource in the created namespace.
    meta = dict(props.get("metadata", {}))
    meta["namespace"] = namespace_name
    props["metadata"] = meta
    return pulumi.ResourceTransformResult(props=props, opts=args.opts)

guestbook = ConfigGroup("guestbook",
    files=["yaml/*.yaml"],
    opts=pulumi.ResourceOptions(
        provider=eks_provider,
        transforms=[xform],
    )
)
