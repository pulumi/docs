---
title_tag: Before You Begin | Pulumi IDP
title: Before you begin
h1: "Pulumi IDP: Before you begin"
meta_desc: This page provides an overview on how to get started with Pulumi IDP.
weight: 2
menu:
  idp:
    parent: idp-get-started
    identifier: idp-get-started-begin
---

Before you get started using Pulumi IDP, let's run through a few quick steps to ensure your environment is set up correctly.

### Create a Pulumi account

Pulumi IDP is a service of Pulumi Cloud, meaning you will need to create a Pulumi account to be able to use it. To do so, navigate to the [Pulumi Cloud console](https://app.pulumi.com) and create a new account. Once created, you can [optionally create an access token](/docs/pulumi-cloud/access-management/access-tokens/). Doing so will provide you an alternative way to sign into the Pulumi Cloud via the CLI. The token can also be used to automate your usage of the Pulumi Cloud using the REST API.

### [Optional] Configure OpenID Connect (OIDC)

Pulumi supports [OpenID Connect (OIDC) integration](/docs/pulumi-cloud/oidc/) across various services including Pulumi IDP. OIDC enables secure interactions between Pulumi and cloud providers by leveraging signed, short-lived tokens issued by the Pulumi Cloud. Use one of the following guides below to configure OIDC between Pulumi IDP and your chosen cloud provider:

- [OIDC Configuration for AWS](/docs/pulumi-cloud/oidc/provider/aws/)
- [OIDC Configuration for Azure](/docs/pulumi-cloud/oidc/provider/azure/)
- [OIDC Configuration for Google Cloud](/docs/pulumi-cloud/oidc/provider/gcp/)

This is an optional step that is not required to get started with Pulumi IDP. There are some steps in this series that will require OIDC configuration to complete, but that will be indicated on the relevant pages.

In the next section, you will start your journey with Pulumi IDP by creating a new environment.

{{< get-started-stepper >}}
