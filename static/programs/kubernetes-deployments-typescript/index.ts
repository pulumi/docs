import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

const nginxDeployment = new k8s.apps.v1.Deployment("nginx-deployment", {
    metadata: {
        name: "nginx-deployment",
    },
    spec: {
        replicas: 1,
        selector: {
            matchLabels: {
                app: "nginx",
            },
        },
        template: {
            metadata: {
                labels: {
                    app: "nginx",
                },
            },
            spec: {
                containers: [
                    {
                        name: "nginx",
                        image: "nginx:latest",
                    },
                ],
            },
        },
    },
});

export const _ = nginxDeployment.metadata.name;

let config = new pulumi.Config();

const namespace = config.get("namespace") || "namespace";
const nginxImage = config.get("nginxImage") || "nginx:latest";
const replicas = config.getNumber("replicas") || 1;
const numberOfDeployments = config.getNumber("numberOfDeployments") || 1;

for (let i = 0; i < numberOfDeployments; i++) {
    new k8s.apps.v1.Deployment(`nginxDeployment-${i}`, {
        metadata: {
            name: `nginx-deployment-${i}`,
            namespace: namespace,
        },
        spec: {
            replicas: replicas,
            selector: {
                matchLabels: {
                    app: `nginx-${i}`,
                },
            },
            template: {
                metadata: {
                    labels: {
                        app: `nginx-${i}`,
                    },
                },
                spec: {
                    containers: [
                        {
                            name: "nginx",
                            image: nginxImage,
                        },
                    ],
                },
            },
        },
    });
}
