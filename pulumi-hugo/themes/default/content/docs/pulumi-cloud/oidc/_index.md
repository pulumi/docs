---
title_tag: OpenID Connect
meta_desc: This page provides an overview of how Pulumi can integrate with OIDC providers
title: OpenID
h1: OpenID Connect Provider integration
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        identifier: openid-connect
        weight: 5
---

Pulumi supports OpenID Connect (OIDC) integration across various services by leveraging signed, short-lived tokens and eliminating the necessity for hardcoded cloud provider credentials and facilitates the exchange of these tokens for short-term credentials.

## Overview

There are two ways Pulumi can integrate using OpenID Connect. Pulumi can operate as an [OIDC provider](/docs/pulumi-cloud/oidc/provider/) issuing signed, short-lived tokens that can be exchanged by short-term credentials from your cloud provider; or as an [OIDC client](/docs/pulumi-cloud/oidc/client/) accepting short-liver OIDC Tokens issued by a trusted OIDC provided to be exchanged by short-liver Pulumi access tokens.

## Solving the Secret Zero problem

The integration of different pieces of infrastructure and tools comes with the unavoidable requirement of distributing credentials across all the different pieces that interact. Different mechanisms evolved to make this process simpler, but there is always a last secret to unblock secure access to a secrets vault, this is known as "Secret Zero".

Relying on OpenId Connect solves the Secret Zero problem while complying with a Zero Trust model. It establishes a secure mechanism to exchange credentials between Pulumi and other services, removing the need to maintain that last secret and reducing the risk of leaking a credential that could make the entire system vulnerable.
