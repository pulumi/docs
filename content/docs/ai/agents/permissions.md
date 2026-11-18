---
title: Permissions and approvals
title_tag: Permissions and approvals | Pulumi Agents
h1: Permissions and approvals
meta_desc: Configure Pulumi Cloud roles, connected credentials, approval modes, and teammate access for Pulumi Agents.
aliases:
- /docs/ai/concepts/neo/permissions/
- /docs/ai/neo/permissions/
menu:
    ai:
        name: Permissions and approvals
        parent: ai-agents
        identifier: ai-agents-permissions
        weight: 50
---

An agent's Pulumi Cloud permissions control access to stacks and ESC environments. Credentials for connected systems control what it can do in those systems. Approval modes determine when it asks for confirmation; an approval does not grant additional access.

## Pulumi Cloud access {#scope-pulumi-cloud-access}

For an agent your team creates, select a Pulumi Cloud role in its **Role** field. The role applies across its tasks. The default **Reader** role can read the organization's stacks, environments, and cloud accounts. Organizations using legacy roles retain the generated **Agent Read Only** default, which can read stack state, deployment settings, ESC environment definitions, and cloud account information, but cannot decrypt stack secrets or open ESC environments. See [Set its access](/docs/ai/agents/configure/#set-its-access) to change the assigned role.

By default, Neo uses your Pulumi Cloud permissions. Pulumi checks permissions each time a task accesses a resource, so revoking the account's access also removes the task's access.

<span id="what-neo-can-access-per-pulumi-cloud-area"></span>

Use [Pulumi Cloud roles](/docs/administration/concepts/rbac/) to restrict access to the stacks, ESC environments, deployment settings, policy results, cloud accounts, and audit logs the agent needs.

### Read-only mode {#the-core-invariant}

For Neo, choose **Read-only** in the task's permission settings to block Pulumi Cloud writes. The task can still read resources permitted by its role, run previews, change code, and prepare pull requests. In the CLI and API, the permission-mode values are `default` (use the account's permissions) and `read-only`.

Read-only mode also instructs Neo not to modify infrastructure, but does not restrict credentials used by connected tools. Those credentials must enforce any restrictions on AWS, Azure, Google Cloud, or other systems.

## Connected credentials {#scope-credentials-for-connected-tools}

<span id="design-access-around-the-job"></span>

Give each connection credentials for the resources and actions the agent needs. For example, checking S3 bucket settings requires permission to read those settings, but not to change them or read the bucket's objects. Use read-only credentials when the agent must not change resources. Instructions and integration selections do not reduce the permissions of those credentials.

Use a dedicated role or service account where supported. A user-owned token gives the agent the token owner's access. Prefer short-lived credentials; assign someone to rotate and revoke long-lived keys. Store credentials through the [integration setup](/docs/ai/agents/integrations/) or Pulumi ESC, never in task messages or instructions.

### ESC environments {#esc-secrets-and-downstream-cloud-access}

Cloud CLI integrations use `pulumi env run` to obtain credentials from an ESC environment. The agent's Pulumi Cloud role needs `environment:open` on that environment. Reading an environment definition does not grant this permission. The credentials returned by ESC determine what the CLI can do in the cloud account.

Limit which environments the agent can open, and use [ESC open approvals](/docs/esc/concepts/approvals/) when access requires review. An enabled connection still fails if the agent cannot open its environment.

Secrets supplied through ESC are accessible to the task and can reach the model if a command prints them. The agent is instructed not to run secret-revealing commands such as `pulumi env open` or `pulumi env get --show-secrets`. Pulumi replaces recognized credential patterns in task events with `[REDACTED]` before storing them, but cannot detect every secret. [MCP integration credentials](/docs/ai/integrations/external-mcp-servers/) are supplied to the integration without being exposed to the model.

## Approval modes {#separate-approvals-from-access}

<span id="permission-mode-and-approval-mode"></span>
<span id="the-control-inventory"></span>

For an agent your team creates, select **Edit** on its page and choose **Default mode**. For Neo, open **Task options** in the message box and choose a mode under **Autonomy**.

- **Manual** waits for a response to every approval request, including previews, pull requests, and deployments. Neo's console calls this mode **Review**; the CLI and API use `manual`.
- **Balanced** automatically approves routine requests, but waits for sensitive actions such as `pulumi up`, state-modifying `pulumi import`, and destructive changes.
- **Auto** automatically approves action requests. An agent with no saved mode also uses Auto, including when its configuration shows **Default**.

