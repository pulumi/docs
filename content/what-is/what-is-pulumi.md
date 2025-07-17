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

## How Pulumi works

At its core, Pulumi follows a declarative model where you describe your desired infrastructure state in code, and the platform handles the complexities of provisioning, updating, and managing cloud resources to achieve that state. This process involves several key components working together seamlessly.

The Pulumi SDK provides language-specific libraries that offer strongly-typed bindings for cloud resources across 170+ providers. These libraries enable developers to define infrastructure using familiar programming constructs like functions, loops, conditionals, and classes, while providing rich IDE support including IntelliSense, error checking, and refactoring capabilities.

When you run a Pulumi program, the deployment engine analyzes your code, computes the necessary changes to reach your desired state, and executes those changes in the optimal order while respecting resource dependencies. The engine maintains a detailed record of your infrastructure state, enabling features like drift detection, rollback capabilities, and collaborative workflows.

The Pulumi CLI serves as the primary interface for managing deployments, providing commands for previewing changes, executing deployments, and managing the infrastructure lifecycle. For teams requiring additional collaboration and governance features, Pulumi Cloud offers a managed service that provides centralized state management, team collaboration tools, policy enforcement, and detailed audit trails.

## Key concepts and architecture

Understanding Pulumi's architecture requires familiarity with several foundational concepts that distinguish it from traditional infrastructure tools.

**Projects and stacks** form the organizational backbone of Pulumi's approach. A project represents a directory containing your infrastructure code and metadata, while stacks provide isolated instances of your project for different environments like development, staging, and production. This separation enables teams to manage multiple environments from a single codebase while maintaining appropriate isolation and configuration differences.

**Resources** represent the fundamental building blocks of your infrastructure, from individual cloud services like AWS S3 buckets to complex, multi-resource constructs like entire application architectures. Pulumi's resource model supports both primitive resources that map directly to cloud provider APIs and component resources that encapsulate multiple resources into reusable abstractions.

**Configuration and secrets management** is handled through a sophisticated system that provides stack-specific configuration values while ensuring sensitive information remains encrypted. Pulumi ESC (Environments, Secrets, and Configuration) extends this capability by providing centralized secrets management across environments and applications, integrating with existing secret stores and identity providers.

The **state management** system maintains a comprehensive record of your infrastructure's current state, enabling Pulumi to compute the minimal set of changes needed for any deployment. Unlike some tools that store state in plain text, Pulumi encrypts sensitive information by default and provides robust state management capabilities through both local and cloud-based backends.

## The power of real programming languages

One of Pulumi's most significant differentiators is its support for general-purpose programming languages rather than domain-specific languages. This design choice has profound implications for how teams approach infrastructure management.

Using familiar programming languages means developers can apply existing skills and knowledge to infrastructure problems. They can leverage the full ecosystem of language features, including package managers, testing frameworks, and development tools. This approach eliminates the need to learn proprietary configuration languages and enables teams to create more sophisticated, maintainable infrastructure code.

The ability to use standard programming constructs like loops, conditionals, and functions enables dynamic infrastructure definitions that would be difficult or impossible with templating-based approaches. For example, you might programmatically create resources based on environment variables, implement complex business logic within your infrastructure code, or generate resources based on external data sources.

Furthermore, Pulumi's language support extends beyond basic resource definitions to include comprehensive testing capabilities. Teams can write unit tests for their infrastructure code, validate resource configurations before deployment, and implement integration tests to ensure their infrastructure behaves correctly in different scenarios.

## Multi-cloud and provider ecosystem

Pulumi's architecture supports an extensive ecosystem of cloud providers, enabling teams to adopt multi-cloud strategies or migrate between providers without rewriting their infrastructure code. The platform maintains native providers for major cloud platforms like AWS, Microsoft Azure, and Google Cloud Platform, ensuring same-day support for new cloud services and features.

This multi-cloud capability extends beyond traditional cloud providers to include specialized services like Cloudflare, Datadog, Auth0, and GitHub, as well as private cloud technologies like VMware vSphere and OpenStack. The consistent API across all providers means teams can apply the same patterns and practices regardless of their underlying infrastructure choices.

The provider ecosystem also includes community-maintained providers and the ability to create custom providers for internal services or specialized requirements. This extensibility ensures that Pulumi can adapt to virtually any infrastructure environment or organizational need.

## Open source foundation with enterprise capabilities

Pulumi's approach to open source versus commercial offerings reflects a commitment to community-driven development while providing enterprise-grade capabilities for organizations with advanced requirements.

The open source foundation includes the Pulumi CLI, SDKs for all supported languages, and a vast ecosystem of community providers. This foundation is released under the Apache 2.0 license, ensuring that core functionality remains freely available and that the community can contribute to the platform's continued development.

Pulumi Cloud provides enterprise-grade features including team collaboration tools, advanced security capabilities, compliance reporting, and governance features. These capabilities enable organizations to implement sophisticated policies, maintain audit trails, and ensure that infrastructure deployments meet regulatory and organizational requirements.

