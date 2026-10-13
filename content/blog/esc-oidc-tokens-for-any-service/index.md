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
        Pulumi ESC can now mint a short-lived OIDC token for any service that accepts one: Aembit, Cloudsmith, JFrog Artifactory, and more.

        Set the audience, pin the subject in the service's trust policy, and delete the stored API key.
    linkedin: |
        Most services that matter to a deploy pipeline accept OpenID Connect tokens from an outside issuer: package registries, secrets brokers, workload identity platforms. Until now, a Pulumi ESC environment could only sign in that way to a fixed set of providers. For everything else it held a stored API key.

        The new fn::open::oidc provider removes that key. When you open the environment, ESC signs an OIDC token for an audience you choose, from ESC's general OIDC issuer. The service checks the signature, the audience, and a stable subject that names your organization and environment by ID, then issues its own short-lived credential. The token lives for an hour at most, and nothing is stored.

        The post walks through the environment definition, the claims in the token, a worked Aembit example, and the one rule every trust policy needs: pin the subject.
    bluesky: |
        Pulumi ESC can now sign a short-lived OIDC token for any audience you choose. Aembit, Cloudsmith, and JFrog can each exchange it for their own credential, so the stored API key goes away.

        One rule: pin the subject in the trust policy.
---

A [Pulumi ESC](/docs/esc/) environment can now mint a short-lived OpenID Connect (OIDC) token for any service that accepts one.

Services such as Aembit, Cloudsmith, and JFrog Artifactory take an OIDC token from an outside issuer and trade it for their own short-lived credentials. Until now, an ESC environment could sign in that way only to a fixed set of providers. For everything else, it held a stored API key.

With the new [`fn::open::oidc`](/docs/esc/providers/login/oidc/) provider, ESC signs the token for an audience you choose when you open the environment. A service that trusts that environment exchanges the token for its own credential. The token is short-lived, and ESC stores nothing.

<!--more-->

## Why the stored key is the weak link

A stored key for a registry or a secrets broker sits in ESC until someone rotates it. It works for anyone who reads it, from any machine, for as long as it exists. If it leaks, you rotate it, and every consumer of the environment breaks until it picks up the new one.

An OIDC token works the other way around. ESC mints it at the moment you open the environment, signs it with a key only Pulumi holds, and stamps it with an expiry. The service checks it against the trust policy you configured and issues a credential with its own lifetime. You store nothing, so you rotate nothing.

## Why this matters for agents

An AI agent that opens an environment gets whatever the environment holds. A stored key works from anywhere until someone rotates it, and one bad prompt can copy it out. A `fn::open::oidc` token works for one service and expires within the hour, or within minutes if you set `duration`. Put the access an agent needs in its own environment, let Pulumi Cloud permissions decide who may open it, and pin each service's trust policy to that environment's subject. The agent reaches the services you chose and nothing else.

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
  "https://pulumi.com/actor": "alice"
}
```

The issuer publishes its signing keys through the standard discovery document at `https://api.pulumi.com/oidc/v2/.well-known/openid-configuration`, so most services need only the issuer URL. The subject names your organization and the environment that declares the block, by ID. IDs survive renames, and Pulumi never reuses one, so a trust policy that pins the subject keeps working and cannot be claimed by a later environment with the same name. The readable names travel in the `https://pulumi.com/` claims for your logs.

To see the exact claims before you touch a trust policy, swap in [`debug-oidc-claims`](/docs/esc/providers/login/debug-oidc-claims/) with the same inputs. It returns the claims as plain values and signs nothing.

## Pin the subject

Pin the subject in every trust policy you write. Every Pulumi organization shares the `/oidc/v2` issuer, and whoever mints the token picks the audience, so a policy that checks only those two accepts tokens from any organization that typed the same audience string. The service checks three things: the signature, through the issuer's published keys; the audience, which you chose; and the subject, which names your organization and environment by ID. Pulumi Cloud shows the subject above the environment editor with a copy button, so you never assemble it by hand.

## Example: Aembit

Aembit identifies a workload by its OIDC token and then hands it the credentials its access policy allows. In your Aembit tenant, create a trust provider of type **OIDC ID Token** that discovers keys from `https://api.pulumi.com/oidc/v2`, with match rules for the issuer, the audience from the environment, and the environment's subject. Then create a client workload identified by **OIDC ID Token Subject** with the same subject, and an access policy that joins the two to the credential provider the workload needs.

Open the environment and send the token to the Aembit Edge API at `https://<your-edge-url>/edge/v1/auth`, together with your Edge SDK client ID:

```json
{
  "clientId": "<client-id>",
  "client": {
    "oidc": {
      "identityToken": "<value of AEMBIT_OIDC_TOKEN>"
    }
  }
}
```

Aembit answers with an `accessToken` for its later calls, and the ESC token has done its job. Cloudsmith and JFrog Artifactory follow the same shape, and the [relying-party guide](/docs/esc/guides/configuring-oidc/custom-audience/) walks through each of them.

## Define it once, import it everywhere

The subject belongs to the environment that declares the block. Put `fn::open::oidc` in one environment, [import](/docs/esc/concepts/imports/) it from the environments that need the token, and each of them presents the same subject. Your trust policy stays at one entry, and ESC's own permissions decide who may open each importing environment. Each token ESC mints adds an `environment-oidc-token-issued` entry to your organization's [audit log](/docs/administration/guides/audit-logs/) with the subject, the audience, the environment, and the lifetime.

## What stays the same

The `aws-login`, `azure-login`, `gcp-login`, and `vault-login` providers keep using the `https://api.pulumi.com/oidc` issuer with its own keys, so your existing trust relationships keep working. Use them when ESC can do the exchange for you, and `fn::open::oidc` when you need the token itself.

## Get started

`fn::open::oidc` is available now in every Pulumi Cloud organization.

1. Add a `fn::open::oidc` block with the service's audience and `identityToken.version: v2`, and save the environment.
1. Copy the **OIDC subject** shown above the environment editor into the service's trust policy, together with the `https://api.pulumi.com/oidc/v2` issuer and the audience.
1. Open the environment with [`pulumi env run`](/docs/iac/cli/commands/pulumi_env_run/) and exchange the token.

The [provider reference](/docs/esc/providers/login/oidc/) lists the inputs and the troubleshooting steps, and the [relying-party guide](/docs/esc/guides/configuring-oidc/custom-audience/) walks through Cloudsmith, JFrog Artifactory, and Aembit. Questions and feedback are welcome in the [Pulumi Community Slack](https://slack.pulumi.com/).
