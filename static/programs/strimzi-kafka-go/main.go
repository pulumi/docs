package main

import (
	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	apiextensions "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	helm "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	meta "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		// Deploy Strimzi Kafka operator using Helm chart
		strimzi, err := helm.NewRelease(ctx, "strimzi-kafka-operator", &helm.ReleaseArgs{
			Chart:           pulumi.String("oci://quay.io/strimzi-helm/strimzi-kafka-operator"),
			Namespace:       pulumi.String("strimzi"),
			CreateNamespace: pulumi.Bool(true),
			Values: pulumi.Map{
				"watchAnyNamespace": pulumi.Bool(true),
			},
		})
		if err != nil {
			return err
		}

		// Deploy Kafka Node Pool
		_, err = apiextensions.NewCustomResource(ctx, "kafkaNodePool", &apiextensions.CustomResourceArgs{
			ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
			Kind:       pulumi.String("KafkaNodePool"),
			Metadata: &meta.ObjectMetaArgs{
				Name: pulumi.String("my-kafka-nodepool"),
				Labels: pulumi.StringMap{
					"strimzi.io/cluster": pulumi.String("my-cluster"),
				},
			},
			OtherFields: k8s.UntypedArgs{
				"spec": pulumi.Map{
					"replicas": pulumi.Int(1),
					"roles": pulumi.StringArray{
						pulumi.String("controller"),
						pulumi.String("broker"),
					},
					"storage": pulumi.Map{
						"type": pulumi.String("ephemeral"),
					},
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{strimzi}))
		if err != nil {
			return err
		}

		// Deploy Kafka Cluster
		_, err = apiextensions.NewCustomResource(ctx, "kafkaCluster", &apiextensions.CustomResourceArgs{
			ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
			Kind:       pulumi.String("Kafka"),
			Metadata: &meta.ObjectMetaArgs{
				Name: pulumi.String("my-cluster"),
				Annotations: pulumi.StringMap{
					"strimzi.io/kraft":      pulumi.String("enabled"),
					"strimzi.io/node-pools": pulumi.String("enabled"),
				},
			},
			OtherFields: k8s.UntypedArgs{
				"spec": pulumi.Map{
					"kafka": pulumi.Map{
						"replicas":        pulumi.Int(1),
						"version":         pulumi.String("3.8.0"),
						"storage":         pulumi.Map{"type": pulumi.String("ephemeral")},
						"metadataVersion": pulumi.String("3.8-IV0"),
						"listeners": pulumi.Array{
							pulumi.Map{
								"name": pulumi.String("plain"),
								"port": pulumi.Int(9092),
								"type": pulumi.String("internal"),
								"tls":  pulumi.Bool(false),
							},
							pulumi.Map{
								"name": pulumi.String("tls"),
								"port": pulumi.Int(9093),
								"type": pulumi.String("internal"),
								"tls":  pulumi.Bool(true),
							},
						},
						"config": pulumi.StringMap{
							"offsets.topic.replication.factor":         pulumi.String("1"),
							"transaction.state.log.replication.factor": pulumi.String("1"),
							"transaction.state.log.min.isr":            pulumi.String("1"),
							"default.replication.factor":               pulumi.String("1"),
							"min.insync.replicas":                      pulumi.String("1"),
						},
					},
					"entityOperator": pulumi.Map{
						"topicOperator": pulumi.Map{},
						"userOperator":  pulumi.Map{},
					},
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{strimzi}))
		if err != nil {
			return err
		}

		// Deploy Kafka Topic
		_, err = apiextensions.NewCustomResource(ctx, "kafkaTopic", &apiextensions.CustomResourceArgs{
			ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
			Kind:       pulumi.String("KafkaTopic"),
			Metadata: &meta.ObjectMetaArgs{
				Name: pulumi.String("my-topic"),
				Labels: pulumi.StringMap{
					"strimzi.io/cluster": pulumi.String("my-cluster"),
				},
			},
			OtherFields: k8s.UntypedArgs{
				"spec": pulumi.Map{
					"partitions": pulumi.Int(5),
					"replicas":   pulumi.Int(1),
					"config": pulumi.StringMap{
						"retention.ms":  pulumi.String("7200000"),
						"segment.bytes": pulumi.String("1073741824"),
					},
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{strimzi}))
		if err != nil {
			return err
		}

		// Deploy Kafka User
		_, err = apiextensions.NewCustomResource(ctx, "kafkaUser", &apiextensions.CustomResourceArgs{
			ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
			Kind:       pulumi.String("KafkaUser"),
			Metadata: &meta.ObjectMetaArgs{
				Name: pulumi.String("my-kafka-user"),
				Labels: pulumi.StringMap{
					"strimzi.io/cluster": pulumi.String("my-cluster"),
				},
			},
			OtherFields: k8s.UntypedArgs{
				"spec": pulumi.Map{
					"authentication": pulumi.Map{
						"type": pulumi.String("scram-sha-512"),
					},
					"authorization": pulumi.Map{
						"type": pulumi.String("simple"),
						"acls": pulumi.Array{
							pulumi.Map{
								"resource": pulumi.Map{
									"type":        pulumi.String("topic"),
									"name":        pulumi.String("my-topic"),
									"patternType": pulumi.String("literal"),
								},
								"operation": pulumi.String("Read"),
								"host":      pulumi.String("*"),
							},
						},
					},
				},
			},
		}, pulumi.DependsOn([]pulumi.Resource{strimzi}))
		if err != nil {
			return err
		}

		return nil
	})
}
