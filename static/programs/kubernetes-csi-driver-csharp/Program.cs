using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Helm;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using Pulumi.Kubernetes.ApiExtensions;
using System.Collections.Generic;



return await Deployment.RunAsync(() =>
{
    var secretsStoreCsiDriver = new Release("secrets-store-csi-driver", new()
    {
        Chart = "secrets-store-csi-driver",
        Namespace = "kube-system",
        RepositoryOpts = new Pulumi.Kubernetes.Types.Inputs.Helm.V3.RepositoryOptsArgs
        {
            Repo = "https://kubernetes-sigs.github.io/secrets-store-csi-driver/charts",
        },
        Values = new Dictionary<string, object>
        {
            { "nodeSelector", new Dictionary<string, object>
            {
                { "kubernetes.io/os", "linux" },
            } },
        },
    });

    var secretsStoreCsiPulumiEscProvider = new Release("secrets-store-csi-pulumi-esc-provider", new()
    {
        Chart = "oci://ghcr.io/pulumi/helm-charts/pulumi-esc-csi-provider",
        Namespace = "kube-system",
        Values = new Dictionary<string, object>
        {
            { "nodeSelector",  new Dictionary<string, object>
            {
                { "kubernetes.io/os", "linux" },
            } },
        },
    }, new CustomResourceOptions { DependsOn = { secretsStoreCsiDriver } });

    var config = new Config();
    var pulumiPAT = config.Require("pulumi-pat");

    var mySecret = new Secret("my-secret", new SecretArgs
    {
        Metadata = new ObjectMetaArgs
        {
            Namespace = "default",
            Name = "pulumi-access-token",
        },
        StringData =
        {
            { "pulumi-access-token", pulumiPAT }
        },
        Type = "Opaque",
    }, new CustomResourceOptions { DependsOn = { secretsStoreCsiPulumiEscProvider } });

    var secretProviderClass = new Pulumi.Kubernetes.ApiExtensions.CustomResource("example-provider-pulumi-esc", new SecretProviderClassArgs
    {
        Metadata = new ObjectMetaArgs
        {
            Name = "example-provider-pulumi-esc",
            Namespace = "default",
        },
        Spec = new SecretProviderClassSpecArgs
        {
            Provider = "pulumi",
            Parameters = new InputMap<object>
            {
                { "apiUrl", "https://api.pulumi.com/api/esc" },
                { "organization", "dirien" },
                { "project", "esc-secrets-store-csi-driver-demo" },
                { "environment", "csi-secrets-store-app" },
                { "authSecretName", mySecret.Metadata.Apply(metadata => metadata.Name) },
                { "authSecretNamespace", mySecret.Metadata.Apply(metadata => metadata.Namespace) },
                { "secrets", "- secretPath: \"/\"\n  fileName: \"hello\"\n  secretKey: \"app.hello\"\n" }
            },
        },
    }, new CustomResourceOptions { DependsOn = { secretsStoreCsiPulumiEscProvider } });

    var deployment = new Pulumi.Kubernetes.Apps.V1.Deployment("example-provider-pulumi-esc", new Pulumi.Kubernetes.Types.Inputs.Apps.V1.DeploymentArgs
    {
        Metadata = new ObjectMetaArgs
        {
            Name = "example-provider-pulumi-esc",
            Namespace = "default",
            Labels =
            {
                { "app", "example-provider-pulumi-esc" },
            },
        },
        Spec = new Pulumi.Kubernetes.Types.Inputs.Apps.V1.DeploymentSpecArgs
        {
            Replicas = 1,
            Selector = new Pulumi.Kubernetes.Types.Inputs.Meta.V1.LabelSelectorArgs
            {
                MatchLabels =
                {
                    { "app", "example-provider-pulumi-esc" },
                },
            },
            Template = new Pulumi.Kubernetes.Types.Inputs.Core.V1.PodTemplateSpecArgs
            {
                Metadata = new ObjectMetaArgs
                {
                    Labels =
                    {
                        { "app", "example-provider-pulumi-esc" },
                    },
                },
                Spec = new Pulumi.Kubernetes.Types.Inputs.Core.V1.PodSpecArgs
                {
                    Containers =
                    {
                        new Pulumi.Kubernetes.Types.Inputs.Core.V1.ContainerArgs
                        {
                            Name = "client",
                            Image = "busybox:latest",
                            Command =
                            {
                                "sh",
                                "-c",
                            },
                            Args =
                            {
                                "set -eux\nls /run/secrets\nfind /run/secrets/ -mindepth 1 -maxdepth 1 -not -name '.*' | xargs -t -I {} sh -c 'echo \"$(cat \"{}\")\"'\ntail -f /dev/null",
                            },
                            VolumeMounts =
                            {
                                new Pulumi.Kubernetes.Types.Inputs.Core.V1.VolumeMountArgs
                                {
                                    Name = "data",
                                    MountPath = "/run/secrets",
                                },
                            },
                        },
                    },
                    Volumes =
                    {
                        new Pulumi.Kubernetes.Types.Inputs.Core.V1.VolumeArgs
                        {
                            Name = "data",
                            Csi = new Pulumi.Kubernetes.Types.Inputs.Core.V1.CSIVolumeSourceArgs
                            {
                                Driver = "secrets-store.csi.k8s.io",
                                ReadOnly = true,
                                VolumeAttributes =
                                {
                                    { "secretProviderClass", secretProviderClass.Metadata.Apply(metadata => metadata.Name) },
                                },
                            },
                        },
                    },
                },
            },
        },
    }, new CustomResourceOptions { DependsOn = { secretProviderClass } });

    return new Dictionary<string, object?>
    {
        { "deploymentName", deployment.Metadata.Apply(metadata => metadata.Name) },
    };
});


class SecretProviderClassArgs : CustomResourceArgs
{
    public SecretProviderClassArgs(): base("secrets-store.csi.x-k8s.io/v1", "SecretProviderClass")
    {
    }

    [Input("spec")]
    public Input<SecretProviderClassSpecArgs>? Spec { get; set; }
}


class SecretProviderClassSpecArgs : ResourceArgs
{
    [Input("provider")]
    public Input<string>? Provider { get; set; }

    [Input("parameters")]
    public Input<InputMap<object>>? Parameters { get; set; }
}

class SecretProviderParametersArgs : ResourceArgs
{
    [Input("apiUrl")]
    public Input<string>? ApiUrl { get; set; }

    [Input("organization")]
    public Input<string>? Organization { get; set; }

    [Input("project")]
    public Input<string>? Project { get; set; }

    [Input("environment")]
    public Input<string>? Environment { get; set; }

    [Input("authSecretName")]
    public Input<string>? AuthSecretName { get; set; }

    [Input("authSecretNamespace")]
    public Input<string>? AuthSecretNamespace { get; set; }

    [Input("secrets")]
    public Input<string>? Secrets { get; set; }
}