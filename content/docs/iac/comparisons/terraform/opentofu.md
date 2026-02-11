---
title_tag: "OpenTofu vs. Terraform"
meta_desc: Compare and contrast OpenTofu and Terraform across key features. Learn how they differ and why many teams are migrating to Pulumi.
title: OpenTofu vs. Terraform
h1: OpenTofu vs. Terraform
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: OpenTofu vs. Terraform
        parent: iac-comparisons-terraform
        weight: 2
    concepts:
        parent: vs-terraform
        weight: 2
aliases:
    - /docs/intro/vs/terraform/opentofu/
    - /docs/concepts/vs/terraform/opentofu/
    - /docs/iac/concepts/vs/terraform/opentofu/
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

OpenTofu and Terraform are both infrastructure as code technologies that have similarities but fundamental differences. They both provide infrastructure as code software for cloud service management with a consistent CLI workflow. They allow you to write, plan, and apply changes to deliver infrastructure as code. In this comprehensive guide, we'll explore their key differences and similarities to help you choose the right infrastructure as code platform to meet your needs.

## OpenTofu vs. Terraform: Similarities {#similarities}

OpenTofu is a fork of Terraform 1.6.x so there are many similarities for now. They both have the ability to create, deploy, and manage infrastructure as code on any cloud. Both Terraform and OpenTofu follow a desired state infrastructure as code model, where the IaC code represents the desired state of the infrastructure. The deployment engine compares this desired state with the current state of the stack and determines the necessary actions, such as creating, updating, or deleting resources. Both Terraform and OpenTofu support many cloud providers, including [AWS](/aws/), [Azure](/azure/), and [Google Cloud](/gcp/), plus other services like CloudFlare, Digital Ocean, and more. They also both require the use of a domain-specific language: HashiCorp Configuration Language (HCL).

## OpenTofu vs. Terraform: Key Differences {#differences}

