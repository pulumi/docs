import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks

# Create a VPC for the Kubernetes cluster.
eks_vpc = awsx.ec2.Vpc("eks-vpc", enable_dns_hostnames=True, cidr_block="10.0.0.0/16")

# Create the EKS cluster itself.
eks_cluster = eks.Cluster(
    "eks-cluster",
    vpc_id=eks_vpc.vpc_id,
    public_subnet_ids=eks_vpc.public_subnet_ids,
    private_subnet_ids=eks_vpc.private_subnet_ids,
    instance_type="t3.medium",
    desired_capacity=3,
    min_size=3,
    max_size=6,
)

# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", eks_cluster.kubeconfig)
