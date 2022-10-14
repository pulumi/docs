---
title: Google Cloud Serverless Application
layout: template
meta_desc: The Google Cloud Serverless Template makes it easy to deploy a serverless application on GCP with Pulumi, Google Cloud Functions, and Google Cloud Storage.
meta_image: meta.png
card_desc: Deploy a serverless application on Google Cloud with Pulumi, Google Cloud Functions, and Google Cloud Storage.
template:
  prefix: serverless-gcp
  dirname: my-serverless-app
  languages:
    - typescript
    - python
    - go
    - csharp
    - yaml
cloud:
  name: Google Cloud Platform
  slug: gcp
---

The Serverless Application template creates an infrastructure as code project in your favorite language that deploys a serverless application to Google Cloud Platform with Pulumi. It deploys a [Google Cloud Storage bucket]({{< relref "/registry/packages/gcp/api-docs/storage/bucket" >}}) configured for static website hosting and another bucket to host the source code for a [Cloud Function]({{< relref "/registry/packages/gcp/api-docs/cloudfunctions/function" >}}) written in the same language as the template. The template ships with placeholder content to give you a working project out of the box that you can customize easily and extend to suit your needs.

![An architecture diagram of the Pulumi Google Cloud Serverless Application template](./architecture.png)

## Using this template

To use this template to deploy your own serverless application, make sure you've [installed Pulumi]({{< relref "/docs/get-started/install" >}}) and [configured your Google Cloud credentials]({{< relref "/registry/packages/gcp/installation-configuration#credentials" >}}), then create a new [project]({{< relref "/docs/intro/concepts/project" >}}) using the template in your language of choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

The template requires no additional configuration. Once the new project is created, you can deploy it immediately with [`pulumi up`]({{< relref "/docs/reference/cli/pulumi_up" >}}):

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output]({{< relref "/docs/intro/concepts/stack#outputs" >}}) values:

siteURL
: The HTTP URL of the static website.

apiURL
: The HTTP URL of the serverless function endpoint.

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources. The computed `siteURL`, for example, can be used from the command line to open the newly deployed website in your favorite web browser:

```bash
$ open $(pulumi stack output siteURL)
```

## Customizing the project

Projects created with the serverless template expose the following [configuration]({{< relref "/docs/intro/concepts/config" >}}) settings:

sitePath
: The path to the folder containing the files of the website. Defaults to `www`, which is the name (and relative path) of the folder included with the template.

appPath
: The path to the folder containing the serverless functions to be deployed. Defaults to `app`, which is also included with the template.

indexDocument
: The file to use for top-level pages. Defaults to `index.html`.

errorDocument
: The file to use for error pages. Defaults to `error.html`.

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`]({{< relref "/docs/reference/cli/pulumi_config_set" >}}) as shown below.

```bash
$ pulumi config set www_path ../my-existing-website/build
$ pulumi up
```

## Tidying up

You can cleanly destroy the stack and all of its infrastructure with [`pulumi destroy`]({{< relref "/docs/reference/cli/pulumi_destroy" >}}):

```bash
$ pulumi destroy
```

## Learn more

Congratulations! You're now well on your way to managing a production-grade serverless application on Google Cloud with Pulumi --- and there's lots more you can do from here:

* Discover more architecture templates in [Templates &rarr;]({{< relref "/templates" >}})
* Dive into the Google Cloud Classic package by exploring the [API docs in the Registry &rarr;]({{< relref "/registry/packages/gcp" >}})
* Expand your understanding of how Pulumi works in [Learn Pulumi &rarr;]({{< relref "/learn" >}})
* Read up on the latest new features [in the Pulumi Blog &rarr;](/blog/tag/google-cloud)
