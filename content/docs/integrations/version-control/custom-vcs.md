---
title_tag: "Custom VCS Integration | Version Control"
meta_desc: Connect any Git or Mercurial version control system to Pulumi Cloud for webhook-driven deployments using Custom VCS integrations.
title: "Custom VCS"
h1: "Custom VCS"
menu:
    integrations:
        name: Custom VCS
        parent: integrations-version-control
        weight: 5
aliases:
- /docs/version-control/custom-vcs/
---

Custom VCS integrations let you connect any Git or Mercurial version control system to [Pulumi Deployments](/docs/deployments/concepts/), including self-hosted and third-party servers. You configure webhooks on your VCS server to notify Pulumi Cloud when commits are pushed, and Pulumi automatically triggers deployments for matching stacks.

Unlike the first-party [GitHub](/docs/integrations/version-control/github-app/), [GitLab](/docs/integrations/version-control/gitlab/), [Azure DevOps](/docs/integrations/version-control/azure-devops-integration/), and [Bitbucket](/docs/integrations/version-control/bitbucket/) integrations, Custom VCS uses [ESC environments](/docs/esc/) for credential management and requires manual webhook configuration. It supports push-to-deploy but does not support pull request comments, commit status checks, or review stacks.

[Neo](/docs/ai/), Pulumi's AI assistant, can clone and push to Git and Mercurial repositories registered with a Custom VCS integration using the credentials from the integration's ESC environment. Neo cannot open pull requests or create new repositories on Custom VCS servers at this time. Those operations require VCS-specific APIs only available through native integrations.

## Prerequisites

