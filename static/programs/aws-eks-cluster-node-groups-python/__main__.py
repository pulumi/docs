import pulumi
import json
import pulumi_aws as aws
import pulumi_eks as eks

managed_policy_arns = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
]
assume_role_policy = json.dumps({
    "Version": "2012-10-17",
    "Statement": [{
        "Action": "sts:AssumeRole",
        "Effect": "Allow",
        "Principal": {
            "Service": "ec2.amazonaws.com",
        },
    }],
})
role1 = aws.iam.Role("role1",
    assume_role_policy=assume_role_policy,
    managed_policy_arns=managed_policy_arns)
role2 = aws.iam.Role("role2",
    assume_role_policy=assume_role_policy,
    managed_policy_arns=managed_policy_arns)
instance_profile1 = aws.iam.InstanceProfile("instanceProfile1", role=role1.name)
instance_profile2 = aws.iam.InstanceProfile("instanceProfile2", role=role2.name)
cluster = eks.Cluster("cluster",
    skip_default_node_group=True,
    instance_roles=[role1, role2])
fixed_node_group = eks.NodeGroupV2("fixedNodeGroup",
    cluster=cluster,
    instance_type="t2.medium",
    desired_capacity=2,
    min_size=1,
    max_size=3,
    spot_price="1",
    labels={
        "ondemand": "true",
    },
    instance_profile=instance_profile1)
spot_node_group = eks.NodeGroupV2("spotNodeGroup",
    cluster=cluster,
    instance_type="t2.medium",
    desired_capacity=1,
    min_size=1,
    max_size=2,
    labels={
        "preemptible": "true",
    },
    instance_profile=instance_profile2)
pulumi.export("kubeconfig", cluster.kubeconfig)
