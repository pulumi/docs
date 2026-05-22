---
title_tag: "Agent Accounts | Pulumi Cloud"
meta_desc: Agent accounts let AI agents provision ephemeral Pulumi Cloud accounts automatically so agents can use state and ESC without manual signup.
title: Agent Accounts
h1: Agent accounts
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    administration:
        name: Agent Accounts
        parent: administration-organizations-teams
        weight: 2
---

{{% notes type="info" %}}
Agent accounts are in **preview**. Behavior and limits may change based on feedback.
{{% /notes %}}

Agent accounts automatically give AI agents a free ephemeral Pulumi Cloud account to work in, without requiring a human to sign up first. When the Pulumi CLI detects it is running in an agent context and no Pulumi Cloud credentials are available, it creates an account silently and continues. The human claims the account later to take permanent ownership.

## How it works

1. An AI agent uses the Pulumi CLI with an automatically-created ephemeral Pulumi Cloud account.
   - An AI agent (Claude Code, Codex, Cursor, etc.) runs a Pulumi CLI command that would normally prompt for login, such as `pulumi do`.
   - The Pulumi CLI finds no Pulumi Cloud credentials: no `PULUMI_ACCESS_TOKEN`, no entry in `~/.pulumi/credentials.json`.
   - Instead of prompting, the CLI provisions a new Pulumi Cloud account.
   - The CLI prints a claim link on stderr, where the agent sees it.
   - The CLI command continues and does its work normally in the new cloud account.
1. The agent relays the claim link to the user and continues to use Pulumi CLI to achieve their vision.
   - The CLI continues to print the claim link on stderr, where the agent sees it.
   - As time passes and new sessions occur, the agent re-presents the claim link periodically so it is not forgotten.
1. The user claims the account at any time by visiting the link and signing in.
   - All stacks and esc environments are transferred to the user's account.
   - The agent's access is disabled until the user logs in to their account.
1. The user logs the agent into their Pulumi Cloud account.
   - The user runs `pulumi login` or sets the `PULUMI_ACCESS_TOKEN` to their credentials.
1. The agent continues to use Pulumi CLI, collaborating with the user in their Pulumi Cloud account.
   - The Pulumi CLI finds Pulumi Cloud credentials and proceeds normally.

```
pulumi: created an agent account on Pulumi Cloud so this work persists.
        Claim within 30 days to take ownership.
        https://app.pulumi.com/claim/abc123
```

The agent does not block on the claim. It continues running commands while the user decides whether to claim. Only operations that require a claimed identity (inviting teammates, billing) wait for the claim.

## What agents can do with the account

The provisioned account is a Pulumi Cloud individual account. Agents can:

- Store and manage infrastructure state across sessions
- Use [Pulumi ESC](/docs/esc/) for secrets and configuration

## Claiming an account

The user clicks the claim link and signs in with any supported identity (GitHub, GitLab, Google, Atlassian, email/password, or SAML SSO). The claim replaces the placeholder identity with the user's real identity. All state, history, and resources transfer automatically. No migration is needed.

Claiming never reduces capability. Everything available before the claim is still available after, plus features gated on having a real identity (inviting teammates, billing, Neo).

## Lifecycle

**Active period (3 days).** The account is fully functional for 72 hours from creation. The CLI prints the claim link on every command that touches Pulumi Cloud, so the user has multiple opportunities to claim.

**Claim window (30 days).** After the active period, the account goes read-only. State stays, can be viewed, but cannot be updated or deployed. The user has 30 days from account creation to claim the account using the claim link. Claiming unlocks the account and restores full functionality.

**After the claim window.** If the account is not claimed within 30 days, it locks permanently. The user's cloud resources are never touched.

**Resources are never destroyed.** Pulumi state stays accessible in read-only mode after the active period ends. Cloud resources (S3 buckets, VMs, databases) created by the agent continue running in your cloud provider account regardless of the Pulumi Cloud account's state.

## When agent accounts are not created

The CLI does not provision a new account if:

- A valid `PULUMI_ACCESS_TOKEN` environment variable is set
- Valid credentials exist in `~/.pulumi/credentials.json`
- The user is already logged in to Pulumi Cloud

In these cases, the CLI uses the existing credentials. If multiple agents run on the same machine (for example, Cursor and Claude Code), the second agent reuses the credentials the first agent created.

## Limitations

- **Agent context only.** The automatic provisioning only triggers when the CLI detects it is running under an AI agent. Humans still see the standard login prompt.
- **Single user.** Agent accounts support one owner. Multi-admin is not available until the account is claimed and upgraded.
- **Active period is 3 days.** After 72 hours, unclaimed accounts go read-only. Claim within 30 days to restore full access.
- **Claim link is the only recovery path.** If the claim link is lost and no email was set, recovery requires running the CLI on the same machine where the account was created.

## See also

- [Pulumi Cloud accounts](/docs/administration/organizations-teams/accounts/)
- [The agentic infrastructure era](/blog/the-agentic-infrastructure-era/) (blog post)
- [Direct resource operations](/docs/iac/cli/direct-resource-operations/)
