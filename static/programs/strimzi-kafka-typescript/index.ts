import * as k8s from "@pulumi/kubernetes";

const strimzi = new k8s.helm.v3.Release("strimzi-kafka-operator", {
    chart: "oci://quay.io/strimzi-helm/strimzi-kafka-operator",
    values: {
        watchAnyNamespace: true, // if you want the operator to watch all namespaces
    },
    namespace: "strimzi",
    createNamespace: true,
});

export const strimziName = strimzi.name;

const kafkaNodePool = new k8s.apiextensions.CustomResource("kafkaNodePool", {
    apiVersion: "kafka.strimzi.io/v1beta2",
    kind: "KafkaNodePool",
    metadata: {
        name: "my-kafka-nodepool",
        labels: {
            "strimzi.io/cluster": "my-cluster",
        },
    },
    spec: {
        replicas: 1,
        roles: ["controller", "broker"],
        storage: {
            type: "ephemeral",
        },
    },
});

const kafkaCluster = new k8s.apiextensions.CustomResource(
    "kafkaCluster",
    {
        apiVersion: "kafka.strimzi.io/v1beta2",
        kind: "Kafka",
        metadata: {
            name: "my-cluster",
            annotations: {
                "strimzi.io/kraft": "enabled",
                "strimzi.io/node-pools": "enabled",
            },
        },
        spec: {
            kafka: {
                replicas: 1,
                version: "3.8.0",
                storage: {
                    type: "ephemeral",
                },
                listeners: [
                    { name: "plain", port: 9092, type: "internal", tls: false },
                    { name: "tls", port: 9093, type: "internal", tls: true },
                ],
                metadataVersion: "3.8-IV0",
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
    },
    { dependsOn: [strimzi] },
);

const kafkaTopic = new k8s.apiextensions.CustomResource(
    "kafkaTopic",
    {
        apiVersion: "kafka.strimzi.io/v1beta2",
        kind: "KafkaTopic",
        metadata: {
            name: "my-topic",
            labels: {
                "strimzi.io/cluster": "my-cluster",
            },
        },
        spec: {
            partitions: 5,
            replicas: 1,
            config: {
                "retention.ms": 7200000,
                "segment.bytes": 1073741824,
            },
        },
    },
    { dependsOn: [strimzi] },
);

const kafkaUser = new k8s.apiextensions.CustomResource(
    "kafkaUser",
    {
        apiVersion: "kafka.strimzi.io/v1beta2",
        kind: "KafkaUser",
        metadata: {
            name: "my-kafka-user",
            labels: {
                "strimzi.io/cluster": "my-cluster",
            },
        },
        spec: {
            authentication: {
                type: "scram-sha-512",
            },
            authorization: {
                type: "simple",
                acls: [
                    {
                        resource: {
                            type: "topic",
                            name: "my-topic",
                            patternType: "literal",
                        },
                        operation: "Read",
                        host: "*",
                    },
                ],
            },
        },
    },
    { dependsOn: [strimzi] },
);
