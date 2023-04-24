---
title_tag: "Overview of Pulumi Cloud"
title: "Pulumi Cloud"
meta_desc: Pulumi Cloud is a secure cloud service for individuals and teams using Pulumi's open-source SDK.
menu:
  intro:
    identifier: pulumi-cloud
    weight: 5
no_on_this_page: true
aliases:
- /docs/reference/service/
- /docs/intro/console/accounts-and-organizations/editions/
- /docs/intro/console/
- /docs/intro/pulumi-service/
---

[Pulumi Cloud](https://app.pulumi.com) is a secure cloud service for individuals and teams using Pulumi's open-source SDK. It manages deployment state and secrets, enables search across your clouds, runs deployments, integrates with CI/CD, and enforces policies and access controls.

The Pulumi CLI automatically uses Pulumi Cloud unless you set up a [self-managed backend](/docs/intro/concepts/state/#using-a-self-managed-backend).

## Getting Started

In your browser, navigate to <a href="https://app.pulumi.com" target="_blank">app.pulumi.com</a> and create an account.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>

When you sign in to Pulumi Cloud, a personal organization is automatically
created on the **Individual** Edition. The Pulumi Individual Edition is free forever for unlimited individual use.

You can create an unlimited number of stacks, encrypt configuration and resource secrets, and browse stack history. To collaborate with other developers or use advanced features like [SAML SSO](/docs/guides/saml/), you'll need to create a Pulumi [organization](/docs/intro/pulumi-cloud/organizations/).

## Key features

Explore the following sections to learn more about the features and benefits of using Pulumi Cloud.

### Identity and Organizations

* [Accounts](/docs/intro/pulumi-cloud/accounts/)
* [Organizations](/docs/intro/pulumi-cloud/organizations/)
* [Personal Access Tokens](/docs/intro/pulumi-cloud/accounts/#personal-access-tokens)
* [Organization and Team Access Tokens](/docs/intro/pulumi-cloud/organization-access-tokens/)
* [SAML Integrations](/docs/guides/saml/)

### Teams and Collaboration

Collaborate with other developers and coordinate on updates. Provide fine-grained access to stacks and use RBAC (Role-based Access Control) for your organization.

* [Organization Roles](/docs/intro/pulumi-cloud/organizations#organization-roles)
* [Teams](/docs/intro/pulumi-cloud/teams/)
* [Stack Permissions](/docs/intro/pulumi-cloud/projects-and-stacks#stack-permissions)
* [Project and Stack Management](/docs/intro/pulumi-cloud/projects-and-stacks/)

### CI/CD Integrations and Extensions

Integrate Pulumi with your current continuous delivery pipeline. Build your own extensions, and create reusable templates.

* [CI/CD Integration Assistant](/docs/intro/pulumi-cloud/ci-cd-integration-assistant)
* [Pulumi Service Provider](/registry/packages/pulumiservice/): A Pulumi Provider To Configure Pulumi
* [Continuous Delivery](/docs/guides/continuous-delivery/)
* [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/)
* [Webhooks](/docs/intro/pulumi-cloud/webhooks/)

### Hosted Deployments Service

* [Pulumi Deployments](/docs/intro/deployments/)
* [Deploy with Pulumi Button](/docs/intro/pulumi-cloud/pulumi-button)

### Insights and Analytics

* [Pulumi Insights: Resource Search, Data Export](/docs/intro/insights)

### Security and Compliance

* [Audit Logs](/docs/intro/pulumi-cloud/audit-logs/)
* [Policy Packs](/docs/guides/crossguard/configuration/)
* [Pulumi Cloud security whitepaper](/security/pulumi-cloud-security-whitepaper.pdf): Pulumi Cloud is multi-tenanted and runs within an AWS Virtual Private Cloud (VPC). All communications between Pulumi clients and the server are encrypted using TLS. Pulumi is SOC 2 Type II certified.

## Upgrade Editions

The following editions are also available as upgrade options:

* **Pulumi Team** is ideal for teams of up to 10 members and provides the basics of infrastructure as code in popular languages, enabling teams to ship faster. Includes 150K free credits each month.

* **Pulumi Enterprise** is ideal for large teams and organizations in production. It offers an unlimited number of members and teams and provides full cloud engineering capabilities.

* **Pulumi Business Critical** is ideal for enterprises that have specific requirements, like advanced security and compliance features, premium support, and [self-hosting options](/docs/guides/self-hosted/).

For more information about the specific differences and capabilities offered for the
Pulumi Team, Enterprise and Business Critical editions, refer to the [pricing page](/pricing/).
