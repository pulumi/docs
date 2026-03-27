import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

// Create an NGINX Deployment and load balanced Service.
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
});

// Export the URL for the load balanced service.
export const url = myService.status.apply(status => status?.loadBalancer?.ingress[0]?.hostname);
