import pulumi
import pulumi_kubernetes as kubernetes

def apply_patchforce_annotation(args: pulumi.ResourceTransformArgs):
    if not args.type_ == "kubernetes:helm.sh/v4:Chart":
        if not "metadata" in args.props:
            args.props["metadata"] = {}
        if not "annotations" in args.props["metadata"]:
            args.props["metadata"]["annotations"] = {}
        args.props["metadata"]["annotations"]["cost-center"] = "12345"

    return pulumi.ResourceTransformResult(props=args.props, opts=args.opts)


certman = kubernetes.helm.v4.Chart(
    "cert-manager",
    namespace="cert-manager",
    chart="oci://registry-1.docker.io/bitnamicharts/cert-manager",
    version="1.3.1",
    opts=pulumi.ResourceOptions(transforms=[apply_patchforce_annotation])
)
