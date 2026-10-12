---
title: "Pulumi ESC now issues OIDC tokens for any service"
# TODO(devon): set the launch date. The far-future date keeps the post out of production; the PR preview still renders it.
date: 2099-01-01
draft: false
meta_desc: "Pulumi ESC now signs short-lived OIDC tokens for any audience you set, with a stable subject you can pin in each service's trust policy."
# TODO(devon): render feature.png with /blog-feature-image, or label the PR needs-design, then set feature_image: feature.png.
feature_image:
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
        Pulumi ESC can now mint a short-lived OIDC token for any service that accepts one: HashiCorp Vault, Cloudsmith, JFrog Artifactory, Aembit, AWS STS.

        Set the audience, pin the subject in the service's trust policy, and delete the stored API key.
    linkedin: |
        Most services that matter to a deploy pipeline accept OpenID Connect tokens from an outside issuer: package registries, secrets brokers, workload identity platforms. Until now, a Pulumi ESC environment could only sign in that way to a fixed set of clouds. For everything else it held a stored API key.

        The new fn::open::oidc provider removes that key. When you open the environment, ESC signs an OIDC token for an audience you choose, from the issuer https://api.pulumi.com/oidc/v2. The service checks the signature, the audience, and a stable subject that names your organization and environment by ID, then issues its own short-lived credential. The token lives for an hour at most, and nothing is stored.

        The post walks through the environment definition, the claims in the token, a worked HashiCorp Vault example, and the one rule every trust policy needs: pin the subject.
    bluesky: |
        Pulumi ESC can now sign a short-lived OIDC token for any audience you choose. Vault, Cloudsmith, JFrog, Aembit, and AWS STS can all exchange it for their own credential, so the stored API key goes away.

        One rule: pin the subject in the trust policy.
---

Services such as HashiCorp Vault, Cloudsmith, and JFrog Artifactory accept OpenID Connect (OIDC) tokens from an outside issuer and trade them for their own short-lived credentials. Until now, a [Pulumi ESC](/docs/esc/) environment could sign in that way to a fixed set of clouds. For everything else, it held a stored API key.

With the new [`fn::open::oidc`](/docs/esc/providers/login/oidc/) provider, ESC signs an OIDC token for an audience you choose when you open the environment. Any service that trusts the `https://api.pulumi.com/oidc/v2` issuer can exchange it. The token expires after an hour at most, and ESC stores nothing.

<!--more-->

## Why the stored key is the weak link

A stored key for a registry or a secrets broker sits in ESC until someone rotates it. It works for anyone who reads it, from any machine, for as long as it exists. When it leaks, you learn about it from the audit log or the bill, and the fix is a rotation that touches every consumer.

An OIDC token works the other way around. ESC mints it at the moment you open the environment, signs it with a key only Pulumi holds, and stamps it with an expiry. The service checks the signature and the claims, then issues a credential with its own lifetime. You store nothing, so you rotate nothing.

## How it works

Declare the provider in an environment, name the audience the service expects, and export the token:

```yaml
values:
  vault:
    login:
      fn::open::oidc:
        audience: https://vault.example.com
        duration: 15m
        identityToken:
          version: v2
  environmentVariables:
    VAULT_JWT: ${vault.login}
```

The provider takes three inputs. `audience` becomes the token's `aud` claim, the name the service checks. `identityToken.version` selects the token format; `v2` is the only value, and the input has no default, so an existing environment keeps its meaning if a later format arrives. `duration` sets the lifetime, from one minute to one hour, and defaults to one hour. ESC refuses any other input.

Opening the environment yields a signed token. Decoded and trimmed, its claims look like this:

```json
{
  "iss": "https://api.pulumi.com/oidc/v2",
  "sub": "pulumi:org:8a4f0c2e-91d3-4b6a-b7e0-5c2f8d1a9e44:env:2c9d7f61-3e58-4a02-9b8f-6d4e0a7c3b15",
  "aud": "https://vault.example.com",
  "exp": 1789000900,
  "https://pulumi.com/org": "acme",
  "https://pulumi.com/current_env": "vault/login",
  "https://pulumi.com/actor": "alice"
}
```

