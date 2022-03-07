---
title: Accelerating Enterprise Innovation through Cloud Engineering
description: |
    Pulumi is a cloud engineering platform that gives enterprises a unified process for delivering infrastructure and applications for greater innovation velocity.
meta_desc: |
    Pulumi is a cloud engineering platform that gives enterprises a unified process for delivering infrastructure and applications for greater innovation velocity.
customer_name: Enterprise Whitepaper
customer_logo:
customer_url:

exec_summary: |
    Enterprises are facing an unprecedented challenge of delivering business innovation and customer value more quickly and at high scale. They must tame complexity across hybrid clouds and increase reliability and security across the organization in order to accelerate release velocity and match the scale of customer demand. Enterprises are faced with managing disparate teams across infrastructure, development, and compliance using countless technologies and tools to deliver and manage infrastructure critical for business innovation. Cloud engineering is the practice of applying software engineering to tame the complexity of delivering and managing modern cloud applications.

    In this whitepaper, we will look at the implications of cloud engineering and present solutions for adopting cloud engineering to fully maximize the benefits of the modern cloud and capitalize on software engineering as a lever for digital transformation.

sections:
    - label: Executive Summary
      anchor: executive-summary
    - label: Introduction to Cloud Engineering
      anchor: introduction-to-cloud-engineering
    - label: Accelerating Innovation through Cloud Engineering
      anchor: accelerating-innovation-through-cloud-engineering
    - label: The Cloud Engineering Journey
      anchor: the-cloud-engineering-journey
    - label: Success Stories
      anchor: success-stories
    - label: Conclusion
      anchor: conclusion
---

## Introduction to Cloud Engineering

Since the early 2010s, enterprises have embarked on a migration from on-premises data centers to the cloud. This shift was driven by 1/ the business needs of increasing innovation and reducing costs, 2/ satisfying increased customer needs for access to their products or services, and 3/ the inability to scale to compete with other businesses who had more resources. The cloud provided on-demand infrastructure that allowed near-infinite scalability, reduction of upfront infrastructure capital expenditures, increased availability and uptime of infrastructure, and global geographic reach. The practice of DevOps and tools like Infrastructure as Code were employed to automate the complexity of VM-centric deployments and infrastructure.

During that migration, businesses drove innovation through software engineering, which enabled companies to meet customer demand for increased reliability and increase the speed to market. To support the needs of software engineering, cloud architectures also evolved with the introduction of new technologies like containerization, microservices, Kubernetes, and serverless systems. This shift to a world where the business capabilities defined services drove an increase in the number of cloud services and APIs that make up an application, and that number continues to grow exponentially. This evolution forms what we know today as the modern cloud. In addition, the traditional line between development and operations has blurred with the rise of shared responsibility for services brought by DevOps cultures. Operations and infrastructure teams have shifted to providing platform-like systems or applying software engineering practices to cloud infrastructure, all driven by the rise in API capabilities with cloud services that enables more automation and more code-based management. As a result, developers are increasingly involved in the provisioning of infrastructure. Meanwhile, compliance teams have gained more insight into the software development lifecycle and the cloud itself through those same APIs, enabling security and compliance through automation and code.

As these changes in organization, process, and tooling happened, a new order of problems started to emerge. The need to utilize these new architectures and technologies cause the management of infrastructure spanning multiple clouds, including existing on-premises private clouds, to become increasingly fragmented and complex. Developers who now need to work more closely with infrastructure face significant learning curves. Infrastructure teams managing service-level agreements and defining reliability best practices face further difficulty from the complexity and scale. Compliance and security teams enforcing policies at scale across the entire organization need to do so without slowing down development velocity. The existing processes of DevOps and legacy Infrastructure as Code tools are not equipped to keep up with these changes and solve these problems. Delivery and innovation velocities experience slowdowns as a result.

Against these challenges, new best practices started to develop amongst enterprises. Infrastructure, development, and compliance teams must work as one organization to deliver and manage modern cloud applications. Those best practices are collectively known as cloud engineering, and the goal of cloud engineering is to tame the complexity of the modern cloud and increase innovation velocity. There are three pillars of practices to cloud engineering:  build, deploy, and manage.

### Build

Cloud engineering teams define cloud infrastructure using standard programming languages, which gets them access to constructs like conditionals, loops, functions, and classes. Programming languages have been built over multiple decades to tame complexity at scale—the very complexity modern cloud architectures operating at global scale need to tackle.  Teams can share and reuse common infrastructure components, just like they would any software package. This practice significantly improves the ability to cut down on boilerplate and to enforce best practices. The use of standard programming languages allows infrastructure development to leverage IDEs, test frameworks, and package managers.

