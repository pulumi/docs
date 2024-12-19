import * as pulumi from "@pulumi/pulumi";
import * as k8s from "@pulumi/kubernetes";

const secretsStoreCSIDriver = new k8s.helm.v4.Chart("secrets-store-csi-driver", {
    chart: "secrets-store-csi-driver",
    namespace: "kube-system",
    repositoryOpts: {
        repo: "https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts",
    },
    values: {
        nodeSelector: {
            "kubernetes.io/os": "linux",
        },
    },
});

const secretsStoreCSIPulumiESCProvider = new k8s.helm.v4.Chart(
    "secrets-store-csi-pulumi-esc-provider",
    {
        chart: "oci://ghcr.io/pulumi/helm-charts/pulumi-esc-csi-provider",
        namespace: "kube-system",
        values: {
            nodeSelector: {
                "kubernetes.io/os": "linux",
            },
        },
    },
    { dependsOn: secretsStoreCSIDriver },
);

const config = new pulumi.Config();

const mySecret = new k8s.core.v1.Secret(
    "my-secret",
    {
        metadata: {
            namespace: "default",
            name: "pulumi-access-token",
        },
        stringData: {
            "pulumi-access-token": config.require("pulumi-pat"),
        },
        type: "Opaque",
    },
    { dependsOn: secretsStoreCSIPulumiESCProvider },
);

const secretProviderClass = new k8s.apiextensions.CustomResource(
    "example-provider-pulumi-esc",
    {
        apiVersion: "secrets-store.csi.x-k8s.io/v1",
        kind: "SecretProviderClass",
        metadata: {
            name: "example-provider-pulumi-esc",
            namespace: "default",
        },
        spec: {
            provider: "pulumi",
            parameters: {
                apiUrl: "https://api.pulumi.com/api/esc",
                organization: "dirien",
                project: "esc-secrets-store-csi-driver-demo",
                environment: "csi-secrets-store-app",
                authSecretName: mySecret.metadata.name,
                authSecretNamespace: mySecret.metadata.namespace,
                secrets: `- secretPath: "/"
  fileName: "hello"
  secretKey: "app.hello"
`,
            },
        },
    },
    { dependsOn: secretsStoreCSIPulumiESCProvider },
);

const deployment = new k8s.apps.v1.Deployment("example-provider-pulumi-esc", {
    metadata: {
        name: "example-provider-pulumi-esc",
        namespace: "default",
        labels: {
            app: "example-provider-pulumi-esc",
        },
    },
    spec: {
        replicas: 1,
        selector: {
            matchLabels: {
                app: "example-provider-pulumi-esc",
            },
        },
        template: {
            metadata: {
                labels: {
                    app: "example-provider-pulumi-esc",
                },
            },
            spec: {
                containers: [
                    {
                        name: "client",
                        image: "busybox:latest",
                        command: ["sh", "-c"],
                        args: [
                            `set -eux
                            ls /run/secrets
                            find /run/secrets/ -mindepth 1 -maxdepth 1 -not -name '.*' | xargs -t -I {} sh -c 'echo "$(cat "{}")"'
                            tail -f /dev/null`,
                        ],
                        volumeMounts: [
                            {
                                name: "data",
                                mountPath: "/run/secrets",
                            },
                        ],
                    },
                ],
                volumes: [
                    {
                        name: "data",
                        csi: {
                            driver: "secrets-store.csi.k8s.io",
                            readOnly: true,
                            volumeAttributes: {
                                secretProviderClass: secretProviderClass.metadata.name,
                            },
                        },
                    },
                ],
            },
        },
    },
});

export const deploymentName = deployment.metadata.name;
