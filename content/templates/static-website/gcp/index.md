---
title_tag: Deploy a Static Website to Google Cloud
title: Google Cloud Static Website
layout: template
schema_type: howto
meta_desc: Deploy a static website on Google Cloud with Pulumi, Cloud Storage, and Cloud CDN in TypeScript, Python, Go, C#, YAML, or HCL.
meta_image: meta.png
card_desc: Deploy a static website on Google Cloud with Pulumi, Cloud Storage, and Cloud CDN.
template:
  prefix: static-website-gcp
  dirname: my-site
  languages:
    - typescript
    - python
    - go
    - csharp
    - yaml
    - hcl
cloud:
    name: Google Cloud
    slug: gcp
---

The Google Cloud Static Website template scaffolds a Pulumi project that stores site files in a [Cloud Storage bucket](/registry/packages/gcp/api-docs/storage/bucket/) configured for static website hosting and serves them through Cloud CDN, fronted by a [Global Address](/registry/packages/gcp/api-docs/compute/globaladdress/) for low-latency delivery and caching. The template ships with placeholder web content so the project deploys end to end out of the box.

![An architecture diagram of the Google Cloud Static Website template](/templates/static-website/gcp/architecture.png)

## Using this template

To use this template to deploy a website of your own, make sure you've [installed Pulumi](/docs/install/) and [configured your Google Cloud credentials](/registry/packages/gcp/installation-configuration#credentials), then create a new [project](/docs/iac/concepts/projects/) using the template in the language of your choice:

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
: The provider-assigned hostname of the Google Cloud Storage bucket.

originURL
: The fully-qualified HTTP URL of the storage bucket endpoint.

cdnHostname
: The provider-assigned hostname of the Google Cloud CDN. Useful for creating `CNAME` records to associate custom domains.

cdnURL
: The fully-qualified HTTPS URL of the Google Cloud CDN.

{{% /choosable %}}

{{% choosable language hcl %}}

origin_url
: The fully-qualified HTTP URL of the storage bucket endpoint.

origin_hostname
: The provider-assigned hostname of the Google Cloud Storage bucket.

cdn_url
: The fully-qualified HTTPS URL of the Google Cloud CDN.

cdn_hostname
: The provider-assigned hostname of the Google Cloud CDN. Useful for creating `CNAME` records to associate custom domains.

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

path
: The path to the folder containing the files of the website. Defaults to `./www`, which is the relative path of the folder included with the template.

index_document
: The file to use for top-level pages. Defaults to `index.html`.

error_document
: The file to use for error pages. Defaults to `error.html`.

{{% /choosable %}}

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set):

### Using your own web content

If you already have a static website you'd like to deploy on Google Cloud with Pulumi, you can do so either by replacing placeholder content in the `www` folder or by configuring the stack to point to another folder on your computer with the `path` setting:

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
* Explore the [Google Cloud provider API docs](/registry/packages/gcp) in the Pulumi Registry.
* Walk through Pulumi from the ground up in [Pulumi Tutorials](/tutorials/).
* Read the latest [Google Cloud posts on the Pulumi blog](/blog/tag/google-cloud).
