---
title_tag: "Using Pulumi Deployments"
meta_desc: Learn how to configure and use Pulumi Deployments to automate your infrastructure deployments
title: "Using Deployments"
h1: "Using Pulumi Deployments"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: Using Deployments
    parent: pulumi-cloud-deployments
    weight: 2
    identifier: pulumi-cloud-deployments-using
aliases:
  - /docs/intro/deployments/reference/
  - /docs/pulumi-cloud/deployments/reference/
  - /docs/pulumi-cloud/deployments/using-deployments/
---

This page provides an overview of how to use Pulumi Deployments to automate your infrastructure deployments.

## Getting Started with Deployments

Pulumi Deployments are configured on a per-stack basis. To use Deployments effectively, follow these steps:

1. **Configure Deployment Settings**: First, set up your [deployment settings](./settings) which include source code location, cloud credentials, environment variables, and build requirements.
1. **Set Up Triggers**: Configure how [deployment triggers](./triggers) are initiated. A common pattern is to:
   - Run a `pulumi preview` when a PR is created
   - Run a `pulumi up` when a PR is merged to main
1. **Expand Your Usage**: As you grow more comfortable with Deployments, consider using additional features:
   - [Drift detection](../drift) to automatically detect when your infrastructure differs from its desired state
   - [Review stacks](../review-stacks) for temporary environments on PRs
   - [TTL stacks](../ttl) for ephemeral environments
   - [Post-deployment automation](./post-automation) for dependent stack updates
   - [Webhooks](/docs/pulumi-cloud/webhooks/#deployment-webhooks) for custom automation

## Automating at Scale

For teams managing many stacks or platforms serving multiple teams, you can automate Deployments at scale using:

- The **[Pulumi Cloud Provider](/registry/packages/pulumiservice/api-docs/deploymentsettings)**: Manage deployment settings as code
- The **[REST API](../api)**: Programmatically control all aspects of Deployments

## Additional Resources

- [Deployment Settings](./settings): Configure your source code, credentials, environment variables, and more
- [Deployment Triggers](./triggers): Control how deployments are initiated
- [Private Repositories and Packages](./private-repositories): Configure access to private Git repositories and package feeds
- [Post-Deployment Automation](./post-automation): Set up automated workflows after deployments complete
