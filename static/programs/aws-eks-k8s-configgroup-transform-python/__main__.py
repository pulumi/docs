import pulumi
import pulumi_eks as eks
from pulumi_kubernetes.yaml.v2 import ConfigGroup

# Create an EKS cluster.
cluster = eks.Cluster("my-cluster")
eks_provider = cluster.provider
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
        provider=cluster.provider,
        transforms=[xform],
    )
)
