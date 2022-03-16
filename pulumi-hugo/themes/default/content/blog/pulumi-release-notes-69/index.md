---
title: "Pulumi Release Notes: Pulumi Import Improvements, RetainOnDelete as a resource option, and more!"
allow_long_title: true

# The date represents the post's publish date, and by default corresponds with
# the date this file was generated. Posts with future dates are visible in development,
# but excluded from production builds. Use the time and timezone-offset portions of
# of this value to schedule posts for publishing later.
date: 2022-03-15T08:47:42-08:00

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or social-media
# previews. This field is required or the build will fail the linter test.
meta_desc: The latest Pulumi updates also include the new `pulumi state rename` command, changing the default `pulumi plugin install` to the latest version, adding console output in non-interactive mode, and `pulumi cancel` support for self-managed state backends.

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

---

The team has been busy releasing new features and improvements in the last 3 weeks. Read on to learn about what's new in this release!

- Pulumi CLI and core technologies
  - [`pulumi import` Improvements](#pulumi-import-improvements)
  - [Add `RetainOnDelete` as a resource option](#add-retainondelete-as-a-resource-option)
  - [New `pulumi state rename` command](#new-pulumi-state-rename-command)
  - [Default `pulumi plugin install` to the latest version](#default-pulumi-plugin-install-to-the-latest-version)
  - [Add console output in non-interactive mode](#add-console-output-in-non-interactive-mode)
  - [Support `pulumi cancel` for filestate backends](#support-pulumi-cancel-for-filestate-backends)

<!--more-->


## Pulumi CLI and core technologies

### `pulumi import` Improvements

Last year, we introduced a new Pulumi import feature that allows you to import existing infrastructure into your Pulumi program. We’ve listened to feedback and delivered a plethora of updates and fixes to streamline the import experience to make it more useful, more convenient, and more powerful. Not only can this feature bring a resource into your Pulumi state file, but it can also generate the source code for your Pulumi program too. 

You can now use the `pulumi import` command to import using all input fields instead of only the ones flagged as required, which will result in less check failures. If there are check failures, they are now treated as a warning not an error. In addition, we added an optional flag to `pulumi import` that allows users to skip the code generation step of import.

Learn more in the [Improved Import blog post]({{< relref "/blog/changes-to-import" >}}), [import improvements GitHub issue](https://github.com/pulumi/pulumi/issues/9134) and the [disable codegen GitHub issue](https://github.com/pulumi/pulumi/issues/9134). 


### Add `RetainOnDelete` as a resource option

Pulumi is frequently used to manage the entire lifecycle of a resource, from creation, to updates, to replacement, to deletion. However, there are some cases where it is important to ensure that a resource’s life can extend beyond the lifetime of the Pulumi program that created it. To support these use cases, Pulumi now supports a new resource option [`RetainOnDelete`]({{< relref "/docs/intro/concepts/resources/options/retainondelete" >}}) which allows a resource to be retained in a cloud provider even after it is deleted from the Pulumi stack it is part of.

Learn more in the [RetainOnDelete blog post]({{< relref "/blog/retainondelete" >}}) and in the [RetainOnDelete GitHub issue](https://github.com/pulumi/pulumi/issues/7747).


### New `pulumi state rename` command

In some cases users may need to rename existing resources, which historically has been done by editing the checkpoint file directly. We’ve now made this even easier by offering a CLI command to rename resources. You can now use [`pulumi state rename`]({{< relref "/docs/reference/cli/pulumi_state_rename" >}}) to rename resources in an easy and safe manner. This feature will also be useful for customers migrating to the Azure AD provider without replacing resources. 

Learn more in the [add `pulumi state` GitHub issue](https://github.com/pulumi/pulumi/issues/2060).

### Default `pulumi plugin install` to the latest version

When using `pulumi plugin install`, the version argument is now optional and will default to the latest version when a version argument is not provided. This will save users time when they want to use the latest plugin version as they no longer need to look it up. 

Learn more in the [latest plugin version GitHub issue](https://github.com/pulumi/pulumi/issues/9001).

### Add console output in non-interactive mode

When resources are slow to create, Pulumi will now have a dot spinner in non-interactive mode. When running Pulumi in a hosted CI environment (such as CircleCI) if there is no console output while waiting for resources to create the CI tool may forcibly terminate the job. We have added a parameter to set a delay for a heartbeat message in non-interactive mode to keep the CI tool from killing jobs. 

Learn more in the [console output non-interactive mode GitHub issue](https://github.com/pulumi/pulumi/issues/6574).

### Support `pulumi cancel` for filestate backends

We now support `pulumi cancel` for self-managed state backends, such as S3. 

Learn more in the [support `pulumi cancel` GitHub issue](https://github.com/pulumi/pulumi/issues/4605).