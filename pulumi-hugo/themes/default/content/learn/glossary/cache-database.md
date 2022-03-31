---
title: Database Cache
meta_desc: A database cache is supplementary to your primary database, either built into your database itself or as an additional layer.
layout: glossary/single
---

## Definition

A database cache is supplementary to your primary database, either built into your database itself or as an additional layer. It exists to radically speed up read access to frequently-queried data and reduce pressure on the primary database, allowing you to scale while consuming fewer resources. Caches exist for both relational and non-relational databases. These solutions frequently use a key-value data structure.

### Use Cases

Placing the data most frequently requested by users in fast-access memory or closer to the front-end allows you to serve up content much more quickly. As a result, it is particularly useful for applications where speed is key, such as real-time or location-based recommendation engines, mobile development, and web development.

### Examples

[Amazon Elasticache](https://aws.amazon.com/elasticache/), [Redis](https://redis.io/), [Memorystore](https://cloud.google.com/memorystore)
