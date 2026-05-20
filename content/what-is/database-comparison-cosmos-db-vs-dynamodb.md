---
title: "Database Comparison: Cosmos DB vs DynamoDB"
meta_desc: "Compare Azure Cosmos DB and Amazon DynamoDB across data model, consistency, performance, pricing, and ecosystem to pick the right NoSQL database."
meta_image: /images/what-is/database-comparison-cosmos-db-vs-dynamodb-meta.png
type: what-is
page_title: "Database Comparison: Cosmos DB vs DynamoDB"

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

**Azure Cosmos DB is Microsoft's fully-managed, multi-model NoSQL database with five tunable consistency levels and built-in global distribution. Amazon DynamoDB is AWS's fully-managed, serverless key-value and document database, optimized for single-digit-millisecond access at any scale.** Both are [NoSQL](/tutorials/glossary/nosql/) services that target high-throughput transactional workloads, but they diverge on data model breadth, consistency configuration, pricing, and cloud platform.

In this article, we'll compare Cosmos DB and DynamoDB across:

* At-a-glance comparison
* Data model and APIs
* Consistency and transactions
* Performance and latency
* Pricing model
* Scalability and limits
* Ecosystem and integrations
* When to choose Cosmos DB vs DynamoDB
* Provisioning either database with Pulumi
* Frequently asked questions

## At-a-glance comparison

| Dimension | Azure Cosmos DB | Amazon DynamoDB |
|---|---|---|
| Cloud | Azure only | AWS only |
| Data model | Multi-model: document, key-value, graph, wide-column, table | Key-value and document |
| APIs | Core (SQL), MongoDB, Cassandra, Gremlin, Table, PostgreSQL | DynamoDB API, PartiQL |
| Consistency | 5 tunable levels (strong, bounded staleness, session, consistent prefix, eventual) | Eventual (default) or strong on reads |
| Transactions | ACID within a logical partition | ACID across up to 100 items |
| Pricing model | Request Units (RU/s), provisioned or serverless | On-demand or provisioned RCU/WCU |
| Max item / document size | 2 MB (Core API) | 400 KB |
| Global distribution | Built-in, single click, multi-region writes | Global Tables (multi-region active-active) |
| Caching | Integrated cache | DAX in-memory cache |
| Best for | Multi-model Azure workloads, global low-latency apps | Serverless AWS workloads, OLTP at scale |

## Data model and APIs

Both stores hold JSON-like items, but Cosmos DB exposes several wire-compatible APIs over a single engine while DynamoDB stays close to one model.

### Cosmos DB

Cosmos DB is **multi-model**. A single backend exposes:

* **Core (SQL) API** — JSON documents with a SQL-like query language; the most feature-rich option.
* **MongoDB API** — wire-compatible with the MongoDB query language.
* **Cassandra API** — CQL-compatible wide-column.
* **Gremlin API** — property-graph traversal.
* **Table API** — Azure Table-compatible key-value.
* **PostgreSQL** — Citus-based distributed Postgres (separate service tier).

Pick the API at account creation; switching later requires migration. The Core API exposes the most Cosmos DB features (change feed, stored procedures, vector search, integrated cache).

### DynamoDB

DynamoDB stores **items** in tables keyed by a partition key, optionally with a sort key. Items are schemaless with typed attributes (string, number, binary, boolean, list, map, set). DynamoDB also supports a SQL-compatible query layer called **PartiQL** for ad-hoc queries.

| Aspect | Cosmos DB | DynamoDB |
|---|---|---|
| Data model | Multi-model | Key-value and document |
| Item size limit | 2 MB | 400 KB |
| Query language | SQL (Core API), MongoDB, CQL, Gremlin, etc. | DynamoDB API or PartiQL |
| Secondary indexes | Automatic indexing on all properties; composite indexes | Local and global secondary indexes (explicit) |
| Schema | Schema-flexible | Schemaless items, typed attributes |

A practical consequence: Cosmos DB indexes every property by default (you can opt out), so ad-hoc queries don't require new indexes. DynamoDB indexes only the primary key plus any LSIs/GSIs you create — schema and access patterns must be co-designed up front.

## Consistency and transactions

Cosmos DB and DynamoDB take different approaches to consistency.

### Cosmos DB

Cosmos DB offers **five tunable consistency levels**, chosen per account or per request:

* **Strong** — linearizable reads; lowest staleness, highest cost.
* **Bounded staleness** — reads lag writes by at most *K* versions or *T* seconds.
* **Session** — read-your-writes within a session (default for many apps).
* **Consistent prefix** — reads never see out-of-order writes.
* **Eventual** — lowest latency and cost; no ordering guarantees.

Transactions are ACID within a single logical partition; the Core API supports **transactional batch** across documents in the same partition. Cross-partition transactions are limited.

### DynamoDB

