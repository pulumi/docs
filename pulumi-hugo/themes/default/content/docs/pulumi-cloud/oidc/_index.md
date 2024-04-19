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

There are two ways Pulumi can integrate using OpenID Connect. Pulumi can operate as an [OIDC provider](/docs/pulumi-cloud/oidc/provider/) issuing signed, short-lived tokens that can be exchanged by short-term credentials from your cloud provider; or as an [OIDC client](/docs/pulumi-cloud/oidc/client/) accepting OIDC tokens issued by a trusted OIDC provider to be exchanged for short-lived Pulumi access tokens.


## Solving the Secret Zero problem

Often before to integrate with Pulumi from a cloud or CICD provider you would have to maintain a static, long-term access token, sometimes known as "secret zero". These secrets are often set and forgotten, leading to security issues if they need to be rotated or or in the event they are compomised.

OIDC is an alternative to distributing long-term, static credentials by relying on digitally-signed identity tokens issued by the cloud provider. The process involves configuring a trust relationship between providers based on public-key cryptography.

An OIDC token represents the identity of an application or workload that is running in a particular cloud environment, and is often called a workload identity. The token contains claims such as the application's name for identification purposes. A service provider may be configured to allow access to resources based on these claims.
