---
title: "Introducing Pulumi ESC Projects and Environment Tags"
allow_long_title: true
date: 2024-09-12T13:00:00-04:00
draft: false
meta_desc: "ESC Projects and Environment Tags allow you to organize your environments
  and collaborate effectively."
meta_image: "meta.png"
authors:
  - derek-schaller
  - arun-loganathan
tags:
  - esc
  - secrets
  - features
search:
  keywords:
    - esc
    - environments
    - tags
    - projects
    - environment
    - introducing
    - organize
---

We're thrilled to unveil two new features that will empower you to organize your collection of [Pulumi ESC](/docs/esc/) Environments: <b>Projects</b> and <b>Environment Tags</b>.  Projects offer a structured way to group related environments and Environment Tags allow you to add contextual information to each environment. Together, they offer a powerful way for you to manage, navigate, and collaborate on your secrets and configurations.

<!--more-->

## Overview of Pulumi ESC 

Pulumi ESC is a developer-first platform designed to simplify the management of secrets and configurations into collections called <i>[environments](/docs/esc/environments/)</i>. As a fully managed solution, it offers [dynamic cloud provider credential](/docs/esc/get-started/esc-run-command/) resolution, a rich set of [providers](/docs/esc/providers/) to retrieve secrets from external platforms, and the ability to use the secrets and configurations you have defined across any surface, including your applications and infrastructure via [Multi-language SDKs](/docs/esc/sdk/), [REST APIs](/docs/pulumi-cloud/cloud-rest-api/#environments), [CLI](/docs/esc-cli/), [Pulumi-Service Provider](/registry/packages/pulumiservice/api-docs/environment/), and [Automation API](/blog/esc-automation-api-pulumi-service-provider-launch/#streamline-automated-workflows-with-automation-api-enhancements). Like all Pulumi functionality, Pulumi ESC focuses on enhancing both agility and security in modern cloud development.

As developers have embraced Pulumi ESC to manage their collections of secrets and configurations across many teams and projects, the demand for more sophisticated organizational tools has increased. To address this growing need for more organized and efficient management of cloud environments, we are introducing Projects and Environment Tags in Pulumi ESC.

## Introducing Projects

Projects offer a structured way to organize environments into logical groupings. Each Project has a distinct name, providing context for the environments within it, and can contain multiple environments with variations, each having a specific purpose. Additionally, Projects help large organizations simplify environment management by mitigating possible environment name conflicts and ensuring changes are made in isolation to the correct environments.

For example, your organization could have a project named "payments-app" containing `dev`, `staging`, and `prod` environments within it. Your organization could also have a project called "dev-credentials" which contains different environments used to provide temporary runtime access to credentials for developers while working. 

We have two additional features as part of this launch: 
- **Grouping and Search**: You can group environments by either Project name or by Environment Tags, as well as search by them, making it simple to locate and manage your environments.
- **Environment Clone**: Using the built-in cloning functionality, you can securely copy environments with sensitive information, preserving either the entire version history or just the latest environment state, depending on your needs.

{{% notes "info" %}}
To use Projects and Environment Tags, please update your [ESC CLI](/docs/esc-cli/) or [Pulumi CLI](/docs/cli/) and [SDK](/docs/esc/sdk/) to the latest. 
{{% /notes %}}

{{% notes "info" %}}
Environments will now need to be referenced by specifying the project as part of the environment identifier. Any existing environments within your organization will be available in the `default` project. Projects are fully backward compatible - all your existing programs, imports and CLI commands will work without requiring any changes at the moment. Note that only environments within the `default` project will be backwards compatibly and resolve without a project prefix.

Users will be able to create new environments in the default project until <b>Nov 30, 2024</b>. Starting Dec 1, 2024, users will not be able to create new environments in the default project. 

Starting <b>Apr 1, 2025</b>, users will not be able to edit their environments within the ‘default’ Project. We recommend customers migrate their existing environments to user-created projects at the earliest to take advantage of new Pulumi ESC capabilities.

Moving environments out of the `default` project is as easy as cloning the environment into a new project and updating any references to it. An example clone command that preserves all environment history, tags, and team access looks as follows

```bash
  $ esc env clone default/dev your-project/dev --preserve-history --preserve-env-tags --preserve-rev-tags --preserve-access
```
{{% /notes %}}

We offer numerous ways for you to get started with Projects via the Pulumi Web Console, [SDK](/docs/esc/sdk/), [REST API](/docs/pulumi-cloud/cloud-rest-api/#environments), [CLI](/docs/esc-cli/) and [Pulumi-Service Provider](/registry/packages/pulumiservice/api-docs/environment/) - choose what best fits your workflow. Here is one example using the ESC CLI to create and list environments within a project: 

 ```bash
  $ esc env init cloud-pe/demo
  Environment created: dschaller/cloud-pe/demo

  $ esc env ls -p cloud-pe
  cloud-pe/demo
  pulumi/cloud-pe/demo
 ```

### Breaking Changes

With the introduction of Projects, all existing environments part of the `default` project will continue to work without requiring any changes. However, when moving existing environments out of the default project you may notice some differences that we have outlined below.

* If your environment was interpolating the `context.currentEnvironment.name` or `context.rootEnvironment.name` from [Contextual information](/docs/esc/environments/#pulumi-contextual-information), this value will now include the project for any environments outside of the `default` project.
* If you were using any of the [secrets providers with OIDC](/docs/esc/environments/#using-secrets-providers-and-oidc), you will need to update both the subject and audience if a trust relationship has been set up. The subject will be either `pulumi:environments:org:<organization name>:env:<project name>/<environment name>` if no `subjectAttributes` are specified or if the `currentEnvironment.name` subject attribute is specified it will now resolve to `currentEnvironment.name:<project name>/<environment name>`. The audience will be the provider's platform name (`aws`, `azure`, or `gcp`) followed by the org name of the environment (e.g. `aws:pulumi`).

## Introducing Environment Tags
Using Environment Tags, teams can now assign any number of custom tags to each environment within Pulumi ESC. These tags serve as contextual identifiers that can streamline workflows by enabling you to group and search across environments based on specific criteria such as teams, project stages, deployment environments, compliance requirements, or geographic locations. This multi-dimensional approach provides unparalleled flexibility and control, ensuring your Pulumi ESC environments can scale seamlessly with your organizations evolving needs.

For example, suppose your organization has multiple environments across different geographic regions. You can use Environment Tags like 'region: us-east' or 'region: eu-central-1' to quickly filter environments by region. Similarly, for security audits, you might tag environments with ‘Compliance: SOC2’ or ‘Compliance: GDPR’ to easily find relevant environments and ensure they are compliant. 

You can use the Pulumi Web Console and the [CLI](/docs/esc-cli/) to create and manage Environment Tags. Here is an example of using the CLI to add and list Environment Tags.

```bash
$ esc env tag cloud-pe/demo region us-east-1
Name: region
Value: us-east-1
Last updated at 2024-09-10 11:03:05.708 -0700 PDT by Derek <dschaller>

$ esc env tag ls cloud-pe/demo
Name: region
Value: us-east-1
Last updated at 2024-09-10 11:03:05.708 -0700 PDT by Derek <dschaller>
```

## Conclusion
Pulumi ESC Projects and Environment Tags are powerful additions that bring order and clarity to your secrets and configuration to even the most complex infrastructure landscapes. By enabling you to organize, group, and search for your environments with ease, we're empowering you to scale your infrastructure with high confidence and flexibility.  

We're excited to see how you leverage these new capabilities. Check out the docs to learn more about Pulumi ESC Projects and Environment Tags and start organizing your environments today!

As always, please share your [feedback](https://github.com/pulumi/esc/issues/new/choose) on how we can further improve Pulumi ESC to suit your needs.
