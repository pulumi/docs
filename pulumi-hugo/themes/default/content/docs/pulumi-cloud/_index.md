---
title_tag: Pulumi Cloud Overview
meta_desc: Pulumi Cloud is a secure cloud service for individuals and teams using Pulumi's open-source SDK and Pulumi ESC.
title: Pulumi Cloud
h1: Pulumi Cloud overview
no_on_this_page: true
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  pulumicloud:
    name: Overview
    identifier: pulumi-cloud

aliases:
- /docs/reference/service/
- /docs/intro/console/accounts-and-organizations/editions/
- /docs/intro/console/
- /docs/intro/pulumi-service/
- /docs/intro/pulumi-cloud/
---

[Pulumi Cloud](https://app.pulumi.com) is a secure cloud service for individuals and teams using Pulumi's open-source SDK and Pulumi Environments, Secrets and Configuration (ESC). It manages deployment state and secrets, enables search across your clouds, runs deployments, integrates with CI/CD, and enforces policies and access controls.

The Pulumi CLI automatically uses Pulumi Cloud unless you set up a [self-managed backend](/docs/concepts/state/#using-a-self-managed-backend).

## Getting started

In your browser, navigate to <a href="https://app.pulumi.com" target="_blank">app.pulumi.com</a> and create an account.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>

When you sign in to Pulumi Cloud, a personal organization is automatically
created on the **Individual** Edition. The Pulumi Individual Edition is free forever for unlimited individual use.

You can create an unlimited number of stacks, encrypt configuration and resource secrets, and browse stack history. To collaborate with other developers or use advanced features like [SAML SSO](/docs/pulumi-cloud/access-management/saml/), you'll need to create a Pulumi [organization](/docs/pulumi-cloud/organizations/).

## Key features

Explore the following sections to learn more about the features and benefits of using Pulumi Cloud.

### Identity and organizations

* [Accounts](/docs/pulumi-cloud/accounts/)
* [Organizations](/docs/pulumi-cloud/organizations/)
* [Personal Access Tokens](/docs/pulumi-cloud/accounts/#personal-access-tokens)
* [Organization and Team Access Tokens](/docs/pulumi-cloud/access-management/organization-access-tokens/)
* [SAML Integrations](/docs/pulumi-cloud/access-management/saml/)

### Teams and collaboration

Collaborate with other developers and coordinate on updates. Provide fine-grained access to stacks and use RBAC (Role-based Access Control) for your organization.

* [Organization Roles](/docs/pulumi-cloud/organizations#organization-roles)
* [Teams](/docs/pulumi-cloud/access-management/teams/)
* [Stack Permissions](/docs/pulumi-cloud/projects-and-stacks#stack-permissions)
* [Project and Stack Management](/docs/pulumi-cloud/projects-and-stacks/)

### Pulumi Environments, Secrets and Configuration (ESC)

Pulumi ESC Environments allow teams to tackle configuration complexity at scale, alleviating maintenance and operational burden and reducing costly mistakes, and creating a more secure by default posture.

* [Pulumi ESC](/docs/using-pulumi/esc/)
* [Pulumi ESC Syntax Reference](/docs/using-pulumi/esc/reference/)

### CI/CD integrations and extensions

Integrate Pulumi with your current continuous delivery pipeline. Build your own extensions, and create reusable templates.

* [CI/CD Integration Assistant](/docs/pulumi-cloud/deployments/ci-cd-integration-assistant/)
* [Pulumi Service Provider](/registry/packages/pulumiservice/): A Pulumi Provider To Configure Pulumi
* [Continuous Delivery](/docs/using-pulumi/continuous-delivery/)
* [Pulumi Cloud REST API](/docs/pulumi-cloud/cloud-rest-api/)
* [Webhooks](/docs/pulumi-cloud/webhooks/)

### Hosted Deployments service

* [Pulumi Deployments](/docs/pulumi-cloud/deployments/)
* [Deploy with Pulumi Button](/docs/pulumi-cloud/pulumi-button)

### Insights and Analytics

* [Pulumi Insights: Resource Search, Data Export](/docs/intro/insights)

### Security and compliance

* [Audit Logs](/docs/pulumi-cloud/audit-logs/)
* [Policy Packs](/docs/using-pulumi/crossguard/configuration/)
* [Pulumi Cloud security whitepaper](/security/pulumi-cloud-security-whitepaper.pdf): Pulumi Cloud is multi-tenanted and runs within an AWS Virtual Private Cloud (VPC). All communications between Pulumi clients and the server are encrypted using TLS. Pulumi is SOC 2 Type II certified.

## Upgrade editions

The following editions are also available as upgrade options:

* **Pulumi Team** is ideal for teams of up to 10 members and provides the basics of infrastructure as code in popular languages, enabling teams to ship faster. Includes 150K free credits each month.

* **Pulumi Enterprise** is ideal for large teams and organizations in production. It offers an unlimited number of members and teams and provides full cloud engineering capabilities.

* **Pulumi Business Critical** is ideal for enterprises that have specific requirements, like advanced security and compliance features, premium support, and [self-hosting options](/docs/pulumi-cloud/self-hosted/).

For more information about the specific differences and capabilities offered for the
Pulumi Team, Enterprise and Business Critical editions, refer to the [pricing page](/pricing/).