The issuer publishes its signing keys through the standard discovery document at `https://api.pulumi.com/oidc/v2/.well-known/openid-configuration`, so most services need only the issuer URL. The subject names your organization and the environment that declares the block, by ID. IDs survive renames, and Pulumi never reuses one, so a trust policy that pins the subject keeps working and cannot be claimed by a later environment with the same name. The readable names travel in the `https://pulumi.com/` claims for your logs.

To see the exact claims before you touch a trust policy, swap in [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) with the same inputs. It returns the claims as plain values and signs nothing.

## Pin the subject

Every Pulumi organization shares the `/oidc/v2` issuer, and any organization can set any audience. A trust rule that checks only the issuer and the audience accepts tokens from every organization that typed the same audience string. Pin the subject, or the `https://pulumi.com/org_id` claim, in every trust policy you write. Pulumi Cloud shows the subject above the environment editor with a copy button, so you never assemble it by hand.

## Example: HashiCorp Vault

Mount Vault's JWT auth method, point it at the issuer, and create a role that binds the audience and the subject:

```bash
vault auth enable -path=pulumi-esc jwt
vault write auth/pulumi-esc/config \
  oidc_discovery_url=https://api.pulumi.com/oidc/v2 \
  bound_issuer=https://api.pulumi.com/oidc/v2
vault write auth/pulumi-esc/role/deploy \
  role_type=jwt \
  bound_audiences=https://vault.example.com \
  user_claim=sub \
  bound_subject=pulumi:org:<org-id>:env:<environment-id> \
  token_policies=deploy \
  token_ttl=15m
```

Then log in from the environment:

```bash
pulumi env run acme/vault/login -- sh -c \
  'vault write auth/pulumi-esc/login role=deploy jwt="$VAULT_JWT"'
```

Vault returns a token scoped to the `deploy` policy and good for 15 minutes. The same shape works for Cloudsmith, JFrog Artifactory, Aembit, and AWS STS. The [relying-party guide](/docs/esc/guides/configuring-oidc/custom-audience/) has the exact settings for each.

## Define it once, import it everywhere

The subject belongs to the environment that declares the block. Put `fn::open::oidc` in one environment, [import](/docs/esc/concepts/imports/) it from the environments that need the token, and each of them presents the same subject. Your trust policy stays at one entry, and ESC's own permissions decide who may open each importing environment. Each token ESC mints adds an `environment-oidc-token-issued` entry to your organization's [audit log](/docs/administration/guides/audit-logs/) with the subject, the audience, the environment, and the lifetime.

## What stays the same

The `aws-login`, `azure-login`, `gcp-login`, and `vault-login` providers keep using the `https://api.pulumi.com/oidc` issuer with its own keys, so your existing trust relationships keep working. Use them when ESC can do the exchange for you, and `fn::open::oidc` when you need the token itself.

## Get started

`fn::open::oidc` is available now in every Pulumi Cloud organization.

1. Add a `fn::open::oidc` block with the service's audience and `identityToken.version: v2`, and save the environment.
1. Copy the **OIDC subject** shown above the environment editor into the service's trust policy, together with the `https://api.pulumi.com/oidc/v2` issuer and the audience.
1. Open the environment with [`pulumi env run`](/docs/iac/cli/commands/pulumi_env_run/) and exchange the token.

The [provider reference](/docs/esc/providers/login/oidc/) lists the inputs and the troubleshooting steps, and the [relying-party guide](/docs/esc/guides/configuring-oidc/custom-audience/) walks through Cloudsmith, JFrog Artifactory, Aembit, and Vault. Questions and feedback are welcome in the [Pulumi Community Slack](https://slack.pulumi.com/).
