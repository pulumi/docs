---
title: What is Pulumi?
meta_desc: |
    Discover what Pulumi is, how it works, and why it's revolutionizing infrastructure as code with familiar programming languages.
type: what-is
page_title: "What is Pulumi?"
---

The modern cloud landscape has transformed how organizations build and deploy applications, but managing cloud infrastructure often remains a complex, error-prone process involving clicking through web consoles, writing brittle scripts, or learning domain-specific languages. Pulumi emerges as a solution that fundamentally changes this paradigm by enabling developers and infrastructure teams to manage cloud resources using the same programming languages they already know and love.

Pulumi is a cloud engineering platform that treats infrastructure as software, allowing teams to define, deploy, and manage cloud resources using familiar programming languages like TypeScript, Python, Go, C#, Java, and YAML. Rather than forcing teams to learn proprietary configuration languages or rely on limited templating systems, Pulumi brings the full power of modern software development practices to infrastructure management.

## The evolution of infrastructure management

To understand Pulumi's significance, it's helpful to consider how infrastructure management has evolved. In the early days of cloud computing, infrastructure was typically managed through web consoles or command-line interfaces. While functional, this approach suffered from poor repeatability, limited collaboration capabilities, and difficulty tracking changes over time.

The introduction of infrastructure as code (IaC) tools like Terraform and AWS CloudFormation represented a significant improvement, enabling teams to define infrastructure declaratively and version control their configurations. However, these tools introduced their own challenges through domain-specific languages that required additional learning curves and offered limited expressiveness compared to general-purpose programming languages.

Pulumi represents the next evolution in this space by embracing what the company calls "infrastructure as software." This approach enables teams to leverage the full software engineering ecosystem—including testing frameworks, package managers, IDEs, and development workflows—when managing their cloud infrastructure.

## Pulumi in the AI coding era

The emergence of AI-powered code generation tools is fundamentally transforming how software is developed. More code is being written faster than ever before, with AI assistants generating complex applications and infrastructure configurations at unprecedented speeds. However, this shift brings both opportunities and challenges that make platforms like Pulumi more essential, not less.

While AI can accelerate code creation, it doesn't eliminate the need for governance, security, and operational best practices. In fact, as teams generate more code with potentially less deep understanding of every component, the importance of having robust infrastructure management practices becomes even more critical. Code still needs to run securely, cost-effectively, and in compliance with organizational policies regardless of how it was created.

Pulumi serves as the essential building block for this AI-driven future—functioning as "Git for your cloud infrastructure." Just as version control systems became indispensable as software development scaled, infrastructure as code platforms have become crucial as AI accelerates both application and infrastructure development. The platform provides the governance layer that ensures AI-generated infrastructure follows organizational standards, security requirements, and cost controls.

The combination of AI coding tools with Pulumi's platform capabilities, particularly through Internal Developer Platforms (IDPs), enables organizations to marry the speed and creativity of AI-assisted development with the reliability and governance required for production cloud environments. This approach prevents AI from becoming the new "ClickOps"—where rapid changes bypass proper controls and oversight.

## How Pulumi works

At its core, Pulumi follows a declarative model where you describe your desired infrastructure state in code, and the platform handles the complexities of provisioning, updating, and managing cloud resources to achieve that state. This process involves several key components working together seamlessly.

The Pulumi SDK provides language-specific libraries that offer strongly-typed bindings for cloud resources across 150+ providers. These libraries enable developers to define infrastructure using familiar programming constructs like functions, loops, conditionals, and classes, while providing rich IDE support including IntelliSense, error checking, and refactoring capabilities.

When you run a [Pulumi program](/docs/iac/concepts/projects/), the deployment engine analyzes your code, computes the necessary changes to reach your desired state, and executes those changes in the optimal order while respecting resource dependencies. The engine maintains a detailed record of your infrastructure state, enabling features like drift detection, rollback capabilities, and collaborative workflows.

The [Pulumi CLI](/docs/iac/cli/) serves as the primary interface for managing deployments, providing commands for previewing changes, executing deployments, and managing the infrastructure lifecycle. For teams requiring additional collaboration and governance features, Pulumi Cloud offers a managed service that provides centralized state management, team collaboration tools, policy enforcement, and detailed audit trails.

## Key concepts and architecture

Understanding Pulumi's architecture requires familiarity with several foundational concepts that distinguish it from traditional infrastructure tools.

**[Projects](/docs/iac/concepts/projects/) and [stacks](/docs/iac/concepts/stacks/)** form the organizational backbone of Pulumi's approach. A project represents a directory containing your infrastructure code and metadata, while stacks provide isolated instances of your project for different environments like development, staging, and production. This separation enables teams to manage multiple environments from a single codebase while maintaining appropriate isolation and configuration differences.

