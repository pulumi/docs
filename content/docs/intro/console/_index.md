---
title: Pulumi Console
menu:
  intro:
    identifier: console
    weight: 1
no_on_this_page: true
aliases: [/docs/reference/service]
---

The [Pulumi Console](https://app.pulumi.com) web application automatically manages deployment state and enables collaboration between developers and operators. The Pulumi CLI automatically uses it unless you [explicitly opt out](https://www.pulumi.com/docs/intro/concepts/state/). The Pulumi Console provides the following features and benefits:

* Project and stack management
* Collaboration with teams across different organizations
* Safe storage of resource state and protection against concurrent updates
* Detailed resource view and update history
* Integrations with your CI/CD system
* Extensions via webhooks and reusable project templates

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><i class="fas fa-angle-right pr-2"></i> Getting Started</h3>
        <p>
            In your browser, navigate to <a href="https://app.pulumi.com" target="_blank">app.pulumi.com</a> and sign up. The <a href="{{< relref "editions#community-edition" >}}">Pulumi Community Edition</a> is free forever
            for unlimited individual use.
        </p>
            <a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">SIGN UP</a>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><i class="fas fa-user-circle pr-2"></i> Account Management</h3>
        <p>Learn about the Pulumi product editions. Link your account with a third party identity provider, including one that is compatible with SAML 2.0. Next, you can learn how to create an organization.
        <ul class="p2">
            <li><a href="{{< relref "editions" >}}">Plans and Editions</a></li>
            <li><a href="{{< relref "accounts" >}}">Accounts</a></li>
            <li><a href="{{< relref "/docs/guides/saml" >}}">SAML Integrations</a></li>
            <li><a href="{{< relref "organizations" >}}">Organizations</a></li>
        </ul>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><i class="fas fa-users pr-2"></i> Collaboration</h3>
        <p>
            Collaborate with other developers and coordinate on updates. Provide fine-grained access to stacks and use RBAC (Role-based Access Control) for your organization.
        </p>
        <ul class="p2">
            <li><a href="{{< relref "stack-permissions" >}}">Stack Permissions</a></li>
            <li><a href="{{< relref "project-and-stack-management" >}}">Stack Management</a></li>
            <li><a href="{{< relref "organization-roles" >}}">Organization Roles</a></li>
            <li><a href="{{< relref "teams" >}}">Teams</a></li>
        </ul>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><i class="fab fa-connectdevelop pr-2"></i> Integrations and Extensions</h3>
        <p>Integrate Pulumi with your current continuous delivery pipeline. Build your own extensions, and create reusable templates.
        <ul class="p2">
            <li><a href="{{< relref "/docs/guides/continuous-delivery" >}}">Continuous Delivery</a></li>
            <li><a href="{{< relref "webhooks" >}}">Webhooks</a></li>
            <li><a href="{{< relref "pulumi-button" >}}">"Deploy with Pulumi" Button</a></li>
        </ul>
    </div>
</div>
