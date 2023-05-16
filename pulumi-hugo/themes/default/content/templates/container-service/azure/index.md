---
title_tag: Deploy a Container Service to Azure
title: Container Service on Azure
layout: template

meta_desc: Easily deploy a container service on Azure with Pulumi and Azure Container Instances (ACI) using this template.
meta_image: meta.png
card_desc: Deploy a container service on Azure with Pulumi and Azure Container Instances.
template:
  prefix: container-azure
  dirname: my-container-service
  languages:
    - typescript
    - python
    - go
    - csharp
cloud:
  name: Microsoft Azure
  slug: azure
---

The Container Service template creates an infrastructure as code project in your favorite language that deploys a container service to Azure. You can then use the container service to build your own containerized application. The architecture includes [Azure Container Instances (ACI)](/registry/packages/azure-native/api-docs/containerinstance) for running containers on serverless compute and an [Azure Container Registry](/registry/packages/azure-native/api-docs/containerregistry) that stores the container image. The template generates a complete infrastructure project with example app content, providing you with a working project out of the box that you can customize easily and extend to suit your needs.

![An architecture diagram of the Pulumi Azure Container Service template](./architecture.png)

## Using this template

To use this template to deploy your own container service, make sure you've [installed Pulumi](/docs/get-started/install) and [configured your Azure credentials](/registry/packages/azure/installation-configuration#credentials), then create a new [project](/docs/concepts/projects) using the template in your language of choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

The template requires no additional configuration. Once the new project is created, you can deploy it immediately with [`pulumi up`](/docs/cli/commands/pulumi_up):

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output](/docs/concepts/stack#outputs) values:

hostname
: The hostname of the container group.

ip
: The public IP address of the container group.

url
: The HTTP URL of the container group.

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources. The computed `url`, for example, can be used from the command line to open the newly deployed application in your favorite web browser:

```bash
$ open $(pulumi stack output url)
```

## Customizing the project

Projects created with the Container Service template expose the following [configuration](/docs/concepts/config) settings:

appPath
: The path to the folder containing the application and Dockerfile. Defaults to `./app`, which contains a "Hello world" example.

containerPort
: The port to expose on the container. Defaults to `80`.

cpu
: The number of CPU cores to allocate on the container. Defaults to `1`.

memory
: The amount of memory, in GB, to allocate on the container. Defaults to `2`.

imageName
: The name of the container image to be published to Azure Container Registry. Defaults to `my-app`.

imageTag
: The tag applied to published container images. Defaults to `latest`.

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`](/docs/cli/pulumi_config_set) as shown below:

```bash
$ pulumi config set someProp ../some/value
$ pulumi up
```

## Tidying up

You can cleanly destroy the stack and all of its infrastructure with [`pulumi destroy`](/docs/cli/commands/pulumi_destroy):

```bash
$ pulumi destroy
```

## Learn more

Congratulations! You're now well on your way to managing a production-grade container service on Azure with Pulumi --- and there's lots more you can do from here:

* Discover more architecture templates in [Templates &rarr;](/templates)
* Dive into the Azure Native package by exploring the [API docs in the Registry &rarr;](/registry/packages/azure-native)
* Expand your understanding of how Pulumi works in [Learn Pulumi &rarr;](/learn)
* Read up on the latest new features [in the Pulumi Blog &rarr;](/blog/tag/containers)
