import pulumi
import pulumi_eks as eks

# Create an EKS cluster with a modified configuration.
cluster = eks.Cluster("cluster",
    desired_capacity=5,
    min_size=3,
    max_size=5,
    enabled_cluster_log_types=[
        "api",
        "audit",
        "authenticator",
    ])

# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", cluster.kubeconfig)
