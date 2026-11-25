---
title: Network addresses
title_tag: Pulumi Cloud Network Addresses to Allowlist
h1: Network addresses
meta_desc: The hostnames and IP addresses to allowlist when your network restricts traffic to or from Pulumi Cloud.
menu:
  administration:
    name: Network addresses
    parent: administration-reference
    identifier: administration-reference-network-addresses
    weight: 4
---

If your network restricts egress to Pulumi Cloud or ingress from it, allowlist the following external addresses of the Pulumi Cloud SaaS.

| Type | Address |
|:-----|:--------|
| Hostname | `app.pulumi.com` |
| Hostname | `api.pulumi.com` |
| IP address | `34.208.94.47` |
| IP address | `34.212.116.224` |
| IP address | `44.241.59.217` |
| IP address | `52.40.198.20` |

These addresses apply to the hosted service only.
A [self-hosted](/docs/administration/self-hosting/) Pulumi Cloud uses the addresses of your own deployment.
