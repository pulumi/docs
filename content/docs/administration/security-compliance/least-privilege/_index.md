---
title_tag: "Least Privilege on the Pulumi Cloud Platform"
meta_desc: How to apply least-privilege security across Pulumi IaC, ESC, and CI/CD, from cloud provider credentials to Pulumi Cloud RBAC.
title: Least Privilege on the Pulumi Cloud Platform
h1: Least privilege on the Pulumi Cloud Platform
menu:
    administration:
        name: Least Privilege
        parent: administration-security-compliance
        weight: 5
        identifier: administration-security-compliance-least-privilege
aliases:
- /docs/iac/operations/iac-least-privileges/
- /docs/iac/using-pulumi/iac-least-privileges/
- /docs/iac/guides/basics/iac-least-privileges/
---

Least privilege means giving every person, pipeline, and program only the access it needs, and no more. In the context of a Pulumi IaC program with Pulumi Cloud as the backend, that access takes two related forms:

- The **cloud provider credentials** your Pulumi programs use to create and change real infrastructure in AWS, Azure, Google Cloud, and elsewhere.
- **Access to Pulumi Cloud itself**, governed by [role-based access control (RBAC)](/docs/administration/access-identity/rbac/), which decides who can read state, run updates, and unlock secrets.

Over-broad cloud credentials can damage running infrastructure, and over-broad Pulumi Cloud access can expose secrets or delete stacks and their state. This guide works through both, across the three places where you make access decisions: your infrastructure code (IaC), your secrets and configuration (ESC), and your automation ([CI/CD](/docs/iac/operations/continuous-delivery/) and [Pulumi Deployments](/docs/deployments/concepts/), Pulumi Cloud's managed execution service).

{{% notes type="info" %}}
Pulumi Cloud's configurable RBAC features, including custom roles, permission sets, and team role assignments, are only available in the Pulumi Enterprise or Business Critical editions. To learn more, see the [pricing page](/pricing/).
{{% /notes %}}

## How a Pulumi program gets its privileges

A Pulumi program is ordinary application code. It runs on whatever machine invokes it, whether that is a developer's laptop or a CI runner, and it acts with whatever credentials that machine can reach. Anything the code and those credentials permit, the program can do, including reading the secrets and configuration it loads at runtime. None of this is specific to Pulumi; it holds for every infrastructure as code tool.

This has two practical consequences:

1. Whoever can run a program can use the cloud credentials that run has access to. Controlling who runs programs, and where, matters as much as controlling the credentials themselves.
1. Whoever can run a program against an [ESC](/docs/esc/) environment can cause its secrets and dynamic credentials to be resolved. The sensitive boundary is not read access to a stack. It is the ability to open an environment or run an update.

## Prefer short-lived credentials

One principle runs through everything below: wherever you can, use short-lived credentials issued on demand instead of long-lived keys or tokens stored on disk. This applies to both kinds of access, and each has its own mechanism. For cloud provider credentials, [ESC login providers](/docs/esc/providers/login/) exchange an OIDC token for temporary cloud credentials. For access to Pulumi Cloud from automation, [OIDC issuers](/docs/administration/access-identity/oidc-issuers/) let a pipeline authenticate without a stored Pulumi token. The sections below note where each applies.

## Cloud provider credentials

### Broad credentials are often unavoidable

Most Pulumi programs need broad cloud credentials to do their job, as do most infrastructure as code tools that execute locally, such as Terraform and OpenTofu. A program that stands up a complete workload creates, updates, and deletes resources across many services, so the credentials it runs with tend to be wide-ranging within a target account or subscription.

You can scope cloud IAM more tightly, so a given principal deploys only certain resource types into certain environments. That is a legitimate way to reduce risk, but it comes at a cost: more IAM to maintain, and often awkward program design. You may lose the ability to have one Pulumi program deploy a workload end to end, for example. Tighten cloud IAM where the risk justifies the effort, rather than as a blanket policy.

### Not everyone needs full access everywhere

Your mileage will vary here, and the right split depends on how your teams work, but a good starting point is to separate who can change production from who can only look at it:

1. Give engineers read-only access to production cloud accounts for troubleshooting and inspection.
1. Route write access to production through CI/CD or Pulumi Deployments rather than individual laptops.
1. Keep any direct, elevated production access behind an audited break-glass process.

These are suggestions, not hard rules. Some teams run comfortably with more open access in low-risk accounts, and others lock things down further.

## Least privilege in Pulumi IaC

Pulumi Cloud [RBAC](/docs/administration/access-identity/rbac/) decides who can view and update stacks. Use it to keep access to state and updates narrow.

### Start from conservative defaults

Set your organization's default stack permission to None or Read, so people start with little and receive more only when they need it. The [roles documentation](/docs/administration/access-identity/rbac/roles/#organization-wide-role-settings) covers where to configure this and how the built-in Member role interacts with custom roles.

{{% notes type="info" %}}
Organization-wide role settings are retained from Pulumi Cloud's pre-RBAC permission system for backward compatibility. For new, fine-grained access control, prefer custom roles and permission sets.
{{% /notes %}}

### Grant access explicitly through permission sets and teams

{{< pulumi-cloud "teams" />}}

Grant elevated access with [permission sets](/docs/administration/access-identity/rbac/permission-sets/#stack-permission-sets), assigned through roles and teams rather than to individuals:

- **Stack Read**: read-only access to stacks, including running previews.
- **Stack Write**: update stack configuration and run updates.
- **Stack Admin**: full control over stack operations.

Organize people into [teams](/docs/administration/access-identity/rbac/teams/) and give each team the least access its work requires. A team can hold one or more roles and be granted access to specific stacks. You can also grant a team access to a stack when you create it:

```bash
pulumi stack new --teams YourTeamName
```

That gives the named team permission to read and update the new stack.

### Match access to the environment

Let the sensitivity of an environment set how much direct access people have:

- In development and test, let engineers run `pulumi up` directly. Fast local iteration is where that access earns its keep.
- In production and other sensitive environments, keep direct execution to a minimum, send changes through pull request review, and run updates in automation. The sections below cover how.

## Least privilege in Pulumi ESC

[Pulumi ESC](/docs/esc/) holds secrets and configuration, and it can mint short-lived cloud credentials on demand. The action that matters most for an environment is opening it, since that is what resolves its secrets and credentials. Treat ESC access on its own terms rather than folding it into stack access.

Grant environment access with [environment permission sets](/docs/administration/access-identity/rbac/permission-sets/#environment-permission-sets):

- **Environment Read**: read the definition, but not the secrets or credentials.
- **Environment Open**: read the environment and decrypt its secrets and retrieve dynamic credentials.
- **Environment Write**: open and update the environment.
- **Environment Admin**: full control, including deletion.

When you grant a team environment access, Pulumi Cloud labels these Environment reader, opener, editor, and admin. The [teams reference](/docs/administration/access-identity/rbac/teams/) has the full mapping.

A few practices keep ESC access tight:

1. Reserve Environment Open on production environments for automation and a small set of trusted people, since it is the permission that exposes live secrets.
1. Default the organization's environment permission to None or Read, and grant Open or Write deliberately.
1. Use [dynamic login credentials](/docs/esc/providers/login/) so that opening an environment hands back short-lived credentials instead of stored secrets.

### Scope the roles an environment can assume

When ESC logs in to a cloud provider over OIDC, the cloud IAM role's trust policy decides which environments may assume it. By default that trust policy is broad, so any environment in your organization can assume the role. A custom subject claim tightens it.

[Configuring OIDC for AWS](/docs/esc/guides/configuring-oidc/aws/) walks through this. With the `subjectAttributes` property, you can shape ESC's OIDC subject so a role's trust policy matches only a specific environment, and optionally a specific user. A production database role, for instance, can be written to be assumable only from your `production` environment, so a lower environment cannot borrow it even if someone is able to open that environment.

### Segment environments around your secret stores

The same idea applies when ESC reads from a cloud's managed secret store, such as AWS Secrets Manager or Parameter Store, Azure Key Vault, or Google Secret Manager. ESC assumes a role over OIDC to read those values, and reusing one broad, general-purpose role for the job is tempting. Prefer a role scoped to only the secrets that environment needs.

For example, an environment that imports a handful of values from [AWS Secrets Manager](/docs/esc/providers/secrets/aws-secrets/) should assume a role whose policy allows reading only those secret paths, not a role with full Secrets Manager or account access. Splitting secrets across separate environments, each with its own narrowly scoped role, stops one environment from becoming a path to credentials it was never meant to reach.

## Least privilege in CI/CD and Deployments

For production and other sensitive environments, keep execution off individual machines and run updates through automation instead. That confines broad cloud credentials to an auditable place and puts every change behind review.

### Pulumi Deployments

[Pulumi Deployments](/docs/deployments/concepts/) is Pulumi Cloud's managed execution service. It runs your Pulumi operations on Pulumi-hosted or self-hosted compute in response to version control events, a schedule, or the REST API, rather than on a laptop.

Its default posture is already conservative. A deployment triggered by a git push or pull request runs with an ephemeral stack token that has admin rights on that stack alone and nothing else. When a deployment needs more, grant it through [role assignment](/docs/deployments/operations/permissions/): assign the deployment a least-privilege organization role instead of a broad token, and its stack token inherits only that role's permissions. For cloud credentials, pair this with [Deployments OIDC](/docs/deployments/guides/oidc/) so the runner assumes a scoped cloud role rather than carrying stored keys.

### CI/CD with OIDC

If you run your own CI/CD, prefer OIDC token exchange over a stored Pulumi token. Your pipeline presents an OIDC token from its platform, and Pulumi Cloud exchanges it for a short-lived access token. Any service that can issue OIDC tokens can be registered as a trusted [OIDC issuer](/docs/administration/access-identity/oidc-issuers/):

- On [GitHub Actions](/docs/administration/access-identity/oidc-issuers/github/), the `pulumi/auth-actions` action performs the exchange and can request a team-scoped token, so the run acts within a single team's permissions.
- On [GitLab CI](/docs/administration/access-identity/oidc-issuers/gitlab/), and any other platform that can mint an OIDC token, `pulumi login --oidc-token` performs the same exchange directly through the CLI.

Scope these tokens as narrowly as the work allows. Team-scoped tokens, which confine a run to one team's permissions, require the Enterprise or Business Critical edition.

### Long-lived access tokens

Where OIDC is not an option, you can fall back to a stored [Pulumi access token](/docs/administration/access-identity/access-tokens/). This is the least preferable choice, because a long-lived token in a CI secret is exactly the standing credential OIDC is designed to remove. If you must use one, prefer a team or organization token over a personal one, give it the shortest workable expiration, and rotate it regularly.

## Audit and review access

Least privilege drifts over time, so check it on a regular cadence:

1. Review [audit logs](/docs/administration/security-compliance/audit-logs/) for access and deployment activity.
1. Watch ESC usage for environments being opened when you would not expect it.
1. Revisit team and role assignments periodically, and remove access no one is using.

## Summary

- **Both credential types matter equally.** Guard cloud provider credentials and Pulumi Cloud access with the same seriousness.
- **Cloud credentials:** accept that IaC often needs broad access, but do not give every principal that access in every environment. Favor read-only production for people, production writes through automation, and short-lived credentials over stored keys.
- **IaC:** default organization stack permissions to None or Read, and grant Stack Read, Write, or Admin explicitly through roles and teams.
- **ESC:** treat Environment Open as the sensitive permission, scope the cloud roles an environment can assume, and segment environments around their secret stores.
- **CI/CD and Deployments:** run production changes through Pulumi Deployments or an OIDC-authenticated pipeline, and reserve long-lived tokens for when OIDC is not available.
- **Audit:** review logs and access grants regularly.
