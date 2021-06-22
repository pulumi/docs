---
title: "Credijusto Manages Authentication with Auth0 and Pulumi"
date: 2020-09-22
draft: false
meta_desc: " Simplifying authentication to APIs with the Pulumi Auth0 provider"
meta_image: credijusto.png
authors:
    - fernando-carletti
tags:
    - guest-post
    - auth0
---

*Guest author Lead Devops Engineer Fernando Carletti, writes about using the Pulumi Auth0 provider to manage resources at Credijusto.*

Auth0 allows you to simplify your authentication process. The [Auth0 Provider]({{< relref "/docs/reference/pkg/auth0" >}}) allows you to manage the Auth0 resources, managing Applications, Databases, Social Connections, APIs, and other resources. Here at [Credijusto](https://credijusto.com) we use it manage authentication from the front-end through all the APIs that serve that request, leveraging the complexity of the authentication to Auth0.

For this article, we will start a new Pulumi project in a fresh Auth0 account and fully configure it for a backend and a single page application and set up a connection to Github which allows you apps to authenticate with it using OAuth.

<!--more-->

## Setup the project

Create a new Pulumi program:

```bash
$ pulumi new typescript
```

Install the Auth0 provider SDK:

```bash
$ npm add @pulumi/auth0
```

Create the Auth0 resources in `index.ts` you created as shown in the example below.

## Configure the credentials

Here we will use the credentials of the default application created by Auth0. For production use, you may want to create a new one or rename the `Test Application` to ensure Pulumi uses its own set of credentials.

Note: please use your domain, clientId, and clientSecret. You can find the `Test Application` credentials in Auth0's Applications page.

```bash
pulumi config set auth0:domain my-account.auth0.com
pulumi config set auth0:clientId foo
pulumi config set auth0:clientSecret --secret bar
pulumi config set githubClientId github-foo
pulumi config set githubClientSecret --secret github-bar
```

Tip: You can create your Github OAuth Application [here](https://github.com/settings/applications/new).

## Configure the Tenant

Auth0 creates an initial tenant when a new account is created. Any tenant resource you create will end up configuring the tenant of which the `Test Application` is part of, even while Pulumi is saying a new resource is created, it will only set the properties on its existing tenant.

Let's set a friendly name for our tenant:

```typescript
new auth0.Tenant('default', {
  friendlyName: 'Hello Pulumi!'
});
```

By accessing your settings page you should be to see the `Friendly Name` field configured.

## Create the applications

Now we need to create our applications. Since the Auth0 provider uses the same naming as the [Management API](https://auth0.com/docs/api/management/v2), the Application is called Client.

Let's create both the frontend and backend applications:

```typescript
const backend = new auth0.Client('backend', {
  appType: 'non_interactive'
});

const frontend = new auth0.Client('frontend', {
  appType: 'spa'
});
```

Note that the `backend` is set as the `non_interactive` type, this is referred to as `Machine to machine` in the Auth0 console.

## Create the Github connection

With the applications set, we need to create a social connection using Github and allow those applications to use it:

```typescript
const config = new pulumi.Config();

new auth0.Connection('github', {
  strategy: 'github',
  enabledClients: [backend.id, frontend.id],
  options: {
    clientId: config.require('githubClientId'),
    clientSecret: config.requireSecret('githubClientSecret'),
  }
});
```

Pulumi allows you to manage your Auth0 resources allowing you to easily replicate your configuration across multiple environments. Read more about the [Auth0 Provider]({{< relref "/docs/reference/pkg/auth0" >}}).
