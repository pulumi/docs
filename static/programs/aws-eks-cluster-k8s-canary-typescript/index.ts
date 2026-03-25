import * as pulumi from "@pulumi/pulumi";
import * as eks from "@pulumi/eks";
import * as kubernetes from "@pulumi/kubernetes";

// Create an EKS cluster with the default configuration.
const cluster = new eks.Cluster("cluster", {});
const eksProvider = new kubernetes.Provider("eks-provider", { kubeconfig: cluster.kubeconfigJson });

// Deploy a small canary service (NGINX), to test that the cluster is working.
const myDeployment = new kubernetes.apps.v1.Deployment("my-deployment", {
    metadata: {
        labels: {
            appClass: "my-deployment",
        },
    },
    spec: {
        replicas: 2,
        selector: {
            matchLabels: {
                appClass: "my-deployment",
            },
        },
        template: {
            metadata: {
                labels: {
                    appClass: "my-deployment",
                },
            },
            spec: {
                containers: [
                    {
                        name: "my-deployment",
                        image: "nginx",
                        ports: [
                            {
                                name: "http",
                                containerPort: 80,
                            },
                        ],
                    },
                ],
            },
        },
    },
}, {
    provider: eksProvider,
});
const myService = new kubernetes.core.v1.Service("my-service", {
    metadata: {
        labels: {
            appClass: "my-deployment",
        },
    },
    spec: {
        type: "LoadBalancer",
        ports: [
            {
                port: 80,
                targetPort: "http",
            },
        ],
        selector: {
            appClass: "my-deployment",
        },
    },
}, {
    provider: eksProvider,
});

// Export the cluster's kubeconfig.
export const kubeconfig = cluster.kubeconfig;
// Export the URL for the load balanced service.
export const url = myService.status.apply(status => status?.loadBalancer?.ingress[0]?.hostname);