### Deploy

Cloud engineering teams deliver both infrastructure and application code through a unified process that increases efficiency and quality. Unit, property, and integration tests are run to validate infrastructure changes before deploying to production, reducing errors and increasing deployment confidence. Teams also programmatically deploy infrastructure through APIs or orchestration workflows, moving away from CLI-driven workflows. Infrastructure changes are tracked with end-to-end change histories with the ability to easily roll back changes if needed.

### Manage

Cloud engineering teams manage and secure their cloud infrastructure and applications through repeatable, auditable code and management processes that enable visibility. Teams use policy-as-code as programmable guardrails to enforce security, best practices, and cost across all infrastructure. Auditing controls that track all cloud resource changes across all cloud infrastructure enable faster, more reliable compliance even across the most complex of architectures and deployments. Finally,enabling deeper visibility increases collaboration between infrastructure, development, and compliance teams by reducing miscommunication and friction among teams.<br>

---

Cloud engineering is a practice that provides a blueprint on the processes to employ in order to use software engineering across infrastructure, development, and compliance teams to transform the way infrastructure is managed. The next section discusses the tools needed to make it easier to adopt the practices.

## Accelerating Innovation through Cloud Engineering

Pulumi is a cloud engineering platform that enables enterprises to use an unified software engineering process to deliver infrastructure and applications together and faster. It brings together infrastructure, development, and compliance teams through the entire cloud engineering lifecycle. Pulumi provides developer-first infrastructure as code that allows organizations to build, deploy, and manage cloud infrastructure with popular programming languages including Python, JavaScript, TypeScript, Go, and .NET/C#. Organizations can deploy cloud infrastructure and applications together using a unified delivery process and automation with fine-grained visibility and controls. Pulumi provides advanced security and compliance features, premium support, and self-hosting options to support the most sophisticated production workloads in the modern cloud.

### Pulumi spans the entire cloud engineering lifecycle

Pulumi is designed as a platform to manage the cloud engineering lifecycle for any enterprise. Infrastructure teams and developers are empowered to __build__ infrastructure as code in familiar programming languages. They can use TypeScript, JavaScript, Python, Go, and .NET to model cloud infrastructure by leveraging the features of each language, and they can build on any cloud by accessing the full breadth of services in AWS, Azure, GCP, and 60+ providers through a complete and consistent SDK interface. Infrastructure and compliance teams can encapsulate cloud architectures and best practices as reusable Pulumi Packages and share reusable infrastructure that can be used anywhere in the organization.

Pulumi enables infrastructure teams and developers to __deploy__ cloud infrastructure and applications together. Every infrastructure change can be tested and validated using standard unit test frameworks and integration tests, reducing errors in infrastructure deployments. With Pulumi, infrastructure can be deployed interactively with a CLI, programmatically through Pulumi’s Automation API, or through standard CI/CD processes.

Compliance and infrastructure teams can __manage__ cloud infrastructure and applications with greater visibility and controls. They can enforce server-side, organization-wide policies, including compliance and security best practices, network access restrictions, and cost controls. Enterprises can also control access to sensitive data and operations through fine-grained roles across the entire organization and for specific projects. Pulumi offers federated services for enterprises to leverage existing SAML 2.0 and Single Sign-On (SSO) investments and uses the System for Cross-domain Identity Management (SCIM) protocol for automatic identity synchronization with systems like Microsoft Active Directory, Google G Suite, and Okta, among others. All activity within Pulumi is automatically recorded with the ability to export logs for integration with other security and compliance partners.

Enterprises that require specific data controls can use the self-hosted Pulumi service in their own cloud or datacenter and maintain complete control over their hosting, network isolation, identity, and data ownership. Deployment options include Kubernetes clusters, VMWare vSphere, virtual private clouds in AWS, Azure, Google Cloud, and many other configurations. Pulumi runs in an AWS VPC, and the architecture follows industry best practices. All network communication is encrypted using TLS, and Pulumi’s endpoints are only accessible via HTTPS. Data is encrypted at rest, and Pulumi is compliant with SOC 2 Type II. Pulumi also provides a range of support options, such as dedicated 24x7 support, premium training, onboarding, and professional services.

