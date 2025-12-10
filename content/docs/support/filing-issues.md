---
title: Filing GitHub Issues
title_tag: "Filing GitHub Issues with Pulumi"
meta_desc: Learn how to file bugs and feature requests in the correct Pulumi repository for faster resolution.
h1: Filing GitHub Issues
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    support:
        name: Filing Issues
        parent: support-home
        weight: 5
        identifier: support-filing-issues
---

When you encounter a bug or have a feature request, filing it in the correct GitHub repository helps our team respond faster and more effectively. Use this guide to determine where to file your issue.

## Quick decision guide

Follow this decision tree to find the right repository:

1. **Is this about documentation?** → [pulumi/docs](https://github.com/pulumi/docs/issues)
1. **Is this about a Registry example?** → The corresponding provider repository (see below)
1. **Is this about a cloud provider or resource?** → The corresponding provider repository (see below)
1. **Everything else** → [pulumi/pulumi](https://github.com/pulumi/pulumi/issues)

## Documentation issues

If you've found an error, typo, or missing information in the Pulumi documentation website, please file an issue in the [pulumi/docs repository](https://github.com/pulumi/docs/issues).

**Examples:**

- Broken links in documentation
- Outdated code samples in guides
- Missing or unclear explanations
- Typos or grammatical errors

## Registry example issues

This is a common source of confusion: Registry examples are maintained in provider repositories, not the main Pulumi repository.

If you find a bug in a Registry example (like example code that doesn't work or is outdated), file the issue in the **provider repository** for that cloud provider or service.

**Examples:**

- Bug in an AWS Registry example → [pulumi/pulumi-aws](https://github.com/pulumi/pulumi-aws/issues)
- Bug in an Azure Registry example → [pulumi/pulumi-azure-native](https://github.com/pulumi/pulumi-azure-native/issues)
- Bug in a Kubernetes Registry example → [pulumi/pulumi-kubernetes](https://github.com/pulumi/pulumi-kubernetes/issues)

{{% notes type="tip" %}}
On any Registry page, you can find a link to the provider's repository in the "Repository" section.
{{% /notes %}}

## Provider and resource issues

If you're experiencing issues with a specific cloud provider or resource (errors, missing features, unexpected behavior), file the issue in that provider's repository.

### Major provider repositories

- **AWS** → [pulumi/pulumi-aws](https://github.com/pulumi/pulumi-aws/issues) or [pulumi/pulumi-aws-native](https://github.com/pulumi/pulumi-aws-native/issues)
- **Azure** → [pulumi/pulumi-azure-native](https://github.com/pulumi/pulumi-azure-native/issues) or [pulumi/pulumi-azure](https://github.com/pulumi/pulumi-azure/issues)
- **Google Cloud** → [pulumi/pulumi-gcp](https://github.com/pulumi/pulumi-gcp/issues) or [pulumi/pulumi-google-native](https://github.com/pulumi/pulumi-google-native/issues)
- **Kubernetes** → [pulumi/pulumi-kubernetes](https://github.com/pulumi/pulumi-kubernetes/issues)

### Finding other provider repositories

For other providers, visit the [Pulumi Registry](https://www.pulumi.com/registry/), search for your provider, and click through to its repository.

## Core Pulumi issues

File issues in the main [pulumi/pulumi repository](https://github.com/pulumi/pulumi/issues) for:

- Pulumi CLI bugs or feature requests
- Pulumi engine issues
- State management problems (not specific to a provider)
- Language SDK issues (TypeScript, Python, Go, .NET, Java)
- Issues with `pulumi new`, `pulumi up`, `pulumi preview`, etc.
- Pulumi Cloud-related issues (though you can also [contact support](/contact/))

**Examples:**

- The `pulumi up` command crashes
- State file becomes corrupted
- Problems with stack references
- Issues with secrets encryption
- Language-specific SDK bugs

## Still not sure?

If you're unsure where to file your issue:

1. Start with [pulumi/pulumi](https://github.com/pulumi/pulumi/issues) - the team can redirect you if needed
1. Join the [Pulumi Community Slack](https://slack.pulumi.com/) and ask in the #general channel
1. [Contact support](/contact/) if you're on a paid plan

## Before you file

To help us resolve your issue quickly:

1. **Search existing issues** - your issue might already be reported
1. **Include version information** - run `pulumi version` and include the output
1. **Provide reproduction steps** - minimal code examples are extremely helpful
1. **Enable verbose logging** - see our [logging guide](/docs/support/debugging/logging/) for instructions
1. **Redact sensitive information** - remove credentials, tokens, and secrets from logs

{{% notes type="warning" %}}
Be careful when sharing logs - they may contain sensitive information like credentials or tokens. Always review and redact logs before posting them publicly.
{{% /notes %}}