DynamoDB defaults to **eventual consistency** on reads, with an option to request strongly consistent reads per query (at higher cost and slightly higher latency). It supports **ACID transactions across up to 100 items** in one or more tables in a single request, including condition checks. Conditional writes and atomic counters cover most other concurrency needs.

| Property | Cosmos DB | DynamoDB |
|---|---|---|
| Default consistency | Session | Eventual |
| Optional consistency | 4 other levels | Strong reads per request |
| Multi-item transactions | Within a logical partition | ACID across up to 100 items |
| Conditional writes | Yes | Yes |

## Performance and latency

Both services target **single-digit-millisecond p99 latency** for well-designed workloads.

* **Cosmos DB** publishes p99 read latency commitments under 10 ms for items <1 KB in a single region. The integrated cache and multi-region writes can reduce latency further for hot reads.
* **DynamoDB** delivers consistent low latency regardless of table size; capacity is allocated per partition automatically. **DAX**, an in-memory cache, can push reads into microseconds for cache-friendly workloads.

Throughput is provisioned differently:

* Cosmos DB measures throughput in **Request Units per second (RU/s)** — an abstraction that combines CPU, memory, and IOPS for a given operation. A 1 KB point read costs roughly 1 RU; a write costs about 5 RU.
* DynamoDB measures throughput in **read capacity units (RCU)** and **write capacity units (WCU)** in provisioned mode, or charges per request in on-demand mode. One RCU covers one strongly consistent read of an item up to 4 KB; one WCU covers one write of an item up to 1 KB.

Both services autoscale based on traffic; both can saturate when traffic spikes past configured limits and return 429s (Cosmos DB) or throttle (DynamoDB).

## Pricing model

The two pricing models reflect the architectures.

| Pricing dimension | Cosmos DB | DynamoDB |
|---|---|---|
| Throughput | Provisioned RU/s, autoscale RU/s, or serverless | On-demand (per request) or provisioned RCU/WCU |
| Storage | Per GB-month | Per GB-month |
| Multi-region | Per RU/s and per GB, multiplied by replicated regions | Per Global Table replica region |
| Backup | Periodic free; continuous (PITR) paid | PITR (35 days) and on-demand backups (per GB) |
| Caching | Integrated cache (per cache node) | DAX (per node-hour) |
| Free tier | 1,000 RU/s and 25 GB free forever per account | 25 GB storage, 25 WCU and 25 RCU per month |

Cosmos DB's RU model is granular but requires careful capacity planning. DynamoDB's on-demand mode is the simplest fit for spiky or unpredictable workloads — provisioned mode pays off for steady traffic where capacity can be sized accurately.

## Scalability and limits

| Limit | Cosmos DB | DynamoDB |
|---|---|---|
| Max item size | 2 MB | 400 KB |
| Partitioning | Logical partitions by partition key; auto-managed | Auto-managed by partition key |
| Multi-region | Built-in single-click; optional multi-region writes | Global Tables (active-active multi-region) |
| Indexing | Automatic on all properties; composite indexes | Local and global secondary indexes (explicit) |
| Change feed | Cosmos DB change feed (pull or push) | DynamoDB Streams, Kinesis Data Streams |
| Backup/restore | Continuous (PITR) and periodic | PITR (35 days), on-demand backups |

Both services scale to very large workloads with managed partitioning. Cosmos DB hides partitioning behind logical partitions; DynamoDB does the same with adaptive capacity. The 5x larger item-size limit (2 MB vs 400 KB) is the most concrete data-model difference and can matter for documents that aren't easily split.

## Ecosystem and integrations

| Integration | Cosmos DB | DynamoDB |
|---|---|---|
| Cloud | Azure only | AWS only |
| Analytics | Synapse Link (HTAP), Azure Data Factory, Fabric | S3 exports, Athena Federated Query, Redshift Zero-ETL |
| Streaming | Cosmos DB change feed | DynamoDB Streams, Kinesis Data Streams |
| Caching | Integrated cache | DAX |
| Compute | Azure Functions, App Service, AKS | Lambda, AppSync, API Gateway |
| Drivers | Native SDKs plus wire-compatible MongoDB, Cassandra | AWS SDKs, PartiQL |
| IaC | Azure Native provider | AWS Provider, AWS Native provider |

DynamoDB sits at the center of serverless AWS architectures, with Lambda triggers via DynamoDB Streams, tight IAM integration, and AppSync for GraphQL. Cosmos DB integrates first-class with Azure Functions, Synapse for HTAP analytics, and Microsoft Fabric.

## When to choose Cosmos DB vs DynamoDB

Choose **Cosmos DB** if:

* You're standardizing on Azure and want first-party integration with Azure services.
* You need built-in, single-click global distribution with multi-region writes.
* You want tunable consistency levels picked per-workload.
* You need multiple data models behind one billing relationship (document, graph, wide-column).
* You need item sizes larger than 400 KB (Cosmos DB allows up to 2 MB).
* You want SQL-like queries against JSON documents without provisioning explicit secondary indexes.

