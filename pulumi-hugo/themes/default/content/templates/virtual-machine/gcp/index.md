---
title: Virtual Machine on Google Cloud
layout: template
meta_desc: The Virtual Machine template makes it easy to deploy a virtual machine on Google Cloud with Pulumi and Google Compute Engine. 
meta_image: meta.png
card_desc: Deploy a virtual machine on Google Cloud with Pulumi and Google Compute Engine. 
template:
    prefix: vm-gcp
    dirname: my-virtual-machine
    languages:
      - typescript
      - python
      - go
      - csharp
      - yaml
cloud:
  name: Google Cloud
  slug: gcp
---

The Virtual Machine template creates an infrastructure as code project in your favorite language that deploys a virtul machine to Google Cloud. You can then use the virtual machine to build your own web application, backend service, or database. The architecture includes Compute Engine for the virtual machine and the virtual network. The template generates a complete Pulumi program, including a simple HTTP server, to give you a working project out of the box that you can customize easily and extend to suit your needs.

![An architecture diagram of the Pulumi $CLOUD $ARCHITECTURE template](./architecture.png)

## Using this template

To use this template to deploy a website of your own, make sure you've [installed Pulumi](/docs/get-started/install) and [configured your Google Cloud credentials](/registry/packages/gcp/installation-configuration#credentials), then create a new [project](/docs/intro/concepts/project) using the template in your language of choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

The template requires no additional configuration. Once the new project is created, you can deploy it immediately with [`pulumi up`](/docs/reference/cli/pulumi_up):

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output](/docs/intro/concepts/stack#outputs) values:

ip
: The IP address of the virtual machine.

hostname
: The provider-assigned hostname of the virtual machine.

url
: The fully-qualified HTTP URL of the HTTP server running on the virtual machine.

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources. The computed `url`, for example, can be used from the command line to open the newly deployed website in your favorite web browser:

```bash
$ open $(pulumi stack output url)
```

## Customizing the project

Projects created with the Virtual Machine template expose the following [configuration](/docs/intro/concepts/config) settings:

machineType
: The Compute Engine machine type to use for the VM. Defaults to `f1-micro`.

osImage
: The OS image type to use for the VM. Defaults to `debian-11`.

instanceTag
: The tag to apply to the VM instance. Defaults to `webserver`.

servicePort
: The HTTP service port to expose on the VM. Defaults to `80`.

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`](/docs/reference/cli/pulumi_config_set) as shown below.

## Cleaning up

You can cleanly destroy the stack and all of its infrastructure with [`pulumi destroy`](/docs/reference/cli/pulumi_destroy):

```bash
$ pulumi destroy
```

## Learn more

Congratulations! You're now well on your way to managing a production-grade virtual machine on Google Cloud with Pulumi --- and there's lots more you can do from here:

* Discover more architecture templates as they're available in [Templates &rarr;](/templates)
* Dive into the Google Cloud package by exploring the [API docs in the Registry &rarr;](/registry/packages/gcp)
* Expand your understanding of how Pulumi works in [Learn Pulumi &rarr;](/learn)
* Read up on the latest new features [in the Pulumi Blog &rarr;](/blog/tag/google-cloud)
