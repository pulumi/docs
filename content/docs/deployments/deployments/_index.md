---
title_tag: "Pulumi Deployments"
meta_desc: Pulumi Deployments is the fast way for individuals, teams, enterprises, and platforms to go from code to cloud.
title: "Deployments"
h1: "Pulumi Deployments"
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  deployments:
    name: Deployments
    parent: deployments-home
    identifier: deployments-deployments
    weight: 20
aliases:
- /docs/pulumi-cloud/deployments/
- /docs/platform/deployments/
- /docs/intro/pulumi-service/deployments/
- /docs/intro/deployments/
- /docs/intro/deployments/platform/
- /docs/pulumi-cloud/deployments/platform/
---

Pulumi Deployments is a managed CI/CD platform purpose-built for infrastructure as code. It provides everything you need to securely deploy infrastructure changes across your organization, including managed compute, secure secrets handling, and deep integration with version control systems.

## Key features

### Managed infrastructure CI/CD

- **Zero Touch CI/CD**: App teams can select a template from Pulumi Cloud's [New Project Wizard](/docs/idp/concepts/new-project-wizard) and deploy infrastructure in minutes. Learn how with our [Getting Started guide](/docs/deployments/deployments/get-started).
- **Git Integration**: Automatically preview infrastructure changes on pull requests and deploy on merge with our GitHub integration.
- **Live Preview Environments**: Each pull request can automatically create a [review stack](/docs/deployments/deployments/review-stacks) with real infrastructure, letting you validate changes in a production-like environment before merging.
- **Secure by Default**: Integration with [Pulumi ESC](/docs/pulumi-cloud/esc) ensures your secrets and cloud credentials are securely handled.

### Beyond CI/CD

- **Drift Detection**: [Automatically detect](/docs/deployments/deployments/drift) when your infrastructure differs from its desired state.
- **Scheduled Operations**: Run any Pulumi operation (up/preview/refresh) on a [schedule](/docs/deployments/deployments/schedules).
- **Temporary Infrastructure**: Automatically tear down development or testing environments with [TTL stacks](/docs/deployments/deployments/ttl).
- **Custom Compute**: Run Pulumi operations on your own infrastructure with [customer-managed agents](/docs/deployments/deployments/customer-managed-agents).

### Platform engineering features

- **REST API**: Automate infrastructure operations with our [REST API](/docs/deployments/deployments/api/) to build custom workflows and self-service platforms.
- **Deployment Settings**: Define all deployment requirements (source code, credentials, environment variables) in a single configuration, either through the UI or declaratively using the [Pulumi Cloud Provider](/registry/packages/pulumiservice).
- **Multiple Triggers**: Trigger deployments via git push, REST API, UI button, or schedule to support any workflow.
- **Best Practices Built-in**: Follow our [deployment patterns](/docs/deployments/deployments/reference/) to implement infrastructure automation at scale.

## How it works

Pulumi Deployments combines three key components to enable secure, scalable infrastructure deployments:

1. **Deployment Settings**: Define everything needed to deploy your infrastructure:

   - Source code location and branch
   - Cloud credentials and OIDC configuration
   - Environment variables and secrets
   - Build requirements and custom Docker images

1. **Managed Compute**: Run Pulumi operations on secure, isolated compute instances that:

   - Scale automatically with your deployment needs
   - Handle concurrent deployments across your organization
   - Provide detailed logs and status updates
   - Can be replaced with your own compute resources if needed

1. **Flexible Triggers**: Choose how deployments are initiated:

   - Git push to deploy
   - Pull request preview environments
   - REST API calls
   - UI-triggered deployments
   - Scheduled operations
   - Custom automation via the Remote Automation API

## Getting started

The fastest way to get started with Pulumi Deployments is to:

1. Create a new project using the Pulumi Cloud [New Project Wizard](/docs/idp/concepts/new-project-wizard), which will automatically configure Deployments for your repository
1. Follow our [Getting Started guide](/docs/deployments/deployments/get-started) to configure an existing project
1. Explore our [deployment patterns](/docs/deployments/deployments/reference/) to implement common infrastructure automation scenarios

[Get Started](/docs/deployments/deployments/get-started) today!