The new order of problems that come with the adoption of the modern cloud—multi-cloud complexity, repeatability risks, security and reliability, velocity slowdowns—can be solved through cloud engineering empowered by the Pulumi platform. __Pulumi tames modern cloud complexity.__ It provides one consistent approach to accessing over 60 cloud providers and works for the entire enterprise as each team scales up. __Pulumi reduces risk through automation.__ Enterprises can leverage a rich and programmable cloud interface with reusable packages that abstract away complexity to increase consistency and reduce maintenance across infrastructure. __Pulumi provides better guardrails for reliability and security.__ Pulumi also fosters collaboration between developers, infrastructure teams, and security engineers using Policy as Code to ensure cloud services and resources are used in a secure, consistent, and well-architected way. Lastly, __Pulumi accelerates development velocity.__ Enterprises can employ software engineering practices with Infrastructure as Code—including modularity, testing, and CI/CD—to reduce deployment risks and increase development velocity.

Pulumi accelerates innovation for enterprises because it allows enterprises to fully maximize the benefits of the modern cloud and capitalize on software engineering as a lever for digital transformation. The next section discusses the steps that should be taken to employ cloud engineering.

## The Cloud Engineering Journey

There are three stages to adopting cloud engineering successfully. Each stage comes with certain process and organizational mindsets/objective changes. Different components of the Pulumi platform support different parts of the journey. While not every stage needs to be implemented to be successful with cloud engineering, progressing further through each stage maximizes the benefits—reduction of complexity and risk, increased reliability and security, and acceleration of development velocity—received through cloud engineering.

### Stage 1:  Infrastructure and Policy as Code

The foundation of cloud engineering is infrastructure and policy as code. This foundation involves the process of provisioning and managing infrastructure and enforcing policy through programmatic code stored in version control systems. Infrastructure as code provides automation to provision infrastructure and increases delivery velocity by removing the risk of human errors. Policy as code sets guardrails to enforce compliance for every provisioned resource in the organization.

In Stage 1, Pulumi acts as a single interface across thousands of resources spanning multiple clouds and SaaS providers, and that single interface decreases cognitive load for developers when managing resources. Compliance teams can use policy as code to enforce cost, security, and best practices across all infrastructure. The organizational objective is to empower the provisioning of infrastructure with guardrails and thereby increase security and compliance and enable better cost controls.

#### Building greenfield applications

The first step of Stage 1 is to apply infrastructure as code to new greenfield applications. Teams can engineer new projects from the ground up using infrastructure as code. With Pulumi, new projects can immediately achieve the benefits of infrastructure and policy as code. Security and compliance can be enforced through Pulumi CrossGuard. Project costs can be closely monitored to stay within budgets. Because Pulumi enables teams to build infrastructure alongside their applications with the same programming languages, infrastructure needs can grow with a greenfield application, ensuring it stays compliant and secure throughout the entire project lifecycle.

#### Working in hybrid environments

Enterprise infrastructure spans across private and public clouds. Managing the hybrid infrastructure with one consistent workflow is important for reducing complexity and streamlining processes. With Pulumi, enterprises can use the same tool and process to run workloads on-premises as well as on the public clouds without sacrificing the ability to leverage each cloud’s unique features and capabilities. Applying a consistent approach for infrastructure as code, policy as code, and CI/CD gives enterprises better visibility and control while reducing fragmentation for teams.

#### Migrating legacy infrastructure as code tools

Many enterprises have existing legacy infrastructure as code tools. Many of these tools don’t have the ability to build and provision at the scale and complexity of modern cloud architectures or lack the ability to create custom infrastructure management workflows. Pulumi provides conversion tools that allow enterprises to convert templates written in Terraform HCL, Kubernetes YAML, and Azure ARM into Pulumi programs. This conversion capability preserves existing program structure, such as code layout in terms of names, modules, and configurability, while automatically generating a new, fully-functional Pulumi program that matches the source infrastructure as code program.

#### Managing secrets

Implementing infrastructure as code also means managing secrets (e.g., database passwords, SaaS tokens, credentials files) used to access shared infrastructure resources in an organization. At scale, enterprises employing modern cloud architectures have exponentially increasing diversity of sources requiring secrets that become increasingly difficult to securely store and audit. Security is priority number one for enterprises, and exposure of secrets can have devastating consequences like data leakage and privacy breaches. Pulumi supports secrets as a first-class primitive within Pulumi. It encrypts secrets in transit and at rest, and anything a secret touches (e.g., CLI outputs, Pulumi logs, Pulumi program, state file) is tainted and gets encrypted, which prevents enterprises from accidentally disclosing a secret. Every stack has its own encryption key. Pulumi also provides an extensible encryption facility that allows enterprises to elect to use their own keys managed by a third-party solution.

