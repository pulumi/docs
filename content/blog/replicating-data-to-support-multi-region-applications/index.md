---
title: "Replicating Data to Support Multi-Region Applications"
date: 2023-12-27T11:03:10Z
draft: false
meta_desc: Learn about the tradeoffs in distributed databases and data replication when using them for multi-region applications.
meta_image: meta.png
authors:
    - adora-nwodo
tags:
    - multi-region-databases
    - data-replication
    - cloud-deployment
    - distributed-systems
    - geographic-distribution
    - high-availability

---

In [the previous article](/blog/scaling-apps-across-multiple-regions/), we covered multi-region scaling, its importance, and how you can use Pulumi stacks to represent multiple regions and environments. The big takeaway from that article is that scaling your application across multiple regions is an important architectural decision to enable scalability and availability, but it comes with its own set of considerations. One of these considerations is around the data that your application needs or uses. Data replication is typically necessary in multi-region architectures because if you have multiple application instances worldwide making calls to just one database instance, the latency of your application will be high. After all, it will take a long time for that database instance to perform data operations and send back a result to the user through the application. Some requests might have repeated timeouts. In this article, we will cover data replication in multi-region applications and how it plays a pivotal role in distributed systems.

## Why is data replication important?

In almost every instance of using multi-region scaling with an application, data replication becomes imperative for a few different reasons:

- **Latency reduction:** Replicating data closer to end users minimizes data access latency, providing a seamless and responsive user experience.

- **Availability:** When data is distributed across different locations, applications may be able to remain  available even when there are regional outages or disruptions. There are some architectural/design decisions around this that we’ll discuss in the next section, but generally speaking a globally distributed approach creates redundancy. This means that if one region experiences an outage, application users can still access data from alternative locations.

- **Load balancing:** Data replication enables effective load balancing. To minimize overload on a single server or region, traffic can be distributed among numerous replicas, optimizing resource utilization and boosting overall system performance.

## Data Replication and the CAP Theorem