**[Resources](/docs/iac/concepts/resources/)** represent the fundamental building blocks of your infrastructure, from individual cloud services like AWS S3 buckets to complex, multi-resource constructs like entire application architectures. Pulumi's resource model supports both primitive resources that map directly to cloud provider APIs and component resources that encapsulate multiple resources into reusable abstractions.

**Configuration and secrets management** is handled through an advanced system that provides stack-specific configuration values while ensuring sensitive information remains encrypted. Pulumi ESC (Environments, Secrets, and Configuration) extends this capability by providing centralized secrets management across environments and applications, integrating with existing secret stores and identity providers.

The **state management** system maintains a comprehensive record of your infrastructure's current state, enabling Pulumi to compute the minimal set of changes needed for any deployment. Unlike some tools that store state in plain text, Pulumi encrypts sensitive information by default and provides robust state management capabilities through both local and cloud-based backends.

## The Pulumi Registry: A comprehensive ecosystem

The [Pulumi Registry](/registry/) represents one of Pulumi's most significant advantages over traditional infrastructure tools. This comprehensive ecosystem provides access to over 150 cloud and SaaS providers through a unified, multi-language interface that goes far beyond what any single cloud provider offers.

### Native cloud providers

Pulumi maintains native, first-party providers for major cloud platforms that offer same-day support for new services and features. The AWS provider covers over 900 resources, while Azure Native provides access to the full Azure API surface area, and Google Cloud offers comprehensive coverage of GCP services. These native providers are generated directly from cloud provider APIs, ensuring immediate access to new features without waiting for community contributions or manual updates.

### Beyond traditional clouds

The registry extends far beyond traditional cloud providers to include specialized services that modern applications depend on. Teams can manage Datadog monitoring, Auth0 identity, GitHub repositories, Cloudflare edge services, and dozens of other SaaS platforms using the same patterns and languages they use for their core infrastructure.

### Community and official packages

The registry combines official packages maintained by Pulumi with a growing ecosystem of community contributions. Popular packages include Kubernetes operators, Docker configurations, and specialized industry solutions. Each package is automatically generated for all supported programming languages, meaning a single package definition provides TypeScript, Python, Go, C#, and Java bindings.

### Crosswalk collections

Pulumi Crosswalk collections represent opinionated, well-architected patterns for common cloud scenarios. These collections encapsulate cloud provider best practices into higher-level abstractions, enabling teams to deploy production-ready architectures with minimal code. For example, Crosswalk for AWS provides secure, scalable patterns for containers, serverless applications, and data processing pipelines.

## The power of real programming languages

One of Pulumi's most significant differentiators is its support for general-purpose programming languages rather than domain-specific languages. This design choice has profound implications for how teams approach infrastructure management.

Using familiar programming languages means developers can apply existing skills and knowledge to infrastructure problems. They can leverage the full ecosystem of language features, including package managers, testing frameworks, and development tools. This approach eliminates the need to learn proprietary configuration languages and enables teams to create more sophisticated, maintainable infrastructure code.

The ability to use standard programming constructs like loops, conditionals, and functions enables dynamic infrastructure definitions that would be difficult or impossible with templating-based approaches. For example, you might programmatically create resources based on environment variables, implement complex business logic within your infrastructure code, or generate resources based on external data sources.

Furthermore, Pulumi's language support extends beyond basic resource definitions to include comprehensive [testing capabilities](/docs/iac/guides/testing/). Teams can write unit tests for their infrastructure code, validate resource configurations before deployment, and implement integration tests to ensure their infrastructure behaves correctly in different scenarios.

## Advanced platform capabilities

Pulumi goes beyond basic infrastructure provisioning to provide a comprehensive platform for modern cloud engineering.

### Automation API

The Automation API enables teams to embed infrastructure management directly into their applications, creating custom deployment tools, self-service portals, and dynamic infrastructure provisioning systems. This programmatic approach enables organizations to build advanced infrastructure automation that integrates seamlessly with their development workflows, particularly valuable when dealing with AI-generated code that requires automated deployment pipelines.

### Policy as Code with Pulumi Policies

Pulumi Policies provides policy as code capabilities that are both open source and free, unlike competitive offerings. Teams can write policies in Python, JavaScript, or Open Policy Agent (OPA) Rego to enforce security, compliance, and cost controls across their entire infrastructure. These policies run server-side and can provide automated remediation, ensuring that all infrastructure deployments—whether created by humans or AI—meet organizational standards.

### Pulumi ESC for secrets and configuration

Pulumi ESC addresses one of the most critical challenges in modern cloud operations: secrets and configuration management. This service provides centralized, auditable secrets management that can pull from multiple secret stores, generate dynamic short-lived credentials via OIDC, and compose configurations across environments. ESC can be used with or without Pulumi IaC, making it valuable for any cloud application.

