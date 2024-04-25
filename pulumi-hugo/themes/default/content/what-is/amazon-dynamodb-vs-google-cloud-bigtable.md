---
title: Amazon DynamoDB vs Google Cloud Bigtable
meta_desc: |
     Compare Bigtable vs DynamoDB to learn the many similarities and differences between these two noSQL databases. Learn which is best with Pulumi.

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
---

## Biggest Similarities and Differences Between Google Cloud Bigtable and AWS DynamoDB

Both Google Cloud Bigtable and DynamoDB are [NoSQL](/learn/glossary/nosql/), or non-relational, databases. This concept means their data is stored in some format other than two-dimensional tables. Some commonly-used formats for NoSQL databases in general are documents, key-value pairs, graphs, and columns, each with different strengths and tradeoffs.

Google Cloud Bigtable and AWS DynamoDB are both highly-available, scalable, globally distributed and fully-managed serverless NoSQL databases. Both can function as a key-value store, however DynamoDB additionally supports a document model and Bigtable additionally supports a wide-column store. Both offer two consistency levels: eventual consistency, and immediate consistency.

## Which NoSQL Database is better? Bigtable vs DynamoDB

Choosing a database for your application requires careful consideration of your current and future needs. There are advantages and disadvantages to both Bigtable and DynamoDB, but they differ enough that one will have a clear advantage for your specific application.

### Pros and Cons of Bigtable

Bigtable excels at handling massive quantities of data and providing very low latency for both read and write actions on that data. It is also possible to dynamically adjust throughput, by adding more nodes to the Bigtable cluster for times of particularly high demand, then deleting those nodes once normal activity resumes to keep costs down. BigTable also supports SQL-like queries, through the use of BigQuery.

However, unlike DynamoDB, Bigtable does not support auto-scaling without first defining metrics to monitor and scale in response to. It also sacrifices some availability in exchange for consistency, whereas DynamoDB has made the opposite decision. Bigtable is exclusive to Google Cloud.

### Pros and Cons of DynamoDB

DynamoDB is extremely fast, with response times under 10ms, and also benefits from the entire suite of existing AWS services, including AWS IAM for fine-grained access control. It scales extremely well, with virtually unlimited storage available to you. It is a fully-managed service, meaning you are not responsible for managing any of the underlying infrastructure or upgrades.

While it can be a very affordable option, predicting the costs accurately can be difficult regardless of which billing model you go with (on-demand or provisioned). Those who are used to the specificity of traditional SQL queries may also find the query options lacking, and scanning the database rather than querying it can result in a higher-than-expected bill. It is exclusive to AWS.

## Bigtable vs DynamoDB: Pricing and Service Limits

Bigtable and DynamoDB have very different pricing models.

With Bigtable, your pricing is determined based on three factors: the type of Bigtable instance, the number of nodes you have (with nodes in some regions being more expensive than others), the amount of storage your tables use, and the amount of network bandwidth consumed. Storage and bandwidth usage are measured in binary gigabytes.

DynamoDB offers two different pricing models: on-demand capacity mode, and provisioned capacity mode. Using on-demand capacity mode, you are billed for the amount of data stored as well as the number of reads and writes performed against it, with DynamoDB automatically managing those workloads as they fluctuate. With provisioned capacity mode, you specify the number of reads and writes expected per second. It is possible to utilize auto-scaling to ensure that your application continues to perform well while keeping costs low.

## Which NoSQL Database is Better?

Google Cloud Bigtable and AWS DynamoDB both have strengths and weaknesses that will benefit some teams but hinder others. If your infrastructure is already on AWS, DynamoDB is the stronger offering.

If you have truly large amounts of data that you will require very fast access to, are most comfortable with something that looks like SQL, or the rest of your infrastructure is hosted on Google Cloud, you want Bigtable.

## Conclusion

Regardless of which database suits your needs, standing them up shouldn't be a chore. With Pulumi, provisioning either one is a breeze in the programming language of your choce. Try deploying an [AWS Data Service with DynamoDB](/docs/aws/dynamodb/) or get started with [Google Cloud](/docs/clouds/gcp/get-started/)

## Pulumi Corporation

Pulumi lets infrastructure, developer, and security teams deliver infrastructure as code faster, using programming ([Python](/docs/languages-sdks/python/), [Node.js (JavaScript, TypeScript)](/docs/languages-sdks/javascript/), [Go](/docs/languages-sdks/go/), [.NET (C#, F#, VB)](/docs/languages-sdks/dotnet/), and [Java](/docs/languages-sdks/java/) and markup ([YAML, JSON, and CUE](/docs/languages-sdks/yaml/) languages they already know. It provides a single pipeline for delivering and securing infrastructure and applications on any cloud. [Get started for free today!](/docs/get-started/)
