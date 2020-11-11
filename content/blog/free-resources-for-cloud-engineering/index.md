---
title: "Guide to Free Resources for Cloud Engineering"
date: 2020-11-12
meta_desc: "Free resources for building infrastructure with cloud engineering."
meta_image: cloud_engineering_resources.png
authors:
    - sophia-parafina
tags:
    - cloud engineering
    - AWS
    - Azure
    - Google Cloud
---

Innovation is at the heart of cloud engineering. Finding the right cloud solution requires experimentation to understand each cloud ecosystem and the best practices for each. The good news is that cloud providers have free service tiers for many cloud resources. These resources are often always free under a certain usage threshold or free to use for a limited time, often 12 months after creating an account.

Having free access to resources frees you to experiment, try out new ideas, and implement different application deployment architectures. However, given the number of cloud providers and the range of services they provide, getting started can be intimidating. This article is a guide to popular cloud resources and how to use them.

<!--more-->

## AWS

Amazon offers a free tier composed of always free, 12 months free available to new customers, and short term trials. The following is a selection of always free resources with accompanying tutorials, examples, and blog posts to get you started.

[**Amazon DynamoDB**](https://aws.amazon.com/dynamodb/): Amazon’s NoSQL key-value and document database with 25 GB of storage and 25 units of read and write each month.

- [How to create an AWS DynamoDB data service with Pulumi]({{< relref "/docs/aws/dynamodb" >}})
- [Serverless REST APIs with DynamoDB]({{< relref "/docs/tutorials/cloudfx/rest-api" >}})
- [Creating a DynampDB Table](https://pulumi.awsworkshop.io/additional-content/120_serverless_application_patterns/10_creating_a_dynamodb_table.html)

[**AWS Lambda**](https://aws.amazon.com/lambda/): Amazon’s function-as-a-service can run code for any application or backend service. Upload your code, and Lambda runs and scales your code with high availability with zero administration. Your code can trigger other AWS services or call the function a web or mobile app.

- [AWS Lambda and Serverless Events]({{< relref "/docs/guides/crosswalk/aws/lambda" >}})
- [Serverless App Using API Gateways and Lambda]({{< relref "/docs/tutorials/aws/rest-api" >}})
- [Controlling AWS Costs with Pulumi and AWS Lambda]({{< relref "/blog/controlling-aws-costs-with-lambda-and-pulumi" >}})
- [Scheduling Serverless]({{< relref "/blog/scheduling-serverless" >}})

[**Amazon RDS**](https://aws.amazon.com/rds/): Amazon’s managed-database service — MySQL, MariaDB, PostgreSQL, Oracle Database (you must supply your own license), or SQL Server Express — can be run nonstop monthly as long as you use a Single-AZ db.t2.micro instance, along with 20 GB of SSD-backed database storage and 20 GB of backups.

- [RDS Aurora Cluster]({{< relref "/docs/reference/pkg/aws/rds/cluster" >}})
- [RDS Instance]({{< relref "/docs/reference/pkg/aws/rds/instance" >}})
- [Managing your MySQL databases with Pulumi]({{< relref "/blog/managing-your-mysql-databases-with-pulumi" >}})
- [RDS Postgres and Containerized Airflow]({{< relref "/docs/tutorials/aws/aws-ts-airflow" >}})

[**AWS Step Functions**](https://aws.amazon.com/step-functions/): AWS Step Functions orchestrates AWS Lambda functions and multiple AWS services by sequencing them into applications. The output of a step function is an input to the next, executing each step in order according to your business logic. Step Functions control sequencing, perform error handling and retry logic, and maintain state. Four thousand state transitions are free each month.

- [AWS Step Functions]({{< relref "/docs/tutorials/aws/aws-ts-stepfunctions" >}})
- [Intro to AWS Serverless Step Functions]({{< relref "/blog/intro-to-step-functions" >}})
- [Step Function State Machine]({{< relref "/docs/reference/pkg/aws/sfn/statemachine" >}})

## Azure

Similar to Amazon, Azure offers both an always free tier and 12 months free to new users. Azure also includes a $200 credit for 30 days after signing up. A list of free services and their terms are [available](https://azure.microsoft.com/en-us/free/free-account-faq/). Let's take a look at how we can use some of these resources to build infrastructure.

[**Azure Active Directory**](https://azure.microsoft.com/en-us/services/active-directory/): Azure AD identity service provides single sign-on and multi-factor authentication to protect your users. Up to 50,000 authentications per month are available free.

- [AzureAD]({{< relref "/docs/intro/cloud-providers/azuread" >}})
- [Azure Active Directory with SAML]({{< relref "/docs/guides/saml/aad" >}})

[**Azure App Service**](https://azure.microsoft.com/en-us/services/app-service/): Build, deploy, and scale web apps and APIs. Whether your application is .NET, .NET Core, Node.js, Java, Python, or PHP, in containers or running on Windows or Linux, you can deploy it on a fully managed platform that handles over 40 billion requests per day. Up to 10 web, mobile, or API apps can be created at no charge.

- [Azure App Service with SQL Database and Application Insights]({{< relref "/docs/tutorials/azure/azure-ts-appservice" >}})
- [Todo App Using Azure App Service with SQL Database and Integrated with Azure DevOps]({{< relref "/docs/tutorials/azure/azure-ts-appservice-devops" >}})

[**Azure Cosmos DB**](https://azure.microsoft.com/en-us/services/cosmos-db/): Cosmos DB is a managed NoSQL database service backed by open-source APIs for MongoDB and Cassandra. Up to 500 GB of storage and 400 request units per second are available for free each month.

- [Azure Cosmos DB, an API Connection, and a Logic App]({{< relref "/docs/tutorials/azure/azure-ts-cosmosdb-logicapp" >}})
- [How To Build Globally Distributed Applications with Azure Cosmos DB and Pulumi]({{< relref "/blog/how-to-build-globally-distributed-applications-with-azure-cosmos-db-and-pulumi" >}})
- [Azure Kubernetes Service (AKS) App Using CosmosDB](https://github.com/pulumi/examples/blob/master/azure-ts-aks-mean)
- [Globally Distributed Serverless URL Shortener Using Azure Functions and Cosmos DB](https://github.com/pulumi/examples/blob/master/azure-ts-serverless-url-shortener-global)

[**Azure Functions**](https://azure.microsoft.com/en-us/services/functions/): Functions are an event-driven serverless compute platform for solving complex orchestration problems. You can build and debug locally without additional setup, deploy and operate at scale in the cloud, and integrate services using triggers and bindings. Up to 1 million requests per month are free.

- [Azure Functions]({{< relref "/docs/tutorials/azure/azure-ts-functions" >}})
- [Ten Pearls With Azure Functions in Pulumi]({{< relref "/blog/ten-pearls-with-azure-functions-in-pulumi" >}})
- [Deploy a Function App with KEDA (Kubernetes-based Event-Driven Autoscaling)]({{< relref "/blog/deploy-a-function-app-with-keda" >}})

[**Azure Kubernetes Service (AKS)**](https://docs.microsoft.com/en-us/azure/aks/): Azure AKS deploys containerized applications with a fully managed Kubernetes service. AKS includes serverless Kubernetes and an integrated continuous integration and continuous delivery (CI/CD) experience.

- [Azure Kubernetes Service (AKS) - Hello World!]({{< relref "/docs/tutorials/kubernetes/aks" >}})
- [Azure Kubernetes Service (AKS) Cluster]({{< relref "/docs/tutorials/azure/azure-py-aks" >}})
- [Create AKS Clusters with monitoring and logging using Pulumi-Azure open source SDKs]({{< relref "/blog/create-aks-clusters-with-monitoring-and-logging-with-pulumi-azure-open-source-sdks" >}})
- [Multiple Azure Kubernetes Service (AKS) Clusters]({{< relref "/docs/tutorials/azure/azure-ts-aks-multicluster" >}})

## Google Cloud

Google Cloud has over 20 free services with monthly limits and provides a $300 credit with a new account. Services offered by Google Cloud run on the same infrastructure as their public services. A complete listing of services available on the free tier is [available here](https://cloud.google.com/free).

[**Google Compute Engine**](https://cloud.google.com/compute): Compute Engine provides predefined virtual machine configurations ranging from small general purpose instances to large memory-optimized or fast compute-optimized instances with up to 60 vCPUs. You can create a virtual machine that best fits your workloads.

- [Web Server Virtual Machine Instance on GCE]({{< relref "/docs/tutorials/gcp/gce-webserver" >}})
- [Nginx Server Using Compute Engine](https://github.com/pulumi/examples/tree/master/gcp-py-instance-nginx)
- [Google Cloud Network and Instance with ComponentResource](https://github.com/pulumi/examples/tree/master/gcp-py-network-component)

[**Google Cloud Functions**](https://cloud.google.com/functions): Cloud Functions connect and extend third-party services with code and go to production with end-to-end solutions and complex workflows. Cloud Functions automatically manages and scales underlying infrastructure with the size of workload without server management. The free tier provides two million invocations, both background and HTTP, are free each month. Five GB of outbound network data, 400,000 GB-seconds, and 200,000 GHz-seconds of compute time are included.

- [Simple Serverless programming with Google Cloud Functions and Pulumi]({{< relref "/blog/simple-serverless-programming-with-google-cloud-functions-and-pulumi" >}})
- [Google Cloud Functions in Python deployed with Go]({{< relref "/docs/tutorials/gcp/gcp-go-functions" >}})
- [Google Cloud Functions in Python]({{< relref "/docs/tutorials/gcp/gcp-py-functions" >}})
- [Google Cloud Functions in Python and Go Deployed with TypeScript](https://github.com/pulumi/examples/tree/master/gcp-ts-serverless-raw)

[**Google Cloud Run**](https://cloud.google.com/run): Cloud Run lets you deploy containerized applications on a fully managed serverless platform. Use any container images, and your application automatically scales up or down based on traffic. You can set up triggers to receive events from 60+ Google Cloud sources, and each service gets an out-of-the-box stable HTTPS endpoint, with TLS termination.

- [Google Cloud Run]({{< relref "/docs/tutorials/gcp/gcp-ts-cloudrun" >}})
- [Google Cloud Run: Serverless Containers]({{< relref "/blog/google-cloud-run-serverless-containers" >}})
- [Docker Build and Push to GCR and Deploy to Google Cloud Run using separate projects]({{< relref "/docs/tutorials/gcp/gcp-ts-docker-gcr-cloudrun" >}})

[**Google Cloud Google Kubernetes Engine**](https://cloud.google.com/kubernetes-engine): Secured and managed Kubernetes service with four-way auto scaling and multi-cluster support. GKE provides horizontal pod autoscaling based on CPU utilization or metrics. It automatically scales the node pool and clusters across multiple node pools based on changing workload requirements.

- [Google Kubernetes Engine (GKE) Tutorial]({{< relref "/docs/tutorials/kubernetes/gke" >}})
- [Google Kubernetes Engine (GKE) Cluster]({{< relref "/docs/tutorials/gcp/gcp-ts-gke-hello-world" >}})
- [Google Kubernetes Engine (GKE) with a Canary Deployment](https://github.com/pulumi/examples/tree/master/gcp-py-gke)
- [Containerized Ruby on Rails App Delivery on GCP](https://github.com/pulumi/examples/tree/master/gcp-ts-k8s-ruby-on-rails-postgresql)

## Summary

As you can see, there are many opportunities to get you started on your cloud engineering journey. Whether it's a major cloud service provider or a specialized service, Pulumi has you covered. There are more examples available on [GitHub](https://github.com/pulumi/examples), and you can always join us on [Community Slack](pulumi-community.slack.com) if you have questions.
