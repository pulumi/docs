---
title: What is DevOps?
meta_desc: |
    Understand what is DevOps, Understand key practices of CI/CD, automation, infrastructure testing and security
type: what-is
page_title: "What is DevOps"
---

DevOps integrates the historic siloed disciplines of software development (Dev) and IT operations (Ops) as a methodology and culture shift that aligns people, processes, and technology in the lifecycle of application planning, development, delivery, and operations. For teams that successfully break down these silos and invest in the process and tools, they realize they can respond much more quickly to customer needs and improve products much faster than traditional methods have allowed. Additionally, DevOps practices lead to more reliable and secure software, enabling organizations to adapt swiftly to the pace of technology and market changes.

In this article, we'll touch on the following key areas regarding DevOps:

* DevOps essentials
* DevOps key terms and tools
* DevOps implementation

## Essentials of DevOps

* **Infrastructure as code (IaC)**: [IaC](/what-is/what-is-infrastructure-as-code/) is a key DevOps practice that involves using code and automation to define and manage your infrastructure rather than manual processes. Traditionally, infrastructure management was more manual and less consistent. Methods ranged from manual configurations via user interfaces or command-line interfaces, to less dynamic scripting or basic configuration tools. These methods often lead to challenges in maintaining consistency, scalability, and efficiency, especially as the complexity and size of infrastructures grows. With IaC, your infrastructure becomes versionable, [testable](/what-is/how-to-step-up-cloud-infrastructure-testing/), and repeatable. Infrastructure code can be packaged and shared both within the company and with the broader community. Many Infrastructure as code tools require you to use domain-specific languages, but tools with a modern approach such as [Pulumi](https://www.pulumi.com/), allow you to use general-purpose languages and apply software engineering practices to your infrastructure.

* **Continuous integration and continuous delivery (CI/CD)**: Continuous integration (CI) and continuous delivery (CD) are interconnected practices that streamline the software development process. CI involves developers frequently merging code changes into a central repository where automated builds and tests are conducted to identify and fix bugs swiftly, thus enhancing software quality and shortening the update validation period. CD builds on CI's foundation, automatically building, testing, and preparing code for release. It further automates the deployment of these changes to various testing or production environments, ensuring that the code is not just ready for deployment but is continuously delivered to production with minimal manual intervention. This creates a deployment-ready build artifact that has been rigorously tested, facilitating frequent and stable releases, with monitoring systems in place to ensure transparency throughout the process. [Learn more about Pulumi’s CI/CD integration](/docs/guides/continuous-delivery/).

* **Version control and change management**: Version control is crucial in DevOps, not just for managing software code but also for deploying using infrastructure as code (IaC). By applying version control to IaC processes, teams gain the ability to track changes, collaborate effectively, and quickly revert to previous states of the infrastructure, ensuring consistency and reliability in both application development and the environments where these applications are deployed. This unified approach to version control across software and infrastructure fosters better alignment, efficiency, and quality assurance in the delivery pipeline. Learn more about [Version control in Pulumi](/docs/intro/concepts/state/#backends).

* **Testing infrastructure as code**: [Testing infrastructure as code](/docs/using-pulumi/testing/) (IaC) in DevOps is similar to testing applications using standard testing tools for various test types. Unit tests swiftly validate code segments without real infrastructure, relying on the same programming language as the IaC programs. Property tests take a step further by provisioning real infrastructure to check resource configurations before and after deployment. Integration tests comprehensively establish a temporary infrastructure setup to verify end-to-end functionality, particularly useful in CI/CD workflows. For more robust testing, one might employ fuzz testing to challenge the infrastructure with unexpected inputs, chaos testing to assess resilience by intentionally causing disruptions, and stress testing to push the system to its limits. These advanced tests, enabled by the flexibility of using general-purpose languages for IaC, provide a wide array of tools to ensure the infrastructure's integrity and robustness.

* **Policy as code**: Policy as code refers to the practice of writing high-level policy descriptions in a language that can be processed by a computer. Instead of manually maintaining compliance documentation and procedures, policies are managed in version-controlled systems and integrated into the development and deployment lifecycle. This enables automatic and continuous enforcement of policies, providing a clear, auditable trail of compliance and security practices. Policy as code is an essential part of modern cloud infrastructure, ensuring that policies are consistently applied across all environments and enabling quicker response to policy violations. Learn more about [Policy as code in Pulumi](/docs/guides/crossguard/)

## DevOps terms and tools

The following terms provide a foundational understanding of the key concepts and practices in the field of DevOps.

| Topic | Description | Tools |
|-------|-------------|-------|
| Agile methodology | A set of principles for software development under which requirements and solutions evolve through the collaborative effort of cross-functional teams. Agile advocates adaptive planning, evolutionary development, early delivery, and continual improvement, and it encourages flexible responses to change. | [Scrum](https://www.scrum.org/), [Kanban](https://www.atlassian.com/agile/kanban) |
| Configuration management | The process of systematically handling changes to a system in a way that it maintains integrity over time, often involving tools that automate the deployment and configuration of applications and systems. | [Pulumi ESC](/product/esc/), [Ansible](https://www.ansible.com/) |
| Containerization | The use of containers to encapsulate an application with its own operating environment. This is useful for consistency across multiple development and release cycles, promoting immutability and portability. | [Docker](https://www.docker.com/), [Podman](https://podman.io/) |
| Continuous deployment | An extension of continuous delivery, where every change that passes the automated tests is deployed to production automatically, without explicit approval from a developer, making the deployment process fully automated. | [Pulumi Deployments](/docs/pulumi-cloud/deployments/) |
| Continuous delivery (CD) | A software engineering approach in which teams produce software in short cycles, ensuring that the software can be reliably released at any time. It aims at building, testing, and releasing software with greater speed and frequency. | [Codefresh](https://codefresh.io/docs/docs/getting-started/cd-codefresh/), [AWS CodePipeline](https://aws.amazon.com/codepipeline/) |
| Continuous integration (CI) | A development practice where developers integrate code into a shared repository frequently, ideally several times a day. Each integration is verified by an automated build, allowing teams to detect problems early. | [Jenkins](https://www.jenkins.io/), [CircleCI](https://circleci.com/) |
| Continuous testing | The process of executing automated tests as part of the software delivery pipeline to obtain immediate feedback on the business risks associated with a software release candidate. | [Selenium](https://www.selenium.dev/), [Appium](https://appium.io/docs/) |
| DevOps culture | The set of practices that brings the development and operations teams together to collaborate throughout the entire software lifecycle, from development and testing to deployment and operations. | [O'Reilly Library](https://www.oreilly.com/library/view/building-a-devops/9781449368340/), [Pluralsight](https://www.pluralsight.com/courses/implementing-devops-real-world) |
| Microservices | An architectural style that structures an application as a collection of services that are highly maintainable and testable, loosely coupled, independently deployable, and organized around business capabilities. | [Kubernetes](https://kubernetes.io/), [AWS SQS](https://aws.amazon.com/sqs/) |
| Version control | A system that records changes to a file or set of files over time so that you can recall specific versions later. It's a fundamental tool for enabling collaboration, ensuring traceability, and managing code for teams. | [Git](https://git-scm.com/), [Subversion](https://subversion.apache.org/) |

## DevOps implementation

Implementing and scaling a culture of DevOps is enabled by tools that can reliably and securely deploy solutions to meet the needs of your customers. Pulumi provides the best tools to implement DevOps successfully and build your infrastructure as code in any programming language. You can use Pulumi’s [open source SDK](https://github.com/pulumi/pulumi) to provision infrastructure on any cloud, and securely and collaboratively build and manage infrastructure using Pulumi Cloud, which is available for unlimited free usage and has a free tier for teams and offers advanced editions for larger teams and enterprises.

For a detailed exploration and implementation of DevOps practices, refer to the following Pulumi tools and resources:

* **Infrastructure as code (IaC)**: Start with Infrastructure as Code using Pulumi by accessing our [getting started guide](https://www.pulumi.com/docs/get-started/).

* **Continuous integration and continuous delivery (CI/CD)**: For integrating CI/CD processes with Pulumi, visit our [CI/CD integration documentation](https://www.pulumi.com/docs/guides/continuous-delivery/).

* **Policy as code**: To manage policies using Pulumi CrossGuard, visit the [Pulumi CrossGuard documentation](https://www.pulumi.com/docs/guides/crossguard/).

* **Version control**: Learn about version control systems supported by Pulumi in our [version control documentation](https://www.pulumi.com/docs/intro/concepts/state/#backends).

## Learn more

Pulumi offers a truly modern approach to implementing DevOps practices and infrastructure as code. With Pulumi, you can create, deploy, and manage infrastructure on any cloud using the programming languages and tools you already know. [Get started today](/docs/get-started/).
