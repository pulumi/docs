---
title_tag: gh-login Pulumi ESC Provider
meta_desc: The gh-login Pulumi ESC Provider enables you to log in to GitHub using app credentials.
title: gh-login
h1: gh-login
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    identifier: gh-login
    parent: esc-dynamic-login-credentials
    weight: 4
aliases:
    - /docs/pulumi-cloud/esc/providers/gh-login/
    - /docs/esc/providers/gh-login/
---

The gh-login provider enables you to log in to GitHub using app credentials. The provider will return an
installation access token that can be used to access the GitHub API and repositories.

The provider works as a GitHub App to produce an installation access token for the specified GitHub account, as described
in "[Authenticating as a GitHub App installation](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/authenticating-as-a-github-app-installation)".
Use the token with the [Pulumi ESC GitHub Action](/docs/esc/integrations/dev-tools/github/),
the [GitHub CLI](https://cli.github.com/), etc. The token will expire after 1 hour.

## App Registration

To use the provider, you must register a new GitHub App into your personal GitHub account or an organization account.
Other GitHub accounts then install the application into their account to grant you access with the permissions
defined by your GitHub App.

{{% notes type="info" %}}
This is different from installing the Pulumi GitHub App for Deployments and CI/CD integration, which should be installed according to the instructions in the [GitHub App documentation](/docs/iac/using-pulumi/continuous-delivery/github-app/#installation-and-configuration).
{{% /notes %}}

- To register an app on a personal account, visit: [https://github.com/settings/apps/new](https://github.com/settings/apps/new?contents=read&metadata=read&webhook_active=false&description=Enables%20access%20for%20a%20Pulumi%20ESC%20environment.&url=https://www.pulumi.com/product/esc/).

- To register an app on an organization account, visit: [https://github.com/organizations/ORGANIZATION/settings/apps/new](https://github.com/organizations/ORGANIZATION/settings/apps/new?contents=read&metadata=read&webhook_active=false&description=Enables%20access%20for%20a%20Pulumi%20ESC%20environment.&url=https://www.pulumi.com/product/esc/).
Replace ORGANIZATION with the name of the organization where you'd like to register the app.

It is fine to deploy a separate GitHub app for each Pulumi environment, or to reuse an app across environments.
It is recommended that you store the app’s credentials in a reusable environment that you can import as needed.

## Provider Configuration

Configure the provider with the app ID and private key for the GitHub App that you registered.
See "[Generating Private Keys](https://docs.github.com/en/apps/creating-github-apps/authenticating-with-a-github-app/managing-private-keys-for-github-apps#generating-private-keys)"
for instructions on how to generate a private key (in PEM format) and download to your computer.

Private keys do not expire and need to be manually revoked. You must keep private keys for GitHub Apps secure.
Store the private key as a secret by using the `fn::secret` function.
See "[Pulumi ESC: Store and Retrieve Secrets](/docs/esc/get-started/store-and-retrieve-secrets/#store-environment-values)".

```yaml
appId: 123456
privateKey:
  fn::secret: |
    -----BEGIN RSA PRIVATE KEY-----
    ...
    -----END RSA PRIVATE KEY-----
```

### Owner

An installation access token is always scoped to a particular Github account, set by the environment as `owner`.
The `owner` property may refer to a personal account or an organization account. The owner or app manager of the account must first install
the GitHub App that was registered earlier. For more information, see "[Installing your own GitHub App](https://docs.github.com/en/apps/using-github-apps/installing-your-own-github-app)"
and "[Sharing your GitHub App](https://docs.github.com/en/apps/sharing-github-apps/sharing-your-github-app)".

```yaml
owner: octocat
```

Use multiple instances of the gh-login provider to create installation access tokens for multiple accounts.

### Repository Access

By default, an installation access token has access to all repositories that the installation was granted access to.
Use the `repositories` property to further restrict the allowed repositories.
The token cannot be granted access to repositories that the installation was not granted access to. You can list up to 500 repositories.

```yaml
repositories:
  - "Spoon-Knife"
  - "Hello-World"
```

### Token Permissions

Optionally, use the `permissions` property to specify the permissions that the installation access token should have.
By default, the installation access token will have all of the permissions that were granted to the app.
The installation access token cannot be granted permissions that the app was not granted.

See "[Create an installation access token for an app](https://docs.github.com/en/rest/apps/apps?apiVersion=2022-11-28#create-an-installation-access-token-for-an-app)"
for a list of permissions and associated permission levels.

```yaml
permissions:
  contents: read
  pull_requests: write
```

### GitHub Enterprise Server

To access a GitHub Enterprise Server, configure the `ghe.host` property to your server address.

```yaml
ghe:
  host: ghe.example.com
```

## Example

```yaml
values:
  gh:
    fn::open::gh-login:
      # configure the app credentials
      appId: 123456
      privateKey:
        fn::secret: |
          -----BEGIN RSA PRIVATE KEY-----
          ...
          -----END RSA PRIVATE KEY-----
      # configure the target GH account for the installation access token
      owner: octocat
      # optionally restrict access to specific repos
      repositories:
        - "Spoon-Knife"
      # optionally restrict the token permissions
      permissions:
        contents: read
        pull_requests: write
  environmentVariables:
    # export the GH_TOKEN environment variable
    GH_TOKEN: ${gh.accessToken}
  pulumiConfig:
    # configure the GitHub IaC provider
    github:token: ${gh.accessToken}
```

## Inputs

| Property       | Type                      | Description                                                                 |
|----------------|---------------------------|-----------------------------------------------------------------------------|
| `appId`        | number                    | The ID of the GitHub App providing access tokens for the environment.       |
| `privateKey`   | string                    | The private key of the GitHub App (in PEM format).                          |
| `owner`        | string                    | The GitHub account for which to get an installation access token.           |
| `repositories` | string[]                  | [Optional] List of repositories to allow access to.                         |
| `permissions`  | object                    | [Optional] A map of the permissions that the token should have.             |
| `ghe`          | [GHLoginGHE](#ghloginghe) | [Optional] Options for connecting to a GitHub Enterprise installation.      |

### GHLoginGHE

| Property         | Type   | Description                                                                                  |
|------------------|--------|----------------------------------------------------------------------------------------------|
| `host`           | string | The hostname of your GitHub Enterprise server.                                               |

## Outputs

| Property         | Type   | Description                                                                      |
|------------------|--------|----------------------------------------------------------------------------------|
| `appId`          | number | The ID of the GitHub App providing access tokens for the environment.            |
| `appSlug`        | string | The GitHub App's slug.                                                           |
| `installationId` | number | The ID of the GitHub App installation.                                           |
| `accessToken`    | string | The access token used to authenticate with the GitHub API.                       |
| `expiry`         | string | [Optional] The access token's expiry time (RFC3339).                             |
| `type`           | string | The access token's type.                                                         |
