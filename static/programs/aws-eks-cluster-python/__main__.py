import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks

# Create a VPC for our cluster.
vpc = awsx.ec2.Vpc("vpc")

# Create an EKS cluster inside of the VPC.
cluster = eks.Cluster("cluster",
    vpc_id=vpc.vpc_id,
    public_subnet_ids=vpc.public_subnet_ids,
    private_subnet_ids=vpc.private_subnet_ids,
    node_associate_public_ip_address=False)

# Export the cluster's kubeconfig.
pulumi.export("kubeconfig", cluster.kubeconfig)
