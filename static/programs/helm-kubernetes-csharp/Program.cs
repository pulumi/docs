using System.Threading.Tasks;
using Pulumi;
using Pulumi.Kubernetes.Core.V1;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Core.V1;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Collections.Generic;
using Pulumi.Kubernetes.ApiExtensions;

class PostGreSQLClusterArgs : CustomResourceArgs
{
    [Input("postgresql.cnpg.io/v1")]
    public Input<string> ApiVersion { get; set; }
    [Input("Cluster")]
    public Input<string> Kind { get; set; }
    public ObjectMetaArgs Metadata { get; set; }
    public Dictionary<string, object> Others { get; set; }
    [Input("spec")]
    public InputMap<object> Spec { get; set; }

    public PostGreSQLClusterArgs(string apiVersion, string kind) : base(apiVersion, kind)
    {
    }
}

class FluxInstanceArgs : CustomResourceArgs
{
    public string ApiVersion { get; set; }
    public string Kind { get; set; }
    public ObjectMetaArgs Metadata { get; set; }
    public Dictionary<string, object> Spec { get; set; }

    public FluxInstanceArgs(string apiVersion, string kind) : base(apiVersion, kind)
    {
    }
}

class KafkaNodePoolArgs : CustomResourceArgs
{
    public string ApiVersion { get; set; }
    public string Kind { get; set; }
    public ObjectMetaArgs Metadata { get; set; }
    public Dictionary<string, object> Spec { get; set; }

    public KafkaNodePoolArgs(string apiVersion, string kind) : base(apiVersion, kind)
    {
    }
}

class KafkaClusterArgs : CustomResourceArgs
{
    public string ApiVersion { get; set; }
    public string Kind { get; set; }
    public ObjectMetaArgs Metadata { get; set; }
    public Dictionary<string, object> Spec { get; set; }

    public KafkaClusterArgs(string apiVersion, string kind) : base(apiVersion, kind)
    {
    }
}

class KafkaTopicArgs : CustomResourceArgs
{
    public string ApiVersion { get; set; }
    public string Kind { get; set; }
    public ObjectMetaArgs Metadata { get; set; }
    public Dictionary<string, object> Spec { get; set; }

    public KafkaTopicArgs(string apiVersion, string kind) : base(apiVersion, kind)
    {
    }
}

