---
title: Amazon DynamoDB vs Google Cloud Bigtable
meta_desc: "Compare Amazon DynamoDB and Google Cloud Bigtable across data model, consistency, latency, pricing, and scale to pick the right NoSQL database."
meta_image: /images/what-is/amazon-dynamodb-vs-google-cloud-bigtable-meta.png
type: what-is
page_title: "Amazon DynamoDB vs Google Cloud Bigtable"

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

**Amazon DynamoDB is a fully-managed, serverless key-value and document database from AWS, optimized for single-digit-millisecond access at any scale. Google Cloud Bigtable is a fully-managed wide-column NoSQL database optimized for petabyte-scale analytical, IoT, and time-series workloads.** Both are [NoSQL](/tutorials/glossary/nosql/) services from major cloud providers, but they target overlapping yet distinct workloads: DynamoDB is built for high-throughput transactional applications with predictable low latency, while Bigtable is built for very large analytical and time-series tables that need consistent, low-latency reads at petabyte scale.

In this article, we'll compare DynamoDB and Bigtable across:

* At-a-glance comparison
* Data model
* Consistency and transactions
* Performance and latency
* Pricing model
* Scalability and limits
* Ecosystem and integrations
* When to choose DynamoDB vs Bigtable
* Provisioning either database with Pulumi
* Frequently asked questions

## At-a-glance comparison

| Dimension | Amazon DynamoDB | Google Cloud Bigtable |
|---|---|---|
| Cloud | AWS | Google Cloud |
| Data model | Key-value and document | Wide-column (sparse, sorted map) |
| Query interface | DynamoDB API, PartiQL | HBase API, Bigtable client libraries, GoogleSQL (preview) |
| Consistency | Eventual (default) or strong on reads | Strong within a single cluster |
| Transactions | ACID across up to 100 items | Single-row atomic only |
| Typical p99 read latency | Single-digit milliseconds | Single-digit milliseconds |
| Pricing model | On-demand per request, or provisioned RCU/WCU | Per-node-hour plus storage |
| Max item / row size | 400 KB per item | 256 MB per row (recommended <100 MB) |
| Global distribution | Global Tables (multi-region active-active) | Multi-cluster replication with routing policies |
| Serverless | Yes | No (node-based clusters; autoscaling available) |
| Best for | OLTP, session stores, shopping carts, ad tech | Time series, IoT, analytics, large-scale event data |

## Data model

DynamoDB and Bigtable both reject relational tables, but they organize data differently.

### DynamoDB

DynamoDB stores **items** in tables. Every item has a primary key, which can be a single partition key or a partition key plus a sort key. Non-key attributes are schemaless — items in the same table can have different attributes. Values are typed (string, number, binary, boolean, list, map, set), so DynamoDB is effectively a key-value store with first-class document support up to 400 KB per item. Secondary indexes (local and global) make it possible to query on non-key attributes.

### Bigtable

Bigtable stores data in a single, massive **sparse, sorted, distributed map**: rows are keyed by a single row key (a byte string) and sorted lexicographically. Each row contains column families, each family contains columns, and each cell can hold multiple timestamped versions. Bigtable is schema-flexible within column families, scales horizontally across nodes, and is purpose-built for very large tables where queries are typically range scans on the row key. There are no secondary indexes — query patterns are designed around the row-key layout.

| Aspect | DynamoDB | Bigtable |
|---|---|---|
| Primary key | Partition key (+ optional sort key) | Single row key (byte string, sorted) |
| Secondary indexes | Local and global secondary indexes | None — design row keys for access patterns |
| Schema | Schemaless items, typed attributes | Schemaless within column families |
| Document support | Native (lists, maps) up to 400 KB | Not document-oriented; rows hold many columns |

## Consistency and transactions

DynamoDB and Bigtable both prioritize consistency *within* the unit they consider primary, but the units are different.

### DynamoDB

DynamoDB reads are **eventually consistent by default**, with an option to request strongly consistent reads (at higher cost and slightly higher latency). It supports **ACID transactions** across up to 100 items in one or more tables in a single request, including condition checks. Conditional writes and atomic counters cover most other concurrency needs.

### Bigtable

Bigtable provides **strong consistency** for reads and writes within a single cluster. Multi-cluster routing (eventual consistency across replicas) is configurable per app profile. Bigtable supports **single-row atomic operations** — including read-modify-write and check-and-mutate — but does not offer cross-row or cross-table transactions. Applications that need multi-row atomicity model it through row-key design.

