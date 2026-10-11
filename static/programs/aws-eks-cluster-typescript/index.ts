import * as pulumi from "@pulumi/pulumi";
import * as awsx from "@pulumi/awsx";
import * as eks from "@pulumi/eks";

// Create a VPC for our cluster.
const vpc = new awsx.ec2.Vpc("vpc", {});

// Create an EKS cluster inside of the VPC.
const cluster = new eks.Cluster("cluster", {
    vpcId: vpc.vpcId,
    publicSubnetIds: vpc.publicSubnetIds,
    privateSubnetIds: vpc.privateSubnetIds,
    nodeAssociatePublicIpAddress: false,
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