### AI-powered development assistance

Pulumi integrates artificial intelligence to accelerate infrastructure development while maintaining quality and governance standards. Pulumi AI can generate infrastructure code from natural language descriptions, translate between different infrastructure tools, and provide intelligent suggestions based on best practices. This AI integration helps teams achieve dramatic productivity improvements while ensuring that generated code follows organizational patterns and policies.

## Multi-cloud and provider ecosystem

Pulumi's architecture supports an extensive ecosystem of cloud providers, enabling teams to adopt multi-cloud strategies or migrate between providers without rewriting their infrastructure code. The platform maintains native providers for major cloud platforms like AWS, Microsoft Azure, and Google Cloud Platform, ensuring same-day support for new cloud services and features.

This multi-cloud capability extends beyond traditional cloud providers to include specialized services like Cloudflare, Datadog, Auth0, and GitHub, as well as private cloud technologies like VMware vSphere and OpenStack. The consistent API across all providers means teams can apply the same patterns and practices regardless of their underlying infrastructure choices.

The provider ecosystem also includes community-maintained providers and the ability to create custom providers for internal services or specialized requirements. This extensibility ensures that Pulumi can adapt to virtually any infrastructure environment or organizational need.

## Enterprise-grade security and governance

Pulumi provides comprehensive security and governance capabilities that meet the needs of the largest enterprises while remaining accessible to smaller teams.

### Security by default

Unlike tools that store secrets in plain text, Pulumi encrypts all sensitive information by default, both in transit and at rest. The platform maintains SOC 2 Type II compliance and provides comprehensive audit trails for all infrastructure changes. Integration with existing security tools and identity providers ensures that Pulumi fits seamlessly into enterprise security practices.

### Team collaboration and governance

Pulumi Cloud provides sophisticated team management capabilities, including role-based access controls, stack-level permissions, and policy enforcement across the entire organization. Teams can implement GitOps workflows, automated testing, and deployment pipelines while maintaining the security and governance controls required for enterprise environments.

### Self-hosted deployment options

For organizations with strict data sovereignty requirements, Pulumi offers self-hosted deployment options that provide the same enterprise features while maintaining complete control over data and infrastructure. These options support air-gapped environments and can be deployed in private clouds or on-premises infrastructure.

## Real-world applications and success stories

Organizations across various industries have adopted Pulumi to address diverse infrastructure challenges, demonstrating the platform's versatility and effectiveness in real-world scenarios.

Snowflake, a leading cloud data platform, used Pulumi to reduce its deployment time from 1.5 weeks to a single day while improving reliability and maintainability. The ability to use familiar programming languages enabled their development teams to contribute directly to infrastructure management, reducing silos between development and operations.

BMW manages infrastructure for over 11,000 developers using Pulumi, leveraging the platform's collaboration features and policy enforcement capabilities to maintain consistency and security across their global development organization. The company particularly benefits from Pulumi's ability to create reusable components that encapsulate their infrastructure best practices.

Starburst achieved a 112x improvement in deployment speed, reducing deployment times from two weeks to just three hours. This dramatic improvement was enabled by Pulumi's testing capabilities and the ability to create sophisticated deployment pipelines using familiar programming languages.

These success stories demonstrate how Pulumi enables organizations to achieve substantial improvements in deployment speed, developer productivity, and operational reliability while maintaining the security and governance capabilities required for enterprise environments.

## Competitive advantages and positioning

When compared to established infrastructure as code tools, Pulumi offers several distinct advantages that address common pain points in infrastructure management.

Traditional tools like Terraform require teams to learn domain-specific languages with limited expressiveness compared to general-purpose programming languages. Pulumi's approach enables teams to leverage existing language skills while providing access to the full ecosystem of development tools and practices.

The testing capabilities represent another significant advantage. While some tools offer limited testing options, Pulumi's integration with language-native testing frameworks enables comprehensive testing strategies including unit tests, integration tests, and property-based testing approaches.

Security represents a critical differentiator, particularly regarding secrets management. While some tools store sensitive information in plain text within state files, Pulumi encrypts secrets by default and provides comprehensive secrets management capabilities that integrate with existing organizational security practices.

The provider ecosystem and same-day support for new cloud services ensure that teams can take advantage of the latest cloud capabilities without waiting for provider updates or community contributions. This agility is particularly important in rapidly evolving cloud environments where new services and features are constantly being introduced.

Additionally, Pulumi's open source foundation under the Apache 2.0 license provides greater flexibility compared to tools with more restrictive licensing models, ensuring that organizations can adopt and modify the platform according to their needs without vendor lock-in concerns.

## The future of cloud engineering and platform engineering

