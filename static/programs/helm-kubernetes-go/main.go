package main

import (
	k8s "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes"
	apiv1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/apiextensions"
	corev1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/core/v1"
	helmv3 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/helm/v3"
	metav1 "github.com/pulumi/pulumi-kubernetes/sdk/v4/go/kubernetes/meta/v1"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		ns, err := corev1.NewNamespace(ctx, "cnpg-system", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("cnpg-system"),
			},
		})
		if err != nil {
			return err
		}

		_, err = helmv3.NewRelease(ctx, "cloudnativepg", &helmv3.ReleaseArgs{
			Chart:           pulumi.String("oci://ghcr.io/cloudnative-pg/charts/cloudnative-pg"),
			Namespace:       ns.Metadata.Name().Elem(),
			CreateNamespace: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		namespace, err := corev1.NewNamespace(ctx, "flux-system", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("flux-system"),
			},
		})
		if err != nil {
			return err
		}

		_, err = helmv3.NewRelease(ctx, "flux-operator", &helmv3.ReleaseArgs{
			Chart:           pulumi.String("oci://ghcr.io/controlplaneio-fluxcd/charts/flux-operator"),
			Namespace:       namespace.Metadata.Name().Elem(),
			CreateNamespace: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		namespaceKafka, err := corev1.NewNamespace(ctx, "kafka", &corev1.NamespaceArgs{
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("kafka"),
			},
		})
		if err != nil {
			return err
		}

		_, err = helmv3.NewRelease(ctx, "strimzi-kafka-operator", &helmv3.ReleaseArgs{
			Chart:     pulumi.String("strimzi-kafka-operator"),
			Namespace: namespaceKafka.Metadata.Name(),
			RepositoryOpts: helmv3.RepositoryOptsArgs{
				Repo: pulumi.String("https://strimzi.io/charts/"),
			},
			CreateNamespace: pulumi.Bool(true),
		})
		if err != nil {
			return err
		}

		_, err = apiv1.NewCustomResource(ctx, "cluster-example-with-backup", &apiv1.CustomResourceArgs{
			ApiVersion: pulumi.String("postgresql.cnpg.io/v1"),
			Kind:       pulumi.String("Cluster"),
			Metadata: &metav1.ObjectMetaArgs{
				Name: pulumi.String("cluster-example-with-backup"),
			},
			OtherFields: k8s.UntypedArgs{
				"instances":             pulumi.Int(3),
				"primaryUpdateStrategy": pulumi.String("unsupervised"),
				"storage": pulumi.Map{
					"storageClass": pulumi.String("standard"),
					"size":         pulumi.String("1Gi"),
				},
				"backup": pulumi.Map{
					"barmanObjectStore": pulumi.Map{
						"destinationPath": pulumi.String("s3://backups/"),
						"endpointURL":     pulumi.String("http://minio:9000"),
						"s3Credentials": pulumi.Map{
							"accessKeyId": pulumi.Map{
								"name": pulumi.String("minio"),
								"key":  pulumi.String("ACCESS_KEY_ID"),
							},
							"secretAccessKey": pulumi.Map{
								"name": pulumi.String("minio"),
								"key":  pulumi.String("ACCESS_SECRET_KEY"),
							},
						},
						"wal": pulumi.Map{
							"compression": pulumi.String("gzip"),
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}

		_, err = apiv1.NewCustomResource(ctx, "flux", &apiv1.CustomResourceArgs{
			ApiVersion: pulumi.String("fluxcd.controlplane.io/v1"),
			Kind:       pulumi.String("FluxInstance"),
			Metadata: &metav1.ObjectMetaArgs{
				Name:      pulumi.String("flux"),
				Namespace: pulumi.String("flux-system"),
				Annotations: pulumi.StringMap{
					"fluxcd.controlplane.io/reconcileEvery":   pulumi.String("1h"),
					"fluxcd.controlplane.io/reconcileTimeout": pulumi.String("5m"),
				},
			},
			OtherFields: k8s.UntypedArgs{
				"distribution": pulumi.Map{
					"version":  pulumi.String("2.x"),
					"registry": pulumi.String("ghcr.io/fluxcd"),
					"artifact": pulumi.String("oci://ghcr.io/controlplaneio-fluxcd/flux-operator-manifests"),
				},
				"components": pulumi.StringArray{
					pulumi.String("source-controller"),
					pulumi.String("kustomize-controller"),
					pulumi.String("helm-controller"),
					pulumi.String("notification-controller"),
					pulumi.String("image-reflector-controller"),
					pulumi.String("image-automation-controller"),
				},
				"cluster": pulumi.Map{
					"type":          pulumi.String("kubernetes"),
					"multitenant":   pulumi.Bool(false),
					"networkPolicy": pulumi.Bool(true),
					"domain":        pulumi.String("cluster.local"),
				},
				"kustomize": pulumi.Map{
					"patches": pulumi.Array{
						pulumi.Map{
							"target": pulumi.Map{
								"kind": pulumi.String("Deployment"),
								"name": pulumi.String("(kustomize-controller|helm-controller)"),
							},
							"patch": pulumi.Array{
								pulumi.Map{
									"op":    pulumi.String("add"),
									"path":  pulumi.String("/spec/template/spec/containers/0/args/-"),
									"value": pulumi.String("--concurrent=10"),
								},
								pulumi.Map{
									"op":    pulumi.String("add"),
									"path":  pulumi.String("/spec/template/spec/containers/0/args/-"),
									"value": pulumi.String("--requeue-dependency=5s"),
								},
							},
						},
					},
				},
			},
		})
		if err != nil {
			return err
		}

		_, err = apiv1.NewCustomResource(ctx, "example-kafka-node-pool", &apiv1.CustomResourceArgs{
			ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
			Kind:       pulumi.String("KafkaNodePool"),
			Metadata: &metav1.ObjectMetaArgs{
				Name:      pulumi.String("example-kafka-node-pool"),
				Namespace: pulumi.String("kafka"),
				Labels: pulumi.StringMap{
					"strimzi.io/cluster": pulumi.String("example-kafka-cluster"),
				},
			},
			OtherFields: k8s.UntypedArgs{
				"replicas": pulumi.Int(1),
				"roles": pulumi.StringArray{
					pulumi.String("controller"),
					pulumi.String("broker"),
				},
				"storage": pulumi.Map{
					"type": pulumi.String("ephemeral"),
				},
			},
		})
		if err != nil {
			return err
		}

		_, err = apiv1.NewCustomResource(ctx, "example-kafka-cluster", &apiv1.CustomResourceArgs{
			ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
			Kind:       pulumi.String("Kafka"),
			Metadata: &metav1.ObjectMetaArgs{
				Name:      pulumi.String("example-kafka-cluster"),
				Namespace: pulumi.String("kafka"),
				Annotations: pulumi.StringMap{
					"strimzi.io/kraft":      pulumi.String("enabled"),
					"strimzi.io/node-pools": pulumi.String("enabled"),
				},
			},
			OtherFields: k8s.UntypedArgs{
				"kafka": pulumi.Map{
					"replicas": pulumi.Int(1),
					"version":  pulumi.String("3.8.0"),
					"storage": pulumi.Map{
						"type": pulumi.String("ephemeral"),
					},
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
					"config": pulumi.Map{
						"offsets.topic.replication.factor":         pulumi.Int(1),
						"transaction.state.log.replication.factor": pulumi.Int(1),
						"transaction.state.log.min.isr":            pulumi.Int(1),
						"default.replication.factor":               pulumi.Int(1),
						"min.insync.replicas":                      pulumi.Int(1),
					},
				},
				"entityOperator": pulumi.Map{
					"topicOperator": pulumi.Map{},
					"userOperator":  pulumi.Map{},
				},
			},
		})
		if err != nil {
			return err
		}

		_, err = apiv1.NewCustomResource(ctx, "example-kafka-topic", &apiv1.CustomResourceArgs{
			ApiVersion: pulumi.String("kafka.strimzi.io/v1beta2"),
			Kind:       pulumi.String("KafkaTopic"),
			Metadata: &metav1.ObjectMetaArgs{
				Name:      pulumi.String("example-kafka-topic"),
				Namespace: pulumi.String("kafka"),
				Labels: pulumi.StringMap{
					"strimzi.io/cluster": pulumi.String("example-kafka-cluster"),
				},
			},
			OtherFields: k8s.UntypedArgs{
				"partitions": pulumi.Int(5),
				"replicas":   pulumi.Int(1),
				"config": pulumi.Map{
					"retention.ms":  pulumi.Int(7200000),
					"segment.bytes": pulumi.Int(1073741824),
				},
			},
		})
		if err != nil {
			return err
		}

		return nil
	})
}
