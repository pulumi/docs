---
title_tag: Deploy a Virtual Machine to Azure
title: Virtual Machine on Azure
layout: template
schema_type: howto
meta_desc: Deploy an Azure virtual machine with Pulumi and Azure Virtual Machines in TypeScript, Python, Go, C#, YAML, or HCL.
meta_image: meta.png
card_desc: Deploy a virtual machine on Azure with Pulumi and Azure Virtual Machines.
template:
  prefix: vm-azure
  dirname: my-virtual-machine
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

The Azure Virtual Machine template scaffolds a Pulumi project that provisions an [Azure virtual machine](/registry/packages/azure-native/api-docs/compute/virtualmachine/) inside a new [Azure Virtual Network](/registry/packages/azure-native/api-docs/network/virtualnetwork/). The instance boots an HTTP server on port 80 from a small init script, so the project deploys end to end out of the box. Use it as a starting point for a web application, backend service, or database VM.

![An architecture diagram of the Azure Virtual Machine template](/templates/virtual-machine/azure/architecture.png)

## Using this template

To use this template to deploy your own virtual machine, make sure you've [installed Pulumi](/docs/install/) and [configured your Azure credentials](/registry/packages/azure-native/installation-configuration#credentials), then create a new [project](/docs/iac/concepts/projects/) using the template in the language of your choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

The template requires no additional configuration. Once the new project is created, you can deploy it immediately with [`pulumi up`](/docs/iac/cli/commands/pulumi_up):

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output](/docs/iac/concepts/stacks/#outputs) values:

{{% choosable language "typescript,python,go,csharp,yaml" %}}

ip
: The IP address of the virtual machine.

hostname
: The provider-assigned hostname of the virtual machine.

url
: The fully-qualified HTTP URL of the HTTP server running on the virtual machine.

{{% /choosable %}}

{{% choosable language hcl %}}

ip
: The IP address of the virtual machine.

hostname
: The provider-assigned hostname of the virtual machine.

url
: The fully-qualified HTTP URL of the HTTP server running on the virtual machine.

private_key
: The PEM-encoded private key for SSH access to the VM. This value is a secret.

{{% /choosable %}}

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources. The computed `url`, for example, can be used from the command line to open the newly deployed website in your favorite web browser:

```bash
$ open $(pulumi stack output url)
```

## Customizing the project

Projects created with the Virtual Machine template expose the following [configuration](/docs/iac/concepts/config/) settings:

{{% choosable language "typescript,python,go,csharp,yaml" %}}

adminUsername
: The user account to create on the VM. Defaults to `pulumiuser`.

vmName
: The DNS hostname prefix to use for the VM. Defaults to `my-server`.

vmSize
: The machine size to use for the VM. Defaults to `Standard_A1_v2`.

osImage
: The Azure URN of the base image to use for the VM. Defaults to `Debian:debian-11:11:latest`.

servicePort
: The HTTP service port to expose on the VM. Defaults to `80`.

sshPublicKey
: The public key data to use for SSH authentication.

{{% /choosable %}}

{{% choosable language hcl %}}

location
: The Azure location to deploy into. Defaults to `WestUS2`.

admin_username
: The user account to create on the VM. Defaults to `pulumiuser`.

vm_name
: The DNS hostname prefix to use for the VM. Defaults to `my-server`.

vm_size
: The machine size to use for the VM. Defaults to `Standard_A1_v2`.

os_image
: The Azure image reference (publisher:offer:sku:version) to use for the VM. Defaults to `Debian:debian-11:11:latest`.

service_port
: The HTTP service port to expose on the VM. Defaults to `80`.

{{% /choosable %}}

All of these settings are optional and may be adjusted either by editing the stack configuration file directly (by default, `Pulumi.dev.yaml`) or by changing their values with [`pulumi config set`](/docs/iac/cli/commands/pulumi_config_set):

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