#### Setting up role-based access controls

Empowering developers to provision infrastructure requires proper authentication and access controls. Enterprises can leverage their existing SAML 2.0 and Single Sign-On (SSO) solutions and use the System for Cross-domain Identity Management (SCIM) protocol for automatic identity synchronization with systems like Microsoft Active Directory, Google G Suite, and Okta. They can also control access to sensitive data and infrastructure management operations through fine-grained roles across the entire organization and for specific projects. Pulumi automatically records all activity and exports the logs to security and compliance tools.

### Stage 2:  Infrastructure CI/CD

[Infrastructure CI/CD]({{< relref "/solutions/infrastructure-ci-cd" >}}) is the process of automating the testing, provisioning, and management of infrastructure through a software delivery pipeline. Infrastructure CI/CD further automates infrastructure provisioning and management from Stage 1 by building the entire IaC process into a CI/CD pipeline. In Stage 2, all infrastructure updates run through a standard set of unit and integration tests, allowing reduced mean time to resolution, increased reliability, and increased delivery velocity.

In modern cloud architectures, the division between application and infrastructure is increasingly blurred. Constructing infrastructure alongside applications and delivering them together creates higher levels of efficiency and reliability. With Pulumi, infrastructure can be modeled with the same programming language used by the application code and delivered through the same CI/CD system. The organizational objective is to deliver software, both the application and infrastructure, daily and scale infrastructure managed as code from tens to thousands of environments.

#### Setting up CI/CD pipelines

CI/CD automates the software release process and eliminates manual tasks to deliver updates faster and find and address bugs quicker. As with applications, infrastructure delivery also receives the same benefits when CI/CD is applied. With Pulumi, enterprises can take advantage of native testing frameworks and perform automated tests of their infrastructure because Pulumi uses general purpose programming languages to provision cloud resources. Pulumi provides unit tests (fast in-memory tests that mock all external calls), property tests (run resource-level assertions while infrastructure is being deployed), and integration tests (deploy ephemeral infrastructure and run external tests against it). Pulumi integrates with existing CI/CD providers including AWS Code Services, Azure DevOps, CircleCI, CodeFresh, GitHub Actions, GitLab Pipelines, Google Cloud Build, Jenkins, Octopus Deploy, Jetbrains TeamCity, Spinnaker, and TravisCI. Pulumi also supports GitOps workflows in Kubernetes through the Pulumi Kubernetes Operator.

#### Securing the pipeline

Providing granular access controls for infrastructure delivery is the next step for enterprises once infrastructure changes are delivered through a CI/CD pipeline. Pulumi enables fine-grained access controls to secure pipelines. Enterprises can lock down all production deployments and ensure only authorized users are allowed to perform infrastructure changes to production environments, ensuring consistent and secure infrastructure CI/CD.

#### Performing end-to-end change management

Enterprises require end-to-end visibility into infrastructure changes in order to maintain security and compliance. Pulumi keeps track of which user changed what and when by associating source code changes with cloud resource changes all the way to the actual modifications made to cloud environments. By using Pulumi SSO capabilities at all stages in the delivery pipeline—from source to deployment—enterprises have visibility and control into all production infrastructure changes, assisting with live-site debugging, change control, auditing, and more.

### Stage 3:  Shared Services Platforms

Stage 3 builds upon the foundations of Stages 1 and 2 by taking automated pipelines for deploying infrastructure managed by code and building a platform with shared resources, self-service components, and automated deployments. [Shared Services Platforms (SSPs)]({{< relref "/solutions/shared-services-platforms" >}}) are an internal company service that allows application developers to request and manage infrastructure environments by themselves. SSPs are the best practice to share common infrastructure and automate the provisioning of infrastructure for development teams. They abstract away the complexity of the cloud for developers, reduce deployment risks through automation, and increase reliability and security through building blocks with centrally enforced policies.

In Stage 3, Pulumi makes it easy to model and provision the SSP control plane as well as automate the provisioning of the data plane stacks. SSPs maintain centralized control over security and compliance while developers can directly access and deploy to infrastructure without contacting operations or cluster managers. The organizational objective is to achieve self-service infrastructure without disrupting existing developer workflows.

#### Defining shared services

The first step is to define the common infrastructure components or resources that will be shared across the platform and by all the developers (end users). Then, define the infrastructure components/resources that are configured and managed by the developer. Next, define the boundary between the platform space and end user space, which is how the developer will access the shared resources (e.g., via StackReference). Finally, define how developers will interact with the platform. This interaction may be through a self-service portal where they can pick and choose their infrastructure, a GitOps workflow, or directly with a CI/CD pipeline.

