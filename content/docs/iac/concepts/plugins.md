---
title_tag: Plugins
meta_desc: Learn about Pulumi plugins, the core extensibility mechanism that enables Pulumi to work with cloud providers, languages, and tools.
title: Plugins
h1: Plugins
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Plugins
        parent: iac-concepts
        weight: 140
    concepts:
        weight: 140
---

{{% notes type="info" %}}
Most Pulumi users don't need to understand plugins in depth, as most plugin installation and management happens automatically.

If you're interested in learning more about Pulumi internals, see the [Pulumi Developer Documentation](https://pulumi-developer-docs.readthedocs.io/latest/docs/architecture/plugins.html).
{{% /notes %}}

Plugins are Pulumi's core extensibility mechanism, allowing the Pulumi engine to communicate in a uniform manner with various languages, resource providers, and other tools. Plugins always run as separate processes and mostly use gRPC for communication with the Pulumi engine.

## Plugin types

Pulumi supports five categories of plugins:

### Resource plugins

Resource plugins (also known as [providers](/docs/iac/concepts/resources/providers/)) expose standardized interfaces for managing cloud resources. Resource plugins are distributed as [Pulumi packages](/docs/iac/concepts/packages/). A listing of providers is available in the [Pulumi Registry](/registry/).

In addition to the packages in the Pulumi Registry, you can write your own [components](/docs/iac/concepts/resources/components/) and distribute them as resource plugins, enabling consumption in any Pulumi language. Components can be published to [Pulumi IDP](/docs/idp/) for discoverability within your organization or shared directly via Git references.

When you first run `pulumi preview` or `pulumi up`, the Pulumi CLI will install any required providers that are not already in your plugin cache.

### Language plugins

Language plugins (also known as language hosts) host programs written in specific languages, enabling the Pulumi engine to execute your Pulumi code without understanding language-specific details. As described in [How Pulumi works](/docs/iac/concepts/how-pulumi-works/#language-hosts), language plugins consist of:

1. A language executor binary named `pulumi-language-<language-name>`, which Pulumi uses to launch the runtime for your program's language (e.g., Node.js or Python). This binary is distributed with the Pulumi CLI.
1. For all languages except YAML, a language SDK that prepares your program for execution and observes resource registrations.

Pulumi-supported language plugins are installed automatically with the Pulumi CLI. Community-supported language plugins can be installed separately.

### Analyzer plugins

Analyzer plugins scan Pulumi programs for potential issues and power [Pulumi Policy as Code](/docs/insights/policy/). These plugins enable you to enforce compliance, security, and best practices across your infrastructure.

Policy plugins are installed automatically with the Pulumi CLI.

### Converter plugins

Converter plugins transform existing infrastructure-as-code from other tools (like Terraform, Kubernetes YAML, or CloudFormation) into Pulumi programs. Learn more about [conversion tools](/docs/iac/guides/migration/converters/).

Converter plugins are installed automatically with the Pulumi CLI when you run the [`pulumi convert`](/docs/iac/cli/commands/pulumi_convert) command.

### Tool plugins

Tool plugins enable integration between Pulumi and external tools, extending Pulumi's capabilities to work with your existing workflows and toolchains.

## Plugin installation and management

### Automatic installation

The Pulumi CLI normally handles plugin installation automatically. For example:

- **Resource plugins** (provider binaries) are installed automatically when you first run `pulumi preview` or `pulumi up` if they are not already present in the plugin cache
- **Language plugins** are installed with the Pulumi CLI
- **Policy plugins** are installed with the Pulumi CLI
- The Pulumi CLI ensures your resource plugins are present when you run your Pulumi program

### Manual installation

Most users will not need to run the [`pulumi plugin install`](/docs/iac/cli/commands/pulumi_plugin_install/) command manually. However, manual plugin installation can be useful for scenarios like:

- Pre-loading plugins on a custom Docker image to speed up CI/CD pipelines
- Working in air-gapped environments
- Testing pre-release versions of plugins
- Installing plugins that are community-maintained

### Plugin storage

Plugins are stored in different locations depending on their type:

- All plugins that ship with the Pulumi CLI, including all of our supported **Language plugins** and **policy plugins** are stored in `~/.pulumi/bin`
- All plugins that are installed by the user, whether explicitly or automatically by the Pulumi CLI, are cached in `~/.pulumi/plugins`

### Plugin management commands

You can manage your local plugin cache using the following CLI commands:

- [`pulumi plugin ls`](/docs/iac/cli/commands/pulumi_plugin_ls/) - List installed plugins
- [`pulumi plugin rm`](/docs/iac/cli/commands/pulumi_plugin_rm/) - Remove cached plugins
- [`pulumi plugin install`](/docs/iac/cli/commands/pulumi_plugin_install/) - Manually install a plugin

## Plugin implementation details

Plugins are deployed through two approaches:

- **Executables** following the naming convention `pulumi-<kind>-<name>` (e.g., `pulumi-resource-aws`)
- **Directory-based plugins** containing a `PulumiPlugin.yaml` configuration file, where the engine uses the specified runtime to execute the plugin through the language plugin's interface

For more details about Pulumi plugin architecture and how to contribute to plugin development, see the [Pulumi Developer Documentation](https://pulumi-developer-docs.readthedocs.io/latest/docs/architecture/plugins.html).

## Related topics

- [Providers](/docs/iac/concepts/resources/providers/) - Learn more about resource plugins (providers)
- [How Pulumi works](/docs/iac/concepts/how-pulumi-works/) - Understand how plugins fit into Pulumi's architecture
- [Policy as Code](/docs/insights/policy/) - Learn about analyzer plugins for policy enforcement
- [Conversion tools](/docs/iac/guides/migration/converters/) - Use converter plugins to migrate from other IaC tools
