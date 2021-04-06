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

The [Pulumi Console](https://app.pulumi.com) web application automatically manages deployment state and enables collaboration between developers and operators. The Pulumi CLI automatically uses it unless you [explicitly opt out]({{< relref "/docs/intro/concepts/state" >}}). Explore the different sections to learn more about the features and benefits of using the Pulumi Console.

## Getting Started

In your browser, navigate to <a href="https://app.pulumi.com" target="_blank">app.pulumi.com</a> and sign up.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Sign up</a>

### Pulumi Plans

#### Community

When you sign into the Pulumi Console, an personal account is automatically
created on the Community plan. The Pulumi Community Plan is free forever for unlimited individual use.

You can create an unlimited number of stacks, encrypt configuration and resource secrets, and browse stack history. To collaborate with other developers or use advanced features like [SAML SSO]({{< relref "/docs/guides/saml" >}}), you'll need to create a Pulumi [organization]({{< relref "organizations" >}}).

#### Other Plans

**Pulumi Team Starter** is ideal for teams just getting started deploying cloud
applications and infrastructure.

**Pulumi Team Pro** is ideal for medium to large teams using Pulumi for multiple projects
or clouds.

**Pulumi Enterprise** is ideal for large organizations running cloud software at
scale, with advanced or custom needs.

For more information about the specific differences and capabilities offered for the
Pulumi Team and Enterprise plans, refer to the [pricing page]({{< relref "/pricing" >}}).

## Accounts & Organizations

* [Accounts]({{< relref "/docs/intro/console/accounts" >}})
* [Organizations]({{< relref "/docs/intro/console/organizations" >}})
* [SAML Integrations]({{< relref "/docs/guides/saml" >}})

## Collaboration

Collaborate with other developers and coordinate on updates. Provide fine-grained access to stacks and use RBAC (Role-based Access Control) for your organization.

* [Organization Roles]({{< relref "/docs/intro/console/organization-roles" >}})
* [Teams]({{< relref "/docs/intro/console/teams" >}})
* [Stack Permissions]({{< relref "/docs/intro/console/stack-permissions" >}})
* [Project and Stack Management]({{< relref "/docs/intro/console/project-and-stack-management" >}})
* [Audit Logs]({{< relref "/docs/intro/console/auditing" >}})

## Integrations and Extensions

Integrate Pulumi with your current continuous delivery pipeline. Build your own extensions, and create reusable templates.

* [CI/CD Integration Assistant]({{< relref "/docs/intro/console/ci-cd-integration-assistant" >}})
* [Continuous Delivery]({{< relref "/docs/guides/continuous-delivery" >}})
* [Webhooks]({{< relref "/docs/intro/console/webhooks" >}})
* ["Deploy with Pulumi" Button]({{< relref "/docs/intro/console/pulumi-button" >}})
