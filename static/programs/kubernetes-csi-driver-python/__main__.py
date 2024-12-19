import pulumi
import pulumi_kubernetes as k8s

secrets_store_csi_driver = k8s.helm.v4.Chart(
    "secrets-store-csi-driver",
    k8s.helm.v4.ChartArgs(
        chart="secrets-store-csi-driver",
        namespace="kube-system",
        repository_opts=k8s.helm.v4.RepositoryOptsArgs(
            repo="https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts",
        ),
        values={
            "nodeSelector": {
                "kubernetes.io/os": "linux",
            },
        },
    ),
)

secrets_store_csi_pulumi_esc_provider = k8s.helm.v4.Chart(
    "secrets-store-csi-pulumi-esc-provider",
    k8s.helm.v4.ChartArgs(
        chart="oci://ghcr.io/pulumi/helm-charts/pulumi-esc-csi-provider",
        namespace="kube-system",
        values={
            "nodeSelector": {
                "kubernetes.io/os": "linux",
            },
        },
    ),
    opts=pulumi.ResourceOptions(depends_on=[secrets_store_csi_driver]),
)

config = pulumi.Config()

my_secret = k8s.core.v1.Secret(
    "my-secret",
    metadata=k8s.meta.v1.ObjectMetaArgs(
        namespace="default", name="pulumi-access-token"
    ),
    string_data={
        "pulumi-access-token": config.require("pulumi-pat"),
    },
    type="Opaque",
    opts=pulumi.ResourceOptions(depends_on=[secrets_store_csi_pulumi_esc_provider]),
)

secret_provider_class = k8s.apiextensions.CustomResource(
    "example-provider-pulumi-esc",
    api_version="secrets-store.csi.x-k8s.io/v1",
    kind="SecretProviderClass",
    metadata=k8s.meta.v1.ObjectMetaArgs(
        name="example-provider-pulumi-esc", namespace="default"
    ),
    spec={
        "provider": "pulumi",
        "parameters": {
            "apiUrl": "https://api.pulumi.com/api/esc",
            "organization": "dirien",
            "project": "esc-secrets-store-csi-driver-demo",
            "environment": "csi-secrets-store-app",
            "authSecretName": my_secret.metadata["name"],
            "authSecretNamespace": my_secret.metadata["namespace"],
            "secrets": '- secretPath: "/"\n  fileName: "hello"\n  secretKey: "app.hello"\n',
        },
    },
    opts=pulumi.ResourceOptions(depends_on=[secrets_store_csi_pulumi_esc_provider]),
)

deployment = k8s.apps.v1.Deployment(
    "example-provider-pulumi-esc",
    metadata=k8s.meta.v1.ObjectMetaArgs(
        namespace="default",
        name="example-provider-pulumi-esc",
        labels={
            "app": "example-provider-pulumi-esc",
        },
    ),
    spec=k8s.apps.v1.DeploymentSpecArgs(
        replicas=1,
        selector=k8s.meta.v1.LabelSelectorArgs(
            match_labels={
                "app": "example-provider-pulumi-esc",
            },
        ),
        template=k8s.core.v1.PodTemplateSpecArgs(
            metadata=k8s.meta.v1.ObjectMetaArgs(
                labels={
                    "app": "example-provider-pulumi-esc",
                },
            ),
            spec=k8s.core.v1.PodSpecArgs(
                containers=[
                    k8s.core.v1.ContainerArgs(
                        name="client",
                        image="busybox:latest",
                        command=["sh", "-c"],
                        args=[
                            "set -eux\nls /run/secrets\nfind /run/secrets/ -mindepth 1 -maxdepth 1 -not -name '.*' | xargs -t -I {} sh -c 'echo \"$(cat \"{}\")\"'\ntail -f /dev/null",
                        ],
                        volume_mounts=[
                            k8s.core.v1.VolumeMountArgs(
                                name="data",
                                mount_path="/run/secrets",
                            ),
                        ],
                    ),
                ],
                volumes=[
                    k8s.core.v1.VolumeArgs(
                        name="data",
                        csi=k8s.core.v1.CSIVolumeSourceArgs(
                            driver="secrets-store.csi.k8s.io",
                            read_only=True,
                            volume_attributes={
                                "secretProviderClass": secret_provider_class.metadata[
                                    "name"
                                ],
                            },
                        ),
                    ),
                ],
            ),
        ),
    ),
)

pulumi.export("deploymentName", deployment.metadata["name"])
