import pulumi
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes

cluster = eks.Cluster("cluster")
eks_provider = kubernetes.Provider("eks-provider", kubeconfig=cluster.kubeconfig_json)
wordpress = kubernetes.helm.v3.Release("wordpress",
    repository_opts=kubernetes.helm.v3.RepositoryOptsArgs(
        repo="https://charts.bitnami.com/bitnami",
    ),
    chart="wordpress",
    values={
        "wordpressBlogName": "My Cool Kubernetes Blog!",
    },
    opts=pulumi.ResourceOptions(provider=eks_provider))
pulumi.export("kubeconfig", cluster.kubeconfig)
