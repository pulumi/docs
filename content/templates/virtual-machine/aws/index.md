---
title_tag: Deploy a Virtual Machine to AWS
title: Virtual Machine on AWS
layout: template
schema_type: howto
meta_desc: Deploy an Amazon EC2 virtual machine on AWS running Amazon Linux 2023 with Pulumi in TypeScript, Python, Go, C#, YAML, or HCL.
meta_image: meta.png
card_desc: Deploy a virtual machine on AWS with Pulumi and Amazon EC2.
template:
    prefix: vm-aws
    dirname: my-virtual-machine
    languages:
      - typescript
      - python
      - go
      - csharp
      - yaml
      - hcl
cloud:
  name: Amazon Web Services
  slug: aws
---

The AWS Virtual Machine template scaffolds a Pulumi project that provisions an [Amazon EC2 instance](/registry/packages/aws/api-docs/ec2/instance/) running Amazon Linux 2023 inside a new [Amazon VPC](/registry/packages/aws/api-docs/ec2/vpc/). The instance boots a small Python HTTP server on port 80 from user data, so the project deploys end to end out of the box. Use it as a starting point for a web application, backend service, or database VM.

![An architecture diagram of the AWS Virtual Machine template](/templates/virtual-machine/aws/architecture.png)

## Using this template

To use this template to deploy your own virtual machine, make sure you've [installed Pulumi](/docs/install/) and [configured your AWS credentials](/registry/packages/aws/installation-configuration#credentials), then create a new [project](/docs/iac/concepts/projects/) using the template in the language of your choice:

{{< templates/pulumi-new >}}

Follow the prompts to complete the new-project wizard. When it's done, you'll have a complete Pulumi project that's ready to deploy and configured with the most common settings. Feel free to inspect the code in {{< langfile >}} for a closer look.

## Deploying the project

The template requires no additional configuration. Once the new project is created, you can deploy it immediately with [`pulumi up`](/docs/iac/cli/commands/pulumi_up):

```bash
$ pulumi up
```

When the deployment completes, Pulumi exports the following [stack output](/docs/iac/concepts/stacks/#outputs) values:

ip
: The IP address of the EC2 instance.

hostname
: The provider-assigned hostname of the EC2 instance.

url
: The fully-qualified HTTP URL of the HTTP server running on the EC2 instance.

Output values like these are useful in many ways, most commonly as inputs for other stacks or related cloud resources. The computed `url`, for example, can be used from the command line to open the newly deployed website in your favorite web browser:

```bash
$ open $(pulumi stack output url)
```

## Customizing the project

Projects created with the Virtual Machine template expose the following [configuration](/docs/iac/concepts/config/) settings:

{{% choosable language "typescript,python,go,csharp,yaml" %}}

instanceType
: The EC2 instance type to use for the VM. Defaults to `t3.micro`.

vpcNetworkCidr
: The network CIDR to use for the VPC. Defaults to `10.0.0.0/16`.

{{% /choosable %}}

{{% choosable language hcl %}}

instance_type
: The EC2 instance type to use for the VM. Defaults to `t3.micro`.

vpc_network_cidr
: The network CIDR to use for the VPC. Defaults to `10.0.0.0/16`.

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
* Explore the [AWS provider API docs](/registry/packages/aws) in the Pulumi Registry.
* Walk through Pulumi from the ground up in [Pulumi Tutorials](/tutorials/).
* Read the latest [AWS posts on the Pulumi blog](/blog/tag/aws).