class MyStack : Stack
{
    public MyStack()
    {
        var ns = new Namespace("cnpg-system", new NamespaceArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Name = "cnpg-system"
            }
        });

        var release = new Release("cloudnativepg", new ReleaseArgs
        {
            Chart = "oci://ghcr.io/cloudnative-pg/charts/cloudnative-pg",
            Namespace = ns.Metadata.Apply(m => m.Name),
            CreateNamespace = true
        });

        var namespaceFluxSystem = new Namespace("flux-system", new NamespaceArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Name = "flux-system",
            },
        });

        var fluxOperator = new Release("flux-operator", new ReleaseArgs
        {
            Chart = "oci://ghcr.io/controlplaneio-fluxcd/charts/flux-operator",
            Namespace = namespaceFluxSystem.Metadata.Apply(metadata => metadata.Name),
            CreateNamespace = true,
        });
        var namespaceKafka = new Namespace("kafka", new NamespaceArgs
        {
            Metadata = new ObjectMetaArgs
            {
                Name = "kafka",
            }
        });

        var strimziKafkaOperator = new Release("strimzi-kafka-operator", new ReleaseArgs
        {
            Chart = "strimzi-kafka-operator",
            Namespace = namespaceKafka.Metadata.Apply(ns => ns.Name),
            RepositoryOpts = new RepositoryOptsArgs
            {
                Repo = "https://strimzi.io/charts/",
            },
            CreateNamespace = true,
        });

        var postgresqlCluster = new Pulumi.Kubernetes.ApiExtensions.CustomResource("cluster-example-with-backup", new PostGreSQLClusterArgs("postgresql.cnpg.io/v1", "Cluster")
        {
            ApiVersion = "postgresql.cnpg.io/v1",
            Kind = "Cluster",
            Metadata = new ObjectMetaArgs
            {
                Name = "cluster-example-with-backup",
            },
            Spec = new InputMap<object>
            {
                { "instances", 3 },
                { "primaryUpdateStrategy", "unsupervised" },
                { "storage", new InputMap<object>
                    {
                        { "storageClass", "standard" },
                        { "size", "1Gi" },
                    }
                },
                { "backup", new InputMap<object>
                    {
                        { "barmanObjectStore", new InputMap<object>
                            {
                                { "destinationPath", "s3://backups/" },
                                { "endpointURL", "http://minio:9000" },
                                { "s3Credentials", new InputMap<object>
                                    {
                                        { "accessKeyId", new InputMap<object>
                                            {
                                                { "name", "minio" },
                                                { "key", "ACCESS_KEY_ID" },
                                            }
                                        },
                                        { "secretAccessKey", new InputMap<object>
                                            {
                                                { "name", "minio" },
                                                { "key", "ACCESS_SECRET_KEY" },
                                            }
                                        },
                                    }
                                },
                                { "wal", new InputMap<object>
                                    {
                                        { "compression", "gzip" },
                                    }
                                },
                            }
                        },
                    }
                },
            }
        });

        var flux = new Pulumi.Kubernetes.ApiExtensions.CustomResource("flux", new FluxInstanceArgs("fluxcd.controlplane.io/v1", "FluxInstance")
        {
            ApiVersion = "fluxcd.controlplane.io/v1",
            Kind = "FluxInstance",
            Metadata = new ObjectMetaArgs
            {
                Name = "flux",
                Annotations =
                {
                    { "fluxcd.controlplane.io/reconcileEvery", "1h" },
                    { "fluxcd.controlplane.io/reconcileTimeout", "5m" },
                }
            },
            Spec = new Dictionary<string, object>
            {
                { "distribution", new Dictionary<string, object>
                    {
                        { "version", "2.x" },
                        { "registry", "ghcr.io/fluxcd" },
                        { "artifact", "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests" }
                    }
                },
                { "components", new[]
                    {
                        "source-controller",
                        "kustomize-controller",
                        "helm-controller",
                        "notification-controller",
                        "image-reflector-controller",
                        "image-automation-controller"
                    }
                },
                { "cluster", new Dictionary<string, object>
                    {
                        { "type", "kubernetes" },
                        { "multitenant", false },
                        { "networkPolicy", true },
                        { "domain", "cluster.local" }
                    }
                },
                { "kustomize", new Dictionary<string, object>
                    {
                        { "patches", new[]
                            {
                                new Dictionary<string, object>
                                {
                                    { "target", new Dictionary<string, object>
                                        {
                                            { "kind", "Deployment" },
                                            { "name", "(kustomize-controller|helm-controller)" }
                                        }
                                    },
                                    { "patch", new[]
                                        {
                                            new Dictionary<string, object>
                                            {
                                                { "op", "add" },
                                                { "path", "/spec/template/spec/containers/0/args/-" },
                                                { "value", "--concurrent=10" }
                                            },
                                            new Dictionary<string, object>
                                            {
                                                { "op", "add" },
                                                { "path", "/spec/template/spec/containers/0/args/-" },
                                                { "value", "--requeue-dependency=5s" }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
        });

        var kafkaNodePool = new Pulumi.Kubernetes.ApiExtensions.CustomResource("exampleKafkaNodePool", new KafkaNodePoolArgs("kafka.strimzi.io/v1beta2", "KafkaNodePool")
                {
                    ApiVersion = "kafka.strimzi.io/v1beta2",
                    Kind = "KafkaNodePool",
                    Metadata = new ObjectMetaArgs
                    {
                        Name = "example-kafka-node-pool",
                        Labels =
                        {
                            { "strimzi.io/cluster", "example-kafka-cluster" }
                        }
                    },
                    Spec = new Dictionary<string, object>
                    {
                        { "replicas", 1 },
                        { "roles", new List<string> { "controller", "broker" } },
                        { "storage", new Dictionary<string, object> { { "type", "ephemeral" } } }
                    }
                });

        var kafkaCluster = new Pulumi.Kubernetes.ApiExtensions.CustomResource("exampleKafkaCluster", new KafkaClusterArgs("kafka.strimzi.io/v1beta2", "Kafka")
        {
            ApiVersion = "kafka.strimzi.io/v1beta2",
            Kind = "Kafka",
            Metadata = new ObjectMetaArgs
            {
                Name = "example-kafka-cluster",
                Annotations =
                {
                    { "strimzi.io/kraft", "enabled" },
                    { "strimzi.io/node-pools", "enabled" }
                }
            },
            Spec = new Dictionary<string, object>
            {
                { "kafka", new Dictionary<string, object> {
                    { "replicas", 1 },
                    { "version", "3.8.0" },
                    { "storage", new Dictionary<string, object> { { "type", "ephemeral" } } },
                    { "metadataVersion", "3.8-IV0" },
                    { "listeners", new List<Dictionary<string, object>> {
                        new Dictionary<string, object> {
                            { "name", "plain" },
                            { "port", 9092 },
                            { "type", "internal" },
                            { "tls", false }
                        },
                        new Dictionary<string, object> {
                            { "name", "tls" },
                            { "port", 9093 },
                            { "type", "internal" },
                            { "tls", true }
                        }
                    }},
                    { "config", new Dictionary<string, object> {
                        { "offsets.topic.replication.factor", 1 },
                        { "transaction.state.log.replication.factor", 1 },
                        { "transaction.state.log.min.isr", 1 },
                        { "default.replication.factor", 1 },
                        { "min.insync.replicas", 1 }
                    }}
                }},
                { "entityOperator", new Dictionary<string, object> {
                    { "topicOperator", new Dictionary<string, object>() },
                    { "userOperator", new Dictionary<string, object>() }
                }}
            }
        });

        var kafkaTopic = new Pulumi.Kubernetes.ApiExtensions.CustomResource("exampleKafkaTopic", new KafkaTopicArgs("kafka.strimzi.io/v1beta2", "KafkaTopic")
        {
            ApiVersion = "kafka.strimzi.io/v1beta2",
            Kind = "KafkaTopic",
            Metadata = new ObjectMetaArgs
            {
                Name = "example-kafka-topic",
                Labels =
                {
                    { "strimzi.io/cluster", "example-kafka-cluster" }
                }
            },
            Spec = new Dictionary<string, object>
            {
                { "partitions", 5 },
                { "replicas", 1 },
                { "config", new Dictionary<string, object> {
                    { "retention.ms", 7200000 },
                    { "segment.bytes", 1073741824 }
                }}
            }
        });
    }
}

class Program
{
    static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
