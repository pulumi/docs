---
title_tag: Deploy a Container Service to Google Cloud
title: Container Service on Google Cloud
layout: template
schema_type: howto
meta_desc: Deploy a container service on Google Cloud with Pulumi, Cloud Run, and Artifact Registry in TypeScript, Python, Go, C#, or HCL.
meta_image: meta.png
card_desc: Deploy a container service on Google Cloud with Pulumi and Google Cloud Run.
template:
  prefix: container-gcp
  dirname: my-container-service
  languages:
    - typescript
    - python
    - go
    - csharp
    - hcl
cloud:
  name: Google Cloud
  slug: gcp
---

The Google Cloud Container Service template scaffolds a Pulumi project that deploys a containerized service to [Google Cloud Run](/registry/packages/gcp/api-docs/cloudrun) for serverless container execution, with the container image stored in Artifact Registry. The template ships with placeholder app content so the project deploys end to end out of the box.

![An architecture diagram of the Google Cloud Container Service template](/templates/container-service/gcp/architecture.png)

## Using this template

To use this template to deploy your own container service, make sure you've [installed Pulumi](/docs/install/) and [configured your Google Cloud credentials](/registry/packages/gcp/installation-configuration#credentials), then create a new [project](/docs/iac/concepts/projects/) using the template in the language of your choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

{{% choosable language "typescript,python,go,csharp" %}}

You must supply an existing Google Cloud project ID and choose a region before deploying the container service. You can input both through the new-project wizard. Once the project is created, you can deploy it with [`pulumi up`](/docs/iac/cli/commands/pulumi_up):

{{% /choosable %}}

{{% choosable language hcl %}}

The template deploys into your active Google Cloud project (read from your gcloud credentials) and defaults to the `us-central1` region, which you can change with the `region` setting. Once the new project is created, you can deploy it with [`pulumi up`](/docs/iac/cli/commands/pulumi_up):

{{% /choosable %}}

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output](/docs/iac/concepts/stacks/#outputs) values:

url
: The HTTP URL of your Cloud Run service.

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources. The computed `url`, for example, can be used from the command line to open the newly deployed container in your favorite web browser:

```bash
$ open $(pulumi stack output url)
```

## Customizing the project

Projects created with the Container Service template expose the following [configuration](/docs/iac/concepts/config/) settings:

{{% choosable language "typescript,python,go,csharp" %}}

containerPort
: The port mapping for the container service. Defaults to port `8080`.

cpu
: The amount of CPU to allocate to each container instance. Defaults to `1` CPU.

memory
: The amount of memory to allocate to each container instance. Defaults to `1Gi`.

concurrency
: The maximum number of concurrent requests per container instance. Defaults to `50`.

imageName
: The name of the container image deployed to your Cloud Run service. Defaults to `my-app`.

appPath
: The location of the Dockerfile used to build the container image. Defaults to the `app` folder, which contains a "Hello World" example app.

{{% /choosable %}}

{{% choosable language hcl %}}

region
: The Google Cloud region to deploy into. Defaults to `us-central1`.

app_path
: The location of the Dockerfile used to build the container image. Defaults to the `app` folder, which contains a "Hello World" example app.

image_name
: The name of the container image deployed to your Cloud Run service. Defaults to `my-app`.

container_port
: The port mapping for the container service. Defaults to port `8080`.

cpu
: The amount of CPU to allocate to each container instance. Defaults to `1` CPU.

memory
: The amount of memory to allocate to each container instance. Defaults to `1Gi`.

concurrency
: The maximum number of concurrent requests per container instance. Defaults to `80`.

{{% /choosable %}}

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set):

{{% choosable language "typescript,python,go,csharp" %}}

```bash
$ pulumi config set containerPort 3000
$ pulumi up
```

{{% /choosable %}}

{{% choosable language hcl %}}

```bash
$ pulumi config set container_port 3000
$ pulumi up
```

{{% /choosable %}}

## Cleaning up

You can cleanly destroy the stack and all of its infrastructure with [`pulumi destroy`](/docs/iac/cli/commands/pulumi_destroy):

```bash
$ pulumi destroy
```

## Learn more

* Browse other architecture templates in the [Templates gallery](/templates).
* Explore the [Google Cloud provider API docs](/registry/packages/gcp) in the Pulumi Registry.
* Walk through Pulumi from the ground up in [Pulumi Tutorials](/tutorials/).
* Read the latest [container posts on the Pulumi blog](/blog/tag/containers).
