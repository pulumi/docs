---
title: What is Continuous Integration/Continuous Delivery (CI/CD)?
meta_desc: |
    Learn about CI/CD practices that improve dev process with automation for effective, rapid software delivery.
type: what-is
page_title: "What is Continuous Integration/Continuous Delivery (CI/CD)?"
lastmod: 2026-05-12
about:
  name: CI/CD
  sameAs: https://en.wikipedia.org/wiki/CI/CD
keywords:
  - continuous integration
  - continuous delivery
  - ci/cd
  - devops
  - deployment pipeline
---

Continuous integration and continuous delivery (CI/CD) is a software development practice that automates the integration of code changes, testing, and release of new versions to production. CI/CD shortens release cycles, reduces bugs, and lets teams ship features more reliably and frequently.

## Key takeaways

- **CI/CD has two halves**: continuous integration automates code merging and testing; continuous delivery automates release readiness, with continuous deployment as the optional final step that pushes every passing change to production.
- **A CI/CD pipeline** is the automated path code travels from commit to production, typically running build, test, security scan, and deploy stages.
- **CI/CD is a foundational [DevOps](/what-is/what-is-devops/) practice** — it operationalizes the cultural goal of shipping fast and safely.
- **The biggest wins** come from automating the boring parts: builds, regression tests, environment provisioning, and rollbacks.
- **Infrastructure as code pairs naturally with CI/CD** because the same pipeline that ships application code can also ship infrastructure changes.

## What is continuous integration (CI)?

Continuous integration (CI) is a development practice where developers frequently merge tested code changes into a shared repository, often multiple times a day. Each merge triggers an automated build and test suite that catches integration problems early.

A test can be a simple code linter or a more complex process like checking for security vulnerabilities. Proper tests, including unit, integration, and regression tests, are standard in CI.

## What is continuous delivery (CD)?

In continuous delivery (CD), developers ensure that software is consistently maintained in a deployable state by automating various release process stages, including testing, deployment, and configuration. A release typically consists of a set of new features, improvements, bug fixes, or other changes that have been implemented since the previous release. Release creation may require bundling configuration files, binaries, and other artifacts such as certificates. The new release may be intended for end-user consumption, where it is deployed to production environments, or it may undergo user acceptance testing (UAT) before being released to a broader audience. CD facilitates the automation of these processes.

## What is continuous deployment?

Continuous deployment extends continuous delivery by automatically releasing every change that passes the pipeline straight to production. Continuous delivery keeps the codebase deployable; continuous deployment removes the manual approval step and ships it.

## What is a CI/CD pipeline?

