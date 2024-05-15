---
title_tag: "Pulumi vs. AWS CloudFormation"
meta_desc: Pulumi and AWS CloudFormation share some similarities, but there are many key differences. Learn about these major differences here.
title: AWS CloudFormation
h1: Pulumi vs AWS CloudFormation
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    parent: vs
    weight: 2
aliases:
- /docs/intro/vs/cloud-templates/cloudformation/
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

Choosing the right infrastructure as code tool is important, and we want you to have as much information as possible to make the choice that best suits your needs. We've created this document to help you understand how Pulumi compares with AWS CloudFormation.

## What is CloudFormation?

CloudFormation is an AWS managed service that provisions AWS cloud resources using templates written in JSON or YAML. With CloudFormation, you write configuration code in template files describing the cloud resources you want to exist, then upload that code to the CloudFormation service for evaluation and deployment.

## Pulumi vs. CloudFormation: Similarities {#similarities}

Like CloudFormation, Pulumi is a declarative infrastructure-as-code platform that's built on the concept of _desired state_ and oriented around managing groups of related cloud resources called _stacks_. In both Pulumi and CloudFormation, desired state is expressed by declaring one or more cloud resources in code that's evaluated by the deployment engine, which in turn decides whether to create, update or destroy the resources of a given stack by comparing the stack's last known state with the new state expressed in the code.

## Pulumi vs. CloudFormation: Key Differences {#differences}

There are a couple of fundamental differences between CloudFormation and Pulumi.

First, a CloudFormation stack is a template file written in JSON or YAML, whereas a Pulumi stack is a program written in a general-purpose programming language like Python, TypeScript, C#, Go, and Java, or a markup language like YAML. CloudFormation resources are configured with simple key-value pairs, whereas in Pulumi, they're declared with programming constructs --- classes in object-oriented languages like Python or TypeScript, functions in languages like Go, and the like. Ultimately, this approach unlocks a great deal more flexibility in terms of expressing, composing, and managing cloud architectures.

Secondly, a CloudFormation deployment is performed out of band by the CloudFormation service (in response to a template file upload, for example), whereas a Pulumi deployment is performed by the Pulumi CLI itself, which communicates directly with the cloud provider to create, update, or destroy cloud resources as defined by your program. This approach provides not only a more interactive CLI experience but also a number of additional features like rich diffing, drift detection, and a tighter development loop that can often be several times faster than working with CloudFormation.

The following table summarizes some additional similarities and differences between Pulumi and CloudFormation, and the sections below the table go into more detail.

### Feature Comparisons

