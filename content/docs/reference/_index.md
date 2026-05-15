---
title: Reference
docs_home: true
notitle: true
norightnav: true
menu:
  reference:
    identifier: reference-home
    weight: 1
meta_desc: Complete reference documentation for Pulumi CLI, Cloud REST API, language SDKs, and configuration syntax.
meta_image: /images/docs/meta-images/docs-meta.png
h1: Reference Documentation
description: <p>Reference documentation for Pulumi command-line tools, REST APIs, language SDKs, and configuration syntax.</p>
aliases:
  - /docs/reference/

sections:
- type: button-cards
  heading: Command-line tools
  cards:
  - icon: pulumi-iac
    heading: Pulumi CLI
    description: Command reference for the Pulumi infrastructure as code CLI.
    link: /docs/iac/cli/

  - icon: pulumi-secrets
    heading: ESC CLI
    description: Command reference for the Pulumi ESC secrets and configuration CLI.
    link: /docs/esc/cli/

- type: button-cards
  heading: Language SDKs
  cards:
  - image: /logos/tech/typescript.svg
    heading: TypeScript (Node.js) ↗
    description: API reference for the Node.js SDK with TypeScript and JavaScript.
    link: /docs/reference/pkg/nodejs/pulumi/pulumi/

  - image: /logos/tech/python.svg
    heading: Python ↗
    description: API reference for the Python SDK.
    link: /docs/reference/pkg/python/pulumi/

  - image: /logos/tech/go.svg
    heading: Go ↗
    description: API reference for the Go SDK.
    link: https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi

  - image: /logos/tech/dotnet.svg
    heading: .NET (C#, F#, VB) ↗
    description: API reference for the .NET SDK.
    link: /docs/reference/pkg/dotnet/pulumi/pulumi.html

  - image: /logos/tech/java.svg
    heading: Java ↗
    description: API reference for the Java SDK.
    link: /docs/reference/pkg/java/

  - image: /logos/tech/yaml.svg
    heading: YAML
    description: Reference for writing Pulumi programs in YAML.
    link: /docs/iac/languages-sdks/yaml/

- type: button-cards
  heading: Policy SDKs
  cards:
  - icon: shield-check
    heading: TypeScript Policy SDK ↗
    description: API reference for writing policies in TypeScript.
    link: /docs/reference/pkg/nodejs/pulumi/policy/

  - icon: shield-check
    heading: Python Policy SDK ↗
    description: API reference for writing policies in Python.
    link: /docs/reference/pkg/python/pulumi_policy/

- type: button-cards
  heading: ESC SDKs
  cards:
  - image: /logos/tech/typescript.svg
    heading: TypeScript ESC SDK ↗
    description: API reference for automating Pulumi ESC from Node.js with TypeScript or JavaScript.
    link: /docs/reference/pkg/nodejs/pulumi/esc-sdk/

  - image: /logos/tech/python.svg
    heading: Python ESC SDK ↗
    description: API reference for automating Pulumi ESC from Python.
    link: /docs/reference/pkg/python/pulumi_esc_sdk/

  - image: /logos/tech/go.svg
    heading: Go ESC SDK ↗
    description: API reference for automating Pulumi ESC from Go.
    link: https://pkg.go.dev/github.com/pulumi/esc-sdk/sdk/go

  - image: /logos/tech/dotnet.svg
    heading: .NET ESC SDK ↗
    description: API reference for automating Pulumi ESC from .NET.
    link: /docs/reference/pkg/dotnet/esc-sdk/pulumi.esc.sdk/pulumi.esc.sdk.html

- type: button-cards
  heading: APIs & Configuration
  cards:
  - icon: plug
    heading: Pulumi Cloud REST API
    description: Programmatic access to Pulumi Cloud for automation and integrations.
    link: /docs/reference/cloud-rest-api/

  - icon: gear
    heading: ESC Environment Syntax
    description: Reference for ESC environment definitions, interpolations, functions, and providers.
    link: /docs/esc/environments/syntax/

  - icon: link
    heading: Property Paths
    description: Reference for property path syntax used in resource options, ESC, and Insights.
    link: /docs/reference/property-paths/

- type: button-cards
  heading: Packages & Providers
  cards:
  - icon: package
    heading: Package Registry
    description: Browse packages for AWS, Azure, Google Cloud, Kubernetes, and 120+ providers.
    link: /registry/

- type: flat
  heading: Have questions?
  description: <p>For questions or feedback, reach out on <a href="https://slack.pulumi.com" target="_blank">community Slack</a>, <a href="https://github.com/pulumi" target="_blank">GitHub</a>, or <a href="/support/">contact support</a>.</p>
---