A CI/CD pipeline is the deployable unit path for CI/CD — the sequence of automated stages that code travels from commit to production. A pipeline starts when code is committed to a repository like GitHub. The next step is a notification to a build system, such as [GitHub Actions](https://docs.github.com/en/actions). The build system compiles the code and runs unit tests. Integration tests are the next step if your code passes the unit tests. If your code passes both unit and integration tests, the images will be created and pushed into a registry service in the case of containers. This is the simplest example of a pipeline. You can do many more things, such as security scans, CVE checks (Common Vulnerabilities and Exploits), Slack notifications, and quality checks. A pipeline can be fully automated or have checkpoints that require approval before resuming.

## CI/CD terms and tools

The following terms provide a foundational understanding of the key concepts and practices in the field of CI/CD.

| Topic | Description | Tools |
|-------|-------------|-------|
| Build automation | The process of automating the creation of a software build and the associated processes including compiling computer source code into binary code, packaging binary code, and running automated tests. | [Docker](https://www.docker.com/), [GitHub Actions](https://github.com/features/actions) |
| Continuous deployment | An extension of continuous delivery, where every change that passes the automated tests is deployed to production automatically, without explicit approval from a developer, making the deployment process fully automated. | [Pulumi Deployments](/docs/platform/deployments/) |
| Continuous delivery (CD) | A software engineering approach in which teams produce software in short cycles, ensuring that the software can be reliably released at any time. It aims at building, testing, and releasing software with greater speed and frequency. | [Codefresh](https://codefresh.io/docs/docs/getting-started/cd-codefresh/), [AWS CodePipeline](https://aws.amazon.com/codepipeline/), [GitHub Actions](https://github.com/features/actions) |
| Continuous integration (CI) | A development practice where developers integrate code into a shared repository frequently, ideally several times a day. Each integration is verified by an automated build, allowing teams to detect problems early. | [Jenkins](https://www.jenkins.io/), [CircleCI](https://circleci.com/) |
| Continuous testing | The process of executing automated tests as part of the software delivery pipeline to obtain immediate feedback on the business risks associated with a software release candidate. | [Selenium](https://www.selenium.dev/), [Appium](https://appium.io/docs/en/2.2/) |
| Feature flagging | A technique that allows developers to turn certain functionalities on and off, typically used in a continuous delivery environment. | [LaunchDarkly](https://launchdarkly.com/), [FeatureToggle](https://featuretoggle.org/) |
| Test automation | Using special software to control the execution of tests and the comparison of actual outcomes with predicted outcomes. | [Selenium](https://www.selenium.dev/), [JUnit](https://junit.org/junit5/) |
| Version control systems (VCS) | Systems that record changes to a file or set of files over time so that you can recall specific versions later. | [Git](https://git-scm.com/), [Subversion](https://subversion.apache.org/) |

## Best practices for CI/CD pipelines

To build an effective CI/CD pipeline, platform and development teams must adopt and invest in DevOps best practices.

- **Use a single repository** - Maintain a centralized repository containing all the necessary files, scripts, source code, and resources for the build and deployment processes.
- **Adopt [trunk-based development](https://www.atlassian.com/continuous-delivery/continuous-integration/trunk-based-development)**  - Integrate code changes regularly into the main branch to avoid complex merges and ensure a continuous flow of minor, incremental updates.
- **Automate the build** - Automatically compile code to catch errors early and use tools to check and improve code standards.
- **Include comprehensive testing** - Implement automated testing at various levels (unit, integration, and end-to-end) to ensure code quality and functionality.  Integrate tools to identify and fix security vulnerabilities.
- **Deploy stable environments** - Automate setting up and deploying to different environments such as development, QA, pre-production, and production.
- **Perform routine deployments** - Deployments ought to be familiar enough for the team to execute them confidently at any time. Opting for frequent deployments with minimal changes reduces risks and allows straightforward rollback procedures when needed.
- **Provide team-wide visibility** - Integrate monitoring tools to receive real-time application performance feedback, helping you promptly identify and resolve issues.
An effective CI/CD pipeline automates and streamlines software development and delivery, ensuring rapid and reliable releases with high code quality.

For a detailed exploration and steps to implement CI/CD and DevOps practices, refer to the following Pulumi tools and resources:

- **Continuous integration and continuous delivery (CI/CD)**: For integrating CI/CD processes with Pulumi, visit our [CI/CD integration documentation](https://www.pulumi.com/docs/guides/continuous-delivery/).

- **Policy as code**: To manage policies using Pulumi Policies, visit the [Pulumi Policies documentation](https://www.pulumi.com/docs/insights/policy/).

- **[Infrastructure as code (IaC)](/what-is/what-is-infrastructure-as-code/)**: Start with Infrastructure as Code using Pulumi by accessing our [getting started guide](https://www.pulumi.com/docs/get-started/).

- **Version control**: Learn about version control systems supported by Pulumi in our [version control documentation](https://www.pulumi.com/docs/intro/concepts/state/#backends).

## Get started with CI/CD using Pulumi

1. **Define your infrastructure as code**:

   ```bash
   pulumi new aws-typescript
   ```

1. **Run `pulumi preview` on every PR** and `pulumi up` on merge — see Pulumi's [CI/CD integration guide](/docs/iac/using-pulumi/continuous-delivery/) for GitHub Actions, GitLab, CircleCI, Jenkins, and more.

1. **Promote stacks** (`pulumi stack select prod && pulumi up`) for environment-by-environment rollouts, with [policy checks](/docs/insights/policy/) at each gate.

## Learn more

Pulumi offers a truly modern approach to implementing DevOps practices and infrastructure as code. With Pulumi, you can create, deploy, and manage infrastructure on any cloud using the programming languages and tools you already know. [Get started today](/docs/get-started/).
