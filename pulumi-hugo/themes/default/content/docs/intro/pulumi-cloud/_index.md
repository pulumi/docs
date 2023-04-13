---
title_tag: "Overview of The Pulumi Cloud"
title: "Pulumi Cloud"
meta_desc: The Pulumi Cloud web application automatically manages deployment state and enables collaboration between developers and operators.
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

The [Pulumi Cloud](https://app.pulumi.com) web application automatically manages deployment state and enables collaboration between developers and operators. The Pulumi CLI automatically uses the Pulumi Cloud unless you use a [self-managed backend](/docs/intro/concepts/state/).

## Getting Started

In your browser, navigate to <a href="https://app.pulumi.com" target="_blank">app.pulumi.com</a> and create an account.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>

When you sign in to the Pulumi Cloud, an personal account is automatically
created on the **Individual** Edition. The Pulumi Individual Edition is free forever for unlimited individual use.

You can create an unlimited number of stacks, encrypt configuration and resource secrets, and browse stack history. To collaborate with other developers or use advanced features like [SAML SSO](/docs/guides/saml/), you'll need to create a Pulumi [organization](/docs/intro/pulumi-cloud/organizations/).

The following editions are also available as upgrade options:

* **Pulumi Team** is ideal for teams of up to 10 members and provides the basics of infrastructure as code in popular languages, enabling teams to ship faster.

* **Pulumi Enterprise** is ideal for large teams and organizations in production. It offers an unlimited number of members and teams and provides full cloud engineering capabilities.

* **Pulumi Business Critical** is ideal for enterprises that have specific requirements, like advanced security and compliance features, premium support, and self-hosting options.

For more information about the specific differences and capabilities offered for the
Pulumi Team, Enterprise and Business Critical editions, refer to the [pricing page](/pricing/).

Explore the following sections to learn more about the features and benefits of using the Pulumi Cloud.

## Accounts & Organizations

* [Accounts](/docs/intro/pulumi-cloud/accounts/)
* [Organizations](/docs/intro/pulumi-cloud/organizations/)
* [Access Tokens](/docs/intro/pulumi-cloud/accounts#access-tokens)
* [SAML Integrations](/docs/guides/saml/)

## Collaboration

Collaborate with other developers and coordinate on updates. Provide fine-grained access to stacks and use RBAC (Role-based Access Control) for your organization.

* [Organization Roles](/docs/intro/pulumi-cloud/organizations#organization-roles)
* [Teams](/docs/intro/pulumi-cloud/teams/)
* [Stack Permissions](/docs/intro/pulumi-cloud/projects-and-stacks#stack-permissions)
* [Project and Stack Management](/docs/intro/pulumi-cloud/projects-and-stacks/)
* [Audit Logs](/docs/intro/pulumi-cloud/audit-logs/)
* [Pulumi Insights](insights)

## Integrations and Extensions

Integrate Pulumi with your current continuous delivery pipeline. Build your own extensions, and create reusable templates.

* [CI/CD Integration Assistant](/docs/intro/pulumi-cloud/ci-cd-integration-assistant)
* [Pulumi Servuce Provider](/registry/packages/pulumiservice/): A Pulumi Provider To Configure Pulumi
* [Continuous Delivery](/docs/guides/continuous-delivery/)
* [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/)
* [Webhooks](/docs/intro/pulumi-cloud/webhooks/)
* ["Deploy with Pulumi" Button](/docs/intro/pulumi-cloud/pulumi-button)
