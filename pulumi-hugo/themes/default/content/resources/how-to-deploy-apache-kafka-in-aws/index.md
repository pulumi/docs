---
title: "How to deploy Apache Kafka on Amazon MSK"
allow_long_title: true
meta_desc: "Learn about Apache Kafka deployment on Amazon MSK with our Pulumi example. Perfect for DevOps and developers managing Kafka clusters daily."
type: ai-answers
date: 2023-07-24
---

For deploying Apache Kafka, I would suggest using the Amazon Managed Streaming for Kafka (Amazon MSK) service. The Pulumi AWS package enables us to use aws.msk.Cluster to accomplish this task.

For the demonstration purposes, I'll deploy a simple MSK cluster with some of the required properties filled. For the actual program, please make sure to use production-ready configurations.

```java

import com.pulumi.*;
import com.pulumi.aws.msk.Cluster;
import com.pulumi.aws.mskBrokerNodeGroupInfoArgs;

public class KafkaStack extends Stack {
    public KafkaStack() {
        Cluster kafkaCluster = new Cluster("example-kafka-cluster", new ClusterArgs
            .BrokerNodeGroupInfoArgs()
            .setAzDistribution("DEFAULT")
            .setClientSubnets(new String[]{"subnet-abc01234", "subnet-def56789"})
            .setInstanceType("kafka.m5.large");
            .setEbsVolumeSize(1(new String[]{"sg-123456"})
        .setKafkaVersion("1.1.1")
        .setNumberOfBrokerNodes(2));

        this.export("kafkaClusterArn", kafkaCluster.arn);
        this.export("kafkaClusterZookeeperConnectString", kafkaCluster.zookeeperConnectString);
    }
}


```

In this program, we're creating an Apache Kafka cluster in MSK using Cluster from aws.msk. Please replace "sg-123456", "subnet-abc01234", "subnet-def56789" with your actual security group ID and the subnets you wish to use.

After creating the cluster, the ARN of the cluster and Zookeeper connect string are exported as stack outputs.

This program uses the [aws.msk.Cluster resource](https://www.pulumi.com/registry/packages/aws/api-docs/msk/cluster/)

Please note that this is just a simple example. For a production-grade setup, you may need to configure many more properties such as encryption, VPC settings, monitoring, and more. For these options please refer to the Resource documentation above.

Remember to run pulumi up to apply the changes after setting the appropriate AWS credentials.
