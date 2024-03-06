---
title_tag: "Terraform vs. OpenTofu"
meta_desc: Terraform and OpenTofu have a few similarities and key differences. This page helps provide a rundown of these major differences.
title: Terraform vs. OpenTofu
h1: Terraform vs. OpenTofu
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    identifier: vs-terraform-opentofu
    parent: vs
    weight: 1

---

<style>
    main table {
        font-size: 0.94em;
    }

    main table th,
    main table td {
        width: 33.3%;
    }
</style>

Terraform and OpenTofu are both infrastructure as code technologies that have similarities but fundamental differences. They both provide infrastructure as code software for cloud service management with a consistent CLI workflow. They allow you to write, plan, and apply changes to deliver infrastructure as code. In this comprehensive guide, we'll explore their key differences and similarities to help you choose the right infrastructure as code platform to meet your needs.

## Terraform vs. OpenTofu: Similarities {#similarities}

OpenTofu is a fork of Terraform 1.6.x so there are many similiarities for now. They both have the ability to create, deploy, and manage infrastructure as code on any cloud. Both Terraform and OpenTofu follow a desired state infrastructure as code model, where the IaC code represents the desired state of the infrastructure. The deployment engine compares this desired state with the current state of the stack and determines the necessary actions, such as creating, updating, or deleting resources. Both Terraform and OpenTofu support many cloud providers, including [AWS](/aws/), [Azure](/azure/), and [Google Cloud](/gcp/), plus other services like CloudFlare, Digital Ocean, and more. They also both require the use of a domain-specific language: HashiCorp Configuration Language (HCL).

## Terraform vs. OpenTofu: Key Differences {#differences}

Terraform and OpenTofu differ in that Terraform is not open source, using the Business Source License model. OpenTofu, however, uses the weak copyleft [Mozilla Public License 2.0](https://github.com/HashiCorp/terraform/blob/main/LICENSE). Terraform also has a paid offering called Terraform Cloud, a fully managed SaaS service that version controls and manages Terraform state. Terraform Cloud also provides access to remote operations, policy as code, and audit logging. OpenTofu is supported by env0 and Spacelift SaaS services for managing Terraform state. As Terraform and OpenTofu continue to diverge, more key differences will emerge.

Here is a summary of the key differences between Terraform and OpenTofu:

| Feature | Terraform | OpenTofu |
| ------- | ------ | --------- |
| [OSS License](#license) | No, Business Source License 1.1 | Yes, Mozilla Public License 2.0 |
| [Language Support](#language) | HashiCorp Configuration Language (HCL) | HashiCorp Configuration Language (HCL) |
| [IDE Support](#ide) | Limited | Limited |
| [State Management](#state) | Self-managed by default, managed SaaS offering available. | Self-managed by default, managed SaaS offerings available. |
| [Provider Support](#providers) | Support across multiple IaaS, SaaS, and PaaS providers. | Support across multiple IaaS, SaaS, and PaaS providers. |
| [Cloud Native Support](#cloud-native) | Core API typed. Generic support for CRD. | Core API typed. Generic support for CRD. |
| [Dynamic Provider Support](#dynamic-providers) | No | No |
| [Infrastructure Reuse and Modularity](#reuse) | Constrained. Can only reuse Terraform modules. | Constrained. Can only reuse OpenTofu modules. |
| [Testing and Validation](#testing) | Integration testing only. | Integration testing only. |
| [Modes of Execution](#modes) | Run CLI commands or perform remote runs with SaaS offering. | Run CLI commands only. |
| [Embed within Application Code](#embedding) | No | No |
| [Third-party CI/CD Tools Support](#cicd) | Yes | No |
| [Policy as Code](#policy) | Yes | No |
| [Secrets Management](#secrets) | No. Secrets are stored in a  separate product (Vault). There is no way to encrypt them in the state file. | No. Secrets can be stored in a 3rd party product. There is no way to encrypt them in the state file. |
| [Audit Capabilities](#auditing) | Limited | No |
| [Adopt Existing Resources](#adopting) | Yes. No code generation capabilities. | Yes. No code generation capabilities. |
| [Aliases](#aliases) | Limited | Limited |
| [Transformations](#transformations) | No | No |
| [Import Code from other IaC Tools](#converting) | No | No |

Are you constrained by Terraform or OpenTofu? Let us help you migrate to Pulumi so you can have greater developer productivity, ability to scale, and delivery velocity. Follow our comprehensive guides in our [Migration Hub](/blog/migration-hub/) or work with our [Expert Services teams](/contact?form=tf-migration) that can help you with migration and training. If you would like to deploy a simple program, follow our Get Started guide:

{{< get-started >}}
