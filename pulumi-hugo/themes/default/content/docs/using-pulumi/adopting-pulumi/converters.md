---
title_tag: "Convert Code to Pulumi"
meta_desc: Pulumi convert allows you to convert ARM, CloudFormation, Kubernetes CustomResources, Kubernetes YAML, and Terraform to Pulumi.
title: Convert code
h1: Convert code to Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  usingpulumi:
    identifier: converters
    parent: adopting-pulumi
    weight: 4
aliases:
- /docs/converters/
---

The `pulumi convert` command allows you translate supported sources to the various [languages that Pulumi supports]((/docs/languages-sdks/), such as TypeScript, JavaScript, Go, Python, C#, or Java.). Conversion sources are supported via a plugin model, and include other IaC tools like Terraform. Pulumi YAML programs can also be converted to any other supported Pulumi language.

For the detailed usage of this command and options, refer to the [pulumi convert CLI documentation.](https://www.pulumi.com/docs/cli/commands/pulumi_convert/)

### Supported source languages

* [YAML](/docs/languages-sdks/yaml/)
* [Terraform](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-terraform/)
* [Kubernetes](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-kubernetes/)
* [ARM](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-azure)
* [Bicep](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-azure)

### Supported destination languages

* [TypeScript/Javascript](/docs/languages-sdks/javascript/)
* [Go](/docs/languages-sdks/go/)
* [Python](/docs/languages-sdks/python/)
* [C#](/docs/languages-sdks/dotnet/)
* [Java](/docs/languages-sdks/java/)

### Use cases for using pulumi convert

The `pulumi convert` subcommand is designed to address a variety of migration and conversion scenarios where IaC practices evolve alongside your project needs. Here are some common use cases:

* **Migrating from other IaC tools:** If you're looking to transition your infrastructure definitions from tools like Terraform, Bicep, or ARM templates into Pulumi.
* **Converting from Pulumi YAML:** If you started your project with Pulumi YAML and find your requirements have evolved, you can convert and take advantage of the benefits offered by popular programming languages, such as complex logic capabilities and the flexibility to create modular and reusable components.

### Additional conversion tools and resources

The following list of web-based tools and resources can quickly help you convert your source IaC languages or formats for use with the `pulumi convert --from` command. The resulting file can be copied or downloaded for use with a [new Pulumi project](/docs/get-started/).

* [Terraform to Pulumi](/tf2pulumi/)
* [ARM to Pulumi](/arm2pulumi)
* [Kubernetes CustomResources to Pulumi](/blog/introducing-crd2pulumi/)
* [CloudFormation to Pulumi](/cf2pulumi/)
* [Kubernetes YAML to Pulumi](/kube2pulumi/)
