---
title: "Introducing Auto-naming Configuration in Pulumi"
date: 2025-01-16T08:00:00-07:00
meta_desc: "Learn how to configure Pulumi's resource naming to match your organization's naming conventions and requirements across all cloud providers."
meta_image: meta.png
authors:
    - mikhail-shilkov
tags:
    - features
social:
    twitter: |
        🎉 New in Pulumi: Auto-naming Configuration!
        
        Take full control of your cloud resource names with:
        - Custom naming patterns
        - Verbatim mode
        - Disabled auto-naming option

        A highly requested feature that makes resource management even better.

        Read more ⬇️
    linkedin: >
        🚀 Excited to announce Pulumi's Auto-naming Configuration! 
        
        This highly anticipated feature gives you complete control over how your cloud resources are named across all cloud providers. Whether you want to disable auto-naming entirely, use logical names as-is, or create custom naming patterns that match your organization's conventions - we've got you covered.
        
        Key capabilities:
        - Custom naming patterns with static text, resource information, and random components
        - Verbatim mode for exact logical name matching
        - Option to disable auto-naming entirely
        - Support across all cloud providers
        
        Ready to try it out? Check out our latest blog post to learn more about this game-changing feature for infrastructure management.
---

I'm thrilled to announce the release of our auto-naming configuration feature. This highly anticipated capability addresses one of our most requested features [pulumi/pulumi#1518](https://github.com/pulumi/pulumi/issues/1518) and gives you complete control over how Pulumi names your cloud resources.

<!--more-->

## The Journey to Better Resource Naming

Since Pulumi's early days, auto-naming has been a core feature that ensures unique names for cloud resources by generating random name suffixes. While this approach solved many challenges around zero-downtime deployments and stack co-existence, we heard consistently from our community that you needed more control over how your resources are named.

The original [feature request](https://github.com/pulumi/pulumi/issues/1518) I opened in June 2018 has generated extensive discussion, with users sharing various use cases and requirements. Today, I'm happy to finally close that issue with a solution that addresses the community's needs while maintaining Pulumi's robust resource management capabilities.

## Introducing Auto-naming Configuration

With the new auto-naming configuration feature, you now have full control over how Pulumi generates resource names. Here are some common scenarios you can achieve:

### Disable Auto-naming

If you want complete control over your resource names, you can disable auto-naming entirely:

```yaml
pulumi:autonaming:
  mode: disabled
```

In this mode, Pulumi will require you to provide explicit physical names for all resources.

### Use Logical Names As-Is

For scenarios where you want Pulumi to copy exactly the logical names to become the physical names, you can use the `verbatim` mode:

```yaml
pulumi:autonaming:
  mode: verbatim
```

No random suffixes will be added to the resource names.

Note, when an update requires replacing the resource, Pulumi's default behavior is to create the new resource and then deleting the old resource. However, when using verbatim names or patterns without random components, resources that need to be replaced will be deleted before creating the new resource. This can lead to downtime.

### Custom Naming Patterns

Create your own naming patterns that combine static text, resource information, and random elements:

```yaml
pulumi:autonaming:
  pattern: ${project}-${stack}-${name}${alphanum(6)}
```

See the [auto-naming configuration documentation](/docs/concepts/resources/names/#autonaming-configuration) to see the full list of available expressions.

### Configuration Syntax

The configuration syntax differs slightly depending on where you define it:

In your project file `Pulumi.yaml`:

```yaml
config:
  pulumi:autonaming:
    value:
      mode: verbatim
```

In your stack configuration file `Pulumi.<stack-name>.yaml`:

```yaml
config:
  pulumi:autonaming:
    mode: verbatim
```

The same applies to other configuration patterns shown above - use the `value:` key in project-level configuration, but omit it in stack-level configuration.

## Getting Started

To use the auto-naming configuration feature, you'll need:

1. Pulumi CLI 3.146.0 or later
2. The following minimum provider versions:
   - AWS provider 6.66.0 or later
   - Azure Native provider 2.78.0 or later
   - Azure Classic provider 6.14.0 or later
   - Google Cloud Platform provider 8.11.0 or later
   - AWS Cloud Control provider 1.21.0 or later

Once you have the required versions installed, simply add your desired auto-naming configuration to your Pulumi configuration file.

For complete documentation and advanced usage scenarios, visit our [auto-naming configuration documentation](/docs/intro/concepts/resources/names/#auto-naming-configuration).

## General Availability

We're excited to announce that the auto-naming configuration feature is now generally available across our major cloud providers. This release marks an important milestone in Pulumi's evolution, delivering a robust and flexible solution for resource naming that our community has been asking for.

Thank you to everyone who participated in the [RFC discussion](https://github.com/pulumi/pulumi/discussions/17592) and preview period and provided valuable feedback. Your input has been invaluable in creating a solution that works for diverse use cases while maintaining Pulumi's core strengths.

If you have any questions or feedback about the auto-naming configuration feature, please don't hesitate to reach out to us on GitHub or in the [Pulumi Community Slack](https://slack.pulumi.com).
