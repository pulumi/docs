---
title: What is Continuous Integration/Continuous Delivery (CI/CD)?
meta_desc: |
    Learn about CI/CD practices that improve dev process with automation for effective, rapid software delivery.
type: what-is
page_title: "What is Continuous Integration/Continuous Delivery (CI/CD)?"
---

Continuous integration/continuous delivery (CI/CD) is a methodology in software development that emphasizes frequent, automated integration of code changes into a shared repository, followed by automated and reliable software release processes. As a foundational component of [modern DevOps practices](/what-is/what-is-devops/) CI/CD practices and tools increase efficiency, reduce bugs, and enable faster release cycles, thereby enhancing overall software quality and accelerating time-to-market for new features.

In Continous Integration (CI), developers frequently merge code changes, often multiple times a day, which are immediately tested to identify and fix integration issues early. Continuous Delivery (CD) builds on this by ensuring that the codebase is always in a deployable state, automating the deployment process to enable rapid and safe release to production. This approach enables developers to deliver features and fixes more quickly and reliably, reducing manual efforts and enhancing the quality of software deployments.

In this article, we'll touch on the following key areas:

* CI/CD essentials
* CI/CD key terms and tools
* CI/CD best practices

### What is CI/CD - essentials

CI/CD comprises two software development practices that work in tandem to improve software development and deployment processes.

### What is continuous integration (CI)

Continuous integration (CI) is a development practice that encourages frequent integration of tested code changes into a shared code repository.

Developers submit the new code changes, and automated builds and tests are triggered to ensure the new code integrates with the existing codebase. A test can be a simple code linter or a more complex process like checking for security vulnerabilities. Proper tests, including unit, integration, and regression tests, are standard in CI.

### What is continuous delivery (CD)

In continuous delivery (CD), developers ensure that software is consistently maintained in a deployable state by automating various release process stages, including testing, deployment, and configuration. A release typically consists of a set of new features, improvements, bug fixes, or other changes that have been implemented since the previous release. Release creation may require bundling configuration files, binaries, and other artifacts such as certificates. The new release may be intended for end-user consumption, where it is deployed to production environments, or it may undergo user acceptance testing (UAT) before being released to a broader audience. CD facilitates the automation of these processes.

### What is continuous deployment?

You may have also heard the phrase "continuous deployment." Continuous deployment encompasses the automatic release of software to production. It deploys the packaged code and makes the application available to end users.

To add continuous deployment to our Hello World example, we'd take the latest Docker image tag and deploy it in a running container so that end users can take advantage of the new code changes. However, let's first learn about pipelines before we show you how to do so.

### What is a CI/CD pipeline?

The sequential nature of continuous integration, delivery, and deployment practices creates a symbolic pipeline, hence the CI/CD pipeline.

