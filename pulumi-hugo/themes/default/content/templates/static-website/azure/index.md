---
title: Azure Static Website
meta_desc: The Azure Static Website template makes it easy to deploy a static website on Azure with Pulumi, Azure Blob Storage, and Azure CDN.
meta_image: meta.png
card_desc: Deploy a static website on Azure with Pulumi, Azure Blob Storage, and Azure CDN.
layout: template
template:
    prefix: static-website-azure
cloud:
    name: Microsoft Azure
    slug: azure
draft: true
---

The Azure Static Website template deploys an HTML website on Microsoft Azure.

![An architecture diagram of the Pulumi Azure Static Website template](./architecture.png)

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-azure-typescript
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-azure-python
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-azure-go
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-azure-csharp
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-azure-yaml
```

{{% /choosable %}}
