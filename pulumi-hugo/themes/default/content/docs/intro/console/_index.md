---
title: Pulumi Console
meta_desc: An overview of the Pulumi Console web application.
menu:
  intro:
    identifier: console
    weight: 5
no_on_this_page: true
aliases:
- /docs/reference/service
- /docs/intro/console/accounts-and-organizations/editions/
---

The [Pulumi Console](https://app.pulumi.com) web application automatically manages deployment state and enables collaboration between developers and operators. The Pulumi CLI automatically uses it unless you [explicitly opt out]({{< relref "/docs/intro/concepts/state" >}}).

## Getting Started

In your browser, navigate to <a href="https://app.pulumi.com" target="_blank">app.pulumi.com</a> and sign up.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Sign up</a>

When you sign into the Pulumi Console, an personal account is automatically
created on the **Individual** Edition. The Pulumi Individual Edition is free forever for unlimited individual use.

You can create an unlimited number of stacks, encrypt configuration and resource secrets, and browse stack history. To collaborate with other developers or use advanced features like [SAML SSO]({{< relref "/docs/guides/saml" >}}), you'll need to create a Pulumi [organization]({{< relref "organizations" >}}).

The following editions are also available as upgrade options:

* **Pulumi Team** is ideal for teams of all sizes from just getting started deploying cloud
applications and infrastructure to managing multiple projects and/or clouds.

* **Pulumi Enterprise** is ideal for large organizations running cloud software at
scale, with advanced or custom needs.

For more information about the specific differences and capabilities offered for the
Pulumi Team and Enterprise editions, refer to the [pricing page]({{< relref "/pricing" >}}).

Explore the following sections to learn more about the features and benefits of using the Pulumi Console.

## Accounts & Organizations

* [Accounts]({{< relref "/docs/intro/console/accounts" >}})
* [Organizations]({{< relref "/docs/intro/console/organizations" >}})
* [SAML Integrations]({{< relref "/docs/guides/saml" >}})

## Collaboration

Collaborate with other developers and coordinate on updates. Provide fine-grained access to stacks and use RBAC (Role-based Access Control) for your organization.

* [Organization Roles]({{< relref "/docs/intro/console/organizations#organization-roles" >}})
* [Teams]({{< relref "/docs/intro/console/teams" >}})
* [Stack Permissions]({{< relref "/docs/intro/console/projects-and-stacks#stack-permissions" >}})
* [Project and Stack Management]({{< relref "/docs/intro/console/projects-and-stacks" >}})
* [Audit Logs]({{< relref "/docs/intro/console/audit-logs" >}})

## Integrations and Extensions

Integrate Pulumi with your current continuous delivery pipeline. Build your own extensions, and create reusable templates.

* [CI/CD Integration Assistant]({{< relref "/docs/intro/console/ci-cd-integration-assistant" >}})
* [Continuous Delivery]({{< relref "/docs/guides/continuous-delivery" >}})
* [Pulumi Service REST API]({{< relref "/docs/reference/service-rest-api" >}})
* [Webhooks]({{< relref "/docs/intro/console/webhooks" >}})
* ["Deploy with Pulumi" Button]({{< relref "/docs/intro/console/pulumi-button" >}})
