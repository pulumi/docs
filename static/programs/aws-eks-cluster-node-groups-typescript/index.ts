import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as eks from "@pulumi/eks";

const managedPolicyArns = [
    "arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy",
    "arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy",
    "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly",
];
const assumeRolePolicy = JSON.stringify({
    Version: "2012-10-17",
    Statement: [
        {
            Action: "sts:AssumeRole",
            Effect: "Allow",
            Principal: {
                Service: "ec2.amazonaws.com",
            },
        },
    ],
});
const role1 = new aws.iam.Role("role1", {
    assumeRolePolicy: assumeRolePolicy,
    managedPolicyArns: managedPolicyArns,
});
const role2 = new aws.iam.Role("role2", {
    assumeRolePolicy: assumeRolePolicy,
    managedPolicyArns: managedPolicyArns,
});
const instanceProfile1 = new aws.iam.InstanceProfile("instanceProfile1", { role: role1.name });
const instanceProfile2 = new aws.iam.InstanceProfile("instanceProfile2", { role: role2.name });
const cluster = new eks.Cluster("cluster", {
    skipDefaultNodeGroup: true,
    instanceRoles: [role1, role2],
});
const fixedNodeGroup = new eks.NodeGroupV2("fixedNodeGroup", {
    cluster: cluster,
    instanceType: "t2.medium",
    desiredCapacity: 2,
    minSize: 1,
    maxSize: 3,
    spotPrice: "1",
    labels: {
        ondemand: "true",
    },
    instanceProfile: instanceProfile1,
});
const spotNodeGroup = new eks.NodeGroupV2("spotNodeGroup", {
    cluster: cluster,
    instanceType: "t2.medium",
    desiredCapacity: 1,
    minSize: 1,
    maxSize: 2,
    labels: {
        preemptible: "true",
    },
    instanceProfile: instanceProfile2,
});
export const kubeconfig = cluster.kubeconfig;
