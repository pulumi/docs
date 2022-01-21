---
title: Pulumi vs. Terraform
meta_desc: "Pulumi and Terraform have a few similarities, but they differ in many key ways. This page helps provide a rundown of the differences."
linktitle: Terraform
menu:
  intro:
    parent: vs
    weight: 1
aliases:
- /docs/reference/vs/terraform/
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

Choosing the right cloud engineering platform is critical. We want you to have the best information possible to pick the solution that fits your needs.

## What is Terraform?

Terraform provides open-source [infrastructure as code]({{< relref "/what-is/what-is-infrastructure-as-code" >}}) software for cloud service management with a consistent CLI workflow. Terraform allows you to write, plan, and apply changes to deliver infrastructure as code.

## Pulumi vs. Terraform: Similarities {#similarities}

Terraform and Pulumi have some similarities in that you can create, deploy and manage infrastructure as code on any cloud. Like Terraform, Pulumi is [open source on GitHub](https://github.com/pulumi/pulumi) and is [free to use]({{< relref "/docs/get-started" >}}). Both Terraform and Pulumi offer a desired state infrastructure as code model where the code represents the desired infrastructure state and the deployment engine compares this desired state with the stack’s current state and determines what resources need to be created, updated or deleted.  Both Terraform and Pulumi support many cloud providers, including [AWS](/aws), [Azure](/azure), and [Google Cloud](/gcp), plus other services like CloudFlare, Digital Ocean, and more. Thanks to integration with Terraform providers, Pulumi is also able to support a superset of the providers that Terraform currently offers.

## Pulumi vs. Terraform: Key Differences {#differences}

Pulumi and Terraform differ in that Terraform requires the use of a domain-specific language: HashiCorp Configuration Language (HCL). In contrast, Pulumi allows you to use familiar general purpose languages like [Python]({{< relref "/docs/intro/languages/python" >}}), [TypeScript]({{< relref "/docs/intro/languages/javascript" >}}), [JavaScript]({{< relref "/docs/intro/languages/javascript" >}}), [Go]({{< relref "/docs/intro/languages/go" >}}) and [.NET]({{< relref "/docs/intro/languages/dotnet" >}}) with the tools you already use to accomplish the same goals. Terraform recently released the beta of a development kit that allows you to use programming languages that compile to HCL.

Here is a summary of the key differences between Pulumi and Terraform:

| Feature | Pulumi | Terraform |
| ------- | ------ | --------- |
| [Language Support](#language) | Python, TypeScript, JavaScript, Go, C#, F# | HashiCorp Configuration Language (HCL) |
| [IDE Support](#ide) | Code completion, strong typing, error squiggles, rich resource documentation, etc. | Limited |
| [State Management](#state) | Managed through Pulumi Service by default, self-managed options available. | Self-managed by default, managed SaaS offering available. |
| [Provider Support](#providers) | Native cloud providers with 100% same-day resource coverage plus Terraform-based providers for additional coverage. | Support across multiple IaaS, SaaS, and PaaS providers. |
| [Cloud Native Support](#cloud-native) | Richly typed. Includes CRDs & in-cluster operator support for GitOps delivery. | Core API typed. Generic support for CRD. |
| [Dynamic Provider Support](#dynamic-providers) | Yes | No |
| [OSS License](#license) | Apache License 2.0 | Mozilla Public License 2.0 |
| [Infrastructure Reuse and Modularity](#reuse) | Flexible. Reuse functions, classes, packages, and Pulumi components. | Constrained. Can only reuse Terraform modules. |
| [Testing and Validation](#testing) | Unit, property, and integration testing. Supports popular test frameworks. | Integration testing only |
| [Modes of Execution](#modes) | Run CLI commands or initiate commands programmatically with Automation API. | Run CLI commands or perform remote runs with SaaS offering. |
| [Embed within Application Code](#embedding) | Yes, via Automation API | No |
| [Third-party CI/CD Tools Support](#cicd) | Yes | Yes |
| [Policy as Code](#policy) | Yes | Yes |
| [Secrets Management](#secrets) | Yes. Secrets are encrypted in transit and in the state file. | No. Secrets are stored in a  separate product (Vault). There is no way to encrypt them in the state file. |
| [Audit Capabilities](#auditing) | Yes | Limited |
| [Adopt Existing Resources](#adopting) | Yes. Generates code as part of the import process. | Yes. No code generation capabilities. |
| [Aliases](#aliases) | Yes | Limited |
| [Transformations](#transformations) | Yes | No |
| [Import Code from other IaC Tools](#converting) | Yes | No |

Getting started with Pulumi is easy. If you have experience with Terraform and already have HCL, you can convert it to Pulumi. Follow our [Converting Terraform HCL to Pulumi]({{< relref "/docs/guides/adopting/from_terraform#converting-terraform-hcl-to-pulumi" >}}) guide. If you would like a reference on Terraform terminology or command equivalents in Pulumi, see [Terminology and Command Equivalence]({{< relref "/docs/intro/vs/terraform/terminology" >}}) table. If you would like to deploy a simple program, follow our Get Started guide:

{{< get-started >}}

The following sections go into further detail on the differences between Pulumi and Terraform.

### Language Support {#language}

Terraform requires that you and your team write programs in a custom domain-specific language (DSL) called HashiCorp Configuration Language (HCL). In contrast, Pulumi lets you use programming languages like Python, Go, JavaScript, TypeScript, and C#. Because of the use of familiar languages, you get familiar constructs like conditionals, loops, functions, and classes. This significantly improves the ability to cut down on boilerplate and enforce best practices. With HCL, it is common to copy and paste blocks of HCL code between different projects. Pulumi’s supported programming languages have been built over multiple decades to tame complexity at scale---the very complexity modern cloud architectures operating at global scale need to tackle. Instead of creating a new ecosystem of modules and sharing, Pulumi lets you leverage existing package management tools and techniques.

### IDE Support {#ide}

Terraform has plugins for some IDEs. However, the features are varied and limited. With Pulumi, you can tap into decades of innovation with great IDEs. The IDEs automatically provide code completion, strong typing, error squiggles, rich resource documentation, and more.

### State Management {#state}

The Terraform engine takes care of provisioning and updating resources. With Pulumi, you use general purpose languages to express desired state, and Pulumi’s engine similarly gives you diffs and a way to robustly update your infrastructure.

By default, Terraform requires that you manage concurrency and state manually, by way of its “state files.” Pulumi, in contrast, uses the free [Pulumi Service](https://app.pulumi.com/) to eliminate these concerns. This makes getting started with Pulumi, and operationalizing it in a team setting, much easier. For advanced use cases, it is possible to [use Pulumi without the Service]({{< relref "/docs/troubleshooting/faq#can-i-use-pulumi-without-depending-on-the-pulumi-service" >}}), which works a lot more like Terraform, but requires you to manage state and concurrency issues. Pulumi errs on the side of ease-of-use.

For more information on how Pulumi manages state or how to use different backends, see [State and Backends]({{< relref "/docs/intro/concepts/state" >}}).

### Provider Support {#providers}

Pulumi supports over 60 of the leading cloud providers and modern cloud SaaS offerings including Amazon Web Services, Microsoft Azure, Google Cloud, Kubernetes, Auth0, CloudFlare, Confluent Cloud, Datadog, DigitalOcean, Docker, GitHub, Kong, MinIO, MongoDB Atlas, PagerDuty, Snowflake, Spot by NetApp, and SumoLogic. Pulumi also has [native providers]({{< relref "/blog/pulumiup-native-providers" >}}) for AWS, Azure, Google, and Kubernetes that provide same-day support for every new release. For more information on Pulumi providers, see [Pulumi Registry]({{< relref "/registry/" >}}).

Pulumi also has deep support for cloud native technologies like Kubernetes, and supports advanced deployment scenarios that cannot be expressed with Terraform. This includes Prometheus-based canaries, automatic Envoy sidecar injection, and more. Pulumi is a proud member of the Cloud Native Computing Foundation (CNCF).

#### Using Terraform Providers {#providers-terraform}

Pulumi is able to adapt [any Terraform Provider](https://github.com/terraform-providers) for use with Pulumi, enabling management of any infrastructure supported by the Terraform Providers ecosystem using Pulumi programs.

Indeed, some of Pulumi’s most interesting providers have been created this way, delivering access to robust, tried-and-true infrastructure management. The Terraform Providers ecosystem is mature and healthy, and enjoys contributions from many cloud and infrastructure leaders across the industry, ourselves included.

Most Pulumi users don’t need to know about this detail, however we are proud to be building on the work of others, and contributing our own open source back to this vibrant ecosystem, and thought you should know.

In the event you’d like to add new providers, or understand how this integration works, check out the [Pulumi Terraform bridge repo](https://github.com/pulumi/pulumi-terraform-bridge). This bridge is fully open source and makes it easy to create new Pulumi providers out of existing Terraform Providers.

#### Converting From Terraform to Pulumi {#providers-converting}

Pulumi offers a tool called [tf2pulumi](https://github.com/pulumi/tf2pulumi) that converts Terraform HCL to Pulumi. It is open source on GitHub, and works well for most projects. (If you run into a snag, issues and pull requests are welcome!) To learn more, see [Converting Terraform HCL to Pulumi]({{< relref "/docs/guides/adopting/from_terraform#converting-terraform-hcl-to-pulumi" >}}) in our Adopting Pulumi user guide.

For an example of how to do a Terraform-to-Pulumi conversion, see our article, [From Terraform to Infrastructure as Software]({{< relref "/blog/from-terraform-to-infrastructure-as-software" >}}).

#### Using Pulumi and Terraform Side-by-Side {#providers-side-by-side}

Pulumi supports [consuming local or remote Terraform state]({{< relref "/blog/using-terraform-remote-state-with-pulumi" >}}) from your Pulumi programs. This helps with incremental adoption, whereby you continue managing a subset of your infrastructure with Terraform while you incrementally move to Pulumi.

For example, maybe you would like to keep your VPC and low-level network definitions written in Terraform so as to avoid any disruption, or maybe some of the team would like to stay on Terraform for now and make a shift in the future. Using the state reference support described previously, you can author higher-level infrastructure in Pulumi that consumes the Terraform-provisioned VPC information (such as the VPC ID, Subnet IDs, etc.), making the co-existence of Pulumi and Terraform easy to automate.

To learn more, see [Referencing Terraform State]({{< relref "/docs/guides/adopting/from_terraform#referencing-terraform-state" >}}) in our Adopting Pulumi user guide.

### Cloud Native Support {#cloud-native}

Pulumi supports the cloud native ecosystem. This includes a native Kubernetes provider with 100% Kubernetes API coverage in all languages, including compile-time type-checking. Pulumi also includes Helm 2 and 3 support, strongly typed CustomResourceDefinitions (CRDs), deploying Kubernetes YAML or Kustomize templates, as well as a YAML-to-Pulumi conversion tool that can translate any Kubernetes YAML into your desired language. Pulumi also offers playbooks with built-in best practices for production cluster deployments for AWS EKS, Azure AKS, and Google GKE. Pulumi also offers a Kubernetes operator that allows you to continuously deliver via GitOps. Terraform offers similar support for the Kubernetes core API and Helm but has generic support for CRDs, meaning no compile-type type-checking or auto-complete.

### Dynamic Provider Support {#dynamic-providers}

Pulumi provides dynamic providers that allow you to extend your system by creating new kinds of custom resources by directly coding CRUD operations for the new resource in your Pulumi program. This can be used to support new resource types in addition to performing complex integrations like database migrations, configuration management for virtual machines, and more, all orchestrated alongside your IaC workflows. Terraform does not have a direct equivalent to Dynamic Providers and would require writing complex and proprietary modules in order to build custom resources with CRUD operations. To learn more, see [Dynamic Providers]({{< relref "docs/intro/concepts/resources/dynamic-providers" >}}).

### OSS License {#license}

Terraform uses the weak copyleft [Mozilla Public License 2.0](https://github.com/HashiCorp/terraform/blob/main/LICENSE). Conversely, Pulumi open-source projects use the permissive and business-friendly [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE). This includes the core [Pulumi repo](https://github.com/pulumi/pulumi), all of the open-source Pulumi resource providers (such as the [Azure Native provider](https://github.com/pulumi/pulumi-azure-native)), conversion utilities like [tf2pulumi](https://github.com/pulumi/tf2pulumi), and other useful projects.

### Infrastructure Reuse and Modularity {#reuse}

Pulumi promotes creating reusable and modular components which allows standard and well-architected infrastructure building blocks to be templatized and easily reused. With Pulumi, you can reuse functions, classes, and packages. Pulumi also has a built-in component model that lets you abstract and encapsulate complexity with higher-level abstractions. These components have a trackable state, appear in diffs, and use a logical name that tracks the resource identity across deployments. Pulumi also provides Pulumi Packages which allows you to author components in one language and make the component accessible in all the other languages that Pulumi supports. Terraform uses HCL which requires you to build proprietary modules and Go-based providers in order to build modular and reusable infrastructure. For more information about how to author reusable components, see [Component Resources]({{< relref "/docs/intro/concepts/resources/#components" >}}).

Pulumi also provides the [Pulumi Registry]({{< relref "/registry/" >}}) which is a searchable collection of Pulumi Packages published by Pulumi and our partners. With Pulumi Registry, you can easily find the package with the resources you need, install that package directly into your project, and start building.

### Testing and Validation {#testing}

Terraform supports integration testing. With Pulumi, you can take advantage of native testing frameworks and perform automated tests of your infrastructure because Pulumi uses general purpose programming languages to provision cloud resources. Pulumi provides unit tests (fast in-memory tests that mock all external calls), property tests (run resource-level assertions while infrastructure is being deployed), and integration tests (deploy ephemeral infrastructure and run external tests against it). For more information on how to run tests with Pulumi, see [Testing]({{< relref "/docs/guides/testing/" >}}).

### Modes of Execution {#modes}

Both Pulumi and Terraform can execute commands through their CLI. Terraform can also do remote operations through Terraform Cloud. Pulumi also provides two APIs by which you can execute Pulumi commands. First, the Automation API allows you to provision, update, and destroy infrastructure through Pulumi directly in your application code. This enables higher order orchestration workflows and dynamically managed infrastructure. Second, the REST API allows you to query and interact with state information, history, stack tags when using the Managed Pulumi Service. To learn more, see [Automation API]({{< relref "/docs/guides/automation-api" >}}) and [REST API]({{< relref "/docs/reference/service-rest-api" >}}).

### Embed within Application Code {#embedding}

Pulumi has the ability to embed Pulumi programs directly into your application code through the Automation API, a programmatic interface for running Pulumi programs without the Pulumi CLI. The Automation API is a strongly typed and safe way to use Pulumi in embedded contexts such as web servers without having to shell out to a CLI. You can easily create custom experiences on top of Pulumi that are tailored to your use-case, domain, and team. Terraform does not have an equivalent to Automation API. To learn more, see [Automation API]({{< relref "/docs/guides/automation-api/" >}}).

### Third-Party CI/CD Tools Support {#cicd}

Pulumi integrates with existing CI/CD providers including AWS Code Services, Azure DevOps, CircleCI, CodeFresh, GitHub Actions, GitLab Pipelines, Google Cloud Build, Jenkins, Octopus Deploy, Jetbrains TeamCity, Spinnaker, and Travis. Pulumi allows you to use the same CI/CD system for your infrastructure as your application code. Terraform also has similar support with existing CI/CD providers.

For more information on how to integrate your CI/CD system with Pulumi, see [Continuous Delivery]({{< relref "/docs/guides/continuous-delivery/" >}}).

### Policy as Code {#policy}

Terraform provides policy as code through its Sentinel product, which is closed source and limited to Terraform Enterprise and Terraform Cloud. Sentinel also requires the use of a proprietary HashiCorp Sentinel Language. Pulumi, however, provides policy as code through CrossGuard which acts as programmable guardrails to enforce security, best practices, and cost across all infrastructure. CrossGuard is open source, free to use, and lets you write rules in Python, JavaScript, or Open Policy Agent (OPA) Rego. For more information on how to implement policy as code using Pulumi, see [Policy as Code ("CrossGuard")]({{< relref "/docs/guides/crossguard/" >}}).

### Secrets Management {#secrets}

Pulumi always transmits and stores entire state files securely. However, Pulumi also supports encrypting sensitive values (e.g., database passwords, SaaS tokens, credentials files)  as secrets for extra protection. Secrets are supported as a first-class primitive within Pulumi.  Pulumi encrypts secrets in transit and at rest, and anything a secret touches (e.g., CLI outputs, Pulumi logs, Pulumi program, state file) is tainted and gets encrypted, which prevents you from accidentally disclosing a secret. Every stack has its own encryption key. Pulumi also provides an extensible encryption facility that allows you to elect to use your own keys managed by a 3rd party solution. Terraform manages secrets through Vault, a separate product. However, even when pulling secrets from Vault, secrets are stored as plaintext and not encrypted within the state file. For more information on storing secrets with Pulumi, see [Secrets]({{< relref "/docs/intro/concepts/secrets" >}}).

### Audit Capabilities {#auditing}

Pulumi provides audit logs that enable you to track the activity of users within an organization. Audit logs capture the UNIX timestamp of the event, the user who invoked the action, the event that took place, and the source IP of the call the user made. These logs are available to organizations with an Enterprise level subscription. The logs are immutable and record all user actions. Terraform Cloud only provides a stream of audit events that describe changes throughout an organization with 14 days of retention. To learn more, see [Audit Logs]({{< relref "/docs/intro/pulumi-service/audit-logs" >}}).

### Adopt Existing Resources {#adopting}

Both Pulumi and Terraform support importing existing resources so that they can be managed by each. Pulumi also allows you to generate code in your language of choice from the existing state. Terraform only supports importing state but requires you to hand-author the HCL. To learn more, see [Importing Infrastructure]({{< relref "/docs/guides/adopting/import" >}}) in our Adopting Pulumi user guide.

### Aliases

Aliases help facilitate refactoring by allowing you to modify certain properties of a resource without risk of replacing it. With an alias, you can change the logical name of a given resource, change its parent (i.e., move it from one component to another), change its underlying resource type, or even move it to an entirely different project or stack. Both Pulumi and Terraform support the notion of resource renaming and reparenting, but Terraform does not currently support declaratively changing a resource's underlying type or moving it to another workspace. To learn more, see [Aliases]({{< relref "/docs/intro/concepts/resources/options/aliases" >}}) in the Resource documentation.

### Transformations

Transformations, which are unique to Pulumi, allow you to programmatically set or override the input properties of resources belonging to a particular collection, such as the child resources of a Pulumi component or even all of the resources belonging to a stack. Transformations make it easy to apply consistent settings across your infrastructure without having to manipulate the properties of individual resources. To learn more, see [Transformations]({{< relref "docs/intro/concepts/resources/options/transformations" >}}) in the Resource documentation.

### Import Code from Other IaC Tools {#converting}

Pulumi allows you to convert templates by Terraform HCL , Kubernetes YAML, and Azure ARM into Pulumi programs. This preserves existing program structure, which may be important if you carefully designed your existing infrastructure as code layout in terms of names, modules, and configurability. Conversion takes care of the static program structure and will automatically generate a new, fully-functional Pulumi program that matches the source infrastructure as code program. To learn more, see [Conversion]({{< relref "/docs/guides/adopting/#conversion" >}}) in our Adopting Pulumi user guide.