Choose **DynamoDB** if:

* You're already on AWS and want tight integration with Lambda, API Gateway, IAM, and AppSync.
* Your workload is high-throughput OLTP — shopping carts, gaming, session stores, ad-tech.
* You need ACID transactions across multiple items, possibly across tables.
* You want fully serverless pricing that scales to zero between spikes.
* You need active-active multi-region writes with Global Tables and last-writer-wins.

If your application is genuinely cloud-agnostic, look at MongoDB Atlas or self-managed Apache Cassandra rather than picking one vendor's NoSQL.

## Provisioning either database with Pulumi

[Pulumi](/docs/get-started/) lets you provision Cosmos DB and DynamoDB as code in TypeScript, Python, Go, .NET, Java, or YAML, using the [Azure Native provider](/registry/packages/azure-native/) and the [AWS provider](/registry/packages/aws/).

Example Cosmos DB account:

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

Example DynamoDB table:

```typescript
import * as aws from "@pulumi/aws";

const orders = new aws.dynamodb.Table("orders", {
    billingMode: "PAY_PER_REQUEST",
    hashKey: "orderId",
    attributes: [{ name: "orderId", type: "S" }],
    pointInTimeRecovery: { enabled: true },
});
```

Both providers cover the full surface — encryption keys, IAM, replication, autoscaling, backups — and integrate with [Pulumi Policies](/docs/insights/policy/) to enforce safe defaults across the org.

## Frequently asked questions

### Which is faster, Cosmos DB or DynamoDB?

Both achieve single-digit-millisecond p99 latency for well-designed workloads. Cosmos DB publishes explicit latency commitments under 10 ms for items <1 KB. DynamoDB's latency is similarly consistent and stays flat as data grows. Caching layers (Cosmos DB's integrated cache, DynamoDB DAX) can push hot-read latencies into microseconds on either side.

### Can I run Cosmos DB on AWS or DynamoDB on Azure?

No. Cosmos DB is exclusive to Azure and DynamoDB is exclusive to AWS. For workloads that need cross-cloud portability, consider MongoDB Atlas (runs on AWS, Azure, and GCP) or self-managed Apache Cassandra or ScyllaDB.

### Do both support multi-document transactions?

Yes, with different scopes. Cosmos DB supports ACID transactions within a single logical partition (transactional batch). DynamoDB supports ACID transactions across up to 100 items in one or more tables in a single request.

### Is there a free tier?

Cosmos DB has a free tier that gives 1,000 RU/s and 25 GB of storage per account, forever. DynamoDB's free tier provides 25 GB of storage and 25 WCU plus 25 RCU per month.

### Which has the larger item size limit?

Cosmos DB allows items up to 2 MB. DynamoDB caps items at 400 KB. For domains with large embedded documents, the 5x difference matters.

### Can I query either with SQL?

Cosmos DB's Core API uses a SQL-like dialect; you can run real `SELECT` queries against JSON documents. DynamoDB supports a subset of SQL through PartiQL. Neither replaces a relational database — both are NoSQL stores where keys and indexes shape query patterns.

### How do I migrate from one to the other?

There's no automated path. Typical migrations export data (DynamoDB to S3 or via Streams; Cosmos DB via the change feed or Data Factory), transform it because the data models differ, and bulk-load it into the target. Plan a redesign of the schema and access patterns — a 1:1 port is rarely the right answer.

### Which is more cost-effective?

It depends on workload shape. DynamoDB on-demand wins for spiky or low-utilization workloads because you pay nothing when idle. Cosmos DB's serverless option is similar for low-traffic apps; provisioned RU/s is more cost-effective for steady traffic where the RUs can be tightly sized. Run a representative workload through both calculators before committing.

### Do both support multi-region writes?

Yes. Cosmos DB offers multi-region writes as a single-click option on any account. DynamoDB offers it through Global Tables, with active-active replication and last-writer-wins conflict resolution.

### Do both support vector search for AI workloads?

Cosmos DB offers native vector search on the Core API. DynamoDB does not have a first-party vector index; teams typically pair it with a dedicated vector store (OpenSearch, pgvector, Pinecone) for retrieval-augmented generation pipelines.

## Learn more

Pulumi gives teams a single way to provision Cosmos DB on Azure or DynamoDB on AWS, using the same programming languages, review workflow, and policy enforcement. [Get started today](/docs/get-started/).

Related reading:

* [Cosmos DB vs MongoDB: Know the differences](/what-is/cosmos-db-vs-mongodb-know-the-differences/)
* [Amazon DynamoDB vs Google Cloud Bigtable](/what-is/amazon-dynamodb-vs-google-cloud-bigtable/)
* [Pulumi Azure Native provider](/registry/packages/azure-native/)
* [Pulumi AWS provider](/registry/packages/aws/)
