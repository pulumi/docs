import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const config = new pulumi.Config();
const k8sNamespace = config.get("k8sNamespace") || "nginx-ingress";
const appLabels = {
    app: "nginx-ingress",
};

// Create a namespace (user supplies the name of the namespace)
const ingressNs = new kubernetes.core.v1.Namespace("ingressns", {
    metadata: {
        labels: appLabels,
        name: k8sNamespace,
    },
});

// Use Helm to install the Nginx ingress controller
const ingressController = new kubernetes.helm.v3.Release("ingresscontroller", {
    chart: "nginx-ingress",
    namespace: ingressNs.metadata.name,
    repositoryOpts: {
        repo: "https://helm.nginx.com/stable",
    },
    skipCrds: true,
    values: {
        controller: {
            enableCustomResources: false,
            appprotect: {
                enable: false,
            },
            appprotectdos: {
                enable: false,
            },
            service: {
                extraLabels: appLabels,
            },
        },
    },
    version: "0.14.1",
});

// Export some values for use elsewhere
export const name = ingressController.name;
