---
title: Pulumi Console
meta_desc: An overview of the Pulumi Console web application.
menu:
  intro:
    identifier: console
    weight: 3
no_on_this_page: true
aliases: [/docs/reference/service]
---

The [Pulumi Console](https://app.pulumi.com) web application automatically manages deployment state and enables collaboration between developers and operators. The Pulumi CLI automatically uses it unless you [explicitly opt out](https://www.pulumi.com/docs/intro/concepts/state/). Explore the different sections to learn more about the features and benefits of using the Pulumi Console.

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="https://app.pulumi.com" target="_blank"><i class="fas fa-angle-right pr-2"></i> Getting Started</a></h3>
        <p>
            In your browser, navigate to <a href="https://app.pulumi.com" target="_blank">app.pulumi.com</a> and sign up. The <a href="{{< relref "editions#community-edition" >}}">Pulumi Community Edition</a> is free forever
            for unlimited individual use.
        </p>
            <a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">SIGN UP</a>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "accounts-and-organizations" >}}"><i class="fas fa-user-circle pr-2"></i> Accounts & Organizations</a></h3>
        <p>Learn about the Pulumi product editions. Link your account with a third party identity provider, including one that is compatible with SAML 2.0. Next, you can learn how to create an organization.
        <ul class="p2">
            <li><a href="{{< relref "editions" >}}">Plans and Editions</a></li>
            <li><a href="{{< relref "accounts" >}}">Accounts</a></li>
            <li><a href="{{< relref "organizations" >}}">Organizations</a></li>
            <li><a href="{{< relref "/docs/guides/saml" >}}">SAML Integrations</a></li>
        </ul>
    </div>
</div>

<div class="md:flex flex-row mt-6 mb-6">
    <div class="w-1/2 border-solid border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><i class="fas fa-users pr-2"><a href="{{< relref "collaboration" >}}"></i> Collaboration</a></h3>
        <p>
            Collaborate with other developers and coordinate on updates. Provide fine-grained access to stacks and use RBAC (Role-based Access Control) for your organization.
        </p>
        <ul class="p2">
            <li><a href="{{< relref "organization-roles" >}}">Organization Roles</a></li>
            <li><a href="{{< relref "teams" >}}">Teams</a></li>
            <li><a href="{{< relref "stack-permissions" >}}">Stack Permissions</a></li>
            <li><a href="{{< relref "project-and-stack-management" >}}">Project and Stack Management</a></li>
        </ul>
    </div>
    <div class="w-1/2 border-solid ml-4 border-t-2 border-gray-200">
        <h3 class="no-anchor pt-4"><a href="{{< relref "extensions" >}}"><i class="fab fa-connectdevelop pr-2"></i> Integrations and Extensions</a></h3>
        <p>Integrate Pulumi with your current continuous delivery pipeline. Build your own extensions, and create reusable templates.
        <ul class="p2">
            <li><a href="{{< relref "/docs/guides/continuous-delivery" >}}">Continuous Delivery</a></li>
            <li><a href="{{< relref "webhooks" >}}">Webhooks</a></li>
            <li><a href="{{< relref "pulumi-button" >}}">"Deploy with Pulumi" Button</a></li>
        </ul>
    </div>
</div>
