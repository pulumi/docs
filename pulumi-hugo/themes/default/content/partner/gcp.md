---
title: Cloud Infrastructure as Code for Google Cloud
layout: gcp
url: /gcp

hero:
    ide:
        tabs:
            - title: index.ts
              language: typescript
              code: |
                import * as pulumi from "@pulumi/pulumi";
                import * as gcp from "@pulumi/gcp";

                const bucket = new gcp.storage.Bucket("bucket", {
                    location: "US",
                });

                export const bucketName = bucket.url;

            - title: __main__.py
              language: python
              code: |
                import pulumi
                import pulumi_gcp as gcp

                bucket = gcp.storage.Bucket("static-site",
                    location="US")

                pulumi.export('bucket_name',  bucket.url)

            - title: main.go
              language: go
              code: |
                package main

                import (
                    "github.com/pulumi/pulumi-gcp/sdk/v6/go/gcp/storage"
                    "github.com/pulumi/pulumi/sdk/v2/go/pulumi"
                )

                func main() {
                    pulumi.Run(func(ctx *pulumi.Context) error {
                        bucket, err := storage.NewBucket(ctx, "my-bucket", &storage.BucketArgs{
                            Location: pulumi.String("US"),
                        })
                        if err != nil {
                            return err
                        }

                        ctx.Export("bucketName", bucket.Url)
                        return nil
                    })
                }
            - title: MyStack.cs
              language: csharp
              code: |
                using Pulumi;
                using Pulumi.Gcp.Storage;

                class MyStack : Stack
                {
                    public MyStack()
                    {
                        var bucket = new Bucket("my-bucket");

                        // Export the DNS name of the bucket
                        this.BucketName = bucket.Url;
                    }

                    [Output]
                    public Output<string> BucketName { get; set; }
                }

            - title: Pulumi.yaml
              language: yaml
              code: |
                name: gcp-bucket
                runtime: yaml
                description: A simple Pulumi program.
                resources:
                  bucket:
                    type: gcp:storage:Bucket
                    properties:
                      location: "US"
                outputs:
                  bucketName: ${bucket.url}


            - title: Main.java
              language: java
              code: |
                package com.pulumi.example.infra;

                import com.pulumi.Context;
                import com.pulumi.Exports;
                import com.pulumi.Pulumi;
                import com.pulumi.gcp.storage.Bucket;
                import com.pulumi.gcp.storage.BucketArgs;

                public class Main {

                    public static void main(String[] args) {
                        Pulumi.run(Main::stack);
                    }

                    private static Exports stack(Context ctx) {
                        var bucket = new Bucket("bucket",
                          BucketArgs.builder()
                          .location("US"
                          .build());

                        ctx.export("bucketName", bucket.url);
                        return ctx.exports();
                    }
                }

package:
  ts: |
    import * as pulumi from "@pulumi/pulumi";
    import * as cloudrun from "@pulumi/gcp-global-cloudrun";

    const conf = new pulumi.Config()
    const project = conf.require("project")

    const deployment = new cloudrun.Deployment("my-sample-deployment", {
        projectId: project,

        imageName: "gcr.io/ahmetb-public/zoneprinter",
        serviceName: "demo-service-ts"
    });

    export const ip = deployment.ipAddress;

  py: |
    import pulumi
    import pulumi_gcp_global_cloudrun as cloudrun

    config = pulumi.Config()
    project = config.require("project")

    deployment = cloudrun.Deployment("my-sample-deployment",
                                    project_id=project,
                                    image_name="gcr.io/ahmetb-public/zoneprinter",
                                    service_name="demo-service-py")

    pulumi.export('ip', deployment.ip_address)

  go: |
    package main

    import (
      "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
      "github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
      cloudrun "github.com/pulumi/pulumi-gcp-global-cloudrun/sdk/go/gcp"
    )

    func main() {
      pulumi.Run(func(ctx *pulumi.Context) error {
        c := config.New(ctx, "")
        project := c.Require("project")

        deployment, err := cloudrun.NewDeployment(ctx, "demo-deployment-go", &cloudrun.DeploymentArgs{
          ImageName:   pulumi.String("gcr.io/ahmetb-public/zoneprinter"),
          ServiceName: "demo-service-ts",
          ProjectId:   project,
        })
        if err != nil {
          return err
        }

        ctx.Export("ip", deployment.IpAddress)

        return nil
      })
    }

  csharp: |
    using Pulumi;
    using Pulumi.GcpGlobalCloudRun.Deployment;
    using Pulumi.GcpGlobalCloudRun.DeploymentArgs;

    class MyStack: Stack
    {
        public MyStack()
        {
            var config = new Config("gcp-cloud-run");
            var project = config.Require("project");

            var deployment = new Deployment("demo-deployment-csharp", new DeploymentArgs{
              ImageName = "gcr.io/ahmetb-public/zoneprinter",
              ServiceName = "demo-service-csharp",
              ProjectId = project,
            });

            this.IP = deployment.IpAddress;
        }

        [Output]
        public Output<string> IP { get; set; }
    }

  java: |
    package gcpglobalcloudrunexample;

    import com.pulumi.Context;
    import com.pulumi.Exports;
    import com.pulumi.Pulumi;
    import com.pulumi.gcpglobalcloudrun.Deployment;
    import com.pulumi.gcpglobalcloudrun.DeploymentArgs;

    public class Main {

        public static void main(String[] args) {
            Pulumi.run(Main::stack);
        }

        private static Exports stack(Context ctx) {
            var config = ctx.config();
            var project = config.require("project");

            var deployment = new Deployment("demo-deployment-java", DeploymentArgs.builder()
                    .imageName("gcr.io/ahmetb-public/zoneprinter")
                    .serviceName("demo-service-java")
                    .projectId(project)
                    .build());

            ctx.exports("ip", deployment.ipAddress);
            return ctx.exports();
        }
    }

  yaml: |
    name: gcp-cloud-run
    runtime: yaml
    description: A simple Pulumi program.
    configuration:
      project:
        type: String
        default: "project"
    resources:
      deployment:
        type: gcp-global-cloudrun:index:Deployment
        properties:
          imageName: "gcr.io/ahmetb-public/zoneprinter"
          serviceName: "demo-service-yaml"
          projectId: ${project}
    outputs:
      ip: ${deployment.ipAddress}

native:
  java: |
    package googlenative;

    import com.pulumi.Context;
    import com.pulumi.Exports;
    import com.pulumi.Pulumi;
    import com.pulumi.googlenative.storage_v1.Bucket;
    import com.pulumi.googlenative.storage_v1.BucketArgs;

    public class Main {

        public static void main(String[] args) {
            Pulumi.run(Main::stack);
        }

        private static Exports stack(Context ctx) {
            var config = ctx.config();
            var project = config.require("project");
            var bucketName = "pulumi-goog-native-bucket-cs-01";

            var bucket = new Bucket("my-bucket", BucketArgs.builder()
                    .name(bucketName)
                    .bucket(bucketName)
                    .project(project)
                    .build());

            ctx.export("bucketName", bucket.selfLink);
            return ctx.exports();
        }
    }
  yaml: |
    name: gcp-native
    runtime: yaml
    description: A simple Pulumi program.
    configuration:
      project:
        type: String
        default: "my-bucket"
    resources:
      bucket:
        type:
        properties:
          name: "pulumi-goog-native-bucket-cs-01"
          bucket: "pulumi-goog-native-bucket-cs-01"
          project: ${project}
    outputs:
      bucketName: ${bucket.selfLink}
  csharp: |
    using System.Threading.Tasks;
    using Pulumi;
    using Pulumi.GoogleNative.Storage.V1;

    class Program
    {
        static Task Main() =>
            Deployment.Run(() => {
                var config = new Config("google-native");
                var project = config.Require("project");
                var bucketName = "pulumi-goog-native-bucket-cs-01";
                // Create a Google Cloud resource (Storage Bucket)
                var bucket = new Bucket("my-bucket", new BucketArgs{
                    Name = bucketName,
                    Bucket = bucketName,
                    Project = project,
                });
            });
    }

  go: |
    package main

    import (
      storage "github.com/pulumi/pulumi-google-native/sdk/go/google/storage/v1"
      "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    )

    func main() {
      const bucketName = "pulumi-goog-native-bucket-go-01"
      pulumi.Run(func(ctx *pulumi.Context) error {
        conf := config.New(ctx, "google-native")
        project := conf.Require("project")
        // Create a Google Cloud resource (Storage Bucket)
        bucket, err := storage.NewBucket(ctx, "bucket", &storage.BucketArgs{
          Name:    pulumi.StringPtr(bucketName),
          Bucket:  pulumi.String(project),
          Project: project,
        })
        if err != nil {
          return err
        }
        // Export the bucket self-link
        ctx.Export("bucket", bucket.SelfLink)

        return nil
      })
    }
  py: |
    import pulumi
    from pulumi_google_native.storage import v1 as storage

    config = pulumi.Config()
    project = config.require('project')
    # Create a Google Cloud resource (Storage Bucket)
    bucket_name = "pulumi-goog-native-bucket-py-01"
    bucket = storage.Bucket('my-bucket', name=bucket_name, bucket=bucket_name, project=project)

    # Export the bucket self-link
    pulumi.export('bucket', bucket.self_link)
  ts: |
    import * as storage from "@pulumi/google-native/storage/v1";
    import * as pulumi from "@pulumi/pulumi";

    const config = new pulumi.Config("google-native");
    const project = config.require("project");
    const bucketName = "pulumi-goog-native-ts-01";

    // Create a Google Cloud resource (Storage Bucket)
    const bucket = new storage.Bucket("my-bucket", {
        name:bucketName,
        bucket:bucketName,
        project: project,
    });

    // Export the bucket self-link
    export const bucketName = bucket.selfLink;

gke:
  java: |
    package gcpgke;

    import com.pulumi.Context;
    import com.pulumi.Exports;
    import com.pulumi.Pulumi;
    import com.pulumi.core.Output;
    import com.pulumi.gcp.container.Cluster;
    import com.pulumi.gcp.container.ClusterArgs;
    import com.pulumi.gcp.container.ContainerFunctions;
    import com.pulumi.gcp.container.NodePool;
    import com.pulumi.gcp.container.NodePoolArgs;
    import com.pulumi.gcp.container.inputs.NodePoolManagementArgs;
    import com.pulumi.gcp.container.inputs.NodePoolNodeConfigArgs;
    import com.pulumi.gcp.container.outputs.GetEngineVersionsResult;
    import com.pulumi.kubernetes.Provider;
    import com.pulumi.kubernetes.ProviderArgs;
    import com.pulumi.kubernetes.apps_v1.Deployment;
    import com.pulumi.kubernetes.apps_v1.DeploymentArgs;
    import com.pulumi.kubernetes.apps_v1.inputs.DeploymentSpecArgs;
    import com.pulumi.kubernetes.core_v1.Namespace;
    import com.pulumi.kubernetes.core_v1.NamespaceArgs;
    import com.pulumi.kubernetes.core_v1.Service;
    import com.pulumi.kubernetes.core_v1.ServiceArgs;
    import com.pulumi.kubernetes.core_v1.enums.ServiceSpecType;
    import com.pulumi.kubernetes.core_v1.inputs.ContainerArgs;
    import com.pulumi.kubernetes.core_v1.inputs.ContainerPortArgs;
    import com.pulumi.kubernetes.core_v1.inputs.PodSpecArgs;
    import com.pulumi.kubernetes.core_v1.inputs.PodTemplateSpecArgs;
    import com.pulumi.kubernetes.core_v1.inputs.ServicePortArgs;
    import com.pulumi.kubernetes.core_v1.inputs.ServiceSpecArgs;
    import com.pulumi.kubernetes.meta_v1.inputs.LabelSelectorArgs;
    import com.pulumi.kubernetes.meta_v1.inputs.ObjectMetaArgs;
    import com.pulumi.resources.CustomResourceOptions;

    import java.text.MessageFormat;
    import java.util.Map;

    public class App {
        public static void main(String[] args) {
            Pulumi.run(App::stack);
        }

        private static Exports stack(Context ctx) {
            final String name = "helloworld";

            final var masterVersion = ctx.config().get("masterVersion").orElse(
                    ContainerFunctions.getEngineVersions()
                    .thenApply(GetEngineVersionsResult::latestMasterVersion).join()
            );

            ctx.export("masterVersion", Output.of(masterVersion));

            // Create a GKE cluster
            // We can't create a cluster with no node pool defined, but we want to only use
            // separately managed node pools. So we create the smallest possible default
            // node pool and immediately delete it.
            final var cluster = new Cluster(name,
                    ClusterArgs.builder().initialNodeCount(1)
                            .removeDefaultNodePool(true)
                            .minMasterVersion(masterVersion)
                            .build()
            );

            final var nodePool = new NodePool("primary-node-pool",
                    NodePoolArgs.builder()
                            .cluster(cluster.name())
                            .location(cluster.location())
                            .version(masterVersion)
                            .initialNodeCount(2)
                            .nodeConfig(NodePoolNodeConfigArgs.builder()
                                    .preemptible(true)
                                    .machineType("n1-standard-1")
                                    .oauthScopes(
                                            "https://www.googleapis.com/auth/compute",
                                            "https://www.googleapis.com/auth/devstorage.read_only",
                                            "https://www.googleapis.com/auth/logging.write",
                                            "https://www.googleapis.com/auth/monitoring"
                                    )
                                    .build()
                            )
                            .management(NodePoolManagementArgs.builder()
                                    .autoRepair(true)
                                    .build()
                            )
                            .build(),
                    CustomResourceOptions.builder()
                            .dependsOn(cluster)
                            .build());
            ctx.export("clusterName", cluster.name());

            // Manufacture a GKE-style kubeconfig. Note that this is slightly "different"
            // because of the way GKE requires gcloud to be in the picture for cluster
            // authentication (rather than using the client cert/key directly).
            final var gcpConfig = new com.pulumi.gcp.Config();
            var clusterName = String.format("%s_%s_%s",
                    gcpConfig.project().orElseThrow(),
                    gcpConfig.zone().orElseThrow(),
                    name
            );

            var masterAuthClusterCaCertificate = cluster.masterAuth()
                    .applyValue(a -> a.clusterCaCertificate().orElseThrow());

            var kubeconfig = cluster.endpoint()
                    .apply(endpoint -> masterAuthClusterCaCertificate.applyValue(
                            caCert -> MessageFormat.format(String.join("\n",
                                    "apiVersion: v1",
                                    "clusters:",
                                    "- cluster:",
                                    "    certificate-authority-data: {2}",
                                    "    server: https://{1}",
                                    "  name: {0}",
                                    "contexts:",
                                    "- context:",
                                    "    cluster: {0}",
                                    "    user: {0}",
                                    "  name: {0}",
                                    "current-context: {0}",
                                    "kind: Config",
                                    "preferences: '{}'",
                                    "users:",
                                    "- name: {0}",
                                    "  user:",
                                    "    auth-provider:",
                                    "      config:",
                                    "        cmd-args: config config-helper --format=json",
                                    "        cmd-path: gcloud",
                                    "        expiry-key: \"'{.credential.token_expiry}'\"",
                                    "        token-key: \"'{.credential.access_token}'\"",
                                    "      name: gcp"
                            ), clusterName, endpoint, caCert)
                    ));
            ctx.export("kubeconfig", kubeconfig);

            // Create a Kubernetes provider instance that uses our cluster from above.
            final var clusterProvider = new Provider(name,
                    ProviderArgs.builder()
                            .kubeconfig(kubeconfig)
                            .build(),
                    CustomResourceOptions.builder()
                            .dependsOn(nodePool, cluster)
                            .build()
            );
            final var clusterResourceOptions = CustomResourceOptions.builder()
                    .provider(clusterProvider)
                    .build();

            // Create a Kubernetes Namespace
            final var ns = new Namespace(name,
                    NamespaceArgs.Empty,
                    clusterResourceOptions
            );

            // Export the Namespace name
            var namespaceName = ns.metadata()
                    .applyValue(m -> m.orElseThrow().name().orElseThrow());

            ctx.export("namespaceName", namespaceName);

            final var appLabels = Map.of("appClass", name);

            final var metadata = ObjectMetaArgs.builder()
                    .namespace(namespaceName)
                    .labels(appLabels)
                    .build();

            // Create a NGINX Deployment
            final var deployment = new Deployment(name, DeploymentArgs.builder()
                    .metadata(metadata)
                    .spec(DeploymentSpecArgs.builder()
                            .replicas(1)
                            .selector(LabelSelectorArgs.builder()
                                    .matchLabels(appLabels)
                                    .build())
                            .template(PodTemplateSpecArgs.builder()
                                    .metadata(metadata)
                                    .spec(PodSpecArgs.builder()
                                            .containers(ContainerArgs.builder()
                                                    .name(name)
                                                    .image("nginx:latest")
                                                    .ports(ContainerPortArgs.builder()
                                                            .name("http")
                                                            .containerPort(80)
                                                            .build())
                                                    .build())
                                            .build())
                                    .build())
                            .build())
                    .build(), clusterResourceOptions);

            // Export the Deployment name
            ctx.export("deploymentName", deployment.metadata()
                    .applyValue(m -> m.orElseThrow().name().orElseThrow()));

            // Create a LoadBalancer Service for the NGINX Deployment
            final var service = new Service(name, ServiceArgs.builder()
                    .metadata(metadata)
                    .spec(ServiceSpecArgs.builder()
                            .type(Output.ofRight(ServiceSpecType.LoadBalancer))
                            .ports(ServicePortArgs.builder()
                                    .port(80)
                                    .targetPort(Output.ofRight("http"))
                                    .build())
                            .selector(appLabels)
                            .build())
                    .build(), clusterResourceOptions);

            // Export the Service name and public LoadBalancer endpoint
            ctx.export("serviceName", service.metadata()
                    .applyValue(m -> m.orElseThrow().name().orElseThrow()));

            ctx.export("servicePublicIP", service.status()
                    .applyValue(s -> s.orElseThrow().loadBalancer().orElseThrow())
                    .applyValue(status -> status.ingress().get(0).ip().orElseThrow()));

            return ctx.exports();
        }
    }

  csharp: |
    using Pulumi;
    using Pulumi.Gcp.Container;
    using Pulumi.Gcp.Container.Inputs;
    using Pulumi.Gcp.Container.Outputs;

    class KubernetesStack : Stack
    {
        public KubernetesStack()
        {
            var masterVersion = new Config().Get("masterVersion")
                                ?? (Input<string>) Output.Create(GetEngineVersions.InvokeAsync())
                                    .Apply(v => v.LatestMasterVersion);

            var cluster = new Cluster("helloworld", new ClusterArgs
            {
                InitialNodeCount = 2,
                MinMasterVersion = masterVersion,
                NodeVersion = masterVersion,
                NodeConfig = new ClusterNodeConfigArgs
                {
                    MachineType = "n1-standard-1",
                    OauthScopes =
                    {
                        "https://www.googleapis.com/auth/compute",
                        "https://www.googleapis.com/auth/devstorage.read_only",
                        "https://www.googleapis.com/auth/logging.write",
                        "https://www.googleapis.com/auth/monitoring"
                    }
                }
            });

            this.KubeConfig = Output.Tuple(cluster.Name, cluster.Endpoint, cluster.MasterAuth).Apply(
                t => GetKubeconfig(t.Item1, t.Item2, t.Item3)
            );

            this.ClusterName = cluster.Name;
        }

        [Output] public Output<string> ClusterName { get; set; }

        [Output] public Output<string> KubeConfig { get; set; }

        private static string GetKubeconfig(string clusterName, string clusterEndpoint, ClusterMasterAuth clusterMasterAuth)
        {
            var context = $"{Pulumi.Gcp.Config.Project}_{Pulumi.Gcp.Config.Zone}_{clusterName}";
            return $@"apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: {clusterMasterAuth.ClusterCaCertificate}
        server: https://{clusterEndpoint}
      name: {context}
    contexts:
    - context:
        cluster: {context}
        user: {context}
      name: {context}
    current-context: {context}
    kind: Config
    preferences: {{}}
    users:
    - name: {context}
      user:
        auth-provider:
          config:
            cmd-args: config config-helper --format=json
            cmd-path: gcloud
            expiry-key: '{{.credential.token_expiry}}'
            token-key: '{{.credential.access_token}}'
          name: gcp";
        }
    }
  go: |
    package main

    import (
      "github.com/pulumi/pulumi-gcp/sdk/v5/go/gcp/container"
      "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes"
      appsv1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/apps/v1"
      corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/core/v1"
      metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v3/go/kubernetes/meta/v1"
      "github.com/pulumi/pulumi/sdk/v3/go/pulumi"
    )

    func main() {
      pulumi.Run(func(ctx *pulumi.Context) error {

        engineVersions, err := container.GetEngineVersions(ctx, &container.GetEngineVersionsArgs{})
        if err != nil {
          return err
        }
        masterVersion := engineVersions.LatestMasterVersion

        cluster, err := container.NewCluster(ctx, "demo-cluster", &container.ClusterArgs{
          InitialNodeCount: pulumi.Int(2),
          MinMasterVersion: pulumi.String(masterVersion),
          NodeVersion:      pulumi.String(masterVersion),
          NodeConfig: &container.ClusterNodeConfigArgs{
            MachineType: pulumi.String("n1-standard-1"),
            OauthScopes: pulumi.StringArray{
              pulumi.String("https://www.googleapis.com/auth/compute"),
              pulumi.String("https://www.googleapis.com/auth/devstorage.read_only"),
              pulumi.String("https://www.googleapis.com/auth/logging.write"),
              pulumi.String("https://www.googleapis.com/auth/monitoring"),
            },
          },
        })
        if err != nil {
          return err
        }

        ctx.Export("kubeconfig", generateKubeconfig(cluster.Endpoint, cluster.Name, cluster.MasterAuth))

        k8sProvider, err := kubernetes.NewProvider(ctx, "k8sprovider", &kubernetes.ProviderArgs{
          Kubeconfig: generateKubeconfig(cluster.Endpoint, cluster.Name, cluster.MasterAuth),
        }, pulumi.DependsOn([]pulumi.Resource{cluster}))
        if err != nil {
          return err
        }

        namespace, err := corev1.NewNamespace(ctx, "app-ns", &corev1.NamespaceArgs{
          Metadata: &metav1.ObjectMetaArgs{
            Name: pulumi.String("demo-ns"),
          },
        }, pulumi.Provider(k8sProvider))
        if err != nil {
          return err
        }

        appLabels := pulumi.StringMap{
          "app": pulumi.String("demo-app"),
        }
        _, err = appsv1.NewDeployment(ctx, "app-dep", &appsv1.DeploymentArgs{
          Metadata: &metav1.ObjectMetaArgs{
            Namespace: namespace.Metadata.Elem().Name(),
          },
          Spec: appsv1.DeploymentSpecArgs{
            Selector: &metav1.LabelSelectorArgs{
              MatchLabels: appLabels,
            },
            Replicas: pulumi.Int(3),
            Template: &corev1.PodTemplateSpecArgs{
              Metadata: &metav1.ObjectMetaArgs{
                Labels: appLabels,
              },
              Spec: &corev1.PodSpecArgs{
                Containers: corev1.ContainerArray{
                  corev1.ContainerArgs{
                    Name:  pulumi.String("demo-app"),
                    Image: pulumi.String("jocatalin/kubernetes-bootcamp:v2"),
                  }},
              },
            },
          },
        }, pulumi.Provider(k8sProvider))
        if err != nil {
          return err
        }

        service, err := corev1.NewService(ctx, "app-service", &corev1.ServiceArgs{
          Metadata: &metav1.ObjectMetaArgs{
            Namespace: namespace.Metadata.Elem().Name(),
            Labels:    appLabels,
          },
          Spec: &corev1.ServiceSpecArgs{
            Ports: corev1.ServicePortArray{
              corev1.ServicePortArgs{
                Port:       pulumi.Int(80),
                TargetPort: pulumi.Int(8080),
              },
            },
            Selector: appLabels,
            Type:     pulumi.String("LoadBalancer"),
          },
        }, pulumi.Provider(k8sProvider))
        if err != nil {
          return err
        }

        ctx.Export("url", service.Status.ApplyT(func(status *corev1.ServiceStatus) *string {
          ingress := status.LoadBalancer.Ingress[0]
          if ingress.Hostname != nil {
            return ingress.Hostname
          }
          return ingress.Ip
        }))

        return nil
      })
    }

    func generateKubeconfig(clusterEndpoint pulumi.StringOutput, clusterName pulumi.StringOutput,
      clusterMasterAuth container.ClusterMasterAuthOutput) pulumi.StringOutput {
      context := pulumi.Sprintf("demo_%s", clusterName)

      return pulumi.Sprintf(`apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: %s
        server: https://%s
      name: %s
    contexts:
    - context:
        cluster: %s
        user: %s
      name: %s
    current-context: %s
    kind: Config
    preferences: {}
    users:
    - name: %s
      user:
        auth-provider:
          config:
            cmd-args: config config-helper --format=json
            cmd-path: gcloud
            expiry-key: '{.credential.token_expiry}'
            token-key: '{.credential.access_token}'
          name: gcp`,
        clusterMasterAuth.ClusterCaCertificate().Elem(),
        clusterEndpoint, context, context, context, context, context, context)
    }

  py: |
    from pulumi import Config, export, get_project, get_stack, Output, ResourceOptions
    from pulumi_gcp.config import project, zone
    from pulumi_gcp.container import Cluster, ClusterNodeConfigArgs
    from pulumi_kubernetes import Provider
    from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
    from pulumi_kubernetes.core.v1 import ContainerArgs, PodSpecArgs, PodTemplateSpecArgs, Service, ServicePortArgs, ServiceSpecArgs
    from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs
    from pulumi_random import RandomPassword

    # Read in some configurable settings for our cluster:
    config = Config(None)

    # nodeCount is the number of cluster nodes to provision. Defaults to 3 if unspecified.
    NODE_COUNT = config.get_int('node_count') or 3
    # nodeMachineType is the machine type to use for cluster nodes. Defaults to n1-standard-1 if unspecified.
    # See https://cloud.google.com/compute/docs/machine-types for more details on available machine types.
    NODE_MACHINE_TYPE = config.get('node_machine_type') or 'n1-standard-1'
    # username is the admin username for the cluster.
    USERNAME = config.get('username') or 'admin'
    # password is the password for the admin user in the cluster.
    PASSWORD = config.get_secret('password') or RandomPassword("password", length=20, special=True).result
    # master version of GKE engine
    MASTER_VERSION = config.get('master_version')

    # Now, actually create the GKE cluster.
    k8s_cluster = Cluster('gke-cluster',
        initial_node_count=NODE_COUNT,
        node_version=MASTER_VERSION,
        min_master_version=MASTER_VERSION,
        node_config=ClusterNodeConfigArgs(
            machine_type=NODE_MACHINE_TYPE,
            oauth_scopes=[
                'https://www.googleapis.com/auth/compute',
                'https://www.googleapis.com/auth/devstorage.read_only',
                'https://www.googleapis.com/auth/logging.write',
                'https://www.googleapis.com/auth/monitoring'
            ],
        ),
    )

    # Manufacture a GKE-style Kubeconfig. Note that this is slightly "different" because of the way GKE requires
    # gcloud to be in the picture for cluster authentication (rather than using the client cert/key directly).
    k8s_info = Output.all(k8s_cluster.name, k8s_cluster.endpoint, k8s_cluster.master_auth)
    k8s_config = k8s_info.apply(
        lambda info: """apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: {0}
        server: https://{1}
      name: {2}
    contexts:
    - context:
        cluster: {2}
        user: {2}
      name: {2}
    current-context: {2}
    kind: Config
    preferences: {{}}
    users:
    - name: {2}
      user:
        auth-provider:
          config:
            cmd-args: config config-helper --format=json
            cmd-path: gcloud
            expiry-key: '{{.credential.token_expiry}}'
            token-key: '{{.credential.access_token}}'
          name: gcp
    """.format(info[2]['cluster_ca_certificate'], info[1], '{0}_{1}_{2}'.format(project, zone, info[0])))

    # Make a Kubernetes provider instance that uses our cluster from above.
    k8s_provider = Provider('gke_k8s', kubeconfig=k8s_config)

    # Create a canary deployment to test that this cluster works.
    labels = { 'app': 'canary-{0}-{1}'.format(get_project(), get_stack()) }
    canary = Deployment('canary',
        spec=DeploymentSpecArgs(
            selector=LabelSelectorArgs(match_labels=labels),
            replicas=1,
            template=PodTemplateSpecArgs(
                metadata=ObjectMetaArgs(labels=labels),
                spec=PodSpecArgs(containers=[ContainerArgs(name='nginx', image='nginx')]),
            ),
        ), opts=ResourceOptions(provider=k8s_provider)
    )

    ingress = Service('ingress',
        spec=ServiceSpecArgs(
            type='LoadBalancer',
            selector=labels,
            ports=[ServicePortArgs(port=80)],
        ), opts=ResourceOptions(provider=k8s_provider)
    )

    # Finally, export the kubeconfig so that the client can easily access the cluster.
    export('kubeconfig', k8s_config)
    # Export the k8s ingress IP to access the canary deployment
    export('ingress_ip', ingress.status.apply(lambda status: status.load_balancer.ingress[0].ip))

  ts: |
    import * as gcp from "@pulumi/gcp";
    import * as k8s from "@pulumi/kubernetes";
    import * as pulumi from "@pulumi/pulumi";

    const name = "helloworld";

    const config = new pulumi.Config();
    export const masterVersion = config.get("masterVersion") ||
        gcp.container.getEngineVersions().then(it => it.latestMasterVersion);

    // Create a GKE cluster
    const cluster = new gcp.container.Cluster(name, {
        // We can't create a cluster with no node pool defined, but we want to only use
        // separately managed node pools. So we create the smallest possible default
        // node pool and immediately delete it.
        initialNodeCount: 1,
        removeDefaultNodePool: true,

        minMasterVersion: masterVersion,
    });

    const nodePool = new gcp.container.NodePool(`primary-node-pool`, {
        cluster: cluster.name,
        initialNodeCount: 2,
        location: cluster.location,
        nodeConfig: {
            preemptible: true,
            machineType: "n1-standard-1",
            oauthScopes: [
                "https://www.googleapis.com/auth/compute",
                "https://www.googleapis.com/auth/devstorage.read_only",
                "https://www.googleapis.com/auth/logging.write",
                "https://www.googleapis.com/auth/monitoring",
            ],
        },
        version: masterVersion,
        management: {
            autoRepair: true,
        },
    }, {
        dependsOn: [cluster],
    });

    // Export the Cluster name
    export const clusterName = cluster.name;

    // Manufacture a GKE-style kubeconfig. Note that this is slightly "different"
    // because of the way GKE requires gcloud to be in the picture for cluster
    // authentication (rather than using the client cert/key directly).
    export const kubeconfig = pulumi.
        all([ cluster.name, cluster.endpoint, cluster.masterAuth ]).
        apply(([ name, endpoint, masterAuth ]) => {
            const context = `${gcp.config.project}_${gcp.config.zone}_${name}`;
            return `apiVersion: v1
    clusters:
    - cluster:
        certificate-authority-data: ${masterAuth.clusterCaCertificate}
        server: https://${endpoint}
      name: ${context}
    contexts:
    - context:
        cluster: ${context}
        user: ${context}
      name: ${context}
    current-context: ${context}
    kind: Config
    preferences: {}
    users:
    - name: ${context}
      user:
        auth-provider:
          config:
            cmd-args: config config-helper --format=json
            cmd-path: gcloud
            expiry-key: '{.credential.token_expiry}'
            token-key: '{.credential.access_token}'
          name: gcp
    `;
        });

    // Create a Kubernetes provider instance that uses our cluster from above.
    const clusterProvider = new k8s.Provider(name, {
        kubeconfig: kubeconfig,
    }, {
      dependsOn: [nodePool],
    });

    // Create a Kubernetes Namespace
    const ns = new k8s.core.v1.Namespace(name, {}, { provider: clusterProvider });

    // Export the Namespace name
    export const namespaceName = ns.metadata.name;

    // Create a NGINX Deployment
    const appLabels = { appClass: name };
    const deployment = new k8s.apps.v1.Deployment(name,
        {
            metadata: {
                namespace: namespaceName,
                labels: appLabels,
            },
            spec: {
                replicas: 1,
                selector: { matchLabels: appLabels },
                template: {
                    metadata: {
                        labels: appLabels,
                    },
                    spec: {
                        containers: [
                            {
                                name: name,
                                image: "nginx:latest",
                                ports: [{ name: "http", containerPort: 80 }],
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

    // Export the Deployment name
    export const deploymentName = deployment.metadata.name;

    // Create a LoadBalancer Service for the NGINX Deployment
    const service = new k8s.core.v1.Service(name,
        {
            metadata: {
                labels: appLabels,
                namespace: namespaceName,
            },
            spec: {
                type: "LoadBalancer",
                ports: [{ port: 80, targetPort: "http" }],
                selector: appLabels,
            },
        },
        {
            provider: clusterProvider,
        },
    );

    // Export the Service name and public LoadBalancer endpoint
    export const serviceName = service.metadata.name;
    export const servicePublicIP = service.status.loadBalancer.ingress[0].ip;

benefits:
  title: The benefits of using Pulumi
  items:
    - title: Tame cloud complexity
      icon: code-window
      icon_color: salmon
      description: |
        Deliver infrastructure from 50+ cloud and SaaS providers. Pulumi’s SDKs provide a complete and consistent interface that offers full access to
        clouds and abstracts complexity.

    - title: Bring the cloud closer to application development
      icon: download-from-cloud
      icon_color: violet
      description: |
        Build reusable cloud infrastructure and infrastructure platforms that empower
        developers to build modern cloud applications faster and with less overhead.

    - title: Use engineering practices with infrastructure
      icon: exchange
      icon_color: blue
      description: |
        Use engineering practices with infrastructure” to: “Replace inefficient, manual infrastructure processes with automation.
        Test and deliver infrastructure through CI/CD workflows or automate deployments with code at runtime.
    - title: Foster collaboration and innovate faster
      icon: lightning
      icon_color: yellow
      description: |
        Unite infrastructure teams, developers, and security teams around shared languages and tools so that everyone can ship products quickly and reliably.

meta_desc: Infrastructure as code on Google Cloud with Pulumi for huge productivity gains and a unified programming model for developers and operators.
contact_us_form:
    section_id: contact-us
    hubspot_form_id: 3eee19cc-77d0-440a-85d9-8979e775b4e5
    headline: Need help with cloud-native infrastructure as code on GCP?
    quote:
        title: Learn how top engineering teams are using Pulumi's SDK to create, deploy, and manage GCP resources.
        name: Josh Imhoff
        name_title: Site Reliability Engineer, Cockroach Labs
        content: |
            We are building a distributed-database-as-a-service product that runs on Kubernetes clusters across
            multiple public clouds including GCP, AWS and others. Pulumi's declarative model, the support for real
            programming languages, and the uniform workflow on any cloud make our SRE team much more efficient.
---
