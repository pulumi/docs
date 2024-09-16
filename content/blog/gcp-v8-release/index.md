---
title: "Pulumi Google Cloud Provider Version 8.0.0"
date: 2024-09-16T10:08:42-07:00
draft: false
meta_desc: "Release of the next version of the Pulumi Provider for Google Cloud"
meta_image: meta.png
authors:
    - guineveresaenger
tags:
    - gcp
    - release
---

The latest major release of the Pulumi Google Cloud Provider is available now!
Our 8.0 release contains the latest upstream changes to keep you up-to-date along with the latest features and improvements from Pulumi.

The Pulumi Google Cloud provider can be used to provision any of the Google Cloud resources available in the upstream provider.
The provider is open source and available on GitHub so you can always follow along with current issues and developments, or even open your first pull request.

<!--more-->

Here are a few links to help you get started if you are new to Pulumi:

- [Getting Started](https://www.pulumi.com/docs/clouds/gcp/get-started/) - A guided walkthrough for creating your first project
- [Setup & Install](https://www.pulumi.com/registry/packages/gcp/installation-configuration/) - Instructions on installing the Google Cloud provider
- [How-to guides](https://www.pulumi.com/registry/packages/gcp/how-to-guides/) - Learn how to use the Google Cloud provider to provision specific resources
- [Templates](https://www.pulumi.com/templates/serverless-application/gcp/) - Use a quickstart template to create a new project
- [Pulumi AI](https://www.pulumi.com/ai) - Ask Pulumi AI to create a new project

## What’s New in 8.0

### Looking Back

Since the last major release of this provider, we have continuously shipped improvements to our ecosystem, bringing the latest Pulumi features to your production stack.
We have rolled out an improved diffing strategy in the Pulumi Terraform Bridge, removing spurious diffs on preview and increasing confidence when deploying.
Additionally we have worked hard to improve accuracy and coverage for registry documentation.

### Notable upstream features

Several resources have new `deletionProtection` fields:

- gcp.cloudrunv2.Service
- gcp.cloudrunv2.Job
- gcp.activedirectory.Domain
- gcp.organizations.Folder
- gcp.organizations.Project

A new default label, `goog-pulumi-provisioned` lets you discover your Pulumi-provisioned resources in the GCP console
to help you track resources and how they were created.
This label is available as an Output only and can be disabled in your provider configuration.
