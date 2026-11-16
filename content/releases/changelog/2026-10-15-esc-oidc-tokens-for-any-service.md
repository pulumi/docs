---
title: "Pulumi ESC now issues OIDC tokens for any service"
date: 2026-10-15
meta_desc: Pulumi ESC can now sign short-lived OIDC tokens for any audience you set, with a stable subject you can pin in each service's trust policy.
authors:
    - christian-nunciato
---

Pulumi ESC can now sign short-lived OIDC tokens for any service, not just the clouds it already integrates with. Set the audience you need, and ESC issues a token with a stable subject you can pin in that service's trust policy — so you can authenticate to any OIDC-aware system with a credential that expires instead of a long-lived secret.

To learn more, read the [announcement post](/blog/esc-oidc-tokens-for-any-service/) or the [custom audience documentation](/docs/esc/guides/configuring-oidc/custom-audience/).
