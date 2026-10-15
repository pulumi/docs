---
title: "Pulumi ESC now issues OIDC tokens for any service"
date: 2026-10-15
draft: false
meta_desc: "Pulumi ESC now signs short-lived OIDC tokens for any audience you set, with a stable subject you can pin in each service's trust policy."
feature_image: feature.png
authors:
    - devon-grove
tags:
    - esc
    - oidc
    - security
    - features
category: product
schema_type: auto

social:
    twitter: |
        Pulumi ESC can now mint a short-lived OIDC token for any service that accepts one: Anthropic, Cloudsmith, JFrog Artifactory, and more.

        Set the audience, pin the subject in the service's trust policy, and delete the stored API key.
    linkedin: |
        Most services that matter to a deploy pipeline accept OpenID Connect tokens from an outside issuer, from package registries such as Cloudsmith and JFrog Artifactory to the Claude API through Anthropic's workload identity federation. Until now, a Pulumi ESC environment could only sign in that way to a fixed set of providers. For everything else it held a stored API key.

        The new fn::open::oidc provider removes that key. When you open the environment, ESC signs an OIDC token for an audience you choose, from ESC's general OIDC issuer. The service checks the signature, the audience, and a stable subject that names your organization and environment by ID, then issues its own short-lived credential. The token lives for an hour at most, and nothing is stored.

        The post walks through the environment definition, the claims in the token, a worked Anthropic example, and the one rule every trust policy needs: pin the subject.
    bluesky: |
        Pulumi ESC can now sign a short-lived OIDC token for any audience you choose. Anthropic, Cloudsmith, and JFrog can each exchange it for their own credential, so the stored API key goes away.

        One rule: pin the subject in the trust policy.
---

A [Pulumi ESC](/docs/esc/) environment can now mint a short-lived OpenID Connect (OIDC) token for any service that accepts one.

Every pipeline and agent that touches your infrastructure eventually needs credentials for services beyond your cloud: a package registry such as Cloudsmith or JFrog Artifactory, an AI platform such as Anthropic, or a workload access platform such as Aembit. The default historically has been to store a long-lived API key that sits in an environment, which presents a much higher risk of exposure than short-lived credentials.

With the new [`fn::open::oidc`](/docs/esc/providers/login/oidc/) provider, ESC signs a short-lived token for the audience you choose when you open the environment. The service named in that audience checks the signature and exchanges the token for a credential of its own. The token expires within the hour, and ESC stores nothing.

<!--more-->

## Why the stored key is the weak link

A stored key for a registry or an access platform sits in ESC until someone rotates it. It works for anyone who reads it, from any machine, for as long as it exists. If it leaks, you rotate it, and every consumer of the environment breaks until it picks up the new one.

An OIDC token works the other way around. ESC mints it at the moment you open the environment, signs it with a key only Pulumi holds, and stamps it with an expiry. The service checks it against the trust policy you configured and issues a credential with its own lifetime. You store nothing, so you rotate nothing.

## Why this matters for agents

An AI agent that opens an environment gets whatever the environment holds. A stored key works from anywhere until someone rotates it, and one bad prompt can copy it out. A `fn::open::oidc` token is tightly scoped and short-lived so your agents will only access what they need and nothing more.

## How it works

Declare the provider in an environment, name the audience the service expects, and export the token:

```yaml
values:
  aembit:
    login:
      fn::open::oidc:
        audience: https://acme.aembit.io
        duration: 15m
        identityToken:
          version: v2
  environmentVariables:
    AEMBIT_OIDC_TOKEN: ${aembit.login}
```

The provider takes three inputs. `audience` becomes the token's `aud` claim, the name the service checks. `identityToken.version: v2` selects the token format. `duration` sets the lifetime, from one minute to one hour, and defaults to one hour. ESC refuses any other input.

Opening the environment yields a signed token. Decoded and trimmed, its claims look like this:

```json
{
  "iss": "https://api.pulumi.com/oidc/v2",
  "sub": "pulumi:org:8a4f0c2e-91d3-4b6a-b7e0-5c2f8d1a9e44:env:2c9d7f61-3e58-4a02-9b8f-6d4e0a7c3b15",
  "aud": "https://acme.aembit.io",
  "exp": 1789000900,
  "https://pulumi.com/org": "acme",
  "https://pulumi.com/current_env": "aembit/login",
  "https://pulumi.com/actor": "alice",
  "https://pulumi.com/actor_id": "5f3a9c0d-7e21-4b8a-9d6c-1e0f2a3b4c5d"
}
```

