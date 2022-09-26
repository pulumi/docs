---
title: "Database Comparison: Cosmos DB vs DynamoDB"
meta_desc: |
     Compare NoSQL databases Cosmos DB vs DynamoDB. See the similarities and differences between these databases to determine which is best for you.

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
---

## Cosmos DB vs DynamoDB: What Are The Similarities?

Both Cosmos DB and DynamoDB are [NoSQL]({{< relref "/learn/glossary/nosql" >}}), or non-relational, databases. This concept means their data is stored in some format other than two-dimensional tables. Some commonly-used formats for NoSQL databases in general are documents, key-value pairs, graphs, and columns, each with different strengths and tradeoffs.

Cosmos DB and DynamoDB are both highly-available, scalable, globally distributed and fully-managed serverless NoSQL databases. Both function as document&ndash; or key-value&ndash;based databases.

## Cosmos DB vs DynamoDB: What Are The Differences?

The most significant difference between Cosmos DB and DynamoDB is that Cosmos DB was designed as a drop-in replacement for an enterprise-scale relational database, and thus supports queries that look very similar to traditional SQL. DynamoDB does not support SQL-style queries, although its own filters do allow you to get similar information with a different syntax.

### Pros and Cons of Cosmos DB

Cosmos DB offers a high degree of flexibility, thanks to its variety of available data models and the ability to use SQL-like queries in addition to Gremlin, Azure Tables, and MongoDB APIs when interacting with your data. While DynamoDB functions only as a document or a key-value database, Cosmos DB can function as document, key-value, wide column, and graph-based database. Its five consistency models (eventually consistent, consistent prefix, session, bounded staleness, and strong consistency) allow you to fine-tune your latency, and it scales quite well. It is priced according to storage and throughput.

However, this flexibility can make Cosmos DB somewhat more difficult to use at first. Understanding the various data models available to you and the intended use case of each one is key to ensuring that you are getting the most optimum performance for the price, according to your application's specific needs.

### Pros and Cons of DynamoDB

DynamoDB is extremely fast, with response times under 10ms, and also benefits from the entire suite of existing AWS services, including AWS IAM for fine-grained access control. If the rest of your infrastructure is already on AWS, it is the natural choice. It scales extremely well, with virtually unlimited storage available to you. It is a fully-managed service, meaning you are not responsible for managing any of the underlying infrastructure or upgrades.

While it can be cheaper than Cosmos DB, predicting the costs accurately can be difficult regardless of which billing model you go with (on-demand or provisioned). Those who are used to the specificity of traditional SQL queries may also find the query options lacking, and scanning the database rather than querying it can result in a higher-than-expected bill. DynamoDB is also exclusively available on the cloud, with no on-premise deployment option.

## Which NoSQL Database is the Best?

Cosmos DB is best if you need the wider flexibility of more data models, as well as the ability to leverage traditional SQL queries against non-relational data. If your existing infrastructure is already on Azure, it's a clear choice.

DynamoDB is best if the rest of your infrastructure is already on AWS or your priority is high performance for low cost over flexibility.

Both Cosmos DB and DynamoDB are quick to stand up when using Pulumi. Try [Cosmos DB]({{< relref "/blog/how-to-build-globally-distributed-applications-with-azure-cosmos-db-and-pulumi" >}}) and [DynamoDB]({{< relref "/docs/aws/dynamodb" >}}) for yourself!

## Pulumi Corporation

Pulumi's Cloud Engineering Platform unites infrastructure teams, application developers, and compliance teams around a unified software engineering process for delivering modern cloud applications faster and speeding innovation. Pulumi’s open-source tools help infrastructure teams tame the cloud’s complexity with Universal Infrastructure-as-Code using the world’s most popular programming languages and communities, including Python, YAML, Node.js (JavaScript, TypeScript), Go, and .NET (C#, F#, VB). [Get started for free today!]({{< relref "/docs/get-started" >}})
