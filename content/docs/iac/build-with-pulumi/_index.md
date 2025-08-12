---
title_tag: Build with Pulumi
meta_desc: Pulumi offers a number of ways to extend its functionality via providers, components, packages, and more, in any Pulumi language.
title: Build with Pulumi
h1: Build with Pulumi
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Build with Pulumi
        parent: iac-home
        weight: 76
        identifier: iac-build-with-pulumi
aliases:
- /docs/iac/using-pulumi/extending-pulumi/
- /docs/iac/extending-pulumi/
---

Pulumi offers a number of ways to extend its functionality including [providers](/docs/iac/concepts/resources/providers/), [components](/docs/iac/concepts/resources/components/), [packages](/docs/iac/concepts/packages/), and more.

## What are my options?

Deciding which way to extend Pulumi will depend on your use case. Some options require more or less code, have certain language or functionality limitations, and can be shared in different ways.

This comparison chart will help guide you on how to invest your time and energy into customizing Pulumi to your needs.

### Comparison Chart

| Technique | Description | Language Support | Sharing | Use Case | Limitations |
| --------- | ----------- | ---------------- | ------- | -------- | ----------- |
| **Component** | A customized abstraction of one or more resources | Write and use in all Pulumi languages | Local, Git repo, or Pulumi package | Create reusable abstractions on top of existing provider resources, often to encode company standards and security policies | Components do not define new resources. They are an abstraction on top of existing provider resources. |
| **Packaged Provider**  | A plugin that performs CRUD operations against cloud service APIs, providing resources used in Pulumi programs. | Write in Go, use in all Pulumi languages | Local, Git repo, or Pulumi package | Add support for a new cloud service to Pulumi, for all languages, and publish it for reuse | Requires the most development investment |
| **Dynamic Provider** | A simplified type of provider that doesn't require packaging | Write in TypeScript, JavaScript, and Python, use *only* in the same language | Local only | Quickly mock-up a provider to manage resources in a cloud service not already supported by Pulumi | Can't be packaged or published to the Pulumi Registry, code must be serializable, can't generate multi-language SDKs |
| **Bridged Provider** | A wrapper for a Terraform provider | Write in Go, use in all Pulumi languages | Local, Git repo, or Pulumi package | Use an existing Terraform provider within Pulumi | Must have an existing Terraform provider |
| **Terraform Module** | Adapts existing Terraform modules to use in Pulumi | Use in all Pulumi languages | Local, Git repo, or Pulumi package | Leverage existing Terraform modules directly within Pulumi programs | Some limitations for targeted updates and transforms |

## Resources, Providers, and Components

Pulumi programs work with three core concepts; *resources*, *providers*, and *components*.

### Resources

In the simplest terms, the purpose of a Pulumi program is to manage cloud *resources*. A resource is a representation of an artifact that exists within an external cloud service. A Pulumi *program* describes the *desired state* of the resources, while the Pulumi *backend* keeps track of the state of those resources.

### Providers

Pulumi manages resources by interacting with *providers*, which are plugins that create, update, and destroy resources. During an update, the provider will compare what is described in the Pulumi program to the state stored in the backend, determining what operations, if any, are needed to update the resources to match. The Pulumi engine will then load and interact with one or more provider plugins, calling the necessary operations through a standard provider API. The provider plugin implements the necessary resource-specific create, update, and delete operations, often by calling external cloud service APIs directly.

### Components

Components are higher-level abstractions of one or more resources that work together in a logical unit. Imagine that you need to create multiple instances of a web server, its backing database, and the network they communicate over. All of those need to be in compliance with your company's security policy and coding standards, but also need some customization for each instance of this group of resources. A component can be created that encodes those required standards and surfaces the configurable parts in a simple-to-use API for your internal developers.

While providers sometimes surface higher-level components for common use cases, they usually only provide the low-level resources. Components–which under the hood are resources themselves–can be developed alongside your Pulumi programs, and used locally, shared via a git repo, or packaged and published in the Pulumi Registry, without the need to implement CRUD operations directly against the underlying cloud service APIs. This makes them a very flexible way to extend and customize Pulumi as long as there is a provider available for the cloud service you want to interact with.

### Do I need a Component or a Provider?

Here's some quick rules-of-thumb for deciding whether to create a component or a provider:

| Topic | Components | Providers |
| ----- | ---------- | --------- |
| **Use Case** | Create a ***component*** when you need to make reusable higher-level abstractions over *existing* resources already available in Pulumi (e.g. to encode company policies) | Create a ***provider*** when you need to make new resource types *not* already available in Pulumi (e.g. to manage resources in a cloud service not already supported by Pulumi) |
| **Language Support** | Components can be both *used* and *written* in any Pulumi language | Providers can be *used* in any Pulumi language, but can only be *written* in Go |
| **Sharing and Reusablity** | Components can be used locally (from another directory on the filesystem), downloaded from a Git repo, or published and shared via the Pulumi Registry | Providers must be published to the Pulumi Registry to be used (with the exception of [Dynamic Providers](/docs/iac/concepts/resources/dynamic-providers)) |

## Local vs Remote

