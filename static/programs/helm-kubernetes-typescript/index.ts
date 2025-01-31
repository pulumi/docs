import * as k8s from "@pulumi/kubernetes";
import * as k8shelm from "@pulumi/kubernetes/helm/v3";

const ns = new k8s.core.v1.Namespace("cnpg-system", {
    metadata: {
        name: "cnpg-system",
    },
});

new k8shelm.Release("cloudnativepg", {
    chart: "oci://ghcr.io/cloudnative-pg/charts/cloudnative-pg",
    namespace: ns.metadata.name,
    createNamespace: true,
});

const namespace = new k8s.core.v1.Namespace("flux-system", {
    metadata: {
        name: "flux-system",
    },
});

new k8s.helm.v3.Release("flux-operator", {
    chart: "oci://ghcr.io/controlplaneio-fluxcd/charts/flux-operator",
    namespace: namespace.metadata.name,
    createNamespace: true,
});

const namespaceKafka = new k8s.core.v1.Namespace("kafka", {
    metadata: {
        name: "kafka",
    },
});

new k8s.helm.v3.Release("strimzi-kafka-operator", {
    chart: "strimzi-kafka-operator",
    namespace: namespaceKafka.metadata.name,
    repositoryOpts: {
        repo: "https://strimzi.io/charts/",
    },
    createNamespace: true,
});

new k8s.apiextensions.CustomResource("cluster-example-with-backup", {
    apiVersion: "postgresql.cnpg.io/v1",
    kind: "Cluster",
    metadata: {
        name: "cluster-example-with-backup",
    },
    spec: {
        instances: 3,
        primaryUpdateStrategy: "unsupervised",

        // Persistent storage configuration
        storage: {
            storageClass: "standard",
            size: "1Gi",
        },

        // Backup properties
        backup: {
            barmanObjectStore: {
                destinationPath: "s3://backups/",
                endpointURL: "http://minio:9000",
                s3Credentials: {
                    accessKeyId: {
                        name: "minio",
                        key: "ACCESS_KEY_ID",
                    },
                    secretAccessKey: {
                        name: "minio",
                        key: "ACCESS_SECRET_KEY",
                    },
                },
                wal: {
                    compression: "gzip",
                },
            },
        },
    },
});

new k8s.apiextensions.CustomResource("flux", {
    apiVersion: "fluxcd.controlplane.io/v1",
    kind: "FluxInstance",
    metadata: {
        name: "flux",
        namespace: "flux-system",
        annotations: {
            "fluxcd.controlplane.io/reconcileEvery": "1h",
            "fluxcd.controlplane.io/reconcileTimeout": "5m",
        },
    },
    spec: {
        distribution: {
            version: "2.x",
            registry: "ghcr.io/fluxcd",
            artifact: "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests",
        },
        components: ["source-controller", "kustomize-controller", "helm-controller", "notification-controller", "image-reflector-controller", "image-automation-controller"],
        cluster: {
            type: "kubernetes",
            multitenant: false,
            networkPolicy: true,
            domain: "cluster.local",
        },
        kustomize: {
            patches: [
                {
                    target: {
                        kind: "Deployment",
                        name: "(kustomize-controller|helm-controller)",
                    },
                    patch: `
                    - op: add
                      path: /spec/template/spec/containers/0/args/-
                      value: --concurrent=10
                    - op: add
                      path: /spec/template/spec/containers/0/args/-
                      value: --requeue-dependency=5s
                    `,
                },
            ],
        },
    },
});

new k8s.apiextensions.CustomResource("example-kafka-node-pool", {
    apiVersion: "kafka.strimzi.io/v1beta2",
    kind: "KafkaNodePool",
    metadata: {
        name: "example-kafka-node-pool",
        labels: {
            "strimzi.io/cluster": "example-kafka-cluster",
        },
        namespace: "kafka",
    },
    spec: {
        replicas: 1,
        roles: ["controller", "broker"],
        storage: {
            type: "ephemeral",
        },
    },
});

new k8s.apiextensions.CustomResource("example-kafka-cluster", {
    apiVersion: "kafka.strimzi.io/v1beta2",
    kind: "Kafka",
    metadata: {
        name: "example-kafka-cluster",
        annotations: {
            "strimzi.io/kraft": "enabled",
            "strimzi.io/node-pools": "enabled",
        },
        namespace: "kafka",
    },
    spec: {
        kafka: {
            replicas: 1,
            version: "3.8.0",
            storage: {
                type: "ephemeral",
            },
            metadataVersion: "3.8-IV0",
            listeners: [
                {
                    name: "plain",
                    port: 9092,
                    type: "internal",
                    tls: false,
                },
                {
                    name: "tls",
                    port: 9093,
                    type: "internal",
                    tls: true,
                },
            ],
            config: {
                "offsets.topic.replication.factor": 1,
                "transaction.state.log.replication.factor": 1,
                "transaction.state.log.min.isr": 1,
                "default.replication.factor": 1,
                "min.insync.replicas": 1,
            },
        },
        entityOperator: {
            topicOperator: {},
            userOperator: {},
        },
    },
});

new k8s.apiextensions.CustomResource("example-kafka-topic", {
    apiVersion: "kafka.strimzi.io/v1beta2",
    kind: "KafkaTopic",
    metadata: {
        name: "example-kafka-topic",
        labels: {
            "strimzi.io/cluster": "example-kafka-cluster",
        },
        namespace: "kafka",
    },
    spec: {
        partitions: 5,
        replicas: 1,
        config: {
            "retention.ms": 7200000,
            "segment.bytes": 1073741824,
        },
    },
});
