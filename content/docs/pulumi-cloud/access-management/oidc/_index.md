---
title_tag: OpenID Connect
meta_desc: This page provides an overview of how Pulumi can integrate with OIDC providers
title: OpenID
h1: OpenID Connect Provider integration
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  cloud:
    name: OpenID
    parent: pulumi-cloud-access-management
    weight: 4
    identifier: pulumi-cloud-access-management-oidc
aliases:
- /docs/pulumi-cloud/oidc/
---

Pulumi supports OpenID Connect (OIDC) integration across various services by leveraging signed, short-lived tokens and eliminating the necessity for hardcoded cloud provider credentials and facilitates the exchange of these tokens for short-term credentials.

## Overview

There are two ways Pulumi can integrate using OpenID Connect. Pulumi can operate as an [OIDC provider](/docs/pulumi-cloud/oidc/provider/) issuing signed, short-lived tokens that can be exchanged by short-term credentials from your cloud provider; or as an [OIDC client](/docs/pulumi-cloud/oidc/client/) accepting OIDC tokens issued by a trusted OIDC provider to be exchanged for short-lived Pulumi access tokens.

## Solving the Secret Zero problem

When teams adopt Pulumi, securely managing authentication is the cornerstone of a strong security posture. One approach is to integrate Pulumi with a cloud or CI/CD provider using a long-term access token, but this introduces the "secret zero problem" and potential security risks. These credentials are often set once and forgotten, making them vulnerable if rotation is needed or if they become compromised.

The best practice for securing Pulumi and provider authentication is to use OIDC, which replaces static credentials with short-term digitally signed identity tokens issued by the cloud provider. This approach eliminates the need for long-lived secrets by establishing a trust relationship using public-key cryptography.

An OIDC token represents an application's or workload's identity in a cloud environment—often called a workload identity. It includes claims such as the application's name, which a service provider can use to grant access to resources based on best-practice security policies.