In our documentation we sometimes refer to things as being "local" vs "remote" (e.g. using a local package). This has to do with where the Pulumi Engine is running. When you run the `pulumi up` command via the CLI, the Pulumi Engine will run on the same machine. That engine loads and runs the plugins and interacts with the backend to manage state. In this mode, it is running *locally*, and therefore has access to the filesystem on that machine, and could load a plugin directly from a locally stored directory. However, when using Pulumi Deployments in Pulumi Cloud, the Pulumi Engine is running in a virtual machine on our infrastructure. In that case, it is running "remotely".

This matters when we talk about components and providers because Pulumi Deployments might fail to load a plugin that doesn't exist in its environment. In order for Pulumi Deployments to access the plugin, it needs to be packaged and published to the Pulumi Registry, so that it can be downloaded at runtime. Or, in the case of components and dynamic providers, the code needs to be committed alongside your normal Pulumi program code, in the same Git repository.

## Packaging and Publishing

Pulumi [*packages*](/docs/iac/concepts/packages/) are a standardized way to share providers and components. After building a provider or component, the next steps involve generating docs and end-user SDK code in various target languages, both of which are based on the [`schema.json` file](schema/). Those user-facing assets are packaged up in a tarball. Once you have a package, this can either be used locally or shared via the Pulumi Registry.

Learn more in the [package documentation](/docs/iac/concepts/packages).

![A diagram showing how Pulumi Package code can be authored in one language and made available in all other languages supported by Pulumi](/docs/iac/concepts/img/pulumi-package-concepts.png)

### Language Limitations

One of the most powerful aspects of using Pulumi is the flexibility to author in your preferred language. Pulumi programs can be written in TypeScript, JavaScript, Python, Go, Java, the .NET languages like C# and F#.

When extending Pulumi, you get the same great flexibility, with some caveats:

- [Components](/docs/iac/concepts/resources/components/) can be written and used in any of Pulumi's supported languages except for JavaScript.
- [Providers](/docs/iac/concepts/resources/providers/) can be written in Go, and used in any of Pulumi's supported languages.
- [Dynamic Providers](/docs/iac/concepts/resources/dynamic-providers) can be written in TypeScript, JavaScript, and Python, and can only be used in the same language they were authored in. Also, the code [must be serializable](/docs/iac/concepts/miscellaneous/function-serialization/).

This flexibility is made possible through code generation. When you author a component or provider, the `schema.json` is used to generate docs and SDKs in all target languages. Those SDKs are included in the Pulumi package, and the docs generated and published in the Pulumi Registry, making it very easy for end users to consume your code.

![A graphic representation of the steps listed above](/docs/iac/concepts/img/pulumi-package-overview.png)

## Leveraging the Ecosystem

Another great thing about Pulumi is that it exists within a vast ecosystem of tooling and community. Before writing a component or provider, we strongly encourage you to look for prior art within the ecosystem. Some places you can look for help are:

- **The [Pulumi Registry](/registry)** - our hosted repository of providers and components contains hundreds of existing packages that can be used directly within Pulumi. These are all open-source code, with their code repository linked directly on every page.
- **The [Terraform Provider Registry](https://registry.terraform.io/)** - any Terraform-compatible provider can be [*bridged*](/blog/any-terraform-provider/) to work within Pulumi. That gives you access to thousands of existing providers! If the provider you need isn't in our registry, but does exist in Terraform's registry, you can use it immediately via the [terraform-provider](https://www.pulumi.com/registry/packages/terraform-provider/).
- **The [Terraform Module Registry](https://registry.terraform.io/browse/modules)** - you can [use Terraform modules directly](/docs/iac/using-pulumi/extending-pulumi/use-terraform-module/) within Pulumi programs. This gives you access to thousands of pre-built, reusable infrastructure modules without needing to rewrite them.
- **The [OpenTofu Registry](https://search.opentofu.org/providers)** - a fork of Terraform that maintains its own registry of thousands of Terraform-compatible providers, which can also be [bridged into Pulumi](/blog/any-terraform-provider/).
- **The [Pulumi Command Provider](https://www.pulumi.com/registry/packages/command/)** - a Pulumi provider that allows you to run arbitrary shell commands. Many use cases can be covered by using this provider, shelling out to use the third-party CLI tool for a new cloud product, instead of writing a provider from scratch. This is often the lightest-weight way to extend Pulumi.

If you're not having luck finding what you need on your own, you can always reach out to other Pulumi users via our [Community Slack](https://slack.pulumi.com) channel.

### Contributing

If there is an existing provider, but it lacks functionality you need, instead of writing a new provider, consider filing an issue and/or contributing to the open source code. This will both solve your problem and also make that solution available to anyone else who might encounter it.

That said, there are times when you need to write an entirely new provider from scratch. While you can absolutely build, host, use, and maintain that provider privately, we strongly encourage you to make the code public and share it via the Pulumi Registry. [Packaging](/docs/iac/concepts/packages) up and [publishing](publishing-packages) your components and providers allows others to both benefit from your work as well contribute to the code, reducing your long-term maintenance costs. It's a great way to connect with other Pulumi users and attract talented engineers to your company.
