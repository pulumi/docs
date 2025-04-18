---
title: "How to Manage Kafka Clusters in Confluent Cloud with Pulumi"
date: 2023-02-15
updated: 2025-03-26
meta_desc: Learn how to manage Confluent Kafka clusters with Pulumi—create topics, service accounts, and secure infrastructure using real code with IaC best practices.
meta_image: "managing-confluent-clusters.png"
authors: ["josh-kodroff"]
tags: ["confluent", "kafka"]
---

Event streaming is used across diverse industries that demand real-time data processing. Apache Kafka is the most popular open-source streaming platform. Confluent Cloud lets you run Kafka on the cloud provider of your choice.

In this blog post, you'll use the [Confluent Cloud Pulumi provider](https://www.pulumi.com/registry/packages/confluentcloud/) and Pulumi to create a Kafka cluster, topic, and customer account.

1. [About Apache Kafka and Confluent Cloud](/blog/create-manage-confluent-kafka-cluster-with-pulumi/#about-apache-kafka-and-confluent-cloud)
2. [Initializing the Project](/blog/create-manage-confluent-kafka-cluster-with-pulumi/#initializing-the-project)
3. [Adding Resources](/blog/create-manage-confluent-kafka-cluster-with-pulumi/#adding-resources)
4. [Testing Kafka Cluster](/blog/create-manage-confluent-kafka-cluster-with-pulumi/#testing-kafka-cluster)
5. [See it in action](/blog/create-manage-confluent-kafka-cluster-with-pulumi/#see-it-in-action)
6. [Conclusion](/blog/create-manage-confluent-kafka-cluster-with-pulumi/#conclusion)
7. [Additional Resources](/blog/create-manage-confluent-kafka-cluster-with-pulumi/#additional-resources)

## About Apache Kafka and Confluent Cloud

### What is Apache Kafka?

[Apache Kafka](https://kafka.apache.org/) is an event store and stream-processing platform, used by more than 30% of the Fortune 500 today. Using Kafka streams, developers can write modern, event-driven applications for real-time data streaming and processing. Kafka is used across many industries, including gaming, financial services, healthcare, retail, automotive, and manufacturing.

Kafka was created to allow scalable high-throughput applications to store, analyze, and reprocess streaming data. However, managing Kafka clusters can require significant operational expertise, leading many organizations to look for a managed solution.

### What is Confluent Cloud?

[Confluent Cloud](https://docs.confluent.io/cloud/current/get-started/pulumi-provider.html) provides managed Kafka clusters along with major value-add features such as elasticity, integrated security, stream governance, and improved monitoring. Clusters can be provisioned in AWS, Azure, or Google Cloud to reduce network latency and egress charges. Confluent Cloud also offers [cluster linking capabilities](https://docs.confluent.io/platform/current/multi-dc-deployments/cluster-linking/overview.html) to on-prem producers and consumers for hybrid cloud scenarios.

Using Pulumi, you can manage your Confluent resources and maximize your organization's ability to quickly ship modern, secure, event-driven workloads.

## Initializing the Project

Before you can add Confluent resources to your Pulumi program, you'll need to ensure you have a Confluent Cloud account and an API key. You can [sign up for a free trial of Confluent Cloud](https://www.confluent.io/get-started/) if you do not already have a Confluent Cloud account. [Create an API key](https://docs.confluent.io/cloud/current/access-management/authenticate/api-keys/api-keys.html#create-a-cloud-api-key) and set its values as environment variables:

```bash
export CONFLUENT_CLOUD_API_KEY=<your API key>
export CONFLUENT_CLOUD_API_SECRET=<your API secret>
```

Now you can create a new directory and initialize the Pulumi program:

```bash
mkdir confluent-blog-post
cd confluent-blog-post
pulumi new typescript
```

After a few seconds, the Pulumi program has been initialized. Next, you'll need to add a reference to the Pulumi Confluent provider:

```bash
npm i @pulumi/confluentcloud
```

Finally, you'll need to add a reference to the top of the scaffolded `index.ts` file:

```typescript
import * as confluent from "@pulumi/confluentcloud";
```

Now you're ready to create and manage Confluent resources!

## Adding Resources

Your example architecture will have the following components:

- A Kafka cluster for our messages ("inventory").
- An admin service account which you'll use to create objects within the cluster (topics and users).
- A Kafka topic for our cluster, which will hold our sample messages.
- A producer service account, which you'll use to write messages to the topic.
- A consumer service account, which you'll use to read messages from the topic.

You'll be keeping all of your resources in a single file: `index.ts`.

The first resource you'll need to create is a Confluent environment which is a container for the other Confluent resources you'll be creating:

```typescript
const env = new confluent.Environment("environment", {
    displayName: "pulumi-confluent-blog",
});
```

Next, you'll create a standard Kafka cluster. A couple notes about the cluster you're creating:

1. The cluster is a single-zone cluster for cost reasons, but if you're creating a cluster for production scenarios you'll likely want to use the `MULTI_ZONE` option for `availability`.
1. While this cluster is in AWS' us-east-2 region, Confluent Cloud also supports Azure and Google Cloud as well as other regions within AWS. For a full list of supported options for the `cloud` and `region` attributes, see [Cloud Providers and Regions for Confluent Cloud](https://docs.confluent.io/cloud/current/clusters/regions.html#cloud-providers-and-regions).

Add the following code to your Pulumi program:

```typescript
const cluster = new confluent.KafkaCluster("cluster", {
    displayName: "inventory",
    availability: "SINGLE_ZONE",
    cloud: "AWS",
    region: "us-east-2",
    environment: {
        id: env.id,
    },
    standard: {}
});
```

Next, you'll need to create the admin-level service account you'll use to create our Kafka topic and our producer and consumer accounts. This app manager account is similar to the "DBA" account you may be familiar with in relational databases or the root account in Linux:

```typescript
const serviceAccount = new confluent.ServiceAccount("app-manager", {
    description: "Service account to manage 'inventory' Kafka cluster",
});

const roleBinding = new confluent.RoleBinding("app-manager-kafka-cluster-admin", {
    principal: pulumi.interpolate`User:${serviceAccount.id}`,
    roleName: "CloudClusterAdmin",
    crnPattern: cluster.rbacCrn,
});

const managerApiKey = new confluent.ApiKey("app-manager-kafka-api-key", {
    displayName: "app-manager-kafka-api-key",
    description: "Kafka API Key that is owned by 'app-manager' service account",
    owner: {
        id: serviceAccount.id,
        kind: serviceAccount.kind,
        apiVersion: serviceAccount.apiVersion,
    },
    managedResource: {
        id: cluster.id,
        apiVersion: cluster.apiVersion,
        kind: cluster.kind,
        environment: {
            id: env.id,
        },
    }
}, {
    dependsOn: roleBinding
});
```

Next, you'll create your Kafka topic using the cluster admin service account credentials you just created (see the `credentials` input in the following code):

```typescript
const topic = new confluent.KafkaTopic("orders", {
    kafkaCluster: {
        id: cluster.id,
    },
    topicName: "orders",
    restEndpoint: cluster.restEndpoint,
    credentials: {
        key: managerApiKey.id,
        secret: managerApiKey.secret,
    },
});
```

Now that you have your topic, you need to create a producer service account and give that account permissions to write to the topic, again using the credentials of your cluster admin account:

```typescript
const producerAccount = new confluent.ServiceAccount("producer", {
    description: "Service account to produce to 'orders' topic of 'inventory' Kafka cluster",
});

const producerApiKey = new confluent.ApiKey("producer-api-key", {
    owner: {
        id: producerAccount.id,
        kind: producerAccount.kind,
        apiVersion: producerAccount.apiVersion,
    },
    managedResource: {
        id: cluster.id,
        apiVersion: cluster.apiVersion,
        kind: cluster.kind,
        environment: {
            id: env.id,
        },
    },
});

new confluent.KafkaAcl("app-producer-write", {
    kafkaCluster: {
        id: cluster.id,
    },
    resourceType: "TOPIC",
    resourceName: topic.topicName,
    patternType: "LITERAL",
    principal: pulumi.interpolate`User:${producerAccount.id}`,
    host: "*",
    operation: "WRITE",
    permission: "ALLOW",
    restEndpoint: cluster.restEndpoint,
    credentials: {
        key: managerApiKey.id,
        secret: managerApiKey.secret,
    }
});
```

Now you create our consumer account which will read messages from your Kafka topic. It's created similarly to the producer:

```typescript
const consumerAccount = new confluent.ServiceAccount("consumer", {
    description: "Service account to consume from 'orders' topic of 'inventory' Kafka cluster",
});

const consumerApiKey = new confluent.ApiKey("consumer-api-key", {
    owner: {
        id: consumerAccount.id,
        kind: consumerAccount.kind,
        apiVersion: consumerAccount.apiVersion,
    },
    managedResource: {
        id: cluster.id,
        apiVersion: cluster.apiVersion,
        kind: cluster.kind,
        environment: {
            id: env.id,
        },
    },
});

new confluent.KafkaAcl("consumer-read-topic-acl", {
    kafkaCluster: {
        id: cluster.id,
    },
    resourceType: "TOPIC",
    resourceName: topic.topicName,
    patternType: "LITERAL",
    principal: pulumi.interpolate`User:${consumerAccount.id}`,
    host: "*",
    operation: "READ",
    permission: "ALLOW",
    restEndpoint: cluster.restEndpoint,
    credentials: {
        key: managerApiKey.id,
        secret: managerApiKey.secret,
    }
});

new confluent.KafkaAcl("consumer-read-group-acl", {
    kafkaCluster: {
        id: cluster.id,
    },
    resourceType: "GROUP",
    resourceName: "confluent_cli_consumer_",
    patternType: "PREFIXED",
    principal: pulumi.interpolate`User:${consumerAccount.id}`,
    host: "*",
    operation: "READ",
    permission: "ALLOW",
    restEndpoint: cluster.restEndpoint,
    credentials: {
        key: managerApiKey.id,
        secret: managerApiKey.secret,
    }
});
```

Finally, add some Pulumi stack outputs. Stack outputs allow you to access values from your Pulumi program in two ways:

1. Via [stack references](https://www.pulumi.com/learn/building-with-pulumi/stack-references/) in other Pulumi programs, which you won't use in this blog tutorial.
1. From the command line via the `pulumi stack output` command, which you will use to test your Kafka cluster.

The syntax for Pulumi stack outputs varies by language, but in TypeScript programs they are accomplished by a simple `export` statement:

```typescript
export const ordersTopicName = topic.topicName;
export const environmentId = env.id;
export const clusterId = cluster.id;

export const producerApiKeyId = producerApiKey.id;
export const producerApiKeySecret = producerApiKey.secret;

export const consumerApiKeyId = consumerApiKey.id;
export const consumerApiKeySecret = consumerApiKey.secret;
```

Your Pulumi program is now complete! You can deploy our infrastructure by running the following command:

```bash
pulumi up
```

After a short wait, your cluster is up and running, and you are ready to test your infrastructure!

## Testing Kafka Cluster

To simulate your producer and consumer, you can use the [Confluent CLI](https://docs.confluent.io/confluent-cli/current/overview.html) to send messages to and read messages from your topic. You will use the values of your Pulumi stack outputs to formulate the command.

{{% notes type="info" %}}
Make sure you run the `confluent login` command first if you have not yet done so. At the time of writing, failure to do so will lead to misleading error messages from the Confluent CLI. The `confluent login` command will need to be run periodically as the token it generates expires after a few hours.
{{% /notes %}}

To simulate a message producer, you can send messages to your Kafka topic with the following command:

```bash
confluent kafka topic produce $(pulumi stack output ordersTopicName) \
  --environment $(pulumi stack output environmentId) \
  --cluster $(pulumi stack output clusterId) \
  --api-key $(pulumi stack output producerApiKeyId) \
  --api-secret "$(pulumi stack output producerApiKeySecret --show-secrets)"
```

You can enter a few sample records like the following and then press `Ctrl-C` when you're done to exit:

```json
{"number":1,"date":18500,"shipping_address":"899 W Evelyn Ave, Mountain View, CA 94041, USA","cost":15.00}
{"number":2,"date":18501,"shipping_address":"1 Bedford St, London WC2E 9HG, United Kingdom","cost":5.00}
{"number":3,"date":18502,"shipping_address":"3307 Northland Dr Suite 400, Austin, TX 78731, USA","cost":10.00}
```

To simulate your consumer and read the records you just wrote, you can enter the following command:

```bash
$ confluent kafka topic consume $(pulumi stack output ordersTopicName) \
  --from-beginning \
  --environment $(pulumi stack output environmentId) \
  --cluster $(pulumi stack output clusterId) \
  --api-key $(pulumi stack output consumerApiKeyId) \
  --api-secret $(pulumi stack output consumerApiKeySecret --show-secrets)
```

You should see the events you entered as the producer:

```json
Starting Kafka Consumer. Use Ctrl-C to exit.
{"number":3,"date":18502,"shipping_address":"3307 Northland Dr Suite 400, Austin, TX 78731, USA","cost":10.00}
{"number":1,"date":18500,"shipping_address":"899 W Evelyn Ave, Mountain View, CA 94041, USA","cost":15.00}
{"number":2,"date":18501,"shipping_address":"1 Bedford St, London WC2E 9HG, United Kingdom","cost":5.00}
```

The producer is able to write events to your topic, and the consumer is able to read them. Your architecture has been proven to work!

## See it in action

Want to see this in action? Here is a [Modern Infrastructure video](https://www.youtube.com/playlist?list=PLyy8Vx2ZoWloyj3V5gXzPraiKStO2GGZw) demonstrating everything discussed in this blog post:

{{< youtube "NWm9kAzQGXY?rel=0" >}}
<div>
    <div class="accordion-item text-2xl py-3 border-b-2 border-t-2">
        <input type="checkbox" class="absolute hidden" id="Transcript" />
        <label for="Transcript" class="accordion-label">
            <h5 class="mt-2 w-2/3">Video Transcript</h5>
            <div class="flex flex-grow justify-end items-center">
                <span class="closed-accordion">+</span>
                <span class="open-accordion hidden">-</span>
            </div>
        </label>
        <div class="accordion-item-body-no-animation text-base">
            <p>
                Hello, and welcome to another episode of Modern Infrastructure Wednesday. I’m your host, Lee Zen, and today we’re going to be covering how easy it is to use Pulumi to deploy an application using AWS App Runner. App Runner is a new service from Amazon that lets you deploy a container image or a source code repository as an application without having to do too much configuration. You don’t have to configure load balancers or any of the typical stuff you usually have to set up. Here, you can see I’m running the main.go file, and it’s going to create all the necessary resources, along with, finally, the App Runner service.
            </p>
            <p>
We’re going to dive into all the source code to explain how this works, but right now you can see what’s happening: we’re actually doing the Docker build that’s going to publish the image. After the Docker build completes, it’s pushing the image into our ECR repository. Finally, you can see here the update succeeds, and we actually get the service URL. Now let’s go take a look at our service. While the service is updating, you’ll notice it takes a little bit of time—not too much—but just a little bit to get going.
            </p>
            <p>
Now we’re going to see how our code actually works. Let’s look at our deployment.go file, which main.go actually calls. We’ve built an Automation API-based program, and as you can see in the outputs, we create the image and various other resources. Let’s take a closer look at the code: the first thing we do is create an ECR repository using auto-naming, so it automatically generates the name. Next, we create a role so that App Runner can pull the image from our repository. We create this role and give it the appropriate policy. Afterward, we publish our image. You can see here we have the image resource, and there we feed it the repository credentials. Let’s also take a quick look at the Dockerfile we’re building—it’s just copying an index.html file over, making it a very simple setup.
            </p>
            <p>
That’s really all there is to the infrastructure—it’s super simple. If we look at the Automation API side of things, all we’re doing is the usual Automation API stuff: setting up a stack and deploying our program. Right here, we point out where we’re deploying the program. Once we’ve finished deploying, we’re going to use the outputs from that program—namely, the image URL and the access role—and we’ll feed those to App Runner. This will invoke the Create Service API call, which is what’s actually doing the work. Going back to the console, you can now see we have the app running, and voilà, exactly what we expected to see! Hopefully, you enjoyed this demo. Like I said, it’s just so easy to get everything running with App Runner in just a few simple lines of code and Pulumi. Thanks for watching, and have a great day!
            </p>
        </div>
    </div>
</div>

## Conclusion

By combining the operational simplicity and rich functionality of Confluent Cloud with the power of [Pulumi's infrastructure as code](https://www.pulumi.com/product/) platform to manage Confluent resources using real programming languages, organizations can quickly and securely deploy Apache Kafka clusters.

No matter whether your organization is using data streaming today or looking to adopt it in the future, using Confluent Cloud with Pulumi will allow your organization to quickly spin up and manage Kafka infrastructure so you can focus on what really matters: delivering value to customers and stakeholders.

## Additional Resources

Watch Collin James, Engineering Leader, and Software Architect at Dutchie, describe how a small team has [enabled Kafka adoption by creating a monorepo of Pulumi projects that manage resources on Confluent Cloud](https://www.pulumi.com/resources/enabling-kafka-adoption-pulumi-and-confluent-cloud/).