Any discussion of data replication among multiple regions invariably needs to address [the CAP theorem](https://en.wikipedia.org/wiki/CAP_theorem). In a nutshell, the CAP theorem (also known as Brewer’s theorem) states that a distributed data store can only provide two of three guarantees: consistency, availability, and partition tolerance. Generally, these three guarantees are defined in this way:

- **Consistency – all clients always have the same view of the data:** Choosing strong consistency assures that all clients, regardless of their geographical location in the distributed system, see the same data. However, the pursuit of uniformity frequently results in increased latency, particularly when dealing with low bandwidth and/or high latency networks.

- **Availability – all clients can always read and write the data:** Prioritizing high availability means that the system responds to client read and write requests even in the event of network partitions. Accepting eventual consistency and accepting some transient divergence among replicas may be required to achieve availability.

- **Partition Tolerance – the system will continue to work despite partitions:** Partition tolerance is non-negotiable in cloud computing, when systems span numerous regions and components are distributed. It ensures that the system continues to function even in the face of physical partitions or network outages, but doing so will require strategic compromises in terms of consistency or availability.

To reiterate, application and infrastructure architects have no choice but to tolerate network partitioning, as networks outside their control or influence—either the cloud provider’s network or the internet or both—typically fall in the replication path. Therefore, application and infrastructure architects have to choose the behavior of the data store when (not if) network partitioning occurs:

- Does the data store cancel the operation, preserving consistency but affecting availability?

- Does the data store proceed with the operation, prioritizing availability at the cost of consistency?

As mentioned earlier, though, more than just network partitioning comes into play here. Network bandwidth affects the balance between preserving consistency or optimizing for availability in the context of multi-region applications. Network configurations also come into play; what impact will a larger MTU (Maximum Transmission Unit) have on data replication? Decisions here are full of trade-offs. For example, prioritizing replication speed to ensure data consistency across regions may lead to increased latency, affecting the system's ability to meet stringent availability requirements. An extension to the CAP theorem, known as [PACELC](https://en.wikipedia.org/wiki/PACELC_theorem), captures the trade-off between latency and consistency even when network partitions aren’t present.

Therefore, the challenge lies in finding the right balance. Striking a compromise between data consistency and system performance (in the form of availability) is a delicate task requiring a careful analysis of the principles of the CAP theorem, guiding system architects in making informed choices that align with the specific needs and priorities of their distributed applications.

## Using Pulumi to configure data replication

Now that you’ve seen the impact of CAP theorem-related decisions on distributed data stores and the applications that use them, let’s take a look at a specific example. Let’s say you are building a distributed system and you want to have a central database with multiple replicas across the different availability zones (or regions) where your application will be deployed.

Cloud providers such as Azure, AWS, and Google Cloud all have databases that offer multi-region capabilities (AWS has DynamoDB, Azure has Cosmos DB, and Google Cloud has Cloud Spanner). Thanks to Pulumi’s integration with a variety of cloud providers, including (but not limited to) Azure, AWS, and Google Cloud, you can use Pulumi to deploy instances of these multi-region databases in your preferred programming language. This allows you to take advantage of these offerings and still reap the benefits of using infrastructure as code with Pulumi.

Let's look at an example of using Pulumi to define an Azure Cosmos DB account with multi-region replication:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure-native";

const resourceGroup = new azure.resources.ResourceGroup("myResourceGroup");

const cosmosDbAccount = new azure.documentdb.DatabaseAccount("myCosmosDbAccount", {
    resourceGroupName: resourceGroup.name,
    location: resourceGroup.location,
    locations: [
        { locationName: "East US" },
        { locationName: "West US" },
        // Add additional Azure regions for replication
    ],
    databaseAccountOfferType: "Standard",
    consistencyPolicy: {
        defaultConsistencyLevel: "Session",
    },
});
```

In this example, the `locations` parameter is used to specify the Azure regions where Cosmos DB replicas will be deployed, enabling global data distribution. Aligning these locations with the locations where your application code is deployed allows you to minimize latency due to reading from the database.

Additionally, you can also enable multi-region writes. This is typically useful for write-active scenarios, ensuring that write operations can be directed to any region with a writable replica, and can reduce latency associated with writes to the database. This reduction in write latency often translates directly into improved performance for a multi-region application.

```typescript
const cosmosDbAccount = new azure.documentdb.DatabaseAccount("myCosmosDbAccount", {
    resourceGroupName: resourceGroup.name,
    … // more code
    enableMultipleWriteLocations: true,
});
```

### Consistency

You will need to choose a consistency level that aligns with your application requirements, such as "Session," "Bounded staleness," "Eventual," "Strong," or "Consistent prefix." [This page](https://learn.microsoft.com/en-us/azure/cosmos-db/consistency-levels) has more details on the different consistency levels, but let’s look at a couple specific configurations.

Recall that strong consistency ensures that all nodes or replicas in the system view the same data simultaneously, regardless of which node they are accessing. In other words, after performing a write operation, any subsequent read action from any node must return the most recent write value. This consistency mode guarantees the linear ordering of processes, and the system behaves like a single, coherent entity. Strong consistency prioritizes consistency over availability in the event of network partition. It also hinders performance as the write must be acknowledged by multiple nodes.

You can prioritize strong consistency by configuring the Azure Cosmos DB account to use the "Strong" consistency level. This ensures that all read and write operations observe the most recent version of the data across all replicas.

```typescript
const cosmosDbAccount = new azure.documentdb.DatabaseAccount("myCosmosDbAccount", {
    resourceGroupName: resourceGroup.name,
    consistencyPolicy: {
        defaultConsistencyLevel: "Strong",
    },
});
```

Cosmos DB also supports tunable consistency. Tunable consistency means that the consistency can be changed for each read and write request. Tunable consistency levels can be used in instances when strict strong consistency is not required. When configured this way, the application now assumes the responsibility for determining the consistency.

This next code snippet shows how to configure the Cosmos DB account with a "Bounded Staleness" consistency level, which allows you to balance consistency and latency based on application requirements.

```typescript
const cosmosDBAccount = new azure.documentdb.DatabaseAccount("myCosmosDB", {
    resourceGroupName: resourceGroup.name,
    consistencyPolicy: {
        // Leverage tunable consistency levels for specific scenarios
        defaultConsistencyLevel: "BoundedStaleness",
        maxStalenessPrefix: 100,
    },
});
```

Now that the responsibility for assigning consistency is with the client, the code snippet below shows how to make API calls with tunable consistency for both reads and writes using Azure Cosmos DB SDK:

```typescript
import { CosmosClient } from "@azure/cosmos";

const endpointUri = "Your_Cosmos_DB_Endpoint_URI";
const primaryKey = "Your_Cosmos_DB_Primary_Key";
const databaseId = "Your_Database_Id";
const containerId = "Your_Container_Id";

const cosmosClient = new CosmosClient({ endpoint: endpointUri, key: primaryKey });
const database = cosmosClient.database(databaseId);
const container = database.container(containerId);

async function writeDocumentWithTunableConsistency() {
    const document = { id: "1", PartitionKey: "MyPartitionKey", Message: "Hello, Cosmos DB!" };

    const requestOptions = {
        consistencyLevel: "BoundedStaleness",
        maxStalenessPrefix: 100,
    };

    await container.items.create(document, requestOptions);

    console.log("Document written with tunable consistency.");
}

async function readDocumentWithTunableConsistency() {
    const documentId = "Your_Document_Id";

    const requestOptions = {
        consistencyLevel: "Eventual",
    };

    const { resource } = await container.item(documentId, "Your_Partition_Key").read(requestOptions);

    console.log(`Document read with tunable consistency. Message: ${resource.Message}`);
}

(async () => {
    await writeDocumentWithTunableConsistency();
    await readDocumentWithTunableConsistency();
})();
```

### Availability

In the context of the CAP and PACELC theorems, availability refers to the guarantee that every request will receive a non-error response—but without the guarantee that it contains the most recent write. As we’ve discussed throughout this article, when dealing with distributed data stores this means navigating the trade-offs between consistency and availability. If you opt for solid consistency then you ensure uniform data views but you reduce availability during partitions. If you opt to prioritize availability, then you have no choice but to deal with consistency issues.

This tradeoff becomes especially relevant when uninterrupted system availability is necessary, such as high-traffic applications or systems with stringent service level agreements (SLAs).

It’s also important to understand that availability is not the same as fault tolerance, especially in a CAP theorem context. Going back to our example of using multiple Cosmos DB replicas to support a multi-region application, Cosmos DB (as shown earlier) absolutely supports placing replicas in different availability zones or different regions. This enables cross-region replication, ensuring that the data exists in multiple locations. In the event one of these locations fails or becomes unreachable or inoperable, the application can tolerate this fault (meaning the application isn’t necessarily completely down and there is little or no data loss) but availability may still be impacted. For example, choosing to prioritize consistency over availability means that when this fault occurs the database may block, restrict, or delay operations until the fault is resolved.

So how does one tune availability with a distributed data store? Consistency and availability are two sides of the same coin; adjusting consistency affects availability. With Cosmos DB, you tune availability by adjusting the consistency settings on the database instance. If you opt for strict consistency, then availability is impacted; if you opt for a less strict consistency level, then availability is not impacted as much (or not at all).

Here’s how to configure CosmosDB to prioritize availability:

```typescript
const cosmosDbAccount = new azure.documentdb.DatabaseAccount("myCosmosDbAccount", {
    resourceGroupName: resourceGroup.name,
    location: resourceGroup.location,
    locations: [
        { locationName: "East US" },
        { locationName: "West US" },
        // Add additional Azure regions for replication
    ],
    consistencyPolicy: {
        defaultConsistencyLevel: "Eventual",
    },
    enableAutomaticFailover: true,
});
```

When prioritizing availability, you might choose to use a default consistency level of “Eventual,” as shown in the example above. Eventual consistency prioritizes high availability by enabling updates to propagate gradually across replicas. While it has decreased read latency, it accepts temporary inconsistencies that resolve over time. As you might expect, your application will need to be prepared to deal with these temporary inconsistencies.

A more balanced option is called “BoundedStaleness.” This choice introduces staleness in read operations, allowing for better availability during network partitions. "BoundedStaleness" provides a controlled staleness window (maxStalenessPrefix), enabling developers to fine-tune the balance between consistency and availability. Bounded Staleness offers a sort of middle ground, allowing users to define a controlled maximum lag for read operations and therefore ensuring a specified level of consistency while maintaining availability during network partitions. This model suits scenarios where a compromise between consistency and availability is necessary, and the application can tolerate a defined level of data staleness.

Your application's requirements influence the decision between these options.

By also enabling `enableAutomaticFailover`, the code ensures that Cosmos DB automatically performs failover in the event of a regional or node failure. Automatic failover improves availability by redirecting traffic to healthy instances and minimizing downtime during unexpected disruptions.

### Partition tolerance

Partition tolerance isn’t a tunable/configurable parameter. Application and infrastructure architects need to accept that network partitions will occur, and instead need to configure the data store to behave in an expected fashion (either prioritizing consistency at the expense of availability, or prioritizing availability at the cost of consistency).

The CAP theorem posits that, during network partitions, a system must make a trade-off between consistency and availability. In Cosmos DB, tweaking the consistency level influences data presentation to clients. Opting for solid consistency ensures uniform data views but may reduce availability during partitions. Conversely, prioritizing availability over consistency allows for continuous operation, even with potential data discrepancies. High consistency levels may result in increased latency and reduced availability during partitions, while prioritizing availability ensures responsiveness, even in partitioned scenarios.

Understanding these trade-offs is crucial for designing resilient systems. It allows for informed decisions about the system's behavior during network partitions, ultimately contributing to effectively managing partition tolerance in distributed systems and databases.

## Conclusion

Data replication is important for ensuring the resilience and performance of stateful distributed services.  This article not only emphasized the significance of data replication in distributed systems, but it also demonstrated how Pulumi, in collaboration with Azure, enables developers to architect and manage resilient, performant, and globally distributed infrastructures for their stateful applications. As cloud-native architectures expand, the importance of infrastructure as code (IaC) in ensuring optimal data replication outcomes becomes increasingly important, and Pulumi can be used to provision the infrastructure required.

Did you learn something new? We’d like to know. If you’d like to try this out for yourself, you can get started with Pulumi Cloud [here](/product/pulumi-cloud/). You can also join our community to be a part of the continuous conversation, and we can’t wait to see what you build!