| Property | DynamoDB | Bigtable |
|---|---|---|
| Default consistency | Eventual | Strong (single cluster) |
| Optional consistency | Strong reads per request | Eventual across multi-cluster replicas |
| Multi-item transactions | ACID across up to 100 items | Not supported (single-row atomic only) |
| Conditional writes | Yes | Yes (check-and-mutate) |

## Performance and latency

Both services target **single-digit-millisecond p99 latency** for well-designed workloads, but the operational profile differs.

* **DynamoDB** delivers consistent low latency across any scale because storage and throughput are decoupled from servers — capacity is allocated per partition automatically. DAX, an in-memory cache, can push reads into microseconds for cache-friendly workloads.
* **Bigtable** delivers consistent low latency for reads and writes proportional to the number of nodes in a cluster. Throughput scales linearly with nodes (roughly 10,000 ops/second/node on SSD), and large sequential scans are particularly efficient because data is stored in row-key order.

Workload fit:

* DynamoDB excels at high-concurrency point lookups and small writes — shopping carts, session stores, ad-tech bid logs.
* Bigtable excels at large sequential scans, high write throughput, and time-series ingest — financial tick data, IoT telemetry, monitoring metrics, large feature stores for ML.

## Pricing model

Pricing reflects the architectural difference: DynamoDB charges per request and per GB stored, while Bigtable charges per node-hour and per GB stored.

| Pricing dimension | DynamoDB | Bigtable |
|---|---|---|
| Compute / throughput | On-demand (per read/write request) or provisioned (RCU/WCU) | Per node-hour (SSD or HDD) |
| Storage | Per GB-month | Per GB-month (SSD costs more than HDD) |
| Network | Cross-region replication, data transfer out | Cross-cluster replication, data transfer out |
| Caching | DAX (per node-hour) | Cluster cache is built in |
| Backups | PITR and on-demand backups (per GB) | Backups per GB-month |
| Free tier | 25 GB storage, 25 WCU and 25 RCU/month | No free tier; per-hour billing |

DynamoDB's on-demand mode means you only pay for what you use, which is forgiving for spiky or unpredictable workloads. Bigtable's per-node-hour model rewards steady, high-throughput workloads where each node is well utilized.

## Scalability and limits

Both services scale to very large workloads, but the units and limits differ.

| Limit | DynamoDB | Bigtable |
|---|---|---|
| Max item / row size | 400 KB per item | 256 MB per row (recommended <100 MB) |
| Max table size | Unlimited | Petabytes per instance |
| Throughput model | RCU/WCU or on-demand; auto-scales | Add nodes (manually or with autoscaling) |
| Partitions | Managed automatically | Tablets split automatically by row-key range |
| Multi-region | Global Tables (active-active, multi-region) | Multi-cluster replication with app profile routing |
| Backup and restore | PITR (35 days), on-demand backups | Backups and import/export to Cloud Storage |

DynamoDB Global Tables provide active-active replication across regions with last-writer-wins conflict resolution. Bigtable's multi-cluster replication supports both same-region and cross-region clusters with configurable routing — useful for read locality, HA, and workload isolation between online and analytical traffic.

## Ecosystem and integrations

| Integration | DynamoDB | Bigtable |
|---|---|---|
| Analytics | DynamoDB exports to S3, Athena Federated Query, Redshift via Zero-ETL | Native integration with BigQuery, Dataflow, Dataproc |
| Streaming | DynamoDB Streams, Kinesis Data Streams | Bigtable change streams, Pub/Sub via Dataflow |
| Caching | DAX in-memory cache | Built-in block cache; Memorystore for app-side cache |
| Compute | Lambda, AppSync, API Gateway | Cloud Functions, Dataflow, GKE |
| IaC | AWS Provider, AWS Native Provider | Google Cloud Provider |
| API compatibility | AWS SDKs, PartiQL | HBase 1.x API, plus native gRPC clients |

DynamoDB sits at the center of serverless AWS architectures, with Lambda triggers via DynamoDB Streams and tight integration with AppSync. Bigtable plugs into Google's analytics stack — BigQuery can query Bigtable directly, and Dataflow is the standard way to land streaming data into Bigtable tables.

## When to choose DynamoDB vs Bigtable

Choose **DynamoDB** if:

* You're already on AWS and want tight integration with Lambda, API Gateway, IAM, and AppSync.
* Your workload is online transactional — shopping carts, user profiles, gaming leaderboards, session stores, ad-tech.
* You need ACID transactions across multiple items.
* You want fully serverless pricing that scales to zero between spikes.
* You need active-active multi-region writes with Global Tables.

Choose **Bigtable** if:

* You're on Google Cloud and want native BigQuery, Dataflow, and Dataproc integration.
* Your workload is time-series, IoT, telemetry, monitoring, or large analytical event data.
* You need to store petabytes in a single table with consistent low-latency reads and high write throughput.
* You can model access patterns around a single sorted row key and don't need cross-row transactions.
* You want HBase API compatibility for portability with existing Hadoop or HBase code.

If you're truly cloud-agnostic and want a comparable analytical store on AWS, **Amazon Keyspaces** or **Amazon Timestream** can be closer fits than DynamoDB. For OLTP on Google Cloud, **Cloud Spanner** or **Firestore** are typically better fits than Bigtable.

## Provisioning either database with Pulumi

[Pulumi](/docs/get-started/) lets you provision DynamoDB and Bigtable as code in TypeScript, Python, Go, .NET, Java, or YAML, using the [AWS provider](/registry/packages/aws/) and the [Google Cloud provider](/registry/packages/gcp/). Both providers expose the full service surface, including IAM, replication, backups, and autoscaling.

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

Example Bigtable instance:

```typescript
import * as gcp from "@pulumi/gcp";

const instance = new gcp.bigtable.Instance("telemetry", {
    clusters: [{
        clusterId: "telemetry-c1",
        zone: "us-central1-a",
        numNodes: 3,
        storageType: "SSD",
    }],
});
```

With either provider you can put encryption keys, IAM bindings, and replication into the same program — and enforce safe defaults across the org with [Pulumi Policies](/docs/insights/policy/).

## Frequently asked questions

### Is DynamoDB or Bigtable faster?

Both target single-digit-millisecond p99 latency for well-designed workloads. DynamoDB wins for point-lookup-heavy OLTP traffic, especially with DAX in front. Bigtable wins for large sequential scans and very high sustained write throughput. The "faster" service depends on the access pattern, not a benchmark.

### Can I run DynamoDB on Google Cloud or Bigtable on AWS?

No. DynamoDB is exclusive to AWS and Bigtable is exclusive to Google Cloud. If you need portability across clouds, look at self-managed alternatives like Apache Cassandra (similar wide-column model) or ScyllaDB.

### Do DynamoDB and Bigtable support transactions?

DynamoDB supports ACID transactions across up to 100 items in a single request. Bigtable only supports single-row atomic operations — there are no multi-row or multi-table transactions. Applications that need multi-row atomicity on Bigtable typically design row keys so related data lives in the same row.

### Is there a free tier?

DynamoDB has a free tier of 25 GB of storage and 25 WCU plus 25 RCU per month. Bigtable does not have a free tier — every node accrues per-hour cost from the moment the cluster is created.

### How do I migrate from one to the other?

There is no automated path between DynamoDB and Bigtable. A typical migration extracts data via DynamoDB Streams or S3 exports, transforms it (because the data model differs), and bulk-loads it into Bigtable through Dataflow. Plan a redesign of the schema and access patterns — a 1:1 port is rarely the right answer.

### Which is more cost-effective?

It depends on the workload shape. DynamoDB on-demand is cheaper for spiky or low-utilization workloads because you pay nothing when idle. Bigtable is cheaper for sustained, high-throughput workloads where nodes are consistently well utilized. Storage costs are broadly comparable.

### Can I query DynamoDB or Bigtable with SQL?

DynamoDB supports a subset of SQL through PartiQL. Bigtable supports GoogleSQL (in preview) and is also queryable from BigQuery via federation. Neither replaces a relational database — both are NoSQL stores where the query model is shaped around the key design, not arbitrary SQL.

### Are there managed backup options for each?

Yes. DynamoDB supports point-in-time recovery (PITR) for 35 days and on-demand backups. Bigtable supports backups stored in the same instance and import/export to Cloud Storage.

### Can I use the HBase API with DynamoDB?

No. The HBase API is specific to Bigtable. DynamoDB uses its own API (and PartiQL). Existing HBase applications can typically point at Bigtable with minor configuration changes.

## Learn more

Pulumi gives teams a single way to provision DynamoDB on AWS or Bigtable on Google Cloud, using the same programming languages, the same review workflow, and the same policy enforcement. [Get started today](/docs/get-started/).

Related reading:

* [Database Comparison: Cosmos DB vs DynamoDB](/what-is/database-comparison-cosmos-db-vs-dynamodb/)
* [Cosmos DB vs MongoDB: Know the differences](/what-is/cosmos-db-vs-mongodb-know-the-differences/)
* [Pulumi AWS provider](/registry/packages/aws/)
* [Pulumi Google Cloud provider](/registry/packages/gcp/)
