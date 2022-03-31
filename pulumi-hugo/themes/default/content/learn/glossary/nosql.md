---
title: NoSQL
meta_desc: A type of database that does not store its data in tables.
layout: glossary/single
---

## Definition

A type of database that organizes data into some data structure other than the two-dimensional tables seen in relational databases. Also called non-relational databases, NoSQL databases can be [document-based](/learn/glossary/document-oriented) (like MongoDB), [column-based](/learn/glossary/column-oriented) (like Apache Cassandra), [graph-based](/learn/glossary/graph-oriented) (like Neo4j), or [key-value](/learn/glossary/key-value) (like DynamoDB). Other flavors of NoSQL databases do exist, including hybrids, but these are the most commonly-used.

| Database Type 	| Use Cases                                                      	| Cloud Examples                  	| Self-hosted Examples 	|
|---------------	|----------------------------------------------------------------	|---------------------------------	|----------------------	|
| Key-Value     	| ECommerce, recommendation engines, high-traffic                	| [DynamoDB](https://aws.amazon.com/dynamodb/), [CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/), [BigTable](https://cloud.google.com/bigtable)    	| [Redis](https://redis.io/)                	|
| Column        	| Business intelligence, data warehousing                        	| [Keyspaces](https://aws.amazon.com/keyspaces/), [CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/)             	| [Apache Cassandra](https://cassandra.apache.org/_/index.html)     	|
| Graph         	| Recommendation engines, fraud detection, social networks       	| [Neptune](https://aws.amazon.com/neptune/)                         	| [Neo4j](https://neo4j.com/)                	|
| Document      	| Content management systems, user profiles, product information 	| [DocumentDB](https://aws.amazon.com/documentdb/), [CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/), [Firestore](https://firebase.google.com/docs/firestore) 	| [MongoDB](https://www.mongodb.com/)              	|
