---
title_tag: Templates for Deploying Virtual Machines
title: Virtual Machine Templates
layout: overview
schema_type: faq
description: Pulumi templates for virtual machines on AWS, Azure, and Google Cloud, in your language of choice.
meta_desc: Deploy virtual machines (VMs) on AWS, Azure, or Google Cloud with Pulumi Virtual Machine templates.
meta_image: meta.png
weight: 1
---

## About these templates

### What is a virtual machine?

A virtual machine (VM) is a software-based computer that runs its own operating system and applications on top of shared physical hardware. Cloud providers offer VMs on demand with configurable CPU, memory, storage, networking, and OS image, billed per second or hour of use.

### Which compute service should I use on each cloud?

Each major cloud has a dedicated VM service:

- **AWS**: [Amazon EC2](/registry/packages/aws/api-docs/ec2/instance/) — instances launched from an AMI inside an [Amazon VPC](/registry/packages/aws/api-docs/ec2/vpc/).
- **Azure**: [Azure Virtual Machines](/registry/packages/azure-native/api-docs/compute/virtualmachine/) — instances inside an [Azure Virtual Network](/registry/packages/azure-native/api-docs/network/virtualnetwork/).
- **Google Cloud**: [Compute Engine](/registry/packages/gcp/api-docs/compute/instance/) — instances inside a [VPC network](/registry/packages/gcp/api-docs/compute/network/).

### How do I deploy a virtual machine with Pulumi?

Use one of the Virtual Machine templates above to scaffold a Pulumi project that provisions the VM and the surrounding network, security, and (optionally) SSH-key resources. Each template boots the instance with a small HTTP server so the project deploys end to end with `pulumi new` followed by `pulumi up`.

### Can I customize the OS image, instance type, or network for the VM?

Yes. Each template exposes the OS image, instance/machine type, and (where applicable) the VPC CIDR as Pulumi [configuration values](/docs/iac/concepts/config/). You can change them with `pulumi config set` before running `pulumi up`, or edit the program directly to extend the resources further.
