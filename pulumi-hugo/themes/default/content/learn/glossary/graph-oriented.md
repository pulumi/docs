---
title: Graph Oriented Database
meta_desc: A type of NoSQL database that relies on the graph data structure to define and manage relationships between different entries.
layout: glossary/single
---

## Definition

A graph-oriented database is a type of NoSQL database that relies on the graph data structure to define and manage relationships between different entries. Like the data structure, graph-oriented databases have the concepts of nodes and edges. Each entry or record in the database is a node, and the edges of each node are that entry’s relationship to other nodes in the database. An edge of one node could describe an action taken involving another node in the database, ownership over an account, or provenance of the node. For instance, determining a pattern of purchases amongst users who have similar behavior.

### Use Cases

The strength of a graph-oriented database lies in its ability to enable semantic queries. Because of this, it’s great for things like recommendation engines (“people who bought $product also bought $otherProduct!”) and social networks (friends of friends).

### Examples

[Neptune](https://aws.amazon.com/neptune/), [Neo4j](https://neo4j.com/)
