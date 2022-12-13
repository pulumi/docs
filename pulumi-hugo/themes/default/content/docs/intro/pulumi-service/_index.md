---
title: Overview of The Pulumi Service
meta_desc: The Pulumi Service web application automatically manages deployment state and enables collaboration between developers and operators.
menu:
  intro:
    identifier: pulumi-service
    weight: 5
no_on_this_page: true
aliases:
- /docs/reference/service
- /docs/intro/console/accounts-and-organizations/editions/
- /docs/intro/console/
---

The [Pulumi Service](https://app.pulumi.com) web application automatically manages deployment state and enables collaboration between developers and operators. The Pulumi CLI automatically uses the Pulumi Service unless you use a [self-managed backend](/docs/intro/concepts/state/).

## Getting Started

In your browser, navigate to <a href="https://app.pulumi.com" target="_blank">app.pulumi.com</a> and create an account.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>

When you sign in to the Pulumi Service, an personal account is automatically
created on the **Individual** Edition. The Pulumi Individual Edition is free forever for unlimited individual use.

You can create an unlimited number of stacks, encrypt configuration and resource secrets, and browse stack history. To collaborate with other developers or use advanced features like [SAML SSO](/docs/guides/saml/), you'll need to create a Pulumi [organization](/docs/intro/pulumi-service/organizations/).

The following editions are also available as upgrade options:

* **Pulumi Team** is ideal for teams of up to 10 members and provides the basics of infrastructure as code in popular languages, enabling teams to ship faster.

* **Pulumi Enterprise** is ideal for large teams and organizations in production. It offers an unlimited number of members and teams and provides full cloud engineering capabilities.

* **Pulumi Business Critical** is ideal for enterprises that have specific requirements, like advanced security and compliance features, premium support, and self-hosting options.

For more information about the specific differences and capabilities offered for the
Pulumi Team, Enterprise and Business Critical editions, refer to the [pricing page](/pricing/).

Explore the following sections to learn more about the features and benefits of using the Pulumi Service.

## Accounts & Organizations

* [Accounts](/docs/intro/pulumi-service/accounts/)
* [Organizations](/docs/intro/pulumi-service/organizations/)
* [Access Tokens](/docs/intro/pulumi-service/accounts#access-tokens)
* [SAML Integrations](/docs/guides/saml/)

## Collaboration

Collaborate with other developers and coordinate on updates. Provide fine-grained access to stacks and use RBAC (Role-based Access Control) for your organization.

* [Organization Roles](/docs/intro/pulumi-service/organizations#organization-roles)
* [Teams](/docs/intro/pulumi-service/teams/)
* [Stack Permissions](/docs/intro/pulumi-service/projects-and-stacks#stack-permissions)
* [Project and Stack Management](/docs/intro/pulumi-service/projects-and-stacks/)
* [Audit Logs](/docs/intro/pulumi-service/audit-logs/)

## Integrations and Extensions

Integrate Pulumi with your current continuous delivery pipeline. Build your own extensions, and create reusable templates.

* [CI/CD Integration Assistant](/docs/intro/pulumi-service/ci-cd-integration-assistant)
* [Pulumi Service Provider](/registry/packages/pulumiservice/): A Pulumi Provider To Configure Pulumi
* [Continuous Delivery](/docs/guides/continuous-delivery/)
* [Pulumi Service REST API](/docs/reference/service-rest-api/)
* [Webhooks](/docs/intro/pulumi-service/webhooks/)
* ["Deploy with Pulumi" Button](/docs/intro/pulumi-service/pulumi-button)
