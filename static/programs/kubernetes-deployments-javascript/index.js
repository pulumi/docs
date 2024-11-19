"use strict";
const k8s = require("@pulumi/kubernetes");

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
