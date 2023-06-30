---
title: "Converting Full Terraform Programs to Pulumi"
date: 2023-06-12
meta_desc: Learn how to convert whole Terraform programs to Pulumi using the new Terraform converter
meta_image: meta.png
authors:
    - justin-vanpatten
tags:
    - migration
---

Over the last 2 years, we've seen an increasing trend of cloud development teams migrating to Pulumi from Terraform. These teams often have experience with and meaningful investment in Terraform, but have also typically run into limits of expressivity, productivity, scalability, or reliability with their existing tools. One of the first questions we hear when they decide to move to Pulumi is "how will I migrate my existing Terraform projects over?".

Today, we're excited to announce new support for converting whole Terraform projects to Pulumi via the `pulumi convert` command in the Pulumi CLI. The new Terraform converter includes support for Terraform modules, core features of Terraform 1.4, and the majority of Terraform built-in functions, converting to Pulumi TypeScript, Python, Go, or C#. The new converter can significantly reduce the amount of time it takes to migrate Terraform to Pulumi. Let's dig in to learn more about the new converter and how to use it.

<!--more-->

Historically, we have offered a separate [tf2pulumi](https://github.com/pulumi/tf2pulumi) tool to convert small snippets of Terraform to Pulumi. The new converter is no longer a separate tool. As of [v3.71.0](/docs/install/), you can run the new converter directly from the Pulumi CLI with the `pulumi convert --from terraform` command. And you can convert more than small snippets -- the new converter supports converting full Terraform programs.

The new support in `pulumi convert` builds upon Pulumi's [CrossCode](/crosscode/) foundations for providing universal infrastructure as code support across a wide variety of programming languages and conversion tooling between them. It also introduces a new concept of `converter` plugin in the Pulumi engine, which allows conversion tools from other Infrastructure as Code platforms to be integrated into the same `pulumi convert` experience in the future, both as part of the core project, as well as by other ecosystem partners and contributors.

Several common use cases are supported via the new `pulumi convert --from terraform` support in the Pulumi CLI:

* Converting your organization's existing Terraform projects to Pulumi
* Converting your organization's existing Terraform modules to Pulumi, to be consumed as part of existing Pulumi projects
* Converting 3rd party open source Terraform modules or projects which address a use case you want to incorporate into your existing Pulumi projects

<iframe width="560" height="315" src="https://www.youtube.com/embed/1MAhhNE9a3Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## Supported Terraform Features

The following major features are supported:

* Variables, outputs, resources, and data sources
* Terraform modules are converted to Pulumi components
* Almost all HCL2 expression syntax

In cases where the converter does not yet support a feature, the `pulumi convert` command succeeds but generates a TODO in the form of a call to a <pulumi-chooser type="language" options="typescript,python,go,csharp" option-style="none" class="inline">
    <pulumi-choosable type="language" value="typescript"><code>notImplemented</code></pulumi-choosable>
    <pulumi-choosable type="language" value="python"><code>not_implemented</code></pulumi-choosable>
    <pulumi-choosable type="language" value="go"><code>notImplemented</code></pulumi-choosable>
    <pulumi-choosable type="language" value="csharp"><code>NotImplemented</code></pulumi-choosable>
</pulumi-chooser> function that will need to be filled in manually. For most projects, the converter should be able to convert 90-95% of the code without any TODOs, with only a small percentage of items to address manually, significantly reducing migration time compared to doing an entire migration by hand. We are actively improving the converter by adding support for missing features and improving the overall quality of the converted code to reduce the amount of manual fix-ups required.

## Converting a Real World Program

Let's walk through converting a Terraform codebase to Pulumi. [Avant Terraform Vault Setup](https://github.com/avantoss/vault-infra) is an open source project that provides a high-availability installation of Vault using a variety of managed AWS services. It defines a fairly complex installation with dozens of AWS resources in over 1,000 lines of Terraform HCL, including the main program and a Vault module. Let's convert it to Pulumi.

First, clone the repo and `cd` into the directory containing the Terraform project:

```bash
$ git clone https://github.com/avantoss/vault-infra.git
$ cd vault-infra/terraform/main
```

Next, run the converter:

{{< chooser language "typescript,python,go,csharp" >}}
{{% choosable language typescript %}}

```bash
$ pulumi convert --from terraform --language typescript --out pulumi
```

{{% /choosable %}}
{{% choosable language python %}}

```bash
$ pulumi convert --from terraform --language python --out pulumi
```

{{% /choosable %}}
{{% choosable language go %}}

```bash
$ pulumi convert --from terraform --language go --out pulumi
```

{{% /choosable %}}
{{% choosable language csharp %}}

```bash
$ pulumi convert --from terraform --language csharp --out pulumi
```

{{% /choosable %}}
{{< /chooser >}}

![pulumi convert](pulumi-convert-from-terraform.gif)

The converted code is generated in the specified `pulumi` output directory. A complete Pulumi project is generated, including two primary code files specific to this this program's conversion:

* {{< langfile >}} contains the converted code for the main program
* <pulumi-chooser type="language" options="typescript,python,go,csharp" option-style="none" class="inline">
    <pulumi-choosable type="language" value="typescript"><code>vault.ts</code></pulumi-choosable>
    <pulumi-choosable type="language" value="python"><code>vault.py</code></pulumi-choosable>
    <pulumi-choosable type="language" value="go"><code>vault.go</code></pulumi-choosable>
    <pulumi-choosable type="language" value="csharp"><code>vault.cs</code></pulumi-choosable>
  </pulumi-chooser> contains the <code>Vault</code> Pulumi component, converted from the Terraform module

### Addressing TODOs

The file for the `Vault` component makes up the bulk of the implementation and contains some TODOs emitted by the converter that must be addressed manually.

For example, the converter doesn't yet support the `replace`, `element`, and `split` built-in functions.

{{< chooser language "typescript,python,go,csharp" >}}
{{% choosable language typescript %}}

```typescript
const plainDomain = notImplemented("replace(element(split(\":\",var.vault_dns_address),1),\"////\",\"\")");
```

{{% /choosable %}}
{{% choosable language python %}}

```python
plain_domain = not_implemented("replace(element(split(\":\",var.vault_dns_address),1),\"////\",\"\")")
```

{{% /choosable %}}
{{% choosable language go %}}

```go
plainDomain := notImplemented("replace(element(split(\":\",var.vault_dns_address),1),\"////\",\"\")");
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var plainDomain = NotImplemented("replace(element(split(\":\",var.vault_dns_address),1),\"////\",\"\")");
```

{{% /choosable %}}
{{< /chooser >}}

We can fill in an implementation. Note that we get to use the full expressiveness of the native and familiar string manipulation libraries in our target programming language, instead of the relatively constrained options of the Terraform DSL.

{{< chooser language "typescript,python,go,csharp" >}}
{{% choosable language typescript %}}

```typescript
const plainDomain = pulumi.output(args.vaultDnsAddress)
    .apply(a => a.split(":")[1].replace("//", ""));
```

{{% /choosable %}}
{{% choosable language python %}}

```python
plain_domain = pulumi.Output.from_input(args["vaultDnsAddress"]) \
    .apply(lambda a: a.split(":")[1].replace("//", ""))
```

{{% /choosable %}}
{{% choosable language go %}}

```go
plainDomain := args.VaultDnsAddress.ToStringOutput().ApplyT(func(a string) string {
	return strings.ReplaceAll(strings.Split(a, ":")[1], "//", "")
}).(pulumi.StringOutput)
```

{{% /choosable %}}
{{% choosable language csharp %}}

```csharp
var plainDomain = args.VaultDnsAddress
    .Apply(a => a.Split(':')[1].Replace("//", ""));
```

{{% /choosable %}}
{{< /chooser >}}

### Wrapping Up

After addressing the remaining TODOs and some other tweaks so that the code compiles, we can now run the converted program with `pulumi up` to provision the Vault installation with Pulumi.

The converter has saved us a ton of time, converting over 1,000 lines of Terraform to a modern Pulumi language, with only a small number of manual fix-ups required. From here, we can leverage our IDE and compiler to further refactor and improve the code, one of the many benefits of Pulumi!

## Importing State

It's great that the new converter can migrate Terraform projects to Pulumi for new deployments, but what if you want to import existing resource states from a `.tfstate` file to avoid unnecessarily recreating your infrastructure?

If you're using TypeScript or Go, there is some additional code that can be added to your converted Pulumi program to import resource states from a `.tfstate` file. See the [Importing Resources](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-terraform/#importing-resources) reference documentation for more details.

We're working to make this even more seamless with built-in support for importing state from `.tfstate` files in a future update coming soon.

## Get Started

Support for the new `pulumi convert --from terraform` command is now available in v3.71.0 of the Pulumi CLI. [Download](/docs/install/) the latest Pulumi CLI and give the new converter a try today. If you run into any issues, please [let us know](https://github.com/pulumi/pulumi/issues/new/choose) or reach out in the [Pulumi Community Slack](https://slack.pulumi.com) with any questions!