Questions that need information and approval to leave [plan mode](/docs/ai/agents/tasks/#plan-mode) require a response in every mode. After you approve a plan, the task's permissions and approval mode still apply.

Organization administrators set [the default mode for Neo tasks](/docs/ai/concepts/neo/settings/#task-modes). For command-line options, see [Use Neo in the CLI](/docs/ai/concepts/neo/neo-in-the-cli/).

### Approval requests {#what-triggers-an-approval-prompt}

When an agent runs tools in Pulumi Cloud, the tools for previews, deployments, and imports that change stack state request approval. The agent is instructed to request approval for other writes, including commits, pushes, and pull requests, and to mark destructive actions such as deletion or credential rotation as sensitive.

Approval modes do not check every shell command or integration call. A write allowed by connected credentials can occur without a separate approval request, including in **Manual** mode. Use roles and credentials to restrict operations such as `pulumi destroy`, `pulumi refresh`, state commands, and cloud CLI writes. When you use [`pulumi neo`](/docs/ai/concepts/neo/neo-in-the-cli/) to run commands on your machine, the CLI handles approval prompts.

## Teammate access {#give-teammates-access}

These rules apply to agents your team creates. For Neo, see [task sharing](/docs/ai/agents/tasks/#ownership-and-sharing).

### Start a task

A teammate needs `agent_task:create` and access to the agent. All organization members pass the agent role check when the agent uses the built-in **Reader** role or the generated **Agent Read Only** role. For other roles, a teammate passes the check if any of the following applies:

- They hold the agent's role directly or through a team.
- They have every permission the role grants across the entire organization.
- They have `organization:update`.

### View and contribute to tasks

Organization members who pass the agent role check above can view tasks started directly. Viewing does not require `agent_task:create`.

For tasks started by an organization-owned automation, `agent_automations:read` grants viewing access, and `agent_automations:update` grants access to reply and approve actions. Holding the agent's role alone does not grant access to these tasks.

Task owners and teammates with task-specific permissions can also access tasks: `agent_task:read` permits viewing, `agent_task:contribute` permits replies, and `agent_task:approve` permits approvals. Running a shared agent from a user-owned schedule does not give other teammates access to the resulting tasks.

All replies and approvals also require `agent_task:create`, including for task owners and automation runs.

## Identity {#execution-identity-per-surface}

Agents your team creates have their own identity and assigned Pulumi Cloud role. By default, Neo uses the account associated with the way you start the task:

| Entry point | Pulumi Cloud account |
| --- | --- |
| Pulumi Cloud console | The signed-in user |
| [`pulumi neo`](/docs/ai/concepts/neo/neo-in-the-cli/) | The account signed in with `pulumi login`; local commands also use local CLI logins, environment variables, and Kubernetes configuration |
| [Slack](/docs/ai/integrations/slack/) | The Pulumi account linked to the Slack user |
| [Code reviews and mentions](/docs/ai/concepts/neo/code-reviews/) | The linked GitHub author's account for automatic reviews; the requester's account for `@pulumi-neo` requests |
| Schedules created under a user account | The user who created the schedule |
| API requests with a user access token | The token's owner |
| API requests with an organization token | The organization's service account |

### Version control accounts {#vcs-identity-per-provider}

Version control uses the connected repository integration, which can have different permissions from the Pulumi Cloud account:

| Provider | Account used |
| --- | --- |
| GitHub.com | The shared Pulumi GitHub App for pull requests, commits, comments, and checks. Creating repositories requires a connected GitHub account. A linked account is also required to trigger code reviews. |
| GitHub Enterprise Server | The shared installation, or a connected user account when an administrator enables individual authentication. Requires Enterprise edition. User-owned scheduled tasks and API-created operations always use the shared installation. |
| Azure DevOps, GitLab, and Bitbucket | The organization integration for repository reads and writes. Connecting a user account also allows repository creation. |
| [Custom VCS](/docs/integrations/version-control/custom-vcs/) | Shared credentials from the integration's ESC environment. Supports cloning and pushing Git or Mercurial code, but not opening pull requests or creating repositories. |

When an operation requires a connected user account, the task asks you to connect it. Agents do not comment on Azure DevOps pull requests, GitLab merge requests, or Bitbucket pull requests. Comments from those version control integrations come from Pulumi Deployments. Agent [code reviews](/docs/ai/concepts/neo/code-reviews/) support GitHub.com only.

## Remove access {#review-and-remove-access}

Before revoking shared credentials, check which tasks and agents use them. To stop work already running, use the [agent controls](/docs/ai/agents/manage/#pause-future-work-and-stop-current-work) or [task controls](/docs/ai/agents/tasks/#interruptions-and-resuming).

<span id="learn-more"></span>
