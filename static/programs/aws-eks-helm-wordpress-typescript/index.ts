import * as pulumi from "@pulumi/pulumi";
import * as eks from "@pulumi/eks";
import * as kubernetes from "@pulumi/kubernetes";

const cluster = new eks.Cluster("cluster", {});
const eksProvider = new kubernetes.Provider("eks-provider", { kubeconfig: cluster.kubeconfigJson });
const wordpress = new kubernetes.helm.v3.Release("wordpress", {
    repositoryOpts: {
        repo: "https://charts.bitnami.com/bitnami",
    },
    chart: "wordpress",
    values: {
        wordpressBlogName: "My Cool Kubernetes Blog!",
    },
}, {
    provider: eksProvider,
});
export const kubeconfig = cluster.kubeconfig;
