---
title: "Converting Full Terraform States to Pulumi"
date: 2023-10-25
meta_desc: Learn how to convert whole Terraform states to Pulumi using the new Terraform converter
meta_image: meta.png
authors:
    - fraser-waters
tags:
    - migration
---

Building on our work of [converting Terraform projects](/blog/converting-full-terraform-programs-to-pulumi/), we now have support for adopting resources from Terraform state.

<!--more-->

In the prior blog post about converting from Terraform we called out that while it was great that the converter could migrate a Terraform project, but what if you had existing infrastructure resources.

Historically we've shared some AWS specific code for [TypeScript](https://github.com/pulumi/tf2pulumi/blob/master/misc/import/import.ts) and [Go](https://github.com/pulumi/tf2pulumi/blob/master/misc/import-go/import.go) to import from `.tfstate` files. These have been useful, but they're limited to the AWS provider and either Go or TypeScript programs.

From [v3.87.0](/docs/install) we have extended our converter system to also include state in addition to code. So now it's possible to import resources from other state systems, the first of which is Terraform.

## Converting a Real World Workspace

Terraform stores its state in workspaces. In the most simple case this is just a `terraform.tfstate` file in the directory with the code. For remote state it can be fetched with [terraform state pull](https://developer.hashicorp.com/terraform/cli/commands/state/pull).

Given a `terraform.tfstate` file we can set up a Pulumi stack and tell it to import the resource from Terraform.

```bash
$ pulumi stack init
$ pulumi import --from terraform ./terraform.tfstate
```

Pulumi will try to convert the resources in the Terraform state into their matching Pulumi types and import strings (normally just the resource ID).

Some resources don't use their ID as the import string. For some well known AWS resources the converter will handle this; for others, they might still cause an error at import time. However, if the import does fail (for any reason) the import file listing all the resources will be written out to the current directory, allowing you the opportunity to manually fix up issues with type tokens or import strings, and then try again using `pulumi import --file`.

We're working on ensuring more types correctly translate, so feel free to open issues with any import errors you get while using this new converter to help us improve.

## Get Started

Support for the new `pulumi import --from terraform` command is now available in v3.87.0 of the Pulumi CLI. [Download](/docs/install/) the latest Pulumi CLI and give the new converter a try today. If you run into any issues, please [let us know](https://github.com/pulumi/pulumi/issues/new/choose) or reach out in the [Pulumi Community Slack](https://slack.pulumi.com) with any questions!
