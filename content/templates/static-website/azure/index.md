---
title_tag: Deploy a Static Website to Azure
title: Azure Static Website
layout: template
schema_type: howto
meta_desc: Deploy a static website on Azure with Pulumi, Azure Blob Storage, and Azure CDN in TypeScript, Python, Go, C#, YAML, or HCL.
meta_image: meta.png
card_desc: Deploy a static website on Azure with Pulumi, Azure Blob Storage, and Azure CDN.
template:
  prefix: static-website-azure
  dirname: my-site
  languages:
    - typescript
    - python
    - go
    - csharp
    - yaml
    - hcl
cloud:
    name: Microsoft Azure
    slug: azure
---

The Azure Static Website template scaffolds a Pulumi project that stores site files in an [Azure Blob Storage account](/registry/packages/azure-native/api-docs/storage/storageaccount/) configured for static website hosting and serves them through an [Azure CDN Endpoint](/registry/packages/azure-native/api-docs/cdn/endpoint/) for low-latency delivery, caching, and HTTPS. The template ships with placeholder web content so the project deploys end to end out of the box.

![An architecture diagram of the Azure Static Website template](/templates/static-website/azure/architecture.png)

## Using this template

To use this template to deploy a website of your own, make sure you've [installed Pulumi](/docs/install/) and [configured your Azure credentials](/registry/packages/azure-native/installation-configuration#credentials), then create a new [project](/docs/iac/concepts/projects/) using the template in the language of your choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a finished project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

The template requires no additional configuration. Once the new project is created, you can deploy it immediately with [`pulumi up`](/docs/iac/cli/commands/pulumi_up):

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output](/docs/iac/concepts/stacks/#outputs) values:

{{% choosable language "typescript,python,go,csharp,yaml" %}}

originHostname
: The provider-assigned hostname of the Azure Blob Storage container.

originURL
: The fully-qualified HTTP URL of the storage container endpoint.

cdnHostname
: The provider-assigned hostname of the Azure CDN. Useful for creating `CNAME` records to associate custom domains.

cdnURL
: The fully-qualified HTTPS URL of the Azure CDN.

{{% /choosable %}}

{{% choosable language hcl %}}

origin_url
: The fully-qualified HTTP URL of the storage container endpoint.

origin_hostname
: The provider-assigned hostname of the Azure Blob Storage container.

cdn_url
: The fully-qualified HTTPS URL of the Azure CDN.

cdn_hostname
: The provider-assigned hostname of the Azure CDN. Useful for creating `CNAME` records to associate custom domains.

{{% /choosable %}}

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources. The computed CDN URL, for example, can be used from the command line to open the newly deployed website in your favorite web browser:

{{% choosable language "typescript,python,go,csharp,yaml" %}}

```bash
$ open $(pulumi stack output cdnURL)
```

{{% /choosable %}}

{{% choosable language hcl %}}

```bash
$ open $(pulumi stack output cdn_url)
```

{{% /choosable %}}

## Customizing the project

Projects created with the Static Website template expose the following [configuration](/docs/iac/concepts/config/) settings:

{{% choosable language "typescript,python,go,csharp,yaml" %}}

path
: The path to the folder containing the files of the website. Defaults to `www`, which is the name (and relative path) of the folder included with the template.

indexDocument
: The file to use for top-level pages. Defaults to `index.html`.

errorDocument
: The file to use for error pages. Defaults to `error.html`.

{{% /choosable %}}

{{% choosable language hcl %}}

location
: The Azure region to deploy into. Defaults to `WestUS`.

path
: The path to the folder containing the files of the website. Defaults to `./www`, which is the name (and relative path) of the folder included with the template.

index_document
: The file to use for top-level pages. Defaults to `index.html`.

error_document
: The file to use for error pages. Defaults to `error.html`.

{{% /choosable %}}

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set):

### Using your own web content

If you already have a static website you'd like to deploy on Azure with Pulumi, you can do so either by replacing placeholder content in the `www` folder or by configuring the stack to point to another folder on your computer with the `path` setting:

```bash
$ pulumi config set path ../my-existing-website/build
$ pulumi up
```

## Cleaning up

You can cleanly destroy the stack and all of its infrastructure with [`pulumi destroy`](/docs/iac/cli/commands/pulumi_destroy):

```bash
$ pulumi destroy
```

## Learn more

* Browse other architecture templates in the [Templates gallery](/templates).
* Explore the [Azure Native provider API docs](/registry/packages/azure-native) in the Pulumi Registry.
* Walk through Pulumi from the ground up in [Pulumi Tutorials](/tutorials/).
* Read the latest [Azure posts on the Pulumi blog](/blog/tag/azure).
