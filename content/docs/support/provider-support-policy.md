---
title: Provider support policy
title_tag: "Pulumi provider support policy"
meta_desc: How long Pulumi maintains each provider major version, which providers get long-term support, and what a long-term support release contains.
h1: Provider support policy
menu:
    support:
        name: Provider support policy
        parent: support-home
        weight: 3
        identifier: support-provider-support-policy
---

Pulumi actively maintains the latest released major version of every provider it publishes.
For a set of widely used providers, Pulumi also ships security updates for the previous major version for up to 12 months, or until the next major version is released, whichever comes first.

## Providers covered

- `pulumi-aws`
- `pulumi-azure`
- `pulumi-azure-native`
- `pulumi-azuread`
- `pulumi-command`
- `pulumi-docker-build`
- `pulumi-gcp`
- `pulumi-kubernetes`
- `pulumi-tls`
- `pulumi-vault`

## Duration of long-term support

A provider's LTS branch is supported until the next major version ships, for up to 12 months.

## What ships on the long-term support branch

High/Critical CVE security patches:

- Fixes for CVEs affecting the provider's code or its direct dependencies.
- Fixes for broken internal infrastructure on the LTS branch needed to ship the above.

An LTS release does not contain:

- New upstream API versions.
- New resources or new resource properties.
- Performance improvements.
- Non-security bug fixes, including customer-reported bugs.
- Compatibility with newer versions of the Pulumi engine, the Pulumi SDKs, or language runtimes.

### Engine support

Providers will be compatible with the version of Pulumi they were frozen at unless otherwise prompted via security fixes.

## Summary

At any time, exactly one major version of a covered provider is the LTS version. Older majors receive no patches.

| Support phase | Which version | Duration | What ships |
| --- | --- | --- | --- |
| **Current major (N)** | The latest released major. If v3 is the newest release, v3 is N. | Until the next major, N+1, ships. | New features, new resources, bug fixes, security patches, dependency upgrades, and new upstream API versions. |
| **Long-term support (N−1)** | The major immediately before the current one. If v3 is N, then v2 is N−1. | Up to 12 months from the general availability of N, or until N+1 ships, whichever comes first. | Security updates in the provider's code or its direct dependencies. |
| **End of life (N−2 and older)** | Every older major. | — | Nothing. |

### What the policy guarantees

- Exactly one long-term support major exists per provider at any time.
- When N+1 ships, it becomes the new N, and the old N becomes the new LTS major.
  The old long-term support major reaches end of life on the same day, regardless of how much of its 12-month window remained.
- Within the long-term support major, only the latest minor version receives patches. Earlier minors are frozen.

## How to consume LTS releases

- LTS releases follow the same distribution channels as current-major releases (i. e. the relevant SDK package registries for each language), but are tagged differently.
- Customers pinning to a specific major version (recommended) will automatically receive patch releases as they ship.

## Learn more

- [Best practices for maintaining provider versions](/docs/support/faq/infrastructure/#what-are-the-best-practices-for-maintaining-provider-versions)
- [Pulumi Registry](/registry/)
- [Getting support](/docs/support/getting-support/)
