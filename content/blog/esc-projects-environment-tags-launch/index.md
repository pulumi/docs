---
title: "Introducing Pulumi ESC Projects and Environment Tags"
allow_long_title: true
date: 2024-09-11T00:00:00-04:00
draft: false
meta_desc: "ESC Projects and Environment Tags allow you to organize your environments and collaborate effectively. "
meta_image: "meta.png"
authors:
  - arun-loganathan
tags:
  - esc
  - secrets
  - features
---

We're thrilled to unveil two new features that will empower you to organize your collection of [Pulumi ESC](https://www.pulumi.com/docs/esc/) Environments: <b>Projects</b> and <b>Environment Tags</b>.  Projects offer a structured way to group related environments into a project path and Environment tags allow you to add more contextual information. Together, they offer a powerful way for you to manage, navigate, and collaborate on your secrets and configurations.

<!--more-->

## Overview of Pulumi ESC 

Pulumi ESC is a developer-first platform designed to simplify the management of secrets and configurations across your cloud environments. As a fully managed solution, it offers dynamic cloud provider credential generation, a rich set of providers to retrieve secrets from other platforms, and the ability to use the secrets and configurations you have defined across any surface including your applications and infrastructure via Multi-language SDKs, REST API, CLI, Pulumi-Service Provider, and Automation API. Like all Pulumi functionality, ESC’s versioning feature adopts a software engineering approach: you can tag versions and pin a version to imports, enhancing both agility and security in modern cloud development. 

As developers have embraced Pulumi ESC to manage their collections of secrets and configurations across many teams and projects, the demand for more sophisticated organizational tools has increased. To address this growing need for more organized and efficient management of cloud environments, we are introducing Projects and Environment Tags in Pulumi ESC.

## Introducing Projects

Projects offer a structured way to organize environments into logical groupings. Each Project has a distinct name that provides context for the environments it contains. Within each project, you can have multiple environments with variations, each with a specific purpose. Projects help teams avoid environment name conflicts and ensure that changes are made to the correct environments without affecting others.

For example, you could create a project called "Payments-app" and have `dev`, `staging`, and `prod` environments within it or you could have a project called "dev-credentials" that contains different environments providing temporary runtime access to credentials for developers for various scenarios. 

We have two additional features as part of this launch: 
- **Group and Search**: You can group the environments by Project Name or by Environment Tags, as well as search by them, making it simple to locate and manage your environments.
- **Environment Clone**: Using the built-in cloning functionality, you can securely copy environments with sensitive information, preserving either the entire version history or just the latest environment state, depending on your needs.

{{% notes "info" %}}
Environments will now need to be referenced by specifying the project path. All existing environments within your organization will be available in the `default` project. Projects are fully backward compatible - all your existing programs, imports and CLI commands will work without requiring any changes. Project name is not required in the path when referencing environment names within the `default` project. 

Users will be able to create new environments in the default project until <b>Nov 30, 2024</b>. Starting Dec 1, 2024, users will not be able to create new environments in the default project. 

Starting <b>Apr 1, 2025</b>, users will not be able to edit their environments within the ‘default’ Project. We recommend customers migrate their existing environments to named projects at the earliest to take advantage of new ESC capabilities. 

{{% /notes %}}

We offer numerous ways for you to get started and use Projects. You can use Pulumi Web Console, ESC CLI, SDK, Pulumi-service provider, and our REST API - choose what best fits your workflow. Here are the CLI commands: 

### CLI

 ```bash
   **(To-be-added)**
   ```


## Introducing Environment Tags
Using Environment Tags, teams can now assign multiple customizable tags to each environment within Pulumi ESC. These tags serve as contextual identifiers that can streamline workflows by enabling you to group and search environments based on specific criteria such as teams, project stages, deployment environments, compliance requirements, or geographic locations. This multi-dimensional approach provides unparalleled flexibility and control, ensuring your ESC environment organization scales seamlessly with your evolving needs.

For example, suppose your organization has multiple environments across different geographic regions. You can use Environment Tags like 'region: us-east' or 'region: eu-central-1' to quickly filter environments by region. Similarly, for security audits, you might tag environments with ‘Compliance: SOC2’ or ‘Compliance: GDPR’ to easily find relevant environments and ensure they are compliant. 

You can use Pulumi Web Console and the ESC CLI to create and manage environment tags. Here are the CLI commands

```bash
   **(To-be-added)**
   ```

## Demo

Here is a quick demo of how you can use all the features we’re releasing today within Pulumi Cloud Console: 

**(To-be-added)**

## Conclusion
Pulumi ESC Projects and Environment Tags are powerful additions that bring order and clarity to your secrets and configuration to even the most complex infrastructure landscapes. By enabling you to organize, group, and search for your environments with ease, we're empowering you to scale your infrastructure with high confidence and flexibility.  

We're excited to see how you leverage these new capabilities. Check out the docs to learn more about Pulumi ESC Projects and Environment Tags and start organizing your environments today!


