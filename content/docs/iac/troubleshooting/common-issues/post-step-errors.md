---
title_tag: "Resolving Post-Step Event Errors in Pulumi"
meta_desc: "Learn how to handle post-step event errors and determine if you've encountered a bug in Pulumi."
title: Post-step event errors
h1: Post-step event returned an error
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Post-Step Event Errors
        parent: iac-troubleshooting-common-issues
        weight: 30
---

If an I/O error occurs after "post-step event returned an error", you can safely re-start your update. If you see "after mutation of snapshot", you have hit a bug in Pulumi. You will possibly need to do some [manual intervention to repair your stack](/docs/iac/troubleshooting/editing-state-files/).

The Pulumi engine runs a small amount of code after every "step" that it performs. If this code fails for any reason, it will fail the entire update. One of the things that the Pulumi engine does before and after every step is a self-check on its internal data structures to ensure that they are in a consistent state. If they are not, Pulumi will issue an error and fail the deployment.

There are two reasons why this error could occur:

1. You experienced a network partition while performing an update.
2. The Pulumi engine failed its data structure self-check.

In each case, some more specific information is printed in addition to "post-step returned an error". In the first case, it is common for you to see an additional error indicating that some I/O operation has failed. This can be disregarded and it is safe to re-start the update. You may need to [recover from the interrupted update](/docs/iac/troubleshooting/common-issues/interrupted-updates/).

In the second case, you may see an additional error message "after mutation of snapshot". This error message is **always a bug in Pulumi**. If you see this error message, please open a [GitHub issue](https://github.com/pulumi/pulumi/issues). We also recommend joining our [Pulumi Community Slack](https://slack.pulumi.com/) and sharing your problem if you experience this error message.