The issuer publishes its signing keys through the standard discovery document at `https://api.pulumi.com/oidc/v2/.well-known/openid-configuration`, so most services need only the issuer URL. The subject names your organization and the environment that declares the block, by ID. IDs survive renames, and Pulumi never reuses one, so a trust policy that pins the subject keeps working and cannot be claimed by a later environment with the same name. The readable names travel in the `https://pulumi.com/` claims for your logs.

To see the exact claims before you touch a trust policy, swap in [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) with the same inputs. It returns the claims as plain values and signs nothing.

## Pin the subject

Pin the subject in every trust policy you write. Configure the policy with the issuer, the audience, and the subject. The service checks the signature against the issuer's published keys. The issuer and the audience confirm the token came from Pulumi and was meant for this service, and the subject confirms it came from your environment. Without the subject, the policy accepts a token from any Pulumi organization that typed the same audience string, since every organization shares the `/oidc/v2` issuer. Pulumi Cloud shows the subject above the environment editor with a copy button, so you never assemble it by hand.

## Example: Anthropic

Anthropic's [workload identity federation](https://platform.claude.com/docs/en/manage-claude/workload-identity-federation) lets a workload call the Claude API with a short-lived token from an issuer you trust instead of an `sk-ant-...` API key. In the Claude Console, open **Workload identity**, choose **Connect workload**, and pick **Custom OIDC**. Register `https://api.pulumi.com/oidc/v2` as the issuer with key discovery, create a service account, and create a federation rule that matches the environment's subject exactly and the audience `https://api.anthropic.com`.

Mint a token for that audience and export it beside the IDs the wizard shows you:

```yaml
values:
  anthropic:
    login:
      fn::open::oidc:
        audience: https://api.anthropic.com
        identityToken:
          version: v2
  environmentVariables:
    ANTHROPIC_IDENTITY_TOKEN: ${anthropic.login}
    ANTHROPIC_FEDERATION_RULE_ID: fdrl_...
    ANTHROPIC_ORGANIZATION_ID: <anthropic-org-id>
    ANTHROPIC_SERVICE_ACCOUNT_ID: svac_...
    ANTHROPIC_WORKSPACE_ID: wrkspc_...
```

Run the workload under the environment and every Claude SDK does the rest: it reads those variables, posts the token to `https://api.anthropic.com/v1/oauth/token`, and calls the API with the `sk-ant-oat01-...` access token it gets back. The code constructs the client with no key at all. Anthropic accepts each token once, so the access token lasts as long as the ESC token did; open the environment again for the next one.

Cloudsmith, JFrog Artifactory, and Aembit follow the same shape, and the [relying-party guide](/docs/esc/guides/configuring-oidc/custom-audience/) walks through each of them.

## Define it once, import it everywhere

The subject belongs to the environment that declares the block. Put `fn::open::oidc` in one environment, [import](/docs/esc/concepts/imports/) it from the environments that need the token, and each of them presents the same subject. Your trust policy stays at one entry. ESC checks open permission on every environment it loads, imports included, so only someone who can open the declaring environment can mint a token with that subject. Each token ESC mints adds an `environment-oidc-token-issued` entry to your organization's [audit log](/docs/administration/guides/audit-logs/) with the subject, the audience, the environment, and the lifetime.

## What stays the same

The `aws-login`, `azure-login`, `gcp-login`, and `vault-login` providers keep using the `https://api.pulumi.com/oidc` issuer with its own keys, so your existing trust relationships keep working. Use them when ESC can do the exchange for you, and `fn::open::oidc` when you need the token itself.

## Get started

`fn::open::oidc` is available now in every Pulumi Cloud organization.

1. Add a `fn::open::oidc` block with the service's audience and `identityToken.version: v2`, and save the environment.
1. Copy the **OIDC subject** shown above the environment editor into the service's trust policy, together with the `https://api.pulumi.com/oidc/v2` issuer and the audience.
1. Open the environment with [`pulumi env run`](/docs/iac/cli/commands/pulumi_env_run/) and exchange the token.

The [provider reference](/docs/esc/providers/login/oidc/) lists the inputs and the troubleshooting steps, and the [relying-party guide](/docs/esc/guides/configuring-oidc/custom-audience/) walks through Anthropic, Cloudsmith, JFrog Artifactory, and Aembit. Questions and feedback are welcome in the [Pulumi Community Slack](https://slack.pulumi.com/).
