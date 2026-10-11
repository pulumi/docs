import pulumi
import pulumi_kubernetes as kubernetes

config = pulumi.Config()
k8s_namespace = config.get("k8sNamespace", "nginx-ingress")
app_labels = {
    "app": "nginx-ingress",
}

# Create a namespace (user supplies the name of the namespace)
ingress_ns = kubernetes.core.v1.Namespace(
    "ingressns",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels=app_labels,
        name=k8s_namespace,
    ),
)

# Use Helm to install the Nginx ingress controller
ingresscontroller = kubernetes.helm.v3.Release(
    "ingresscontroller",
    chart="nginx-ingress",
    namespace=ingress_ns.metadata.name,
    repository_opts={
        "repo": "https://helm.nginx.com/stable",
    },
    skip_crds=True,
    values={
        "controller": {
            "enableCustomResources": False,
            "appprotect": {
                "enable": False,
            },
            "appprotectdos": {
                "enable": False,
            },
            "service": {
                "extraLabels": app_labels,
            },
        },
    },
    version="0.14.1",
)

# Export some values for use elsewhere
pulumi.export("name", ingresscontroller.name)
