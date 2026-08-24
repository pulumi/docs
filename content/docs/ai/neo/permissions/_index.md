---
title: Neo's permissions model
title_tag: Neo's permissions model | Pulumi Neo
h1: Neo's permissions model
meta_desc: What Pulumi Neo can do, which identity it acts as on each surface, how permission and approval modes constrain it, and how to scope its access.
menu:
    ai:
        name: Permissions model
        parent: ai-neo
        identifier: ai-permissions
        weight: 12
---

This page is the canonical reference for Neo's permissions model: what Neo can do, which identity it acts as on each surface, what constrains it, and how to scope it down. If you are a security reviewer or platform admin working out what Neo can do, as whom, and how to constrain it, start here.

## The core invariant

Neo acts on behalf of the user invoking it, and Neo can only do what that user could do themselves.

- Neo operates within the acting user's [role-based access control (RBAC)](/docs/administration/concepts/rbac/) entitlements and cannot perform actions that user couldn't perform.
- No privilege escalation: Neo never gets more access than the user has, only the same or less.
- Tasks are private to the user who created them. That user can [share a task](/docs/ai/neo/tasks/#ownership-and-sharing) with the rest of the organization as a read-only link: viewers see the conversation but cannot act through it, and any stack or resource it links to still enforces the viewer's own RBAC.

The rest of this page describes which user Neo acts as on each surface, the ceiling that user's RBAC sets, and the controls that narrow it further.

{{% notes type="info" %}}
Neo has no identity of its own: by default a task carries the acting user's full set of [role](/docs/administration/concepts/rbac/) assignments. On Enterprise and Business Critical editions, a task can instead assume a single role, and then runs with that role's permissions in place of the user's own assignments. You can only assume a role you already hold, so this narrows Neo's access and never widens it. Per-task roles are still rolling out; if your organization doesn't have them yet, the levers for constraining Neo are the acting user's RBAC and the ESC environments they can open.
{{% /notes %}}

## Execution identity per surface

Neo is one agent reachable from the surfaces below. Whichever surface starts a task, the task runs as a specific Pulumi identity:

| Surface | Runs as | Notes |
| :--- | :--- | :--- |
| Pulumi Cloud console | The signed-in user | The main home for tasks, automations, and settings. |
| [`pulumi neo`](/docs/ai/neo/pulumi-cli/) (CLI) | Your Pulumi user, via `pulumi login` | Also inherits your local setup: authenticated CLIs, environment variables, and kubeconfigs. |
| [Slack](/docs/ai/neo/integrations/slack/) | The Pulumi user linked to your Slack identity | Requires connecting your Slack identity in Neo settings first. |
| PR mentions / [code reviews](/docs/ai/neo/code-reviews/) | The Pulumi user matched to your VCS identity | Neo matches your GitHub identity to your Pulumi user. |
| [Scheduled automations](/docs/ai/neo/automations/) | The user who scheduled the automation | RBAC is evaluated at execution time — if that user's permissions change, the new permissions apply. |
| API / [MCP](/docs/ai/neo/integrations/mcp/)-created tasks | The Pulumi user whose token created the task | The task runs with that user's RBAC, exactly as if they had started it in the console. |

These identities govern what Neo does in Pulumi Cloud. Writes to your version control provider are a separate matter: Neo authenticates as the shared app installation for its VCS interactions no matter which surface started the task (see [VCS identity per provider](#vcs-identity-per-provider)).

Because a task's Pulumi RBAC is evaluated at execution time, it never runs with stale permissions: if the acting user is deactivated or loses access, the task loses that access immediately, including in the middle of a running task.

## What Neo can access, per Pulumi Cloud area

Neo's access ceiling is the acting user's RBAC. Within that ceiling, Neo reads broadly — it leans on the Pulumi Cloud APIs heavily to retrieve and search your infrastructure — and it makes changes two ways: through code and pull requests for anything you manage in IaC, and directly through the Pulumi Cloud APIs for anything you don't. Managing your Pulumi estate in IaC is what routes Neo's changes through code review.

| Area | What Neo can read | How Neo changes it |
| :--- | :--- | :--- |
| IaC stacks and state | Stack state, resources, and outputs for stacks the user can read | Proposes IaC code changes via [pull requests](/docs/ai/neo/pull-requests/) and runs `pulumi preview` / `pulumi up` (gated by [approval mode](#permission-mode-and-approval-mode)). It does not edit state directly. |
| Environments and secrets ([ESC](/docs/esc/)) | Any environment the user can open — including decrypting secrets and minting dynamic cloud credentials | Through ESC code changes where the environment is managed in IaC; otherwise Neo edits the environment definition directly. Environments with [update approvals](/docs/esc/concepts/approvals/) force those edits into a draft that a reviewer must approve. |
| Deployment settings | Settings the user can read | Through code and pull requests where the settings are managed in IaC; otherwise Neo edits them directly through the API. |
| Policy packs | Packs and results the user can read | No direct management of policy packs. |
| Cloud accounts | Accounts and scan results the user can read | No direct management of accounts. |
| Audit logs | Logs, if the user holds an audit-log read permission (typically Admin) | Read-only resource. |

### ESC, secrets, and downstream cloud access

Neo inherits the acting user's ESC access. If the user can [open](/docs/administration/concepts/rbac/) an environment (the `environment:open` permission), so can Neo — which means Neo can decrypt that environment's secrets and use any dynamic cloud credentials it mints. If an environment brokers OIDC credentials to an AWS, Azure, or Google Cloud account, Neo can assume those roles and operate in that cloud account, exactly as the user could.

This has two consequences worth stating plainly:

- **"Read-only" is scoped to Pulumi Cloud, not to your cloud accounts.** Read-only mode blocks writes in Pulumi Cloud and instructs Neo not to make modifications, but it does not technically prevent Neo from opening ESC environments or reaching the cloud accounts those environments unlock. Treat read-only as "no Pulumi Cloud mutations," not "no side effects anywhere."
- **Handling of secret values.** ESC secrets carry a weaker guarantee than [MCP integration credentials](/docs/ai/neo/integrations/mcp/), which are never exposed to the language model at all: an ESC-sourced secret value *can* reach the model if a task reads it directly. Three things limit that exposure. Neo is instructed never to run `pulumi env open` or `pulumi env get --show-secrets`, and where possible it moves secret values without reading them into context — for example, redirecting a cloud CLI's output straight to a file. Pulumi then scans the events a task produces for credential patterns and replaces what it detects with `[REDACTED]` before storing them, so detected values stay out of task history, shared task views, and Slack and pull request output. Treat that scan as defense in depth rather than a guarantee: it matches known credential shapes, not every string a secret value could take. Neo's models run through Amazon Bedrock, which does not retain prompts or completions, and an idle task's runtime session is torn down — the next turn rebuilds context from the stored, redacted history.

To constrain what Neo can reach, scope the acting user's RBAC and the ESC environments they can open. Prefer read-only cloud roles in ESC environments and broaden them deliberately. For the environments that unlock the most, [ESC open approvals](/docs/esc/concepts/approvals/) put a reviewer in front of every attempt to open them — including Neo's, since Neo opens them as you.

## Permission mode and approval mode

Neo has two independent axes of control. Do not conflate them:

| Axis | Values | Governs |
| :--- | :--- | :--- |
| **Permission mode** | `default` ("Use my permissions") / `read-only` | *What Neo can change.* Read-only removes the ability to trigger Pulumi Cloud writes while keeping read, preview, code, and PR abilities. |
| **Approval mode** (also called task mode) | Review / Balanced / Auto | *When Neo pauses for your approval.* Review is strictest; Auto never pauses. |

Approval-mode gates:

- **Review mode**: Neo requires approval before running `pulumi preview`, running `pulumi up`, and opening a pull request.
- **Balanced mode**: Neo requires approval only before running `pulumi up`.
- **Auto mode**: Neo does not require any approvals.

{{% notes type="info" %}}
In the `pulumi neo` CLI and the API, the strictest approval mode is named **`manual`**, which is the same mode the console calls **Review**. The permission-mode values (`default`, `read-only`) are the same in both places.
{{% /notes %}}

[Plan Mode](/docs/ai/neo/tasks/#plan-mode) is a separate, pre-execution control: it makes Neo research and agree on a plan with you before it acts, and it composes with any permission or approval mode.

## What triggers an approval prompt

Approval mode gates the Pulumi actions above — `pulumi preview`, `pulumi up`, and opening a pull request. It's important to understand what it does *not* gate.

By design, Neo investigates autonomously. During the investigation phase it reads state, opens ESC environments, and reaches the cloud accounts, clusters, and integrations it has access to **without prompting for each action** — an explicit tradeoff to avoid approval fatigue on the many small reads a real investigation requires. Approval prompts apply to the Pulumi write actions listed above (and to sensitive writes Neo surfaces for confirmation), not to bare read access.

The practical implication: if you need Neo to stay within a boundary, set that boundary with permissions (the user's RBAC and the ESC environments they can open), not by relying on approval prompts to catch every access.

## The control inventory

Every lever that shapes what a Neo task can do, and who sets it:

| Control | Values | Configured by | Where |
| :--- | :--- | :--- | :--- |
| Permission mode | `default` / `read-only` | User, per task | Task creation; `--permission-mode` in the CLI |
| Approval (task) mode | Review-`manual` / Balanced / Auto | User per task; org admin sets the default | Task UI; `--approval-mode` in the CLI; org default in [Settings](/docs/ai/neo/settings/#task-modes) |
| Plan Mode | On / off | User, per task | Task UI; **Shift+Tab** in the CLI |
| Per-automation overrides | Permission and approval mode | User who owns the automation | [Automations](/docs/ai/neo/automations/) |
| Disable integrations for a task | On / off | User, per task | `--disable-integrations` in the CLI |
| Neo on/off switch and per-feature toggles | On / off | Org admin | [Settings > Neo access](/docs/ai/neo/settings/#neo-access) |
| Integration enablement and credentials | Per integration | Org admin | [Integrations](/docs/ai/neo/integrations/) |

For scheduled automations, settings resolve in this order: the per-automation setting, then the org-level default, then the built-in fallback (auto approval and read-only permissions).

Org-level defaults for permission and approval mode set the starting point for new tasks; a user can override them per task.

[CLI integrations](/docs/ai/neo/integrations/cli/) are a distinct, admin-controlled capability: an organization admin points a CLI at an ESC environment, and every task in the organization is then offered that integration unless the user turns it off for the task. Being offered an integration is not the same as being able to use it. Neo invokes the CLI with `pulumi env run`, as the acting user, so the integration only works for users who can open the backing environment — for anyone else, the call fails with a permission error rather than handing over the environment's credentials. Connecting an integration doesn't widen anyone's access; it makes an environment the user could already open convenient for Neo to reach. Scope each integration's ESC environment to what Neo needs — prefer a read-only cloud role and broaden it deliberately.

## VCS identity per provider

Neo's version control writes do not run as you. Neo authenticates as the shared app installation for its VCS interactions — opening pull requests, pushing commits, commenting, posting checks. Creating a repository is the exception: that runs as your connected individual account, which is why it needs individual access.

| Provider | Neo writes as | Individual access | Notes |
| :--- | :--- | :--- | :--- |
| GitHub.com | The shared Pulumi GitHub App for all VCS interactions (opening PRs, pushing commits, PR comments, checks); your connected GitHub account for creating repositories | **Required** to create repositories and to trigger [Neo code reviews](/docs/ai/neo/code-reviews/); optional otherwise | When a task needs individual access you don't have connected, Neo posts a nudge prompting you to grant it. |
| GitHub Enterprise Server | The shared app installation by default; your connected account when individual user authentication is enabled | Enabled per integration by an admin, then connected per user | Business Critical edition. Scheduled Neo tasks and API-created operations always use the shared installation. |
| Azure DevOps | The org integration for repository reads and writes; individual access lets Neo create repositories | Optional | Neo does not comment on Azure DevOps pull requests. [Neo code reviews](/docs/ai/neo/code-reviews/) are GitHub-only, and the integration's pull request comments come from Pulumi Deployments, not Neo. |
| GitLab | The org integration for repository reads and writes; individual access lets Neo create repositories | Optional | Neo does not comment on GitLab merge requests. [Neo code reviews](/docs/ai/neo/code-reviews/) are GitHub-only, and the integration's merge request comments come from Pulumi Deployments, not Neo. |
| Bitbucket | The org integration for repository reads and writes; individual access lets Neo create repositories | Optional | Neo does not comment on Bitbucket pull requests. [Neo code reviews](/docs/ai/neo/code-reviews/) are GitHub-only, and the integration's pull request comments come from Pulumi Deployments, not Neo. |
| [Custom VCS](/docs/integrations/version-control/custom-vcs/) | The credentials from the integration's ESC environment — a shared identity belonging to whoever configured the integration | N/A | Neo can clone and push (Git and Mercurial) but cannot open pull requests or create repositories on Custom VCS servers. |

## Learn more

- [Role-based access control](/docs/administration/concepts/rbac/) — the permission model Neo inherits
- [Least-privilege access](/docs/administration/guides/least-privilege/) — scoping down what a user, and so Neo, can do
- [Pulumi ESC](/docs/esc/) — environments, secrets, and dynamic credentials
- [ESC approvals](/docs/esc/concepts/approvals/) — review gates on opening and updating an environment
- [Tasks](/docs/ai/neo/tasks/) — Plan Mode and approval modes in depth
- [Automations](/docs/ai/neo/automations/) — scheduled tasks and their defaults
- [Integrations](/docs/ai/neo/integrations/) — MCP and CLI integration credentials
- [Version control](/docs/integrations/version-control/) — per-provider VCS setup
