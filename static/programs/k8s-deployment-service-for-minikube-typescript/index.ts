import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

const appName = "nginx";
const appLabels = { app: appName };
const deployment = new k8s.apps.v1.Deployment(appName, {
    spec: {
        selector: { matchLabels: appLabels },
        replicas: 1,
        template: {
            metadata: { labels: appLabels },
            spec: { containers: [{ name: appName, image: "nginx" }] },
        },
    },
});

const frontend = new k8s.core.v1.Service(appName, {
    metadata: { labels: appLabels },
    spec: {
        type: "ClusterIP",
        ports: [{ port: 80, targetPort: 80, protocol: "TCP" }],
        selector: appLabels,
    },
});
