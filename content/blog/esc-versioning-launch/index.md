---
title: "Unveiling Pulumi ESC Versioning: Manage Secrets and Deployments with Confidence"
allow_long_title: true
date: 2024-06-05T00:00:00-03:00
draft: false
meta_desc: "The new ESC Versioning features allows you bring agile practices to your
  secrets and configuration management, and streamline deployments"
meta_image: "meta.png"
authors:
  - arun-loganathan
  - pat-gavlin
tags:
  - esc
  - secrets
  - features
search:
  keywords:
    - esc
    - confidence
    - deployments
    - versioning
    - unveiling
    - secrets
    - agile
---

Since the launch of [Pulumi Environments, Secrets and Configuration](/product/esc) (ESC), our developer-first configuration and secrets management platform, we've seen exponential growth in usage. Customers have used it to simplify their secrets and configuration management by organizing them into composable collections called 'environments'. Today, we are thrilled to introduce a comprehensive suite of versioning features, giving you unprecedented control and confidence in managing your environments.

<!--more-->

## Uncover the Key Features of Pulumi ESC Versioning

Pulumi ESC Versioning introduces a range of powerful features:

- **Immutable Revision History**: Every time you save an environment, a new, immutable revision is created, preserving a complete and tamper-proof history of your changes.
- **Compare Revisions Side-by-Side**: Gain a clear understanding of changes between revisions with our detailed side-by-side comparison view. This helps identify differences, troubleshoot issues, and ensure smooth transitions between versions.
- **Tag Revisions**: Assign meaningful names to specific revisions, enabling you to easily manage and deploy different versions of your environments. You can use tags like `production`, `v1.2.1`, `stable`, `pre-release`, and `in-development` to clearly communicate the purpose or stage of each version. Each environment has a built-in `latest` tag that always points to the environment’s most recent revision.
- **Import Specific Versions**: Precisely control which version of an environment is imported, either by specifying a tag (e.g., `environmentA@prod`) or using a specific revision number (e.g., `environmentB@2`). This method also applies when [importing environments](/docs/esc/environments/#importing-other-environments) via [Pulumi Stack Config](/docs/esc/environments/#using-environments-with-pulumi-iac) or via other environments, to effectively 'pin' the desired version. 
- **Rollback to a Specific Version**: Quickly revert your environment to a previous state by rolling back to a specific version or revision. This provides a safety net for deployments and makes it easy to undo unwanted changes.
- **Retract a Revision**: Quickly remove a revision from your history – crucial for situations like accidentally exposing a secret in plaintext.

## Level Up Your Workflow

Pulumi ESC Versioning delivers significant benefits that can transform your development process:

- **Disaster Prevention**: By pinning a version during import, you can test new configurations in isolation before applying them to critical production systems. This minimizes downtime, reduces risk, and ensures business continuity, boosting confidence in deployments and supporting agile practices.
- **Improved Auditing and Collaboration**: Easily track the complete history of your environments, including who made changes and when. This granular audit trail enhances security, ensures compliance, and promotes seamless collaboration within your team.
- **Streamlined Development Workflows**: Similar to Docker tags, Pulumi ESC version tags provide a familiar and intuitive way to categorize and utilize specific revisions to manage different stages of your environments.

{{% notes "info" %}}
Tags and specific version imports are available on the Enterprise and Business Critical editions of Pulumi Cloud. The Team Edition offers access to the latest 5 revisions.
{{% /notes %}}

## How to Get Started

Ready to start using versioning in Pulumi ESC? Here's how you can get started using the CLI or the Console:

### Using the CLI

Make sure you have the latest [ESC CLI](/docs/install/esc/) installed before you perform these steps. In your terminal, 

1. Run `esc env edit <environment-name>` to edit an environment
2. Run `esc env version history <environment-name>` to view all revision history
3. Run `esc env diff <environment-name>[@<version>] [[<environment-name>]@<version>]` to compare changes between versions
4. Run `esc env version tag <environment-name>@<tag>` to assign a tag to the latest revision
5.  Create a new environment using `esc env init <new-environment-name>` and import the previously edited environment using this syntax:
```yaml
imports:
- <environment-name>@<tag>
```
6. Run `esc open <new-environment-name>` to open and confirm that you have imported the right environment version

Check out the [ESC CLI documentation](/docs/esc-cli/) for more details on available options and commands.

### Using the Console

In your Pulumi Cloud Console,

1. Open an environment, make a change, and click `Save`
2. Go to the `Versions` Tab and select `Revision History` view to see the history of changes made to the environment
3. Click on a revision to see its details or view the differences between revisions using `compare revisions`
4. Add a tag to a revision by clicking on the Actions menu
5. Go to the `Tags` view and copy the reference to the tag
6. Create a new environment and import the tag

{{< video title="Pulumi ESC Versioning Demo" src="esc-versioning-demo.mp4" autoplay="true" loop="true" >}}

## Real-world Scenarios
Here are a few examples of how you might use these features:

- **Global Infrastructure Update**: You need to deploy a new configuration to a global service spanning multiple regions. Tag the updated configuration as `next` and deploy it to one region for testing. After verifying stability, you can confidently roll it out to other regions. If issues arise, quickly revert to the previous `stable` version, ensuring resilient and minimally disruptive deployments.
- **Platform Team Releases**: If you're a Platform team responsible for generating configurations, by tagging releases with labels like `v1.0-stable` and `v1.2-development`, you can clearly communicate which configurations are production-ready, keeping other teams informed about the ongoing development, and fostering seamless collaboration.
- **Code Review and Debugging**: You're working in a development environment where the latest revision includes multiple recent changes, and you notice that the application is experiencing performance issues. By using the Compare Revisions Side-by-Side feature or `esc env diff`, you can quickly identify the specific changes that might be causing the problem, enabling faster troubleshooting and resolution.

These examples are just a glimpse of how Pulumi ESC’s versioning capabilities can streamline your development and deployment process. The possibilities are vast, and you can tailor your tagging strategy to fit your specific needs and operational workflows.

## Conclusion

The versioning capabilities in Pulumi ESC mark a significant step towards a more developer-friendly and efficient platform for configuration and secrets management. These features provide a robust foundation for secure, reliable, and auditable deployments, whether you're rolling out infrastructure updates or ensuring compliance with industry regulations.

We're excited to see how you leverage these powerful capabilities. Your feedback is crucial in helping us shape the product to better serve your needs. We encourage you to open new issues on our [GitHub repository](https://github.com/pulumi/esc/issues/new/choose), upvote existing [ones](https://github.com/pulumi/esc/issues), or join the conversation on our [community Slack](https://slack.pulumi.com/) channel.

Check out the [ESC CLI](/docs/esc-cli/) and [Versioning](/docs/esc/environments/#versioning-environments) docs.
