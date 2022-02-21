---
title: Infrastructure as Code for DevOps
meta_desc: |
     Discover how infrastructure as code for devops helps foster two important aspects of devops by enabling automation and building a true devops culture.

type: what-is
page_title: "Infrastructure as Code for DevOps"

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
---

DevOps isn’t any one thing. It’s a term that represents a blend of culture, tools and practices that aims to improve the software delivery life cycle (SDLC)  and to deliver your products (which may be an app for outside customers but might also be cloud infrastructure to internal developers) as quickly and reliably as possible. Two of the most important aspects of DevOps are automation and culture. [Infrastructure as Code]({{< relref "/what-is/what-is-infrastructure-as-code" >}}) (IaC) is a practice that’s fundamental to both.

## What is Infrastructure as Code for Devops?

First, let’s define IaC. IaC means that you use code to define and manage your infrastructure rather than manual processes. It is a common practice used in DevOps methodologies that can increase your team’s output while reducing errors. With IaC, your infrastructure becomes versionable, [testable]({{< relref "/what-is/how-to-step-up-cloud-infrastructure-testing" >}}), and repeatable. Infrastructure code can be packaged and shared both within the company and with the broader community. As published code, IaC also fosters collaboration because developers can offer solutions to problems and suggestions for improvements to existing code. Many IaC tools require you to use domain-specific languages, but tools with a modern approach to IaC allow you to use general purpose languages and apply [software engineering practices]({{< relref "/blog/what-exactly-is-cloud-engineering" >}}) to your infrastructure. Modern IaC was developed to be a more effective solution to managing cloud infrastructure, especially modern architectures that include containers, [Kubernetes]({{< relref "/blog/kubernetes-fundamentals-part-one" >}}), and [serverless]({{< relref "/blog/architecture-as-code-serverless" >}}).

## Automation and Infrastructure as Code for DevOps

The fundamental point of IaC is that you can, when resources are represented as code, build, deploy, and manage cloud infrastructure with some tool or platform that performs these tasks for you automatically. For many organizations, an IaC tool that uses a declarative approach works best. In a declarative approach, you define the desired state of the system, including what resources you need and any properties they should have, and the IaC tool will figure out how to make that desired state happen.  If you make changes to the desired state, a declarative IaC tool will apply those changes for you.

With a modern approach to using infrastructure as code for DevOps, you can apply many of the same software engineering best practices used in application development to your infrastructure. Examples of [IaC automation]({{< relref "/blog/automation-api-supercharged-cloud-tooling" >}}) include:

- **Version control.** IaC source files can be stored in a version control system. That means you have a history of when changes were made and what they were. You always know what happened. If there’s a problem, you can roll back to a previous version until the problem’s fixed.
- **Automated CI/CD.** With IaC, you can use an automated CI/CD pipeline that’s tied to the version control system. You can set the pipeline up to kick off whenever you want, such as when someone makes a change. That automated pipeline can apply a wide range of tests, signal designated stakeholders to review the code, and deploy safe, tested code. If you’re using modern IaC, you could use the same CI/CD pipeline for your infrastructure and application code.

Applying those standards has many benefits:

- **Safe, stable infrastructure.** As we mentioned above, with IaC you can incorporate [all sorts of tests]({{< relref "/blog/testing-in-practice" >}}) such as security tests. This means you can involve interested stakeholders, such as a security team in the deployment process. DevOps is all about “shifting left,” which means testing and finding problems early in the development process, when they’re easy to fix. Modern approaches to IaC provide even more benefits than others: you can run standard unit tests, integration tests, and security tests.
- **Faster time to market.** Automation speeds up the entire deployment process. You’ll get new features to market (or in terms of infrastructure, get new resources set up) much faster if you let go of manual, error-prone processes.

## Culture and Infrastructure as Code for DevOps

There’s a big cultural component to DevOps. It’s not only about automated testing and continuous deployments. DevOps culture is about a shared understanding between developers and operations, and sharing responsibility for the software they build. What does IaC have to do with culture? It gives easy access to infrastructure data. The state of the infrastructure is represented in source files that anyone can read. IaC gives stakeholders a common language in which to talk about the infrastructure in terms everyone can understand. A common language means you can start breaking down silos (the bane of DevOps practitioners) and broaden the base of participants. Using infrastructure as code for DevOps allows this shared culture to grow.

### Reuse

IaC also makes reuse of components possible and is another way to share information. Reusability means you build higher-level components out of individual cloud resources. These components can be written with your company’s best practices built in, automatically tested, and shared within the company and with the community.

## Summary

IaC is fundamental to DevOps. IaC fosters automation and a DevOps culture. If you want to increase your rate of innovation and [decrease your time to market]({{< relref "/case-studies/snowflake" >}}), infrastructure as code for DevOps is the key.

## Pulumi

Pulumi's Cloud Engineering Platform unites infrastructure teams, application developers, and compliance teams around a unified software engineering process for delivering modern cloud applications faster and speeding innovation. Pulumi’s open-source tools help infrastructure teams tame the cloud’s complexity using the world’s most popular programming languages. [Get started for free today]({{< relref "/docs/get-started" >}}), or check out an [on-demand workshop]({{< relref "/resources/introduction-to-pulumi" >}}) for getting started with IaC.
