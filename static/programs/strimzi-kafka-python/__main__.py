import pulumi
import pulumi_kubernetes as k8s

strimzi = k8s.helm.v3.Release(
    "strimzi-kafka-operator",
    k8s.helm.v3.ReleaseArgs(
        chart="oci://quay.io/strimzi-helm/strimzi-kafka-operator",
        namespace="strimzi",
        create_namespace=True,
        values={
            "watchAnyNamespace": True,  # if you want the operator to watch all namespaces
        },
    ),
)

strimzi_name = pulumi.Output.strimzi_name(strimzi)

kafka_node_pool = (
    k8s.apiextensions.CustomResource(
        "kafkaNodePool",
        api_version="kafka.strimzi.io/v1beta2",
        kind="KafkaNodePool",
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name="my-kafka-nodepool",
            labels={
                "strimzi.io/cluster": "my-cluster",
            },
        ),
        spec={
            "replicas": 1,
            "roles": ["controller", "broker"],
            "storage": {
                "type": "ephemeral",
            },
        },
        opts=pulumi.ResourceOptions(depends_on=[strimzi]),
    ),
)

kafka_cluster = (
    k8s.apiextensions.CustomResource(
        "kafkaCluster",
        api_version="kafka.strimzi.io/v1beta2",
        kind="Kafka",
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name="my-cluster",
            annotations={
                "strimzi.io/kraft": "enabled",
                "strimzi.io/node-pools": "enabled",
            },
        ),
        spec={
            "kafka": {
                "replicas": 1,
                "version": "3.8.0",
                "storage": {"type": "ephemeral"},
                "listeners": [
                    {"name": "plain", "port": 9092, "type": "internal", "tls": False},
                    {"name": "tls", "port": 9093, "type": "internal", "tls": True},
                ],
                "metadataVersion": "3.8-IV0",
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
        opts=pulumi.ResourceOptions(depends_on=[strimzi]),
    ),
)

kafka_topic = (
    k8s.apiextensions.CustomResource(
        "kafkaTopic",
        api_version="kafka.strimzi.io/v1beta2",
        kind="KafkaTopic",
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name="my-topic",
            labels={
                "strimzi.io/cluster": "my-cluster",
            },
        ),
        spec={
            "partitions": 5,
            "replicas": 1,
            "config": {
                "retention.ms": 7200000,
                "segment.bytes": 1073741824,
            },
        },
        opts=pulumi.ResourceOptions(depends_on=[strimzi]),
    ),
)

kafka_user = (
    k8s.apiextensions.CustomResource(
        "kafkaUser",
        api_version="kafka.strimzi.io/v1beta2",
        kind="KafkaUser",
        metadata=k8s.meta.v1.ObjectMetaArgs(
            name="my-kafka-user",
            labels={
                "strimzi.io/cluster": "my-cluster",
            },
        ),
        spec={
            "authentication": {
                "type": "scram-sha-512",
            },
            "authorization": {
                "type": "simple",
                "acls": [
                    {
                        "resource": {
                            "type": "topic",
                            "name": "my-topic",
                            "patternType": "literal",
                        },
                        "operation": "Read",
                        "host": "*",
                    },
                ],
            },
        },
        opts=pulumi.ResourceOptions(depends_on=[strimzi]),
    ),
)
