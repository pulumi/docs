---
title_tag: "Using Pulumi Deployments"
meta_desc: Learn how to configure and use Pulumi Deployments to automate your infrastructure deployments
title: "Using Deployments"
h1: "Using Pulumi Deployments"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: Using Deployments
    parent: deployments-deployments
    weight: 20
    identifier: deployments-deployments-using
aliases:
- /docs/pulumi-cloud/deployments/using/
- /docs/intro/deployments/reference/
- /docs/pulumi-cloud/deployments/reference/
- /docs/pulumi-cloud/deployments/using-deployments/
- /docs/deployments/deployments/reference/
- /docs/platform/deployments/reference/

---

This page provides an overview of how to use Pulumi Deployments to automate your infrastructure deployments.

## Getting Started with Deployments

Pulumi Deployments are configured on a per-stack basis. To use Deployments effectively, follow these steps:

1. **Configure Deployment Settings**: First, set up your [deployment settings](/docs/deployments/deployments/using/settings) which include source code location, cloud credentials, environment variables, and build requirements.
1. **Set Up Triggers**: Configure how [deployment triggers](/docs/deployments/deployments/using/triggers) are initiated. A common pattern is to:
   - Run a `pulumi preview` when a PR is created
   - Run a `pulumi up` when a PR is merged to main
1. **Expand Your Usage**: As you grow more comfortable with Deployments, consider using additional features:
   - [Drift detection](/docs/deployments/deployments/drift) to automatically detect when your infrastructure differs from its desired state
   - [Review stacks](/docs/deployments/deployments/review-stacks) for temporary environments on PRs
   - [TTL stacks](/docs/deployments/deployments/ttl) for ephemeral environments
   - [Post-deployment automation](/docs/deployments/deployments/using/post-automation) to create webhooks to trigger additional actions, like updating additional stacks
   - [Webhooks](/docs/deployments/webhooks/#deployment-webhooks) for custom automation

## Automating at Scale

For teams managing many stacks or platforms serving multiple teams, you can automate Deployments at scale using:

- The **[Pulumi Cloud Provider](/registry/packages/pulumiservice/api-docs/deploymentsettings)**: Manage deployment settings as code
- The **[REST API](/docs/deployments/deployments/api)**: Programmatically control all aspects of Deployments

## Additional Resources

- [Private Repositories and Packages](/docs/deployments/deployments/using/private-repositories): Configure access to private Git repositories and package feeds
