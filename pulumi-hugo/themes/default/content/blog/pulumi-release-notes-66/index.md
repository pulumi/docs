---
title: "Jan. releases: Pulumi Packages support for plugins hosted anywhere and Pulumi Service 3rd party audit for secrets decryption"

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-01-26T13:20:48-08:00

allow_long_title: true

# Draft posts are visible in development, but excluded from production builds.
# Set this property to `false` before submitting your post for review.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
meta_desc: The latest Pulumi updates also include Pulumi import support for Kubernetes CRD, various improvements to Helm Release, and native ES Module support.

# The meta_image appears in social-media previews and on the blog home page.
# A placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the `id`
# properties of the team member files at /data/team/team. Create a file for yourself
# if you don't already have one.
authors:
    - meagan-cojocar

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - features

# See the blogging docs at https://github.com/pulumi/docs/blob/master/BLOGGING.md.
# for additional details, and please remove these comments before submitting for review.
---

Over the holidays we have been releasing new features and improvements. Read on to learn about what's new in this release!

- Cloud Providers and Packages
  - [New `Command` package]({{< relref "/blog/pulumi-release-notes-66#new-command-package" >}})
  - [Support pulumi import for Kubernetes CRDs]({{< relref "/blog/pulumi-release-notes-66#support-pulumi-import-for-kubernetes-crds" >}})
  - [Various improvements to Helm Release]({{< relref "/blog/pulumi-release-notes-66#various-improvements-to-helm-release" >}})
- Pulumi CLI and core technologies
  - [Support using native ES modules as Pulumi scripts]({{< relref "/blog/pulumi-release-notes-66#support-using-native-es-modules-as-pulumi-scripts" >}})
  - [Support packages with plugins hosted in any third-party location]({{< relref "/blog/pulumi-release-notes-66#support-packages-with-plugins-hosted-in-any-third-party-location" >}})
  - [State locking default enabled]({{< relref "/blog/pulumi-release-notes-66#state-locking-default-enabled" >}})
- Pulumi Service
  - [Audit logging for third-party secrets managers]({{< relref "/blog/pulumi-release-notes-66#audit-logging-for-third-party-secrets-managers" >}})

<!--more-->

## Cloud Providers and Packages

### New `Command` package

As part of creating or updating infrastructure, it is often necessary to run scripts and/or commands. In order to improve this experience we released a new [Pulumi Command package]({{< relref "/registry/packages/command" >}}) in the Pulumi Registry which enables users to run scripts locally or remotely on a target VM as part of the Pulumi resource lifecycle.

This new package is supported in all Pulumi languages.

The Command package supports quite a few common patterns involving local and remote scripts execution, such as:
- [A simple local resource (random)]({{< relref "registry/packages/command#a-simple-local-resource-random" >}})
- [Remote provisioning of an EC2 instance]({{< relref "/registry/packages/command#remote-provisioning-of-an-ec2-instance" >}})
- [Invoking a Lambda during a Pulumi deployment]({{< relref "/registry/packages/command#invoking-a-lambda-during-pulumi-deployment" >}})
- [Using local.Command with curl to manage an external REST API]({{< relref "/registry/packages/command#using-localcommand-with-curl-to-manage-external-rest-api" >}})
- [Graceful cleanup of workloads in a Kubernetes cluster]({{< relref "/registry/packages/command#graceful-cleanup-of-workloads-in-a-kubernetes-cluster" >}})

Learn more in the [Command package GitHub issue](https://github.com/pulumi/pulumi/issues/99)

### Support `pulumi import` for Kubernetes CRDs

We have added `pulumi import` support for Kubernetes CustomResourceDefiniton (CRD). Now the spec of a CRD will be imported during `pulumi import`. The same fix improves input generation for other Kubernetes resources as well, providing significantly better fidelity in covering inputs for existing resources.

[Learn more in this GitHub issue](https://github.com/pulumi/pulumi-kubernetes/issues/1410).

### Various improvements to Helm `Release`

This milestone we spent some time making improvements to the Helm `Release` support. Of particular note are the ability to import existing Helm releases installed via the Helm command line into Pulumi and the ability to supply Helm values through YAML files. In addition, we have made a variety of bug fixes this iteration to make Helm Release a more robust option to use for your Kubernetes environment.

Learn more in these GitHub issues:
- [Fix import handling for Helm `Release`](https://github.com/pulumi/pulumi-kubernetes/pull/1818)
- [Add support for using values from YAML files](https://github.com/pulumi/pulumi-kubernetes/pull/1828)

## Pulumi CLI and core technologies

### Support using native ES modules as Pulumi scripts

Native ECMAScript module (ESM) support has been added for the Node.js SDK. Pulumi users can now use Pulumi in projects with "type": "module" configured. In addition, we can now support top-level `await` in Node.js within Pulumi programs.

Learn more in these GitHub issue:
- [Support native ES module for Node.js SDK](https://github.com/pulumi/pulumi/issues/7764)
- [Support top-level `await` in Node.js](https://github.com/pulumi/pulumi/issues/5161)

### Support packages with plugins hosted in any third-party location

Pulumi Packages can now host their plugins anywhere (like GitHub releases) instead of needing to be published by Pulumi. We now detect any dependency that contains pulumi-plugin.json and treat it as a Pulumi Package, automatically downloading associated plugins as needed. To support this, the freshly generated Multi-Language Component (MLC) plugin will now include `pulumi-plugin.json` by default.

Learn more in the following GitHub issues:
- [Check for `pulumiplugin.json` on package lookup](https://github.com/pulumi/pulumi/issues/8515)
- [Check for `pulumiplugin.json` in `GetRequiredPlugins`](https://github.com/pulumi/pulumi/issues/8516)
- [Check for `pulumiplugin.json` in package lookup](https://github.com/pulumi/pulumi/issues/8517)
- [Emit `pulumiplugin.json` as part of codegen](https://github.com/pulumi/pulumi/issues/8530)
- [Emit `pulumiplugin.json` by default](https://github.com/pulumi/pulumi/issues/8527)
- [Emit `pulumiplugin.json` during codegen](https://github.com/pulumi/pulumi/issues/8532)

### State locking default enabled

We [previously added](https://github.com/pulumi/pulumi/pull/2697) support for self-managed backend state locking behind the  PULUMI_SELF_MANAGED_STATE_LOCKING=1 flag. After positive feedback from users on this feature, we are making this the default when using a local or cloud backend such as Amazon S3, Google Cloud Storage and Azure Blob Storage.

[Learn more in this GitHub issue](https://github.com/pulumi/pulumi/issues/8565).

## Pulumi Service & Pulumi.com

### Audit logging for third-party secrets managers

Previously secret decryption [Audit Log]({{< relref "/docs/intro/pulumi-service/audit-logs" >}}) events were only logged for users using the Pulumi Service secrets provider. Now users who use the Pulumi Service for their state but a third-party secrets provider (AWS KMS, Azure KeyVault, HashiCorp Vault, etc.) will have a log of these events.

[Learn more in this GitHub issue](https://github.com/pulumi/pulumi/issues/8563).
