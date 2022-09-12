---
title: Google Cloud Static Website
meta_desc: The Google Cloud Static Website template makes it easy to deploy a static website on Google Cloud with Pulumi, Google Cloud Storage, and Google Cloud CDN.
meta_image: meta.png
card_desc: Deploy a static website on Google Cloud with Pulumi, Google Cloud Storage, and Google Cloud CDN.
layout: template
template:
    prefix: static-website-google-cloud
cloud:
    name: Google Cloud Platform
    slug: gcp
draft: true
---

The Google Cloud Static Website template deploys an HTML website on Google Cloud Platform.

![An architecture diagram of the Pulumi Google Cloud Static Website template](./architecture.png)

{{% chooser language "typescript,python,go,csharp,yaml" / %}}

{{% choosable language typescript %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-gcp-typescript
```

{{% /choosable %}}

{{% choosable language python %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-gcp-python
```

{{% /choosable %}}

{{% choosable language go %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-gcp-go
```

{{% /choosable %}}

{{% choosable language csharp %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-gcp-csharp
```

{{% /choosable %}}

{{% choosable language yaml %}}

```bash
$ mkdir my-site && cd my-site
$ pulumi new static-website-gcp-yaml
```

{{% /choosable %}}
