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

There are two ways Pulumi can integrate using OpenID Connect.  Pulumi can operate as an [OIDC provider](/docs/pulumi-cloud/oidc/provider/) issuing signed, short-lived tokens that can be exchanged by short-term credentials from your cloud provider; or as an [OIDC client](/docs/pulumi-cloud/oidc/client/) accepting short-liver OIDC Tokens issued by a trusted OIDC provided to be exchanged by short-liver Pulumi access tokens.
