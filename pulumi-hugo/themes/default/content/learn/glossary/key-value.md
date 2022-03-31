---
title: Key-Value Oriented Database
meta_desc: A type of NoSQL database that relies on a key-value structure like a dictionary or hash table to store and retrieve data.
layout: glossary/single
---

## Definition

A key-value database is a type of NoSQL database that relies on a key-value structure like a dictionary or hash table to store and retrieve data. Each dictionary contains a collection of objects, each of which has its own attributes. Only the key can be queried, so reads and writes are typically very fast.

In a key-value database, the schema for an entry’s attributes is defined on a per-object basis, rather than across the whole collection. For instance, the first key may be a unique identifier (say, a UUID), and its value may be another key-value pair, like the type of object (“book”) and its attributes (the author, genre, publication date, and ISBN). The second entry doesn’t necessarily need to have the same attributes, or even be the same type of object.

### Use Cases

These types of databases are used when flexibility and speed are key. They are particularly useful in e-commerce, where you may need to be able to handle a lot of continuous read/write actions with inconsistently-shaped data, as in the case of a large product catalog and a shopping cart.

### Examples

[DynamoDB](https://aws.amazon.com/dynamodb/), [CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/), [Bigtable](https://cloud.google.com/bigtable), [Redis](https://redis.io/)
