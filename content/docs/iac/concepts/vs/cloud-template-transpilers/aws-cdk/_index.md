---
title_tag: "Pulumi vs. AWS CDK"
meta_desc: Pulumi and AWS Cloud Development Kit (CDK) share some similarities, but there are many key differences. Learn about these major differences here.
title: Pulumi vs AWS Cloud Development Kit (CDK)
h1: Pulumi vs AWS Cloud Development Kit (CDK)
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Pulumi vs AWS Cloud Development Kit (CDK)
        parent: cloud-template-transpilers
        weight: 3
    concepts:
        parent: vs
        weight: 3
aliases:
- /docs/intro/vs/cloud-template-transpilers/aws-cdk/
- /docs/concepts/vs/cloud-template-transpilers/aws-cdk/
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

Choosing the right infrastructure as code tool is important, and we want you to have as much information as possible to make the choice that best suits your needs. We've created this document to help you understand how Pulumi compares with AWS Cloud Development Kit.

## What is AWS CDK?

AWS Cloud Development Kit (CDK) is an AWS-specific infrastructure as code tool for defining cloud resources with general-purpose programming languages. CDK is based on Node.js and converts program code into AWS CloudFormation JSON/YAML templates that are then deployed by the AWS CloudFormation deployment service.

## Why choose Pulumi over AWS CDK?

