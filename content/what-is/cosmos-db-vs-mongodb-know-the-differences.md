---
title: Cosmos DB vs MongoDB, Know The Differences?
meta_desc: "Compare Azure Cosmos DB and MongoDB across data model, consistency, transactions, pricing, and ecosystem to pick the right NoSQL database."
meta_image: /images/what-is/cosmos-db-vs-mongodb-know-the-differences-meta.png
type: what-is
page_title: "Cosmos DB vs MongoDB, Know The Differences"

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
authors: ["kat-cosgrove"]
---

**Azure Cosmos DB is Microsoft's fully-managed, multi-model NoSQL database with five tunable consistency levels and built-in global distribution. MongoDB is a document-oriented database with a mature query language, ACID transactions, and a thriving ecosystem; MongoDB Atlas is the vendor-managed cloud offering that runs on AWS, Azure, and Google Cloud.** Both are [NoSQL](/tutorials/glossary/nosql/) services that store flexible JSON-like documents, but they differ in data model breadth, pricing model, cloud portability, and how transactions and consistency work.

In this article, we'll compare Cosmos DB and MongoDB across:

* At-a-glance comparison
* Data model and APIs
* Consistency and transactions
* Performance and latency
* Pricing model
* Scalability and limits
* Ecosystem and integrations
* When to choose Cosmos DB vs MongoDB
* Provisioning either database with Pulumi
* Frequently asked questions

## At-a-glance comparison

| Dimension | Azure Cosmos DB | MongoDB / MongoDB Atlas |
|---|---|---|
| Cloud | Azure only | AWS, Azure, GCP (Atlas); self-managed anywhere |
| Data model | Multi-model: document, key-value, graph, wide-column, table | Document (BSON) |
| APIs | Core (SQL), MongoDB, Cassandra, Gremlin, Table, PostgreSQL | MongoDB query language; Atlas Search (Lucene) |
| Consistency | 5 levels (strong, bounded staleness, session, consistent prefix, eventual) | Read concerns: local, majority, linearizable, available |
| Transactions | ACID within a logical partition; cross-partition transactions on Core API | Multi-document ACID since MongoDB 4.0 (4.2 sharded) |
| Pricing model | Request Units (RU/s), provisioned or serverless | Atlas: per-cluster hourly; self-managed: free |
| Max item / document size | 2 MB (Core API) | 16 MB |
| Global distribution | Built-in, single click, multi-region writes | Atlas Global Clusters (zoned sharding) |
| Search | Built-in indexing; vector search (Core API) | Atlas Search (Lucene), Atlas Vector Search |
| Best for | Azure-native apps, multi-model needs, global low-latency apps | Cloud-portable document workloads, content management, search-heavy apps |

## Data model and APIs

Both stores hold JSON-like documents, but Cosmos DB ships several APIs over the same engine while MongoDB stays focused on documents.

### Cosmos DB

Cosmos DB is **multi-model**: a single backend that exposes multiple wire-compatible APIs.

* **Core (SQL) API** — JSON documents with a SQL-like query language; the most feature-rich option.
* **MongoDB API** — wire-compatible with several MongoDB server versions.
* **Cassandra API** — CQL-compatible wide-column.
* **Gremlin API** — property-graph traversal.
* **Table API** — Azure Table-compatible key-value.
* **PostgreSQL** — Citus-based distributed Postgres (separate service tier).

Pick the API at account-creation time; you cannot switch later. The Core API exposes the most Cosmos DB features (change feed, stored procedures, vector search, integrated cache).

### MongoDB

MongoDB stores BSON documents in collections, organized into databases. The query language is MongoDB's own (`find`, `aggregate`, `$match`, `$lookup`), implemented through native drivers and the MongoDB Shell. **Atlas Search** layers Lucene-powered full-text search on top, and **Atlas Vector Search** adds vector indexes for embeddings.

| Aspect | Cosmos DB | MongoDB |
|---|---|---|
| Data model | Multi-model | Document only |
| Document size limit | 2 MB | 16 MB |
| Query language | SQL (Core API), MongoDB, CQL, Gremlin, etc. | MongoDB query + aggregation |
| Schema | Schema-flexible documents | Schema-flexible documents; optional schema validation |
| Joins | Within a partition only | `$lookup` for cross-collection lookup |

## Consistency and transactions

The two systems take different approaches to consistency.

### Cosmos DB

Cosmos DB exposes **five tunable consistency levels**, chosen per account or per request:

* **Strong** — linearizable reads; lowest staleness, highest cost.
* **Bounded staleness** — reads lag writes by at most *K* versions or *T* seconds.
* **Session** — read-your-writes within a single client session (default; best balance for many apps).
* **Consistent prefix** — reads never see out-of-order writes.
* **Eventual** — lowest latency and cost; no ordering guarantees.

Transactions are ACID within a single logical partition. The Core API supports **transactional batch** operations across documents in the same partition; cross-partition transactions are limited.

### MongoDB

