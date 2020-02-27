---
title: "Pulumi 1.0"
authors: ["joe-duffy"]
tags: ["Pulumi-News"]
meta_desc: "We are excited to announce Pulumi 1.0, a modern infrastructure as code platform that works for any cloud, AWS, Azure, GCP, or Kubernetes included."
date: "2019-09-05"

meta_image: "pulumi-1-0.png"
---

Today we are excited to announce the general availability of Pulumi 1.0. Pulumi is a modern infrastructure as code tool that lets you declare infrastructure using real languages, with a SaaS management console for configuring identities, organizations, and related policies. By using real languages, developers and operators are able to work better together, sharing and reusing best practices, accomplishing new levels of automation, and unlocking access to ecosystems of existing tools. The 1.0 release is a siginificant milestone for us, our community, and our customers, and signals completeness, stability, and compatibility.

## What is Pulumi?

Using Pulumi, you:

* **Declare infrastructure** in TypeScript, JavaScript, Python, or Go.
* **Leverage tools** such as libraries, package managers, IDEs, and test frameworks from your language of choice.
* **Access all of the services from many clouds**, including AWS, Azure, GCP, Kubernetes, and DigitalOcean.
* **Use the Pulumi CLI or CI/CD integrations** to perform deployments predictably and reliably.
* **Build modern, reliable, and scalable applications** using a multitude of cloud architectures, including containers, serverless functions, and static websites.
* **Use higher level frameworks** that abstract away tedious aspects of cloud development.

This functionality is delivered through an open source SDK consisting of a CLI and assorted libraries. Pulumi also provides a hosted service for improved usability, reliability, security, and other management features.

## Additional Features

In addition to the core infrastructure as code features, Pulumi's SDK offers:

* **Stack management**: deploy to and promote between multiple environments.
* **State storage**: use the free Pulumi service or choose instead to manually manage state in AWS S3, Azure Storage, Google Cloud Storage, or the filesystem.
* **Configuration**: easily manage different configuration between environments.
* **Encrypted secrets**: use the free Pulumi KMS service to encrypt sensitive configuration, such as passwords or tokens, or plug in AWS KMS, Azure KeyVault, GCP KMS, or HashiCorp Vault.

Using Pulumi in conjunction with the Pulumi service delivers the following additional features:

* **Pulumi Console**: a dashboard for gaining visibility into and managing your deployments.
* **Identity**: user and organization identity provider integrations with GitHub, GitLab, Atlassian, or SAML/SSO, including Active Directory, Okta, Google G Suite, and others.
* **Role based access controls**: team management, also integrated with your identity provider.
* **REST API and Webhooks**: a fully programmable web API for advanced automation scenarios.
* **CI/CD Integrations**: automated deployment integrations with Azure DevOps, AWS Code Services, CircleCI, Codefresh, GitHub, GitLab, Google Cloud Build, Jenkins, Travis, and others.

The Pulumi service is available as a free Community Edition as well as advanced Team and Enterprise SaaS editions for larger teams looking for robust enterprise capabilities.

## Why Pulumi?

Using real languages offers significant advantages for declaring your infrastructure:

* **Control flow**: use if statements, for loops, case statements, etc.
* **Abstractions and reuse**: leverage classes and functions to avoid repeating the same boilerplate over and over again
* **Package managers**: share libraries with your team or the community
* **IDEs**: use your favorite IDE and get statement completion, live error checking, and interactive documentation
* **Project organization**: use modules and well known techniques for managing complex projects
* **Testing**: apply standard test tools, frameworks, and techniques to infrastructure
* **Code review**: use existing code review practices for infrastructure changes

This approach unlocks access to entire ecosystems that aren't available to markup DSLs. This approach also helps developers and operators work better together using a shared foundation.

## How Pulumi Works

Although Pulumi uses general-purpose imperative languages, it is declarative. The program simply declares a set of resources and the Pulumi engine orchestrates all CRUD operations.

Packages in your language of choice provide full access to many clouds, including AWS, Azure, GCP, Kubernetes, DigitalOcean, and more. Each package projects the full set of services from the underlying cloud provider as classes and APIs. Declaring a new S3 bucket is as easy as:

```typescript
let b = new aws.s3.Bucket("my-bucket", { acl: "private" });
```

Because of higher level components, even creating a new Kubernetes cluster is this easy:

```typescript
let cluster = new eks.Cluster("my-cluster");
export let kubeconfig = cluster.kubeconfig;
```

The `pulumi up` CLI command runs this program using Pulumi's multi-language engine, and presents a plan for review &mdash; including an overview of the resources to create, update, and/or delete. After you choose to apply those changes, the Pulumi engine coordinates those API calls in parallel to accomplish your deployment.

To see this workflow in action, watch this short 5 minute video:

{{< youtube "QfJTJs24-JM" >}}

## How to Get It

The Pulumi 1.0 milestone signals completeness, stability, and compatibility, and is the result of two years of work helping 1,000s of customers take modern cloud architectures across many clouds into production. This includes startups and Global 2000s looking to innovate faster using the cloud.

If you're already a Pulumi user, simply upgrade in the usual ways.

If this is your first time using Pulumi, [give it a try today](https://pulumi.com/docs/get-started). It is open source and free to use.

For more information about Pulumi Team and Enterprise editions, visit [our products page](https://pulumi.com/product).

We'd like to sincerely thank our community and customers for coming along on this journey with us. Without you, we couldn't have reached this milestone. We hope you enjoy Pulumi 1.0!
