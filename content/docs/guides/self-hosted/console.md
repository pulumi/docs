---
title: Pulumi Console
menu:
    userguides:
        parent: self_hosted
        identifier: self_hosted_console_service
        weight: 2
meta_desc: Pulumi Console is one of the components required for self-hosting Pulumi. Self-hosting is available as part of the Enterprise Edition.
---

<div class="note note-info" role="alert">
    <p>
        Self-hosting is only available with the <strong>Pulumi Enterprise Edition</strong>.
    </p>
</div>

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

The Console container is a Node 10-based image. A single web server handles delivering UI static assets to your web browser, as well as handling authentication callbacks.

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
| RECAPTCHA_SITE_KEY | Use for password reset requests by users. Create a new reCaptcha v2 [here](https://www.google.com/recaptcha/admin). |

### GitHub OAuth

| Variable Name | Description |
| ------------- | ----------- |
| GITHUB_OAUTH_ID | GitHub OAuth app client ID. Used for GitHub OAuth signins. Create a new GitHub OAuth app [here](https://github.com/settings/applications/new). |
| GITHUB_OAUTH_SECRET | GitHub OAuth app client secret. See above. |
| GITHUB_OAUTH_ENDPOINT | |

### GitLab OAuth

| Variable Name | Description |
| ------------- | ----------- |
| GITLAB_OAUTH_ID | GitLab OAuth app client ID. Used for GitLab OAuth signins. Create a new GitLab OAuth app [here](https://gitlab.com/profile/applications). |
| GITLAB_OAUTH_SECRET | GitLab OAuth app client secret. See above. |
| GITLAB_OAUTH_ENDPOINT | |

### Bitbucket OAuth

| Variable Name | Description |
| ------------- | ----------- |
| BITBUCKET_OAUTH_ID| Atlassian Bitbucket OAuth consumer client ID. Used for Bitbucket OAuth signins. |
| BITBUCKET_OAUTH_SECRET | |
