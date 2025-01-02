---
title: Get started with Pulumi Cloud
meta_desc: How to set up an account and get started with Pulumi Cloud.
menu:
    cloud:
        name: Get started
        parent: cloud-home
        weight: 1
        identifier: pulumi-cloud-get-started
---

{{% notes type="info" %}}
An **onboarding guide** is available to guide you through setting up Pulumi Cloud for your whole team. It not only walks you comprehensively through the full capabilities of Pulumi Cloud, but also recommended best practices. [Read the onboarding guide here](./onboarding-guide). For a briefer introduction to Pulumi Cloud, see the overview below instead. [Contact us](/contact) if you'd like assistance with any of this.
{{% /notes %}}

In your browser, navigate to <a href="https://app.pulumi.com" target="_blank">app.pulumi.com</a> and create an account.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>

When you sign in to Pulumi Cloud, a personal organization is automatically
created on the **Individual** Edition. The Pulumi Individual Edition is free forever for unlimited individual use.

You can create an unlimited number of stacks, encrypt configuration and resource secrets, and browse stack history. To collaborate with other developers or use advanced features like [SAML SSO](/docs/pulumi-cloud/access-management/saml/), you'll need to create a Pulumi [organization](/docs/pulumi-cloud/organizations/).

## Key features

Explore the following sections to learn more about the features and benefits of using Pulumi Cloud.

### Identity and organizations

Pulumi Cloud has a rich set of features around identity, authentication, organizations, teams, roles, and user management. Pulumi Cloud integrates with many popular identity providers like [GitHub](/docs/pulumi-cloud/admin/organizations/#github-identity-provider), [GitLab](/docs/pulumi-cloud/admin/organizations/#gitlab-identity-provider). Pulumi Cloud provides RBAC (Role-based Access Control) for your organization can also do things like [import your teams directly from GitHub](/docs/pulumi-cloud/access-management/teams/#github-based-teams).

* [Organizations](/docs/pulumi-cloud/organizations/) and [Accounts](/docs/pulumi-cloud/accounts/)
* [Teams](/docs/pulumi-cloud/access-management/teams/) and [Roles](/docs/pulumi-cloud/organizations/#organization-roles) Management
* [Project and Stack Management](/docs/pulumi-cloud/projects-and-stacks/)
* [SAML](/docs/pulumi-cloud/access-management/saml/) and [OIDC](/docs/pulumi-cloud/oidc/) Integrations

### Hosted Deployments service and CI/CD integrations

Pulumi Cloud offers a flexible and convenient [hosted deployment service](/docs/pulumi-cloud/deployments/). Pulumi Cloud can also integrate with your current continuous delivery pipeline, and provides tools to build your own extensions, and create reusable templates.

* [Pulumi Deployments](/docs/pulumi-cloud/deployments/)
* [Continuous Delivery](/docs/using-pulumi/continuous-delivery/) and the [CI/CD Integration Assistant](/docs/pulumi-cloud/deployments/ci-cd-integration-assistant/)
* [Pulumi Cloud REST API](/docs/pulumi-cloud/cloud-rest-api/)
* [Webhooks](/docs/pulumi-cloud/webhooks/)

### Pulumi ESC Integration

[Pulumi ESC](/docs/esc/) (Environments, Secrets, and Configuration) allows teams to tackle configuration complexity at scale, alleviating maintenance and operational burden and reducing costly mistakes, and creating a more secure by default posture.

* [Pulumi ESC](/docs/esc/)
* [Pulumi ESC Syntax Reference](/docs/esc/reference/)

### Building developer portals

Dealing with a larger organization? Pulumi Cloud offers all the features you need to build an effective internal developer portal (IDP).

* [New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard) and [Organization Templates](/docs/pulumi-cloud/developer-portals/templates)
* [Pulumi Backstage Plugin](/docs/pulumi-cloud/developer-portals/backstage)
* [Pulumi Insights: Resource Search, Data Export](/docs/intro/insights)

### Security and compliance

Pulumi Cloud offers powerful security and compliance tools.

* [Audit Logs](/docs/pulumi-cloud/audit-logs/)
* [Policy Packs](/docs/using-pulumi/crossguard/configuration/)
* [Pulumi Cloud security whitepaper](/security/pulumi-cloud-security-whitepaper.pdf): Pulumi Cloud is multi-tenanted and runs within an AWS Virtual Private Cloud (VPC). All communications between Pulumi clients and the server are encrypted using TLS. Pulumi is SOC 2 Type II certified.
