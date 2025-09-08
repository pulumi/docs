---
title: Developer Tools
linktitle: Developer Tools
capability: developer-tools
docs_home: true
notitle: true
menu:
    developer-tools:
        identifier: developer-tools-home
        weight: 1
expanded_menu_ids:
    - developer-tools-cli
    - developer-tools-sdks
meta_desc: Technical interfaces and tools for developers. CLIs, SDKs, APIs, and AI-powered development assistance for infrastructure as code.
meta_image: /images/docs/meta-images/docs-meta.png
h1: <strong>Developer Tools</strong> and Interfaces
description: <p>Technical tools and interfaces for developers - command-line tools, programming language SDKs, REST APIs, and AI-powered development assistance.</p>
link_buttons:
  primary:
    label: Install CLI
    link: /docs/iac/download-install/
  secondary:
    label: Try Pulumi AI
    link: /ai/

sections:
- type: full-width-cards
  heading: Core Developer Tools
  cards:
  - icon: 💻
    heading: Command Line Interface
    description: Powerful CLI for managing infrastructure deployments, configurations, and cloud resources.
    link: /docs/iac/cli/
  - icon: 🔧
    heading: Language SDKs
    description: Native SDKs for TypeScript, Python, Go, .NET, Java, and YAML with full IDE support.
    link: /docs/iac/languages-sdks/
  - icon: 🔌
    heading: REST APIs
    description: Programmatic access to Pulumi Cloud services for custom integrations and automation.
    link: /docs/pulumi-cloud/cloud-rest-api/
  - icon: 🤖
    heading: Pulumi AI
    description: AI-powered infrastructure generation, optimization, and intelligent assistance.
    link: /ai/
- type: cards-logo-label-link
  heading: Programming Languages
  description: Build infrastructure using your favorite programming language.
  cards:
  - label: TypeScript
    icon: icon-32-32 node-color-32-32
    link: /docs/iac/languages-sdks/javascript/
  - label: Python
    icon: icon-32-32 python-color-32-32
    link: /docs/iac/languages-sdks/python/
  - label: Go
    icon: icon-32-32 go-color-32-32
    link: /docs/iac/languages-sdks/go/
  - label: .NET
    icon: icon-32-32 dotnet-color-32-32
    link: /docs/iac/languages-sdks/dotnet/
  - label: Java
    icon: icon-32-32 java-color-32-32
    link: /docs/iac/languages-sdks/java/
  - label: YAML
    icon: icon-32-32 yaml-color-32-32
    link: /docs/iac/languages-sdks/yaml/
- type: button-cards
  heading: Development Environment
  description: Tools and integrations for your development workflow.
  cards:
  - heading: IDE Extensions
    description: "Rich IDE support with IntelliSense, syntax highlighting, and debugging for VS Code, IntelliJ, and more."
    link: /docs/iac/languages-sdks/
    primary_button_label: Get Extensions
    primary_button_link: /docs/iac/languages-sdks/
  - heading: Automation API
    description: "Embed Pulumi directly in your applications with programmatic infrastructure deployment and management."
    link: /docs/iac/automation-api/
    primary_button_label: Learn More
    primary_button_link: /docs/iac/automation-api/
  - heading: Testing Framework
    description: "Unit test and integration test your infrastructure code with familiar testing tools and patterns."
    link: /docs/iac/using-pulumi/testing/
    primary_button_label: Start Testing
    primary_button_link: /docs/iac/using-pulumi/testing/
- type: full-width-cards
  heading: Command Line Tools
  cards:
  - icon: pulumi-blue-21-21
    heading: Pulumi CLI
    description: Deploy, manage, and operate cloud infrastructure with the main Pulumi command-line tool.
    link: /docs/iac/cli/
  - icon: esc-blue-21-21
    heading: ESC CLI
    description: Manage environments, secrets, and configuration with the dedicated ESC command-line tool.
    link: /docs/esc/cli/
  - icon: convert-blue-21-21
    heading: Conversion Tools
    description: Migrate from Terraform, CloudFormation, Kubernetes YAML, and other formats to Pulumi.
    link: /docs/iac/adopting-pulumi/migrating-to-pulumi/
  - icon: ai-blue-21-21
    heading: AI-Powered Generation
    description: Generate infrastructure code from natural language descriptions using Pulumi AI.
    link: /ai/
- type: full-width-cards
  heading: Integration & Automation
  cards:
  - icon: webhook-blue-21-21
    heading: Webhooks
    description: Integrate with external systems through webhooks for deployment notifications and triggers.
    link: /docs/pulumi-cloud/webhooks/
  - icon: workflow-blue-21-21
    heading: CI/CD Integration
    description: Seamless integration with GitHub Actions, GitLab CI, Azure DevOps, and other CI/CD systems.
    link: /docs/iac/using-pulumi/continuous-delivery/
  - icon: script-blue-21-21
    heading: Scripting & Automation
    description: Automate infrastructure operations with scripts, policies, and custom workflows.
    link: /docs/iac/automation-api/
  - icon: debug-blue-21-21
    heading: Debugging & Troubleshooting
    description: Tools and techniques for debugging infrastructure deployments and resolving issues.
    link: /docs/iac/support/troubleshooting/
- type: flat
  heading: Ready to start developing?
  description: <p><a href="/docs/iac/download-install/">Install the CLI</a>, explore the <a href="/docs/iac/languages-sdks/">SDKs</a>, or try <a href="/ai/">Pulumi AI</a>. Check out our <a href="/docs/iac/get-started/">getting started guide</a> and join us on <a href="https://slack.pulumi.com" target="_blank">Slack</a> for support.</p>
---