---
title: Get started with Pulumi Cloud
meta_desc: How to set up an account and get started with Pulumi Cloud.
menu:
    deployments:
        name: Get Started
        parent: deployments-home
        weight: 1
        identifier: deployments-get-started
aliases:
  - /docs/deployments/get-started/
  - /docs/pulumi-cloud/get-started/
---

Pulumi Cloud is a managed service that provides state management, secrets handling, team collaboration, and automation capabilities for infrastructure as code. It works seamlessly with Pulumi's open source IaC tool to help teams build, deploy, and manage cloud infrastructure.

## Is Pulumi Cloud right for you?

New to Pulumi or evaluating your options? Read [Pulumi Cloud and Open Source Pulumi](/docs/iac/concepts/pulumi-cloud/) to understand:

- How Pulumi Cloud relates to the open source Pulumi IaC tool
- The tradeoffs between using Pulumi Cloud versus self-managed backends
- Why most teams choose Pulumi Cloud for collaboration and security

## Getting started

### For individual developers

The Pulumi Individual Edition is free forever for unlimited individual use. Create an account to start building with Pulumi Cloud:

<a class="btn btn-secondary" href="https://app.pulumi.com/signup">Create an Account</a>

When you sign in, a personal organization is automatically created. You can create unlimited stacks, encrypt configuration and secrets, and browse stack history.

### For teams

{{% notes type="info" %}}
Setting up Pulumi Cloud for your team? The **[Onboarding Guide](/docs/administration/onboarding-guide/)** provides comprehensive guidance on:

- Choosing your deployment model and subscription tier
- Configuring security, testing strategies, and code reusability
- Organizing teams, projects, and collaboration workflows
- Migrating existing infrastructure to Pulumi

[Contact us](/contact/) if you'd like assistance with team onboarding.
{{% /notes %}}

To collaborate with other developers or use advanced features like [SAML SSO](/docs/administration/access-identity/saml/), you'll need to create a Pulumi organization. Learn more about [organizations and teams](/docs/administration/organizations-teams/).

## Core capabilities

### State and secrets management

- **State management**: Automatic state locking, history, and recovery
- **Secrets encryption**: Built-in secrets management with automatic encryption
- **Configuration environments**: Use [Pulumi ESC](/docs/esc/) to organize secrets and configuration across multiple projects

### Deployment and automation

- **[Pulumi Deployments](/docs/deployments/deployments/)**: Hosted Git-based deployments with built-in CI/CD
- **CI/CD integrations**: Connect with [GitHub Actions, GitLab, and other pipelines](/docs/iac/using-pulumi/continuous-delivery/)
- **[Review Stacks](/docs/deployments/deployments/review-stacks/)**: Ephemeral environments for pull request validation
- **[Drift detection](/docs/deployments/deployments/drift/)**: Identify and remediate infrastructure changes made outside IaC

### Team collaboration

- **Identity and access**: [Organizations](/docs/administration/organizations-teams/organizations/), [teams](/docs/administration/organizations-teams/teams/), and role-based access control
- **[SAML/SSO](/docs/administration/access-identity/saml/)**: Enterprise identity provider integration
- **[Audit logs](/docs/administration/security-compliance/audit-logs/)**: Complete activity tracking and compliance reporting
- **[Projects and stacks](/docs/deployments/projects-and-stacks/)**: Organized infrastructure with full deployment history

### Developer experience

- **[Pulumi Neo](/docs/ai/)**: AI agent for infrastructure automation, debugging, code generation, and infrastructure questions
- **[Developer portals](/docs/idp/concepts/)**: Self-service infrastructure with templates and the New Project Wizard
- **[Pulumi Insights](/docs/insights/)**: Search, visualize, and manage cloud resources across your organization

### Extensibility

- **[REST API](/docs/reference/cloud-rest-api/)**: Programmatic access to all Pulumi Cloud features
- **[Webhooks](/docs/deployments/webhooks/)**: Event-driven workflows and custom integrations
- **[Automation API](/docs/iac/using-pulumi/automation-api/)**: Embed IaC capabilities in your own applications

## Next steps

- **Explore features**: Browse the sections in the left navigation to learn about specific Pulumi Cloud capabilities
- **See it in action**: Try the [Get Started tutorial](/docs/iac/get-started/) to deploy your first infrastructure
- **Review security**: Read the [Pulumi Cloud security whitepaper](/security/pulumi-cloud-security-whitepaper) for details on our SOC 2 Type II certified platform
