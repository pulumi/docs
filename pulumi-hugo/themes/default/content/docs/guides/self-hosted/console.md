---
title: Pulumi Console
menu:
    userguides:
        parent: self_hosted
        identifier: self_hosted_console_service
        weight: 2
meta_desc: Pulumi Console is one of the components required for self-hosting Pulumi. Self-hosting is available as part of the Enterprise Edition.
---

{{% notes type="info" %}}
Self-hosting is only available with **Pulumi Enterprise**. [Contact us]({{< relref "/contact.md" >}}) if you would like to evaluate Self-Hosted Pulumi Enterprise.

To manage your state with a self-managed backend, such as a cloud storage bucket, see [State and Backends]({{< relref "/docs/intro/concepts/state" >}}).
{{% /notes %}}

The Pulumi Console allows users to view the stacks they have created, see any past activities recorded for those stacks. It also allows you to manage RBAC for your users.

In order for the CLI to persist the state of a particular stack, a user must login to the CLI. In order to login to the CLI, you should have created an account using the Console first.

## Dependencies

The Console service depends on the API service. It relies on the API service for authentication callbacks. Depending on the type of authentication mechanism you choose for your users, the services in the Console container may need to communicate with the API container.

## Prerequisites

* Provide a server or virtual machine to install and run the Pulumi components (see Minimum System Requirements below).

You can run this container on the same host that your API container is running or on a different host. If you are running this container on a separate host than the API, be sure to set the appropriate environment variables (more on that below) in order for the Console to be able to reach the API service.

## Minimum System Requirements

| Type | Properties | Notes |
| ---- | ---------- | ----- |
| Compute | 1 CPU core w/ 1 GB memory | |

## What's In The Container?

{{% notes type="info" %}}
The container image repository is private. [Contact us]({{< relref "/contact.md" >}}) if you would like to evaluate the Self-Hosted Enterprise Edition.
{{% /notes %}}

The Console container runs a web server using a Node 10-based image.

### Server

The container runs a single web server which handles delivering UI static assets to your web browser, as well as handling authentication callbacks. The console will be served using port `3000` over HTTP by default. If [TLS](#tls-environment-variables) is configured the console will instead be served using port `3443` over HTTPS.

## Primary Environment Variables

The following are the core environment variables that are required at a minimum.

> **Tip**: The quickstart solutions set reasonable default values for these variables, so you can get started without worrying about configuration.

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_API | The endpoint URL where the service APIs can be reached. This should match the value of PULUMI_API_DOMAIN. Default is `http://localhost:8080`. |
| PULUMI_API_INTERNAL_ENDPOINT | The endpoint URL local to the container using which the Console app can reach the API container using a container-to-container network. |
| CONSOLE_DOMAIN | `CONSOLE_DOMAIN` is used to redirect the user after they have **signed-in** using a social identity or SAML SSO. |
| HOMEPAGE_DOMAIN | `HOMEPAGE_DOMAIN` is used to redirect the user after they have **signed-out**. |

### Environment Variables For Identities

| Variable Name | Description |
| ------------- | ----------- |
| RECAPTCHA_SITE_KEY | Used for password reset requests by users. [Create a new reCaptcha v2](https://www.google.com/recaptcha/admin). |
| SAML_SSO_ENABLED | Default is `false`. Set to `true` to enable the SAML SSO signin/signup option. Before enabling, make sure you have completed the steps in the [Enabling SAML SSO]({{< relref "saml-sso" >}}) guide. |

### GitHub OAuth

| Variable Name | Description |
| ------------- | ----------- |
| GITHUB_OAUTH_ID | GitHub OAuth app client ID. Used for GitHub OAuth signins. [Create a new GitHub OAuth app](https://github.com/settings/applications/new). |
| GITHUB_OAUTH_SECRET | GitHub OAuth app client secret. See above. |
| GITHUB_OAUTH_ENDPOINT | |

### GitLab OAuth

| Variable Name | Description |
| ------------- | ----------- |
| GITLAB_OAUTH_ID | GitLab OAuth app client ID. Used for GitLab OAuth signins. [Create a new GitLab OAuth app](https://gitlab.com/profile/applications). |
| GITLAB_OAUTH_SECRET | GitLab OAuth app client secret. See above. |
| GITLAB_OAUTH_ENDPOINT | |

### Bitbucket OAuth

| Variable Name | Description |
| ------------- | ----------- |
| BITBUCKET_OAUTH_ID| Atlassian Bitbucket OAuth consumer client ID. Used for Bitbucket OAuth signins. |
| BITBUCKET_OAUTH_SECRET | |

### Email and password {#email-identity}

| Variable Name | Description |
| ------------- | ----------- |
| PULUMI_HIDE_EMAIL_LOGIN | When `true`, hides the email identity as a login option but does not disable the API handler. To disable the API handler for email logins set the API container environment variable `PULUMI_DISABLE_EMAIL_LOGIN`. Refer to the API container [environment variables]({{< relref "/docs/guides/self-hosted/api#other-env-vars" >}}) for more information. |
| PULUMI_HIDE_EMAIL_SIGNUP | When `true` hides the email identity as a signup option but does not disable the API handler. To disable the API handler for email signups set the API container environment variable `PULUMI_DISABLE_EMAIL_SIGNUP`. Refer to the API container [environment variables]({{< relref "/docs/guides/self-hosted/api#other-env-vars" >}}) for more information. |

### TLS Environment Variables

The following environment variables must be configured to enable TLS. The values of the environment variables may either be a filepath or the actual value of the entity. If these variables are set, the console will be served over HTTPS (i.e. using TLS) using port `3443`. If the following variables are not set the console will default to serving over HTTP using port `3000`.

| Variable Name       | Description                                                                                                       |
|---------------------|-------------------------------------------------------------------------------------------------------------------|
| CONSOLE_TLS_CERTIFICATE | The TLS certificate. The certificate must be supplied in X.509 format and must be PEM encoded.                |
| CONSOLE_TLS_PRIVATE_KEY | The private key associated with the TLS certificate. The private key must be PEM encoded.                     |
| CONSOLE_MIN_TLS_VERSION | The minimum version of TLS to allow (must be in \<major>.\<minor> format, e.g. `1.2`). This variable is optional, if not set a minimum version will not be enforced.|
| ALLOW_INVALID_CERTS | This optional value can be set to allow connections originating from the Console container to the Service container to connect without TLS verification. This can be helpful in scenarios like testing or when using self-signed certs for internal traffic. |

> Note: Self-signed certificates may be used to configure TLS in the event the need for a trusted entity is not necessary. A self-signed cert and private key may be generated using OpenSSL. The following command uses OpenSSL to generate a self-signed certificate. This example will output two files, the certificate (cert.pem) and the private key (key.pem) used to sign it.

>
```
openssl \
  req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem \
  -days { days_until_expiration } -nodes -subj "/CN={ common_name }"
```
