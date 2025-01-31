import pulumi_kubernetes as k8s
import pulumi_kubernetes.helm.v3 as k8shelm
import pulumi_kubernetes.meta.v1 as meta

ns = k8s.core.v1.Namespace(
    "cnpg-system",
    metadata=meta.ObjectMetaArgs(
        name="cnpg-system",
    ),
)

release = k8shelm.Release(
    "cloudnativepg",
    chart="oci://ghcr.io/cloudnative-pg/charts/cloudnative-pg",
    namespace=ns.metadata["name"],
    create_namespace=True,
)

flux_namespace = k8s.core.v1.Namespace(
    "flux-system",
    metadata=meta.ObjectMetaArgs(
        name="flux-system",
    ),
)
flux_operator = k8shelm.Release(
    "flux-operator",
    chart="oci://ghcr.io/controlplaneio-fluxcd/charts/flux-operator",
    namespace=flux_namespace.metadata["name"],
    create_namespace=True,
)

kafka_namespace = k8s.core.v1.Namespace(
    "kafka",
    metadata=meta.ObjectMetaArgs(
        name="kafka",
    ),
)

strimzi_kafka_operator = k8shelm.Release(
    "strimzi-kafka-operator",
    chart="strimzi-kafka-operator",
    namespace=kafka_namespace.metadata["name"],
    repository_opts={
        "repo": "https://strimzi.io/charts/",
    },
    create_namespace=True,
)

from pulumi_kubernetes import apiextensions

postgresql_cluster = apiextensions.CustomResource(
    "cluster-example-with-backup",
    api_version="postgresql.cnpg.io/v1",
    kind="Cluster",
    metadata=meta.ObjectMetaArgs(
        name="cluster-example-with-backup",
    ),
    spec={
        "instances": 3,
        "primaryUpdateStrategy": "unsupervised",
        # Persistent storage configuration
        "storage": {
            "storageClass": "standard",
            "size": "1Gi",
        },
        # Backup properties
        "backup": {
            "barmanObjectStore": {
                "destinationPath": "s3://backups/",
                "endpointURL": "http://minio:9000",
                "s3Credentials": {
                    "accessKeyId": {
                        "name": "minio",
                        "key": "ACCESS_KEY_ID",
                    },
                    "secretAccessKey": {
                        "name": "minio",
                        "key": "ACCESS_SECRET_KEY",
                    },
                },
                "wal": {
                    "compression": "gzip",
                },
            },
        },
    },
)

flux_instance = k8s.apiextensions.CustomResource(
    "flux",
    api_version="fluxcd.controlplane.io/v1",
    kind="FluxInstance",
    metadata={
        "name": "flux",
        "namespace": flux_namespace.metadata["name"],
        "annotations": {
            "fluxcd.controlplane.io/reconcileEvery": "1h",
            "fluxcd.controlplane.io/reconcileTimeout": "5m",
        },
    },
    spec={
        "distribution": {
            "version": "2.x",
            "registry": "ghcr.io/fluxcd",
            "artifact": "oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests",
        },
        "components": [
            "source-controller",
            "kustomize-controller",
            "helm-controller",
            "notification-controller",
            "image-reflector-controller",
            "image-automation-controller",
        ],
        "cluster": {
            "type": "kubernetes",
            "multitenant": False,
            "networkPolicy": True,
            "domain": "cluster.local",
        },
        "kustomize": {
            "patches": [
                {
                    "target": {
                        "kind": "Deployment",
                        "name": "(kustomize-controller|helm-controller)",
                    },
                    "patch": [
                        {
                            "op": "add",
                            "path": "/spec/template/spec/containers/0/args/-",
                            "value": "--concurrent=10",
                        },
                        {
                            "op": "add",
                            "path": "/spec/template/spec/containers/0/args/-",
                            "value": "--requeue-dependency=5s",
                        },
                    ],
                }
            ]
        },
    },
)

kafka_node_pool = k8s.apiextensions.CustomResource(
    "example-kafka-node-pool",
    api_version="kafka.strimzi.io/v1beta2",
    kind="KafkaNodePool",
    metadata={
        "name": "example-kafka-node-pool",
        "labels": {
            "strimzi.io/cluster": "example-kafka-cluster",
        },
        "namespace": kafka_namespace.metadata["name"],
    },
    spec={
        "replicas": 1,
        "roles": ["controller", "broker"],
        "storage": {
            "type": "ephemeral",
        },
    },
)

kafka_cluster = k8s.apiextensions.CustomResource(
    "example-kafka-cluster",
    api_version="kafka.strimzi.io/v1beta2",
    kind="Kafka",
    metadata={
        "name": "example-kafka-cluster",
        "annotations": {
            "strimzi.io/kraft": "enabled",
            "strimzi.io/node-pools": "enabled",
        },
        "namespace": kafka_namespace.metadata["name"],
    },
    spec={
        "kafka": {
            "replicas": 1,
            "version": "3.8.0",
            "storage": {
                "type": "ephemeral",
            },
            "metadataVersion": "3.8-IV0",
            "listeners": [
                {
                    "name": "plain",
                    "port": 9092,
                    "type": "internal",
                    "tls": False,
                },
                {
                    "name": "tls",
                    "port": 9093,
                    "type": "internal",
                    "tls": True,
                },
            ],
            "config": {
                "offsets.topic.replication.factor": 1,
                "transaction.state.log.replication.factor": 1,
                "transaction.state.log.min.isr": 1,
                "default.replication.factor": 1,
                "min.insync.replicas": 1,
            },
        },
        "entityOperator": {
            "topicOperator": {},
            "userOperator": {},
        },
    },
)

kafka_topic = k8s.apiextensions.CustomResource(
    "example-kafka-topic",
    api_version="kafka.strimzi.io/v1beta2",
    kind="KafkaTopic",
    metadata={
        "name": "example-kafka-topic",
        "labels": {
            "strimzi.io/cluster": "example-kafka-cluster",
        },
        "namespace": kafka_namespace.metadata["name"],
    },
    spec={
        "partitions": 5,
        "replicas": 1,
        "config": {
            "retention.ms": 7200000,
            "segment.bytes": 1073741824,
        },
    },
)