MongoDB supports **multi-document ACID transactions** since version 4.0 (4.2 added support across sharded clusters). Reads expose configurable read concerns (`local`, `available`, `majority`, `linearizable`) and writes expose write concerns (`{ w: <n> }`, `majority`, etc.). The default `majority` write concern combined with `majority` read concern gives strong, linearizable-like guarantees that most workloads want.

| Property | Cosmos DB | MongoDB |
|---|---|---|
| Consistency levels | 5 tunable | Read concern + write concern |
| Default | Session | Majority |
| Multi-document ACID | Within a logical partition | Yes (4.0+; 4.2+ sharded) |
| Linearizable reads | Strong level | `linearizable` read concern |

## Performance and latency

Both services target single-digit-millisecond p99 latency for typical workloads.

* **Cosmos DB** publishes p99 read latency commitments under 10 ms for items <1 KB in a single region. Multi-region writes and the integrated cache can reduce latency further for hot reads.
* **MongoDB Atlas** delivers similar latency on dedicated clusters; performance scales with cluster tier (M10 through M700+) and disk IOPS. Sharded clusters scale throughput linearly with shards.

Throughput in Cosmos DB is measured in **Request Units per second (RU/s)** — an abstraction that combines CPU, memory, and IOPS for a given operation. A 1 KB point read costs roughly 1 RU; a write costs about 5 RU. MongoDB Atlas throughput is bounded by the cluster's tier (vCPU, RAM, IOPS) — closer to a traditional server-sizing model.

## Pricing model

Pricing reflects the two architectures.

| Pricing dimension | Cosmos DB | MongoDB Atlas |
|---|---|---|
| Throughput | Provisioned RU/s, autoscale RU/s, or serverless (per million RUs) | Per-cluster hourly (vCPU/RAM/storage) |
| Storage | Per GB-month | Included in cluster + per-GB overflow |
| Multi-region | Per RU/s and per GB, multiplied by replicated regions | Multi-region cluster pricing |
| Backup | Periodic free; continuous (PITR) paid | Continuous backup tiered by retention |
| Free tier | 1000 RU/s and 25 GB free forever per account | M0 free shared cluster (512 MB) |
| Self-managed | Not available | Free (MongoDB Community Server) |

Cosmos DB's RU model is granular but requires capacity planning — under-provision and requests get 429-throttled; over-provision and the bill climbs. Atlas cluster pricing is simpler to predict but pays for unused headroom.

## Scalability and limits

| Limit | Cosmos DB | MongoDB |
|---|---|---|
| Max document size | 2 MB | 16 MB |
| Partitioning | Logical partitions by partition key; auto-managed | Sharding by shard key (Atlas: zoned sharding for geo) |
| Multi-region | Built-in, single-click; optional multi-region writes | Atlas Global Clusters, replica sets across regions |
| Storage | Unlimited per container (subject to partition design) | Unlimited per sharded cluster |
| Change feed | Cosmos DB change feed (pull or push) | MongoDB change streams |

Both scale to very large workloads. Cosmos DB hides the partitioning model — you provide a partition key and the service handles tablet splits. MongoDB exposes sharding more directly; choosing a good shard key remains an explicit engineering task.

## Ecosystem and integrations

| Integration | Cosmos DB | MongoDB |
|---|---|---|
| Cloud | Azure only | AWS, Azure, GCP (Atlas); on-prem and any cloud (self-managed) |
| Analytics | Synapse Link (HTAP), Azure Data Factory, Fabric | Atlas Data Federation, Atlas SQL, BI Connector |
| Search | Native indexing, vector search (Core API) | Atlas Search (Lucene), Atlas Vector Search |
| Compute | Azure Functions, App Service, AKS | Anywhere; popular with Node.js, Python, Java |
| Drivers | Native SDKs plus wire-compatible MongoDB and Cassandra drivers | First-party drivers in 12+ languages |
| IaC | Azure Native provider | MongoDB Atlas provider |

MongoDB has by far the larger general-purpose ecosystem — drivers, community, ODMs (Mongoose), tutorials, books. Cosmos DB has the strongest integration with the Azure data and analytics stack (Synapse, Fabric, Event Hubs, Functions).

## When to choose Cosmos DB vs MongoDB

Choose **Cosmos DB** if:

* You're standardizing on Azure and want first-party integration with Azure services.
* You need built-in, single-click global distribution with multi-region writes.
* You want tunable consistency levels picked per-workload.
* You need multiple data models behind one billing relationship (document, graph, wide-column).
* You want a serverless option with very low minimum spend.

Choose **MongoDB** if:

* You need cloud portability — Atlas runs on AWS, Azure, and GCP, and Community Server runs anywhere.
* You're document-first and want the richest document query language and tooling.
* You need multi-document ACID transactions as a first-class feature.
* Your documents can be up to 16 MB.
* You want a large pool of developers already fluent in the platform and a mature plugin/driver ecosystem.

Many teams use **Cosmos DB's MongoDB API** as a middle ground: MongoDB wire compatibility with the operational profile of Cosmos DB. Verify which MongoDB server version's features you actually need; Cosmos DB's MongoDB API supports a subset that varies by version.