| Feature | Pulumi | CloudFormation |
| ------- | ------ | -------------- |
| [Language Support](#language) | TypeScript, JavaScript, Python, Go, C#, F#, VB.NET, Java, YAML | YAML or JSON only |
| [IDE Support](#ide) | IntelliSense, code completion, strong typing, error squiggles, rich documentation, interactive debugging, and more | Plugin-based |
| [State Management](#state) | Managed by Pulumi Cloud or with self-managed options | Managed by the AWS CloudFormation service |
| [Provider Support](#providers) | All major cloud providers supported, including 100% same-day coverage of new resources with [AWS Native](/registry/packages/aws-native/) | Third-party providers supported through CloudFormation Registry extensions |
| [Cloud Native Support](#cloud-native) | Richly typed support for the full cloud-native ecosystem and Kubernetes | AWS only |
| [Dynamic Provider Support](#dynamic-providers) | Yes | Limited |
| [OSS License](#license) | Apache License 2.0 | None |
| [Infrastructure Reuse and Modularity](#reuse) | Flexible and extensible: functions, classes, modules, Component Resources, multi-language packages, and more | Limited |
| [Testing and Validation](#testing) | Unit, property, and integration testing supported with popular test frameworks | Limited |
| [Modes of Execution](#modes) | Standard deployments performed with the Pulumi CLI, programmatic deployments through [Automation API](/automation/) | Deployments performed by the CloudFormation service |
| [Embed within Application Code](#embedding) | Yes, via [Automation API](/automation/) | No |
| [Third-party CI/CD Integration](#cicd) | Yes | Limited |
| [Policy as Code](#policy) | Yes | Limited |
| [Secrets Management](#secrets) | Built-in support for encrypted secrets, third-party providers supported as well | No built-in support, available through other services |
| [Drift Detection](#drift-detection) | Yes | Yes |
| [Stack Configuration and Deployment Environments](#configuration) | Yes | Limited |
| [Audit Capabilities](#auditing) | Yes | Yes |
| [Adopt Existing Resources](#adopting) | Yes, with code generation as part of the import process | Yes (manual) |
| [Convert Code from other IaC Tools](#converting) | Yes | No |
| [Resource Aliases](#aliases) | Yes | Limited |
| [Resource Transformations](#transformations) | Yes | No |

Getting started with Pulumi is easy if you already have experience with a general-purpose programming language. Follow our [Adopting Pulumi from AWS CloudFormation guide](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-aws/) or try our [CloudFormation conversion tool](/cf2pulumi/). To deploy a simple program, follow our Get Started guide:

{{< get-started >}}

### Language Support {#language}

CloudFormation templates are written in YAML or JSON, which can be easy to get started with, but cumbersome in practice and complex to maintain at scale. With Pulumi, you're able to use general-purpose programming languages like Python, Go, TypeScript, and C#, which not only allows you to manage complexity by using familiar programming constructs like loops, conditionals, functions, and classes, but also simplifies common configuration tasks like string interpolation or array manipulation that are awkward to express with CloudFormation intrinsic functions. First-class support for languages also means you can take full advantage of the entire ecosystem of your language of choice. For more information, see [Languages](/docs/languages-sdks/).

### IDE Support {#ide}

Many high-quality plugins are available to assist you with authoring CloudFormation templates, but in general they're limited to features like code snippets, syntax highlighting, and document validation. Because of its support for general-purpose programming languages, Pulumi allows you to take full advantage of all of the productivity features your IDE has to offer, like IntelliSense, code completion, syntax highlighting, inline documentation, rich typing, compile-time error checking, interactive debugging, code linting, automated refactoring, and more.

### State Management {#state}

Both Pulumi and CloudFormation provide built-in support for keeping track of the state of your infrastructure. By default, Pulumi uses the free Pulumi Cloud, which handles state management automatically, but you can also choose to manage your infrastructure state on your own, either by bringing your own storage mechanism (e.g., an S3 bucket, S3-compatible service, third-party blob storage, or just a flat file) or even self-hosting the Pulumi Cloud within your enterprise network. CloudFormation state is managed entirely within the CloudFormation service.

For more information on how Pulumi manages state, or using alternative backends, see [State and Backends](/docs/concepts/state/).

### Provider Support {#providers}

As an AWS product, CloudFormation offers limited support for third-party cloud providers, whereas Pulumi provides first-class support for more than 60 cloud and SaaS providers in addition to AWS, including Microsoft Azure, Google Cloud Platform, Kubernetes, Auth0, CloudFlare, Confluent Cloud, Datadog, DigitalOcean, Docker, GitHub, Kong, MinIO, MongoDB Atlas, PagerDuty, Snowflake, Spot by NetApp, SumoLogic, and many others.

Pulumi also has [native providers](/blog/pulumiup-native-providers/) for AWS, Azure, Google, and Kubernetes. Native providers are packages generated from cloud-provider API schemas that provide same-day support for new features as they're released.

For a full list of the providers we currently support, visit the [Pulumi Registry](/registry/). To learn more about how you can build providers of your own, see [Pulumi Packages](/docs/using-pulumi/pulumi-packages/) or [Dynamic Providers](/docs/concepts/resources/dynamic-providers/).

#### Extending Pulumi with Terraform Providers {#providers-terraform}

Pulumi is able to adapt [any Terraform provider](https://github.com/terraform-providers) for use with Pulumi, which allows you to manage any infrastructure supported by the Terraform Providers ecosystem with a Pulumi program.

Indeed, some of Pulumi’s most interesting providers have been created this way, delivering access to robust, tried-and-true infrastructure management. The Terraform providers ecosystem is mature and healthy, and enjoys contributions from many cloud and infrastructure leaders across the industry, ourselves included. Most Pulumi users don’t need to know about this detail, however we are proud to be building on the work of others, and contributing our own open-source work back into this vibrant ecosystem.

If you’d like to create a new Pulumi provider, or learn more about how this integration works, check out the [Pulumi Terraform Bridge repository on GitHub](https://github.com/pulumi/pulumi-terraform-bridge). The Terraform Bridge is fully open source and makes it easy to create new a Pulumi provider from an existing Terraform provider.

#### Converting CloudFormation Templates to Pulumi {#providers-converting}

We also offer a tool called [cf2pulumi](/cf2pulumi/) that converts CloudFormation templates into a downloadable Pulumi program written in your programming language of choice. To learn more, see [Converting AWS CloudFormation to Pulumi](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-aws/) in our Adopting Pulumi user guide.

### Cloud Native Support {#cloud-native}

Pulumi supports the full cloud native ecosystem: you can use Pulumi to manage any cloud or SaaS provider, including Kubernetes, with a single, unified programming model. Additionally, Pulumi's native Kubernetes provider offers 100% API coverage in all Pulumi-supported languages, as well as support for Helm charts, strongly typed CustomResourceDefinitions (CRDs), and Kubernetes YAML and Kustomize templates. Pulumi also offers a [Kubernetes operator](/docs/using-pulumi/continuous-delivery/pulumi-kubernetes-operator/) that enables continuous delivery through GitOps. CloudFormation has no support for these capabilities.

To learn more about Pulumi's support for the cloud native ecosystem, see our whitepaper, [Delivering Cloud Native Infrastructure as Code](/whitepapers/delivering-cloud-native-infrastructure-as-code/).

### Dynamic Provider Support {#dynamic-providers}

Occasionally you may want to manage a third-party cloud or SaaS resource that isn't yet supported by Pulumi directly, and isn't covered by a community-supported package in the Pulumi Registry or elsewhere. With Dynamic Providers, you can write custom logic into your Pulumi program to extend the Pulumi resource model to include any local or remote resource that can be managed by way of standard `create`, `read`, `update`, and `delete` operations. Comparable functionality is possible with CloudFormation custom resources, but these require you to create and manage publicly accessible HTTP endpoints to handle deploy-time requests from the CloudFormation service.

To learn more about Dynamic Providers and how to use them, see [Dynamic Providers](/docs/concepts/resources/dynamic-providers/).

### OSS License {#license}

CloudFormation is a closed-source proprietary service of AWS. Pulumi's open-source products, including the core [Pulumi CLI and engine](https://github.com/pulumi/pulumi) and all of its open-source resource providers, use the permissive and business-friendly [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE).

### Infrastructure Reuse and Modularity {#reuse}

With CloudFormation, you can codify and reuse infrastructure configuration by using CloudFormation modules --- specialized templates that can be uploaded to the CloudFormation Registry and referenced from within other CloudFormation templates.

Pulumi also allows you to create modular and reusable infrastructure building blocks, but it does so by building onto the capabilities of your programming language and its ecosystem. With Pulumi [_components_](/docs/concepts/resources/components/), you can abstract and encapsulate complexity into higher-level software resources that have their own trackable state, appear in diffs, and use a logical name that identifies its resources across deployments. Moreover, with Pulumi Packages, you can author components in one language and make them accessible in any language Pulumi supports, and then list those packages on the public Pulumi Registry, a searchable collection of resource providers published by Pulumi, our partners, and the community.

To learn more, see [Components](/docs/concepts/resources/components/), [Pulumi Packages](/docs/using-pulumi/pulumi-packages/), and [Pulumi Registry](/registry/).

### Testing and Validation {#testing}

Testing is an important component of the software-development lifecycle, and Pulumi supports testing in many forms, including unit tests (fast in-memory tests that mock external calls to cloud-provider APIs), property tests (resource-level assertions that can run while infrastructure is being deployed), and integration tests (external tests run against deployed or ephemeral infrastructure). Popular testing libraries and frameworks are also supported. CloudFormation supports only document-level syntax checking and validation.

To learn more about how Pulumi enables testing and test-driven development tools and workflows, see [Testing](/docs/using-pulumi/testing/).

### Modes of Execution {#modes}

CloudFormation deployments are handled fully within the CloudFormation service and in response to an asynchronous request, like a CLI call to `aws cloudformation create-stack` or a browser-based interaction with the AWS Console, and to determine whether a given CloudFormation deployment was successful, you must query or poll the CloudFormation service for the deployment's status. In practice --- particularly when failures occur, and rollbacks are necessary --- this makes for a slow development loop, as template changes have to be made and then resubmitted to the CloudFormation service for subsequent processing.

Pulumi's approach is fundamentally different in that deployments are performed by the CLI itself --- specifically by the Pulumi engine. This results in a much tighter development loop, quicker feedback and debugging, and easier integration into CI/CD workflows because of the CLI's ability to block until deployment is complete and return with a standard exit code indicating whether the deployment succeeded.

Pulumi can also be embedded into application code and driven programmatically with [Automation API](/docs/using-pulumi/automation-api/), enabling higher-order orchestration workflows and more dynamically managed infrastructure.

To learn more about how Pulumi deploys infrastructure, see [How Pulumi Works](/docs/concepts/how-pulumi-works/). To learn more about running Pulumi within the context of another program, see [Automation API](/docs/using-pulumi/automation-api/).

### Embed within Application Code {#embedding}

With Automation API, you can import Pulumi into another application and drive stack operations  programmatically. Automation API gives you a strongly typed and safe way to use Pulumi in many different kinds of embedded contexts --- command-line tools, web applications, self-service portals, or desktop applications --- without having to shell out to a CLI, enabling creation of custom experiences tailored to your use-case, team, or domain. As a managed service, CloudFormation does not have this capability. To learn more about using Pulumi programmatically, see [Automation API](/docs/using-pulumi/automation-api/).

### Third-Party CI/CD Integration {#cicd}

Pulumi integrates with many popular CI/CD providers including AWS Code Services, Azure DevOps, CircleCI, CodeFresh, GitHub Actions, GitLab Pipelines, Google Cloud Build, Jenkins, Octopus Deploy, Jetbrains TeamCity, Spinnaker, and Travis CI. As well, Pulumi has a number of built-in features that facilitate CI/CD workflows including support for unit testing, rich deployment previews with resource-level diffing, drift detection and correction, Git commit tracking, and blocking CLI behavior with standard exit codes. While CloudFormation deployments can generally be triggered from within any CI/CD provider, and are well supported in AWS CodePipeline, CloudFormation itself has no support for these additional CI/CD features.

For more information on how to integrate Pulumi with your CI/CD provider of choice, see our [Continuous Delivery guides](/docs/using-pulumi/continuous-delivery/).

### Policy as Code {#policy}

Pulumi CrossGuard gives you the ability to set guardrails that enforce best practices and security compliance, allowing developers to provision infrastructure easily while at the same time adhering to the standards defined by their teams and organizations. Using Policy as Code, you can write flexible business or security policies in any Pulumi-supported language as well as Open Policy Agent (OPA) Rego, and administrators can apply these policies either to individual stacks or to all of the stacks in an organization. CrossGuard is open source and free to use. Comparable functionality is possible through the use of CloudFormation hooks, though the process of building, testing, and using CloudFormation hooks is considerably different.

To learn more about policy as code with Pulumi, see [Policy as Code ("CrossGuard")](/docs/using-pulumi/crossguard/).

### Secrets Management {#secrets}

In CloudFormation, it's possible to refer to an externally managed secret (like an API token managed with AWS Secrets Manager) from within a CloudFormation template, but CloudFormation itself has no built-in support for managing or handling encrypted secrets.

Pulumi, however, has first-class support for encrypting, storing, and decrypting secret values and for handling them safely throughout the program lifecycle. Secrets are encrypted in transit and at rest, recorded as ciphertext in configuration and state files, are safe to check into version-control systems, and are protected from accidental exposure by the Pulumi CLI. You can also choose to use your own secrets provider (e.g., AWS Key Management Service, Azure Key Vault, Google Cloud KMS, or HashiCorp Vault) with Pulumi.

For more information on managing secrets with Pulumi, see [Secrets](/docs/concepts/secrets/).

### Drift Detection and Correction {#drift-detection}

Both Pulumi and CloudFormation support _drift detection_, which allows you to detect and correct configuration changes that occur outside of the IaC-managed workflow --- for example, as a result of a change made manually in the AWS Console or with the AWS CLI. Whereas CloudFormation's drift detection happens within the CloudFormation service, in Pulumi, it's built into the Pulumi CLI, and can be performed either on demand with `pulumi refresh` or as part of the normal deployment workflow by passing the `--refresh` option. For more information, see [`pulumi up`](/docs/cli/commands/pulumi_up) and [`pulumi refresh`](/docs/cli/commands/pulumi_refresh).

### Stack Configuration and Deployment Environments {#configuration}

With CloudFormation, infrastructure stacks are configured with _parameters_, which are untyped key-value pairs passed as arguments to the AWS CLI. In practice, this means that in order to invoke the AWS CLI (e.g., to deploy a CloudFormation stack), you must first obtain the names and values of all of the stack's parameters, required as well as optional, and then assemble them all into properly formatted command-line arguments before you can submit the deployment request.

Pulumi makes stack configuration less tedious and error-prone, and more collaboration-friendly, by giving each stack its own configuration file and exposing the file's contents to your program at runtime as typed data --- strings, booleans, numbers, arrays, even hierarchical object data. Values can be marked as optional or required, sensitive values can be encrypted and stored safely as ciphertext, and deployment environments (dev, test, staging, production) can be targeted easily with `pulumi stack select`. Configuration files are generally checked into version control as well, and can easily be obtained with `pulumi config refresh`.

To learn more about configuring projects and stacks with Pulumi, see [Configuration](/docs/concepts/config/).

### Audit Capabilities {#auditing}

Administrators of organizations backed by the Pulumi Cloud are able to view and export audit logs that keep track of all user-related activity across the organization. Audit logs capture many kinds of events (stack update requests, failed login attempts, decrypted secrets, removed policies, etc.) along with the timestamp of the event, the user who triggered it, and the source IP address of the call that was made. Audit logs are available to Pulumi Enterprise and Business Critical subscribers. CloudFormation offers similar capability through its integration with AWS CloudTrail.

To learn more about Audit Logs and the kinds of events they capture, see [Audit Logs](/docs/pulumi-cloud/audit-logs/).

### Adopt Existing Resources {#adopting}

Both Pulumi and CloudFormation allow you to bring existing, unmanaged cloud resources into a new or existing stack. In Pulumi, this process is called _importing_, and can be done in one of two ways: either with the Pulumi CLI, using `pulumi import`, which adds the resource to your stack state and generates the code to manage resource going forward; or in code, in a resource declaration using the `import` resource option. CloudFormation also supports this capability, but the process is a bit more involved, requiring a changeset with a modified CloudFormation template or a template fragment supplied on the command line.

To learn more about how to import and manage cloud resources with Pulumi, see [Importing Infrastructure](/docs/using-pulumi/adopting-pulumi/import/) in our Adopting Pulumi user guide.

### Convert Code from Other IaC Tools {#converting}

Pulumi offers a number of useful tools to help you convert code written for other infrastructure-as-code tools (including CloudFormation) into deployable Pulumi programs written in your language of choice. The conversion process automatically generates a new, fully-functional Pulumi program that matches the source IaC program or template. CloudFormation has no comparable support for this feature.

To learn more, see [Conversion](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/#conversion) in our Adopting Pulumi user guide.

### Resource Aliases {#aliases}

Aliases help facilitate refactoring by allowing you to modify certain properties of a resource without risk of replacing it. With an alias, you can change the logical name of a given resource, change its parent (i.e., move it from one component to another), change its underlying resource type, or even move it to an entirely different project or stack. Both Pulumi and CloudFormation support the notion of resource renaming. To learn more about renaming or aliasing existing resources in Pulumi, see [Aliases](/docs/concepts/options/aliases/) in the Resource documentation.

### Resource Transformations {#transformations}

Transformations, which are unique to Pulumi, allow you to programmatically set or override the input properties of resources belonging to a particular collection, such as the child resources of a Pulumi component or even all of the resources belonging to a stack. Transformations make it easy to apply consistent settings across your infrastructure without having to manipulate the properties of individual resources. CloudFormation does not have support for this feature. To learn more, see [Transformations](/docs/concepts/options/transformations/) in the Resource documentation.
