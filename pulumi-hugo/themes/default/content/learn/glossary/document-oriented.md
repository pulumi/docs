---
title: Document Oriented Database
meta_desc: A class of NoSQL database that stores and queries data in the form of documents, usually JSON but sometimes also XML or YAML.
layout: glossary/single
---

## Definition

A document-oriented database is a class of NoSQL database that stores and queries data in the form of documents, usually JSON but sometimes also XML or YAML. Unlike a traditional relational database, objects within a document-based database are stored completely within one document, rather than across multiple tables. As a result, the concept of “joins” is not usually present. This model allows developers to query the database programmatically in a similar fashion to how they already access data within the application code.

Conceptually, you can think of a document as roughly equivalent to an object in your programming language. The structure is similar (or identical), and documents are not required to conform to a specific schema. For example, you may have a class of document called “books.” Each “book” object is not required to contain the same keys; one may include a “co-author” key, but the next may not. This allows for a lot of flexibility with certain types of data.

### Use Cases

Because of the flexibility and speed that document databases allow, they are a great choice for any application that relies on user profiles, content management systems, product information, and even real-time big data analytics.

### Examples

[DocumentDB](https://aws.amazon.com/documentdb/), [CosmosDB](https://azure.microsoft.com/en-us/services/cosmos-db/), [Firestore](https://firebase.google.com/docs/firestore), [MongoDB](https://www.mongodb.com/)
