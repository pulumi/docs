---
title: "How to deploy Apache Kafka on Amazon MSK"
allow_long_title: true
meta_desc: "Learn about Apache Kafka deployment on Amazon MSK with our Pulumi example. Perfect for DevOps and developers managing Kafka clusters daily."
type: ai-answers
date: 2023-07-24
---

Apache Kafka is a popular open-source distributed event streaming platform used for building real-time data pipelines and streaming applications. In many cases, managing and scaling Kafka clusters can be a complex task. However, with the help of Amazon Managed Streaming for Kafka (Amazon MSK), the process becomes much simpler and more efficient.

In this article, we will explore how to deploy Apache Kafka on Amazon MSK using Pulumi. We will walk through a sample Pulumi program that deploys an Apache Kafka cluster on Amazon MSK, and discuss important concepts along the way.

### Prerequisites

Before we dive into the Pulumi program, there are a few prerequisites we need to take care of:

1. Pulumi CLI: Make sure you have the Pulumi CLI installed on your local machine. You can download it from the official [Pulumi website](https://www.pulumi.com/docs/get-started/install/).

2. AWS Account: You'll need an AWS account to provision resources on Amazon MSK. If you don't have an AWS account yet, you can create one for free on the [AWS website](https://aws.amazon.com/).

3. AWS Credentials: Configure your AWS credentials on your local machine. You can do this by either setting environment variables for AWS access key and secret access key, or by using the AWS CLI's `aws configure` command. Make sure the credentials you use have sufficient permissions to create and manage resources on Amazon MSK.

Now that we have the prerequisites covered, let's dive into the Pulumi program.

### Writing the Pulumi Program

To deploy Apache Kafka on Amazon MSK using Pulumi, we'll be using the `aws.msk.Cluster` resource from the Pulumi AWS package. The `aws.msk.Cluster` resource allows us to define the configuration of our Kafka cluster.

Here's a sample Pulumi program that deploys an Apache Kafka cluster on Amazon MSK:

```java
import com.pulumi.*;
import com.pulumi.aws.msk.Cluster;

public class KafkaStack extends Stack {
    public KafkaStack() {
        Cluster kafkaCluster = new Cluster("example-kafka-cluster", new ClusterArgs()
            .setBrokerNodeGroupInfo(new ClusterArgs.BrokerNodeGroupInfoArgs()
                .setAzDistribution("DEFAULT")
                .setClientSubnets(new String[]{"subnet-abc01234", "subnet-def56789"})
                .setInstanceType("kafka.m5.large")
                .setEbsVolumeSize(1))
            .setKafkaVersion("2.7.0")
            .setNumberOfBrokerNodes(3));

        this.export("kafkaClusterArn", kafkaCluster.getArn());
        this.export("kafkaClusterZookeeperConnectString", kafkaCluster.getZookeeperConnectString());
    }
}
```

In this program, we create an instance of the `Cluster` class and pass in the necessary arguments to configure our Kafka cluster. Let's break down the important parts of this program:

- `Cluster`: We create an instance of the `Cluster` class from `aws.msk` package by passing the desired cluster name and a `ClusterArgs` object.

- `BrokerNodeGroupInfoArgs`: We define the configuration for the broker node group using the `setBrokerNodeGroupInfo` method, which is an instance of `ClusterArgs.BrokerNodeGroupInfoArgs` class. Here, we set the availability zone distribution, client subnets, instance type, and EBS volume size. You should replace the subnet IDs (`"subnet-abc01234"` and `"subnet-def56789"`) with the actual subnet IDs you want to use.

- `setKafkaVersion`: We set the desired Kafka version for our cluster. In this example, we set it to `2.7.0`, but you can choose the version that suits your needs.

- `setNumberOfBrokerNodes`: We specify the number of broker nodes we want in our Kafka cluster. In this sample program, we set it to `3`, but you can adjust this number based on your requirements.

- `export`: We use the `export` method to export the ARN and Zookeeper connect string of the created Kafka cluster. This allows us to easily retrieve these values after the stack is deployed and use them in other parts of our infrastructure.

With the Pulumi program written, we are ready to deploy our Apache Kafka cluster on Amazon MSK.

### Deploying the Apache Kafka Cluster

To deploy the Apache Kafka cluster on Amazon MSK, follow these steps:

1. Create a new directory for your Pulumi project and navigate into it:

   ```bash
   mkdir kafka-pulumi
   cd kafka-pulumi
   ```

2. Initialize a new Pulumi project using the following command:

   ```bash
   pulumi new aws-java --name kafka
   ```

3. Replace the auto-generated files with the `KafkaStack.java` file featuring our Kafka cluster configuration.

4. Install the necessary Pulumi packages for AWS:

   ```bash
   npm install @pulumi/aws
   ```

5. Run the following command to provision the Apache Kafka cluster on Amazon MSK:

   ```bash
   pulumi up
   ```

   This command will display a preview of the resources that will be created and ask for confirmation to proceed. Review the changes and enter `yes` to proceed with the deployment.

After the deployment is complete, you will see the ARN and Zookeeper connect string of the deployed Apache Kafka cluster in the output. You can use these values to connect to your cluster and start using it to build real-time data pipelines and streaming applications.

### Conclusion

In this article, we explored how to deploy Apache Kafka on Amazon MSK using Pulumi. We walked through a sample Pulumi program that deploys an Apache Kafka cluster on Amazon MSK. By leveraging the power of Pulumi and the Pulumi AWS package, we can easily provision Apache Kafka clusters and integrate them into our infrastructure as code.

Remember, this is just a sample program to get you started. In a production environment, you may need to configure additional properties such as encryption, VPC settings, monitoring, and more. For more details on configuring the `aws.msk.Cluster` resource, refer to the [Pulumi Resource documentation](https://www.pulumi.com/docs/reference/pkg/aws/msk/cluster/).