- A [Pulumi Cloud](https://app.pulumi.com) organization
- A Git or Mercurial VCS server accessible from Pulumi Cloud (for cloning)
- Org admin access in Pulumi Cloud
- An [ESC environment](/docs/esc/) containing your VCS credentials (see [Configure credentials in ESC](#configure-credentials-in-esc))

## Configure the integration

{{% notes type="info" %}}
To set up a Custom VCS integration, you must be an org admin in Pulumi Cloud.
{{% /notes %}}

1. [Sign in to your Pulumi account.](https://app.pulumi.com/signin)
1. Navigate to **Management** > **Version control**.
1. Select **Add integration** and choose **Custom VCS**.
1. Enter a **Name** for the integration (e.g., "My Git Server"). Names must be unique within your organization.
1. Enter a **Base URL** — the URL prefix for your repositories (e.g., `https://git.example.com/myorg`). Repository names are appended to this URL to form clone URLs.
1. Select the **ESC environment** containing your VCS credentials, in `project/envName` format (e.g., `vcs-creds/git-prod`).
1. Select **Save**.

By default, Custom VCS integrations are created with a VCS type of `git`. To configure a Mercurial integration, create the integration via the [Pulumi Cloud REST API](/docs/reference/cloud-rest-api/) with `vcsType` set to `hg`.

After saving, Pulumi displays a **webhook URL** and **webhook secret**.

{{% notes type="warning" %}}
Copy the webhook secret immediately. It is only displayed once. If you lose it, you can regenerate it from the integration detail page, but you will need to update your VCS server's webhook configuration with the new secret.
{{% /notes %}}

### Configure credentials in ESC

Custom VCS integrations use an [ESC environment](/docs/esc/) to store VCS credentials. The same credential structure works for both Git and Mercurial integrations. Create an environment with one of the following authentication methods:

#### Personal access token

```yaml
values:
  personalAccessToken:
    fn::secret: "your-token-here"
```

#### SSH key

```yaml
values:
  sshPrivateKey:
    fn::secret: |
      -----BEGIN OPENSSH PRIVATE KEY-----
      ...
      -----END OPENSSH PRIVATE KEY-----
  sshPassword:
    fn::secret: "optional-passphrase"
```

#### Basic auth

```yaml
values:
  username: "deploy-bot"
  password:
    fn::secret: "your-password"
```

Credentials are resolved at deployment time using the access permissions of the user who configured the integration. If that user loses access to the ESC environment, deployments will fail with an authentication error.

## Add repositories

Custom VCS integrations do not auto-discover repositories from your VCS server. You must add each repository manually.

1. Navigate to **Management** > **Version control** and select your Custom VCS integration.
1. Select **Add repository**.
1. Enter the repository **name** or path (e.g., `infra-prod` or `team/infra-prod`).
1. Optionally enter a **display name** for the repository.

The repository name is joined with the integration's base URL to form the clone URL. For example, a base URL of `https://git.example.com/myorg` and a repository name of `infra-prod` produces the clone URL `https://git.example.com/myorg/infra-prod`.

To remove a repository, select the repository from the integration detail page and choose **Remove**.

## Configure webhooks

After creating the integration and adding repositories, configure your VCS server to send webhook notifications to Pulumi Cloud.

### Webhook URL

Configure your VCS server to send POST requests to:

```text
https://api.pulumi.com/workflow/generic-vcs
```

### Required headers

Your webhook requests must include the following headers:

| Header | Description | Example |
|---|---|---|
| `X-Generic-VCS-Integration-ID` | Your integration UUID (shown on the integration detail page) | `a1b2c3d4-e5f6-7890-abcd-ef1234567890` |
| `X-Generic-VCS-Signature` | HMAC-SHA256 signature of the request body | `v1=abc123def456...` |
| `Content-Type` | Must be `application/json` | `application/json` |

### Payload format

The request body must be a JSON object with the following fields:

```json
{
  "event": "push",
  "commit": "abc123def456789...",
  "branch": "main",
  "repoUrl": "https://git.example.com/myorg/infra-prod",
  "sender": "deploy-bot",
  "changedFiles": ["infra/main.go", "Pulumi.yaml"]
}
```

| Field | Type | Required | Description |
|---|---|---|---|
| `event` | string | Yes | Event type. Use `push` for a branch push or `tag_push` for a tag push. Other values are ignored. |
| `commit` | string | Yes | Full commit SHA (Git) or changeset ID (Mercurial) |
| `branch` | string | For `push` | Branch name that was pushed to. Required for `push` events. |
| `tag` | string | For `tag_push` | Tag name that was pushed (e.g., `v1.2.0`). Required for `tag_push` events. Enables [tag filtering](#deployment-settings). |
| `repoUrl` | string | Yes | Full repository URL (must match a configured repository) |
| `sender` | string | No | Identifier for the user who pushed |
| `changedFiles` | string[] | No | File paths changed in this push. Enables [path filtering](#deployment-settings). If omitted, path filters are skipped and all pushes trigger deployments. Applies to `push` events only. |

To trigger a deployment on a tag push, send `event: "tag_push"` with the `tag` field set instead of `branch`:

```json
{
  "event": "tag_push",
  "commit": "abc123def456789...",
  "tag": "v1.2.0",
  "repoUrl": "https://git.example.com/myorg/infra-prod",
  "sender": "deploy-bot"
}
```

### HMAC signing

Pulumi verifies webhook authenticity using HMAC-SHA256 signatures. To sign a request:

1. Compute `HMAC-SHA256(webhook_secret, raw_request_body)` using the webhook secret provided during integration setup.
1. Hex-encode the result.
1. Set the header: `X-Generic-VCS-Signature: v1=<hex-encoded-hmac>`.

The `v1` prefix identifies the signing algorithm version.

{{% notes type="info" %}}
Most VCS systems use their own native webhook payload format. You may need a lightweight transformer — such as a serverless function or CI pipeline step — to convert your VCS server's push events into the payload format above.
{{% /notes %}}

## Deployment settings

Configure deployment behavior for Custom VCS-backed stacks under **Stack** > **Settings** > **Deploy**.

| Setting | Description |
|---|---|
| Push to deploy | Automatically deploy when commits are pushed to the configured branch |
| Path filters | Only trigger deployments when changed files match specified glob patterns (e.g., `infrastructure/**`). Requires the webhook payload to include the `changedFiles` field. |
| Tag triggers | Deploy when a tag matching the configured [tag filters](/docs/deployments/concepts/settings/#tag-filtering) is pushed (e.g., `v*`). Requires the webhook to send a `tag_push` event with the `tag` field. |

### Selecting a repository and branch

1. Choose the Custom VCS integration (if multiple are configured).
1. Select a repository from the dropdown. This list shows the repositories you have [manually configured](#add-repositories) on the integration.
1. Enter the target branch name.

{{% notes type="info" %}}
Unlike native integrations, Custom VCS does not auto-discover branches. You must type the branch name manually.
{{% /notes %}}

## Comparison with native integrations

Custom VCS provides webhook-driven push-to-deploy but does not include the deeper VCS platform features available with native integrations.

| Capability | Native integrations | Custom VCS |
|---|---|---|
| Push-to-deploy | Yes | Yes (via webhook) |
| PR/MR previews | Yes | No |
| Commit status checks | Yes | No |
| PR comments | Yes | No |
| Review stacks | Yes | No |
| Auto-discover repos | Yes | No (manual) |
| Branch listing | Yes | No (manual entry) |
| Path filtering | Yes | Yes (requires `changedFiles` in webhook) |
| Tag triggers | Yes | Yes (requires `tag_push` event in webhook) |
| Credential management | OAuth/app tokens | ESC environment |
| Mercurial support | No | Yes |
| Neo clone/push to repos | Yes | Yes (Git and Mercurial) |
| Neo pull request creation | Yes | No |
| Neo repository creation | Yes | No |

## Troubleshooting

| Issue | Resolution |
|---|---|
| Webhook returns 401 Unauthorized | Verify your HMAC signature computation. Ensure you are signing the raw request body with the correct webhook secret and using HMAC-SHA256. Check that the `v1=` prefix is included. |
| Deployments not triggering | Check that `repoUrl` in your webhook payload matches a configured repository URL. Verify the branch matches your deployment settings. Confirm `event` is set to `push` and `deploy on push` is enabled for the stack. |
| Clone fails with authentication error | Verify credentials in your ESC environment. Check that the configuring user still has access to the ESC environment. |
| Integration shows broken credentials | The ESC environment may have been deleted or the configuring user may have lost access. Update the ESC environment reference or have an admin reconfigure the integration. |
| Path filters not working | Path filtering requires the `changedFiles` field in your webhook payload. If omitted, all pushes trigger deployments regardless of path filter settings. |
| Tag pushes not triggering | Confirm the webhook sends `event` set to `tag_push` with the `tag` field populated, that tag triggers are enabled for the stack, and that the tag matches your configured tag filters. |
