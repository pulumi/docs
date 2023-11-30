"use strict";
const pulumi = require("@pulumi/pulumi");
const awsx = require("@pulumi/awsx");
const eks = require("@pulumi/eks");
const kubernetes = require("@pulumi/kubernetes");

const appName = "my-app";

const repository = new awsx.ecr.Repository("repository", {
    forceDelete: true,
});

const image = new awsx.ecr.Image("image", {
    repositoryUrl: repository.url,
    context: "./app",
    platform: "linux/amd64",
});

const cluster = new eks.Cluster("cluster");

const clusterProvider = new kubernetes.Provider("clusterProvider", {
    kubeconfig: cluster.kubeconfig,
    enableServerSideApply: true,
});

const deployment = new kubernetes.apps.v1.Deployment(
    "deployment",
    {
        metadata: {
            labels: {
                appClass: appName,
            },
        },
        spec: {
            replicas: 2,
            selector: {
                matchLabels: {
                    appClass: appName,
                },
            },
            template: {
                metadata: {
                    labels: {
                        appClass: appName,
                    },
                },
                spec: {
                    containers: [
                        {
                            name: appName,
                            image: image.imageUri,
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
    },
    {
        provider: clusterProvider,
    },
);

const service = new kubernetes.core.v1.Service(
    "service",
    {
        metadata: {
            labels: {
                appClass: appName,
            },
        },
        spec: {
            type: "LoadBalancer",
            selector: {
                appClass: appName,
            },
            ports: [
                {
                    port: 80,
                    targetPort: "http",
                },
            ],
        },
    },
    {
        provider: clusterProvider,
    },
);

exports.url = service.status.apply(status => status?.loadBalancer?.ingress?.[0]?.hostname);