Pulumi's approach reflects broader trends in cloud engineering that emphasize developer productivity, collaboration, and the application of software engineering practices to infrastructure management. As cloud environments become increasingly complex and organizations adopt multi-cloud strategies, the need for sophisticated infrastructure management tools continues to grow.

The platform's emphasis on treating infrastructure as software aligns with the DevOps movement and the broader trend toward breaking down silos between development and operations teams. By enabling developers to contribute directly to infrastructure management using familiar tools and languages, Pulumi helps organizations achieve the collaborative, cross-functional approach that defines modern cloud engineering.

Platform engineering represents one of the most significant trends in modern cloud operations, and Pulumi provides purpose-built capabilities to make all aspects of platform engineering vastly simpler. The platform enables organizations to build internal developer platforms that provide self-service capabilities while maintaining security, scalability, repeatability, and consistency.

In the emerging AI-driven development landscape, Pulumi's governance and policy capabilities become even more crucial. As AI tools generate infrastructure code at unprecedented speeds, organizations require robust platforms that ensure generated code adheres to security policies, cost controls, and operational best practices while enabling the rapid innovation that AI makes possible.

Looking forward, Pulumi continues to evolve with features like AI-powered assistance for infrastructure development, enhanced policy enforcement capabilities, and deeper integration with cloud-native development workflows. These developments position Pulumi as a platform that not only addresses current infrastructure challenges but also anticipates the needs of future cloud engineering practices in an AI-augmented world.

## Getting started with Pulumi

For organizations interested in exploring Pulumi, the platform offers multiple entry points depending on your current infrastructure management approach and technical requirements.

Teams with existing infrastructure can leverage Pulumi's import capabilities to bring existing resources under management without disrupting current operations. The platform provides converters for Terraform configurations, AWS CloudFormation templates, Azure Resource Manager templates, and Kubernetes YAML, enabling gradual adoption where teams can start with new projects while progressively migrating existing infrastructure.

The extensive library of example programs and templates in the Pulumi Registry provides starting points for common infrastructure patterns, enabling teams to quickly understand best practices and adapt them to their specific requirements. These examples span multiple cloud providers and use cases, from simple web applications to complex multi-tier architectures and AI/ML workloads.

For teams with specific requirements or complex existing infrastructure, Pulumi offers professional services and consulting to help organizations design and implement infrastructure strategies that align with their business objectives and technical constraints. This includes migration planning, architecture design, and training programs to ensure successful adoption.

The platform provides comprehensive documentation, tutorials, and learning resources that help teams get started quickly while building expertise over time. The community-driven support model, combined with enterprise support options, ensures that organizations can get the assistance they need at every stage of their cloud journey.

## Conclusion

Pulumi represents a fundamental shift in how organizations approach cloud infrastructure management, moving beyond the limitations of domain-specific languages and templating systems to embrace the full power of modern software development practices. By treating infrastructure as software, Pulumi enables teams to leverage existing skills, tools, and workflows while providing the advanced capabilities required for modern cloud environments.

The platform's combination of open source foundation, comprehensive registry ecosystem, and enterprise capabilities ensures that it can serve organizations of all sizes, from startups building their first cloud applications to large enterprises managing complex multi-cloud environments. The proven results achieved by customers demonstrate the real-world impact of adopting a software-centric approach to infrastructure management.

As cloud infrastructure continues to evolve in complexity and importance, particularly in an era where AI is accelerating code generation, Pulumi's approach to infrastructure as software positions it as a crucial tool for organizations seeking to maximize the value of their cloud investments while maintaining the agility and reliability required for modern business operations. The platform's emphasis on governance, security, and policy enforcement ensures that rapid development—whether human or AI-driven—doesn't compromise operational excellence.

Whether you're a developer looking to apply your programming skills to infrastructure problems, an operations team seeking better collaboration with development teams, or an organization pursuing a comprehensive cloud engineering strategy in the AI era, Pulumi offers a path forward that embraces the best practices of modern software development while addressing the unique challenges of cloud infrastructure management at scale.

## Learn more

Ready to experience infrastructure as software? Explore Pulumi's comprehensive platform and discover how it can transform your approach to cloud infrastructure management.

- [Get started with Pulumi](/docs/get-started/)
- [Explore the registry](/registry/)
- [Read customer success stories](/case-studies/)
- [Compare infrastructure as code tools](/blog/infrastructure-as-code-tools/)

### Related topics

- [What is Infrastructure as Code?](/what-is/what-is-infrastructure-as-code/)
- [What is Infrastructure as Software?](/what-is/what-is-infrastructure-as-software/)
- [What is DevOps?](/what-is/what-is-devops/)
- [What is Platform Engineering?](/what-is/what-is-platform-engineering/)
