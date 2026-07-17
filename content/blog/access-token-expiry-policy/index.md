---
title: "Enforce Access Token Expiry Policies in Pulumi Cloud"
date: 2026-07-17
draft: false
meta_desc: "Organization admins can now cap the maximum expiry of personal, organization, and team access tokens, so no credential outlives your rotation policy."
feature_image: feature.png
category: product
authors:
    - devon-grove
tags:
    - features
    - security
social:
    twitter: |
        A never-expiring access token is a breach waiting for a timeline. Pulumi Cloud organizations can now enforce a maximum expiry on every access token used against them.

        Set the cap once; the platform enforces it on every request.
    linkedin: |
        Every organization has a token rotation policy on paper. The hard part has always been enforcement: one long-lived personal token created before the policy existed, or one CI credential that never expires, quietly outlives every security review.

        Pulumi Cloud organizations can now enforce a maximum access token expiry — for personal, organization, and team tokens alike. Admins set a cap in days; the platform checks compliance on every request against the organization.

        Tokens that never expire, or whose remaining lifetime exceeds the cap, are rejected with a clear error telling the user exactly how to get back in: create a new token that meets the policy. Web console sessions are unaffected.

        Here's how it works and how to roll it out to your organization.
    bluesky: |
        Token rotation policies are easy to write and hard to enforce.

        Pulumi Cloud now enforces them for you: org admins can cap the max expiry of every access token used against their organization, checked on every request.
---

Pulumi Cloud organizations can now enforce a maximum expiry on the access tokens used against them. Organization admins set a cap in days, and from that point on, personal, organization, and team tokens must carry an expiration within the cap for requests against the organization to succeed. Tokens that never expire, or that have too much lifetime remaining, are rejected with an error that tells the user exactly how to regain access.

<!--more-->

## Why cap token lifetimes

Access tokens are the keys to your infrastructure: they authorize deployments, state access, and API automation. Most organizations already have a credential rotation policy that says tokens must expire — but until now, Pulumi Cloud could only *recommend* an expiry at creation time. Nothing stopped a member from creating a never-expiring personal token, and nothing aged out the long-lived tokens created before your policy existed.

That gap matters because a leaked token is only as dangerous as its remaining lifetime. A token that expires next week is a contained incident; a token that never expires is a standing liability that survives laptop refreshes, offboarding checklists, and secret-scanning sweeps.

The new **access token expiry policy** closes the gap at the platform level. You set the cap once, and Pulumi Cloud enforces it on every request against your organization — including for tokens that already exist.

## How it works

In your organization's settings, navigate to **Settings** > **Access Management**, open the **Access Tokens** tab, and set the policy under **Access token expiry policy**:

![The access token expiry policy card in Pulumi Cloud organization settings, showing a 1000-day cap and a preview listing one affected machine token.](/blog/access-token-expiry-policy/expiry-policy-settings.png)

The policy is a single number: the maximum expiry, in days, for tokens used against your organization. Compliance is checked on every request, and a token complies when both of these are true:

1. It has an expiration date. Never-expiring tokens violate any policy.
1. Its *remaining lifetime* — the time between now and its expiration — is within the cap.

Because compliance is based on remaining lifetime rather than the expiry chosen at creation, the policy is pragmatic about existing credentials: a token created a year ago with a two-year expiry becomes compliant once it has less than the cap remaining. You're enforcing exposure going forward, not retroactively punishing old tokens that are already near the end of their life.

Enforcement is tailored to each token type:

- **Organization and team tokens** can't be created out of compliance: the creation dialog caps the expiry picker at your policy maximum, and the API rejects requests that exceed it. Existing machine tokens that violate the policy stop authenticating and need to be recreated with a compliant expiry.
- **Personal tokens** span all of a user's organizations, so they can't be blocked at creation. Instead, a non-compliant personal token is rejected when it's used against your organization, and the member sees an error explaining the policy and how to fix it. The personal token creation dialog also warns members when a chosen expiry doesn't meet a policy in one of their organizations, steering them toward a compliant choice up front.
- **Web console sessions are unaffected**, as are the short-lived tokens issued through [OIDC token exchange](/docs/administration/access-identity/oidc-issuers/) — those are already bounded by their issuer.

## Rolling it out without breaking CI

The riskiest moment for any new enforcement policy is the moment you turn it on. Two things make that safe here.

First, **Preview affected tokens** shows you the blast radius before you save: every organization and team token that would stop authenticating under the proposed cap, by name and creator. Recreate those credentials with compliant expiries first, then save the policy.

Second, rejections are designed to be self-explanatory. A blocked request fails with a `403 Forbidden` that names your organization and its policy maximum, so a member whose personal token no longer complies knows immediately what happened and what to do: generate a new token that meets the policy. Policy changes are also recorded in your organization's [audit logs](/docs/administration/security-compliance/audit-logs/).

A reasonable rollout looks like:

1. Decide on a cap that matches your rotation policy — 90 days is a common choice for CI credentials.
1. Use **Preview affected tokens** and recreate any non-compliant machine tokens.
1. Tell your members: personal tokens without a compliant expiry will stop working against the organization.
1. Save the policy. From here on, the platform enforces it for you.

## Get started

The access token expiry policy is available now in your organization's access settings. For the full reference — compliance rules, per-token-type behavior, and exemptions — see the [access tokens documentation](/docs/administration/access-identity/access-tokens/#access-token-expiry-policy).

If you have feedback, we'd love to hear it in the [Pulumi Community Slack](https://slack.pulumi.com/) or on [GitHub](https://github.com/pulumi/pulumi/issues).
