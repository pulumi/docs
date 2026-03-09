---
title_tag: Converters
meta_desc: Learn about Pulumi converters, which translate IaC written in other tools into Pulumi programs in any supported language.
title: Converters
h1: Converters
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Converters
        parent: iac-concepts
        weight: 150
---

Converters are [plugins](/docs/iac/concepts/plugins/) that deterministically translate infrastructure as code written in other tools into Pulumi programs in any [supported Pulumi language](/docs/languages-sdks/).

{{% notes type="info" %}}
For most conversions, using an LLM is the recommended first option. [Pulumi Neo](/docs/ai/), part of Pulumi Cloud, can convert your infrastructure code using AI. For Terraform specifically, Neo has a [specialized migration skill](/docs/ai/skills/).
{{% /notes %}}

## Supported converters

| Converter | `--from` value | Description |
|-----------|---------------|-------------|
| Terraform | `terraform` | Converts Terraform HCL to Pulumi |
| Azure Resource Manager (ARM) | `arm` | Converts ARM JSON templates to Pulumi |
| Azure Bicep | `bicep` | Converts Bicep templates to Pulumi |
| Kubernetes | `kubernetes` | Converts Kubernetes YAML manifests to Pulumi |

## Using a converter

Run `pulumi convert` with the `--from` flag to specify the converter and `--language` to specify the target Pulumi language:

```bash
pulumi convert --from terraform --language typescript
```

Converters are installed automatically when you run `pulumi convert`. For detailed usage and options, see the [`pulumi convert` CLI reference](/docs/iac/cli/commands/pulumi_convert/).

For step-by-step migration guides for each source tool, see [Migrating to Pulumi](/docs/iac/guides/migration/).

## Manual installation

Converter plugins are installed automatically, but you can also install them manually using `pulumi plugin install`:

```bash
pulumi plugin install converter terraform
pulumi plugin install converter arm
pulumi plugin install converter bicep
pulumi plugin install converter kubernetes
```

Manual installation is useful for pre-loading plugins in CI/CD pipelines or air-gapped environments. See [plugin installation](/docs/iac/concepts/plugins/#manual-installation) for more details.
