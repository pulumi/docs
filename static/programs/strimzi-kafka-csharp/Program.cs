using Pulumi;
using Pulumi.Kubernetes.Helm.V3;
using Pulumi.Kubernetes.ApiExtensions;
using Pulumi.Kubernetes.Types.Inputs.Helm.V3;
using Pulumi.Kubernetes.Types.Inputs.Meta.V1;
using System.Threading.Tasks;

class KafKaNodePoolArgs : CustomResourceArgs {
  public KafKaNodePoolArgs() : base("kafka.strimzi.io/v1beta2", "KafkaNodePool") {}
  [Input("spec")]
  public Input<KafakNodePoolSpecArgs> Spec { get; set; }
}

class KafakNodePoolSpecArgs : ResourceArgs {
  public Input<string> Replicas { get; set; }
  public InputList<string> Roles { get; set; }
  public InputMap<object> Storage { get; set; }
}

class KafkaClusterArgs : CustomResourceArgs {
  public KafkaClusterArgs() : base("kafka.strimzi.io/v1beta2", "Kafka") {}
  [Input("spec")]
  public Input<KafakaClusterSpecArgs> Spec { get; set; }
}

class KafakaClusterSpecArgs : ResourceArgs {
  public InputMap<object> Kafka { get; set; }
  public InputMap<object> EntityOperator { get; set; }
}

class KafkaUserArgs : CustomResourceArgs {
  public KafkaUserArgs() : base("kafka.strimzi.io/v1beta2", "KafkaUser") {}
  [Input("spec")]
  public Input<KafkaUserSpecArgs> Spec { get; set; }
}

class KafkaUserSpecArgs : ResourceArgs {
  public InputMap<object> Authentication { get; set; }
  public InputMap<object> Authorization { get; set; }
}

class KafkaTopicArgs : CustomResourceArgs {
  public KafkaTopicArgs() : base("kafka.strimzi.io/v1beta2", "KafkaTopic") {}
  [Input("spec")]
  public Input<KafkaTopicSpecArgs> Spec { get; set; }
}

class KafkaTopicSpecArgs : ResourceArgs {
  public Input<int> Partitions { get; set; }
  public Input<int> Replicas { get; set; }
  public InputMap<object> Config { get; set; }
}

class ListenerArgs : ResourceArgs {
  public Input<string> Name { get; set; }
  public Input<int> Port { get; set; }
  public Input<string> Type { get; set; }
  public Input<bool> Tls { get; set; }
}

class MyStack : Stack {
  public MyStack() {
    // Deploy Strimzi Kafka operator using Helm chart
    var strimzi = new Release("strimzi-kafka-operator", new ReleaseArgs {
      Chart = "oci://quay.io/strimzi-helm/strimzi-kafka-operator",
      Namespace = "strimzi",
      CreateNamespace = true,
      Values =
          new InputMap<object> {
            { "watchAnyNamespace", true },
          },
    });

    // Deploy Kafka Node Pool
    var kafkaNodePool = new Pulumi.Kubernetes.ApiExtensions.CustomResource(
        "kafkaNodePool",
        new KafKaNodePoolArgs {
          Metadata = new ObjectMetaArgs { Name = "my-kafka-nodepool",
                                          Labels = { { "strimzi.io/cluster",
                                                       "my-cluster" } } },
          Spec =
              new KafakNodePoolSpecArgs {
                Replicas = "1",
                Roles = new InputList<string> { "controller", "broker" },
                Storage = new InputMap<object> { { "type", "ephemeral" } }
              },
        },
        new CustomResourceOptions { DependsOn = { strimzi } });

    // Deploy Kafka Cluster
    var kafkaCluster = new Pulumi.Kubernetes.ApiExtensions.CustomResource(
        "kafkaCluster",
        new KafkaClusterArgs {
          Metadata =
              new ObjectMetaArgs { Name = "my-cluster",
                                   Annotations = { { "strimzi.io/kraft", "enabled" },
                                              { "strimzi.io/node-pools",
                                                "enabled" } } },
          Spec =
              new KafakaClusterSpecArgs {
                Kafka =
                    new InputMap<object> {
                      { "version", "3.8.0" },
                      {"replicas", 1 },
                      { "storage",
                        new InputMap<object> { { "type", "ephemeral" } } },
                      { "listeners",
                        new InputList<ListenerArgs> { new ListenerArgs() {
                                                       Name = "plain",
                                                       Port = 9092,
                                                       Type = "internal",
                                                       Tls = false,
                                                     },
                                                      new ListenerArgs() {
                                                        Name = "tls",
                                                        Port = 9093,
                                                        Type = "internal",
                                                        Tls = true,
                                                      } } },
                      { "metadataVersion", "3.8-IV0" },
                      { "config",
                        new InputMap<object> {
                          { "offsets.topic.replication.factor", "1" },
                          { "transaction.state.log.replication.factor", "1" },
                          { "transaction.state.log.min.isr", "1" },
                          { "default.replication.factor", "1" },
                          { "min.insync.replicas", "1" },
                        } }
                    },
                EntityOperator =
                    new InputMap<object> {
                      { "topicOperator", new InputMap<object>() },
                      { "userOperator", new InputMap<object>() }
                    }
              },
        },
        new CustomResourceOptions { DependsOn = { strimzi } });

    // Deploy Kafka Topic
    var kafkaTopic = new Pulumi.Kubernetes.ApiExtensions.CustomResource(
        "kafkaTopic",
        new KafkaTopicArgs {
          Metadata = new ObjectMetaArgs { Name = "my-topic",
                                          Labels = { { "strimzi.io/cluster",
                                                       "my-cluster" } } },
          Spec =
              new KafkaTopicSpecArgs {
                Partitions = 5, Replicas = 1,
                Config =
                    new InputMap<object> { { "retention.ms", "7200000" },
                                           { "segment.bytes", "1073741824" } }
              },
        },
        new CustomResourceOptions { DependsOn = { kafkaCluster } });

    // Deploy Kafka User
    var kafkaUser =
        new Pulumi.Kubernetes.ApiExtensions.CustomResource(
            "kafkaUser",
            new KafkaUserArgs {
              Metadata = new ObjectMetaArgs { Name = "my-kafka-user",
                                              Labels = { { "strimzi.io/cluster",
                                                           "my-cluster" } } },
              Spec =
                  new KafkaUserSpecArgs {
                    Authentication =
                        new InputMap<object> { { "type", "scram-sha-512" } },
                    Authorization =
                        new InputMap<object> {
                          { "type", "simple" },
                          { "acls", new[] { new InputMap<object> {
                              { "resource",
                                new InputMap<object> { { "type", "topic" },
                                                       { "name", "my-topic" },
                                                       { "patternType",
                                                         "literal" } } },
                              { "operation", "Read" },
                              { "host", "*" }
                            } } }
                        }
                  },
            },
            new CustomResourceOptions { DependsOn = { kafkaCluster } });
  }
}
class Program {
  static Task<int> Main() => Deployment.RunAsync<MyStack>();
}