OpenTofu and Terraform differ in that Terraform is not open source, using the [Business Source License](https://github.com/HashiCorp/terraform/blob/main/LICENSE) model. OpenTofu, however, uses the weak copyleft [Mozilla Public License 2.0](https://github.com/opentofu/opentofu/blob/main/LICENSE). Terraform also has a paid offering called Terraform Cloud, a fully managed SaaS service that version controls and manages Terraform state. Terraform Cloud also provides access to remote operations, policy as code, and audit logging. OpenTofu is supported by env0 and Spacelift SaaS services for managing Terraform state. As Terraform and OpenTofu continue to diverge, more key differences will emerge.

Here is a summary of the key differences between OpenTofu and Terraform:

| Feature | OpenTofu | Terraform |
| ------- | ------ | --------- |
| [OSS License](#license) | Yes, Mozilla Public License 2.0 | No, Business Source License 1.1 |
| [Language Support](#language) | HashiCorp Configuration Language (HCL) | HashiCorp Configuration Language (HCL) |
| [IDE Support](#ide) | Limited | Limited |
| [State Management](#state) | Self-managed by default, managed SaaS offering available. | Self-managed by default, managed SaaS offerings available. |
| [Provider Support](#providers) | Support across multiple IaaS, SaaS, and PaaS providers. | Support across multiple IaaS, SaaS, and PaaS providers. |
| [Cloud Native Support](#cloud-native) | Core API typed. Generic support for CRD. | Core API typed. Generic support for CRD. |
| [Dynamic Provider Support](#dynamic-providers) | No | No |
| [Infrastructure Reuse and Modularity](#reuse) | Constrained. Can only reuse OpenTofu modules. | Constrained. Can only reuse Terraform modules. |
| [Testing and Validation](#testing) | Integration testing only. | Integration testing only. |
| [Modes of Execution](#modes) | Run CLI commands only. | Run CLI commands or perform remote runs with SaaS offering. |
| [Embed within Application Code](#embedding) | No | No |
| [Third-party CI/CD Tools Support](#cicd) | No | Yes |
| [Policy as Code](#policy) | No | Yes |
| [Secrets Management](#secrets) | No. Secrets can be stored in a 3rd party product. There is no way to encrypt them in the state file. | No. Secrets are stored in a  separate product (Vault). There is no way to encrypt them in the state file. |
| [Audit Capabilities](#auditing) | No | Limited |
| [Adopt Existing Resources](#adopting) | Yes. No code generation capabilities. | Yes. No code generation capabilities. |
| [Aliases](#aliases) | Limited | Limited |
| [Transformations](#transformations) | No | No |
| [Import Code from other IaC Tools](#converting) | No | No |

Are you constrained by Terraform or OpenTofu? Let us help you migrate to Pulumi so you can have greater developer productivity, ability to scale, and delivery velocity. Follow our comprehensive guides in our [Migration Hub](/blog/migration-hub/) or work with our [Expert Services teams](/contact?form=tf-migration) that can help you with migration and training. If you would like to deploy a simple program, follow our Get Started guide:

{{< get-started >}}

## Pulumi: Terraform and OpenTofu Alternative

The following sections provide a detailed explanation of why Pulumi is a better alternative to both Terraform and OpenTofu.

### OSS License {#license}

Pulumi open-source projects use the permissive and business-friendly [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE). This includes the core [Pulumi repo](https://github.com/pulumi/pulumi), all of the open-source Pulumi resource providers (such as the [Azure Native provider](https://github.com/pulumi/pulumi-azure-native)), and other useful projects.

### Language Support {#language}

Pulumi enables you to build infrastructure using familiar programming languages such as Python, Go, JavaScript, TypeScript, C#, and Java. By using these established languages, you gain access to common constructs like loops, conditionals, functions, and classes—making it easier to reduce boilerplate and enforce best practices. These languages have been refined over decades to manage complexity at scale, which aligns perfectly with the challenges of today’s globally distributed cloud systems. Rather than introducing a new module ecosystem, Pulumi allows you to use existing package managers and development workflows you’re already comfortable with.

### IDE Support {#ide}

Pulumi lets you take advantage of decades of innovation in modern IDEs. These tools offer features like intelligent code completion, type checking, inline error highlighting, and integrated resource documentation—all designed to boost developer productivity.

### State Management {#state}

With Pulumi, you use general purpose languages to express desired state, and Pulumi’s engine similarly gives you diffs and a way to robustly update your infrastructure. It uses the free [Pulumi Cloud](https://app.pulumi.com/) to eliminate concerns around concurrency management requirements and state manually by way of "state files". This makes getting started with Pulumi, and operationalizing it in a team setting, much easier. For advanced use cases, it is possible to [use Pulumi without Pulumi Cloud](/docs/support/faq#can-i-use-pulumi-without-depending-on-the-/pulumi-cloud/), which works a lot more like Terraform, but requires you to manage state and concurrency issues. Pulumi errs on the side of ease-of-use.

For more information on how Pulumi manages state or how to use different backends, see [State and Backends](/docs/concepts/state/).

### Provider Support {#providers}

Pulumi supports over 150 of the leading cloud providers and modern cloud SaaS offerings including Amazon Web Services, Microsoft Azure, Google Cloud, Kubernetes, Auth0, CloudFlare, Confluent Cloud, Datadog, DigitalOcean, Docker, GitHub, Kong, MinIO, MongoDB Atlas, PagerDuty, Snowflake, Spot by NetApp, and SumoLogic. Pulumi also has [native providers](/blog/pulumiup-native-providers/) for AWS, Azure, Google, and Kubernetes that provide same-day support for every new release. For more information on Pulumi providers, see [Pulumi Registry](/registry/).

Pulumi also has deep support for cloud native technologies like Kubernetes, and supports advanced deployment scenarios that cannot be expressed with Terraform Cloud. This includes Prometheus-based canaries, automatic Envoy sidecar injection, and more. Pulumi is a proud member of the Cloud Native Computing Foundation (CNCF).

### Cloud Native Support {#cloud-native}

Pulumi integrates with the cloud native ecosystem. It provides a native Kubernetes provider with complete Kubernetes API coverage across all supported languages, along with compile-time type-checking. Pulumi supports both Helm 2 and 3, strongly typed CustomResourceDefinitions (CRDs), deployment of Kubernetes YAML or Kustomize templates, and includes a YAML-to-Pulumi converter to transform any Kubernetes YAML into your chosen language. It also offers playbooks that incorporate best practices for production cluster deployments on AWS EKS, Azure AKS, and Google GKE. Additionally, Pulumi includes a Kubernetes operator that enables continuous delivery through GitOps without generic CRD support that lacks compile-time type-checking and auto-complete.

### Dynamic Provider Support {#dynamic-providers}

Pulumi supports dynamic providers, enabling you to create new types of custom resources by directly implementing CRUD operations within your Pulumi program. This allows you to define new resource types and handle complex integrations—such as database migrations or virtual machine configuration management—within the same infrastructure as code workflow. Terraform does not offer a direct equivalent to dynamic providers; implementing custom resources with CRUD operations would require building complex and proprietary modules. To learn more, see [Dynamic Providers](/docs/concepts/resources/dynamic-providers/).

### Infrastructure Reuse and Modularity {#reuse}

Pulumi promotes creating reusable and modular components which allows standard and well-architected infrastructure building blocks to be templatized and easily reused. With Pulumi, you can reuse functions, classes, and packages. Pulumi also has a built-in component model that lets you abstract and encapsulate complexity with higher-level abstractions. These components have a trackable state, appear in diffs, and use a logical name that tracks the resource identity across deployments. Pulumi also provides Pulumi Packages which allows you to author components in one language and make the component accessible in all the other languages that Pulumi supports. For more information about how to author reusable components, see [Component Resources](/docs/concepts/resources/#components).

Pulumi also provides the [Pulumi Registry](/registry/) which is a searchable collection of Pulumi Packages published by Pulumi and our partners. With Pulumi Registry, you can easily find the package with the resources you need, install that package directly into your project, and start building.

### Testing and Validation {#testing}

With Pulumi, you can use native testing frameworks to automate infrastructure testing, thanks to its use of general-purpose programming languages for provisioning cloud resources. Pulumi supports unit tests (fast, in-memory tests that mock external calls), property tests (which run resource-level assertions during deployment), and integration tests (which deploy temporary infrastructure and run external tests against it). For more details on testing with Pulumi, see [Testing](/docs/using-pulumi/testing/).

### Modes of Execution {#modes}

Pulumi supports command execution through the CLI and offers two APIs for running Pulumi commands. The first is the Automation API, which lets you provision, update, and destroy infrastructure directly from your application code—enabling advanced orchestration workflows and dynamic infrastructure management. The second is the REST API, which provides access to state information, history, and stack tags when using the Managed Pulumi Cloud. To learn more, see [Automation API](/docs/using-pulumi/automation-api/) and [REST API](/docs/pulumi-cloud/cloud-rest-api/).

### Embed within Application Code {#embedding}

Pulumi allows you to embed Pulumi programs directly within your application code using the Automation API—a programmatic interface for running Pulumi programs without relying on the CLI. The Automation API offers a strongly typed and safe approach for using Pulumi in embedded scenarios, such as web servers, without invoking the CLI. It enables you to build custom experiences on top of Pulumi that fit your specific use case, domain, and team needs. To learn more, see [Automation API](/docs/using-pulumi/automation-api/).

### Third-Party CI/CD Tools Support {#cicd}

Pulumi integrates with existing CI/CD providers, including AWS Code Services, Azure DevOps, CircleCI, CodeFresh, GitHub Actions, GitLab Pipelines, Google Cloud Build, Jenkins, Octopus Deploy, JetBrains TeamCity, Spinnaker, and Travis. Pulumi allows you to use the same CI/CD system for your infrastructure as your application code. For more information on how to integrate your CI/CD system with Pulumi, see [Continuous Delivery](/docs/using-pulumi/continuous-delivery/).

### Policy as Code {#policy}

Pulumi provides policy as code through Pulumi Policies which acts as programmable guardrails to enforce security, best practices, and cost across all infrastructure. Pulumi Policies is open source, free to use, and lets you write rules in Python, JavaScript, or Open Policy Agent (OPA) Rego. For more information on how to implement policy as code using Pulumi, see [Pulumi Policies](/docs/insights/policy/).

### Secrets Management {#secrets}

Pulumi securely transmits and stores full state files at all times. In addition, it supports encrypting sensitive values—such as database passwords, SaaS tokens, and credential files—as secrets for enhanced protection. Secrets are treated as a first-class feature in Pulumi. They are encrypted both in transit and at rest, and any component they interact with—such as CLI outputs, logs, the Pulumi program, or the state file—is marked and encrypted to prevent accidental exposure. Each stack uses its own encryption key, and Pulumi also offers an extensible encryption mechanism that lets you use your own keys managed by a third-party provider. For more information on storing secrets with Pulumi, see [Secrets](/docs/concepts/secrets/).

### Audit Capabilities {#auditing}

Pulumi offers audit logs that allow you to monitor user activity within an organization. These logs record the UNIX timestamp of each event, the user who performed the action, the specific event, and the source IP address of the request. Audit logs are immutable and capture all user actions. They are available to organizations with an Enterprise subscription. To learn more, see [Audit Logs](/docs/pulumi-cloud/audit-logs/).

### Adopt Existing Resources {#adopting}

Pulumi supports importing existing resources so that they can be managed. Pulumi also allows you to generate code in your language of choice from the existing state. To learn more, see [Importing Infrastructure](/docs/using-pulumi/adopting-pulumi/import/) in our Adopting Pulumi user guide.

### Aliases

Aliases help facilitate refactoring by allowing you to modify certain properties of a resource without risk of replacing it. With an alias, you can change the logical name of a given resource, change its parent (i.e., move it from one component to another), change its underlying resource type, or even move it to an entirely different project or stack. Pulumi supports the notion of resource renaming and reparenting, including declaratively changing a resource's underlying type or moving it to another workspace. To learn more, see [Aliases](/docs/concepts/options/aliases/) in the Resource documentation.

### Transformations

Transformations, which are unique to Pulumi, allow you to programmatically set or override the input properties of resources belonging to a particular collection, such as the child resources of a Pulumi component or even all of the resources belonging to a stack. Transformations make it easy to apply consistent settings across your infrastructure without having to manipulate the properties of individual resources. To learn more, see [Transformations](/docs/concepts/options/transformations/) in the Resource documentation.

### Import Code from Other IaC Tools {#converting}

Pulumi allows you to convert templates by Terraform HCL, Kubernetes YAML, and Azure ARM into Pulumi programs. This preserves the existing program structure, which may be important if you carefully designed your existing infrastructure as code layout in terms of names, modules, and configurability. Conversion takes care of the static program structure and will automatically generate a new, fully-functional Pulumi program that matches the source infrastructure as code program. To learn more, see [Conversion](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/#conversion) in our Adopting Pulumi user guide.

## Get Started with Pulumi

Pulumi’s Infrastructure as Code platform supports the widest range of builders, clouds, programming languages, and cloud architectures available today. [Get started today](/docs/get-started/).
