---
title_tag: "Terraform vs. Pulumi IaC"
meta_desc: Pulumi IaC and Terraform have many similarities, and yet they differ in many key ways. This page helps provide a rundown of Pulumi's advantages.
title: Terraform
h1: Terraform vs. Pulumi IaC
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Terraform
        parent: iac-comparisons
        weight: 1
        identifier: iac-comparisons-terraform
    concepts:
        identifier: vs-terraform
        parent: vs
        weight: 1
aliases:
- /docs/reference/vs/terraform/
- /docs/intro/vs/terraform/
- /docs/concepts/vs/terraform/
- /docs/iac/concepts/vs/terraform/
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

{{< youtube "v2XMEZ_LeCY?rel=0" >}}

## Infrastructure Management as Powerful as Your Applications

Pulumi IaC lets you write infrastructure as code in any programming language and deploy to any cloud. Terraform requires learning HCL, a DSL that optimizes for simplicity at the expense of flexibility and scale. Instead, Pulumi IaC integrates into the existing coding tools and workflows you already know while also providing performance, scalability, ease of use and more.

With Pulumi IaC, you can:

- Write infrastructure code in languages like Python, TypeScript, Java, .NET, Go, and more
- Get full IDE support with code completion and error checking
- Use your language's entire ecosystem of libraries and tools to create custom resources or reusable infrastructure components
- Invoke execution via CLI, APIs, or embed infrastructure management in your applications

## At a Glance

**Terraform**

- Uses proprietary domain specific language (HCL)
- Secrets are not encrypted by default (requires Vault)
- When cloud providers release new features, you must wait for community supported providers to integrate them
- Is not considered open source (Business Source License)

**Pulumi IaC**

- Uses mainstream programming languages
- Secrets are encrypted by default (no additional tools)
- Use of native cloud providers means that you don't have to wait for new features to be integrated
- Is fully open source (Apache 2.0)

**Key Differences**

- Low barrier for entry and adoption by developers
- Built-in testing and supports popular testing frameworks
- Advanced automation capabilities
- Enhanced security with built-in secret encryption
- Full IDE support with code completion and type checking
- Automatic resource naming to prevent naming conflicts across stacks
- Zero-downtime replacements using create-before-delete semantics

## What is Pulumi?

Pulumi is an open source [infrastructure as code](/what-is/what-is-infrastructure-as-code/) platform that helps teams tame the cloud’s complexity using the world’s most popular programming languages (TypeScript, Go, .NET, Python, Java, etc) and markup languages (YAML, CUE).

## What is Terraform?

Terraform Cloud provides infrastructure as code software for cloud service management with a consistent CLI workflow. Terraform allows you to write, plan, and apply changes to deliver infrastructure as code.

## An In-Depth Look

Pulumi IaC and Terraform are both infrastructure as code tools for DevOps teams. They have many similarities, but also fundamentally differ. When considering which tool is best for your organization, it helps to examine their design and optimized use cases. Terraform uses a domain-specific language (DSL), which is simpler for beginners but can become complex and hard to maintain. Pulumi IaC uses mainstream programming languages, which are more scalable and widely adopted but may have a steeper learning curve. Pulumi IaC is better for developers familiar with programming, while Terraform is more suited to those new to code.

Terraform’s DSL (known as HCL) helps non-programmers express complex logic and system interactions. Early in the shift to DevOps, DSLs were a good choice to appeal to operators who were new to the world of working in code. However, DSLs make tradeoffs optimizing for simplicity and getting started that can become problematic over time. While DSLs can simplify specific tasks, their lack of clear, standard structures and common functionality tend to create maintenance, support, and portability issues. That rigidity often leads to increased complexity that typically results in low organizational adoption.

