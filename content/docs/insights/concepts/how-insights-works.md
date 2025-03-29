---
title_tag: "How Pulumi Insights Account Discovery Works"
meta_desc: An overview of how Pulumi Insights account discovery works.
title: How Pulumi Insights Account Discovery works
h1: How Pulumi Insights Account Discovery works
meta_image: /images/docs/meta-images/docs-meta.png

menu:
  insights:
    parent: insights-concepts
    identifier: how-pulumi-insights-account-discovery-works
    weight: 1
search:
  keywords:
    - Insights
    - Account
    - Account Discovery
    - Resource Explorer
    - Cloud Infrastructure
---

Insights Account Discovery enables organizations to gain visibility into their entire cloud infrastructure through the Pulumi Insights platform. It works by scanning cloud provider accounts and building a comprehensive inventory of resources in the Insights supergraph, regardless of how those resources were created or are currently managed.

Here are some key concepts:

## Account management

The [Accounts page](/docs/insights/accounts/) in the Pulumi Cloud console serves as the central hub for managing the Account Discovery process. From this page, you can:

- View all configured accounts and their current scan status
- Create new accounts
- Monitor the progress of infrastructure discovery
- Configure scanning settings for each account

When you [create a new account](/docs/insights/get-started/create-accounts/), Insights automatically generates child accounts based on your cloud provider's structure. For AWS accounts for example, this means separate child accounts for each region you specify, allowing granular control over the discovery process.

## Resource discovery process

Account Discovery integrates with [Pulumi ESC](/docs/esc/) to securely manage the credentials needed for scanning cloud resources. This integration ensures that credential management follows enterprise security best practices.

During each scan, Insights:

- Authenticates to your cloud provider using read-only credentials from ESC
- Identifies resources present in your account
- Collects detailed metadata about each resource
- Records resource relationships and dependencies
- Updates the Insights supergraph with the latest resource state

## Exploring Your Infrastructure

Once scanning is complete, your resources become available through three main interfaces:

1. [Resource Explorer](/docs/insights/search/) provides a structured view of your infrastructure, with capabilities for grouping, filtering, and sorting resources
2. [Resource Search](/docs/insights/search/) enables you to find specific resources or groups of resources
3. Pulumi [AI assist](/docs/insights/get-started/using-resource-explorer/#ai-assist-examples) and [Copilot](/docs/pulumi-cloud/copilot/) allow natural language queries about your infrastructure, such as "Find all public IP addresses"

The Resource Explorer interface supports:

- Custom grouping by dragging and dropping column headers
- Advanced filtering through column-specific filters
- Flexible column management for customized views
- Direct access to resource metadata and relationships

## Resource Relationships

Insights maintains a graph of relationships between your resources. For example, it tracks connections between:

- S3 buckets and their associated bucket policies
- Virtual machines and their attached storage
- Network interfaces and security groups
