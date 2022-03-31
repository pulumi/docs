---
title: Column Oriented Database
meta_desc: A type of NoSQL database that stores its data in columns, rather than the two-dimensional column and row organization of a traditional relational database.
layout: glossary/single
---

## Definition

A column-oriented database (sometimes called a wide-column store) is a type of NoSQL database that stores its data in columns, rather than the two-dimensional column and row organization of a traditional relational database. In a SQL database, all of the information about a particular entry is stored in the form of a record across a row, split into columns. All of the data for that record is stored together in memory. In a columnar database, all of the information for a particular field (say, addresses) is stored together in memory. Because of this, columns not relevant to your query are ignored when searching. The drive head doesn’t have to seek (or move) as far across the platter to read a record, and so query times are much shorter.

### Use Cases

The speed that the columnar model provides makes this an extremely popular choice for Big Data applications, data warehousing, and business intelligence. Columnar databases are able to receive huge quantities of data from multiple sources and run queries against them very fast.

### Examples

[Keyspaces](https://aws.amazon.com/keyspaces/), [CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/) , [Apache Cassandra](https://cassandra.apache.org/_/index.html)