#### Sharing and reusing well-architected building blocks

With the definitions in place, code for the shared platform components should be written first followed by the code for the application components that can be selected and used by developers. These application components will have the logic to retrieve credentials or connect to the shared resources in the platform.

Pulumi promotes creating reusable and modular components which allows standard and well-architected infrastructure building blocks to be templatized and easily reused. Pulumi Packages enable shared platform components and application components to be abstracted and encapsulated. These components have a trackable state, appear in diffs, and use a logical name that tracks the resource identity across deployments. The components can be authored in one language and be accessible in all the other languages that Pulumi supports, enabling adoption by developers that have different language preferences and expertise. Pulumi also provides the Pulumi Registry, which is a searchable collection of Pulumi Packages published by Pulumi and its partners. With Pulumi Registry, developers can easily find the package with the resources they need, install that package directly into their project, and start building.

#### Establishing software supply chain

The next step after building reusable and modular components is establishing a secure software supply chain for each of the components. Enterprises broadly implement software versioning and supply chain for application development. Pulumi brings true software versioning and a secure software supply chain to the way organizations manage infrastructure. Legacy markup and DSL toolchains have limited supply chain capabilities leading to configuration drift and insecure practices. Teams often copy-and-paste configuration changes, and when critical security misconfigurations happen in an environment, they need to manually track down all places in which the same configuration mistakes were copied. With Pulumi, an infrastructure change is versioned just like software. Out-of-date versions can be audited the same way, and rollouts can be performed using standard release techniques, giving teams confidence they aren’t running out of date configurations.

#### Automating and orchestrating the control plane

SSPs have a control and data plane. The control plane exposes the interface that users interact with and orchestrates the provisioning of infrastructure requested. The data plane is the shared platform components or application components used by developers. The Pulumi Automation API allows the embedding of Pulumi programs directly into the application code of the SSP control plane. The Automation API is a strongly typed, programmatic interface for running Pulumi programs without the Pulumi CLI. With the Automation API, enterprises can build control planes that natively execute Pulumi programs to provision data plane infrastructure components. No other infrastructure as code tool has this capability.

---

Pulumi provides a platform that supports all stages of the cloud engineering journey with each stage progressively unlocking greater benefits of the modern cloud. Enterprises rely on Pulumi as a trusted advisor and partner through this entire journey.

## Success Stories

Organizations of all sizes, from startups to the Global 2000, have chosen Pulumi for their cloud engineering and modernization needs. Below is a list of customers and their transformational stories.

### Snowflake

Snowflake’s platform team enabled its developers to deploy standardized Kubernetes environments across AWS, Azure, and Google Cloud with a self-service platform that’s powered by Pulumi and Golang. [Read the case study]({{< relref "/case-studies/snowflake" >}}).

### Mercedes-Benz

Mercedes-Benz Research & Development North America and its platform team enabled developers to deploy standardized Kubernetes environments on Azure with a self-service platform.
[Read the case study]({{< relref "/case-studies/mercedes-benz" >}}).

### Atlassian

Atlassian Bitbucket reduced its developers’ time spent on cloud maintenance by 50% through creating a self-service platform that deploys standard development environments for Bitbucket. [Read the case study]({{< relref "/case-studies/atlassian" >}}).

### Skai

Skai’s DevOps group migrated a core monolith service from its private cloud to AWS, and it refactored its infrastructure codebase to use standard programming languages like Python by using Pulumi. [Read the case study]({{< relref "/blog/kenshoo-migrates-to-aws-with-pulumi" >}}).

### SANS Institute

SANS Institute’s DevOps team reduced deployment times for a key service by up to 70% by moving from a domain-specific language to Pulumi and implementing software engineering practices like Git and CI/CD. [Read the case study]({{< relref "/case-studies/sans-institute" >}}).

## Conclusion

Cloud engineering is the logical paradigm for enterprises looking to maximize their infrastructure investments and accelerate business innovation. Pulumi provides an end-to-end solution for unifying infrastructure, development, and compliance teams to deliver cloud infrastructure and applications at high velocity and scale. Pulumi is a trusted advisor and partner for enterprises going through the cloud engineering journey. Organizations from high growth startups to the Global 2000 have chosen Pulumi to tame cloud complexity, reduce risk through automation, increase reliability and security, and accelerate development velocity.