## Provisioning either database with Pulumi

[Pulumi](/docs/get-started/) lets you provision Cosmos DB and MongoDB Atlas as code in TypeScript, Python, Go, .NET, Java, or YAML, using the [Azure Native provider](/registry/packages/azure-native/) and the [MongoDB Atlas provider](/registry/packages/mongodbatlas/).

Example Cosmos DB account and SQL database:

```typescript
import * as azure from "@pulumi/azure-native";

const account = new azure.documentdb.DatabaseAccount("app", {
    resourceGroupName: "app-rg",
    location: "westus",
    databaseAccountOfferType: "Standard",
    locations: [{ locationName: "westus", failoverPriority: 0 }],
    consistencyPolicy: { defaultConsistencyLevel: "Session" },
});
```

Example MongoDB Atlas cluster:

```typescript
import * as mongodbatlas from "@pulumi/mongodbatlas";

const cluster = new mongodbatlas.Cluster("app", {
    projectId: projectId,
    name: "app-cluster",
    providerName: "AWS",
    providerInstanceSizeName: "M10",
    providerRegionName: "US_EAST_1",
});
```

Both providers cover the full surface — encryption, private endpoints, backups, IAM/database users, network rules — and integrate with [Pulumi Policies](/docs/insights/policy/) to enforce safe defaults across the org.

## Frequently asked questions

### Is Cosmos DB just MongoDB on Azure?

No. Cosmos DB is a separate engine that *exposes a MongoDB-compatible API* (alongside Core SQL, Cassandra, Gremlin, Table, and PostgreSQL). The MongoDB API works with standard MongoDB drivers and tools, but the underlying storage, replication, and consistency model are Cosmos DB's. Not every MongoDB feature is supported, and behavior at the edges can differ.

### Which is faster, Cosmos DB or MongoDB?

Both achieve single-digit-millisecond p99 latency on well-designed workloads. Cosmos DB publishes explicit latency commitments; MongoDB Atlas latency depends on the cluster tier. For very small documents and high-concurrency point reads, Cosmos DB's RU model can be very competitive. For large documents or aggregation-heavy workloads, MongoDB often wins.

### Can I run MongoDB on Azure or Cosmos DB on AWS?

You can run MongoDB Atlas on Azure (Atlas supports all three major clouds) or self-host MongoDB on any cloud. Cosmos DB is Azure-only — there is no AWS or GCP version. Teams that want a Microsoft-managed Mongo experience often use Cosmos DB's MongoDB API.

### Does Cosmos DB support ACID transactions?

Yes, within a single logical partition (and across documents in that partition via transactional batch). Cross-partition transactions are limited. MongoDB supports multi-document ACID transactions across replica sets (since 4.0) and sharded clusters (since 4.2).

### What's the difference between MongoDB and MongoDB Atlas?

MongoDB is the open-source database engine. MongoDB Atlas is MongoDB Inc.'s fully-managed cloud service that runs MongoDB on AWS, Azure, or GCP, with automated backups, monitoring, security defaults, and add-on services like Atlas Search and Vector Search.

### Is there a free tier?

Cosmos DB has a free tier that gives 1,000 RU/s and 25 GB of storage per account, forever. MongoDB Atlas offers an M0 shared cluster with 512 MB storage. MongoDB Community Server is free to self-host.

### Which has the larger document size limit?

MongoDB allows documents up to 16 MB. Cosmos DB caps items at 2 MB (Core API). If your domain has documents that routinely approach those limits, the difference matters.

### Can I migrate from MongoDB to Cosmos DB (or vice versa)?

Yes. Cosmos DB's MongoDB API lets standard MongoDB tools migrate data, but verify that the features your app uses are supported by the target API version. Going the other way (Cosmos DB Core API to MongoDB) requires more work because the data model and query language change.

### Do both support vector search?

Yes. Cosmos DB has native vector search on the Core API and on the MongoDB API (in preview by region). MongoDB Atlas offers Atlas Vector Search alongside Atlas Search. Both are common back-ends for retrieval-augmented generation (RAG) pipelines.

### How does pricing actually compare?

It depends on the workload. Cosmos DB's RU model is granular: small, bursty workloads can be very cheap (serverless), while large, steady workloads need careful RU/s sizing. MongoDB Atlas cluster pricing is simpler to forecast but pays for headroom even when idle. Run a representative workload through both calculators before committing.

## Learn more

Pulumi gives teams a single way to provision Cosmos DB on Azure or MongoDB Atlas on any cloud, using the same programming languages, review workflow, and policy enforcement. [Get started today](/docs/get-started/).

Related reading:

* [Database Comparison: Cosmos DB vs DynamoDB](/what-is/database-comparison-cosmos-db-vs-dynamodb/)
* [Amazon DynamoDB vs Google Cloud Bigtable](/what-is/amazon-dynamodb-vs-google-cloud-bigtable/)
* [Pulumi Azure Native provider](/registry/packages/azure-native/)
* [Pulumi MongoDB Atlas provider](/registry/packages/mongodbatlas/)