A pipeline is the deployable unit path for CI/CD. A pipeline starts when code is committed to a repository like GitHub. The next step is a notification to a build system, such as [GitHub Actions](https://docs.github.com/en/actions). The build system compiles the code and runs unit tests. Integration tests are the next step if your code passes the unit tests. If your code passes both unit and integration tests, the images will be created and pushed into a registry service in the case of containers. This is the simplest example of a pipeline. Still, you can do many more things, such as security scans, check modules for CVEs (Common Vulnerabilities and Exploits), send Slack notifications, and run quality checks. A pipeline can be fully automated or have checkpoints that require approval before resuming.

### CI/CD terms and tools

The following terms provide a foundational understanding of the key concepts and practices in the field of CI/CD.

| Topic | Description | Tools |
|-------|-------------|-------|
| Build automation | The process of automating the creation of a software build and the associated processes including compiling computer source code into binary code, packaging binary code, and running automated tests. | [Docker](https://www.docker.com/), [GitHub Actions](https://github.com/features/actions) |
| Continuous deployment | An extension of continuous delivery, where every change that passes the automated tests is deployed to production automatically, without explicit approval from a developer, making the deployment process fully automated. | [Pulumi Deployments](/docs/pulumi-cloud/deployments/) |
| Continuous delivery (CD) | A software engineering approach in which teams produce software in short cycles, ensuring that the software can be reliably released at any time. It aims at building, testing, and releasing software with greater speed and frequency. | [Codefresh](https://codefresh.io/docs/docs/getting-started/cd-codefresh/), [AWS CodePipeline](https://aws.amazon.com/codepipeline/), [GitHub Actions](https://github.com/features/actions) |
| Continuous integration (CI) | A development practice where developers integrate code into a shared repository frequently, ideally several times a day. Each integration is verified by an automated build, allowing teams to detect problems early. | [Jenkins](https://www.jenkins.io/), [CircleCI](https://circleci.com/) |
| Continuous testing | The process of executing automated tests as part of the software delivery pipeline to obtain immediate feedback on the business risks associated with a software release candidate. | [Selenium](https://www.selenium.dev/), [Appium](https://appium.io/docs/en/2.2/) |
| Feature flagging | A technique that allows developers to turn certain functionalities on and off, typically used in a continuous delivery environment. | [LaunchDarkly](https://launchdarkly.com/), [FeatureToggle](https://featuretoggle.org/) |
| Test automation | Using special software to control the execution of tests and the comparison of actual outcomes with predicted outcomes. | [Selenium](https://www.selenium.dev/), [JUnit](https://junit.org/junit5/) |
| Version control systems (VCS) | Systems that record changes to a file or set of files over time so that you can recall specific versions later. | [Git](https://git-scm.com/), [Subversion](https://subversion.apache.org/) |

## Best practices for CI/CD pipelines

To build an effective CI/CD pipeline, platform and development teams must adopt and invest in DevOps best practices.

* **Use a single repository** - Maintain a centralized repository containing all the necessary files, scripts, source code, and resources for the build and deployment processes.
* **Adopt [trunk-based development](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development)**  - Integrate code changes regularly into the main branch to avoid complex merges and ensure a continuous flow of minor, incremental updates.
* **Automate the build** - Automatically compile code to catch errors early and use tools to check and improve code standards.
* **Include comprehensive testing** - Implement automated testing at various levels (unit, integration, and end-to-end) to ensure code quality and functionality.  Integrate tools to identify and fix security vulnerabilities.
* **Deploy stable environments** - Automate setting up and deploying to different environments such as development, QA, pre-production, and production.
* **Perform routine deployments** - Deployments ought to be familiar enough for the team to execute them confidently at any time. Opting for frequent deployments with minimal changes reduces risks and allows straightforward rollback procedures when needed.
* **Provide team-wide visibility** - Integrate monitoring tools to receive real-time application performance feedback, helping you promptly identify and resolve issues.
An effective CI/CD pipeline automates and streamlines software development and delivery, ensuring rapid and reliable releases with high code quality.

For a detailed exploration and steps to implement CI/CD and DevOps practices, refer to the following Pulumi tools and resources:

* **Continuous integration and continuous delivery (CI/CD)**: For integrating CI/CD processes with Pulumi, visit our [CI/CD integration documentation](https://www.pulumi.com/docs/guides/continuous-delivery/).

* **Policy as code**: To manage policies using Pulumi CrossGuard, visit the [Pulumi CrossGuard documentation](https://www.pulumi.com/docs/guides/crossguard/).

* **[Infrastructure as code (IaC)](/what-is/what-is-infrastructure-as-code/)**: Start with Infrastructure as Code using Pulumi by accessing our [getting started guide](https://www.pulumi.com/docs/get-started/).

* **Version control**: Learn about version control systems supported by Pulumi in our [version control documentation](https://www.pulumi.com/docs/intro/concepts/state/#backends).

## Learn more

Pulumi offers a truly modern approach to implementing DevOps practices and infrastructure as code. With Pulumi, you can create, deploy, and manage infrastructure on any cloud using the programming languages and tools you already know. [Get started today](/docs/get-started/).