In contrast, Pulumi IaC integrates into mainstream programming languages which have sophisticated structures, common functionality, and have been optimized (often for decades) for a high degree of portability and maintainability. That tradeoff is made in order to build for scalability, long-term support, and a high degree of organizational adoption. Pulumi IaC’s approach appeals to developers who are new to the world of infrastructure. In an age when DevOps practices have become ubiquitous and many operators are no longer new to programming, modern tools can benefit from rethinking past constraints. Pulumi IaC is widely accessible to both developers and DevOps engineers from any background, although some non-programmers may take slightly longer to get started.

There are additional similarities and key differences. In this comprehensive guide, we’ll explore both using real-world scenarios and map Terraform concepts to Pulumi IaC. We hope this guide helps you choose the right IaC tool best suited to your needs.

### Real World Scenarios

Pulumi IaC’s deep integration with mainstream programming languages isn’t just about syntax preferences – it’s about unlocking the full power of modern software development. Terraform HCL lacks processing constructs like loops, if statements, objects to encapsulate variables, abstractions, and other functionality commonly found in programming languages. Practicing “Don’t Repeat Yourself” (or DRY) principles with HCL is incredibly difficult for most teams and it’s common for Terraform code bases to span tens of thousands of lines in length, with often unreadable amounts of complexity baked in over many churned years of maintenance.

Alternately, consider just a few of the choices that can be made in Pulumi IaC when full programming languages are available:

- **Python**: Leverage NumPy for calculations, Pandas for data processing
- **TypeScript/JavaScript**: Use npm packages, async/await for complex orchestration
- **Java**: Utilize enterprise-grade frameworks and tools
- **Go**: Access powerful concurrency features and standard library
- **.NET**: Integrate with existing enterprise .NET ecosystems
- **YAML**: Available for teams preferring simpler configurations

The freedom and benefits gained when using true programming languages are large fundamental differences with a wealth of additional impacts. For now, let's consider a condensed list of other real world scenarios where differences present themselves.

### Workflow and Developer Experience

- Full IDE support with code completion and error detection
- Pulumi provided test framework (unit, property, and integration tests)
- Support for other popular testing frameworks
- Create new custom resources by directly coding CRUD operations in Dynamic Providers
- Transformations allow you to apply consistent settings across your infrastructure without having to manipulate individual resources

### Cloud Native Power

- Kubernetes provider with 100% K8s API coverage and type checking
- Native support for Helm 2 and Helm 3
- Built-in conversion for YAML to Pulumi IaC code in your desired language
- Pulumi Kubernetes operator for GitOps workflows

### Enterprise-Ready

- Reusable & modular infrastructure components for governance in your Internal Developer Portal
- Compliance via Audit logs to track things like user activity
- Encrypted secrets in transit and rest (by default)
- Policy as Code enforces best practices in your desired programming language

### Migration and Integration

Pulumi IaC’s extensibility also enables cross functionality with Terraform

- Built-in converters to migrate Terraform HCL code to Pulumi IaC
- Reference existing Terraform state with Pulumi IaC
- Enterprise support for Bundled Terraform workspace migrations
- Pulumi support for migration services and training

## Feature by Feature Comparison

The high level consideration of product design and real world use cases are illustrative for big picture context. A closer examination of individual features can also draw out key fundamental differences and similarities.

Here is a summary of more granular comparisons between Pulumi and Terraform:

| Feature | Pulumi | Terraform |
| ------- | ------ | --------- |
| [Language Support](#language) | Python, TypeScript, JavaScript, Go, C#, F#, Java, YAML | HashiCorp Configuration Language (HCL) |
| [IDE Support](#ide) | Code completion, strong typing, error squiggles, rich resource documentation, etc. | Limited |
| [Testing and Validation](#testing) | Unit, property, and integration testing.<br>Supports popular test frameworks. | Integration testing only |
| [CI/CD Pipeline Support](#cicd) | Yes | Yes |
| [Infrastructure Providers](#providers) | Native cloud providers with 100% same-day resource coverage and turn-key access to any Terraform providers | Support across multiple IaaS, SaaS, and PaaS providers |
| [Declarative Infrastructure as Code](#declarative) | Yes | Yes |
| [Cloud Native Support](#cloud-native) | Richly typed across 100% of K8s API<br>Includes CRDs & in-cluster operator support for GitOps delivery | Core API typed<br>Generic support for CRD |
| [Custom Resource Providers](#dynamic-providers) | Yes | No |
| [Modular Resource Components](#reuse) | Flexible<br>Reuse functions, classes, packages, and Pulumi components | Constrained<br>Can only reuse Terraform modules |
| [Execution Modes](#modes) | Run CLI commands<br>Remote execution via SaaS<br>Programmatically via Automation API | Run CLI commands<br>Remote execution via SaaS |
| [Embed IaC Execution in Application Code](#embedding) | Yes | No |
| [Import Code from other IaC Tools](#converting) | Yes | No |
| [Adopt Existing Resources](#adopting) | Yes<br>Generates code as part of the import process | Yes<br>No code generation capabilities |
| [Aliases](#aliases) | Yes | Limited |
| [Transformations](#transformations) | Yes | No |
| [State Management](#state) | Managed through Pulumi Cloud by default<br>Self-managed options available | Self-managed by default<br>Managed via SaaS offering available |
| [Encrypted Secrets by default](#secrets) | Yes<br>Secrets are encrypted both in transit and at rest in the state file | No<br>Secrets are stored in a separate product (Vault)<br>Cannot encrypt secrets in the state file |
| [Policy as Code](#policy) | Yes | Yes |
| [Audit Capabilities](#auditing) | Yes | Limited |
| [Open Source](#license) | Yes<br>Apache License 2.0 | No<br>Business Source License 1.1 |

Getting started with Pulumi IaC is easy, especially if you have prior experience with Terraform. If you already have Terraform HCL code, you can convert it to Pulumi IaC. Follow the comprehensive guides in the [Migration Hub](/blog/migration-hub/) to use our [self-service migration tools](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-terraform/) or work with our [Expert Services teams](/contact?form=tf-migration) that can help you with migration and training. As part of Pulumi Enterprise and Business Critical Editions, [Terraform workspace migrations](/blog/tf-migration-offer) are bundled as part of the onboarding process.

If you’re new to infrastructure as code, or don’t have existing HCL code, just follow the getting started guide below.

## Get Started with Pulumi IaC

If you would like to see how other Pulumi customers have migrated from Terraform to Pulumi IaC, see the [Atlassian case study](/case-studies/atlassian/) and the [Green Park Sports case study](/case-studies/greenpark-sports/). If you would like to deploy a simple program, follow the Get Started guide:

{{< get-started >}}

---

<br>

The following sections go into further detail on the differences between Pulumi and Terraform.

### Language Support {#language}

Terraform requires you and your team to write programs in a custom domain-specific language (DSL) called HashiCorp Configuration Language (HCL). In contrast, Pulumi IaC lets you use programming languages like Python, Go, JavaScript, TypeScript, C#, and Java. Because of the use of familiar languages, you get familiar constructs like conditionals, loops, functions, and classes. This significantly improves the ability to reduce boilerplate and enforce best practices. With HCL, it is common to copy and paste blocks of HCL code between different projects. Pulumi IaC’s supported programming languages have been built over multiple decades to tame complexity at scale—the very complexity modern cloud architectures operating at global scale need to tackle. Instead of creating a bespoke ecosystem of modules and sharing, Pulumi IaC lets you leverage existing package management tools and techniques.

### IDE Support {#ide}

Terraform has plugins for some IDEs. However, the features are varied and limited. With Pulumi IaC, you can tap into decades of innovation and refinement with any IDE. The IDEs automatically provide code completion, strong typing, error squiggles, rich resource documentation, and more.

### Testing and Validation {#testing}

Terraform supports integration testing. With Pulumi IaC, you can take advantage of native testing frameworks and perform automated tests of your infrastructure because Pulumi IaC uses general purpose programming languages to provision cloud resources. Pulumi provides unit tests (fast in-memory tests that mock all external calls), property tests (run resource-level assertions while infrastructure is being deployed), and integration tests (deploy ephemeral infrastructure and run external tests against it). For more information on how to run tests with Pulumi IaC, see [Testing](/docs/using-pulumi/testing/).

### CI/CD Pipeline Support {#cicd}

Pulumi IaC integrates with existing CI/CD providers, including AWS Code Services, Azure DevOps, CircleCI, CodeFresh, GitHub Actions, GitLab Pipelines, Google Cloud Build, Jenkins, Octopus Deploy, JetBrains TeamCity, Spinnaker, and Travis. Pulumi IaC allows you to use the same CI/CD system for your infrastructure as your application code. Terraform has similar support with existing CI/CD providers.

For more information on how to integrate your CI/CD system with Pulumi IaC, see [Continuous Delivery](/docs/using-pulumi/continuous-delivery/).

### Infrastructure Providers {#providers}

Pulumi IaC supports over 150 of the leading cloud providers and modern cloud SaaS offerings including Amazon Web Services, Microsoft Azure, Google Cloud, Kubernetes, Auth0, CloudFlare, Confluent Cloud, Datadog, DigitalOcean, Docker, GitHub, Kong, MinIO, MongoDB Atlas, PagerDuty, Snowflake, Spot by NetApp, and SumoLogic. Pulumi IaC also has [native providers](/blog/pulumiup-native-providers/) for AWS, Azure, Google, and Kubernetes that provide same-day support for every new release. For more information on Pulumi IaC providers, see [Pulumi Registry](/registry/).

Pulumi IaC also has deep support for cloud native technologies like Kubernetes, and supports advanced deployment scenarios that cannot be expressed with Terraform Cloud. This includes Prometheus-based canaries, automatic Envoy sidecar injection, and more. Pulumi is a proud member of the Cloud Native Computing Foundation (CNCF).

### Declarative Infrastructure as Code {#declarative}

Declarative Infrastructure as Code (IaC) defines the desired state of infrastructure without specifying the exact steps to achieve it. It focuses on what the infrastructure should look like, rather than how to get there. Key aspects include a focus on the end state, idempotency, simplified maintenance, reduced configuration drift, and abstraction of complexity. Benefits include consistency, repeatability, efficiency, version control, and collaboration. Both Terraform and Pulumi IaC use a declarative model for managing infrastructure.

### Resource Management and Deployment Workflow {#resource-management}

Pulumi provides intelligent resource management features that minimize downtime and prevent common infrastructure pitfalls.

**Automatic Resource Naming**

Pulumi automatically appends a random suffix to most resource names (for example, `my-bucket` becomes `my-bucket-a1b2c3d`). This auto-naming behavior serves two critical purposes:

1. **Collision prevention across stacks**: Multiple stacks of the same project can coexist without resource name conflicts, making it easy to create separate development, staging, and production environments or to deploy the same infrastructure across multiple regions.

1. **Zero-downtime replacements**: Auto-naming enables Pulumi to create replacement resources before deleting old ones, ensuring continuous availability during updates.

While Terraform requires you to manually ensure unique names across workspaces (often using interpolation with workspace names or random suffixes), Pulumi handles this automatically. You can override auto-naming when specific names are required, but the default behavior optimizes for reliability and multi-stack workflows.

For more details, see [Resource Names](/docs/iac/concepts/resources/names/).

**Create-before-delete replacement strategy**

When a resource needs to be replaced rather than updated in place, Pulumi creates the new resource first, updates any references to point to the new resource, and only then deletes the old resource. This create-before-delete approach minimizes downtime and reduces the risk of service interruption during infrastructure updates.

Terraform typically uses a delete-before-create strategy, which can cause downtime during replacements. While Terraform offers a `create_before_destroy` lifecycle setting, it must be explicitly configured on each resource and comes with limitations. Pulumi makes create-before-delete the default behavior, ensuring zero-downtime deployments without additional configuration.

In cases where create-before-delete is not desired, you can explicitly opt into delete-before-replace semantics using the [`deleteBeforeReplace` resource option](/docs/iac/concepts/resources/options/deletebeforereplace/).

### Cloud Native Support {#cloud-native}

Pulumi IaC supports the cloud native ecosystem. This includes a native Kubernetes provider with 100% Kubernetes API coverage in all languages, including compile-time type-checking. Pulumi IaC also includes Helm 2 and 3 support, strongly typed CustomResourceDefinitions (CRDs), deploying Kubernetes YAML or Kustomize templates, as well as a YAML-to-Pulumi IaC conversion tool that can translate any Kubernetes YAML into your desired language. Pulumi IaC also offers playbooks with built-in best practices for production cluster deployments for AWS EKS, Azure AKS, and Google GKE. Pulumi IaC also offers a Kubernetes operator that allows you to continuously deliver via GitOps. Terraform offers similar support for the Kubernetes core API and Helm but has generic support for CRDs, meaning no compile-time type-checking or auto-complete.

### Custom Resource Providers {#dynamic-providers}

Pulumi IaC provides dynamic providers that allow you to extend your system by creating new kinds of custom resources by directly coding CRUD operations for the new resource in your Pulumi program. This can be used to support new resource types in addition to performing complex integrations like database migrations, configuration management for virtual machines, and more, all orchestrated alongside your IaC workflows. Terraform does not have a direct equivalent to Dynamic Providers and would require writing complex and proprietary modules in order to build custom resources with CRUD operations. To learn more, see [Dynamic Providers](/docs/concepts/resources/dynamic-providers/).

### Modular Resource Components {#reuse}

Pulumi IaC promotes creating reusable and modular components which allows standard and well-architected infrastructure building blocks to be templatized and easily reused. With Pulumi IaC, you can reuse functions, classes, and packages. Pulumi IaC also has a built-in component model that lets you abstract and encapsulate complexity with higher-level abstractions. These components have a trackable state, appear in diffs, and use a logical name that tracks the resource identity across deployments. Pulumi IaC also provides Pulumi Packages which allows you to author components in one language and make the component accessible in all the other languages that Pulumi IaC supports. Terraform uses HCL which requires you to build proprietary modules and Go-based providers in order to build modular and reusable infrastructure. For more information about how to author reusable components, see [Component Resources](/docs/concepts/resources/#components).

Pulumi IaC also provides the [Pulumi Registry](/registry/) which is a searchable collection of Pulumi Packages published by Pulumi and our partners. With Pulumi Registry, you can easily find the package with the resources you need, install that package directly into your project, and start building.

### Execution Modes {#modes}

Both Pulumi IaC and Terraform can execute commands through their CLI. Terraform can also do remote operations through Terraform Cloud. Pulumi IaC also provides two APIs by which you can execute Pulumi commands. First, the Automation API allows you to provision, update, and destroy infrastructure through Pulumi IaC directly in your application code. This enables higher order orchestration workflows and dynamically managed infrastructure. Second, the REST API allows you to query and interact with state information, history, and stack tags when using the Managed Pulumi Cloud. To learn more, see [Automation API](/docs/using-pulumi/automation-api/) and [REST API](/docs/pulumi-cloud/cloud-rest-api/).

### Embed IaC Management in Application Code {#embedding}

Pulumi IaC has the ability to embed Pulumi programs directly into your application code through the Automation API, a programmatic interface for running Pulumi programs without the Pulumi CLI. The Automation API is a strongly typed and safe way to use Pulumi IaC in embedded contexts such as web servers without having to shell out to a CLI. You can easily create custom experiences on top of Pulumi IaC that are tailored to your use-case, domain, and team. Terraform Cloud does not have an equivalent to Automation API. To learn more, see [Automation API](/docs/using-pulumi/automation-api/).

### Import Code from Other IaC Tools {#converting}

Pulumi IaC allows you to convert templates by Terraform HCL, Kubernetes YAML, and Azure ARM into Pulumi programs. This preserves the existing program structure, which may be important if you carefully designed your existing infrastructure as code layout in terms of names, modules, and configurability. Conversion takes care of the static program structure and will automatically generate a new, fully-functional Pulumi program that matches the source infrastructure as code program. To learn more, see  [Conversion](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/#conversion) in the Adopting Pulumi IaC user guide.

### Adopt Existing Resources {#adopting}

Both Pulumi IaC and Terraform support importing existing resources so that they can be managed by each. Pulumi IaC also allows you to generate code in your language of choice from the existing state. Terraform only supports importing state but requires you to hand-author the HCL. To learn more, see [Importing Infrastructure](/docs/using-pulumi/adopting-pulumi/import/) in the Adopting Pulumi IaC user guide.

### Aliases

Aliases help facilitate refactoring by allowing you to modify certain properties of a resource without risk of replacing it. With an alias, you can change the logical name of a given resource, change its parent (i.e., move it from one component to another), change its underlying resource type, or even move it to an entirely different project or stack. Both Pulumi IaC and Terraform support the notion of resource renaming and reparenting, but Terraform Cloud does not currently support declaratively changing a resource's underlying type or moving it to another workspace. To learn more, see [Aliases](/docs/concepts/options/aliases/) in the Resource documentation.

### Transformations

Transformations, which are unique to Pulumi IaC, allow you to programmatically set or override the input properties of resources belonging to a particular collection, such as the child resources of a Pulumi IaC component or even all of the resources belonging to a stack. Transformations make it easy to apply consistent settings across your infrastructure without having to manipulate the properties of individual resources. To learn more, see [Transformations](/docs/concepts/options/transformations/) in the Resource documentation.

### State Management {#state}

The Terraform engine takes care of provisioning and updating resources. With Pulumi IaC, you use general purpose languages to express desired state, and Pulumi IaC’s engine similarly gives you diffs and a way to robustly update your infrastructure.

By default, Terraform requires that you manage concurrency and state manually, by way of its “state files.” Pulumi IaC, in contrast, uses the free [Pulumi Cloud](https://app.pulumi.com/) to eliminate these concerns. This makes getting started with Pulumi IaC, and operationalizing it in a team setting, much easier. For advanced use cases, it is possible to [use Pulumi IaC without Pulumi Cloud](/docs/support/faq#can-i-use-pulumi-without-depending-on-the-/pulumi-cloud/), which works a lot more like Terraform, but requires you to manage state and concurrency issues. Pulumi IaC errs on the side of ease-of-use.

For more information on how Pulumi IaC manages state or how to use different backends, see [State and Backends](/docs/concepts/state/).

#### Using Terraform Providers {#providers-terraform}

Pulumi IaC is able to adapt [any Terraform Provider](https://github.com/terraform-providers) for use, enabling management of any infrastructure supported by the Terraform Providers ecosystem using Pulumi IaC programs.

Some of Pulumi IaC’s most interesting providers have been created this way, delivering access to robust, tried-and-true infrastructure management. The Terraform Providers ecosystem is mature and healthy, and enjoys contributions from many cloud and infrastructure leaders across the industry, ourselves included.

We are proud to be building on the work of others, and contributing our own open source back to this vibrant ecosystem.

In the event you’d like to add new providers, or understand how this integration works, check out the
 [Pulumi Terraform bridge repo](https://github.com/pulumi/pulumi-terraform-bridge). This bridge is fully open source and makes it easy to create new Pulumi IaC providers out of existing Terraform Providers.

#### Converting From Terraform to Pulumi IaC {#providers-converting}

The Pulumi CLI can be used to convert Terraform HCL to Pulumi IaC via `pulumi convert --from terraform`. To learn more, see [Converting Terraform HCL to Pulumi IaC](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-terraform/#converting-terraform-hcl-to-pulumi) in the Adopting Pulumi IaC user guide.

For an example of how to do a Terraform-to-Pulumi conversion, see [Converting Full Terraform Programs to Pulumi](/blog/converting-full-terraform-programs-to-pulumi/).

#### Using Pulumi IaC and Terraform Side-by-Side {#providers-side-by-side}

Pulumi IaC supports [consuming local or remote Terraform state](/blog/using-terraform-remote-state-with-pulumi/) from your Pulumi programs. This helps with incremental adoption, whereby you continue managing a subset of your infrastructure with Terraform while you incrementally move to Pulumi IaC.

For example, maybe you would like to keep your VPC and low-level network definitions written in Terraform so as to avoid any disruption, or maybe some of the team would like to stay on Terraform for now and make a shift in the future. Using the state reference support described previously, you can author higher-level infrastructure in Pulumi IaC that consumes the Terraform-provisioned VPC information (such as the VPC ID, Subnet IDs, etc.), making the co-existence of Pulumi IaC and Terraform easy to automate.

To learn more, see [Referencing Terraform State](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-terraform/#referencing-terraform-state) in the Adopting Pulumi IaC user guide.

### Encrypted Secrets by Default {#secrets}

Pulumi IaC always transmits and stores entire state files securely. However, Pulumi IaC also supports encrypting sensitive values (e.g., database passwords, SaaS tokens, credentials files) as secrets for extra protection. Secrets are supported as a first-class primitive within Pulumi IaC. Pulumi IaC encrypts secrets in transit and at rest, and anything a secret touches (e.g., CLI outputs, Pulumi logs, Pulumi program, state file) is tainted and gets encrypted, which prevents you from accidentally disclosing a secret. Every stack has its own encryption key. Pulumi IaC also provides an extensible encryption facility that allows you to elect to use your own keys managed by a 3rd party solution. Terraform Cloud manages secrets through Vault, a separate product. However, even when pulling secrets from Vault, secrets are stored as plaintext and not encrypted within the state file. For more information on storing secrets with Pulumi IaC, see [Secrets](/docs/concepts/secrets/).

### Policy as Code {#policy}

Terraform provides policy as code through its Sentinel product, which is closed source and limited to Terraform Enterprise and Terraform Cloud. Sentinel also requires the use of a proprietary HashiCorp Sentinel Language. Pulumi IaC, however, provides policy as code through Pulumi Policies which acts as programmable guardrails to enforce security, best practices, and cost across all infrastructure. Pulumi Policies is open source, free to use, and lets you write rules in Python, JavaScript, or Open Policy Agent (OPA) Rego. For more information on how to implement policy as code using Pulumi IaC, see [Pulumi Policies](/docs/insights/policy/).

### Audit Capabilities {#auditing}

Pulumi IaC provides audit logs that enable you to track the activity of users within an organization. Audit logs capture the UNIX timestamp of the event, the user who invoked the action, the event that took place, and the source IP of the call the user made. These logs are available to organizations with an Enterprise level subscription. The logs are immutable and record all user actions. Terraform Cloud only provides a stream of audit events that describe changes throughout an organization with 14 days of retention. To learn more, see [Audit Logs](/docs/pulumi-cloud/audit-logs/).

### Open Source {#license}

Terraform uses the [Business Source License 1.1](https://github.com/HashiCorp/terraform/blob/main/LICENSE), which is not considered open source. Conversely, Pulumi open-source projects use the permissive and business-friendly [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE). This includes the core [Pulumi repo](https://github.com/pulumi/pulumi), all of the open-source Pulumi resource providers (such as the [Azure Native provider](https://github.com/pulumi/pulumi-azure-native)), and other useful projects.

## Try Pulumi IaC for Free

Pulumi’s Infrastructure as Code platform supports the widest range of builders, clouds, programming languages, and cloud architectures available. [Get started today](/docs/get-started/).
<!-- markdownlint-enable MD033 -->