Pulumi and AWS CDK both utilize general-purpose programming languages for infrastructure as code. While CDK is tied to AWS CloudFormation, Pulumi offers distinct advantages in terms of speed, security, cost savings, and scalability. Pulumi's multi-language and multi-cloud capabilities allow it to support deployments across platforms like Azure, Snowflake, and AWS simultaneously, something CDK cannot achieve. Additionally, Pulumi's independent runtime provides a more seamless and productive developer experience, free from the limitations of CloudFormation. Users who have transitioned to Pulumi report improved performance, faster deployment times, and greater developer joy. See the [SST](https://sst.dev/blog/moving-away-from-cdk), [WhyLabs](/case-studies/whylabs/), and [Panther Labs](/case-studies/panther-labs/) case studies for more details.

### Scale

Pulumi is better equipped to handle large-scale deployments across multi-cloud environments.

- __Workflow orchestration__: With its Automation API, Pulumi allows for the programmatic management of infrastructure at scale. This feature enables dynamic orchestration workflows that are not possible with CDK's CLI-based execution model.
- __Multi-cloud support__: Pulumi supports multi-cloud environments, Kubernetes, SaaS providers (e.g., Datadog, Databricks, Okta), and on-premises infrastructure. This flexibility enables organizations to scale across different platforms without being constrained by a single provider like AWS in the case of CDK.
- __Resource limits__: Unlike CloudFormation (and by extension CDK), which imposes a 500-resource limit per template, Pulumi imposes no hard limits on the number of resources in a stack, making it better suited for complex deployments.

### Speed

Pulumi enables faster development and deployment workflows compared to CDK due to its direct integration with cloud providers without going through a transpiler.

- __Deployment__: Pulumi communicates directly with cloud providers, bypassing the intermediate step of generating CloudFormation templates as required by CDK. Since CDK relies on CloudFormation as its deployment engine, it inherits many of CloudFormation's speed limitations. (see [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation/)).
- __Development__: Pulumi's runtime engine allows for immediate feedback (milliseconds) in your IDE during deployment, enabling you to debug and iterate more quickly. In contrast, CDK's reliance on CloudFormation introduces delays (tens of minutes) due to template transpilation and longer error resolution times.
- __Testing__: Pulumi supports fast, in-memory unit tests that mock external calls, enabling developers to validate infrastructure without deploying it. CDK testing is limited to assertions against synthesized CloudFormation templates, which slows down the feedback loop.
- __Developer self-service__: Pulumi empowers you to build modern infrastructure platforms that enable developers to self-service cloud infrastructure. You can easily build GUI, CLI, or YAML based developer portals or use the built-in [New Project Wizard](/docs/pulumi-cloud/developer-portals/new-project-wizard/) with customizable organizational templates. In contrast, CDK lacks features specifically designed for building developer platforms.
- __AI-powered__: [Pulumi Copilot](/docs/pulumi-cloud/copilot/) is an AI-powered assistant that automates any infrastructure management task. It can generate a Pulumi program from a few simple text prompts, and it provides predictive insights to analyze and preempt potential operational issues. CDK doesn't include AI capabilities for generating code or providing operational insights.

### Security

Pulumi natively integrates security features with infrastructure provisioning.

- __Secrets management__: Pulumi has built-in secrets management that encrypts secrets both in transit and at rest. It also integrates seamlessly with external secrets managers like AWS Secrets Manager. CDK has no built-in support for managing or handling encrypted secrets.
- __Policy as code__: Pulumi enables your organization to enforce security and compliance policies during deployment using Pulumi CrossGuard's policy as code. This feature is tightly integrated into Pulumi's workflows, whereas CDK offers only limited support for such policies.

### Savings

Pulumi can deliver cost savings over CDK due to its multi-cloud support and efficiency gains in the inner development loop.

- __Multi-cloud support__. Pulumi supports over 160 cloud providers, allowing your organization to optimize costs by choosing the most cost-effective provider for your needs. CDK is limited to AWS, which may lock you into higher cost AWS services. Using CDK will also necessitate employing another IaC system to manage non-AWS resources which will increase training time for new engineers and operational complexity.
- __Operational efficiency__: Pulumi’s faster deployments reduce engineering time spent on debugging and iteration cycles. This translates into lower development time costs compared to the more time-intensive development workflows required by CDK.
- __Interoperability__: Pulumi can integrate with existing resources managed by other IaC tools, eliminating the need for costly migrations or extensive code refactoring. CDK lacks interoperability with other IaC tools, which requires full migration to CDK code in order to interact with existing resources.

## Pulumi vs. CDK: Similarities {#similarities}

Both Pulumi and CDK allow you to build and deploy infrastructure on AWS using familiar programming languages and tools, and both use a declarative infrastructure as code model built on the concept of _desired state_. In both Pulumi and CDK, desired state is expressed by declaring one or more cloud resources in code that’s evaluated by the deployment engine (though with CDK, that code is rendered CloudFormation text), and the deployment engine determines whether to create, update or destroy the resources of an infrastructure stack by comparing its last known state with the new state expressed by the code. Both have similar concepts for modularity and higher-level abstractions that encapsulate multiple resources. These are known as constructs in CDK and as Component Resources in Pulumi.

## Pulumi vs. CDK: Key Differences {#differences}

First, CDK supports only AWS, whereas Pulumi supports over 150 cloud and SaaS providers, with more being added all the time. Second, while both Pulumi and CDK support languages like TypeScript, Python, Go, C#, and Java, the two tools are fundamentally different in how they interpret these languages and deploy resources. Unlike Pulumi, whose open-source engine understands these languages and communicates directly with cloud providers to deploy infrastructure, CDK is a transpiler (i.e., a [source-to-source compiler](https://en.wikipedia.org/wiki/Source-to-source_compiler)) that first produces AWS Cloud Assembly, an intermediate format consisting of CloudFormation templates and other assets. After the transpilation process, these assets are uploaded to targeted services (such as S3, ECR) and then the CDK invokes the CloudFormation service, which begins the deployment process.

The limits of the transpiler present some significant problems in terms of both speed (of both the inner development loop and the actual deployment) and correctness (errors may not be discovered until hours into the deployment process, rather than at compile time). Because of the inherent CDK dependencies, users need expertise in both CloudFormation and the CDK in order to debug any issues and achieve any successful results.

Moreover, because CDK depends on CloudFormation as the deployment engine, it shares many of the same benefits and limitations as CloudFormation (see [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation/).

Finally, while both CDK and Pulumi support automated testing, the scenarios they're able to support are quite different. For example, both CDK and Pulumi support unit testing, but Pulumi offers significant advantages as a result of the deep integration between language host and runtime. With Pulumi, you can run fast, in-memory (offline) unit tests that mock external calls to cloud providers, whereas with CDK, you're only able to run assertions against the rendered CloudFormation template synthesized by the CDK app, and there is no equivalent option for offline testing.

## Pulumi vs. CDK: Better Together {#better-together}

While there are differences and similarities between Pulumi and AWS CDK, they can actually be used together for a more powerful experience in managing infrastructure. The pulumi-cdk library allows CDK code and constructs to be used directly in Pulumi programs, resulting in AWS resources being deployed and managed via Pulumi. Outputs of resources defined in a Pulumi program can be passed into AWS CDK constructs, and outputs from AWS CDK stacks can be used as inputs to other Pulumi resources. This allows CDK users to be able to use their existing constructs and access all the features of Pulumi Cloud (e.g., policy as code, drift detection, Insights and Copilot). See the [Pulumi CDK Adapter documentation](/docs/iac/clouds/aws/guides/cdk/) for more details.

In addition to CDK interoperability, Pulumi can deploy CloudFormation stacks directly from a Pulumi program. See the [AWS provider documentation](/registry/packages/aws/api-docs/cloudformation/). If you already have CloudFormation resources, Pulumi stacks can reference resources from existing CloudFormation stacks. You can also easily convert CloudFormation templates to Pulumi programs. See the [AWS CloudFormation to Pulumi documention](/docs/iac/adopting-pulumi/migrating-to-pulumi/from-cloudformation/).

The following table summarizes some additional similarities and differences between Pulumi and CDK, and the sections below the table go into more detail.

### Feature Comparisons

| Feature | Pulumi | AWS CDK |
| ------- | ------ | -------------- |
| [Language Support](#language) | TypeScript, JavaScript, Python, Go, C#, F#, VB.NET, Java, YAML | Python, TypeScript, JavaScript, Go (developer preview), C#, Java |
| [State Management](#state) | Managed by Pulumi Cloud or with self-managed options | Managed by the AWS CloudFormation service |
| [Provider Support](#providers) | Supports all major cloud providers, including 100% same-day coverage of new resources with AWS Cloud Control | AWS only |
| [Cloud Native Support](#cloud-native) | Richly typed support for the full cloud-native ecosystem and Kubernetes | AWS only |
| [Dynamic Provider Support](#dynamic-providers) | Yes | Limited |
| [OSS License](#license) | Apache License 2.0 | Apache License 2.0 (only applies to the CDK framework, and not the deployment engine) |
| [Infrastructure Reuse and Modularity](#reuse) | Flexible and extensible: functions, classes, modules, Component Resources, multi-language packages, and more | Reuse functions, classes, packages, and CDK constructs |
| [Testing and Validation](#testing) | Unit, property, and integration testing supported with popular test frameworks | Only supports unit testing that asserts against synthesized YAML/JSON |
| [Modes of Execution](#modes) | Run CLI commands or initiate commands programmatically with Automation API | Run CLI commands to execute CloudFormation deployments |
| [Embed within Application Code](#embedding) | Yes, via Automation API | No |
| [Third-party CI/CD Tools Support](#cicd) | Yes | AWS CodePipeline |
| [Policy as Code](#policy) | Yes | Limited |
| [Secrets Management](#secrets) | Yes. Secrets are encrypted in transit and in the state file | No built-in support, available through other services |
| [Audit Capabilities](#auditing) | Yes | Limited |
| [Adopt Existing Resources](#adopting) | Yes. Generates code as part of the import process | No |
| [Import code from other IaC Tools](#import) | Yes | No |

Getting started with Pulumi is easy if you already have experience with CDK or a general-purpose programming language. Follow our [Adopting Pulumi from AWS CloudFormation](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/from-aws/) or try our [CloudFormation conversion tool](/cf2pulumi/). To deploy CDK constructs with Pulumi, follow our [Pulumi CDK Adapter documentation](/docs/iac/clouds/aws/guides/cdk/).

To deploy a simple program, follow our Get Started guide:

{{< get-started >}}

### Language Support {#language}

While both Pulumi and CDK support using general-purpose programming languages for infrastructure code, they differ in terms of how your code is used at runtime.

With CDK, the code you write is converted into AWS Cloud Assembly --- structured configuration consisting of CloudFormation template code and other assets (to be uploaded later to the CloudFormation service). With Pulumi, however, your code communicates at runtime with the deployment engine, which has deep support for multiple languages and integration with language runtimes. Overall, Pulumi is therefore able to deliver a far richer experience for developers, as its architecture unlocks many advanced capabilities (such as standard unit testing) that may not be possible with CDK.

To learn more about languages and language runtimes in Pulumi, see [How Pulumi Works](/docs/concepts/how-pulumi-works/).

### State Management {#state}

CDK depends on AWS CloudFormation for this capability. See [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation#state) to learn more.

### Provider Support {#providers}

CDK depends on AWS CloudFormation for this capability. See [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation#providers) to learn more.

### Cloud Native Support {#cloud-native}

CDK depends on AWS CloudFormation for this capability. See [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation#cloud-native) to learn more.

### Dynamic Provider Support {#dynamic-providers}

CDK depends on AWS CloudFormation for this capability. See [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation#dynamic-providers) to learn more.

### OSS License {#license}

Both CDK and Pulumi are licensed under [Apache License 2.0](https://github.com/pulumi/pulumi/blob/master/LICENSE), however CDK’s deployment engine (AWS CloudFormation) is a proprietary AWS service. The Pulumi CLI (which contains the deployment engine) is also fully open source, and all Pulumi providers are open source as well.

### Infrastructure Reuse and Modularity {#reuse}

Both CDK and Pulumi support reusability through the built-in capabilities of the languages they support, such as functions, classes, modules, and packages. Both support the concept of higher-level abstractions as well --- CDK through constructs and Pulumi through Component Resources --- and both are supported by public registries that index these abstractions.

The main advantage Pulumi has over CDK in this regard is its ability to create multi-language, reusable packages encapsulating higher-level abstractions and architectural patterns. With Pulumi, you can write a package in your language of choice and then generate equivalent packages in any language Pulumi supports. To learn more, see [Pulumi Packages](/docs/using-pulumi/pulumi-packages/).

### Testing and Validation {#testing}

Unit tests in CDK assert on the synthesized CloudFormation template content rather than the CDK code itself, meaning that in order to write a unit test with CDK, you must first understand the translation of CDK to CloudFormation. This makes testing challenging since you face a contextual gap between the intent specified in CDK code and the synthesized CloudFormation template. However, with Pulumi, unit tests can assert using the same object model as the Pulumi program, which gives you direct debugging and faster productivity. You can run fast in-memory tests that mock external calls, and also validate how data flows across resource dependencies in a way that mimics what would happen in production. In contrast, CDK doesn’t allow you to perform the same level of assertion on dependencies since it converts resource references into values that CloudFormation understands via its `Ref` intrinsic function.

Pulumi also supports property tests (Policy as Code), which run resource-level assertions while infrastructure is being deployed, and integration tests, which deploy ephemeral infrastructure and run external tests against it.

To learn more about how Pulumi enables testing and test-driven development tools and methodologies, see [Testing](/docs/using-pulumi/testing/).

### Modes of Execution {#modes}

The CDK CLI synthesizes CDK apps into CloudFormation templates and initiates deployments through the AWS CloudFormation service. You can also deploy CDK apps through a CI/CD service like AWS CodePipeline.

Pulumi’s approach is fundamentally different in that deployments are performed within the CLI itself by the Pulumi engine. This results in a much tighter development loop, easier debugging, and simpler integration into CI/CD workflows because of the CLI’s ability to block until deployment is complete and return with a standard exit code indicating whether the deployment was successful.
Moreover, with Automation API, Pulumi can be embedded into application code and driven programmatically, enabling higher-order orchestration workflows and dynamically managed infrastructure.

To learn more about how Pulumi deploys infrastructure, see [How Pulumi Works](/docs/concepts/how-pulumi-works/). To learn more about how to run Pulumi within the context of another program, see [Automation API](/docs/using-pulumi/automation-api/).

### Embed within Application Code {#embedding}

With Automation API, you can import Pulumi into another application and drive stack operations programmatically. Automation API gives you a strongly typed and safe way to use Pulumi in many different kinds of embedded contexts — e.g., command-line tools, web applications, self-service portals, or desktop applications — without having to shell out to a CLI, enabling creation of custom experiences tailored to your use-case, team, or domain. CDK does not have this capability. To learn more about using Pulumi programmatically, see [Automation API](/docs/using-pulumi/automation-api/).

### Third-Party CI/CD Support {#cicd}

CDK depends on AWS CloudFormation for this capability. See [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation#cicd) to learn more.

### Policy as Code {#policy}

CDK depends on AWS CloudFormation for this capability. See [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation#policy) to learn more.

### Secrets Management {#secrets}

CDK depends on AWS CloudFormation for this capability. See [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation#secrets) to learn more.

### Audit Capabilities {#auditing}

CDK depends on AWS CloudFormation for this capability. See [Pulumi vs. CloudFormation](/docs/concepts/vs/cloud-templates/cloudformation#auditing) to learn more.

### Adopt Existing Resources {#adopting}

CDK does not support this capability officially. It's possible to import existing resources from an AWS CloudFormation template, but doing so requires adding a CDK API wrapper around the CloudFormation resources and referencing it within your CDK code.

Importing is simpler and more streamlined in Pulumi, and can be done in one of two ways: either with the Pulumi CLI, using `pulumi import`, which adds the resource to your stack state and generates the code to manage resource going forward; or in code, in a resource declaration using the `import` resource option.

To learn more about importing and managing imported cloud resources with Pulumi, see [Importing Infrastructure](/docs/using-pulumi/adopting-pulumi/import/) in our Adopting Pulumi user guide.

### Convert Code from Other IaC Tools {#import}

Pulumi offers a number of useful tools to help you convert code written for other infrastructure-as-code tools (including CloudFormation) into deployable Pulumi programs written in your language of choice. The conversion process automatically generates a new, fully-functional Pulumi program that matches the source IaC program or template. CloudFormation has no comparable support for this feature.

To learn more, see [Conversion](/docs/using-pulumi/adopting-pulumi/migrating-to-pulumi/#conversion) in our Adopting Pulumi user guide.