The self-hosted option allows organizations to run Pulumi entirely within their own infrastructure while maintaining access to enterprise features, addressing data sovereignty and security requirements for highly regulated environments.

## Competitive advantages and positioning

When compared to established infrastructure as code tools, Pulumi offers several distinct advantages that address common pain points in infrastructure management.

Traditional tools like Terraform require teams to learn domain-specific languages with limited expressiveness compared to general-purpose programming languages. Pulumi's approach enables teams to leverage existing language skills while providing access to the full ecosystem of development tools and practices.

The testing capabilities represent another significant advantage. While some tools offer limited testing options, Pulumi's integration with language-native testing frameworks enables comprehensive testing strategies including unit tests, integration tests, and property-based testing approaches.

Security represents a critical differentiator, particularly regarding secrets management. While some tools store sensitive information in plain text within state files, Pulumi encrypts secrets by default and provides sophisticated secrets management capabilities that integrate with existing organizational security practices.

The provider ecosystem and same-day support for new cloud services ensure that teams can take advantage of the latest cloud capabilities without waiting for provider updates or community contributions. This agility is particularly important in rapidly evolving cloud environments where new services and features are constantly being introduced.

## Real-world applications and success stories

Organizations across various industries have adopted Pulumi to address diverse infrastructure challenges, demonstrating the platform's versatility and effectiveness in real-world scenarios.

Snowflake, a leading cloud data platform, used Pulumi to reduce their deployment time from 1.5 weeks to a single day while improving reliability and maintainability. The ability to use familiar programming languages enabled their development teams to contribute directly to infrastructure management, reducing silos between development and operations.

BMW manages infrastructure for over 11,000 developers using Pulumi, leveraging the platform's collaboration features and policy enforcement capabilities to maintain consistency and security across their global development organization. The company particularly benefits from Pulumi's ability to create reusable components that encapsulate their infrastructure best practices.

Starburst achieved a 112x improvement in deployment speed, reducing deployment times from two weeks to just three hours. This dramatic improvement was enabled by Pulumi's testing capabilities and the ability to create sophisticated deployment pipelines using familiar programming languages.

These success stories demonstrate how Pulumi enables organizations to achieve significant improvements in deployment speed, reliability, and developer productivity while maintaining the security and governance capabilities required for enterprise environments.

## The future of cloud engineering

Pulumi's approach reflects broader trends in cloud engineering that emphasize developer productivity, collaboration, and the application of software engineering practices to infrastructure management. As cloud environments become increasingly complex and organizations adopt multi-cloud strategies, the need for sophisticated infrastructure management tools continues to grow.

The platform's emphasis on treating infrastructure as software aligns with the DevOps movement and the broader trend toward breaking down silos between development and operations teams. By enabling developers to contribute directly to infrastructure management using familiar tools and languages, Pulumi helps organizations achieve the collaborative, cross-functional approach that defines modern cloud engineering.

Looking forward, Pulumi continues to evolve with features like AI-powered assistance for infrastructure development, enhanced policy enforcement capabilities, and deeper integration with cloud-native development workflows. These developments position Pulumi as a platform that not only addresses current infrastructure challenges but also anticipates the needs of future cloud engineering practices.

## Getting started with Pulumi

For organizations interested in exploring Pulumi, the platform offers multiple entry points depending on your current infrastructure management approach and technical requirements.

Teams with existing infrastructure can leverage Pulumi's import capabilities to bring existing resources under management without disrupting current operations. This approach enables gradual adoption where teams can start with new projects while progressively migrating existing infrastructure.

The extensive library of example programs and templates provides starting points for common infrastructure patterns, enabling teams to quickly understand best practices and adapt them to their specific requirements. These examples span multiple cloud providers and use cases, from simple web applications to complex multi-tier architectures.

For teams with specific requirements or complex existing infrastructure, Pulumi offers professional services and consulting to help organizations design and implement infrastructure strategies that align with their business objectives and technical constraints.

## Conclusion

Pulumi represents a fundamental shift in how organizations approach cloud infrastructure management, moving beyond the limitations of domain-specific languages and templating systems to embrace the full power of modern software development practices. By treating infrastructure as software, Pulumi enables teams to leverage existing skills, tools, and workflows while providing the advanced capabilities required for modern cloud environments.

The platform's combination of open source foundation and enterprise capabilities ensures that it can serve organizations of all sizes, from startups building their first cloud applications to large enterprises managing complex multi-cloud environments. As cloud infrastructure continues to evolve in complexity and importance, Pulumi's approach to infrastructure as software positions it as a crucial tool for organizations seeking to maximize the value of their cloud investments while maintaining the agility and reliability required for modern business operations.

Whether you're a developer looking to apply your programming skills to infrastructure problems, an operations team seeking better collaboration with development teams, or an organization pursuing a comprehensive cloud engineering strategy, Pulumi offers a path forward that embraces the best practices of modern software development while addressing the unique challenges of cloud infrastructure management.

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
