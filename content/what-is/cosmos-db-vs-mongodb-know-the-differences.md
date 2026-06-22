---
title: Cosmos DB vs MongoDB, Know The Differences?
meta_desc: |
     Compare Cosmos DB and MongoDB strengths and limitations to determine the best database option.

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
{{% notes type="info" %}}
**This document has been updated and expanded into [Cosmos DB vs Mongo DB](https://www.pulumi.com/blog/when-to-use-azure-cosmos-db/#cosmos-db-vs-mongodb) section of the [When to use Cosmos DB Guide](https://www.pulumi.com/blog/when-to-use-azure-cosmos-db/).**
{{% /notes %}}

Both Cosmos DB and MongoDB are [NoSQL](/tutorials/glossary/nosql/), or non-relational, databases. This concept means their data is stored in some format other than two-dimensional tables. Some commonly-used formats for NoSQL databases in general are documents, key-value pairs, graphs, and columns, each with different strengths and tradeoffs. Cosmos DB and MongoDB are both highly-available, scalable, globally distributed and fully-managed NoSQL databases.

### Benefits and Downfalls of Cosmos DB

Cosmos DB offers a high degree of flexibility, thanks to its variety of available data models and the ability to use SQL-like queries in addition to Gremlin, Azure Tables, and MongoDB APIs when interacting with your data. While MongoDB functions only as a document database, Cosmos DB can function as a document, key-value, wide column, and graph-based database. Its five consistency models (eventually consistent, consistent prefix, session, bounded staleness, and strong consistency) allow you to fine-tune your latency, and it scales quite well. It is priced according to storage and throughput.

However, this flexibility can make Cosmos DB somewhat more difficult to use at first. Understanding the various data models available to you and the intended use case of each one is key to ensuring that you are getting the most optimum performance for the price, according to your application's specific needs. It is also only available on Microsoft Azure.

### Benefits and Downfalls of MongoDB

MongoDB is strictly a document-based NoSQL database. However, it allows you to run queries against your data as if it is a SQL, key-value, or graph store, whereas Cosmos DB only allows you to run queries of the same type as the data you created. Due to the JSON-like structure of documents within MongoDB and the radically faster read and write speeds (as compared to a traditional relational database), MongoDB is an extremely popular choice for use with web applications. With a maximum allowed document size of 16MB (versus 2MB with CosmosDB), it can be a more attractive option for some teams. Using MongoDB also allows you to avoid vendor lock-in, as it can run on any cloud provider.

Teams who are used to relational databases may find MongoDB difficult to get used to, since concepts like joins as SQL users understand them don't exist out of the box. When comparing against Cosmos DB, reads and writes tend to be slower until the document size exceeds 2&nbsp;MB, at which point MongoDB excels.

### Getting Started

Neither database is the universally correct answer, and the comparison rarely turns on raw performance. The decision hinges on two constraints you can name up front: which cloud you're committed to, and how large your documents get. If you're already on Azure, or you want a single engine that can speak document, key-value, wide-column, and graph models, Cosmos DB earns its added learning curve. If you need documents above 2&nbsp;MB, want portability across clouds, or want to avoid vendor lock-in, MongoDB is the cleaner fit. Decide those two constraints first, and the rest of the trade-offs fall into place.

Whichever you pick, provisioning it shouldn't slow you down. Try deploying an [AKS application with Cosmos DB](/registry/packages/azure/how-to-guides/classic-azure-ts-aks-mean) or [get started with MongoDB Atlas](/docs/get-started/).
