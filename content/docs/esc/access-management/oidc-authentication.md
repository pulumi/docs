---
title_tag: Configure OpenID Connect authentication | Pulumi ESC
meta_desc: This page provides an overview of how Pulumi ESC can be configured for OIDC authentication with a trusted identity provider.
title: Configure OpenID authentication with ESC
h1: Configure OpenID Connect authentication
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  esc:
    name: OIDC authentication
    parent: pulumi-esc-access-management
    weight: 3
---

Pulumi supports secure authentication by integrating with trusted external identity providers using OpenID Connect (OIDC). When configured as an OIDC client, Pulumi establishes a trust relationship with third-party providers such as Google, AWS or GitHub to accept and validate their issued OIDC tokens. After validation, these tokens are exchanged for short-lived Pulumi access tokens, which removes the need for hardcoded credentials.

To integrate Pulumi with a third-party identity provider, see the detailed [OIDC Client documentation](/docs/pulumi-cloud/access-management/oidc/client/).
