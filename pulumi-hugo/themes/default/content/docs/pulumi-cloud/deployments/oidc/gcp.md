---
title_tag: Configure OpenID Connect for Google Cloud | OIDC
meta_desc: This page describes how to configure OIDC token exchange in Google Cloud for use with Pulumi Deployments
title: Google Cloud
h1: Configuring OpenID Connect for Google Cloud
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    pulumicloud:
        parent: deployments-oidc
        weight: 1

aliases:
- /docs/guides/oidc/gcp
- /docs/intro/deployments/oidc/gcp/
---

This document outlines the steps required to configure Pulumi Deployments to use OpenID Connect to authenticate with Google Cloud. OIDC in Google Cloud uses [workload identity federation](https://cloud.google.com/iam/docs/workload-identity-federation) to allow access to resources. Access to the resources is authorized using attribute conditions that validate the contents of the OIDC token issued by the Pulumi Cloud.

## Prerequisites

* You must be an admin of your Pulumi organization.

## Creating a Google Cloud Workload Identity Provider

To create the Google Cloud Workload Identity Provider, see the [relevant Google Cloud documentation](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-providers).

When following the instructions in the documentation:

* For the provider issuer, use `https://api.pulumi.com/oidc`
* For the audience, use the name of your organization
* Recall the [format of the subject claim](/docs/guides/oidc/#overview) when adding attribute conditions that check the value of the `google.subject` attribute

Make a note of the workload identity pool ID, provider ID, and service account email address. These will be necessary to enable OIDC for your stack.

## Enabling OIDC for your Stack

1. Navigate to your stack in the Pulumi Console.
2. Open the stack's "Settings" tab.
3. Choose the "Deploy" panel.
4. Under the "OpenID Connect" header, toggle "Enable Google Cloud Integration".
5. Enter the numerical ID of your Google Cloud project in the "Project ID" field.
6. Enter the workload pool ID, identity provider ID, and service account email address in the "Workload Pool ID", "Identity Provider ID", and "Service Account Email Address" fields.
7. If desired, enter the stack's Google Cloud region in the "Region" field. This is typically unnecessary.
8. If you would like to constrain the duration of the temporary Google Cloud credentials, enter a duration in the form "XhYmZs" in the "Session Duration" field.
9. Click the "Save deployment configuration" button.

With this configuration, each deployment of this stack will attempt to exchange the deployment's OIDC token for Google Cloud credentials using the specified federated identity prior to running any pre-commands or Pulumi operations. The fetched credentials are published as a credential configuration in the `GOOGLE_CREDENTIALS` environment variable. The raw OIDC token is also available for advanced scenarios in the `PULUMI_OIDC_TOKEN` environment variable and the `/mnt/pulumi/pulumi.oidc` file.
