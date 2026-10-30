---
title_tag: "Cursor Origin integration | Pulumi Docs"
meta_desc: Connect Cursor Origin repositories to Pulumi Cloud for pull request previews, review stacks, push-to-deploy, checks, and infrastructure change comments.
title: Cursor Origin
h1: Cursor Origin
menu:
    integrations:
        name: Cursor Origin
        identifier: integrations-version-control-cursor-origin
        parent: integrations-version-control
        weight: 10
---

Connect your Cursor Origin repositories to Pulumi Cloud to preview infrastructure changes on pull requests and deploy changes when you push code. The integration posts check results and pull request comments in Origin, with links to the corresponding updates in Pulumi Cloud.

The app connects an Origin namespace to a Pulumi organization. You choose which repositories it can access. [Pulumi Deployments](/docs/deployments/) runs automated previews, updates, and review stacks. You can also report results from Pulumi commands run in your own continuous integration (CI) system or locally.

{{% notes type="info" %}}
The integration requires Pulumi Cloud as your stack's backend. Origin apps support Origin-hosted repositories; repositories mirrored from GitHub keep their integrations on GitHub. Use the [Pulumi GitHub app](/docs/integrations/version-control/github-app/) for those repositories. See [Cursor's Origin apps documentation](https://cursor.com/docs/origin/apps) for repository support details.
{{% /notes %}}

## Prerequisites

Before connecting a repository, you need:

- An Origin namespace containing an Origin-hosted Git repository, and permission to install apps for that namespace.
- A Pulumi account with permission to manage the target organization's integrations. Organization admins have this permission.
- The Origin app configured on your Pulumi Cloud instance. The **Cursor Origin** option appears in the console when the app is configured. For an instance you operate, see [self-hosted configuration](#self-hosted-configuration).

To automate previews and updates, configure [Pulumi Deployments](/docs/deployments/get-started/) for your stack and provide the cloud credentials your program needs.

## Install and link the app

1. Sign in to the [Pulumi Cloud console](https://app.pulumi.com/signin) and select your organization.
1. Navigate to **Settings** > **Version control**.
1. Select **Add account**, then **Cursor Origin**.
1. Select **Install in Cursor Origin**. In Origin, choose the namespace and repositories to connect, then approve the app's requested access.
1. On return to Pulumi Cloud, select the organization and choose **Link installation**.

You can also start from the app's installation page in Origin, including a marketplace listing when available. After authorizing the app, complete the **Link installation** step in Pulumi Cloud.

Each Origin app installation can be linked to one Pulumi organization. An installation started from Pulumi must be completed by the same Pulumi user in the organization that started it. The signed installation receipt expires after five minutes. If sign-in or account creation takes longer, restart the installation.

To connect another Origin namespace to the same Pulumi organization, repeat **Add account** for that namespace.

## Configure deployments

Open your stack in Pulumi Cloud and navigate to **Settings** > **Deploy**. Select the Origin integration, repository, and deployment branch, then save the deployment settings. Pulumi discovers the repositories the app can access and their branches.

Enable the triggers you need:

- **Deploy on push** runs an update when commits are pushed to the configured branch. [Path filters](/docs/deployments/concepts/settings/) limit which file changes trigger a deployment.
- **Preview pull requests** runs previews for pull requests targeting the configured branch and reports the results in Origin.
- **Pull request template** uses the stack as a template for [review stacks](/docs/deployments/concepts/review-stacks/). Pulumi creates an environment for each matching pull request and destroys it when the pull request closes or merges.

You can also configure [tag triggers](/docs/deployments/concepts/settings/tag-filtering/) when they are available for your organization. Path filters include both the original and destination paths of renamed files.

If you configure deployment settings through the API, use `origin` as the VCS provider and identify the repository as `owner/name`:

```json
{
    "vcs": {
        "provider": "origin",
        "installationId": "<pulumi-integration-id>",
        "repository": "acme/infrastructure",
        "deployCommits": true,
        "previewPullRequests": true
    }
}
```

`installationId` is the Pulumi integration identifier, not the Origin installation identifier. Pulumi resolves the repository's clone URL and default branch. See [deployment settings](/docs/deployments/concepts/settings/) for operation options, credentials, and other source settings.

## Policies and production approvals

Origin-triggered deployments use the same stack settings, execution permissions, cloud credentials, and [Pulumi policies](/docs/discovery-governance/concepts/policy-as-code/) as other Pulumi Deployments. Mandatory policy violations block the affected update. Pulumi includes policy violations in Origin check results and pull request comments, including previews with policy violations and no resource changes. Disabling comments leaves the check results available.

Pulumi Deployments has no native deployment approval step that pauses a run for reviewer sign-off. A successful pull request preview does not require someone to approve a later update. Enabling **Deploy on push** authorizes automatic updates on matching branch pushes.

If your production process requires approval, leave **Deploy on push** disabled and have an external workflow trigger the deployment after reviewer sign-off. You can keep **Preview pull requests** enabled to review proposed changes. See [deployment triggers](/docs/deployments/concepts/triggers/) for CLI and API options.

[ESC Open approvals](/docs/deployments/guides/gated-deployments/) provide another control over credential access. They require an approved access grant before a deployment obtains its credentials; a run without a grant fails rather than waiting for approval. Automated Git-triggered runs need additional identity configuration described in that guide.

## Report results from CI or your workstation

Pull request reporting also works when you run `pulumi preview` or `pulumi up` outside Pulumi Deployments. Authenticate the Pulumi CLI to Pulumi Cloud separately from the Origin app, using your normal sign-in or a [Pulumi access token](/docs/administration/concepts/access-tokens/).

Run the command from a checkout whose Git remote identifies the Origin repository. Keep the checkout's `.git` directory available so the CLI can capture the repository and commit metadata. When that metadata matches a commit or pull request seen by the integration, Pulumi posts the corresponding check results and pull request comments.

For example, after authenticating to Pulumi Cloud and configuring your cloud credentials:

```sh
pulumi stack select <organization>/<project>/<stack>
pulumi preview
```

Your CI system needs its own credentials to check out the Origin repository. The app's checkout credentials are used by Pulumi Deployments. For CI metadata and detached checkouts, see [continuous delivery](/docs/iac/operations/continuous-delivery/#adding-support-for-cicd-systems).

## Manage reporting and repository access

Navigate to **Settings** > **Version control** and select the Origin integration to configure its reporting preferences:

| Setting | Default | Behavior |
| --- | --- | --- |
| Pull request comments | Enabled | Post Pulumi update results on matching pull requests. Disabling comments leaves check reporting enabled. |
| Draft pull request comments | Enabled | Comment on draft pull requests. When disabled, comments resume when a pull request is published. |
| Detailed diff for pull request comments | Enabled | Include property-level resource changes in comments. |

Manage the installation's repository selection in [Origin app settings](https://cursor.com/codebase/settings/apps). If you add a repository, refresh Pulumi's repository selector. Removing a repository prevents new app access to it; queued deployments recheck access before obtaining checkout credentials.

Suspending the installation stops deployment triggers and reporting. Reactivating it resumes both.

### Permissions and checkout credentials

The app requests these Origin scopes:

- `repository:contents:read` for repository discovery, checkout, and changed-file information.
- `repository:pull_requests:read` for pull request state and existing comments.
- `repository:pull_requests:write` for Pulumi's pull request comments.
- `repository:checks:write` for check results.

Pulumi Deployments mints a short-lived installation token restricted to the source repository when a queued deployment starts. Origin installation tokens expire within 15 minutes. The integration doesn't inject a `GITHUB_TOKEN`; programs that need additional Git operations later in a deployment must get current Origin credentials separately.

### Remove the integration

Deleting the integration from Pulumi uninstalls the Origin app and removes the deployment settings associated with that integration. Uninstalling the app in Origin also removes the linked integration and its deployment settings. Removing the integration does not run `pulumi destroy`.

## Self-hosted configuration

An administrator of a self-hosted Pulumi Cloud instance must register an [Origin app](https://cursor.com/docs/origin/apps) and configure it before organization members can connect repositories.

1. Create the app in the publisher's Origin namespace and register an Ed25519 public key. Keep its PKCS#8 PEM private key secret.
1. Set the webhook URL to `https://<api-host>/workflow/origin` and the installation redirect URI to `https://<console-host>/origin-app/install`.
1. Configure the [scopes](#permissions-and-checkout-credentials) as the app's default scopes and subscribe to `repository.pushed`, `pull_request.created`, `pull_request.published`, `pull_request.reopened`, `pull_request.head_ref.pushed`, `pull_request.base_ref.updated`, `pull_request.closed`, and `pull_request.merged`. Origin delivers installation lifecycle events automatically.
1. Deploy the service and background workers with Origin support before enabling the app. Then supply `ORIGIN_APP_ID` and the secret `ORIGIN_APP_PRIVATE_KEY` to both the service and its background workers. Both values are required. The private key must be an Ed25519 PKCS#8 PEM key.
1. Install the app and follow [the linking steps](#install-and-link-the-app).

These credentials let your Pulumi Cloud instance act as the Origin app. They are separate from the cloud provider credentials your stacks use.

A private Origin app can be installed only in its own namespace. To allow installation in other namespaces, make the app public. A marketplace listing requires a separate review by Cursor; see [publishing an Origin app](https://cursor.com/docs/origin/apps/publish).

## Supported workflows

The integration connects existing Origin repositories to stack deployment settings and update reporting. It doesn't create Origin repositories or provide organization template sources. Origin repositories aren't supported by Pulumi Neo's repository integration or code reviews.

To use the Cursor coding agent with Pulumi, see [Pulumi Agent Skills](/docs/ai/concepts/agent-skills/) and the [Pulumi MCP server](/docs/ai/guides/set-up-mcp-server/).

## Troubleshooting

### Cursor Origin isn't listed

Your Pulumi Cloud instance has no Origin app configuration. For a self-hosted instance, ask your administrator to check [the app configuration](#self-hosted-configuration). For the hosted service, [contact Pulumi support](/support/).

### The installation link is invalid or expired

Restart installation from **Settings** > **Version control** or Origin app settings, and complete the link within five minutes. If you started in Pulumi, use the same Pulumi account and organization when you return.

### The installation is linked to another organization

An installation can belong to only one Pulumi organization. Ask the administrator of the connected organization to remove it, then reinstall the app and link it to the intended organization. Removing the connection also removes its deployment settings.

### A repository is missing or deployments don't trigger

Check that the repository is Origin-hosted, included in the app's repository selection, and accessible to an active installation. Confirm that the stack's deployment branch and trigger settings match the event. Check path filters and tag filters when configured.

If checkout fails after access changes, verify the repository selection and installation status before retrying the deployment. Pulumi obtains fresh checkout credentials when the deployment starts.

### Pull request comments don't appear

Check that comments are enabled for the integration, including draft comments when the pull request is a draft. For CLI and CI runs, verify that the checkout includes `.git` metadata identifying the Origin repository and the pull request's head commit, and that the stack uses Pulumi Cloud as its backend. Check results remain enabled when comments are disabled.

## Learn more

- [Pulumi Deployments](/docs/deployments/)
- [Deployment triggers](/docs/deployments/concepts/triggers/)
- [Review stacks](/docs/deployments/concepts/review-stacks/)
- [Version control integrations](/docs/integrations/version-control/)
